# File: modules/deblurgan.py

import torch
import torch.nn as nn
import torch.nn.functional as F

class ResBlock(nn.Module):
    def __init__(self, channels):
        super(ResBlock, self).__init__()
        self.block = nn.Sequential(
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.InstanceNorm2d(channels, affine=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels, channels, 3, padding=1),
            nn.InstanceNorm2d(channels, affine=True)
        )

    def forward(self, x):
        return x + self.block(x)

class DeblurGANv2(nn.Module):
    def __init__(self):
        super(DeblurGANv2, self).__init__()

        # Encoder
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=1, padding=3)
        self.in1 = nn.InstanceNorm2d(64, affine=True)
        self.relu = nn.ReLU(inplace=True)

        # Downsample
        self.down1 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.in2 = nn.InstanceNorm2d(128, affine=True)
        self.down2 = nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)
        self.in3 = nn.InstanceNorm2d(256, affine=True)

        # Residual blocks
        self.res_blocks = nn.Sequential(*[ResBlock(256) for _ in range(6)])

        # Upsample
        self.up1 = nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.in4 = nn.InstanceNorm2d(128, affine=True)
        self.up2 = nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.in5 = nn.InstanceNorm2d(64, affine=True)

        # Output layer
        self.out_layer = nn.Conv2d(64, 3, kernel_size=7, stride=1, padding=3)

    def forward(self, x):
        x = self.relu(self.in1(self.conv1(x)))
        x = self.relu(self.in2(self.down1(x)))
        x = self.relu(self.in3(self.down2(x)))
        x = self.res_blocks(x)
        x = self.relu(self.in4(self.up1(x)))
        x = self.relu(self.in5(self.up2(x)))
        x = torch.tanh(self.out_layer(x))
        return x

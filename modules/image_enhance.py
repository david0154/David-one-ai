# File: modules/image_enhance.py

from PIL import Image
import numpy as np
import torch
import os
import cv2

from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# Load Real-ESRGAN model (RRDBNet)
def load_enhancer():
    model_path = "models/image_enhance/RealESRGAN_x4plus.pth"
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64,
                    num_block=23, num_grow_ch=32, scale=4)

    upsampler = RealESRGANer(
        scale=4,
        model_path=model_path,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=not torch.cuda.is_available()
    )
    return upsampler

enhancer = load_enhancer()

def enhance_image(image: Image.Image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    output, _ = enhancer.enhance(img, outscale=1)
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    return Image.fromarray(output)

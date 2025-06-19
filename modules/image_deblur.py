# File: modules/image_deblur.py

import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import os

from modules.deblurgan import DeblurGANv2

# Load DeblurGANv2 pretrained model
def load_deblurgan_model():
    model_path = "models/image_deblur/deblurganv2.pth"
    model = DeblurGANv2()
    state_dict = torch.load(model_path, map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model

deblurgan_model = load_deblurgan_model()

transform = transforms.Compose([
    transforms.ToTensor(),
])

def deblur_image(image: Image.Image):
    input_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = deblurgan_model(input_tensor)[0]
    output_image = transforms.ToPILImage()(output.clamp(0, 1))
    return output_image

# File: modules/image_edit.py

from transformers import SegformerFeatureExtractor, SegformerForSemanticSegmentation
from PIL import Image
import torch
import numpy as np

# Load SegFormer model (e.g., for background removal, segmentation-based edits)
feature_extractor = SegformerFeatureExtractor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
seg_model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

def edit_image(image: Image.Image, instruction: str):
    # Basic example: background removal
    if "remove background" in instruction.lower():
        return remove_background(image)
    else:
        return image

def remove_background(image: Image.Image):
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = seg_model(**inputs)
    logits = outputs.logits
    upsampled_logits = torch.nn.functional.interpolate(logits, size=image.size[::-1], mode="bilinear", align_corners=False)
    seg = upsampled_logits.argmax(dim=1)[0].numpy()

    # Create mask (person class = 12 for ADE20K)
    mask = (seg == 12).astype(np.uint8) * 255

    # Convert to PIL and apply mask
    image_np = np.array(image.convert("RGBA"))
    image_np[..., 3] = mask  # set alpha channel
    return Image.fromarray(image_np)

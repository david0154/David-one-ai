# File: modules/brain.py
from modules.image_edit import edit_image
from modules.image_enhance import enhance_image
from modules.image_deblur import deblur_image
from modules.translator import translate, detect_lang
from transformers import pipeline
import torch

class Brain:
    def __init__(self):
        print("🧠 Loading conversation + code AI...")
        self.chat_pipeline = pipeline("text-generation", 
                                      model="TheBloke/deepseek-coder-1.3b-GGUF",
                                      device=0 if torch.cuda.is_available() else -1)

    def process_text(self, input_text):
        lang = detect_lang(input_text)
        print(f"🌍 Detected Language: {lang}")
        text_en = translate(input_text, to_lang="en")

        # Process through the chat AI
        result = self.chat_pipeline(text_en, max_new_tokens=200)[0]["generated_text"]
        result_clean = result[len(text_en):].strip()

        # Translate back to original language
        response_final = translate(result_clean, to_lang=lang)
        return response_final

    def process_code(self, instruction):
        # Just reroute to the same chat model
        return self.process_text(instruction)

    def process_image_edit(self, image, instruction):
        return edit_image(image, instruction)

    def process_image_enhance(self, image):
        return enhance_image(image)

    def process_image_deblur(self, image):
        return deblur_image(image)

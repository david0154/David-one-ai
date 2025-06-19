# File: modules/translator.py

from langdetect import detect
from googletrans import Translator

translator = Translator()

def detect_lang(text: str) -> str:
    try:
        lang = detect(text)
        return lang
    except:
        return "en"

def translate(text: str, to_lang: str = "en") -> str:
    try:
        translated = translator.translate(text, dest=to_lang)
        return translated.text
    except:
        return text

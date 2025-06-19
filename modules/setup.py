# File: modules/setup.py
import os
import subprocess

def setup_environment():
    print("🧠 Checking model requirements...")

    os.makedirs("models", exist_ok=True)

    models = {
        "text_model": "TheBloke/deepseek-coder-1.3b-GGUF",
        "image_enhance": "xinntao/Real-ESRGAN",
        "image_deblur": "naberu/deblurgan-v2",
        "image_edit": "tencent-ailab/segformer",
        "voice_stt": "openai/whisper-small",
        "voice_tts": "coqui/XTTS-v2"
    }

    for key, model in models.items():
        model_path = f"models/{key.replace('/', '_')}"
        if not os.path.exists(model_path):
            print(f"⬇️ Downloading: {model}")
            subprocess.run(["huggingface-cli", "snapshot-download", model, "--local-dir", model_path])
        else:
            print(f"✅ {key} already downloaded.")

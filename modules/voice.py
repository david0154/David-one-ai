# File: modules/voice.py
import sounddevice as sd
import numpy as np
import whisper
from TTS.api import TTS
import tempfile
import threading
import os
import time
import soundfile as sf
import speech_recognition as sr

# Load Whisper model
whisper_model = whisper.load_model("small", download_root="models/voice_stt")

# Load Coqui XTTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", 
          progress_bar=False, 
          gpu=True if TTS().is_cuda_available() else False)

def record_audio(duration=5, fs=16000):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(recording)

def recognize_speech(audio_np):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        sf.write(f.name, audio_np, 16000)
        result = whisper_model.transcribe(f.name)
        return result["text"]

def speak_text(text, language="en"):
    print("🔊 Speaking...")
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    tts.tts_to_file(text=text, speaker_wav=None, language=language, file_path=output_path)
    os.system(f"start {output_path}" if os.name == "nt" else f"aplay {output_path}")

# Background loop
def voice_loop(brain):
    while True:
        try:
            audio = record_audio()
            user_text = recognize_speech(audio)
            if user_text.strip() == "":
                continue
            print(f"🗣️ You said: {user_text}")
            response = brain.process_text(user_text)
            print(f"🤖 David One AI: {response}")
            lang_code = detect_lang(user_text)
            speak_text(response, language=lang_code)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"[Voice Error] {e}")
            time.sleep(1)

def init_voice(brain):
    threading.Thread(target=voice_loop, args=(brain,), daemon=True).start()

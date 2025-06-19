
<p align="center">
  <img src="logo.png" alt="David One AI Logo" width="200"/>
</p>

# 🤖 David One AI – Offline Full‑Stack Multilingual AI

**Author:** David  
**Email:** davidk76011@gmail.com  
**Runs via:** `main.aya` (using the [Arya Framework](https://github.com/david0154/Arya))  
**License:** MIT  

---

## 📥 Download

Get the full project (code, models, logo, everything included) here:  
**[Download David One AI – Complete Package (ZIP)](https://example.com/david_one_ai.zip)**  
*(Link placeholder – replace with your actual hosting URL, e.g., GitHub Releases)*

---

## 🧠 What Is David One AI?

**David One AI** is a fully offline AI assistant that:

- 💬 Holds smart multilingual conversations
- 💻 Helps generate or debug code
- 🖼️ Edits, enhances, and deblurs images
- 🗣️ Speaks and listens in **9+ languages**
- 🧠 Runs **100% locally** after initial setup

---

## ⚙️ Arya Framework Installation

This project uses the [Arya Framework](https://github.com/david0154/Arya). Follow these steps to get it working:

1. Clone Arya:
   ```bash
   git clone https://github.com/david0154/Arya.git
   cd Arya
   pip install -r requirements.txt
   python setup.py install
   ```
2. Ensure `.aya` files run correctly:
   ```bash
   aria run main.aya
   ```
3. Back in the `David-one-ai/` directory, simply run:
   ```bash
   python main.aya
   ```

---

## 🌍 Language Support

Understands & speaks:

🇬🇧 English • 🇮🇳 Hindi • 🇧🇩 Bengali • 🇱🇰 Tamil • 🇮🇳 Marathi • 🇮🇳 Punjabi • 🇵🇰 Urdu • 🇮🇳 Telugu • 🇮🇳 Assamese

---

## 📦 Key Features

| Type        | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| 💬 Chat     | Multilingual chat with intelligent replies                                  |
| 💻 Coding   | Generate code or debug scripts in many languages                            |
| 🖼️ Edit     | Background removal, masking using SegFormer                                 |
| ✨ Enhance  | Upscale and clarify images with Real‑ESRGAN                                  |
| 🔍 Deblur   | Remove motion blur using DeblurGANv2                                        |
| 🗣️ Voice    | Real-time STT + TTS via Whisper & Coqui XTTS                                |
| 🧠 Offline  | Fully self-contained, no internet needed post-download                      |

---

## 📁 Project Structure

```
David‑one‑ai/
│
├── main.aya                 # Launcher script via Arya
├── requirements.txt         # All Python dependencies
├── logo.png                 # David One AI logo image
├── README.md
└── modules/
    ├── setup.py             # Downloads all models (chat, voice, image)
    ├── brain.py             # Core intelligence engine
    ├── ui.py                # Gradio-based UI
    ├── voice.py             # STT & TTS logic
    ├── image_edit.py        # Image background removal/masking
    ├── image_enhance.py     # Real‑ESRGAN upscaling
    ├── image_deblur.py      # DeblurGANv2 module
    ├── deblurgan.py         # DeblurGANv2 neural network code
    └── translator.py        # Multilingual detect/translate functions
```

---

## 🛠️ How to Run

1. Download and unzip the complete package (including `logo.png`).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Arya framework is installed and `aria` is available:
   ```bash
   aria --help
   ```
4. Launch the AI:
   ```bash
   python main.aya
   ```

On first run, the system downloads all pretrained models:

- Chat (Deepseek‑Coder)
- STT (Whisper)
- TTS (Coqui XTTS)
- Image tools: SegFormer, Real‑ESRGAN, DeblurGANv2

---

## 📜 License

Released under the **MIT License**. Feel free to modify and distribute!

---

## 📧 Contact

Questions, feedback, or support? Reach out to:

> **David** – davidk76011@gmail.com

# File: modules/ui.py

import gradio as gr
from modules.translator import detect_lang
from modules.voice import speak_text

def launch_ui(brain):
    def handle_text_input(text):
        response = brain.process_text(text)
        lang = detect_lang(text)
        speak_text(response, language=lang)
        return response

    def handle_code_input(code):
        response = brain.process_code(code)
        return response

    def handle_image_upload(image, task, instruction):
        if task == "Edit":
            return brain.process_image_edit(image, instruction)
        elif task == "Enhance":
            return brain.process_image_enhance(image)
        elif task == "Deblur":
            return brain.process_image_deblur(image)
        else:
            return image

    with gr.Blocks(title="David One AI") as ui:
        gr.Markdown("# 🤖 David One AI – Multilingual Assistant")
        gr.Markdown("Created by **David** | Contact: `davidk76011@gmail.com`")

        with gr.Tab("💬 Conversation"):
            text_input = gr.Textbox(label="Enter your message")
            text_output = gr.Textbox(label="AI Response", interactive=False)
            text_button = gr.Button("Send")
            text_button.click(handle_text_input, inputs=text_input, outputs=text_output)

        with gr.Tab("💻 Code Help"):
            code_input = gr.Textbox(label="Describe what to build")
            code_output = gr.Textbox(label="Generated Code", lines=10)
            code_button = gr.Button("Generate")
            code_button.click(handle_code_input, inputs=code_input, outputs=code_output)

        with gr.Tab("🖼️ Image Tools"):
            image_input = gr.Image(type="pil", label="Upload Image")
            task_dropdown = gr.Dropdown(["Edit", "Enhance", "Deblur"], label="Select Task")
            instruction = gr.Textbox(label="Instruction (for edit only)", placeholder="e.g., remove background")
            image_output = gr.Image(label="Result")
            image_button = gr.Button("Run")
            image_button.click(fn=handle_image_upload, 
                               inputs=[image_input, task_dropdown, instruction], 
                               outputs=image_output)

    print("🚀 Launching UI on http://localhost:7860 ...")
    ui.launch(share=False)

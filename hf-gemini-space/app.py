import os
import gradio as gr
import google.generativeai as genai

# Configure the Gemini API with your secret key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Add it as a Secret in your Space settings (Settings → Secrets)."
    )

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


def generate_text(prompt, max_tokens, temperature):
    """Call Gemini and return the generated text."""
    if not prompt.strip():
        return "Please enter a prompt."

    generation_config = genai.types.GenerationConfig(
        max_output_tokens=int(max_tokens),
        temperature=temperature,
    )

    try:
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


# Build the Gradio interface
with gr.Blocks(title="Gemini Text Generator") as demo:
    gr.Markdown("# Gemini 2.0 Flash — Text Generator")
    gr.Markdown(
        "A simple proof-of-concept that calls Google's Gemini API "
        "from a Hugging Face Space."
    )

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Prompt",
                placeholder="Enter your prompt here...",
                lines=4,
            )
            max_tokens = gr.Slider(
                minimum=50,
                maximum=2048,
                value=512,
                step=50,
                label="Max tokens",
            )
            temperature = gr.Slider(
                minimum=0.0,
                maximum=2.0,
                value=1.0,
                step=0.1,
                label="Temperature",
            )
            btn = gr.Button("Generate", variant="primary")

        with gr.Column():
            output = gr.Textbox(label="Response", lines=12)

    btn.click(
        fn=generate_text,
        inputs=[prompt, max_tokens, temperature],
        outputs=output,
    )

demo.launch()

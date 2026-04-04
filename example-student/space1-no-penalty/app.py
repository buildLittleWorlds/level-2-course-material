import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="distilbert/distilgpt2", device=-1)

def generate_text(prompt, temperature, max_tokens):
    if not prompt.strip():
        return "Please enter a prompt."
    result = generator(
        prompt,
        max_new_tokens=int(max_tokens),
        temperature=float(temperature),
        do_sample=True,
        truncation=True,
    )
    return result[0]["generated_text"]

demo = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(
            label="Prompt",
            placeholder="Start typing about birds...",
            lines=3,
            value="The northern cardinal sings",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=2.0,
            value=1.0,
            step=0.1,
            label="Temperature",
            info="Lower = more predictable, Higher = more creative",
        ),
        gr.Slider(
            minimum=20,
            maximum=200,
            value=80,
            step=10,
            label="Max New Tokens",
            info="How much text to generate",
        ),
    ],
    outputs=gr.Textbox(label="Generated Text", lines=8),
    title="Bird Text Generator",
    description=(
        "A text generation playground using distilgpt2, customized with bird-themed prompts. "
        "This is Riley's Space 1 — a baseline text generator. It can write about birds "
        "but doesn't actually know anything about them. Try different temperature settings "
        "to see how randomness affects the output."
    ),
    examples=[
        ["The northern cardinal sings", 1.0, 80],
        ["In the forest canopy, the warbler", 0.7, 100],
        ["Migration patterns suggest that", 0.5, 120],
        ["The red-tailed hawk circled above the parking lot", 1.0, 80],
        ["At dawn, the chorus of birdsong", 1.3, 100],
    ],
    theme=gr.themes.Soft(),
)

demo.launch()

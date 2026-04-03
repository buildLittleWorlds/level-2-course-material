# ========================================
# DOMAIN-ADAPTED TEXT GENERATOR
# ========================================
# Same model as Session 5's text generator (distilgpt2),
# but with domain preset prompts. The dropdown changes
# the prompt template — the model stays the same.
#
# This demonstrates domain shift: the model writes
# differently (and with different quality) depending
# on the domain of the prompt. It was trained on web
# text, so some domains feel natural and others don't.
# ========================================

import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="distilbert/distilgpt2")

DOMAIN_PRESETS = {
    "Game Dialogue": "The warrior stepped into the dungeon and said:",
    "Medical Notes": "Patient presents with acute onset of",
    "News Article": "Breaking news: scientists announced today that",
    "Poetry": "I wandered through the silver rain and found",
    "Recipe": "To prepare this dish, first you need to",
    "Custom (type your own)": "",
}


def generate(domain, custom_prompt, temperature, max_length):
    # Use custom prompt if provided, otherwise use domain preset
    if custom_prompt and custom_prompt.strip():
        prompt = custom_prompt.strip()
    else:
        prompt = DOMAIN_PRESETS.get(domain, "")

    if not prompt:
        return "Select a domain or type your own prompt above!"

    result = generator(
        prompt,
        max_new_tokens=max_length,
        temperature=max(temperature, 0.01),
        do_sample=True,
        truncation=True,
    )

    generated = result[0]["generated_text"]

    return (
        f"{generated}\n\n"
        f"---\n"
        f"Domain: {domain} | Temperature: {temperature} | Max tokens: {max_length}"
    )


def update_prompt(domain):
    """When a domain is selected, fill the prompt box with its template."""
    return DOMAIN_PRESETS.get(domain, "")


with gr.Blocks(title="Domain Generator") as demo:
    gr.Markdown("# Domain Generator")
    gr.Markdown(
        "Same model, different worlds. Pick a domain and watch how the AI writes. "
        "Some domains feel natural — others fall apart. That's domain shift."
    )

    with gr.Row():
        domain = gr.Dropdown(
            choices=list(DOMAIN_PRESETS.keys()),
            value="Game Dialogue",
            label="Domain Preset",
        )
        temperature = gr.Slider(
            minimum=0.1, maximum=2.0, value=0.7, step=0.1,
            label="Temperature",
        )
        max_length = gr.Slider(
            minimum=20, maximum=200, value=80, step=10,
            label="Max New Tokens",
        )

    prompt_box = gr.Textbox(
        lines=2,
        value=DOMAIN_PRESETS["Game Dialogue"],
        label="Prompt (edit freely or pick a preset above)",
        placeholder="Type a sentence for the model to continue...",
    )

    domain.change(fn=update_prompt, inputs=domain, outputs=prompt_box)

    btn = gr.Button("Generate", variant="primary")
    output = gr.Textbox(label="Generated Text", lines=8)

    btn.click(
        fn=generate,
        inputs=[domain, prompt_box, temperature, max_length],
        outputs=output,
    )

demo.launch()

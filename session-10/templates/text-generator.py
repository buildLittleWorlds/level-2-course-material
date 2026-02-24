# ========================================
# TEXT GENERATOR TEMPLATE
# ========================================
# This template uses distilgpt2 to generate text
# from a prompt. Includes a temperature slider
# so users can control creativity.
#
# To customize:
# - Change the default prompt
# - Adjust max_new_tokens for longer/shorter output
# - Change the temperature range
# ========================================

import gradio as gr
from transformers import pipeline

# Small text generation model — runs on free CPU
generator = pipeline("text-generation", model="distilgpt2")


def generate(prompt, temperature):
    if not prompt or not prompt.strip():
        return "Type a starting sentence above!"

    result = generator(
        prompt,
        max_new_tokens=80,
        temperature=max(temperature, 0.01),  # Avoid zero
        do_sample=True,
        num_return_sequences=1,
    )

    return result[0]["generated_text"]


demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(
            lines=3,
            placeholder="Start a sentence and the AI will finish it...",
            label="Your Prompt",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=2.0,
            value=0.7,
            step=0.1,
            label="Temperature (low = predictable, high = creative)",
        ),
    ],
    outputs=gr.Textbox(label="Generated Text", lines=6),
    title="AI Story Starter",
    description="Type the beginning of a sentence and let the AI continue it. Use the temperature slider to control how creative (or predictable) the output is.",
    examples=[
        ["Once upon a time in a city made entirely of glass,", 0.7],
        ["The scientist looked at the data and realized", 0.3],
        ["Dear diary, today was the strangest day because", 1.2],
    ],
)

demo.launch()

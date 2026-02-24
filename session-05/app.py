from transformers import pipeline
import gradio as gr

# Load a small text generation model (fast on free CPU)
print("Loading distilgpt2...")
generator = pipeline("text-generation", model="distilgpt2")
print("Model loaded!")


def generate_text(prompt, temperature, top_p, max_length):
    if not prompt or not prompt.strip():
        return "Type a prompt above first!"

    result = generator(
        prompt,
        temperature=max(temperature, 0.01),  # avoid division by zero
        top_p=top_p,
        max_length=int(max_length),
        do_sample=True,
        num_return_sequences=1,
    )
    return result[0]["generated_text"]


demo = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(
            lines=3,
            placeholder="Start your text here...",
            label="Prompt",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=2.0,
            value=0.7,
            step=0.1,
            label="Temperature (creativity)",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.9,
            step=0.05,
            label="Top-p (diversity)",
        ),
        gr.Slider(
            minimum=20,
            maximum=200,
            value=100,
            step=10,
            label="Max Length (words-ish)",
        ),
    ],
    outputs=gr.Textbox(label="Generated Text", lines=10),
    title="Text Playground",
    description="Type a prompt and use the sliders to control how the AI writes. Temperature controls creativity (low = predictable, high = wild). Top-p controls word diversity. Max length controls how much it writes.",
    examples=[
        ["Once upon a time in a school where robots", 0.7, 0.9, 100],
        ["The secret ingredient in the recipe was", 1.2, 0.9, 80],
        ["Dear Principal, I am writing to request", 0.3, 0.9, 100],
        ["Breaking news: scientists discover that cats", 0.9, 0.95, 120],
        ["The haunted house at the end of the street", 1.5, 0.8, 150],
    ],
)

demo.launch()

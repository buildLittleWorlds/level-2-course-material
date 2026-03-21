from transformers import pipeline
import gradio as gr

# Load distilgpt2 — a small text generation model (82M parameters)
print("Loading text generation model (distilgpt2)...")
generator = pipeline(
    "text-generation",
    model="distilbert/distilgpt2",
)
print("Model loaded!")


def generate_text(prompt):
    """Generate a continuation of the input text."""
    if not prompt or not prompt.strip():
        return "Type a sentence or two and watch the model try to continue it."

    # Generate with default settings — no temperature control yet
    # (that's Session 5!)
    result = generator(
        prompt,
        max_new_tokens=80,
        num_return_sequences=1,
        do_sample=True,
        truncation=True,
    )

    return result[0]["generated_text"]


demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Type a sentence or the beginning of a story...",
        label="Your Prompt",
    ),
    outputs=gr.Textbox(
        label="What the Model Wrote",
        lines=8,
    ),
    title="Text Generator",
    description=(
        "This model doesn't classify — it creates. "
        "Type a sentence and watch it try to write what comes next. "
        "It's a small model (82M parameters), so the results won't be "
        "perfect — but it's doing something fundamentally different from "
        "the classification models we've used so far."
    ),
    examples=[
        ["Monday morning arrived like a gift from the universe — truly, what better way to start the week than"],
        ["The acceptance letter sat on the kitchen table, and she couldn't stop reading it."],
        ["The volcano had been dormant for three hundred years. When it finally erupted,"],
        ["Once upon a time, in a city made entirely of glass,"],
        ["The capital of France is"],
    ],
)

demo.launch()

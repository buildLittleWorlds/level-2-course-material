import gradio as gr
from transformers import pipeline

# Space 1 — Debate Content Scorer (baseline).
#
# This is the intentionally bad baseline. It uses distilgpt2, a small generic
# text-generation model, and tries to "continue" a debate speech as if that
# were a way of scoring or responding to an argument. It isn't. The point of
# this Space in Prea's arc is to show what text-only, generator-based tools
# *can't* do on a task that fundamentally depends on how speech is delivered.
#
# See research-journal.md, Week 5, for the full write-up.

generator = pipeline("text-generation", model="distilbert/distilgpt2", device=-1)

WSDC_EXAMPLES = [
    (
        "This house would ban single-use plastics in public schools. "
        "The first and most important reason is that",
        0.7,
        100,
    ),
    (
        "My opponent claims the cost of universal transit is prohibitive. "
        "This argument fails because",
        0.7,
        100,
    ),
    (
        "Madam Chair, the evidence is overwhelming. In 2023 alone,",
        1.0,
        120,
    ),
    (
        "We must act now, before it is too late. The reason is simple:",
        0.5,
        100,
    ),
]


def score_speech(prompt, temperature, max_tokens):
    if not prompt.strip():
        return "Please enter a debate prompt."
    result = generator(
        prompt,
        max_new_tokens=int(max_tokens),
        temperature=float(temperature),
        do_sample=True,
        truncation=True,
    )
    return result[0]["generated_text"]


demo = gr.Interface(
    fn=score_speech,
    inputs=[
        gr.Textbox(
            label="Debate Speech Opening",
            placeholder="Enter the first line or two of a debate speech...",
            lines=4,
            value="This house would ban single-use plastics in public schools. The first and most important reason is that",
        ),
        gr.Slider(
            minimum=0.1,
            maximum=1.5,
            value=0.7,
            step=0.1,
            label="Temperature",
            info="Lower = more predictable, Higher = more creative (and more likely to fabricate)",
        ),
        gr.Slider(
            minimum=40,
            maximum=200,
            value=100,
            step=10,
            label="Max New Tokens",
            info="How much text to generate",
        ),
    ],
    outputs=gr.Textbox(label="Model continuation", lines=10),
    title="Debate Content Scorer — Baseline (distilgpt2)",
    description=(
        "This is Prea's Space 1 — an intentionally weak baseline. "
        "It uses distilgpt2 (a small generic text-generation model) to 'continue' "
        "the opening of a debate speech. My original plan was to use this as a content "
        "scorer, but as soon as I tried it on real debate openings I realized that a "
        "text generator can't tell you whether an argument is good — it will happily "
        "fabricate evidence, misquote statistics, and wander off topic. That failure is "
        "the reason Spaces 2 and 3 exist. See research-journal.md, Week 5, for the full "
        "write-up, and try the examples below to watch it make up citations that don't exist."
    ),
    examples=[list(ex) for ex in WSDC_EXAMPLES],
    theme=gr.themes.Soft(),
)

demo.launch()

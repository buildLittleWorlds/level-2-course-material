# ========================================
# TEXT SUMMARIZER WITH CONTROLS
# ========================================
# This Space summarizes long text into a short
# version. Unlike the text generator, this model
# CONDENSES — it reads everything and picks out
# the key points. Both are generative models:
# one creates from scratch, this one rewrites shorter.
#
# Hyperparameters (the controls):
# - Max length: how long the summary can be
# - Min length: how short it's allowed to be
# ========================================

import gradio as gr
from transformers import pipeline

# Distilled summarization model — works on free CPU
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6",
)


def summarize(text, max_length, min_length):
    if not text or not text.strip():
        return "Paste some text above to summarize!"

    word_count = len(text.split())
    if word_count < 30:
        return "The text is too short to summarize — try pasting something longer (at least a paragraph)."

    # Make sure min doesn't exceed max
    min_length = min(min_length, max_length - 10)
    if min_length < 10:
        min_length = 10

    result = summarizer(
        text[:1024],
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
    )

    summary = result[0]["summary_text"]
    summary_words = len(summary.split())

    return (
        f"{summary}\n\n"
        f"---\n"
        f"Original: {word_count} words → Summary: {summary_words} words "
        f"({summary_words / word_count:.0%} of original)"
    )


demo = gr.Interface(
    fn=summarize,
    inputs=[
        gr.Textbox(
            lines=10,
            placeholder="Paste an article, essay, or long text here...",
            label="Text to Summarize",
        ),
        gr.Slider(
            minimum=30,
            maximum=200,
            value=100,
            step=10,
            label="Max Summary Length (tokens)",
        ),
        gr.Slider(
            minimum=10,
            maximum=100,
            value=25,
            step=5,
            label="Min Summary Length (tokens)",
        ),
    ],
    outputs=gr.Textbox(label="Summary", lines=6),
    title="Quick Summarizer",
    description=(
        "Paste a long article or essay and get a short summary. "
        "Use the sliders to control how long or short the summary is. "
        "The AI reads the whole thing and picks out the key points."
    ),
    examples=[
        [
            "Artificial intelligence has transformed many industries over the past decade. "
            "In healthcare, AI systems can now detect diseases from medical images with "
            "accuracy rivaling human doctors. In finance, algorithmic trading powered by "
            "machine learning processes millions of transactions per second. Education is "
            "also being reshaped, with AI tutors providing personalized learning experiences "
            "for students around the world. However, these advances come with significant "
            "challenges. Privacy concerns arise when AI systems require vast amounts of "
            "personal data. Job displacement remains a worry as automation replaces routine "
            "tasks. And bias in AI systems can perpetuate or even amplify existing social "
            "inequalities. Addressing these challenges while harnessing AI's potential will "
            "be one of the defining tasks of our generation.",
            100,
            25,
        ],
        [
            "The patient presented to the emergency department with acute onset of "
            "substernal chest pain radiating to the left arm, accompanied by diaphoresis "
            "and shortness of breath. Initial ECG showed ST-segment elevation in leads "
            "II, III, and aVF, consistent with inferior myocardial infarction. Troponin "
            "levels were elevated at 2.4 ng/mL. The patient was started on dual "
            "antiplatelet therapy and heparin infusion, and cardiology was consulted for "
            "emergent cardiac catheterization. Past medical history is significant for "
            "hypertension, type 2 diabetes mellitus, and hyperlipidemia. The patient "
            "reports a 30-pack-year smoking history.",
            60,
            20,
        ],
        [
            "The Legend of Zelda series has captivated gamers for nearly four decades "
            "with its unique blend of exploration, puzzle-solving, and combat. Starting "
            "with the original 1986 NES title, the franchise established a template for "
            "action-adventure games that continues to influence game design today. Each "
            "entry reimagines the core formula while maintaining the series' identity: "
            "a young hero named Link must rescue Princess Zelda and defeat the villain "
            "Ganondorf across a sprawling fantasy world. The 2017 release of Breath of "
            "the Wild revolutionized open-world game design by giving players complete "
            "freedom to explore Hyrule in any order, solving puzzles with emergent physics "
            "systems rather than predetermined solutions. Its 2023 sequel, Tears of the "
            "Kingdom, expanded on this foundation by adding the ability to build and "
            "combine objects, creating an unprecedented sandbox within a narrative-driven "
            "adventure game.",
            100,
            25,
        ],
    ],
)

demo.launch()

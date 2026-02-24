# ========================================
# TEXT SUMMARIZER TEMPLATE
# ========================================
# This template summarizes long text into a
# short version. Great for articles, essays,
# or long messages.
#
# To customize:
# - Adjust min/max summary length
# - Change the input placeholder and examples
# - Add word count comparison
# ========================================

import gradio as gr
from transformers import pipeline

# Distilled summarization model — works on free CPU
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
)


def summarize(text):
    if not text or not text.strip():
        return "Paste some text above to summarize!"

    word_count = len(text.split())
    if word_count < 30:
        return "The text is too short to summarize — try pasting something longer (at least a paragraph)."

    result = summarizer(
        text[:1024],
        max_length=100,
        min_length=25,
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
    inputs=gr.Textbox(
        lines=10,
        placeholder="Paste an article, essay, or long text here...",
        label="Text to Summarize",
    ),
    outputs=gr.Textbox(label="Summary", lines=6),
    title="Quick Summarizer",
    description="Paste a long article or essay and get a short summary. The AI reads the whole thing and picks out the key points.",
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
            "be one of the defining tasks of our generation."
        ],
    ],
)

demo.launch()

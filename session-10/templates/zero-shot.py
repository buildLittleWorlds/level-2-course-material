# ========================================
# ZERO-SHOT CLASSIFIER TEMPLATE
# ========================================
# This template classifies text into categories
# YOU define — no training required. Similar to
# the Silly Phrase Finder from Session 1.
#
# To customize:
# - Change the default categories
# - Change the description and examples
# - Adjust how results are displayed
# ========================================

import gradio as gr
from transformers import pipeline

# Zero-shot model — you define the labels at runtime
classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-3",
)


def classify(text, categories):
    if not text or not text.strip():
        return "Enter some text above!"
    if not categories or not categories.strip():
        return "Enter at least two categories, separated by commas!"

    labels = [c.strip() for c in categories.split(",") if c.strip()]
    if len(labels) < 2:
        return "Enter at least two categories, separated by commas!"

    result = classifier(text[:512], labels)

    lines = []
    for label, score in zip(result["labels"], result["scores"]):
        bar = "█" * int(score * 20) + "░" * (20 - int(score * 20))
        lines.append(f"{label:20s} {bar} {score:.0%}")

    return "\n".join(lines)


demo = gr.Interface(
    fn=classify,
    inputs=[
        gr.Textbox(lines=3, placeholder="Type or paste text here...", label="Text"),
        gr.Textbox(
            lines=1,
            placeholder="e.g. sports, politics, technology, entertainment",
            label="Categories (comma-separated)",
            value="sports, politics, technology, entertainment",
        ),
    ],
    outputs=gr.Textbox(label="Classification Results", lines=5),
    title="Topic Sorter",
    description="Paste any text and define your own categories. The AI will sort the text into your categories — no training needed!",
    examples=[
        ["The team scored a last-second touchdown to win the Super Bowl.", "sports, politics, technology, entertainment"],
        ["The new smartphone features a 200MP camera and foldable screen.", "sports, politics, technology, entertainment"],
        ["The senator introduced a bill to regulate social media platforms.", "sports, politics, technology, entertainment"],
    ],
)

demo.launch()

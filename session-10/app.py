# ========================================
# YOUR SPACE NAME HERE
# ========================================
# To customize this template:
# 1. Change the model (line 20)
# 2. Change the title and description (line 32-33)
# 3. Change the examples (line 34-37)
# 4. Change how results are displayed (line 27)
# ========================================

import gradio as gr
from transformers import pipeline

# CHANGE THIS: Pick your model from https://huggingface.co/models
# Examples:
#   "distilbert-base-uncased-finetuned-sst-2-english"  → sentiment (positive/negative)
#   "j-hartmann/emotion-english-distilroberta-base"     → emotions (anger, joy, surprise...)
#   "facebook/bart-large-mnli"                          → zero-shot (you pick the labels)
#   "distilgpt2"                                        → text generation
#   "sshleifer/distilbart-cnn-12-6"                     → summarization
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


# CHANGE THIS: Your analysis function
def analyze(text):
    if not text or not text.strip():
        return "Enter some text above!"
    result = model(text[:512])[0]
    return f"{result['label']} ({result['score']:.1%} confidence)"


# CHANGE THIS: Title, description, and examples
demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=5, placeholder="Type or paste text here...", label="Input"),
    outputs=gr.Textbox(label="Result"),
    title="My AI Tool",                # ← Change this
    description="Description here.",    # ← Change this
    examples=[                          # ← Change these
        ["Example input 1"],
        ["Example input 2"],
    ],
)

demo.launch()

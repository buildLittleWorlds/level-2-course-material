import gradio as gr
from transformers import pipeline
import re

# ============================================================
# SESSION 2: Swap the Engine
# ============================================================
# This session explores how different models give different
# answers to the same input. The code below uses the EMOTION
# model (the final state after the live swap exercise).
#
# During class, the instructor starts with the original
# zero-shot model, swaps to sentiment, then lands on emotion.
# ============================================================

# --- OPTION 1: Original zero-shot model (Session 1) ---
# classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")

# --- OPTION 2: Sentiment model (trained on movie reviews) ---
# classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# --- OPTION 3: Emotion model (trained on tweets) --- ACTIVE
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")


def analyze_text(text):
    if not text or not text.strip():
        return "Type or paste some text above first!"

    # Split into sentences
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"])', text) if len(s.strip()) > 10]

    if len(sentences) == 0:
        return "I need at least one full sentence. Try typing a bit more!"

    # Classify each sentence
    output_lines = []
    for sentence in sentences:
        result = classifier(sentence)[0]
        label = result["label"]
        score = result["score"]
        output_lines.append(f"{label.upper()} ({score:.0%}): {sentence}")

    return "\n\n".join(output_lines)


demo = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(lines=8, placeholder="Type or paste some text here..."),
    outputs=gr.Textbox(label="Emotion Analysis", lines=12),
    title="Emotion Detector",
    description="Paste any text and see what emotion the AI detects in each sentence. This model was trained on tweets — how does it handle other kinds of text?",
    examples=[
        ["I can't believe we won the championship! The whole team was screaming. Coach just stood there crying. Best night of my life."],
        ["The test is tomorrow and I haven't started studying. My notes are a mess. I don't even understand chapter 4. Maybe I should just give up."],
        ["The weather today is partly cloudy with a high of 72. Traffic on the highway is moving smoothly. The library closes at 5pm."],
    ],
)

demo.launch()

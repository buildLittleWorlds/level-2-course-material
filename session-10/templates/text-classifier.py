# ========================================
# TEXT CLASSIFIER TEMPLATE
# ========================================
# This template uses an emotion detection model.
# It classifies text into emotions: anger, disgust,
# fear, joy, neutral, sadness, surprise.
#
# To customize:
# - Swap the model for a different classifier
# - Change the output formatting
# - Add your own examples
# ========================================

import gradio as gr
from transformers import pipeline

# Emotion detection model — works great on free CPU
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=3,  # Return top 3 emotions
)

EMOJI_MAP = {
    "anger": "😠",
    "disgust": "🤢",
    "fear": "😨",
    "joy": "😊",
    "neutral": "😐",
    "sadness": "😢",
    "surprise": "😲",
}


def classify(text):
    if not text or not text.strip():
        return "Enter some text above!"

    results = classifier(text[:512])[0]

    lines = []
    for r in results:
        emoji = EMOJI_MAP.get(r["label"], "")
        bar = "█" * int(r["score"] * 20) + "░" * (20 - int(r["score"] * 20))
        lines.append(f"{emoji} {r['label'].title():10s} {bar} {r['score']:.0%}")

    return "\n".join(lines)


demo = gr.Interface(
    fn=classify,
    inputs=gr.Textbox(lines=4, placeholder="Type something...", label="Text"),
    outputs=gr.Textbox(label="Detected Emotions", lines=4),
    title="Emotion Detector",
    description="Paste any text and see what emotions the AI detects.",
    examples=[
        ["I can't believe we won the championship! This is the best day ever!"],
        ["I'm so tired of dealing with this. Nothing ever works out."],
        ["The spider crawled across my desk and I screamed."],
    ],
)

demo.launch()

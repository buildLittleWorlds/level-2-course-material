import gradio as gr
from transformers import pipeline
import re

# Load three models that "read" feelings differently
model_binary = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
model_emotion = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
model_zeroshot = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")

# Default feeling labels for the zero-shot model
DEFAULT_LABELS = "love, grief, anxiety, hope, anger, confusion, calm"

def analyze_feelings(text, custom_labels):
    if not text or not text.strip():
        return "Paste some text above first!", "Paste some text above first!", "Paste some text above first!"

    # Split into sentences
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"])', text) if len(s.strip()) > 10]
    if len(sentences) == 0:
        sentences = [text.strip()]

    # Model 1: Binary (POSITIVE / NEGATIVE)
    binary_lines = []
    for sentence in sentences:
        result = model_binary(sentence)[0]
        label = result["label"]
        score = result["score"]
        emoji = "😊" if label == "POSITIVE" else "😢"
        binary_lines.append(f"{emoji} {label} ({score:.0%}): {sentence}")
    binary_output = "\n\n".join(binary_lines)

    # Model 2: 7 Emotions
    emotion_lines = []
    emoji_map = {
        "anger": "😠", "disgust": "🤢", "fear": "😨",
        "joy": "😄", "neutral": "😐", "sadness": "😢", "surprise": "😲"
    }
    for sentence in sentences:
        result = model_emotion(sentence)[0]
        label = result["label"]
        score = result["score"]
        emoji = emoji_map.get(label, "❓")
        emotion_lines.append(f"{emoji} {label.upper()} ({score:.0%}): {sentence}")
    emotion_output = "\n\n".join(emotion_lines)

    # Model 3: Zero-shot with custom labels
    labels = [l.strip() for l in custom_labels.split(",") if l.strip()]
    if not labels:
        labels = [l.strip() for l in DEFAULT_LABELS.split(",")]
    zeroshot_lines = []
    for sentence in sentences:
        result = model_zeroshot(sentence, candidate_labels=labels)
        top_label = result["labels"][0]
        top_score = result["scores"][0]
        zeroshot_lines.append(f"🏷 {top_label.upper()} ({top_score:.0%}): {sentence}")
    zeroshot_output = "\n\n".join(zeroshot_lines)

    return binary_output, emotion_output, zeroshot_output

demo = gr.Interface(
    fn=analyze_feelings,
    inputs=[
        gr.Textbox(lines=6, placeholder="Paste any text here — the same words will get three different emotional readings..."),
        gr.Textbox(lines=1, value=DEFAULT_LABELS, label="Custom feeling labels (for Model 3 — change these!)",
                   placeholder="e.g., love, grief, anxiety, hope, anger, confusion, calm"),
    ],
    outputs=[
        gr.Textbox(label="Model 1: Binary (Positive / Negative)", lines=6),
        gr.Textbox(label="Model 2: Seven Emotions", lines=6),
        gr.Textbox(label="Model 3: YOUR Feeling Labels", lines=6),
    ],
    title="Emotion Spectrum",
    description="Three AI models read the same text — and see three different kinds of feelings. Model 1 only knows POSITIVE and NEGATIVE. Model 2 knows 7 emotions. Model 3 uses whatever feeling words YOU choose. Which one gets closest to how the text actually feels?",
    examples=[
        ["I can't believe we won the championship! The whole team was screaming. Coach just stood there crying. Best night of my life.", DEFAULT_LABELS],
        ["I stayed up until 4am thinking about what I said to her. I keep replaying it. I don't think I can fix this one.", DEFAULT_LABELS],
        ["The weather today is partly cloudy with a high of 72. Traffic on the highway is moving smoothly. The library closes at 5pm.", DEFAULT_LABELS],
        ["lol my flight got cancelled for the third time this week. I literally cannot with this airline.", DEFAULT_LABELS],
    ],
)

demo.launch()

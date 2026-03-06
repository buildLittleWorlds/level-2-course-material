import gradio as gr
from transformers import pipeline

# Load a sentiment analysis model (works on free CPU)
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def check_mood(text):
    if not text or not text.strip():
        return "Paste some text above first!"

    result = analyzer(text)[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        emoji = "😊" if score > 0.9 else "🙂"
    else:
        emoji = "😢" if score > 0.9 else "😐"

    return f"{emoji} {label}\n\nConfidence: {score:.0%}"

demo = gr.Interface(
    fn=check_mood,
    inputs=gr.Textbox(lines=8, placeholder="Paste any text here — a song lyric, a diary entry, a text from a friend..."),
    outputs=gr.Textbox(label="Mood Reading"),
    title="Mood Meter",
    description="Paste any text and this AI will tell you whether it feels POSITIVE or NEGATIVE — and how confident it is. Does the model agree with how YOU feel about the text?",
    examples=[
        ["I can't believe how lucky I am to have friends like you. Every day feels like an adventure and I wouldn't trade it for anything in the world."],
        ["I don't know why I even bother anymore. Nothing I do seems to matter and nobody notices when I try my hardest."],
        ["Dear future me, I hope you figured it out. I hope you're not still lying awake at 2am wondering if you made the right choice."],
        ["Walking into school on the first day felt like stepping onto another planet. Everyone already knew each other and I just stood there holding my backpack straps."],
    ],
)

demo.launch()

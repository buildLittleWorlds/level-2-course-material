"""
Sentiment Battle Arena
======================
Enter a sentence and see how four different sentiment models interpret it.
VADER (rule-based), Binary (DistilBERT), 7-Emotion (DistilRoBERTa),
and 28-Emotion GoEmotions (RoBERTa) — side by side.
"""

import gradio as gr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# ---------------------------------------------------------------------------
# Load models once at startup
# ---------------------------------------------------------------------------
print("Loading models...")
vader = SentimentIntensityAnalyzer()

binary_clf = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=-1,
)
emotion_clf = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    device=-1,
    top_k=None,
)
go_emotions_clf = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    device=-1,
    top_k=None,
)
print("All models loaded.")

# ---------------------------------------------------------------------------
# Emotion → color mapping
# ---------------------------------------------------------------------------
EMOTION_COLORS = {
    "joy": "#fbbf24", "sadness": "#60a5fa", "anger": "#f87171",
    "fear": "#a78bfa", "surprise": "#34d399", "disgust": "#fb923c",
    "neutral": "#9ca3af",
    # GoEmotions extras
    "admiration": "#fcd34d", "amusement": "#fbbf24", "annoyance": "#fb923c",
    "approval": "#86efac", "caring": "#f9a8d4", "confusion": "#c4b5fd",
    "curiosity": "#67e8f9", "desire": "#f472b6", "disappointment": "#93c5fd",
    "disapproval": "#fca5a5", "embarrassment": "#fda4af", "excitement": "#fde047",
    "gratitude": "#86efac", "grief": "#6b7280", "love": "#fb7185",
    "nervousness": "#d8b4fe", "optimism": "#a3e635", "pride": "#facc15",
    "realization": "#7dd3fc", "relief": "#6ee7b7", "remorse": "#a5b4fc",
}


def get_color(label):
    return EMOTION_COLORS.get(label, "#d1d5db")


# ---------------------------------------------------------------------------
# Analysis function
# ---------------------------------------------------------------------------
def analyze(text):
    if not text or not text.strip():
        return None

    results = {}

    # VADER
    vs = vader.polarity_scores(text)
    compound = vs["compound"]
    if compound >= 0.05:
        vader_label = "POSITIVE"
    elif compound <= -0.05:
        vader_label = "NEGATIVE"
    else:
        vader_label = "NEUTRAL"
    results["vader"] = {
        "label": vader_label,
        "score": abs(compound),
        "detail": f"compound = {compound:+.3f}",
    }

    # Binary
    b = binary_clf(text, truncation=True)[0]
    results["binary"] = {
        "label": b["label"],
        "score": b["score"],
        "detail": f"{b['score']:.1%} confident",
    }

    # 7-Emotion
    emo = emotion_clf(text, truncation=True)[0]
    emo = sorted(emo, key=lambda x: x["score"], reverse=True)
    top3 = emo[:3]
    results["emotion"] = {
        "label": emo[0]["label"],
        "score": emo[0]["score"],
        "top3": top3,
    }

    # GoEmotions
    go = go_emotions_clf(text, truncation=True)[0]
    go = sorted(go, key=lambda x: x["score"], reverse=True)
    active = [r for r in go if r["score"] >= 0.15]
    if not active:
        active = go[:1]
    results["go_emotions"] = {
        "label": ", ".join(r["label"] for r in active),
        "score": go[0]["score"],
        "active": active,
    }

    return results


# ---------------------------------------------------------------------------
# Build HTML output
# ---------------------------------------------------------------------------
def build_html(results):
    if results is None:
        return "<p style='color:#9ca3af; text-align:center;'>Enter a sentence above and click Analyze.</p>"

    def make_bar(score, color="#3b82f6"):
        pct = score * 100
        return f'<div style="background:#e5e7eb;border-radius:4px;height:8px;width:100%;margin-top:4px;"><div style="background:{color};height:8px;border-radius:4px;width:{pct}%;transition:width 0.5s;"></div></div>'

    # Card style
    card = (
        "background:white;border:1px solid #e5e7eb;border-radius:16px;"
        "padding:20px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.05);"
    )

    # VADER card
    v = results["vader"]
    v_color = {"POSITIVE": "#22c55e", "NEGATIVE": "#ef4444", "NEUTRAL": "#9ca3af"}[v["label"]]
    vader_card = f"""
    <div style="{card}">
        <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;">VADER</div>
        <div style="font-size:10px;color:#9ca3af;margin-bottom:8px;">Rule-based lexicon</div>
        <div style="font-size:28px;font-weight:bold;color:{v_color};">{v['label']}</div>
        <div style="font-size:13px;color:#6b7280;margin-top:4px;">{v['detail']}</div>
        {make_bar(v['score'], v_color)}
    </div>
    """

    # Binary card
    b = results["binary"]
    b_color = "#22c55e" if b["label"] == "POSITIVE" else "#ef4444"
    binary_card = f"""
    <div style="{card}">
        <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;">Binary</div>
        <div style="font-size:10px;color:#9ca3af;margin-bottom:8px;">DistilBERT · SST-2</div>
        <div style="font-size:28px;font-weight:bold;color:{b_color};">{b['label']}</div>
        <div style="font-size:13px;color:#6b7280;margin-top:4px;">{b['detail']}</div>
        {make_bar(b['score'], b_color)}
    </div>
    """

    # Emotion card
    e = results["emotion"]
    e_color = get_color(e["label"])
    top3_html = "".join(
        f'<span style="display:inline-block;background:{get_color(t["label"])};color:#1f2937;padding:2px 8px;border-radius:8px;font-size:11px;margin:2px;">{t["label"]} {t["score"]:.0%}</span>'
        for t in e["top3"]
    )
    emotion_card = f"""
    <div style="{card}">
        <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;">7-Emotion</div>
        <div style="font-size:10px;color:#9ca3af;margin-bottom:8px;">DistilRoBERTa · Ekman</div>
        <div style="font-size:28px;font-weight:bold;color:{e_color};">{e['label']}</div>
        <div style="margin-top:8px;">{top3_html}</div>
        {make_bar(e['score'], e_color)}
    </div>
    """

    # GoEmotions card
    g = results["go_emotions"]
    active_html = "".join(
        f'<span style="display:inline-block;background:{get_color(a["label"])};color:#1f2937;padding:2px 8px;border-radius:8px;font-size:11px;margin:2px;">{a["label"]} {a["score"]:.0%}</span>'
        for a in g["active"]
    )
    go_card = f"""
    <div style="{card}">
        <div style="font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;">GoEmotions</div>
        <div style="font-size:10px;color:#9ca3af;margin-bottom:8px;">RoBERTa · 28 emotions</div>
        <div style="font-size:16px;font-weight:bold;color:#1f2937;margin:8px 0;">{g['active'][0]['label']}</div>
        <div style="margin-top:4px;">{active_html}</div>
        {make_bar(g['score'], get_color(g['active'][0]['label']))}
    </div>
    """

    return f"""
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:700px;margin:0 auto;">
        {vader_card}
        {binary_card}
        {emotion_card}
        {go_card}
    </div>
    """


def run_analysis(text):
    results = analyze(text)
    return build_html(results)


# ---------------------------------------------------------------------------
# Gradio app
# ---------------------------------------------------------------------------
EXAMPLES = [
    "This is the best movie I have ever seen in my entire life.",
    "This was an absolutely terrible waste of my time.",
    "The meeting has been moved to 3 PM on Thursday.",
    "Oh great, another Monday morning. Just what I needed.",
    "I'm proud of what we accomplished, but I'm exhausted and a little sad it's over.",
    "You're actually much smarter than you look.",
    "There was a quiet dignity in the way she accepted the news, though her hands trembled.",
]

with gr.Blocks(
    title="Sentiment Battle Arena",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# Sentiment Battle Arena")
    gr.Markdown(
        "Enter a sentence and see how **four different models** interpret its sentiment. "
        "Same input, very different readings."
    )

    with gr.Row():
        text_input = gr.Textbox(
            label="Your sentence",
            placeholder="Type anything here...",
            lines=2,
            scale=4,
        )
        btn = gr.Button("Analyze", variant="primary", scale=1)

    output = gr.HTML(value=build_html(None))

    gr.Examples(examples=EXAMPLES, inputs=text_input)

    btn.click(fn=run_analysis, inputs=text_input, outputs=output)
    text_input.submit(fn=run_analysis, inputs=text_input, outputs=output)

demo.launch()

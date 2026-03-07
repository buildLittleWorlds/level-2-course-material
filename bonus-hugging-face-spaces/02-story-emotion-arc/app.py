"""
Story Emotion Arc Plotter
=========================
Paste a story, scene, or chapter and see the emotional arc plotted
paragraph by paragraph as a line chart. Uses the 7-emotion model
(j-hartmann/emotion-english-distilroberta-base).
"""

import gradio as gr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from transformers import pipeline

# ---------------------------------------------------------------------------
# Load model
# ---------------------------------------------------------------------------
print("Loading emotion model...")
emotion_clf = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    device=-1,
    top_k=None,
)
print("Model loaded.")

EMOTIONS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
EMOTION_COLORS = {
    "anger": "#ef4444",
    "disgust": "#f97316",
    "fear": "#a855f7",
    "joy": "#eab308",
    "neutral": "#9ca3af",
    "sadness": "#3b82f6",
    "surprise": "#10b981",
}

# ---------------------------------------------------------------------------
# Sample text
# ---------------------------------------------------------------------------
SAMPLE_TEXT = """The morning began with an unexpected calm. Sunlight poured through the curtains, and for the first time in weeks, she felt something close to peace.

But the calm didn't last. By noon, the news arrived — a letter she'd been dreading, sealed in a plain white envelope. Her hands shook as she read the words.

She sat for a long time after that, staring at nothing. The house was quiet. Even the birds outside had stopped singing.

Then something shifted. She stood up, folded the letter carefully, and placed it in a drawer. She would not let this define her. There was work to be done.

By evening, she found herself laughing — really laughing — for the first time in months. Her neighbor had brought over a ridiculous cake shaped like a dog, and the absurdity of it broke through everything.

She went to bed that night feeling something she couldn't quite name. Not happiness, exactly, but a kind of tender resolve. Tomorrow would be different. She would make sure of it."""


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def split_paragraphs(text):
    """Split text into paragraphs, filtering out blanks."""
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    return paragraphs


def analyze_arc(text):
    if not text or not text.strip():
        return None, ""

    paragraphs = split_paragraphs(text)
    if len(paragraphs) < 2:
        return None, "Please enter at least two paragraphs (separated by blank lines) to see an arc."

    # Run model on each paragraph
    all_scores = []
    dominant_emotions = []
    for para in paragraphs:
        results = emotion_clf(para, truncation=True)[0]
        score_dict = {r["label"]: r["score"] for r in results}
        all_scores.append(score_dict)
        dominant = max(results, key=lambda x: x["score"])
        dominant_emotions.append(dominant["label"])

    # Build the plot
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#fafafa")
    ax.set_facecolor("#fafafa")

    x = np.arange(1, len(paragraphs) + 1)

    # Plot each emotion as a line
    for emotion in EMOTIONS:
        scores = [s.get(emotion, 0) for s in all_scores]
        ax.plot(
            x, scores,
            color=EMOTION_COLORS[emotion],
            linewidth=2,
            marker="o",
            markersize=5,
            label=emotion,
            alpha=0.85,
        )

    ax.set_xlabel("Paragraph", fontsize=12, fontweight="bold")
    ax.set_ylabel("Score", fontsize=12, fontweight="bold")
    ax.set_title("Emotional Arc", fontsize=16, fontweight="bold", pad=15)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.set_xlim(0.5, len(paragraphs) + 0.5)
    ax.set_ylim(0, 1)
    ax.legend(loc="upper right", fontsize=9, ncol=2)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    # Build paragraph summary HTML
    summary_parts = []
    for i, (para, dom) in enumerate(zip(paragraphs, dominant_emotions)):
        color = EMOTION_COLORS.get(dom, "#9ca3af")
        preview = para[:120] + ("..." if len(para) > 120 else "")
        summary_parts.append(
            f'<div style="display:flex;align-items:flex-start;gap:12px;margin:8px 0;">'
            f'<span style="background:{color};color:white;padding:2px 10px;border-radius:10px;'
            f'font-size:11px;font-weight:bold;white-space:nowrap;">P{i+1}: {dom}</span>'
            f'<span style="font-size:13px;color:#374151;">{preview}</span>'
            f'</div>'
        )

    summary_html = (
        '<div style="max-width:700px;margin:16px auto;">'
        '<h3 style="font-size:14px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Paragraph Breakdown</h3>'
        + "".join(summary_parts)
        + "</div>"
    )

    return fig, summary_html


# ---------------------------------------------------------------------------
# Gradio app
# ---------------------------------------------------------------------------
with gr.Blocks(
    title="Story Emotion Arc Plotter",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# Story Emotion Arc Plotter")
    gr.Markdown(
        "Paste a story, scene, or chapter below (with **blank lines between paragraphs**) "
        "and see the emotional arc plotted over time. Each paragraph is scored for seven emotions."
    )

    text_input = gr.Textbox(
        label="Your text",
        placeholder="Paste a story or scene here... (separate paragraphs with blank lines)",
        lines=10,
        value=SAMPLE_TEXT,
    )
    btn = gr.Button("Plot Emotion Arc", variant="primary")

    plot_output = gr.Plot(label="Emotion Arc")
    summary_output = gr.HTML()

    btn.click(fn=analyze_arc, inputs=text_input, outputs=[plot_output, summary_output])

demo.launch()

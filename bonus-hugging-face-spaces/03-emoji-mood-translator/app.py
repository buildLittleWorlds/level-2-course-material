"""
Emoji Mood Translator
=====================
Type a sentence and see which emotions a 28-category model detects,
translated into emojis with confidence bars.
Uses SamLowe/roberta-base-go_emotions.
"""

import gradio as gr
from transformers import pipeline

# ---------------------------------------------------------------------------
# Load model
# ---------------------------------------------------------------------------
print("Loading GoEmotions model...")
go_emotions_clf = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    device=-1,
    top_k=None,
)
print("Model loaded.")

# ---------------------------------------------------------------------------
# Emoji mapping for all 28 GoEmotions categories
# ---------------------------------------------------------------------------
EMOJI_MAP = {
    "admiration": ("admiration", "\U0001F929", "#fcd34d"),      # star-struck
    "amusement": ("amusement", "\U0001F602", "#fbbf24"),        # face with tears of joy
    "anger": ("anger", "\U0001F621", "#ef4444"),                # pouting face
    "annoyance": ("annoyance", "\U0001F644", "#fb923c"),        # face with rolling eyes
    "approval": ("approval", "\U0001F44D", "#86efac"),          # thumbs up
    "caring": ("caring", "\U0001F917", "#f9a8d4"),              # hugging face
    "confusion": ("confusion", "\U0001F615", "#c4b5fd"),        # confused face
    "curiosity": ("curiosity", "\U0001F914", "#67e8f9"),        # thinking face
    "desire": ("desire", "\U0001F60D", "#f472b6"),              # heart eyes
    "disappointment": ("disappointment", "\U0001F61E", "#93c5fd"),  # disappointed
    "disapproval": ("disapproval", "\U0001F44E", "#fca5a5"),    # thumbs down
    "disgust": ("disgust", "\U0001F922", "#a3e635"),            # nauseated
    "embarrassment": ("embarrassment", "\U0001F633", "#fda4af"),  # flushed
    "excitement": ("excitement", "\U0001F389", "#fde047"),      # party popper
    "fear": ("fear", "\U0001F628", "#d8b4fe"),                  # fearful
    "gratitude": ("gratitude", "\U0001F64F", "#86efac"),        # folded hands
    "grief": ("grief", "\U0001F622", "#6b7280"),                # crying face
    "joy": ("joy", "\U0001F604", "#facc15"),                    # grinning face
    "love": ("love", "\u2764\uFE0F", "#fb7185"),               # red heart
    "nervousness": ("nervousness", "\U0001F630", "#d8b4fe"),    # anxious face
    "optimism": ("optimism", "\U0001F31F", "#a3e635"),          # glowing star
    "pride": ("pride", "\U0001F451", "#facc15"),                # crown
    "realization": ("realization", "\U0001F4A1", "#7dd3fc"),    # light bulb
    "relief": ("relief", "\U0001F60C", "#6ee7b7"),             # relieved face
    "remorse": ("remorse", "\U0001F614", "#a5b4fc"),           # pensive face
    "sadness": ("sadness", "\U0001F622", "#60a5fa"),           # crying face
    "surprise": ("surprise", "\U0001F632", "#34d399"),         # astonished
    "neutral": ("neutral", "\U0001F610", "#9ca3af"),           # neutral face
}


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def analyze(text):
    if not text or not text.strip():
        return "<p style='color:#9ca3af;text-align:center;font-size:16px;'>Type a sentence above to see its emoji mood translation.</p>"

    results = go_emotions_clf(text, truncation=True)[0]
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    # Show all emotions above threshold, or top 5 if none exceed it
    threshold = 0.08
    active = [r for r in results if r["score"] >= threshold]
    if len(active) < 3:
        active = results[:5]

    # Build emoji row — the big visual payoff
    top_emojis = []
    for r in active[:6]:
        info = EMOJI_MAP.get(r["label"], (r["label"], "\u2753", "#9ca3af"))
        size = max(32, int(80 * r["score"]))  # scale emoji size by confidence
        top_emojis.append(
            f'<span title="{info[0]}: {r["score"]:.0%}" '
            f'style="font-size:{size}px;cursor:default;transition:transform 0.2s;">'
            f'{info[1]}</span>'
        )

    emoji_row = (
        '<div style="text-align:center;margin:20px 0;line-height:1.6;">'
        + " ".join(top_emojis)
        + "</div>"
    )

    # Build detailed bars
    bar_rows = []
    for r in active:
        info = EMOJI_MAP.get(r["label"], (r["label"], "\u2753", "#9ca3af"))
        pct = r["score"] * 100
        bar_rows.append(f"""
        <div style="display:flex;align-items:center;gap:10px;margin:6px 0;">
            <span style="font-size:22px;width:32px;text-align:center;">{info[1]}</span>
            <span style="width:110px;font-size:13px;font-weight:600;color:#374151;">{info[0]}</span>
            <div style="flex:1;background:#e5e7eb;border-radius:6px;height:20px;overflow:hidden;">
                <div style="background:{info[2]};height:100%;width:{pct}%;border-radius:6px;
                            transition:width 0.5s;display:flex;align-items:center;justify-content:flex-end;
                            padding-right:6px;font-size:11px;font-weight:bold;color:#1f2937;">
                    {pct:.0f}%
                </div>
            </div>
        </div>
        """)

    bars_section = (
        '<div style="max-width:500px;margin:0 auto;">'
        + "".join(bar_rows)
        + "</div>"
    )

    # Assemble
    return f"""
    <div style="max-width:600px;margin:0 auto;">
        <div style="text-align:center;margin-bottom:8px;">
            <span style="font-size:13px;color:#6b7280;">The model detected <strong>{len(active)}</strong> emotions in your text:</span>
        </div>
        {emoji_row}
        {bars_section}
    </div>
    """


# ---------------------------------------------------------------------------
# Gradio app
# ---------------------------------------------------------------------------
EXAMPLES = [
    "I can't believe she actually did it — I'm so proud of her!",
    "I'm really nervous about the interview tomorrow.",
    "That's the funniest thing I've seen all week.",
    "I shouldn't have said that. I feel terrible about it.",
    "Wait, what? Since when?!",
    "Thank you so much for helping me with this. It means the world.",
    "I don't really care either way. It's fine.",
    "He smiled, but there was something broken behind his eyes.",
]

with gr.Blocks(
    title="Emoji Mood Translator",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# Emoji Mood Translator")
    gr.Markdown(
        "Type any sentence and see it translated into emojis based on **28 different emotions** "
        "detected by the GoEmotions model. Bigger emojis = stronger signal."
    )

    with gr.Row():
        text_input = gr.Textbox(
            label="What's on your mind?",
            placeholder="Type anything here...",
            lines=2,
            scale=4,
        )
        btn = gr.Button("Translate", variant="primary", scale=1)

    output = gr.HTML()

    gr.Examples(examples=EXAMPLES, inputs=text_input)

    btn.click(fn=analyze, inputs=text_input, outputs=output)
    text_input.submit(fn=analyze, inputs=text_input, outputs=output)

demo.launch()

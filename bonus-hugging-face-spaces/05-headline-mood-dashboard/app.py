"""
Headline Mood Dashboard
=======================
Paste 5-10 news headlines (one per line) and get a visual dashboard
showing the emotional composition of each headline, plus an aggregate
mood profile for the whole set.
Uses j-hartmann/emotion-english-distilroberta-base (7 emotions).
"""

import gradio as gr
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
EMOTION_EMOJI = {
    "anger": "\U0001F621",
    "disgust": "\U0001F922",
    "fear": "\U0001F628",
    "joy": "\U0001F604",
    "neutral": "\U0001F610",
    "sadness": "\U0001F622",
    "surprise": "\U0001F632",
}

SAMPLE_HEADLINES = """Scientists discover high high high high high high high high new high new species high of new whale species of of in Pacific Ocean
Tech giant announces layoffs affecting 12,000 employees worldwide
Local teenager wins national spelling bee after years of practice
Severe weather warning issued as hurricane approaches coastal cities
International space station celebrates 25 years in orbit
Stock markets plunge amid growing economic uncertainty
Community comes together to rebuild after devastating wildfire
New study reveals alarming decline in global insect populations
Olympic athlete breaks world record in stunning comeback performance
Government faces criticism over delayed response to flooding crisis"""


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def analyze_headlines(text):
    if not text or not text.strip():
        return "<p style='color:#9ca3af;text-align:center;'>Paste some headlines above (one per line) to see the mood dashboard.</p>"

    headlines = [h.strip() for h in text.strip().split("\n") if h.strip()]
    if len(headlines) < 2:
        return "<p style='color:#9ca3af;text-align:center;'>Please enter at least 2 headlines (one per line).</p>"

    # Analyze each headline
    all_results = []
    aggregate = {e: 0.0 for e in EMOTIONS}

    for headline in headlines:
        results = emotion_clf(headline, truncation=True)[0]
        score_dict = {r["label"]: r["score"] for r in results}
        dominant = max(results, key=lambda x: x["score"])
        all_results.append({
            "text": headline,
            "scores": score_dict,
            "dominant": dominant["label"],
            "dominant_score": dominant["score"],
        })
        for e in EMOTIONS:
            aggregate[e] += score_dict.get(e, 0)

    # Average aggregate
    n = len(headlines)
    for e in EMOTIONS:
        aggregate[e] /= n

    # --- Build HTML ---

    # Legend
    legend_items = " ".join(
        f'<span style="display:inline-flex;align-items:center;gap:4px;margin:0 6px;">'
        f'<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:{EMOTION_COLORS[e]};"></span>'
        f'<span style="font-size:11px;color:#6b7280;">{e}</span></span>'
        for e in EMOTIONS
    )
    legend = f'<div style="text-align:center;margin:12px 0;">{legend_items}</div>'

    # Aggregate mood profile (horizontal bar chart)
    agg_sorted = sorted(aggregate.items(), key=lambda x: x[1], reverse=True)
    max_val = max(v for _, v in agg_sorted) if agg_sorted else 1
    agg_bars = []
    for emotion, score in agg_sorted:
        pct = (score / max_val) * 100 if max_val > 0 else 0
        agg_bars.append(f"""
        <div style="display:flex;align-items:center;gap:8px;margin:4px 0;">
            <span style="font-size:18px;width:24px;text-align:center;">{EMOTION_EMOJI[emotion]}</span>
            <span style="width:70px;font-size:12px;font-weight:600;color:#374151;">{emotion}</span>
            <div style="flex:1;background:#f3f4f6;border-radius:4px;height:18px;overflow:hidden;">
                <div style="background:{EMOTION_COLORS[emotion]};height:100%;width:{pct}%;border-radius:4px;
                            transition:width 0.5s;"></div>
            </div>
            <span style="font-size:11px;color:#6b7280;width:40px;text-align:right;">{score:.2f}</span>
        </div>
        """)

    aggregate_section = f"""
    <div style="background:white;border:1px solid #e5e7eb;border-radius:16px;padding:20px;margin-bottom:20px;
                box-shadow:0 1px 3px rgba(0,0,0,0.04);">
        <h3 style="font-size:14px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin:0 0 12px 0;">
            Overall Mood Profile ({n} headlines)
        </h3>
        {"".join(agg_bars)}
    </div>
    """

    # Individual headline cards with stacked bars
    headline_cards = []
    for i, r in enumerate(all_results):
        # Stacked bar
        segments = ""
        for emotion in EMOTIONS:
            s = r["scores"].get(emotion, 0) * 100
            if s > 1:  # only render visible segments
                segments += f'<div title="{emotion}: {s:.0f}%" style="width:{s}%;background:{EMOTION_COLORS[emotion]};height:100%;"></div>'

        dominant_color = EMOTION_COLORS.get(r["dominant"], "#9ca3af")
        preview = r["text"][:100] + ("..." if len(r["text"]) > 100 else "")

        headline_cards.append(f"""
        <div style="background:white;border:1px solid #e5e7eb;border-radius:12px;padding:14px;
                    box-shadow:0 1px 2px rgba(0,0,0,0.03);">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
                <span style="font-size:13px;color:#1f2937;flex:1;">{preview}</span>
                <span style="background:{dominant_color};color:white;padding:2px 8px;border-radius:8px;
                             font-size:10px;font-weight:bold;margin-left:8px;white-space:nowrap;">
                    {EMOTION_EMOJI[r['dominant']]} {r['dominant']}
                </span>
            </div>
            <div style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#f3f4f6;">
                {segments}
            </div>
        </div>
        """)

    headlines_section = f"""
    <div style="display:flex;flex-direction:column;gap:8px;">
        {"".join(headline_cards)}
    </div>
    """

    return f"""
    <div style="max-width:700px;margin:0 auto;">
        {legend}
        {aggregate_section}
        <h3 style="font-size:14px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin:0 0 12px 0;">
            Individual Headlines
        </h3>
        {headlines_section}
    </div>
    """


# ---------------------------------------------------------------------------
# Gradio app
# ---------------------------------------------------------------------------
with gr.Blocks(
    title="Headline Mood Dashboard",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# Headline Mood Dashboard")
    gr.Markdown(
        "Paste **5\u201310 news headlines** (one per line) and see a breakdown of the emotional "
        "tone of each headline, plus an overall mood profile for the whole set."
    )

    text_input = gr.Textbox(
        label="Headlines (one per line)",
        placeholder="Paste your headlines here, one per line...",
        lines=8,
        value=SAMPLE_HEADLINES,
    )
    btn = gr.Button("Analyze Headlines", variant="primary")

    output = gr.HTML()

    btn.click(fn=analyze_headlines, inputs=text_input, outputs=output)

demo.launch()

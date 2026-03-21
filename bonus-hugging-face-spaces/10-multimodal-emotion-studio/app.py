"""
Multimodal Emotion Studio — A showcase Hugging Face Space
=========================================================
Chains three HF models in a visual pipeline:
  1. BLIP  (image → caption)
  2. DistilRoBERTa  (text → 7 emotions)
  3. BART-large-MNLI  (text → custom zero-shot labels)

Demonstrates: dark-themed Gradio UI, animated SVG radar chart,
multi-step pipeline visualization, glassmorphism cards, and
rich CSS/JS interactivity — all inside a single app.py.
"""

import gradio as gr
import numpy as np
import math
import torch
from html import escape
from hashlib import md5
from transformers import (
    pipeline,
    BlipProcessor,
    BlipForConditionalGeneration,
)

# ── Model loading (lazy singletons) ────────────────────────────

_blip_proc = _blip_model = _emotion_pipe = _zs_pipe = None


def blip():
    global _blip_proc, _blip_model
    if _blip_proc is None:
        _blip_proc = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        _blip_model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
    return _blip_proc, _blip_model


def emotion_classifier():
    global _emotion_pipe
    if _emotion_pipe is None:
        _emotion_pipe = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None,
        )
    return _emotion_pipe


def zero_shot():
    global _zs_pipe
    if _zs_pipe is None:
        _zs_pipe = pipeline(
            "zero-shot-classification", model="facebook/bart-large-mnli"
        )
    return _zs_pipe


# ── Emotion palette ────────────────────────────────────────────

EMOTIONS = {
    "anger":    {"color": "#ff6b6b", "icon": "🔥"},
    "disgust":  {"color": "#51cf66", "icon": "🤢"},
    "fear":     {"color": "#cc5de8", "icon": "😨"},
    "joy":      {"color": "#fcc419", "icon": "✨"},
    "neutral":  {"color": "#adb5bd", "icon": "😐"},
    "sadness":  {"color": "#339af0", "icon": "💧"},
    "surprise": {"color": "#ff922b", "icon": "⚡"},
}

EMOTION_ORDER = list(EMOTIONS.keys())


# ── SVG radar chart builder ────────────────────────────────────

def build_radar_svg(scores: dict, size=320):
    """
    Generate an animated SVG radar chart for 7 emotions.
    Returns an SVG string.
    """
    cx, cy = size / 2, size / 2
    r = size / 2 - 40
    n = len(EMOTION_ORDER)
    angle_step = 2 * math.pi / n

    # Grid rings
    rings = []
    for level in [0.25, 0.5, 0.75, 1.0]:
        pts = []
        for i in range(n):
            a = -math.pi / 2 + i * angle_step
            pts.append(f"{cx + r * level * math.cos(a):.1f},{cy + r * level * math.sin(a):.1f}")
        rings.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>')

    # Axis lines
    axes = []
    for i in range(n):
        a = -math.pi / 2 + i * angle_step
        x2 = cx + r * math.cos(a)
        y2 = cy + r * math.sin(a)
        axes.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>')

    # Data polygon
    data_pts = []
    dots = []
    for i, e in enumerate(EMOTION_ORDER):
        val = scores.get(e, 0)
        a = -math.pi / 2 + i * angle_step
        px = cx + r * val * math.cos(a)
        py = cy + r * val * math.sin(a)
        data_pts.append(f"{px:.1f},{py:.1f}")
        color = EMOTIONS[e]["color"]
        dots.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{color}" '
            f'stroke="white" stroke-width="2" class="radar-dot">'
            f'<animate attributeName="r" from="0" to="5" dur="0.6s" '
            f'begin="{i * 0.08}s" fill="freeze"/></circle>'
        )

    # Labels
    labels = []
    for i, e in enumerate(EMOTION_ORDER):
        a = -math.pi / 2 + i * angle_step
        lx = cx + (r + 24) * math.cos(a)
        ly = cy + (r + 24) * math.sin(a)
        anchor = "middle"
        if math.cos(a) < -0.3:
            anchor = "end"
        elif math.cos(a) > 0.3:
            anchor = "start"
        val_pct = int(scores.get(e, 0) * 100)
        labels.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" '
            f'dominant-baseline="central" fill="{EMOTIONS[e]["color"]}" '
            f'font-size="12" font-weight="600" font-family="Inter, system-ui, sans-serif">'
            f'{EMOTIONS[e]["icon"]} {e} {val_pct}%</text>'
        )

    poly_pts = " ".join(data_pts)
    data_polygon = (
        f'<polygon points="{poly_pts}" fill="rgba(99,102,241,0.15)" '
        f'stroke="url(#radarGrad)" stroke-width="2.5" stroke-linejoin="round" class="radar-poly">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.8s" fill="freeze"/>'
        f'</polygon>'
    )

    svg = f"""
    <svg viewBox="0 0 {size} {size}" class="radar-svg" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="radarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#818cf8"/>
          <stop offset="100%" stop-color="#c084fc"/>
        </linearGradient>
      </defs>
      {"".join(rings)}
      {"".join(axes)}
      {data_polygon}
      {"".join(dots)}
      {"".join(labels)}
    </svg>
    """
    return svg


# ── Pipeline step indicator builder ────────────────────────────

def build_pipeline_html(steps):
    """
    steps: list of dicts with keys 'name', 'model', 'status', 'detail'
    status: 'done' | 'active' | 'pending'
    """
    cards = []
    for i, s in enumerate(steps):
        status_class = s["status"]
        check = "✓" if s["status"] == "done" else ("⟳" if s["status"] == "active" else "○")
        connector = '<div class="pipe-connector"></div>' if i < len(steps) - 1 else ""
        cards.append(f"""
        <div class="pipe-step {status_class}">
            <div class="pipe-icon">{check}</div>
            <div class="pipe-info">
                <div class="pipe-name">{escape(s['name'])}</div>
                <div class="pipe-model">{escape(s['model'])}</div>
                <div class="pipe-detail">{escape(s.get('detail', ''))}</div>
            </div>
        </div>
        {connector}
        """)
    return f'<div class="pipeline">{"".join(cards)}</div>'


# ── Analysis functions ─────────────────────────────────────────

def analyze_image(image, custom_labels_text):
    """Full pipeline: image → caption → emotions → zero-shot."""
    if image is None:
        return "<p class='placeholder'>Upload an image to start the analysis pipeline.</p>"

    # ── Step 1: BLIP caption ───────────────────────────────────
    proc, model = blip()
    image = image.convert("RGB")
    inputs = proc(image, return_tensors="pt")
    with torch.no_grad():
        ids = model.generate(**inputs, max_new_tokens=60)
    caption = proc.decode(ids[0], skip_special_tokens=True)

    # ── Step 2: 7-emotion classification ───────────────────────
    raw = emotion_classifier()(caption[:512])[0]
    score_map = {r["label"]: r["score"] for r in raw}
    top_emotion = max(score_map, key=score_map.get)
    top_score = score_map[top_emotion]

    # ── Step 3: Zero-shot custom labels ────────────────────────
    custom_labels = [l.strip() for l in custom_labels_text.split(",") if l.strip()]
    zs_results = []
    if custom_labels:
        zs = zero_shot()(
            caption,
            candidate_labels=custom_labels,
            multi_label=True,
            hypothesis_template="This image conveys a feeling of {}.",
        )
        for lbl, sc in zip(zs["labels"], zs["scores"]):
            hue = int(md5(lbl.encode()).hexdigest()[:8], 16) % 360
            zs_results.append({
                "label": lbl,
                "score": sc,
                "color": f"hsl({hue}, 70%, 60%)",
            })

    # ── Build HTML output ──────────────────────────────────────

    # Pipeline tracker
    pipeline_steps = [
        {"name": "Image Captioning", "model": "BLIP", "status": "done",
         "detail": f'"{caption[:80]}"'},
        {"name": "Emotion Detection", "model": "DistilRoBERTa", "status": "done",
         "detail": f"Top: {EMOTIONS[top_emotion]['icon']} {top_emotion} ({top_score:.0%})"},
        {"name": "Zero-Shot Labels", "model": "BART-large-MNLI", "status": "done" if custom_labels else "pending",
         "detail": f"{len(custom_labels)} custom labels" if custom_labels else "Add labels above"},
    ]
    pipeline_html = build_pipeline_html(pipeline_steps)

    # Radar chart
    radar = build_radar_svg(score_map)

    # Hero result
    hero_html = f"""
    <div class="hero-result">
        <div class="hero-emoji">{EMOTIONS[top_emotion]['icon']}</div>
        <div class="hero-label" style="color:{EMOTIONS[top_emotion]['color']}">{top_emotion.upper()}</div>
        <div class="hero-score">{top_score:.0%} confidence</div>
    </div>
    """

    # Caption card
    caption_html = f"""
    <div class="glass-card caption-card">
        <div class="card-header">BLIP Caption</div>
        <div class="card-body">"{escape(caption)}"</div>
    </div>
    """

    # Emotion bars (animated)
    bar_rows = []
    for e in EMOTION_ORDER:
        pct = score_map.get(e, 0) * 100
        color = EMOTIONS[e]["color"]
        icon = EMOTIONS[e]["icon"]
        bar_rows.append(f"""
        <div class="emo-bar-row">
            <span class="emo-icon">{icon}</span>
            <span class="emo-name">{e}</span>
            <div class="emo-track">
                <div class="emo-fill" style="--w:{pct:.1f}%;background:{color}"></div>
            </div>
            <span class="emo-pct">{pct:.1f}%</span>
        </div>
        """)

    bars_html = f'<div class="glass-card"><div class="card-header">Emotion Breakdown</div>{"".join(bar_rows)}</div>'

    # Zero-shot results
    zs_html = ""
    if zs_results:
        zs_rows = []
        for item in zs_results:
            pct = item["score"] * 100
            zs_rows.append(f"""
            <div class="emo-bar-row">
                <span class="emo-name zs-label">{escape(item['label'])}</span>
                <div class="emo-track">
                    <div class="emo-fill" style="--w:{pct:.1f}%;background:{item['color']}"></div>
                </div>
                <span class="emo-pct">{pct:.1f}%</span>
            </div>
            """)
        zs_html = f'<div class="glass-card"><div class="card-header">Zero-Shot Custom Labels</div>{"".join(zs_rows)}</div>'

    # Radar section
    radar_html = f'<div class="glass-card radar-card"><div class="card-header">Emotion Radar</div>{radar}</div>'

    return f"""
    <div class="studio-output">
        {pipeline_html}
        {hero_html}
        <div class="results-grid">
            <div class="results-left">
                {caption_html}
                {bars_html}
                {zs_html}
            </div>
            <div class="results-right">
                {radar_html}
            </div>
        </div>
    </div>
    """


def analyze_text(text, custom_labels_text):
    """Text-only pipeline: text → emotions → zero-shot."""
    if not text or not text.strip():
        return "<p class='placeholder'>Enter text to analyze its emotional content.</p>"

    # ── Step 1: Emotion classification ─────────────────────────
    raw = emotion_classifier()(text[:512])[0]
    score_map = {r["label"]: r["score"] for r in raw}
    top_emotion = max(score_map, key=score_map.get)
    top_score = score_map[top_emotion]

    # ── Step 2: Zero-shot custom labels ────────────────────────
    custom_labels = [l.strip() for l in custom_labels_text.split(",") if l.strip()]
    zs_results = []
    if custom_labels:
        zs = zero_shot()(
            text[:512],
            candidate_labels=custom_labels,
            multi_label=True,
            hypothesis_template="This text expresses {}.",
        )
        for lbl, sc in zip(zs["labels"], zs["scores"]):
            hue = int(md5(lbl.encode()).hexdigest()[:8], 16) % 360
            zs_results.append({
                "label": lbl,
                "score": sc,
                "color": f"hsl({hue}, 70%, 60%)",
            })

    # ── Build pipeline tracker ─────────────────────────────────
    pipeline_steps = [
        {"name": "Text Input", "model": "Direct", "status": "done",
         "detail": f'"{text[:60]}{"..." if len(text) > 60 else ""}"'},
        {"name": "Emotion Detection", "model": "DistilRoBERTa", "status": "done",
         "detail": f"Top: {EMOTIONS[top_emotion]['icon']} {top_emotion} ({top_score:.0%})"},
        {"name": "Zero-Shot Labels", "model": "BART-large-MNLI",
         "status": "done" if custom_labels else "pending",
         "detail": f"{len(custom_labels)} custom labels" if custom_labels else "Add labels above"},
    ]
    pipeline_html = build_pipeline_html(pipeline_steps)
    radar = build_radar_svg(score_map)

    hero_html = f"""
    <div class="hero-result">
        <div class="hero-emoji">{EMOTIONS[top_emotion]['icon']}</div>
        <div class="hero-label" style="color:{EMOTIONS[top_emotion]['color']}">{top_emotion.upper()}</div>
        <div class="hero-score">{top_score:.0%} confidence</div>
    </div>
    """

    # Input echo card
    input_html = f"""
    <div class="glass-card caption-card">
        <div class="card-header">Input Text</div>
        <div class="card-body">"{escape(text[:300])}"</div>
    </div>
    """

    # Emotion bars
    bar_rows = []
    for e in EMOTION_ORDER:
        pct = score_map.get(e, 0) * 100
        bar_rows.append(f"""
        <div class="emo-bar-row">
            <span class="emo-icon">{EMOTIONS[e]['icon']}</span>
            <span class="emo-name">{e}</span>
            <div class="emo-track"><div class="emo-fill" style="--w:{pct:.1f}%;background:{EMOTIONS[e]['color']}"></div></div>
            <span class="emo-pct">{pct:.1f}%</span>
        </div>
        """)
    bars_html = f'<div class="glass-card"><div class="card-header">Emotion Breakdown</div>{"".join(bar_rows)}</div>'

    # Zero-shot
    zs_html = ""
    if zs_results:
        zs_rows = []
        for item in zs_results:
            pct = item["score"] * 100
            zs_rows.append(f"""
            <div class="emo-bar-row">
                <span class="emo-name zs-label">{escape(item['label'])}</span>
                <div class="emo-track"><div class="emo-fill" style="--w:{pct:.1f}%;background:{item['color']}"></div></div>
                <span class="emo-pct">{pct:.1f}%</span>
            </div>
            """)
        zs_html = f'<div class="glass-card"><div class="card-header">Zero-Shot Custom Labels</div>{"".join(zs_rows)}</div>'

    radar_html = f'<div class="glass-card radar-card"><div class="card-header">Emotion Radar</div>{radar}</div>'

    return f"""
    <div class="studio-output">
        {pipeline_html}
        {hero_html}
        <div class="results-grid">
            <div class="results-left">
                {input_html}
                {bars_html}
                {zs_html}
            </div>
            <div class="results-right">
                {radar_html}
            </div>
        </div>
    </div>
    """


# ── Massive CSS theme ──────────────────────────────────────────

CUSTOM_CSS = """
/* ── Dark studio theme ─────────────────────────────────────── */
.gradio-container {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%) !important;
    color: #e0e0e0 !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    min-height: 100vh;
}

/* Header area */
.gr-prose h1, .gr-prose h2, .gr-prose h3 {
    background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 800 !important;
    letter-spacing: -0.02em;
}
.gr-prose p, .gr-prose li {
    color: #a0a0b8 !important;
}

/* Form elements */
.gr-input, .gr-textbox textarea, .gr-box, .gr-panel,
input[type="text"], textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: #e0e0e0 !important;
    border-radius: 12px !important;
}
.gr-input:focus, textarea:focus {
    border-color: rgba(129,140,248,0.5) !important;
    box-shadow: 0 0 0 3px rgba(129,140,248,0.15) !important;
}

/* Labels */
label, .gr-label, span.svelte-1gfkn6j {
    color: #a0a0b8 !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    font-size: 0.75em !important;
    letter-spacing: 0.06em;
}

/* Buttons */
button.primary, .gr-button-primary {
    background: linear-gradient(135deg, #818cf8, #6366f1) !important;
    border: none !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 28px !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.85em !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(99,102,241,0.3) !important;
}
button.primary:hover, .gr-button-primary:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(99,102,241,0.4) !important;
}

/* Tab styling */
.gr-tab-nav button, button.svelte-kqij2n {
    background: transparent !important;
    color: #8888a0 !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-size: 0.8em !important;
    transition: all 0.3s ease !important;
    padding: 10px 20px !important;
}
.gr-tab-nav button.selected, button.svelte-kqij2n.selected {
    color: #818cf8 !important;
    border-bottom-color: #818cf8 !important;
}

/* Panels / blocks */
.gr-block, .gr-box, .gr-group, .gr-form, .block {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 16px !important;
}

/* Image upload area */
.gr-image, .gr-file-upload {
    background: rgba(255,255,255,0.03) !important;
    border: 2px dashed rgba(129,140,248,0.2) !important;
    border-radius: 16px !important;
}

/* ── Output elements ───────────────────────────────────────── */

.placeholder {
    color: #555570;
    text-align: center;
    padding: 60px 30px;
    font-size: 1.05em;
    font-style: italic;
}

/* Pipeline tracker */
.pipeline {
    display: flex;
    align-items: center;
    gap: 0;
    margin-bottom: 24px;
    padding: 16px 20px;
    background: rgba(255,255,255,0.03);
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.06);
    overflow-x: auto;
}
.pipe-step {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 14px;
    border-radius: 10px;
    flex-shrink: 0;
    transition: all 0.3s ease;
}
.pipe-step.done {
    background: rgba(81,207,102,0.08);
    border: 1px solid rgba(81,207,102,0.15);
}
.pipe-step.active {
    background: rgba(129,140,248,0.1);
    border: 1px solid rgba(129,140,248,0.2);
    animation: pulse-border 2s infinite;
}
.pipe-step.pending {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    opacity: 0.5;
}
@keyframes pulse-border {
    0%, 100% { border-color: rgba(129,140,248,0.2); }
    50% { border-color: rgba(129,140,248,0.5); }
}
.pipe-icon {
    font-size: 1.4em;
    width: 28px;
    text-align: center;
}
.pipe-step.done .pipe-icon { color: #51cf66; }
.pipe-step.active .pipe-icon { color: #818cf8; }
.pipe-step.pending .pipe-icon { color: #555; }
.pipe-info { min-width: 0; }
.pipe-name {
    font-weight: 700;
    font-size: 0.82em;
    color: #d0d0e0;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
.pipe-model {
    font-size: 0.72em;
    color: #818cf8;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    margin-top: 2px;
}
.pipe-detail {
    font-size: 0.72em;
    color: #8888a0;
    margin-top: 2px;
    max-width: 180px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.pipe-connector {
    width: 32px;
    height: 2px;
    background: linear-gradient(90deg, rgba(129,140,248,0.3), rgba(192,132,252,0.3));
    flex-shrink: 0;
    margin: 0 4px;
    position: relative;
}
.pipe-connector::after {
    content: "▸";
    position: absolute;
    right: -4px;
    top: -8px;
    color: rgba(192,132,252,0.4);
    font-size: 12px;
}

/* Hero result */
.hero-result {
    text-align: center;
    padding: 28px 20px;
    margin-bottom: 24px;
    background: rgba(255,255,255,0.02);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
}
.hero-result::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(129,140,248,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.hero-emoji {
    font-size: 56px;
    margin-bottom: 8px;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}
.hero-label {
    font-size: 2em;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.hero-score {
    color: #8888a0;
    font-size: 0.9em;
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
}

/* Results grid */
.results-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
@media (max-width: 768px) {
    .results-grid { grid-template-columns: 1fr; }
}

/* Glass cards */
.glass-card {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    transition: border-color 0.3s ease, transform 0.3s ease;
}
.glass-card:hover {
    border-color: rgba(129,140,248,0.2);
    transform: translateY(-2px);
}
.card-header {
    font-size: 0.72em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #818cf8;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.caption-card .card-body {
    font-size: 1.05em;
    color: #c0c0d0;
    font-style: italic;
    line-height: 1.5;
}

/* Emotion bars */
.emo-bar-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0;
    transition: background 0.2s ease;
    border-radius: 8px;
}
.emo-bar-row:hover { background: rgba(255,255,255,0.03); padding-left: 6px; }
.emo-icon { width: 24px; font-size: 16px; text-align: center; flex-shrink: 0; }
.emo-name {
    width: 70px;
    font-weight: 600;
    font-size: 0.82em;
    color: #c0c0d0;
    text-transform: capitalize;
    flex-shrink: 0;
}
.zs-label { width: 90px; }
.emo-track {
    flex: 1;
    height: 8px;
    background: rgba(255,255,255,0.05);
    border-radius: 4px;
    overflow: hidden;
}
.emo-fill {
    height: 100%;
    border-radius: 4px;
    width: 0%;
    animation: bar-grow 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
@keyframes bar-grow {
    to { width: var(--w); }
}
.emo-pct {
    width: 48px;
    text-align: right;
    color: #8888a0;
    font-size: 0.78em;
    font-family: 'JetBrains Mono', monospace;
    flex-shrink: 0;
}

/* Radar chart */
.radar-card {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.radar-svg {
    width: 100%;
    max-width: 320px;
    margin-top: 8px;
}
.radar-poly {
    filter: drop-shadow(0 0 12px rgba(129,140,248,0.3));
}
.radar-dot {
    filter: drop-shadow(0 0 4px rgba(255,255,255,0.3));
}

/* Studio output wrapper */
.studio-output {
    animation: fade-in 0.4s ease-out;
}
@keyframes fade-in {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Footer info */
.footer-info {
    text-align: center;
    padding: 20px;
    color: #555570;
    font-size: 0.75em;
    border-top: 1px solid rgba(255,255,255,0.04);
    margin-top: 24px;
}
.footer-info a { color: #818cf8; text-decoration: none; }
"""


# ── Gradio UI ──────────────────────────────────────────────────

with gr.Blocks(
    title="Multimodal Emotion Studio",
    css=CUSTOM_CSS,
    theme=gr.themes.Base(
        primary_hue=gr.themes.colors.indigo,
        secondary_hue=gr.themes.colors.purple,
        neutral_hue=gr.themes.colors.slate,
        font=gr.themes.GoogleFont("Inter"),
        font_mono=gr.themes.GoogleFont("JetBrains Mono"),
    ),
) as demo:

    gr.Markdown(
        """
        # ✦ Multimodal Emotion Studio
        A three-model pipeline that detects emotions from images or text.
        Watch each AI model light up as your input flows through the chain.
        """
    )

    custom_labels = gr.Textbox(
        label="Custom Zero-Shot Labels",
        value="love, hope, nostalgia, excitement, melancholy, wonder, tension, serenity",
        placeholder="Comma-separated emotion labels for BART zero-shot analysis…",
        info="These custom labels are scored by a separate zero-shot model alongside the 7-emotion classifier."
    )

    with gr.Tabs():

        # ── IMAGE TAB ──────────────────────────────────────────
        with gr.Tab("🖼️  Image Analysis"):
            with gr.Row():
                with gr.Column(scale=1):
                    img_input = gr.Image(type="pil", label="Upload an image")
                    img_btn = gr.Button("Analyze Image", variant="primary", size="lg")
                    gr.Examples(
                        examples=[],
                        inputs=img_input,
                        label="Try an example",
                    )

                with gr.Column(scale=2):
                    img_output = gr.HTML(
                        value="<p class='placeholder'>Upload an image and click Analyze to see the full emotion pipeline in action.</p>"
                    )

            img_btn.click(fn=analyze_image, inputs=[img_input, custom_labels], outputs=img_output)

        # ── TEXT TAB ───────────────────────────────────────────
        with gr.Tab("📝  Text Analysis"):
            with gr.Row():
                with gr.Column(scale=1):
                    text_input = gr.Textbox(
                        label="Enter text",
                        lines=6,
                        placeholder="Type or paste any sentence, paragraph, or passage…",
                    )
                    text_btn = gr.Button("Analyze Text", variant="primary", size="lg")
                    gr.Examples(
                        examples=[
                            ["The sunset painted the sky in shades of gold and lavender, and for the first time in months, she felt truly at peace."],
                            ["He slammed the door and stormed into the rain, his fists clenched, tears mixing with the downpour."],
                            ["The results are in, and while preliminary, they suggest a moderate improvement over the baseline across most metrics."],
                        ],
                        inputs=text_input,
                        label="Try an example",
                    )

                with gr.Column(scale=2):
                    text_output = gr.HTML(
                        value="<p class='placeholder'>Enter some text and click Analyze to see its emotional fingerprint.</p>"
                    )

            text_btn.click(fn=analyze_text, inputs=[text_input, custom_labels], outputs=text_output)

    gr.HTML("""
    <div class="footer-info">
        <strong>Pipeline:</strong> BLIP (captioning) → DistilRoBERTa (7 emotions) → BART-MNLI (zero-shot) &nbsp;|&nbsp;
        Built with <a href="https://gradio.app">Gradio</a> &amp;
        <a href="https://huggingface.co/transformers">🤗 Transformers</a>
    </div>
    """)


if __name__ == "__main__":
    demo.launch()

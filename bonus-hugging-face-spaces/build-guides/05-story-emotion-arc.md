# Build Guide 05: Story Emotion Arc

**Complexity:** Medium — single model, paragraph splitting, time-series visualization
**Memory:** ~1.8GB (one model + torch + matplotlib)
**Gradio 6 concepts introduced:** SVG in templates as alternative to matplotlib, interactive hover via `js_on_load`

---

## What This Space Does

Paste a story, scene, or essay (multiple paragraphs). The app analyzes each paragraph's emotional content and plots an "emotion arc" — a line chart showing how emotions rise and fall through the text.

## Why It's Last

Same model as the Headline Dashboard, but the data transformation is more complex. You're splitting text into paragraphs, tracking 7 emotions over a sequence, and producing either a matplotlib plot or an interactive SVG chart. This teaches you the most about data processing and visualization choices.

## requirements.txt

For the matplotlib version (Phases 1-3):
```
gradio>=6.0
transformers
torch
matplotlib
numpy
```

For the pure HTML/SVG version (Phase 4):
```
gradio>=6.0
transformers
torch
```

> Phase 4 drops matplotlib entirely — one less dependency, less memory.

---

## Phase 1: Paragraph Splitting + Text Emotions

Start by splitting text into paragraphs and showing emotion scores as plain text.

```python
import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
    return _classifier

def split_paragraphs(text):
    """Split on blank lines, filter empties."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paras

def analyze(text):
    if not text.strip():
        return "Paste a multi-paragraph text."

    paras = split_paragraphs(text)
    if len(paras) < 2:
        return "Need at least 2 paragraphs (separated by blank lines)."

    output = ""
    for i, para in enumerate(paras[:15]):
        scores = get_classifier()(para[:512])[0]
        top = max(scores, key=lambda x: x["score"])
        preview = para[:60] + ("..." if len(para) > 60 else "")
        output += f"P{i+1}: [{top['label']}] {preview}\n"

    return output

gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Paste a story or essay", lines=10,
                      placeholder="Paragraph one...\n\nParagraph two...\n\nParagraph three..."),
    outputs="text",
    title="Story Emotion Arc"
).launch()
```

**Deploy.** Paste a story with paragraph breaks (blank lines between paragraphs). You should see each paragraph's dominant emotion.

---

## Phase 2: Matplotlib Line Chart

Add a matplotlib plot showing all 7 emotions tracked across paragraphs.

```python
import gradio as gr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
    return _classifier

EMOTIONS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
COLORS = {
    "anger": "#e74c3c", "disgust": "#27ae60", "fear": "#8e44ad",
    "joy": "#f1c40f", "neutral": "#95a5a6", "sadness": "#3498db",
    "surprise": "#e67e22"
}

def split_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

def analyze(text):
    if not text.strip():
        return None, "Paste a multi-paragraph text."

    paras = split_paragraphs(text)
    if len(paras) < 2:
        return None, "Need at least 2 paragraphs (separated by blank lines)."

    # Collect emotion scores per paragraph
    arc_data = {e: [] for e in EMOTIONS}
    summaries = []
    for i, para in enumerate(paras[:15]):
        scores = get_classifier()(para[:512])[0]
        score_map = {r["label"]: r["score"] for r in scores}
        for e in EMOTIONS:
            arc_data[e].append(score_map.get(e, 0))
        top = max(score_map, key=score_map.get)
        preview = para[:50] + "..."
        summaries.append(f"P{i+1} [{top}]: {preview}")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(1, len(paras[:15]) + 1)
    for e in EMOTIONS:
        ax.plot(x, arc_data[e], marker="o", label=e, color=COLORS[e], linewidth=2)
    ax.set_xlabel("Paragraph")
    ax.set_ylabel("Emotion Score")
    ax.set_title("Emotion Arc")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xticks(x)
    ax.grid(alpha=0.3)
    plt.tight_layout()

    return fig, "\n".join(summaries)

with gr.Blocks(title="Story Emotion Arc") as demo:
    gr.Markdown("## Story Emotion Arc\nPaste a multi-paragraph text to see how emotions change across the narrative.")

    text_input = gr.Textbox(label="Paste a story or essay", lines=10,
                            placeholder="Paragraph one...\n\nParagraph two...\n\nParagraph three...")
    btn = gr.Button("Analyze Arc")

    with gr.Row():
        plot_output = gr.Plot(label="Emotion Arc")
        summary_output = gr.Textbox(label="Paragraph Summary", lines=8)

    btn.click(fn=analyze, inputs=text_input, outputs=[plot_output, summary_output])

    gr.Examples(
        examples=[[
            "The morning sun cast long shadows across the quiet village. Birds sang in the ancient oaks, and the air smelled of fresh bread from the bakery on Main Street. Everything felt peaceful and ordinary.\n\nThen the sirens started. At first, just one — a thin wail from the direction of the harbor. Then another, and another, until the whole sky seemed to vibrate with warning. People stopped in the streets, looking up.\n\nMaria grabbed her daughter's hand and ran. She didn't know where she was running to, only that she had to move. Behind her, she could hear shouting, the crash of something heavy, the unmistakable sound of glass breaking.\n\nThey reached the shelter just as the rain began. Inside, dozens of families huddled together. A baby was crying. An old man was praying quietly. Maria held her daughter close and whispered that everything would be okay.\n\nBy evening, the sirens had stopped. They emerged into a changed world — trees down, windows shattered, but the buildings still standing. Neighbors were already helping each other, passing water bottles, checking on the elderly. Someone had started a fire in a metal drum, and people gathered around it, sharing what food they had.\n\nMaria looked at her daughter, who was watching a group of children playing in the rubble, already turning disaster into adventure. She felt something she hadn't expected: hope."
        ]],
        inputs=text_input
    )

demo.launch()
```

**Deploy.** The line chart shows how each emotion rises and falls across paragraphs. The sample story should show fear/sadness spiking in the middle and joy/surprise at the end.

---

## Phase 3: HTML Summary Cards

Add HTML summary cards alongside the matplotlib plot, showing each paragraph's dominant emotion with a colored badge.

```python
import gradio as gr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
    return _classifier

EMOTIONS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
COLORS = {
    "anger": "#e74c3c", "disgust": "#27ae60", "fear": "#8e44ad",
    "joy": "#f1c40f", "neutral": "#95a5a6", "sadness": "#3498db",
    "surprise": "#e67e22"
}

def split_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

def analyze(text):
    if not text.strip():
        return None, "<p style='color:#999;text-align:center;'>Paste a multi-paragraph text.</p>"

    paras = split_paragraphs(text)
    if len(paras) < 2:
        return None, "<p style='color:#999;'>Need at least 2 paragraphs.</p>"

    arc_data = {e: [] for e in EMOTIONS}
    para_results = []
    for i, para in enumerate(paras[:15]):
        scores = get_classifier()(para[:512])[0]
        score_map = {r["label"]: r["score"] for r in scores}
        for e in EMOTIONS:
            arc_data[e].append(score_map.get(e, 0))
        top = max(score_map, key=score_map.get)
        para_results.append({"index": i + 1, "top": top, "preview": para[:70]})

    # Matplotlib plot
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(1, len(paras[:15]) + 1)
    for e in EMOTIONS:
        ax.plot(x, arc_data[e], marker="o", label=e, color=COLORS[e], linewidth=2)
    ax.set_xlabel("Paragraph")
    ax.set_ylabel("Emotion Score")
    ax.set_title("Emotion Arc")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xticks(x)
    ax.grid(alpha=0.3)
    plt.tight_layout()

    # HTML cards
    cards = ""
    for p in para_results:
        color = COLORS.get(p["top"], "#999")
        cards += f"""
        <div style="display:flex;align-items:center;gap:8px;padding:6px 10px;
                    border-left:3px solid {color};margin:4px 0;background:#fafafa;border-radius:0 6px 6px 0;">
            <span style="font-weight:700;color:#888;width:24px;">P{p["index"]}</span>
            <span style="background:{color};color:white;padding:1px 6px;border-radius:8px;font-size:0.72em;">{p["top"]}</span>
            <span style="font-size:0.85em;color:#555;">{p["preview"]}...</span>
        </div>"""

    return fig, f'<div style="font-family:system-ui;">{cards}</div>'

with gr.Blocks(title="Story Emotion Arc") as demo:
    gr.Markdown("## Story Emotion Arc\nPaste a multi-paragraph text to see how emotions change across the narrative.")

    text_input = gr.Textbox(label="Paste a story or essay", lines=10)
    btn = gr.Button("Analyze Arc")
    plot_output = gr.Plot(label="Emotion Arc")
    summary = gr.HTML(label="Paragraph Breakdown")

    btn.click(fn=analyze, inputs=text_input, outputs=[plot_output, summary])

    gr.Examples(
        examples=[[
            "The morning sun cast long shadows across the quiet village. Birds sang in the ancient oaks, and the air smelled of fresh bread from the bakery. Everything felt peaceful and ordinary.\n\nThen the sirens started. At first just one thin wail from the harbor. Then another, and another, until the whole sky seemed to vibrate with warning. People stopped in the streets, looking up.\n\nMaria grabbed her daughter's hand and ran. Behind her, she could hear shouting, the crash of something heavy, the unmistakable sound of glass breaking.\n\nThey reached the shelter just as the rain began. Inside, dozens of families huddled together. A baby was crying. An old man was praying quietly. Maria held her daughter close.\n\nBy evening the sirens had stopped. They emerged into a changed world — trees down, windows shattered, but buildings still standing. Neighbors were already helping each other, passing water bottles, sharing what food they had.\n\nMaria looked at her daughter, who was watching children playing in the rubble, already turning disaster into adventure. She felt something unexpected: hope."
        ]],
        inputs=text_input
    )

demo.launch()
```

**Deploy.** Line chart plus paragraph cards with colored emotion badges.

---

## Phase 4: Gradio 6 — Pure HTML/SVG Arc (No Matplotlib)

> **New Gradio 6 concept: SVG in templates**
> You can embed SVG directly in `html_template` for lightweight, interactive charts without matplotlib. This eliminates a dependency, reduces memory, and enables hover interactivity via `js_on_load`.

This version replaces matplotlib with pure HTML bars and an SVG-based mini arc chart, and adds hover-to-highlight behavior.

```python
import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
    return _classifier

EMOTIONS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
COLORS = {
    "anger": "#e74c3c", "disgust": "#27ae60", "fear": "#8e44ad",
    "joy": "#f1c40f", "neutral": "#95a5a6", "sadness": "#3498db",
    "surprise": "#e67e22"
}

def split_paragraphs(text):
    return [p.strip() for p in text.split("\n\n") if p.strip()]

def analyze(text):
    if not text.strip():
        return {"status": "empty"}

    paras = split_paragraphs(text)
    if len(paras) < 2:
        return {"status": "error", "msg": "Need at least 2 paragraphs separated by blank lines."}

    paragraphs = []
    for i, para in enumerate(paras[:15]):
        scores = get_classifier()(para[:512])[0]
        score_map = {r["label"]: r["score"] for r in scores}
        top = max(score_map, key=score_map.get)
        paragraphs.append({
            "index": i + 1,
            "top": top,
            "top_color": COLORS.get(top, "#999"),
            "preview": para[:70] + ("..." if len(para) > 70 else ""),
            "scores": {e: round(score_map.get(e, 0) * 100) for e in EMOTIONS},
        })

    # Build SVG polyline data for each emotion
    n = len(paragraphs)
    svg_width = 600
    svg_height = 200
    pad_x = 40
    pad_y = 20
    plot_w = svg_width - 2 * pad_x
    plot_h = svg_height - 2 * pad_y

    lines_svg = []
    dots_svg = []
    for e in EMOTIONS:
        points = []
        for i, p in enumerate(paragraphs):
            x = pad_x + (i / max(n - 1, 1)) * plot_w
            y = pad_y + (1 - p["scores"][e] / 100) * plot_h
            points.append(f"{x:.1f},{y:.1f}")
        pts_str = " ".join(points)
        lines_svg.append(f'<polyline class="arc-line" data-emotion="{e}" '
                         f'points="{pts_str}" fill="none" stroke="{COLORS[e]}" '
                         f'stroke-width="2" opacity="0.7"/>')
        # Dots
        for i, p in enumerate(paragraphs):
            x = pad_x + (i / max(n - 1, 1)) * plot_w
            y = pad_y + (1 - p["scores"][e] / 100) * plot_h
            dots_svg.append(f'<circle class="arc-dot" data-emotion="{e}" data-para="{i+1}" '
                            f'cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{COLORS[e]}" opacity="0.7"/>')

    # X-axis labels
    x_labels = []
    for i in range(n):
        x = pad_x + (i / max(n - 1, 1)) * plot_w
        x_labels.append(f'<text x="{x:.1f}" y="{svg_height - 2}" text-anchor="middle" '
                        f'font-size="11" fill="#888">P{i+1}</text>')

    svg = f"""<svg viewBox="0 0 {svg_width} {svg_height}" class="arc-svg">
        <rect x="{pad_x}" y="{pad_y}" width="{plot_w}" height="{plot_h}"
              fill="none" stroke="#eee" stroke-width="1"/>
        {"".join(lines_svg)}
        {"".join(dots_svg)}
        {"".join(x_labels)}
    </svg>"""

    legend = [{"emotion": e, "color": COLORS[e]} for e in EMOTIONS]

    return {
        "status": "done",
        "svg": svg,
        "legend": legend,
        "paragraphs": paragraphs,
    }

with gr.Blocks(title="Story Emotion Arc") as demo:
    gr.Markdown("## Story Emotion Arc\nPaste a multi-paragraph text to see how emotions rise and fall.")

    text_input = gr.Textbox(label="Paste a story or essay", lines=10,
                            placeholder="Paragraph one...\n\nParagraph two...\n\nParagraph three...")
    btn = gr.Button("Analyze Arc")

    result = gr.HTML(
        value={"status": "empty"},
        html_template="""
            {{#if (eq value.status "done")}}
                <div class="legend">
                    {{#each value.legend}}
                        <span class="legend-item" data-emotion="{{this.emotion}}">
                            <span class="dot" style="background:{{this.color}}"></span>
                            {{this.emotion}}
                        </span>
                    {{/each}}
                </div>

                <div class="chart-area">{{{value.svg}}}</div>

                <div class="para-list">
                    {{#each value.paragraphs}}
                        <div class="para-card" data-para="{{this.index}}">
                            <span class="para-num">P{{this.index}}</span>
                            <span class="para-badge" style="background:{{this.top_color}}">{{this.top}}</span>
                            <span class="para-text">{{this.preview}}</span>
                        </div>
                    {{/each}}
                </div>

            {{else if (eq value.status "error")}}
                <p class="msg">{{value.msg}}</p>
            {{else}}
                <p class="msg">Paste a multi-paragraph text and click Analyze Arc.</p>
            {{/if}}
        """,
        css_template="""
            .legend { display: flex; flex-wrap: wrap; gap: 6px 14px; margin-bottom: 12px; }
            .legend-item {
                display: flex; align-items: center; gap: 5px;
                font-size: 0.82em; cursor: pointer; padding: 2px 4px;
                border-radius: 4px;
            }
            .legend-item:hover { background: #f0f0f0; }
            .legend-item.active { background: #e8e8e8; font-weight: 700; }
            .dot { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
            .chart-area { margin: 8px 0 16px; }
            .arc-svg { width: 100%; max-height: 220px; }
            .arc-line { transition: opacity 0.2s, stroke-width 0.2s; }
            .arc-line.highlight { opacity: 1 !important; stroke-width: 3.5; }
            .arc-line.dimmed { opacity: 0.15 !important; }
            .arc-dot { transition: opacity 0.2s, r 0.2s; }
            .arc-dot.highlight { opacity: 1 !important; r: 5; }
            .arc-dot.dimmed { opacity: 0.1 !important; }
            .para-list { display: flex; flex-direction: column; gap: 4px; }
            .para-card {
                display: flex; align-items: center; gap: 8px;
                padding: 6px 10px; border-radius: 6px; cursor: pointer;
                border-left: 3px solid transparent;
            }
            .para-card:hover { background: #f5f5f5; }
            .para-card.active { background: #f0f0ff; border-left-color: #667eea; }
            .para-num { font-weight: 700; color: #888; width: 24px; font-size: 0.85em; }
            .para-badge {
                color: white; padding: 1px 6px; border-radius: 8px;
                font-size: 0.72em; font-weight: 600;
            }
            .para-text { font-size: 0.85em; color: #555; }
            .msg { color: #aaa; text-align: center; padding: 40px; }
        """,
        js_on_load="""
            // Highlight one emotion when hovering its legend item
            element.addEventListener('mouseover', (e) => {
                const legendItem = e.target.closest('.legend-item');
                if (!legendItem) return;
                const emotion = legendItem.dataset.emotion;
                if (!emotion) return;

                element.querySelectorAll('.arc-line').forEach(line => {
                    line.classList.toggle('highlight', line.dataset.emotion === emotion);
                    line.classList.toggle('dimmed', line.dataset.emotion !== emotion);
                });
                element.querySelectorAll('.arc-dot').forEach(dot => {
                    dot.classList.toggle('highlight', dot.dataset.emotion === emotion);
                    dot.classList.toggle('dimmed', dot.dataset.emotion !== emotion);
                });
            });

            // Reset on mouse leave from legend area
            element.addEventListener('mouseout', (e) => {
                const legendItem = e.target.closest('.legend-item');
                if (!legendItem) return;
                element.querySelectorAll('.arc-line, .arc-dot').forEach(el => {
                    el.classList.remove('highlight', 'dimmed');
                });
            });

            // Highlight paragraph card when hovering dots
            element.addEventListener('mouseover', (e) => {
                if (e.target.classList.contains('arc-dot')) {
                    const para = e.target.dataset.para;
                    element.querySelectorAll('.para-card').forEach(card => {
                        card.classList.toggle('active', card.dataset.para === para);
                    });
                }
            });
            element.addEventListener('mouseout', (e) => {
                if (e.target.classList.contains('arc-dot')) {
                    element.querySelectorAll('.para-card').forEach(card => {
                        card.classList.remove('active');
                    });
                }
            });
        """
    )

    btn.click(fn=analyze, inputs=text_input, outputs=result)

    gr.Examples(
        examples=[[
            "The morning sun cast long shadows across the quiet village. Birds sang in the ancient oaks, and the air smelled of fresh bread. Everything felt peaceful.\n\nThen the sirens started. At first just one thin wail from the harbor, then another and another, until the whole sky vibrated with warning.\n\nMaria grabbed her daughter's hand and ran. Behind her she heard shouting, the crash of something heavy, glass breaking.\n\nThey reached the shelter just as rain began. Inside, families huddled together. A baby cried. An old man prayed quietly. Maria held her daughter close.\n\nBy evening the sirens had stopped. They emerged into a changed world — trees down, windows shattered, but buildings standing. Neighbors helped each other, passing water, sharing food.\n\nMaria watched her daughter playing with other children in the rubble, already turning disaster into adventure. She felt something unexpected: hope."
        ]],
        inputs=text_input
    )

demo.launch()
```

**What's new in Phase 4:**
- **No matplotlib:** The emotion arc is now a pure SVG polyline chart built in Python and embedded in the template via `{{{value.svg}}}` (triple braces = unescaped HTML).
- **Legend hover → line highlight:** Hovering an emotion in the legend highlights that line in the chart and dims all others. Pure CSS transitions handle the animation.
- **Dot hover → card highlight:** Hovering a data point on the chart highlights the corresponding paragraph card below.
- **No extra dependencies:** `requirements.txt` drops `matplotlib` and `numpy`.

---

## What You Learned

| Concept | Where |
|---------|-------|
| Paragraph splitting for sequential analysis | Phase 1+ |
| `gr.Plot` with matplotlib | Phase 2-3 |
| SVG generation in Python | Phase 4 |
| SVG embedded in `html_template` via `{{{...}}}` | Phase 4 |
| Multi-target hover (legend → chart → cards) | Phase 4 |
| Replacing heavy dependencies (matplotlib) with pure HTML/SVG | Phase 4 |

## Memory Notes

- With matplotlib: ~1.8GB total (model + torch + matplotlib + numpy)
- Without matplotlib (Phase 4): ~1.5GB (model + torch only)
- The SVG approach is lighter AND more interactive — win-win
- Lazy loading prevents startup crashes
- `para[:512]` truncates long paragraphs before sending to the model — prevents OOM on very long text

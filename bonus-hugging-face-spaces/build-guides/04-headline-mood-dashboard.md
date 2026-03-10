# Build Guide 04: Headline Mood Dashboard

**Complexity:** Medium — single model, multi-input processing, aggregate + individual visualization
**Memory:** ~1.5GB (one transformer model + torch)
**Gradio 6 concepts introduced:** Event delegation in `js_on_load`, interactive tooltips, complex layouts

---

## What This Space Does

Paste 3-10 news headlines (one per line). The app analyzes each headline's emotional content, shows an aggregate mood profile for the whole set, and individual breakdowns per headline.

## Why It's Fourth

Same single model as earlier Spaces, but now you're processing **multiple inputs** and building **two views** (aggregate + individual). The visualization is more complex: stacked bars, color legends, and hover-reveal details.

## requirements.txt

```
gradio==6.8.0
transformers==4.48.0
torch==2.5.0
```

---

## Phase 1: Single Headline Analysis

Start simple — one headline in, emotions out as text.

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

def analyze(text):
    if not text.strip():
        return "Paste a headline."
    results = get_classifier()(text)[0]
    top = sorted(results, key=lambda x: x["score"], reverse=True)
    return "\n".join(f'{r["label"]}: {r["score"]:.1%}' for r in top)

gr.Interface(fn=analyze, inputs="text", outputs="text",
             title="Headline Emotion").launch()
```

**Deploy.** Type a headline like "Scientists make breakthrough discovery" — you should see 7 emotion scores.

---

## Phase 2: Multiple Headlines

Process several headlines at once. Return a text summary.

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

def analyze(text):
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if len(lines) < 2:
        return "Paste at least 2 headlines, one per line."

    results = []
    for headline in lines[:10]:
        scores = get_classifier()(headline)[0]
        score_map = {r["label"]: r["score"] for r in scores}
        results.append({"headline": headline, "scores": score_map})

    # Aggregate: average each emotion across all headlines
    agg = {e: 0 for e in EMOTIONS}
    for r in results:
        for e in EMOTIONS:
            agg[e] += r["scores"].get(e, 0)
    for e in EMOTIONS:
        agg[e] /= len(results)

    output = "=== AGGREGATE MOOD ===\n"
    for e in sorted(agg, key=agg.get, reverse=True):
        output += f"  {e}: {agg[e]:.1%}\n"
    output += "\n=== PER HEADLINE ===\n"
    for r in results:
        top_e = max(r["scores"], key=r["scores"].get)
        output += f"  [{top_e}] {r['headline'][:60]}\n"

    return output

gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Headlines (one per line)", lines=6,
                      placeholder="Paste 3-10 headlines here..."),
    outputs="text",
    title="Headline Mood Dashboard"
).launch()
```

**Deploy.** Paste several headlines — you should see aggregate emotions and per-headline dominant emotions.

---

## Phase 3: HTML Cards + Aggregate Bar

Switch to HTML output with a color legend, aggregate bar chart, and individual headline cards.

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

EMOTIONS = {
    "anger":    {"color": "#e74c3c", "emoji": "😠"},
    "disgust":  {"color": "#27ae60", "emoji": "🤢"},
    "fear":     {"color": "#8e44ad", "emoji": "😨"},
    "joy":      {"color": "#f1c40f", "emoji": "😊"},
    "neutral":  {"color": "#95a5a6", "emoji": "😐"},
    "sadness":  {"color": "#3498db", "emoji": "😢"},
    "surprise": {"color": "#e67e22", "emoji": "😲"},
}

def analyze(text):
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if len(lines) < 2:
        return "<p style='color:#999;text-align:center;padding:30px;'>Paste at least 2 headlines, one per line.</p>"

    all_results = []
    for headline in lines[:10]:
        scores = get_classifier()(headline)[0]
        score_map = {r["label"]: r["score"] for r in scores}
        all_results.append({"headline": headline, "scores": score_map})

    # Aggregate scores
    agg = {e: 0 for e in EMOTIONS}
    for r in all_results:
        for e in EMOTIONS:
            agg[e] += r["scores"].get(e, 0)
    total = sum(agg.values())

    # Legend
    legend = " ".join(
        f'<span style="display:inline-flex;align-items:center;gap:4px;margin:0 6px;">'
        f'<span style="width:12px;height:12px;border-radius:3px;background:{EMOTIONS[e]["color"]};display:inline-block;"></span>'
        f'<span style="font-size:0.82em;">{e}</span></span>'
        for e in EMOTIONS
    )

    # Aggregate stacked bar
    agg_segs = ""
    for e in EMOTIONS:
        pct = (agg[e] / total * 100) if total > 0 else 0
        agg_segs += f'<div style="width:{pct}%;background:{EMOTIONS[e]["color"]};height:100%;min-width:1px;" title="{e}: {pct:.0f}%"></div>'

    # Individual headline cards
    cards = ""
    for r in all_results:
        top_e = max(r["scores"], key=r["scores"].get)
        info = EMOTIONS.get(top_e, {"color":"#999","emoji":"❓"})
        headline_short = r["headline"][:80]

        # Mini stacked bar for this headline
        h_total = sum(r["scores"].values())
        mini_segs = ""
        for e in EMOTIONS:
            pct = (r["scores"].get(e, 0) / h_total * 100) if h_total > 0 else 0
            mini_segs += f'<div style="width:{pct}%;background:{EMOTIONS[e]["color"]};height:100%;"></div>'

        cards += f"""
        <div style="padding:10px;border:1px solid #eee;border-radius:8px;margin:6px 0;background:#fafafa;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:0.9em;">{headline_short}</span>
                <span style="background:{info["color"]};color:white;padding:2px 8px;border-radius:10px;font-size:0.75em;">{top_e}</span>
            </div>
            <div style="display:flex;height:8px;border-radius:4px;overflow:hidden;margin-top:8px;">{mini_segs}</div>
        </div>"""

    return f"""
    <div style="font-family:system-ui;">
        <div style="margin-bottom:12px;">{legend}</div>
        <h4 style="margin:8px 0 4px;">Overall Mood</h4>
        <div style="display:flex;height:24px;border-radius:6px;overflow:hidden;border:1px solid #ddd;">{agg_segs}</div>
        <h4 style="margin:16px 0 8px;">Individual Headlines</h4>
        {cards}
    </div>"""

gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Headlines (one per line)", lines=8,
                      placeholder="Breaking: Major policy change announced\nLocal team wins championship\nStock market drops 3% in morning trading"),
    outputs=gr.HTML(label="Mood Dashboard"),
    title="Headline Mood Dashboard",
    examples=[[
        "Scientists discover high high new species of whale in Pacific Ocean\nStock market plunges amid global uncertainty\nLocal hero saves child from burning building\nNew study reveals alarming pollution levels\nTech giant announces revolutionary AI breakthrough"
    ]]
).launch()
```

**Deploy.** Color legend at top, aggregate stacked bar, then individual cards with mini stacked bars and dominant emotion badges.

---

## Phase 4: Gradio 6 — `js_on_load` for Interactive Tooltips

> **New Gradio 6 concept: Event delegation in `js_on_load`**
> When you have dynamically rendered content (cards, bars), you can't attach event listeners to elements that don't exist yet. Instead, attach one listener to the parent (`element`) and use event delegation to handle clicks/hovers on child elements. This is both more efficient and works with template re-renders.

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

EMOTIONS = {
    "anger":    {"color": "#e74c3c", "emoji": "😠"},
    "disgust":  {"color": "#27ae60", "emoji": "🤢"},
    "fear":     {"color": "#8e44ad", "emoji": "😨"},
    "joy":      {"color": "#f1c40f", "emoji": "😊"},
    "neutral":  {"color": "#95a5a6", "emoji": "😐"},
    "sadness":  {"color": "#3498db", "emoji": "😢"},
    "surprise": {"color": "#e67e22", "emoji": "😲"},
}

def analyze(text):
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if len(lines) < 2:
        return {"status": "empty"}

    all_results = []
    for headline in lines[:10]:
        scores = get_classifier()(headline)[0]
        score_map = {r["label"]: r["score"] for r in scores}
        top_e = max(score_map, key=score_map.get)
        all_results.append({
            "headline": headline[:80],
            "top": top_e,
            "top_color": EMOTIONS[top_e]["color"],
            "breakdown": " | ".join(f"{e}: {score_map.get(e,0):.0%}" for e in EMOTIONS),
            "segments": [
                {"emotion": e, "color": EMOTIONS[e]["color"],
                 "pct": round(score_map.get(e, 0) / sum(score_map.values()) * 100)}
                for e in EMOTIONS
            ]
        })

    # Aggregate
    agg = {e: 0 for e in EMOTIONS}
    for r in all_results:
        for seg in r["segments"]:
            agg[seg["emotion"]] += seg["pct"]
    total = sum(agg.values()) or 1
    agg_segments = [
        {"emotion": e, "color": EMOTIONS[e]["color"], "pct": round(agg[e] / total * 100)}
        for e in EMOTIONS
    ]

    legend = [{"emotion": e, "color": EMOTIONS[e]["color"], "emoji": EMOTIONS[e]["emoji"]}
              for e in EMOTIONS]

    return {
        "status": "done",
        "legend": legend,
        "aggregate": agg_segments,
        "headlines": all_results,
    }

with gr.Blocks(title="Headline Mood Dashboard") as demo:
    gr.Markdown("## Headline Mood Dashboard\nPaste 3-10 news headlines to visualize their collective emotional tone.")

    text_input = gr.Textbox(label="Headlines (one per line)", lines=8,
                            placeholder="Breaking: Major policy change announced\nLocal team wins championship\nStock market drops amid uncertainty")

    result = gr.HTML(
        value={"status": "empty"},
        html_template="""
            {{#if (eq value.status "done")}}
                <div class="legend">
                    {{#each value.legend}}
                        <span class="legend-item">
                            <span class="dot" style="background:{{this.color}}"></span>
                            {{this.emotion}}
                        </span>
                    {{/each}}
                </div>

                <h4 class="section-title">Overall Mood</h4>
                <div class="stacked-bar agg-bar">
                    {{#each value.aggregate}}
                        <div class="seg" style="width:{{this.pct}}%;background:{{this.color}}"
                             data-tip="{{this.emotion}}: {{this.pct}}%"></div>
                    {{/each}}
                </div>

                <h4 class="section-title">Individual Headlines</h4>
                {{#each value.headlines}}
                    <div class="card" data-breakdown="{{this.breakdown}}">
                        <div class="card-top">
                            <span class="card-text">{{this.headline}}</span>
                            <span class="badge" style="background:{{this.top_color}}">{{this.top}}</span>
                        </div>
                        <div class="stacked-bar mini-bar">
                            {{#each this.segments}}
                                <div class="seg" style="width:{{this.pct}}%;background:{{this.color}}"
                                     data-tip="{{this.emotion}}: {{this.pct}}%"></div>
                            {{/each}}
                        </div>
                        <div class="tooltip-area"></div>
                    </div>
                {{/each}}
            {{else}}
                <p class="empty">Paste at least 2 headlines (one per line) to see their mood profile.</p>
            {{/if}}
        """,
        css_template="""
            .legend { display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 14px; }
            .legend-item { display: flex; align-items: center; gap: 5px; font-size: 0.82em; }
            .dot { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }
            .section-title { margin: 14px 0 6px; font-size: 0.95em; color: #555; }
            .stacked-bar {
                display: flex; border-radius: 6px; overflow: hidden;
                border: 1px solid #e0e0e0;
            }
            .agg-bar { height: 26px; }
            .mini-bar { height: 8px; margin-top: 8px; }
            .seg { min-width: 1px; cursor: pointer; position: relative; }
            .seg:hover { opacity: 0.8; }
            .card {
                padding: 10px 12px; border: 1px solid #eee; border-radius: 8px;
                margin: 6px 0; background: #fafafa; position: relative;
            }
            .card:hover { background: #f5f5f5; }
            .card-top { display: flex; justify-content: space-between; align-items: center; }
            .card-text { font-size: 0.88em; flex: 1; margin-right: 8px; }
            .badge {
                color: white; padding: 2px 8px; border-radius: 10px;
                font-size: 0.72em; font-weight: 600; white-space: nowrap;
            }
            .tooltip-area {
                display: none; font-size: 0.78em; color: #666;
                margin-top: 6px; padding-top: 6px; border-top: 1px solid #eee;
            }
            .card.expanded .tooltip-area { display: block; }
            .empty { color: #aaa; text-align: center; padding: 40px; }
        """,
        js_on_load="""
            // Event delegation: one click handler for all cards
            element.addEventListener('click', (e) => {
                const card = e.target.closest('.card');
                if (!card) return;

                // Toggle breakdown visibility
                card.classList.toggle('expanded');
                const tip = card.querySelector('.tooltip-area');
                if (tip && card.classList.contains('expanded')) {
                    tip.textContent = card.dataset.breakdown || '';
                }
            });

            // Hover tooltips on bar segments (title attribute fallback)
            element.addEventListener('mouseover', (e) => {
                if (e.target.classList.contains('seg') && e.target.dataset.tip) {
                    e.target.title = e.target.dataset.tip;
                }
            });
        """
    )

    text_input.submit(fn=analyze, inputs=text_input, outputs=result)

    gr.Examples(
        examples=[[
            "Scientists discover high new species of whale in Pacific Ocean\nStock market plunges amid global uncertainty\nLocal hero saves child from burning building\nNew study reveals alarming pollution levels\nTech giant announces revolutionary AI breakthrough"
        ]],
        inputs=text_input
    )

demo.launch()
```

**What's new in Phase 4:**
- **Event delegation:** One click listener on `element` handles all cards via `e.target.closest('.card')`. This works even when cards are re-rendered.
- **Click to expand:** Clicking a headline card toggles its full emotion breakdown.
- **Hover on segments:** Hovering over any bar segment shows the emotion name and percentage.
- **Data attributes:** `data-breakdown` and `data-tip` store info in the HTML that JavaScript reads on interaction — no round-trip to Python needed.

---

## What You Learned

| Concept | Where |
|---------|-------|
| Multi-input processing (split + iterate) | Phase 2+ |
| Aggregate vs. individual visualization | Phase 3+ |
| Stacked bar charts in HTML/CSS | Phase 3+ |
| Event delegation in `js_on_load` | Phase 4 |
| Click-to-expand with CSS classes | Phase 4 |
| `data-*` attributes for client-side state | Phase 4 |

## Memory Notes

- Same model as Story Emotion Arc — `j-hartmann/emotion-english-distilroberta-base` (~500MB)
- Processing 10 headlines serially takes ~2-5 seconds (acceptable)
- No matplotlib, no extra dependencies — keeps memory low
- Lazy loading prevents startup crashes

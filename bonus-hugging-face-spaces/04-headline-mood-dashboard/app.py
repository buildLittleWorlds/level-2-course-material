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
        return {"is_done": False}

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
        "is_done": True,
        "legend": legend,
        "aggregate": agg_segments,
        "headlines": all_results,
    }

with gr.Blocks(title="Headline Mood Dashboard") as demo:
    gr.Markdown("## Headline Mood Dashboard\nPaste 3-10 news headlines to visualize their collective emotional tone.")

    text_input = gr.Textbox(label="Headlines (one per line)", lines=8,
                            placeholder="Breaking: Major policy change announced\nLocal team wins championship\nStock market drops amid uncertainty")

    result = gr.HTML(
        value={"is_done": False},
        html_template="""
            {{#if value.is_done}}
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

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

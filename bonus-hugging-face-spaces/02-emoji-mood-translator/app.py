import gradio as gr
from transformers import pipeline

EMOJI_MAP = {
    "admiration": "🤩", "amusement": "😄", "anger": "😠", "annoyance": "😤",
    "approval": "👍", "caring": "🤗", "confusion": "😕", "curiosity": "🤔",
    "desire": "😍", "disappointment": "😞", "disapproval": "👎", "disgust": "🤢",
    "embarrassment": "😳", "excitement": "🎉", "fear": "😨", "gratitude": "🙏",
    "grief": "😭", "joy": "😊", "love": "❤️", "nervousness": "😰",
    "neutral": "😐", "optimism": "🌟", "pride": "🏆", "realization": "💡",
    "relief": "😌", "remorse": "😔", "sadness": "😢", "surprise": "😲",
}

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=None
        )
    return _classifier

def analyze(text):
    if not text.strip():
        return []

    results = get_classifier()(text)[0]
    active = [r for r in results if r["score"] > 0.05]
    if len(active) < 3:
        active = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
    active = sorted(active, key=lambda x: x["score"], reverse=True)[:8]

    # Return structured data — the template handles rendering
    return [
        {
            "emoji": EMOJI_MAP.get(r["label"], "❓"),
            "label": r["label"],
            "pct": round(r["score"] * 100),
        }
        for r in active
    ]

with gr.Blocks(title="Emoji Mood Translator") as demo:
    gr.Markdown("## Emoji Mood Translator\nType anything and see its emotional fingerprint as emojis.")

    text_input = gr.Textbox(label="Type anything", lines=2,
                            placeholder="I can't believe how amazing this turned out!")

    result = gr.HTML(
        value=[],
        html_template="""
            {{#if value.length}}
                <div class="emoji-row">
                    {{#each value}}
                        <span class="emoji" title="{{this.label}}: {{this.pct}}%">{{this.emoji}}</span>
                    {{/each}}
                </div>
                <div class="bars">
                    {{#each value}}
                        <div class="bar-row">
                            <span class="bar-emoji">{{this.emoji}}</span>
                            <span class="bar-label">{{this.label}}</span>
                            <div class="bar-track">
                                <div class="bar-fill" style="width:{{this.pct}}%"></div>
                            </div>
                            <span class="bar-pct">{{this.pct}}%</span>
                        </div>
                    {{/each}}
                </div>
            {{else}}
                <p class="empty">Type something to see its emoji mood.</p>
            {{/if}}
        """,
        css_template="""
            .emoji-row {
                text-align: center; padding: 20px 0;
                letter-spacing: 12px; line-height: 1.6;
            }
            .emoji { font-size: 42px; cursor: default; }
            .emoji:hover { transform: scale(1.3); display: inline-block; }
            .bars { margin-top: 12px; }
            .bar-row {
                display: flex; align-items: center; gap: 8px;
                margin: 5px 0;
            }
            .bar-emoji { width: 24px; text-align: center; }
            .bar-label {
                width: 110px; font-size: 0.85em; color: #555;
            }
            .bar-track {
                flex: 1; background: #f0f0f0; border-radius: 4px;
                height: 18px; overflow: hidden;
            }
            .bar-fill {
                height: 100%; background: linear-gradient(90deg, #667eea, #764ba2);
                border-radius: 4px; transition: width 0.4s ease;
                min-width: 3px;
            }
            .bar-pct {
                width: 36px; font-size: 0.8em; color: #999;
                text-align: right;
            }
            .empty { color: #aaa; text-align: center; padding: 40px; }
        """
    )

    text_input.submit(fn=analyze, inputs=text_input, outputs=result)

    gr.Examples(
        examples=[
            ["I'm so proud of what we accomplished together!"],
            ["This is confusing and frustrating."],
            ["I wonder what would happen if we tried something different."],
        ],
        inputs=text_input
    )

demo.launch()

import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "audio-classification",
            model="superb/wav2vec2-base-superb-er"
        )
    return _classifier

LABEL_MAP = {
    "neu": "Neutral", "hap": "Happy", "sad": "Sad", "ang": "Angry",
    "neutral": "Neutral", "happy": "Happy", "sad": "Sad", "angry": "Angry",
}

EMOTION_STYLE = {
    "Happy":  {"emoji": "😊", "color": "#f1c40f"},
    "Sad":    {"emoji": "😢", "color": "#3498db"},
    "Angry":  {"emoji": "😠", "color": "#e74c3c"},
    "Neutral":{"emoji": "😐", "color": "#95a5a6"},
}

def analyze(audio_path):
    if audio_path is None:
        return {"is_done": False}

    results = get_classifier()(audio_path)
    top = max(results, key=lambda x: x["score"])
    top_label = LABEL_MAP.get(top["label"], top["label"])
    top_style = EMOTION_STYLE.get(top_label, {"emoji": "❓", "color": "#999"})

    emotions = []
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        label = LABEL_MAP.get(r["label"], r["label"])
        style = EMOTION_STYLE.get(label, {"emoji": "❓", "color": "#999"})
        emotions.append({
            "label": label,
            "emoji": style["emoji"],
            "color": style["color"],
            "pct": round(r["score"] * 100),
        })

    return {
        "is_done": True,
        "top_emoji": top_style["emoji"],
        "top_label": top_label,
        "top_color": top_style["color"],
        "emotions": emotions,
    }

with gr.Blocks(title="Audio Emotion Detector") as demo:
    gr.Markdown("## Audio Emotion Detector\nRecord your voice or upload a clip to detect its emotional tone.")

    audio_input = gr.Audio(sources=["upload", "microphone"], type="filepath",
                           label="Record or upload audio")

    result = gr.HTML(
        value={"is_done": False},
        html_template="""
            {{#if value.is_done}}
                <div class="hero">
                    <span class="hero-emoji">{{value.top_emoji}}</span>
                    <div class="hero-label" style="color:{{value.top_color}}">{{value.top_label}}</div>
                </div>
                <div class="bars">
                    {{#each value.emotions}}
                        <div class="bar-row">
                            <span class="emo">{{this.emoji}}</span>
                            <span class="name">{{this.label}}</span>
                            <div class="track">
                                <div class="fill" style="--target-width:{{this.pct}}%; background:{{this.color}}"></div>
                            </div>
                            <span class="pct">{{this.pct}}%</span>
                        </div>
                    {{/each}}
                </div>
            {{else}}
                <p class="empty">Record or upload audio to detect its emotion.</p>
            {{/if}}
        """,
        css_template="""
            .hero { text-align: center; padding: 16px 0; }
            .hero-emoji { font-size: 64px; display: block; }
            .hero-label { font-size: 1.3em; font-weight: 700; margin-top: 6px; }
            .bars { margin-top: 12px; }
            .bar-row {
                display: flex; align-items: center; gap: 8px; margin: 6px 0;
                padding: 4px 0;
            }
            .bar-row:hover { background: #f8f8f8; border-radius: 6px; }
            .emo { width: 28px; font-size: 20px; text-align: center; }
            .name { width: 70px; font-weight: 600; font-size: 0.9em; }
            .track {
                flex: 1; background: #f0f0f0; border-radius: 6px;
                height: 22px; overflow: hidden;
            }
            .fill {
                height: 100%; border-radius: 6px; min-width: 3px;
                width: 0%;
                animation: grow 0.6s ease-out forwards;
            }
            @keyframes grow {
                to { width: var(--target-width); }
            }
            .pct { width: 40px; text-align: right; color: #888; font-size: 0.85em; }
            .empty { color: #aaa; text-align: center; padding: 40px; }
        """,
        js_on_load="""
            // Re-trigger bar animations whenever new results appear
            const observer = new MutationObserver(() => {
                element.querySelectorAll('.fill').forEach(bar => {
                    bar.style.animation = 'none';
                    bar.offsetHeight;  // force reflow
                    bar.style.animation = '';
                });
            });
            observer.observe(element, { childList: true, subtree: true });
        """
    )

    audio_input.change(fn=analyze, inputs=audio_input, outputs=result)

demo.launch()

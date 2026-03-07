import gradio as gr
from transformers import pipeline

# Load a sentiment analysis model (works on free CPU)
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# --- Visual Mood Gauge using gr.HTML ---

GAUGE_HTML = """
<div class="mood-gauge">
  <div class="gauge-title">Mood Reading</div>
  <div class="gauge-track">
    <div class="gauge-fill" style="width: ${value.percent}%; background: ${value.color};"></div>
  </div>
  <div class="gauge-labels">
    <span class="label-neg">NEGATIVE</span>
    <span class="label-pos">POSITIVE</span>
  </div>
  <div class="gauge-result" style="color: ${value.color};">
    <span class="gauge-emoji">${value.emoji}</span>
    <span class="gauge-label">${value.label}</span>
  </div>
  <div class="gauge-confidence">${value.confidence}</div>
  <div class="gauge-hint">${value.hint}</div>
</div>
"""

GAUGE_CSS = """
.mood-gauge {
  font-family: 'Segoe UI', system-ui, sans-serif;
  max-width: 480px;
  margin: 0 auto;
  padding: 28px 24px;
  text-align: center;
}
.gauge-title {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #888;
  margin-bottom: 20px;
}
.gauge-track {
  height: 28px;
  background: #e8e8e8;
  border-radius: 14px;
  overflow: hidden;
  position: relative;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}
.gauge-fill {
  height: 100%;
  border-radius: 14px;
  transition: width 0.8s ease, background 0.8s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.gauge-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;
  font-size: 10px;
  letter-spacing: 1px;
  color: #aaa;
}
.gauge-result {
  margin-top: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}
.gauge-emoji {
  font-size: 48px;
  line-height: 1;
}
.gauge-label {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: 1px;
}
.gauge-confidence {
  margin-top: 8px;
  font-size: 18px;
  color: #666;
}
.gauge-hint {
  margin-top: 16px;
  font-size: 13px;
  color: #999;
  font-style: italic;
  min-height: 20px;
}
"""

GAUGE_JS = """
// Animate the fill bar on load
const fill = element.querySelector('.gauge-fill');
if (fill) {
  const target = fill.style.width;
  fill.style.width = '0%';
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      fill.style.width = target;
    });
  });
}
"""

# Default state (before any analysis)
DEFAULT_STATE = {
    "percent": 50,
    "color": "#ccc",
    "emoji": "...",
    "label": "",
    "confidence": "Paste some text and click Submit",
    "hint": "",
}

def check_mood(text, gauge_state):
    if not text or not text.strip():
        return DEFAULT_STATE

    result = analyzer(text)[0]
    label = result["label"]
    score = result["score"]

    # Map to a 0-100 gauge: 0 = fully negative, 100 = fully positive
    if label == "POSITIVE":
        percent = 50 + (score * 50)
        color = "#2ecc71" if score > 0.9 else "#82c91e"
        emoji = "\U0001f60a" if score > 0.9 else "\U0001f642"
    else:
        percent = 50 - (score * 50)
        color = "#e74c3c" if score > 0.9 else "#e67e22"
        emoji = "\U0001f622" if score > 0.9 else "\U0001f610"

    # Confidence hint for students
    if score > 0.95:
        hint = "The model is very sure about this one."
    elif score > 0.8:
        hint = "Pretty confident, but not 100%. Do you agree?"
    else:
        hint = "The model isn't sure. This text might be ambiguous!"

    return {
        "percent": round(percent),
        "color": color,
        "emoji": emoji,
        "label": label,
        "confidence": f"Confidence: {score:.0%}",
        "hint": hint,
    }

# --- Build the app with gr.Blocks ---

with gr.Blocks(title="Mood Meter") as demo:
    gr.Markdown("# Mood Meter")
    gr.Markdown(
        "Paste any text and this AI will tell you whether it feels **POSITIVE** or **NEGATIVE** "
        "— and how confident it is. Does the model agree with how YOU feel about the text?"
    )

    text_input = gr.Textbox(
        lines=6,
        placeholder="Paste any text here — a song lyric, a diary entry, a text from a friend...",
        label="Your text",
    )

    submit_btn = gr.Button("Check the Mood", variant="primary")

    gauge = gr.HTML(
        value=DEFAULT_STATE,
        html_template=GAUGE_HTML,
        css_template=GAUGE_CSS,
        js_on_load=GAUGE_JS,
    )

    submit_btn.click(fn=check_mood, inputs=[text_input, gauge], outputs=gauge)

    gr.Examples(
        examples=[
            "I can't believe how lucky I am to have friends like you. Every day feels like an adventure and I wouldn't trade it for anything in the world.",
            "I don't know why I even bother anymore. Nothing I do seems to matter and nobody notices when I try my hardest.",
            "Dear future me, I hope you figured it out. I hope you're not still lying awake at 2am wondering if you made the right choice.",
            "Walking into school on the first day felt like stepping onto another planet. Everyone already knew each other and I just stood there holding my backpack straps.",
        ],
        inputs=[text_input],
    )

demo.launch()

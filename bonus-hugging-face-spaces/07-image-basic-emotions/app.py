import gradio as gr
from html import escape
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
import torch

# Image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Ekman 6 basic emotions + neutral
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

EMOTION_COLORS = {
    "anger":    "#ef4444",
    "disgust":  "#a3e635",
    "fear":     "#a855f7",
    "joy":      "#facc15",
    "sadness":  "#3b82f6",
    "surprise": "#fb923c",
    "neutral":  "#94a3b8",
}

def analyze(image):
    if image is None:
        return "<p class='empty'>Upload an image to detect its basic emotions.</p>"

    # Generate caption
    image = image.convert("RGB")
    inputs = blip_processor(image, return_tensors="pt")
    with torch.no_grad():
        caption_ids = blip_model.generate(**inputs, max_new_tokens=50)
    caption = blip_processor.decode(caption_ids[0], skip_special_tokens=True)
    safe_caption = escape(caption)

    # Classify emotions
    results = classifier(caption)[0]
    results.sort(key=lambda x: x["score"], reverse=True)

    top = results[0]
    top_color = EMOTION_COLORS.get(top["label"], "#666")

    bars = []
    for r in results:
        color = EMOTION_COLORS.get(r["label"], "#666")
        pct = r["score"] * 100
        safe_label = escape(r["label"].upper())
        bars.append(f"""
        <div class="bar-row">
            <span class="bar-label">{safe_label}</span>
            <div class="bar-track">
                <div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div>
            </div>
            <span class="bar-pct">{pct:.1f}%</span>
        </div>""")

    return f"""
    <div class="caption-box">
        <div class="caption-label">BLIP sees:</div>
        <div class="caption-text">"{safe_caption}"</div>
    </div>
    <div class="verdict" style="background:{top_color}22;color:{top_color};border:1px solid {top_color}44">
        {escape(top['label'].upper())} ({top['score']*100:.1f}%)
    </div>
    <div class="bars">{"".join(bars)}</div>
    """

with gr.Blocks(title="Image Basic Emotions (Ekman 6)") as demo:
    gr.Markdown("## Image Basic Emotions (Ekman 6)\nUpload an image. BLIP describes it, then a model detects 6 basic emotions + neutral.")

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload an image")
        result = gr.HTML(
            value="<p class='empty'>Your emotion analysis will appear here.</p>",
            css_template="""
                .caption-box {
                    background: #f0f4ff; border-radius: 10px; padding: 14px 18px;
                    margin-bottom: 16px; border: 1px solid #d0d8f0;
                }
                .caption-label { font-size: 0.75em; color: #888; text-transform: uppercase; letter-spacing: 0.05em; }
                .caption-text { font-size: 1.1em; margin-top: 4px; color: #333; }
                .verdict {
                    text-align: center; font-weight: 700; font-size: 1.3em;
                    padding: 10px; border-radius: 8px; margin-bottom: 14px;
                }
                .bars { display: flex; flex-direction: column; gap: 8px; }
                .bar-row { display: flex; align-items: center; gap: 10px; }
                .bar-label { width: 80px; font-weight: 600; font-size: 0.8em; text-align: right; }
                .bar-track {
                    flex: 1; height: 22px; background: #f0f0f0; border-radius: 6px; overflow: hidden;
                }
                .bar-fill { height: 100%; border-radius: 6px; }
                .bar-pct { width: 55px; font-family: monospace; font-size: 0.85em; color: #666; }
                .empty { color: #999; text-align: center; padding: 40px 20px; }
            """
        )

    img_input.change(fn=analyze, inputs=img_input, outputs=result)

demo.launch()

import gradio as gr
from hashlib import md5
from html import escape
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
import torch

# Image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Zero-shot classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

DEFAULT_LABELS = "joy, sadness, anger, fear, love, hope, nostalgia, excitement, calm, anxiety"

def analyze(image, labels_text):
    if image is None:
        return "<p class='empty'>Upload an image to classify its emotions with your own labels.</p>"

    labels = []
    seen = set()
    for raw_label in labels_text.split(","):
        label = raw_label.strip()
        if label and label.lower() not in seen:
            seen.add(label.lower())
            labels.append(label)
    if not labels:
        return "<p class='empty'>Enter at least one emotion label.</p>"

    # Generate caption
    image = image.convert("RGB")
    inputs = blip_processor(image, return_tensors="pt")
    with torch.no_grad():
        caption_ids = blip_model.generate(**inputs, max_new_tokens=50)
    caption = blip_processor.decode(caption_ids[0], skip_special_tokens=True)
    safe_caption = escape(caption)

    # Zero-shot classification
    result = classifier(
        caption,
        candidate_labels=labels,
        multi_label=True,
        hypothesis_template="This image conveys {}."
    )

    bars = []
    for label, score in zip(result["labels"], result["scores"]):
        pct = score * 100
        hue = int(md5(label.encode("utf-8")).hexdigest()[:8], 16) % 360
        color = f"hsl({hue}, 65%, 55%)"
        safe_label = escape(label)
        bars.append(f"""
        <div class="bar-row">
            <span class="bar-label">{safe_label}</span>
            <div class="bar-track">
                <div class="bar-fill" style="width:{pct:.1f}%;background:{color}"></div>
            </div>
            <span class="bar-pct">{pct:.1f}%</span>
        </div>""")

    top = result["labels"][0]
    top_score = result["scores"][0]

    return f"""
    <div class="caption-box">
        <div class="caption-label">BLIP sees:</div>
        <div class="caption-text">"{safe_caption}"</div>
    </div>
    <div class="verdict">
        Best match: <strong>{escape(top)}</strong> ({top_score*100:.1f}%)
    </div>
    <div class="bars">{"".join(bars)}</div>
    """

with gr.Blocks(title="Image Zero-Shot Emotions") as demo:
    gr.Markdown("## Image Zero-Shot Emotions\nUpload an image and define your own emotion labels. BLIP describes the image, then a zero-shot model scores each label.")

    labels_input = gr.Textbox(
        label="Emotion labels (comma-separated)",
        value=DEFAULT_LABELS,
        placeholder="e.g. joy, sadness, anger, fear, love"
    )

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload an image")
        result = gr.HTML(
            value="<p class='empty'>Your zero-shot emotion analysis will appear here.</p>",
            css_template="""
                .caption-box {
                    background: #f0f4ff; border-radius: 10px; padding: 14px 18px;
                    margin-bottom: 16px; border: 1px solid #d0d8f0;
                }
                .caption-label { font-size: 0.75em; color: #888; text-transform: uppercase; letter-spacing: 0.05em; }
                .caption-text { font-size: 1.1em; margin-top: 4px; color: #333; }
                .verdict {
                    text-align: center; font-size: 1.15em; padding: 10px;
                    background: #fafafa; border-radius: 8px; border: 1px solid #eee;
                    margin-bottom: 14px;
                }
                .bars { display: flex; flex-direction: column; gap: 8px; }
                .bar-row { display: flex; align-items: center; gap: 10px; }
                .bar-label { width: 90px; font-weight: 600; font-size: 0.85em; text-align: right; text-transform: capitalize; }
                .bar-track {
                    flex: 1; height: 22px; background: #f0f0f0; border-radius: 6px; overflow: hidden;
                }
                .bar-fill { height: 100%; border-radius: 6px; }
                .bar-pct { width: 55px; font-family: monospace; font-size: 0.85em; color: #666; }
                .empty { color: #999; text-align: center; padding: 40px 20px; }
            """
        )

    img_input.change(fn=analyze, inputs=[img_input, labels_input], outputs=result)
    labels_input.change(fn=analyze, inputs=[img_input, labels_input], outputs=result)

demo.launch()

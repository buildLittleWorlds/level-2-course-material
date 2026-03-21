import gradio as gr
from html import escape
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
import torch

# Image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# GoEmotions 28 categories
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def analyze(image):
    if image is None:
        return "<p class='empty'>Upload an image to detect its emotions across 28 categories.</p>"

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

    # Top 5 emotions shown prominently
    top5 = results[:5]
    rest = results[5:]

    top_cards = []
    for i, r in enumerate(top5):
        pct = r["score"] * 100
        opacity = 0.3 + r["score"] * 0.7
        size = 1.1 if i == 0 else 0.95
        safe_label = escape(r["label"])
        top_cards.append(f"""
        <div class="top-card" style="opacity:{opacity};font-size:{size}em">
            <span class="emotion-name">{safe_label}</span>
            <span class="emotion-score">{pct:.1f}%</span>
        </div>""")

    rest_items = []
    for r in rest:
        pct = r["score"] * 100
        safe_label = escape(r["label"])
        rest_items.append(f"""
        <div class="rest-row">
            <span class="rest-label">{safe_label}</span>
            <div class="rest-track">
                <div class="rest-fill" style="width:{pct:.1f}%"></div>
            </div>
            <span class="rest-pct">{pct:.1f}%</span>
        </div>""")

    return f"""
    <div class="caption-box">
        <div class="caption-label">BLIP sees:</div>
        <div class="caption-text">"{safe_caption}"</div>
    </div>
    <div class="section-label">Top 5 Emotions</div>
    <div class="top-grid">{"".join(top_cards)}</div>
    <details class="rest-section">
        <summary>All 28 emotions</summary>
        <div class="rest-list">{"".join(rest_items)}</div>
    </details>
    """

with gr.Blocks(title="Image 28 Emotions (GoEmotions)") as demo:
    gr.Markdown("## Image 28 Emotions (GoEmotions)\nUpload an image. BLIP describes it, then a model scores 28 fine-grained emotion categories.")

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload an image")
        result = gr.HTML(
            value="<p class='empty'>Your 28-emotion analysis will appear here.</p>",
            css_template="""
                .caption-box {
                    background: #f0f4ff; border-radius: 10px; padding: 14px 18px;
                    margin-bottom: 16px; border: 1px solid #d0d8f0;
                }
                .caption-label { font-size: 0.75em; color: #888; text-transform: uppercase; letter-spacing: 0.05em; }
                .caption-text { font-size: 1.1em; margin-top: 4px; color: #333; }
                .section-label { font-weight: 700; font-size: 0.85em; color: #555; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; }
                .top-grid { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
                .top-card {
                    display: flex; justify-content: space-between; align-items: center;
                    padding: 10px 16px; background: #fafafa; border: 1px solid #eee;
                    border-radius: 8px;
                }
                .emotion-name { font-weight: 600; text-transform: capitalize; }
                .emotion-score { font-family: monospace; color: #666; }
                .rest-section { margin-top: 4px; }
                .rest-section summary {
                    cursor: pointer; font-size: 0.85em; color: #888;
                    padding: 6px 0; user-select: none;
                }
                .rest-list { display: flex; flex-direction: column; gap: 4px; margin-top: 8px; }
                .rest-row { display: flex; align-items: center; gap: 8px; font-size: 0.82em; }
                .rest-label { width: 100px; text-align: right; color: #555; text-transform: capitalize; }
                .rest-track { flex: 1; height: 14px; background: #f0f0f0; border-radius: 4px; overflow: hidden; }
                .rest-fill { height: 100%; background: #a78bfa; border-radius: 4px; }
                .rest-pct { width: 50px; font-family: monospace; color: #999; font-size: 0.9em; }
                .empty { color: #999; text-align: center; padding: 40px 20px; }
            """
        )

    img_input.change(fn=analyze, inputs=img_input, outputs=result)

demo.launch()

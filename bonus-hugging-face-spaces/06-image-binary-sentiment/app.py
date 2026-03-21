import gradio as gr
from html import escape
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
import torch

# Image captioning
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Binary sentiment
sentiment = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def analyze(image):
    if image is None:
        return "<p class='empty'>Upload an image to analyze its emotional sentiment.</p>"

    # Generate caption
    image = image.convert("RGB")
    inputs = blip_processor(image, return_tensors="pt")
    with torch.no_grad():
        caption_ids = blip_model.generate(**inputs, max_new_tokens=50)
    caption = blip_processor.decode(caption_ids[0], skip_special_tokens=True)
    safe_caption = escape(caption)

    # Classify sentiment
    result = sentiment(caption)[0]
    label = result["label"]
    score = result["score"]
    other_label = "NEGATIVE" if label == "POSITIVE" else "POSITIVE"
    other_score = 1 - score

    pos = score if label == "POSITIVE" else other_score
    neg = score if label == "NEGATIVE" else other_score

    pos_color = f"rgba(34,197,94,{0.2 + pos * 0.8})"
    neg_color = f"rgba(239,68,68,{0.2 + neg * 0.8})"

    return f"""
    <div class="caption-box">
        <div class="caption-label">BLIP sees:</div>
        <div class="caption-text">"{safe_caption}"</div>
    </div>
    <div class="result-box">
        <div class="bar-row">
            <span class="bar-label">POSITIVE</span>
            <div class="bar-track">
                <div class="bar-fill" style="width:{pos*100:.1f}%;background:{pos_color}"></div>
            </div>
            <span class="bar-pct">{pos*100:.1f}%</span>
        </div>
        <div class="bar-row">
            <span class="bar-label">NEGATIVE</span>
            <div class="bar-track">
                <div class="bar-fill" style="width:{neg*100:.1f}%;background:{neg_color}"></div>
            </div>
            <span class="bar-pct">{neg*100:.1f}%</span>
        </div>
        <div class="verdict {'pos' if label == 'POSITIVE' else 'neg'}">
            {label} ({score*100:.1f}%)
        </div>
    </div>
    """

with gr.Blocks(title="Image Binary Sentiment") as demo:
    gr.Markdown("## Image Binary Sentiment\nUpload an image. BLIP describes it, then a sentiment model classifies the description as positive or negative.")

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload an image")
        result = gr.HTML(
            value="<p class='empty'>Your sentiment analysis will appear here.</p>",
            css_template="""
                .caption-box {
                    background: #f0f4ff; border-radius: 10px; padding: 14px 18px;
                    margin-bottom: 16px; border: 1px solid #d0d8f0;
                }
                .caption-label { font-size: 0.75em; color: #888; text-transform: uppercase; letter-spacing: 0.05em; }
                .caption-text { font-size: 1.1em; margin-top: 4px; color: #333; }
                .result-box { display: flex; flex-direction: column; gap: 10px; }
                .bar-row { display: flex; align-items: center; gap: 10px; }
                .bar-label { width: 80px; font-weight: 600; font-size: 0.85em; text-align: right; }
                .bar-track {
                    flex: 1; height: 24px; background: #f0f0f0; border-radius: 6px; overflow: hidden;
                }
                .bar-fill { height: 100%; border-radius: 6px; transition: width 0.3s; }
                .bar-pct { width: 55px; font-family: monospace; font-size: 0.85em; color: #666; }
                .verdict {
                    text-align: center; font-weight: 700; font-size: 1.3em;
                    margin-top: 10px; padding: 10px; border-radius: 8px;
                }
                .verdict.pos { background: rgba(34,197,94,0.12); color: #16a34a; }
                .verdict.neg { background: rgba(239,68,68,0.12); color: #dc2626; }
                .empty { color: #999; text-align: center; padding: 40px 20px; }
            """
        )

    img_input.change(fn=analyze, inputs=img_input, outputs=result)

demo.launch()

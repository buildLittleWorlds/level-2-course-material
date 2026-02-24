import gradio as gr
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load BLIP captioning model (~1GB)
print("Loading BLIP captioning model (this takes a moment)...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
print("BLIP loaded!")

# Load sentiment model (~250MB)
print("Loading sentiment model...")
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)
print("All models loaded!")


def analyze_image(image):
    if image is None:
        return "Upload an image first!", "", ""

    # Step 1: Generate caption
    inputs = processor(image, return_tensors="pt")
    out = caption_model.generate(**inputs, max_length=50)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # Step 2: Analyze caption sentiment
    result = sentiment(caption)[0]
    sentiment_text = f"{result['label']} ({result['score']:.1%} confidence)"

    # Step 3: Show the full pipeline
    pipeline_view = (
        f"IMAGE\n"
        f"  -> Model 1 (BLIP captioner): \"{caption}\"\n"
        f"  -> Model 2 (sentiment): {result['label']} ({result['score']:.1%})"
    )

    return caption, sentiment_text, pipeline_view


with gr.Blocks(title="Image Story Pipeline") as demo:
    gr.Markdown(
        "# Image Story Pipeline\n"
        "Upload an image. Model 1 describes it in words. Model 2 reads those "
        "words and judges the tone. Two models, connected — the output of the "
        "first becomes the input of the second."
    )

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload an Image")
            btn = gr.Button("Analyze", variant="primary")
        with gr.Column():
            caption_output = gr.Textbox(
                label="Step 1: Caption (BLIP)", interactive=False
            )
            sentiment_output = gr.Textbox(
                label="Step 2: Sentiment of Caption", interactive=False
            )
            pipeline_output = gr.Textbox(
                label="Full Pipeline View", lines=4, interactive=False
            )

    btn.click(
        fn=analyze_image,
        inputs=image_input,
        outputs=[caption_output, sentiment_output, pipeline_output],
    )

    gr.Markdown(
        "### How to break it\n"
        "Try uploading images that are hard to describe — abstract art, memes, "
        "dark photos. If Model 1 gets the caption wrong, Model 2's analysis is "
        "meaningless. That's an **error cascade**."
    )

demo.launch()

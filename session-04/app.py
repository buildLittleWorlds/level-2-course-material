from transformers import pipeline
import gradio as gr

# Load all 3 sentiment models at startup (sequential to manage memory)
print("Loading Movie Review model...")
model_movie = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

print("Loading Twitter model...")
model_twitter = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
)

print("Loading Product Review model...")
model_product = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
)

print("All models loaded!")


def format_result(result):
    """Format a single model result as 'LABEL (XX% confidence)'."""
    label = result["label"]
    score = result["score"]
    return f"{label} ({score:.0%} confidence)"


def compare_sentiment(text):
    if not text or not text.strip():
        return "Enter some text first!", "Enter some text first!", "Enter some text first!"

    # Truncate to 512 chars (model token limits)
    text = text[:512]

    r1 = model_movie(text)[0]
    r2 = model_twitter(text)[0]
    r3 = model_product(text)[0]

    return format_result(r1), format_result(r2), format_result(r3)


demo = gr.Interface(
    fn=compare_sentiment,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Type or paste text to analyze...",
        label="Text to Analyze",
    ),
    outputs=[
        gr.Textbox(label="Movie Review Model (distilbert-sst2)"),
        gr.Textbox(label="Twitter Model (cardiffnlp)"),
        gr.Textbox(label="Product Review Model (nlptown, 1-5 stars)"),
    ],
    title="Sentiment Showdown",
    description="Three AI models read the same text. Do they agree? Each was trained on different data — movie reviews, tweets, and product reviews — so they see the world differently.",
    examples=[
        ["The service was slow but the food was amazing."],
        ["I can't believe how terrible this is. Just kidding, it's great!"],
        ["The movie was fine. Nothing special but not bad either."],
        ["lol this is SO bad it's actually good 😂"],
        ["The product arrived on time and works as described."],
    ],
)

demo.launch()

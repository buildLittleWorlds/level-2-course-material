import gradio as gr
from transformers import pipeline

# Load the same sentiment model students already know —
# the magic is in how we PRESENT the results, not in swapping models.
analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)


def analyze_review(review):
    """Turn raw sentiment output into advice a restaurant owner can act on."""
    if not review or not review.strip():
        return "Paste a review above to analyze!"

    result = analyzer(review[:512])[0]
    label = result["label"]
    score = result["score"]

    if label == "POSITIVE":
        mood = "Happy Customer 😊"
        if score > 0.95:
            advice = (
                "This customer loved the experience! "
                "Consider thanking them publicly and inviting them back."
            )
        else:
            advice = (
                "This customer had a good experience. "
                "A simple thank-you response goes a long way."
            )
    else:
        mood = "Unhappy Customer 😟"
        if score > 0.95:
            advice = (
                "This customer had a very poor experience. "
                "Reach out personally to understand what went wrong."
            )
        else:
            advice = (
                "This customer had a mixed-to-negative experience. "
                "Consider responding with an apology and an offer to make it right."
            )

    confidence_bar = "█" * int(score * 20) + "░" * (20 - int(score * 20))
    return (
        f"Overall Impression:  {mood}\n"
        f"Confidence: {confidence_bar} {score:.0%}\n"
        f"\nSuggested Action:\n{advice}"
    )


demo = gr.Interface(
    fn=analyze_review,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Paste a restaurant review here...",
        label="Customer Review",
    ),
    outputs=gr.Textbox(label="Analysis", lines=6),
    title="🍽️ Restaurant Review Analyzer",
    description=(
        "Paste a customer review and get instant sentiment analysis. "
        "Built for restaurant owners who want to quickly understand "
        "customer feedback and know how to respond."
    ),
    examples=[
        [
            "The pasta was absolutely divine and the service was impeccable. "
            "Will definitely return!"
        ],
        [
            "Waited 45 minutes for cold food. The waiter was rude and "
            "unapologetic. Never again."
        ],
        [
            "Food was okay, nothing special. Decent portion sizes but "
            "overpriced for what you get."
        ],
        [
            "Great ambiance and the appetizers were fantastic, but the "
            "main course was underwhelming. Dessert saved the meal."
        ],
    ],
)

demo.launch()

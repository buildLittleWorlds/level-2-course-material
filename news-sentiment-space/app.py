import os
import gradio as gr
import requests
from transformers import pipeline

# ── Configuration ────────────────────────────────────────────────────
GNEWS_API_KEY = os.environ.get("GNEWS_API_KEY")
if not GNEWS_API_KEY:
    raise ValueError(
        "GNEWS_API_KEY not found. "
        "Add it as a Secret in your Space settings (Settings → Secrets)."
    )

BASE_URL = "https://gnews.io/api/v4/top-headlines"

# Load the sentiment analysis model (runs once at startup)
# This is a lightweight DistilBERT model fine-tuned for positive/negative sentiment.
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

# GNews uses a "topic" parameter for categories
TOPICS = {
    "Breaking News": "breaking-news",
    "Business": "business",
    "Technology": "technology",
    "Science": "science",
    "Health": "health",
    "Sports": "sports",
    "Entertainment": "entertainment",
    "World": "world",
    "Nation": "nation",
}


def label_to_emoji(label, score):
    """Turn the model's POSITIVE/NEGATIVE label into a readable tag."""
    if label == "POSITIVE":
        return f"Good news ({score:.0%})"
    else:
        return f"Bad news ({score:.0%})"


def fetch_and_analyze(topic_name):
    """Fetch latest news from GNews and run sentiment on each headline."""
    if not topic_name:
        return "Please select a topic."

    topic_code = TOPICS[topic_name]

    params = {
        "token": GNEWS_API_KEY,
        "topic": topic_code,
        "max": 10,
        "lang": "en",
    }

    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return f"Error fetching news: {e}"

    articles = data.get("articles", [])
    if not articles:
        return f"No articles found for **{topic_name}**."

    # Run sentiment analysis on all titles at once (batched for speed)
    titles = [a.get("title", "") for a in articles]
    sentiments = sentiment_analyzer(titles, truncation=True)

    lines = []
    for i, (article, sentiment) in enumerate(zip(articles, sentiments), 1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")
        url = article.get("url", "")
        published = article.get("publishedAt", "")[:10]

        tag = label_to_emoji(sentiment["label"], sentiment["score"])

        # Color the tag: green for good, red for bad
        if sentiment["label"] == "POSITIVE":
            badge = f'<span style="background:#d4edda;color:#155724;padding:2px 8px;border-radius:4px;font-weight:bold">{tag}</span>'
        else:
            badge = f'<span style="background:#f8d7da;color:#721c24;padding:2px 8px;border-radius:4px;font-weight:bold">{tag}</span>'

        lines.append(
            f"### {i}. {title}\n"
            f"{badge}\n\n"
            f"**Source:** {source} · **Date:** {published}\n"
            f"[Read full article]({url})\n"
        )

    return "\n".join(lines)


# ── Gradio UI ────────────────────────────────────────────────────────
with gr.Blocks(title="News Sentiment Analyzer") as demo:
    gr.Markdown("# News Sentiment Analyzer")
    gr.Markdown(
        "Fetches the latest news from the "
        "[GNews API](https://gnews.io) and runs each headline "
        "through a Hugging Face sentiment model to classify it as "
        "**good news** or **bad news**."
    )
    gr.Markdown(
        "*Model: "
        "[distilbert-base-uncased-finetuned-sst-2-english]"
        "(https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) "
        "(DistilBERT fine-tuned on SST-2)*"
    )

    with gr.Row():
        topic = gr.Dropdown(
            choices=list(TOPICS.keys()),
            label="News topic",
            value="Breaking News",
        )
        btn = gr.Button("Fetch & Analyze", variant="primary")

    output = gr.Markdown(label="Results")

    btn.click(fn=fetch_and_analyze, inputs=topic, outputs=output)

demo.launch()

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

# Load the zero-shot classification model (runs once at startup)
# This model can classify text into ANY categories you give it —
# no retraining required. It "understands" language well enough to
# judge whether a text matches a label it has never seen before.
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
)

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

PRESETS = {
    "Good news vs. Bad news": "good news, bad news",
    "Neutral reporting vs. Editorial opinion vs. Clickbait": "neutral reporting, editorial opinion, clickbait",
    "Fear-inducing vs. Reassuring vs. Informational": "fear-inducing, reassuring, informational",
    "Hopeful vs. Worrying vs. Mixed signals": "hopeful, worrying, mixed signals",
    "Celebrating vs. Mourning vs. Warning vs. Explaining": "celebrating, mourning, warning, explaining",
    "Custom (edit the box below)": "",
}


def fetch_and_classify(topic_name, preset_name, custom_categories):
    """Fetch news headlines and classify each one with user-defined categories."""
    if not topic_name:
        return "Please select a news topic."

    # Determine categories
    categories_text = custom_categories.strip() if custom_categories.strip() else PRESETS.get(preset_name, "")
    if not categories_text:
        return "Please enter at least two categories, separated by commas."

    candidate_labels = [c.strip() for c in categories_text.split(",") if c.strip()]
    if len(candidate_labels) < 2:
        return "Please enter at least two categories, separated by commas."

    topic_code = TOPICS[topic_name]
    params = {
        "token": GNEWS_API_KEY,
        "topic": topic_code,
        "max": 8,
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

    lines = []
    for i, article in enumerate(articles, 1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")
        url = article.get("url", "")
        published = article.get("publishedAt", "")[:10]

        # Run zero-shot classification
        result = classifier(title, candidate_labels)

        # Build label badges — top label gets a highlight, rest are dimmed
        badges = []
        for label, score in zip(result["labels"], result["scores"]):
            if label == result["labels"][0]:
                badges.append(
                    f'<span style="background:#fbbf24;color:#1a1a2e;padding:2px 8px;'
                    f'border-radius:4px;font-weight:bold">'
                    f'{label} ({score:.0%})</span>'
                )
            else:
                badges.append(
                    f'<span style="background:rgba(255,255,255,0.1);color:#9ca3af;'
                    f'padding:2px 6px;border-radius:4px">'
                    f'{label} ({score:.0%})</span>'
                )

        badge_line = " ".join(badges)

        lines.append(
            f"### {i}. {title}\n"
            f"{badge_line}\n\n"
            f"**Source:** {source} · **Date:** {published}\n"
            f"[Read full article]({url})\n"
        )

    header = (
        f"**Categories tested:** {', '.join(candidate_labels)}\n\n"
        f"---\n\n"
    )
    return header + "\n".join(lines)


def update_categories(preset_name):
    """When a preset is selected, fill the custom box with its categories."""
    return PRESETS.get(preset_name, "")


# ── Gradio UI ────────────────────────────────────────────────────────
with gr.Blocks(title="Zero-Shot News Analyzer") as demo:
    gr.Markdown("# Zero-Shot News Analyzer")
    gr.Markdown(
        "Fetches live headlines and classifies each one using categories **you define**. "
        "The model ([facebook/bart-large-mnli]"
        "(https://huggingface.co/facebook/bart-large-mnli)) has never been trained "
        "on your categories — it figures them out from language alone.\n\n"
        "Try different categories on the same headlines. "
        "Do the labels match your reading? Where does the model get it wrong?"
    )

    topic_choices = ["Breaking News", "Business", "Technology", "Science",
                      "Health", "Sports", "Entertainment", "World", "Nation"]
    preset_choices = [
        "Good news vs. Bad news",
        "Neutral reporting vs. Editorial opinion vs. Clickbait",
        "Fear-inducing vs. Reassuring vs. Informational",
        "Hopeful vs. Worrying vs. Mixed signals",
        "Celebrating vs. Mourning vs. Warning vs. Explaining",
        "Custom (edit the box below)",
    ]

    with gr.Row():
        topic = gr.Dropdown(
            choices=topic_choices,
            label="News topic",
            value="Breaking News",
            allow_custom_value=False,
        )
        preset = gr.Dropdown(
            choices=preset_choices,
            label="Category preset",
            value="Good news vs. Bad news",
            allow_custom_value=False,
        )

    custom = gr.Textbox(
        label="Categories (comma-separated — edit freely)",
        value="good news, bad news",
        placeholder="e.g., neutral reporting, editorial opinion, clickbait",
    )

    preset.change(fn=update_categories, inputs=preset, outputs=custom)

    btn = gr.Button("Fetch & Classify", variant="primary")
    output = gr.Markdown(label="Results")

    btn.click(fn=fetch_and_classify, inputs=[topic, preset, custom], outputs=output)

demo.launch()

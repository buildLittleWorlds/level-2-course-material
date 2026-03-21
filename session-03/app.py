import os
import gradio as gr
import requests

# ── Configuration ────────────────────────────────────────────────────
GNEWS_API_KEY = os.environ.get("GNEWS_API_KEY")
if not GNEWS_API_KEY:
    raise ValueError(
        "GNEWS_API_KEY not found. "
        "Add it as a Secret in your Space settings (Settings → Secrets)."
    )

BASE_URL = "https://gnews.io/api/v4/top-headlines"

# Country codes GNews supports — ten representative choices
COUNTRIES = {
    "United States": "us",
    "United Kingdom": "gb",
    "Canada": "ca",
    "Australia": "au",
    "India": "in",
    "Germany": "de",
    "France": "fr",
    "Nigeria": "ng",
    "Brazil": "br",
    "China": "cn",
}


def fetch_headlines(country_name):
    """Fetch top headlines for a chosen country from GNews."""
    if not country_name:
        return "Please select a country."

    country_code = COUNTRIES[country_name]

    params = {
        "token": GNEWS_API_KEY,
        "country": country_code,
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
        return f"No headlines found for {country_name}."

    lines = []
    for i, article in enumerate(articles, 1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")
        url = article.get("url", "")
        published = article.get("publishedAt", "")[:10]  # date portion

        lines.append(
            f"### {i}. {title}\n"
            f"**Source:** {source} · **Date:** {published}\n"
            f"[Read full article]({url})\n"
        )

    return "\n".join(lines)


# ── Gradio UI ────────────────────────────────────────────────────────
with gr.Blocks(title="World Headlines") as demo:
    gr.Markdown("# World Headlines")
    gr.Markdown(
        "Pick a country to see its latest English-language headlines, "
        "powered by the [GNews API](https://gnews.io)."
    )

    country = gr.Dropdown(
        choices=list(COUNTRIES.keys()),
        label="Country",
        value="United States",
    )
    btn = gr.Button("Get Headlines", variant="primary")
    output = gr.Markdown(label="Headlines")

    btn.click(fn=fetch_headlines, inputs=country, outputs=output)

demo.launch()

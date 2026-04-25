"""
Session 8 demo: Bias Lens — Headline Edition.

A free-tier Gradio Space that connects to Google's Gemini via an API key
stored in Hugging Face Secrets. The user pastes a news headline; the Space
sends it to Gemini with a structured prompt and asks for a JSON response.

The point of the demo is to show two things at once:
  1. How a free-tier Space gets real LLM power by connecting via API.
  2. Where that connection breaks — when the upstream model returns
     something that doesn't match the JSON contract, the parser fails
     and the downstream fields go empty.

Set GEMINI_API_KEY as a Secret in your Space's Settings tab.
"""

import json
import os

import google.generativeai as genai
import gradio as gr

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not set. Add it as a Secret in your Space's "
        "Settings → Variables and secrets tab."
    )

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT_TEMPLATE = """You are a media analyst. Rate the political bias of this news
headline on a scale from -5 (strong left-leaning framing) to +5 (strong right-leaning
framing), where 0 is neutral. Return ONLY a JSON object with these keys:
  - "score": integer from -5 to 5
  - "label": one of "left", "left-leaning", "neutral", "right-leaning", "right"
  - "rationale": one sentence explaining your reasoning

Headline: {headline}

Return only the JSON. No prose, no markdown fences."""


def analyze(headline):
    if not headline or not headline.strip():
        return "", "", "", "", "Status: waiting for input"

    prompt = PROMPT_TEMPLATE.format(headline=headline.strip())

    try:
        raw = model.generate_content(prompt).text
    except Exception as e:
        return "", "", "", "", f"Status: API call failed — {type(e).__name__}: {e}"

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return (
            "",
            "",
            "",
            raw,
            "Status: PARSE FAILED — the contract between models broke",
        )

    return (
        str(data.get("score", "?")),
        data.get("label", "?"),
        data.get("rationale", ""),
        raw,
        "Status: clean JSON received",
    )


with gr.Blocks(title="Bias Lens — Headline Edition") as demo:
    gr.Markdown(
        "# Bias Lens — Headline Edition\n"
        "Paste a news headline. This Space sends it to Google's Gemini model "
        "(running on Google's servers, not yours) and asks for a structured "
        "bias score. **The Space itself runs on free CPU; the heavy thinking "
        "happens upstream.**"
    )

    with gr.Row():
        with gr.Column():
            headline_input = gr.Textbox(
                label="News headline",
                placeholder="Paste a headline here...",
                lines=2,
            )
            btn = gr.Button("Analyze", variant="primary")
            status_output = gr.Textbox(label="Status", interactive=False)
        with gr.Column():
            score_output = gr.Textbox(
                label="Bias score (-5 to +5)", interactive=False
            )
            label_output = gr.Textbox(label="Bias label", interactive=False)
            rationale_output = gr.Textbox(
                label="One-sentence rationale", interactive=False, lines=2
            )
            raw_output = gr.Textbox(
                label="Raw response from Gemini",
                interactive=False,
                lines=5,
            )

    btn.click(
        fn=analyze,
        inputs=headline_input,
        outputs=[
            score_output,
            label_output,
            rationale_output,
            raw_output,
            status_output,
        ],
    )

    gr.Markdown(
        "### How to break the contract on purpose\n"
        "Try a headline that is sarcastic, very long, in another language, "
        "or that asks Gemini a question. Sometimes the model returns prose "
        "or wraps the JSON in a markdown fence. When that happens, the "
        "score / label / rationale boxes go empty and the raw response "
        "shows what actually came back.\n\n"
        "That gap — where the upstream model said one thing and the "
        "downstream code expected another — is **the contract**. When two "
        "models connect through an API, the contract is where errors live."
    )


demo.launch()

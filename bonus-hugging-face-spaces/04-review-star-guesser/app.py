"""
Review Star Guesser
===================
A guessing game: read a real product review, guess the star rating,
then see if you or the model (nlptown 5-star BERT) was closer.
Tracks your score across rounds.
"""

import gradio as gr
import random
from transformers import pipeline

# ---------------------------------------------------------------------------
# Load model
# ---------------------------------------------------------------------------
print("Loading 5-star sentiment model...")
star_clf = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    device=-1,
)
print("Model loaded.")

# ---------------------------------------------------------------------------
# Built-in review bank (real-style product reviews)
# ---------------------------------------------------------------------------
REVIEWS = [
    {"text": "Absolutely love this product! It exceeded all my expectations. The quality is outstanding and it arrived faster than expected. Would buy again in a heartbeat.", "true_stars": 5},
    {"text": "It works, I guess. Nothing special. Does what it says on the box, but I was hoping for a bit more at this price point.", "true_stars": 3},
    {"text": "Total waste of money. Broke after two days. Customer service was unhelpful and rude. Avoid at all costs.", "true_stars": 1},
    {"text": "Pretty good overall. There are a few minor issues — the color is slightly different from the photos, and the instructions could be clearer — but it does the job well.", "true_stars": 4},
    {"text": "Not terrible, but definitely not worth the price. It feels cheaply made and the packaging was damaged when it arrived. Disappointed.", "true_stars": 2},
    {"text": "This is exactly what I needed. Simple, effective, well-designed. My only complaint is that it doesn't come in more colors.", "true_stars": 4},
    {"text": "I've been using this for three months now and it's held up beautifully. Highly recommend to anyone looking for something reliable.", "true_stars": 5},
    {"text": "Meh. It's okay. I've seen better and I've seen worse. If it was on sale I'd say go for it, but at full price? Probably not.", "true_stars": 3},
    {"text": "The product itself is fine but the shipping was a nightmare. Took three weeks and the box arrived crushed. Two stars for the product, zero for the experience.", "true_stars": 2},
    {"text": "I bought this as a gift and the recipient loved it. The presentation was beautiful and the quality was impressive for the price.", "true_stars": 5},
    {"text": "It stopped working after a week. I followed all the instructions carefully. Very frustrating.", "true_stars": 1},
    {"text": "Good value for the money. It's not luxury quality but for everyday use it's perfectly adequate. Would recommend for budget shoppers.", "true_stars": 4},
    {"text": "The size is way smaller than advertised. I feel deceived. Returning it.", "true_stars": 1},
    {"text": "Decent product with a few quirks. The button is a bit stiff and it makes a weird noise sometimes, but overall it does what I need it to do.", "true_stars": 3},
    {"text": "Five stars isn't enough. This completely changed my morning routine. I tell everyone about it. Best purchase I've made all year.", "true_stars": 5},
]


# ---------------------------------------------------------------------------
# Game logic
# ---------------------------------------------------------------------------
def new_round(state):
    """Pick a new review and reset for a fresh round."""
    if state is None:
        state = {"score_human": 0, "score_model": 0, "rounds": 0, "used": []}

    available = [i for i in range(len(REVIEWS)) if i not in state["used"]]
    if not available:
        state["used"] = []
        available = list(range(len(REVIEWS)))

    idx = random.choice(available)
    state["used"].append(idx)
    state["current"] = idx

    review = REVIEWS[idx]

    review_html = f"""
    <div style="max-width:600px;margin:0 auto;background:white;border:1px solid #e5e7eb;
                border-radius:16px;padding:24px;box-shadow:0 2px 8px rgba(0,0,0,0.04);">
        <div style="font-size:12px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">
            Round {state['rounds'] + 1} &mdash; Read this review:
        </div>
        <p style="font-size:16px;line-height:1.6;color:#1f2937;font-style:italic;">
            &ldquo;{review['text']}&rdquo;
        </p>
        <div style="margin-top:16px;text-align:center;">
            <span style="font-size:14px;color:#6b7280;">How many stars would you give this review?</span>
        </div>
    </div>
    """

    score_html = build_scoreboard(state)

    return review_html, "", score_html, state


def make_guess(guess_str, state):
    """Process the player's guess and reveal the model's prediction."""
    if state is None or "current" not in state:
        return "Start a new round first!", "", build_scoreboard(state), state

    try:
        human_guess = int(guess_str)
        if human_guess < 1 or human_guess > 5:
            raise ValueError
    except (ValueError, TypeError):
        return gr.update(), "Please enter a number from 1 to 5.", gr.update(), state

    review = REVIEWS[state["current"]]
    true_stars = review["true_stars"]

    # Model prediction
    result = star_clf(review["text"], truncation=True)[0]
    model_stars = int(result["label"][0])  # "5 stars" → 5

    # Score: closer to true = 1 point; tie = both get a point
    human_diff = abs(human_guess - true_stars)
    model_diff = abs(model_stars - true_stars)

    state["rounds"] += 1

    if human_diff < model_diff:
        winner = "You"
        state["score_human"] += 1
        winner_color = "#22c55e"
    elif model_diff < human_diff:
        winner = "The Model"
        state["score_model"] += 1
        winner_color = "#3b82f6"
    else:
        winner = "Tie"
        state["score_human"] += 1
        state["score_model"] += 1
        winner_color = "#eab308"

    # Star display helper
    def stars_display(n):
        return '<span style="font-size:24px;letter-spacing:2px;">' + "\u2B50" * n + "\u2606" * (5 - n) + "</span>"

    reveal_html = f"""
    <div style="max-width:600px;margin:0 auto;background:#f9fafb;border:1px solid #e5e7eb;
                border-radius:16px;padding:24px;">
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;text-align:center;">
            <div>
                <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">Your Guess</div>
                <div style="margin:8px 0;">{stars_display(human_guess)}</div>
                <div style="font-size:14px;font-weight:bold;">{human_guess} star{'s' if human_guess != 1 else ''}</div>
                <div style="font-size:12px;color:#6b7280;">Off by {human_diff}</div>
            </div>
            <div>
                <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">Actual Rating</div>
                <div style="margin:8px 0;">{stars_display(true_stars)}</div>
                <div style="font-size:14px;font-weight:bold;">{true_stars} star{'s' if true_stars != 1 else ''}</div>
                <div style="font-size:12px;color:#6b7280;">Ground truth</div>
            </div>
            <div>
                <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">Model's Guess</div>
                <div style="margin:8px 0;">{stars_display(model_stars)}</div>
                <div style="font-size:14px;font-weight:bold;">{model_stars} star{'s' if model_stars != 1 else ''}</div>
                <div style="font-size:12px;color:#6b7280;">Off by {model_diff}</div>
            </div>
        </div>
        <div style="text-align:center;margin-top:20px;">
            <div style="font-size:20px;font-weight:bold;color:{winner_color};">
                {'It\'s a tie!' if winner == 'Tie' else f'{winner} win{"s" if winner != "You" else ""}!'}
            </div>
        </div>
    </div>
    """

    score_html = build_scoreboard(state)

    return reveal_html, "", score_html, state


def build_scoreboard(state):
    if state is None:
        return ""
    h = state.get("score_human", 0)
    m = state.get("score_model", 0)
    r = state.get("rounds", 0)
    return f"""
    <div style="display:flex;justify-content:center;gap:32px;padding:12px;">
        <div style="text-align:center;">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">You</div>
            <div style="font-size:28px;font-weight:bold;color:#22c55e;">{h}</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">Rounds</div>
            <div style="font-size:28px;font-weight:bold;color:#6b7280;">{r}</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:11px;color:#6b7280;text-transform:uppercase;">Model</div>
            <div style="font-size:28px;font-weight:bold;color:#3b82f6;">{m}</div>
        </div>
    </div>
    """


# ---------------------------------------------------------------------------
# Gradio app
# ---------------------------------------------------------------------------
with gr.Blocks(
    title="Review Star Guesser",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# Review Star Guesser")
    gr.Markdown(
        "Read a product review and **guess the star rating** (1\u20135). "
        "Then see if you or the AI model was closer to the real rating. "
        "Can you beat a sentiment model?"
    )

    state = gr.State(value=None)

    scoreboard = gr.HTML()
    review_display = gr.HTML()

    with gr.Row():
        guess_input = gr.Textbox(
            label="Your guess (1\u20135 stars)",
            placeholder="Enter 1, 2, 3, 4, or 5",
            scale=2,
        )
        submit_btn = gr.Button("Submit Guess", variant="primary", scale=1)
        next_btn = gr.Button("Next Review", variant="secondary", scale=1)

    result_display = gr.HTML()

    # Wire events
    next_btn.click(
        fn=new_round,
        inputs=state,
        outputs=[review_display, result_display, scoreboard, state],
    )
    submit_btn.click(
        fn=make_guess,
        inputs=[guess_input, state],
        outputs=[result_display, guess_input, scoreboard, state],
    )
    guess_input.submit(
        fn=make_guess,
        inputs=[guess_input, state],
        outputs=[result_display, guess_input, scoreboard, state],
    )

    # Auto-start first round on load
    demo.load(
        fn=new_round,
        inputs=state,
        outputs=[review_display, result_display, scoreboard, state],
    )

demo.launch()

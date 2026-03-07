"""
QED-Nano Proof Explorer
========================
A Hugging Face Space that lets you feed math problems to QED-Nano,
a tiny 4-billion-parameter model trained to write Olympiad-level proofs.

Built by Dr. Daniel Plate as a demo project for the AI + Research Level 2 course.
Uses the same tools and patterns students learn in Sessions 1-10,
applied to a much more ambitious target: mathematical theorem proving.
"""

import gradio as gr
from huggingface_hub import InferenceClient

# --- Model Setup ---
MODEL_ID = "lm-provers/QED-Nano"
client = InferenceClient(model=MODEL_ID)

# --- Example Problems ---
# Curated from competition mathematics at varying difficulty levels.
# These range from accessible (high-school contest) to hard (Olympiad).

EXAMPLES = {
    "Divisibility (Accessible)": (
        "Prove that for every positive integer n, the number n^3 - n is divisible by 6."
    ),
    "Sum of Squares (Accessible)": (
        "Prove that the sum of the first n positive odd numbers equals n^2."
    ),
    "Pigeonhole Principle (Moderate)": (
        "Prove that among any 5 integers, there exist two whose difference is divisible by 4."
    ),
    "Inequality (Moderate)": (
        "Let a, b, c be positive real numbers. Prove that "
        "(a + b)(b + c)(c + a) >= 8abc."
    ),
    "Number Theory (Challenging)": (
        "Prove that there are infinitely many primes of the form 4k + 3."
    ),
    "Sequence Convergence (Challenging)": (
        "Let a_1 = 1 and a_{n+1} = a_n + 1/a_n for n >= 1. "
        "Prove that a_n > 10 for sufficiently large n."
    ),
    "Combinatorics (Hard — Olympiad)": (
        "Let n >= 2 be an integer. Prove that the number of subsets of "
        "{1, 2, ..., n} that contain no two consecutive integers is equal "
        "to the (n+2)-th Fibonacci number."
    ),
    "Irrationality (Hard — Olympiad)": (
        "Prove that the square root of 2 is irrational."
    ),
}

# --- Proof Evaluation Guide ---
EVALUATION_GUIDE = """
## How to Read a Mathematical Proof

When you read the model's proof attempt, ask yourself:

1. **Does each step follow logically from the previous one?**
   A proof is a chain of reasoning. If any link is broken, the whole chain fails.

2. **Are there any unjustified leaps?**
   Watch for phrases like "it is clear that" or "obviously" — these sometimes hide gaps.

3. **Does the proof actually prove what was asked?**
   Sometimes a proof proves something related but not quite the same thing.

4. **Are the assumptions stated clearly?**
   A good proof starts by establishing what is given and what needs to be shown.

5. **Is the proof complete?**
   Does it handle all cases? Does it reach a definitive conclusion?

### Why This Matters

A mathematical proof IS an argument — the most rigorous kind of argument there is.
Every skill you use to evaluate a proof (checking logic, spotting gaps, testing assumptions)
is the same skill you need to evaluate any argument: in an essay, a debate, a news article,
or an AI-generated claim.

**QED-Nano is a 4-billion-parameter model** — tiny by modern standards. The fact that it
can attempt Olympiad-level proofs at all is remarkable. But it's not perfect. Your job
is to be the judge: does the argument hold up?
"""

ABOUT_TEXT = """
## What Is QED-Nano?

**QED-Nano** is a 4-billion-parameter language model trained specifically to write
mathematical proofs. It was created by researchers at CMU, Hugging Face, ETH Zurich,
and Numina (published February 2026).

### Why It's Remarkable

Most AI models that can prove hard math theorems are enormous — hundreds of billions
of parameters. QED-Nano shows that a *tiny* model, trained with the right recipe, can
approach the performance of models 30-150x its size on Olympiad-level proof problems.

### The Training Recipe

1. **Supervised fine-tuning** — Learn the basics of proof-writing from examples
2. **Reinforcement learning** — Get better through practice and grading feedback
3. **Reasoning cache** — Learn to break long proofs into summarize-and-continue cycles

### What This Means for AI

This is evidence that specialized small models can match generalist giants on hard tasks.
It suggests a future where you don't need a trillion-parameter model to do serious reasoning —
you need the right training approach.

### Connection to This Course

In Level 2, you learned to build Spaces using pre-trained models from the Hub.
This Space does exactly that — but the model it uses does something far more ambitious
than sentiment analysis or text classification. It attempts to *reason* through
mathematical arguments step by step.

**The question is: does it actually reason, or does it just pattern-match convincingly?**
That's what you're here to investigate.
"""


def generate_proof(problem_text, temperature, max_tokens):
    """Send a math problem to QED-Nano and get back a proof attempt."""
    if not problem_text.strip():
        return "Please enter a math problem to prove."

    # Format the prompt for proof generation
    system_message = (
        "You are a mathematical proof assistant. Given a mathematical statement, "
        "write a clear, rigorous proof. Show your reasoning step by step. "
        "Use standard mathematical notation and proof techniques."
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Prove the following:\n\n{problem_text}"},
    ]

    try:
        response = client.chat_completion(
            messages=messages,
            max_tokens=int(max_tokens),
            temperature=temperature,
            top_p=0.95,
        )
        proof_text = response.choices[0].message.content
        return proof_text

    except Exception as e:
        return (
            f"**Error generating proof.** This may mean the model is currently "
            f"unavailable on the Inference API, or the request timed out.\n\n"
            f"Technical details: {str(e)}\n\n"
            f"**Try:** Reducing max tokens, or trying again in a moment."
        )


def load_example(example_name):
    """Load a pre-written example problem."""
    return EXAMPLES.get(example_name, "")


# --- Build the Gradio Interface ---

with gr.Blocks(
    title="QED-Nano Proof Explorer",
    theme=gr.themes.Soft(),
) as demo:

    gr.Markdown(
        "# QED-Nano Proof Explorer\n"
        "*Can a tiny AI model prove hard theorems? Feed it a problem and find out.*"
    )

    with gr.Tabs():
        # --- Tab 1: The Proof Explorer ---
        with gr.TabItem("Explore Proofs"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Choose a Problem")
                    example_dropdown = gr.Dropdown(
                        choices=list(EXAMPLES.keys()),
                        label="Example Problems (or write your own below)",
                        value=None,
                    )
                    problem_input = gr.Textbox(
                        label="Math Problem",
                        placeholder="Enter a mathematical statement to prove...",
                        lines=5,
                    )

                    gr.Markdown("### Model Controls")
                    temperature = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=0.6,
                        step=0.1,
                        label="Temperature",
                        info="Lower = more focused reasoning. Higher = more creative (but riskier).",
                    )
                    max_tokens = gr.Slider(
                        minimum=256,
                        maximum=4096,
                        value=2048,
                        step=256,
                        label="Max Tokens",
                        info="How long the proof attempt can be. Harder problems need more tokens.",
                    )
                    prove_btn = gr.Button("Generate Proof", variant="primary")

                with gr.Column(scale=2):
                    gr.Markdown("### Proof Attempt")
                    proof_output = gr.Markdown(
                        value="*Select an example or type a problem, then click 'Generate Proof'.*"
                    )

            # Wire up the example dropdown
            example_dropdown.change(
                fn=load_example,
                inputs=[example_dropdown],
                outputs=[problem_input],
            )

            # Wire up the prove button
            prove_btn.click(
                fn=generate_proof,
                inputs=[problem_input, temperature, max_tokens],
                outputs=[proof_output],
            )

        # --- Tab 2: How to Evaluate a Proof ---
        with gr.TabItem("How to Evaluate a Proof"):
            gr.Markdown(EVALUATION_GUIDE)

        # --- Tab 3: About QED-Nano ---
        with gr.TabItem("About QED-Nano"):
            gr.Markdown(ABOUT_TEXT)

    gr.Markdown(
        "---\n"
        "*Built by Dr. Daniel Plate as a demo project for the "
        "AI + Research Level 2 course (Youth Horizons Learning). "
        "Model: [lm-provers/QED-Nano](https://huggingface.co/lm-provers/QED-Nano) "
        "(Apache 2.0 License).*"
    )

demo.launch()

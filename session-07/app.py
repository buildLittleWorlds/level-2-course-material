import gradio as gr
from transformers import pipeline

# Load sentiment model (same one from Session 4 — students know it)
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)


def analyze_pair(sentence_a, sentence_b):
    if not sentence_a or not sentence_a.strip():
        return "Enter Sentence A first!", "", ""
    if not sentence_b or not sentence_b.strip():
        return "", "Enter Sentence B first!", ""

    result_a = classifier(sentence_a[:512])[0]
    result_b = classifier(sentence_b[:512])[0]

    output_a = f"{result_a['label']} ({result_a['score']:.1%} confidence)"
    output_b = f"{result_b['label']} ({result_b['score']:.1%} confidence)"

    # Compare results
    if result_a["label"] != result_b["label"]:
        diff = (
            f"Different predictions! Same structure, different result.\n"
            f"  A: {result_a['label']} ({result_a['score']:.1%})\n"
            f"  B: {result_b['label']} ({result_b['score']:.1%})"
        )
    else:
        score_diff = abs(result_a["score"] - result_b["score"])
        if score_diff > 0.05:
            diff = (
                f"Same label ({result_a['label']}), but confidence differs by "
                f"{score_diff:.1%}. The model isn't equally sure about both."
            )
        else:
            diff = f"Similar predictions — both {result_a['label']} with close confidence."

    return output_a, output_b, diff


with gr.Blocks(title="Bias Tester") as demo:
    gr.Markdown(
        "# Bias Tester\n"
        "Type two sentences that are identical except for a name, gender, or "
        "demographic detail. Does the model treat them the same?"
    )

    with gr.Row():
        with gr.Column():
            input_a = gr.Textbox(
                label="Sentence A",
                lines=3,
                placeholder="James is a brilliant surgeon.",
            )
            output_a = gr.Textbox(label="Result A", interactive=False)
        with gr.Column():
            input_b = gr.Textbox(
                label="Sentence B",
                lines=3,
                placeholder="Jamila is a brilliant surgeon.",
            )
            output_b = gr.Textbox(label="Result B", interactive=False)

    diff_output = gr.Textbox(label="Comparison", interactive=False)
    btn = gr.Button("Compare", variant="primary")
    btn.click(
        fn=analyze_pair,
        inputs=[input_a, input_b],
        outputs=[output_a, output_b, diff_output],
    )

    gr.Markdown("### Try these pairs")
    gr.Examples(
        examples=[
            ["James is a brilliant surgeon.", "Jamila is a brilliant surgeon."],
            ["He is a natural leader.", "She is a natural leader."],
            [
                "The young man was passionate about his career.",
                "The young woman was passionate about her career.",
            ],
            [
                "The software engineer solved the problem quickly.",
                "The nurse solved the problem quickly.",
            ],
            [
                "My grandfather always told the best stories.",
                "My grandmother always told the best stories.",
            ],
        ],
        inputs=[input_a, input_b],
    )

demo.launch()

# ========================================
# BIOMEDICAL NER — ENTITY EXTRACTION
# ========================================
# A domain-specific model trained on biomedical text.
# Unlike the general-purpose distilgpt2 (which fails on
# medical text), this model was fine-tuned specifically
# to identify diseases, drugs, symptoms, body parts,
# and procedures in clinical language.
#
# This demonstrates the "specialist" path through domain
# shift: instead of training on everything (Path B),
# train a small model on your specific domain (Path A).
#
# Model: d4data/biomedical-ner-all (DistilBERT, 66M params)
# Task: token-classification (Named Entity Recognition)
# Runs on: Free CPU — no API key, no cost
# ========================================

import gradio as gr
from transformers import pipeline

print("Loading biomedical NER model...")
ner = pipeline(
    "token-classification",
    model="d4data/biomedical-ner-all",
    aggregation_strategy="simple",
)
print("Model loaded!")

# Colors for the most common biomedical entity types
ENTITY_COLORS = {
    "Detailed_description": "#6b7280",
    "Disease_disorder": "#ef4444",
    "Sign_symptom": "#f97316",
    "Medication": "#3b82f6",
    "Drug": "#3b82f6",
    "Chemical": "#3b82f6",
    "Therapeutic_procedure": "#8b5cf6",
    "Diagnostic_procedure": "#a855f7",
    "Biological_structure": "#22c55e",
    "Body_part": "#22c55e",
    "Lab_value": "#eab308",
    "Severity": "#f43f5e",
    "Activity": "#14b8a6",
    "Clinical_event": "#ec4899",
}


def analyze(text):
    if not text or not text.strip():
        return [], []

    results = ner(text)

    # Build highlighted text: list of (text_segment, label_or_None)
    highlighted = []
    last_end = 0

    for entity in results:
        start = entity["start"]
        end = entity["end"]
        label = entity["entity_group"]
        score = entity["score"]

        # Add plain text before this entity
        if start > last_end:
            highlighted.append((text[last_end:start], None))

        # Add the entity with its label
        highlighted.append((text[start:end], label))
        last_end = end

    # Add any remaining text after the last entity
    if last_end < len(text):
        highlighted.append((text[last_end:], None))

    # Build entity table for the dataframe
    table = []
    for entity in results:
        table.append({
            "Entity": entity["word"],
            "Label": entity["entity_group"],
            "Score": round(entity["score"], 2),
        })

    return highlighted, table


with gr.Blocks(title="Biomedical NER — Entity Extraction") as demo:
    gr.Markdown("# Biomedical NER — Entity Extraction")
    gr.Markdown(
        "This model reads medical text and labels every disease, drug, symptom, "
        "and body part it finds. **66M parameters, free CPU, no API key.** "
        "Trained specifically on biomedical text — a specialist, not a generalist."
    )

    text_input = gr.Textbox(
        lines=6,
        label="Paste medical text here",
        placeholder="e.g., Patient presents with acute onset of substernal chest pain...",
    )

    btn = gr.Button("Run NER", variant="primary")

    gr.Markdown("### Highlighted Entities")
    highlighted_output = gr.HighlightedText(
        label="Entities found in text",
        color_map=ENTITY_COLORS,
        show_legend=True,
    )

    gr.Markdown("### Entity Table")
    table_output = gr.Dataframe(
        headers=["Entity", "Label", "Score"],
        label="All entities detected",
    )

    btn.click(
        fn=analyze,
        inputs=text_input,
        outputs=[highlighted_output, table_output],
    )

    gr.Examples(
        examples=[
            ["Patient presents with acute onset of substernal chest pain radiating to the left arm. ECG shows ST-elevation in leads II, III, and aVF. Started on aspirin and heparin drip. Cardiology consult requested."],
            ["The patient has a headache, fever, and sore throat. She was prescribed ibuprofen and amoxicillin."],
            ["The warrior stepped into the dungeon and drew his sword."],
        ],
        inputs=text_input,
    )

    gr.Markdown(
        "*This model identifies biomedical terms in text. "
        "It does not provide medical advice, diagnosis, or treatment.*"
    )

demo.launch()

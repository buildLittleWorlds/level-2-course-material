import gradio as gr
from transformers import pipeline
import re

# Load the same sentiment model from Session 1
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def clean_text(text):
    """
    Clean up messy input before sending it to the model.
    Each step fixes a specific kind of noise — especially tone-related noise.
    """
    # 1. Strip leading/trailing whitespace
    text = text.strip()

    # 2. Collapse multiple spaces into one
    text = re.sub(r' {2,}', ' ', text)

    # 3. Limit repeated characters (e.g., "sooooo" -> "soo")
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    # 4. Remove emoji (the model doesn't know what they mean)
    text = re.sub(
        r'[\U0001F600-\U0001F64F'
        r'\U0001F300-\U0001F5FF'
        r'\U0001F680-\U0001F6FF'
        r'\U0001F1E0-\U0001F1FF'
        r'\U00002702-\U000027B0'
        r'\U0000FE00-\U0000FE0F'
        r'\U0001F900-\U0001F9FF'
        r'\U0001FA00-\U0001FA6F'
        r'\U0001FA70-\U0001FAFF'
        r'\U00002600-\U000026FF]+',
        ' ', text
    )

    # 5. Normalize ALL CAPS to Title Case (if more than 3 words are all caps)
    words = text.split()
    caps_count = sum(1 for w in words if w.isupper() and len(w) > 1)
    if caps_count > 3:
        text = text.title()

    # 6. Flag common sarcasm patterns (add a note, don't remove them)
    # This doesn't "fix" sarcasm — it just shows the model can't handle it
    sarcasm_markers = ["oh great", "just what i needed", "how wonderful", "yeah right", "sure jan"]
    text_lower = text.lower()
    has_sarcasm = any(marker in text_lower for marker in sarcasm_markers)

    # Clean up any extra spaces introduced by cleaning
    text = re.sub(r' {2,}', ' ', text).strip()

    return text, has_sarcasm

def check_mood_with_cleaning(text):
    if not text or not text.strip():
        return "Paste some text above first!"

    original = text.strip()
    cleaned, has_sarcasm = clean_text(text)

    # Run model on both versions
    result_original = analyzer(original)[0]
    result_cleaned = analyzer(cleaned)[0]

    label_orig = result_original["label"]
    score_orig = result_original["score"]
    label_clean = result_cleaned["label"]
    score_clean = result_cleaned["score"]

    emoji_orig = "😊" if label_orig == "POSITIVE" else "😢"
    emoji_clean = "😊" if label_clean == "POSITIVE" else "😢"

    output = f"BEFORE CLEANING:\n{emoji_orig} {label_orig} ({score_orig:.0%})\n"
    output += f"Input: \"{original}\"\n\n"
    output += f"AFTER CLEANING:\n{emoji_clean} {label_clean} ({score_clean:.0%})\n"
    output += f"Input: \"{cleaned}\"\n"

    if original != cleaned:
        output += "\n--- Changes made by clean_text() ---"
        if has_sarcasm:
            output += "\n⚠️ Possible sarcasm detected (but the model can't understand it)"
    else:
        output += "\n--- No cleaning needed ---"

    if label_orig != label_clean:
        output += "\n\n🔄 Cleaning changed the model's mind!"
    elif has_sarcasm:
        output += "\n\n🤔 Cleaning couldn't fix this — tone is in the meaning, not the formatting."

    return output

demo = gr.Interface(
    fn=check_mood_with_cleaning,
    inputs=gr.Textbox(lines=8, placeholder="Paste sarcastic, ironic, or confusing text here..."),
    outputs=gr.Textbox(label="Before vs. After Cleaning", lines=12),
    title="Sarcasm Breaker",
    description="Feed the Mood Meter sarcasm, irony, passive aggression, and mixed signals. See how cleaning the input changes (or doesn't change) the model's reading. What can data cleaning fix — and what's beyond its reach?",
    examples=[
        ["Oh GREAT, another Monday. Just what I needed. 😂😂😂"],
        ["I suppose getting into Harvard is okay. Not a big deal or anything."],
        ["Per my last email, as I mentioned before, I'm happy to clarify AGAIN."],
        ["no literally I'm deceased this is the funniest thing 💀💀💀 i can't breathe"],
        ["I'm fine. Everything is fine. This is fine."],
        ["Worst day ever 😂🎉💀 but honestly who cares anymore lolllll"],
    ],
)

demo.launch()

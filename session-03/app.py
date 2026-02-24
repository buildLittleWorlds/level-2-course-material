import gradio as gr
from transformers import pipeline
import re

# Load the same zero-shot model from Session 1
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")


def clean_text(text):
    """
    Clean up messy input before sending it to the model.
    Each step fixes a specific kind of noise.
    """
    # 1. Strip leading/trailing whitespace
    text = text.strip()

    # 2. Collapse multiple spaces into one
    text = re.sub(r' {2,}', ' ', text)

    # 3. Limit repeated characters (e.g., "sooooo" → "soo")
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    # 4. Expand common abbreviations
    abbreviations = {
        "Rep.": "Representative",
        "Dr.": "Doctor",
        "Mr.": "Mister",
        "Mrs.": "Missus",
        "Ms.": "Ms",
        "Jr.": "Junior",
        "Sr.": "Senior",
        "Prof.": "Professor",
        "Gov.": "Governor",
        "Sen.": "Senator",
        "Gen.": "General",
        "St.": "Saint",
    }
    for abbr, full in abbreviations.items():
        text = text.replace(abbr, full)

    # 5. Remove emoji (covers most common emoji ranges)
    text = re.sub(
        r'[\U0001F600-\U0001F64F'   # emoticons
        r'\U0001F300-\U0001F5FF'     # symbols & pictographs
        r'\U0001F680-\U0001F6FF'     # transport & map
        r'\U0001F1E0-\U0001F1FF'     # flags
        r'\U00002702-\U000027B0'     # dingbats
        r'\U0000FE00-\U0000FE0F'     # variation selectors
        r'\U0001F900-\U0001F9FF'     # supplemental symbols
        r'\U0001FA00-\U0001FA6F'     # chess symbols
        r'\U0001FA70-\U0001FAFF'     # symbols extended-A
        r'\U00002600-\U000026FF]+',  # misc symbols
        ' ', text
    )

    # 6. Normalize ALL CAPS to Title Case (if more than 3 words are all caps)
    words = text.split()
    caps_count = sum(1 for w in words if w.isupper() and len(w) > 1)
    if caps_count > 3:
        text = text.title()

    # Clean up any extra spaces introduced by cleaning
    text = re.sub(r' {2,}', ' ', text).strip()

    return text


def find_silliest(text):
    if not text or not text.strip():
        return "Paste some text above first!"

    # Clean the text before processing
    cleaned = clean_text(text)

    # Split on sentence-ending punctuation followed by whitespace
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"])', cleaned) if len(s.strip()) > 30]

    if len(sentences) == 0:
        return "I need at least a couple of sentences to compare. Paste a longer passage!"

    # Score every sentence for "silly" vs "serious" vs "ordinary"
    labels = ["silly and ridiculous", "serious and important", "ordinary and boring"]
    results = classifier(sentences, candidate_labels=labels)

    # Handle single sentence (returns dict instead of list)
    if isinstance(results, dict):
        results = [results]

    # Find the sentence with the highest "silly" score
    best_phrase = ""
    best_score = 0
    for sentence, result in zip(sentences, results):
        silly_idx = result["labels"].index("silly and ridiculous")
        score = result["scores"][silly_idx]
        if score > best_score:
            best_score = score
            best_phrase = sentence

    # Show both original and cleaned versions if they differ
    header = f'"{best_phrase}"\n\nSilliness score: {best_score:.0%}'
    if cleaned != text.strip():
        header += "\n\n---\n(Text was cleaned before analysis)"

    return header


demo = gr.Interface(
    fn=find_silliest,
    inputs=gr.Textbox(lines=10, placeholder="Paste a paragraph or two here — try messy text!"),
    outputs=gr.Textbox(label="The Silliest Phrase"),
    title="Silly Phrase Finder (with Cleaning)",
    description="Same as Session 1, but now with input cleaning! Try pasting messy text — emoji, ALL CAPS, abbreviations, extra spaces — and see how cleaning helps the model.",
    examples=[
        ["The quarterly budget report is due on Friday. My cat learned to open the refrigerator and now judges my food choices. Please remember to submit your timesheets. The printer on the third floor is out of toner again."],
        ["OMG THIS IS SOOOOO AMAZING 🎉🎉🎉 I CANT EVEN BELIEVE IT!!! Dr. Smith said the results were incredible.   Rep. Johnson     gave a speech about    pancakes."],
        ["lolllll 😂😂😂 the penguin just vibed across the entire library floor. Meanwhile Mr. Rogers was teaching kids about kindness. THE WHOLE SCHOOL WAS WATCHING AND NOBODY COULD STOP LAUGHING."],
    ],
)

demo.launch()

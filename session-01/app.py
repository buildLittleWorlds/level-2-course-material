import gradio as gr
from transformers import pipeline
import re

# Load a zero-shot classification model (works on free CPU)
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")

def find_silliest(text):
    if not text or not text.strip():
        return "Paste some text above first!"

    # Split on sentence-ending punctuation followed by whitespace
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"])', text) if len(s.strip()) > 30]

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

    return f'"{best_phrase}"\n\nSilliness score: {best_score:.0%}'

demo = gr.Interface(
    fn=find_silliest,
    inputs=gr.Textbox(lines=10, placeholder="Paste a paragraph or two here..."),
    outputs=gr.Textbox(label="The Silliest Phrase"),
    title="Silly Phrase Finder",
    description="Paste any text and this AI will pick out the silliest phrase. It uses a zero-shot classifier — no one ever trained it on 'silly,' it just figures it out!",
    examples=[
        ["The quarterly budget report is due on Friday. My cat learned to open the refrigerator and now judges my food choices. Please remember to submit your timesheets. The printer on the third floor is out of toner again."],
        ["The sun rose over the mountains. A penguin wearing a tiny hat skateboarded through the library. Students studied quietly. The teacher handed out assignments."],
    ],
)

demo.launch()

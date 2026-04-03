# Comparative Analysis

Session 2 Research Method

## What It Is

Comparative analysis means testing the same question with different tools and observing where they agree, where they disagree, and why. The goal isn't to find the "best" tool — it's to understand what each tool can and can't see.

## When Researchers Use It

- A linguist compares how Google Translate, DeepL, and a human translator render the same poem — not to pick a winner, but to understand what each approach prioritizes (literal accuracy vs. emotional tone vs. cultural context).
- A doctor compares three different diagnostic tests for the same condition to understand when each one gives false positives or misses cases entirely.
- A film critic watches the same story told as a Hollywood blockbuster, an indie film, and an anime series — same plot, different lenses, different things made visible.

## How to Apply It

1. **Pick your question.** What are you trying to understand? ("How well can AI detect sarcasm?" "Which translation model handles slang better?" "Do image classifiers see the same thing in this photo?")
2. **Pick your tools.** Find at least two models or Spaces that address your question but differ in some way — different training data, different architectures, different output categories.
3. **Hold the input constant.** Run the EXACT same inputs through each tool. The comparison only works if the input is identical. Record what each tool says.

## Key Vocabulary

- **Comparative analysis** — Testing the same question with different tools and observing divergence.
- **Operationalization** — The specific way you define and measure a concept. "Emotion" operationalized as 2 categories (positive/negative) vs. 7 categories vs. 28 categories produces different results — not because the text changed, but because the definition changed.

## This Week's Shared Example

In class, we compared three sentiment models on the same text: a binary model (positive/negative), a 7-emotion model, and a 28-emotion model. Same input, three different lenses. The disagreements showed us that "how does this text feel?" depends entirely on how you define "feeling."

## Apply It to Your Own Topic

- What two models or Spaces in your Collection do similar things?
- What input would let you test them fairly against each other?
- If they disagree, can you figure out WHY by reading their model cards?
- What does the disagreement teach you about the models — or about the task itself?

See `GUIDE-research-journal.md` for how to structure your comparison as a journal entry.

## Explore the Training Data

Want to see what each model actually learned from? You can browse these datasets directly on Hugging Face — no code required. Open the dataset page and click the viewer to scroll through real rows.

- **[stanfordnlp/sst2](https://hf.co/datasets/stanfordnlp/sst2)** — 67K movie review sentences labeled POSITIVE or NEGATIVE. This is the dataset behind the binary sentiment model we used in class. If this is all the model ever read, what can't it understand?
- **[dair-ai/emotion](https://hf.co/datasets/dair-ai/emotion)** — 20K English tweets labeled with 6 emotions (anger, fear, joy, love, sadness, surprise). The model knows 6 feelings because someone labeled 20K tweets into exactly these 6 buckets. What feelings are missing?
- **[SetFit/sst5](https://hf.co/datasets/SetFit/sst5)** — The same movie review sentences as SST-2, but labeled on a 5-point scale instead of 2. Same text, different label scheme. Who decided there are only 2 feelings vs. 5?
- **[Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data](https://hf.co/datasets/Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data)** — 1,500 YouTube comments classified as nostalgic vs. non-nostalgic. "Nostalgia" isn't in any standard emotion model. Someone cared about a feeling the big models ignore.

Browse a few rows from each. The differences between these datasets are the reason the models disagree — and that's exactly what comparative analysis is designed to reveal.

---

AI + Research Level 2 • Session 2: Data Collection and Representation

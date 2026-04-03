# Between Sessions 4 & 5

This week's homework has three parts: exploring both sides of the classification/generation fork, a research journal entry, and GitHub uploads. Plan for about 1–2 hours total.

---

## Part 1: Hub Challenge — Explore Both Sides of the Fork

In class we saw the difference between **classification** (sorting into buckets) and **generation** (creating new content). Now explore both on your own.

### Step 1: Find a Classifier

Browse your Collection or the Hugging Face Hub for a **classification model** — one that sorts input into categories. It doesn't have to be sentiment. It could be:
- An emotion classifier
- A language detector
- A topic classifier
- A spam/toxicity detector
- An image classifier

Test it on **3–5 inputs**. For each one, record the label and the confidence score.

### Step 2: Find a Generator

Now find a **text generation model** or Space. Try:
- The Inference Widget on `distilbert/distilgpt2` (the model we used in class)
- Any text generation Space in your Collection
- A story generator, poem writer, or chatbot Space

Give it the **same inputs you used for the classifier**, but as prompts. What does it write?

### Step 3: Compare

For each input, you now have two kinds of output: a classification label and a generated continuation. Ask yourself:

- What does the classifier tell you that the generator doesn't?
- What does the generator produce that the classifier can't?
- Which one feels more "useful" for that particular input? Why?
- If you wanted to understand the input, which output helps more?
- If you wanted to create something new with the input, which one helps more?

### What to Notice

- Classification gives you a single answer. Generation gives you many possible continuations. Which is more informative?
- The generator's output changes each time you run it (even with the same input). The classifier's doesn't. Why?
- Try an adversarial input — something designed to confuse models. How does each type of model handle it?

### Bring It Back

Next session, be ready to share: what was the most interesting difference you found between classification and generation? Did one type of model surprise you?

Think about this: next week we learn about **temperature** — a control that changes how a generation model picks the next word. Before class, try running the same prompt through a generator 3–4 times and notice how the output varies. That variation is what temperature controls.

---

## Part 2: Research Journal Entry

Add your Week 4 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300–500 words.

### Week 4 Entry

```markdown
## Week 4 — Classification vs. Generation

### This Week's Big Idea
(What's the difference between classification and generation? Explain it in your own words, as if you were telling a friend.)

### The Demo
(What happened when we fed prompts to the text generator in class? What surprised you? How was it different from the classification models we used in Sessions 1–3?)

### How I Explored It
(What classifier and generator did you try for homework? What inputs did you use? What did you find?)

### The Training Data Connection
(Why does it matter that classification needs labeled data but generation only needs text? What does that have to do with scale?)

### What I Want to Try Next
(What would you like to generate? Is there a task where generation would be more useful than classification? What about the other way around?)
```

If you're not sure what to write, start with: explain the difference between classification and generation using one example from class. Then describe what you tried on your own.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **6 models and 4 Spaces** by Session 5. This week, try to add at least one **text generation** model or Space. Include a tasting note: what did it generate? Was it any good?

### Notebook

Finish the experiments in today's notebook. Try at least 5 different prompts and save your favorite outputs.

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 4 entry below the Week 3 entry, and commit

### Explorer Notebook (Optional)

Want to compare classification and generation in code? Open the Explorer notebook — it loads both a classifier and a generator, runs them on the same inputs, and displays the outputs side by side. Your results can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-04/explorer.ipynb)

---

AI + Research Level 2 · Session 4: Introduction to Supervised Learning

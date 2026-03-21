# Between Sessions 3 & 4

This week's homework has three parts: a challenge using models from your Collection, a research journal entry, and GitHub uploads. Plan for about 1–2 hours total.

---

## Part 1: Hub Challenge — Break a Model on Purpose

In class we tested a sentiment model and a zero-shot classifier on real news headlines. We found three failure modes: **tone deafness** (missing meaning behind measured language), **emotional flattening** (oversimplifying complex stories), and **anthropomorphic projection** (reading emotion into market metaphors and weather). That's adversarial testing. We also built a Space that calls a live news API and learned the CLEAR framework.

**See `GUIDE-adversarial-testing.md` for the method, the three failure modes, noise vs. meaning, and the CLEAR framework.**

### Option A: Stay with News / Sentiment

1. Open the **News Sentiment Analyzer** or **Zero-Shot News Analyzer** Space
2. Try different news categories and custom classification labels
3. Find 3 headlines where the model clearly gets it wrong
4. For each: is it a noise problem or a meaning problem? Can you match it to one of the three failure modes?
5. Update your Collection — add a tasting note describing what the model misreads

### Option B: Explore Your Own Topic

1. Pick a model or Space from your Collection — any topic
2. Find 3 inputs that break it
3. For each: noise problem or meaning problem?
4. Try cleaning/simplifying the input and re-test
5. Update your Collection with a tasting note

### What to Notice

- Are failures mostly noise or meaning?
- Does changing the categories (in zero-shot) change the model's accuracy?
- Can you match failures to the three failure modes?
- What would the model need to "know" to get these right?

### Bring It Back

Next session we cross from classification to generation. Bring your broken examples. Start thinking: could a model that creates text handle problems that a classifying model can't?

---

## Part 2: Research Journal Entry

Write a Week 3 entry using this template:

```markdown
## Week 3 — Adversarial Testing and the Limits of Classification

### This Week's Method
(What research method did we learn? Adversarial testing — plus zero-shot classification with custom categories.)

### How I Applied It
(What model or Space did you test? What headlines or inputs did you try? Did you experiment with custom categories?)

### What I Expected
(Before testing — what did you think would break the model? Did you expect custom categories to help?)

### What I Found
(What actually happened? Which headlines broke it? Did different categories change the results?)

### Why I Think This Happened
(Connect to training data, noise vs. meaning, the structure of classification, etc.)

### Limitations
(What couldn't you test? Were there failures you couldn't explain?)

### What I Want to Try Next
(Where is your curiosity pulling you?)
```

---

## Part 3: Grow Your Collection + GitHub

**Collection:** At least 5 models and 3 Spaces by Session 4. Include tasting notes for anything you tested adversarially.

**Notebook:** Finish experiments. Try different zero-shot categories on the pre-selected headlines. Key question: "Can better categories solve what classification can't?"

**SpaceCraft Resource:** This week you learned **Adversarial Testing** — deliberately trying to break a system to find its limits. SpaceCraft has a dedicated page for this method: [Adversarial Testing method card](https://buildlittleworlds.github.io/spaceCraft/methods/adversarial-testing.html)

**GitHub:** Upload notebook to `my-ai-portfolio` repo. Edit `research-journal.md` to add your Week 3 entry.

**Explorer Notebook (Optional):** Link to `explorer.ipynb` with Colab badge. "Apply this week's method to a model from your own Collection."

# Between Sessions 3 & 4

This week's homework has three parts: a challenge using models from your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Break a Model on Purpose

In class we tested adversarial inputs on a sentiment model, built a `clean_text()` function to fix noise problems, and then ran three adversarial stories through four different emotion models. We found three failure modes: tone deafness (missing meaning that's there), emotional flattening (oversimplifying complex feelings), and anthropomorphic projection (inventing meaning that isn't there). That's **adversarial testing** — deliberately breaking models to find their limits.

Now apply that same method to **your own interest**. (See `GUIDE-adversarial-testing.md` for a portable reference on this method, the three failure modes, noise vs. meaning, and the CLEAR framework.)

### Option A: Stay with Sentiment / Emotion

1. Open one of the sentiment or emotion models from your Collection (use the Inference Widget on the model's HF page)
2. Try to find **3 inputs that break it** — where the model's reading is clearly wrong
3. For each failure, figure out: is it a **noise problem** (formatting, emoji, caps) or a **meaning problem** (sarcasm, irony, context)?
4. If it's a noise problem, try cleaning the input by hand (remove emoji, fix caps, simplify) and re-test. Did the result change?
5. **Update your Collection** — add a tasting note to the model describing what breaks it and whether cleaning helps

### Option B: Explore Your Own Topic

1. Pick a model or Space from your Collection — any topic (image classification, translation, text generation, anything)
2. Try to find **3 inputs that break it** — where the output is clearly wrong or surprising
3. For each failure, figure out: is it a **noise problem** (bad formatting, weird input) or a **meaning problem** (the model doesn't understand what you actually meant)?
4. If it's a noise problem, try cleaning or simplifying the input and re-test
5. **Update your Collection** — add a tasting note describing the failure and what you learned

The key idea is the same either way: **some failures can be fixed with preprocessing, and some can't**. You saw it in class across three very different stories. Now see if the same pattern holds for whatever topic you're exploring.

### What to Notice

- Are the failures mostly noise problems or meaning problems?
- Does cleaning the input actually change the model's answer?
- Can you match any failure to one of the three failure modes — tone deafness, emotional flattening, or anthropomorphic projection? Or is it a different kind of failure entirely?
- What would the model need to "know" to get these right? (Context? Tone? Cultural knowledge? Domain expertise?)

### Bring It Back

Next session we cross a big line — from models that **classify** (sort things into categories) to models that **generate** (create something new). Bring your broken model examples, and start thinking about this question: could a model that creates text handle the problems that a model that classifies text can't?

---

## Part 2: Research Journal Entry

Add your Week 3 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 3 Entry

```markdown
## Week 3 — Adversarial Testing and Data Preprocessing

### This Week's Method
(What research method did we learn? Hint: adversarial testing — deliberately trying to break a model — and controlled before/after comparison with preprocessing.)

### How I Applied It
(What model or Space from your Collection did you test? What adversarial inputs did you try? Did you attempt any cleaning/preprocessing?)

### What I Expected
(Before testing — what did you think would break the model? Did you expect cleaning to help?)

### What I Found
(What actually happened? Which inputs broke it? Did preprocessing fix any of the failures?)

### Why I Think This Happened
(Your explanation. Connect it to training data, what the model can and can't "see," noise vs. meaning, etc.)

### Limitations
(What couldn't you test? Were there failures you couldn't classify as noise or meaning? What might be different with a different model?)

### What I Want to Try Next
(Where is your curiosity pulling you? Are you starting to notice a topic you keep coming back to?)
```

If you're not sure what to write, start with the simplest version: describe what you broke, whether cleaning helped, and why you think the model failed. You can always add more.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **5 models and 3 Spaces** by Session 4. For any new items you add, include a tasting note — and if you tested adversarial inputs on them, note what broke and why.

### Notebook

Finish the experiments in today's notebook. Try editing the `clean_text()` function to add your own cleaning step — the notebook has a cell ready for you to experiment with.

The key question: **What can cleaning fix, and what is beyond its reach?**

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 3 entry below the Week 2 entry, and commit

### Explorer Notebook (Optional)

Want to apply this week's method in code? Open the Explorer notebook — it lets you load a model from your Collection, feed it adversarial inputs, apply cleaning, and compare before/after results. Your observations can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/explorer.ipynb)

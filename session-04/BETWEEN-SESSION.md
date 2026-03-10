# Between Sessions 4 & 5

This week's homework has three parts: a challenge using models from your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Compare Models Side by Side

In class we ran a **model evaluation** — putting three sentiment models side by side on the same text and comparing their answers. That's a research method called **baseline comparison** — testing multiple tools on the same data to see which one performs best.

Now apply that same method to **your own interest**.

### Option A: Stay with Sentiment / Emotion

1. Open two or more sentiment/emotion models from your Collection (use the Inference Widget on each model's HF page)
2. Test them on the **same 5 inputs** — choose texts that are emotionally ambiguous or interesting
3. For each input, record: which model's answer do you agree with most? Which model seems most trustworthy overall?
4. **Update your Collection** — add a tasting note to each model describing its strengths and weaknesses compared to the others

### Option B: Explore Your Own Topic

1. Find **2+ models or Spaces** from your Collection that do similar things (two image classifiers, two translation models, two text generators — anything)
2. Test them on the **same 5 inputs**
3. For each input, record: which one gave the better answer? Why?
4. **Update your Collection** — add tasting notes comparing them. Which do you trust more, and why?

The key idea is the same either way: **when multiple models tackle the same task, they disagree — and the disagreement reveals something about the models and the task.** You saw it with sentiment tonight. Now see if it's true for your topic.

### What to Notice

- Do the models disagree more on some types of input than others?
- Is one model consistently better, or does it depend on the input?
- Can you explain WHY they disagree by reading their model cards?

### Bring It Back

Next session, be ready to share: what did you compare, and which model did you trust more?

---

## Part 2: Research Journal Entry

Add your Week 4 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 4 Entry

```markdown
## Week 4 — Model Evaluation and Baseline Comparison

### This Week's Method
(What research method did we learn? Hint: model evaluation — putting multiple models side by side on the same inputs and comparing their answers.)

### How I Applied It
(What models or Spaces from your Collection did you compare? What inputs did you test them on? How many inputs did you try?)

### What I Expected
(Before testing — which model did you think would be better? Why?)

### What I Found
(What actually happened? Where did the models agree? Where did they disagree? Which one did you trust most?)

### Why I Think This Happened
(Your explanation. Connect it to training data, model design, the type of task, etc.)

### Limitations
(What couldn't you test? Would more inputs change your conclusion? What about different types of inputs?)

### What I Want to Try Next
(Is a topic emerging from your explorations? What would you investigate if you had more time?)
```

If you're not sure what to write, start with: describe which models you compared, what inputs you used, and which model you trusted more. Then try to explain why.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **6 models and 4 Spaces** by Session 5. For any new items you add, include a tasting note — and if you compared them to another model, note which one you preferred and why.

### Notebook

Finish the experiments in today's notebook. The score table is especially useful — try at least 5 inputs and track which model wins each time.

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 4 entry below the Week 3 entry, and commit

### Explorer Notebook (Optional)

Want to apply this week's method in code? Open the Explorer notebook — it lets you load 2-3 models from your Collection, run them on the same inputs, and tabulate which one you trust most. Your results can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-04/explorer.ipynb)

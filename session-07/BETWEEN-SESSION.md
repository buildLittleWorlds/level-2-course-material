# Between Sessions 7 & 8

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Test for Bias

In class we did **fairness auditing** — designing paired tests where we changed only one variable (a name, a pronoun, a job title) and measured whether the model's output changed. That's how you test for **algorithmic bias** — does the model treat different groups equally?

Now apply that same method to **your own interest**.

### Option A: Stay with Sentiment

1. Open the Bias Tester Space (your copy or the class version)
2. Design **5 new paired-sentence tests** we didn't try in class. Try different categories:
   - Names from different cultural backgrounds
   - Age references (young/old, teenager/elderly)
   - Regional or dialect differences ("y'all" vs. "you all")
   - Emotional expression styles ("I'm upset" vs. "This is unacceptable")
3. For each pair, note: same result or different? Which direction? Who got the more positive score?
4. **Bonus:** Search https://huggingface.co/models for a sentiment model that claims to be "fair" or "debiased." Test it with your pairs. Does it do better?
5. **Update your Collection** with any new models you found

### Option B: Explore Your Own Topic

1. Pick a model or Space from your Collection
2. Design a **paired test** — two inputs that are identical except for one demographic detail:
   - Image classifier: same object, different skin tones in the background or hands holding it
   - Translation model: same sentence with different names or cultural references
   - Text generator: same prompt with different character names or genders
   - Any model: test with inputs from different cultural contexts
3. Run both inputs and compare the results
4. Document what happens: does the model treat them equally, or differently?
5. **Update your Collection** — add a tasting note about any bias you found (or didn't find)

The key idea is the same either way: **models learn patterns from data, and data reflects a world that isn't always fair.** You tested it with sentiment tonight. Now test it with whatever topic you're exploring.

### What to Notice

- Did any results surprise you?
- Can you find a pattern in which swaps cause the biggest differences?
- Were there pairs where you expected bias but didn't find it? That's data too.

### Bring It Back

Next session, be ready to share your most surprising finding — either a bias you found or one you expected but didn't see.

---

## Part 2: Research Journal Entry

Add your Week 7 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 7 Entry

```markdown
## Week 7 — Fairness Auditing and Bias Testing

### This Week's Method
(What research method did we learn? Hint: fairness auditing — designing paired tests to check whether a model treats different groups equally.)

### How I Applied It
(What model or Space did you test? What pairs did you design? What variable did you change — name, gender, role, age, something else?)

### What I Expected
(Before testing — did you think the model would show bias? In which direction?)

### What I Found
(What actually happened? Were there differences? How big? Was there a pattern?)

### Why I Think This Happened
(Your explanation. Connect it to the training data — what patterns might the model have learned? From what kind of text?)

### Limitations
(What kinds of bias couldn't you test with this model? What groups or categories did you not cover?)

### What I Want to Try Next
(Is your topic coming into focus? What question keeps pulling you back?)
```

If you're not sure what to write, start with: what pairs did I test, what did I expect, and what surprised me? That's the core of a fairness audit.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **9 models and 6 Spaces** by Session 8. For new items, include tasting notes — especially note anything you've observed about fairness or who the model works best for.

### Notebook

Finish the experiments in the Session 7 notebook:
- Fill in all 5 of your own test pairs in Experiment 1
- Run Experiment 2 (find the biggest bias gap)
- Try at least one new category of swap in Experiment 3

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 7 entry below the Week 6 entry, and commit

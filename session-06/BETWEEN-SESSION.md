# Between Sessions 6 & 7

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Test Across Domains

In class we did **cross-domain testing** — taking models trained on one type of data and testing them on completely different types. That's how you test **generalization** and **external validity** — does the model actually work outside its training world?

Now apply that same method to **your own interest**.

### Option A: Stay with Sentiment

1. Open your Sentiment Showdown Space (your duplicate from Session 4)
2. Find **2-3 new domains** we didn't test in class — try text from a world the models have definitely never seen (fan fiction, video game dialogue, a recipe, a religious text, sports commentary)
3. For each domain, note: which model handles it best? Which falls apart? Why?
4. **Bonus:** Search https://huggingface.co/models for a sentiment model trained on the domain where your models failed. Can you find one? Add it to your Collection with a tasting note explaining what domain it was trained on
5. **Update your Collection** with any new models you found

### Option B: Explore Your Own Topic

1. Pick a model or Space from your Collection
2. Find out what it was trained on — check the model card, the README, or the dataset description
3. Test it on **data from a different domain** than its training data. For example:
   - Image classifier trained on photos → test with drawings, paintings, or screenshots
   - Translation model trained on news → test with slang, poetry, or song lyrics
   - Text model trained on English → test with code-switched text or dialect
4. Document what happens: does it generalize, or does it break?
5. **Update your Collection** — add a tasting note describing the domain shift you found

The key idea is the same either way: **a model's training data defines its world, and the real world is bigger than any training set.** You saw it with sentiment tonight. Now test it with whatever topic you're exploring.

### What to Notice

- Does the model fail gracefully (lower confidence) or confidently get it wrong?
- Is there a pattern in what kinds of inputs break it?
- Could you predict the failure from the model card alone?

### Bring It Back

Next session, be ready to share: what domain did you test, and what did the model miss? Your domain-shift findings set up the next problem — what happens when the solution to domain shift (training on everything) brings its own costs.

### Looking Ahead

**Optional deeper reading:** The `bonus-bert-content-moderation` module explains how BERT was trained, why pretraining + fine-tuning was a breakthrough, and how Twitter used BERT-style models for content moderation. It bridges the domain-shift problem from this session into Session 7's topic: bias. If you're curious about the breakthrough we discussed at the end of class, start there.

---

## Part 2: Research Journal Entry

Add your Week 6 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 6 Entry

```markdown
## Week 6 — Same Space, Different Worlds

### This Week's Method
(What research method did we learn? Hint: cross-domain testing — taking a model out of its training domain to see if it generalizes.)

### How I Applied It
(What model or Space did you test? What was its original training domain? What new domain did you test it on?)

### What I Expected
(Before testing — did you think the model would handle the new domain? Why or why not?)

### What I Found
(What actually happened? Did it generalize or fail? Were the failures obvious or subtle?)

### Why I Think This Happened
(Your explanation. Connect it to the training data — what did the model learn, and what was missing from its world?)

### Limitations
(What domains couldn't you test? Would a different model trained on different data handle it better?)

### What I Want to Try Next
(Is your topic coming into focus? What question keeps pulling you back?)
```

If you're not sure what to write, start with: what was the model trained on, what did I give it instead, and what broke? That's the core of domain shift.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **8 models and 5 Spaces** by Session 7. For new items, include tasting notes — especially note what domain each model was trained on and whether you've tested it outside that domain.

### Notebook

Finish the experiments in the Session 6 notebook:
- Test at least 2 more domains of your own choosing
- Fill in the observation table for Experiment 3
- Write your observations in the "My Observations" markdown cell (double-click to edit)

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 6 entry below the Week 5 entry, and commit

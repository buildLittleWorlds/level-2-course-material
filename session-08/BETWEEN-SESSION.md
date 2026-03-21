# Between Sessions 8 & 9

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Chain Two Models

In class we built a **multi-model pipeline** — connecting the output of one model to the input of another. We saw how **errors cascade**: when the captioner gets the image wrong, the sentiment model analyzes a wrong description.

Now think about chaining in **your own interest**.

### Option A: Stay with Sentiment

1. Open the Image Story Pipeline Space (your copy or the class version)
2. Upload **5 different kinds of images** and run the pipeline on each:
   - A photo of something obvious (baseline)
   - A photo with ambiguous emotion (person with unclear expression)
   - An image with text (meme, sign, screenshot)
   - Abstract art or a pattern
   - A very dark, blurry, or unusual photo
3. For each image, track:
   - What the image actually shows
   - What the caption said
   - What the sentiment said
   - Which step went wrong (if either did)
4. **Bonus:** Find the most interesting error cascade — where the caption is wrong AND the wrong caption leads to a wrong sentiment. Can you find a case where the caption is wrong but the sentiment accidentally gets it right?
5. **Update your Collection** with any interesting models you discover

### Option B: Explore Your Own Topic

1. Think about two models from your Collection that could be chained together. For example:
   - Image classifier → text generator (describe what the classifier found)
   - Translation model → sentiment model (translate then analyze mood)
   - Text generator → text classifier (generate then evaluate)
   - Any model whose output could become another model's input
2. You don't have to build this — just **think through the chain on paper**:
   - What would Model 1 output?
   - What would Model 2 do with that output?
   - What could go wrong at each step?
3. If you want to try it: use the Hub to find both models, test them separately, then manually feed Model 1's output into Model 2
4. **Update your Collection** — add a tasting note about any chaining possibilities you see

The key idea is the same either way: **when models are connected, errors don't just happen — they travel.** You saw it with our image-caption-sentiment pipeline tonight. Now think about where errors could travel in your own topic.

### What to Notice

- How often does the captioner get it right?
- When it's wrong, is it completely wrong or just slightly off?
- Does a wrong caption always lead to a wrong sentiment? Or can the sentiment model still get it right by accident?

### Bring It Back

Next session, be ready to share either your best broken pipeline result or your idea for chaining two models from your Collection.

### Looking Ahead

Tonight was the last piece of Act II. You've now seen the full set of ideas behind modern AI: classification, generation, controls, domain shift, pretraining, bias, and pipelines.

Next session, we shift from what's inside the machine to what's outside it. You'll take a sentiment analysis demo — something like what we've been building all course — and redesign it into a tool for a real audience. A restaurant owner reading reviews. A teacher analyzing student feedback. A therapist monitoring journal entries. The model stays the same. The design around it changes everything. That's Session 9: prompt engineering and human-AI interaction.

---

## Part 2: Research Journal Entry

Add your Week 8 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 8 Entry

```markdown
## Week 8 — Multi-Model Pipelines and Error Cascades

### This Week's Method
(What research method did we learn? Hint: error propagation analysis — tracing how mistakes travel through a multi-model system.)

### How I Applied It
(What pipeline did you test? What images or inputs did you use? Did you think about chaining models from your own Collection?)

### What I Expected
(Before testing — did you think errors would always cascade? Or did you expect the second model to sometimes fix things?)

### What I Found
(What actually happened? Where did errors start? Where did they end up? Any surprising results?)

### Why I Think This Happened
(Your explanation. Connect it to the models' training data and how they process information differently.)

### Limitations
(What kinds of pipelines couldn't you test? What would you need to build a real chained system for your topic?)

### What I Want to Try Next
(Your topic should be coming into focus by now. What would you build if you had two models working together?)
```

If you're not sure what to write, start with: what image broke the pipeline, what did the caption say, and why did the error cascade? That's the core of error propagation analysis.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **10 models and 6 Spaces** by Session 9. For new items, include tasting notes — especially note any models that could be chained together or whose outputs could feed into another model.

### Notebook

Finish the experiments in the Session 8 notebook:
- Upload at least 3 different images and run the pipeline on each
- Fill in the error tracking table in Experiment 3
- Try the "corrected caption" test — does fixing the caption change the sentiment?

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 8 entry below the Week 7 entry, and commit

# Between Sessions 2 & 3

This week's homework has three parts: a challenge using the Hub, a research journal entry, and GitHub setup. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Find a Model the Current Ones Miss

In class we compared three sentiment models that each "see" feelings differently because of their training data. That's a research method called **comparative analysis** — testing the same question with different tools and observing where they diverge.

Now apply that same method to **your own interest**. (See `GUIDE-comparative-analysis.md` for a portable reference on this method, and `GUIDE-grow-your-collection.md` for step-by-step Collection instructions.)

### Option A: Stay with Sentiment / Emotion

1. Go to [huggingface.co/models](https://huggingface.co/models)
2. Search for "emotion" or "sentiment" and find a model that uses different categories than the ones we tried tonight
3. Test it using the **Inference Widget** — type a sentence and see what it returns
4. **Add it to your Collection** with a tasting note (model name, what it classifies, trained on, easy test, interesting test, strength, weakness)

### Option B: Explore Your Own Topic

1. Go to [huggingface.co/models](https://huggingface.co/models) or [huggingface.co/spaces](https://huggingface.co/spaces)
2. Browse for something that interests you — image classification, translation, text generation, code, music, anything
3. Find **two models or Spaces** that do similar things but differently (different models, different training data, different outputs)
4. Test both with the same inputs. **Add both to your Collection** with tasting notes that compare them

The key idea is the same either way: **different training data → different results**. You saw it with sentiment tonight. Now see if it's true for whatever topic catches your eye.

### What to Notice

- Do the two models/Spaces you found use different categories or labels?
- Do they give different answers on the same input?
- Can you figure out *why* they disagree by reading the model cards?

### Bring It Back

Next session, be ready to share: what did you compare, and where did they disagree?

---

## Part 2: Research Journal Entry

This is new — and you'll do one of these every week. Create a file called `research-journal.md` in your GitHub repo (instructions below). Each week you'll add an entry.

The journal is where you document what YOU are investigating — not just what we did in class, but how you're applying it to your own interests. (See `GUIDE-research-journal.md` for a full guide with section-by-section explanations, a worked example, and the five-step tasting process.)

### Week 2 Entry

Write 300-500 words using this template:

```markdown
## Week 2 — Training Data and Representation

### This Week's Method
(What research method did we learn? Hint: comparative analysis — testing multiple models on the same inputs.)

### How I Applied It
(What did you compare? Which models or Spaces from your Collection did you test? What inputs did you use?)

### What I Expected
(Before you tested — what did you think would happen?)

### What I Found
(What actually happened? Where did the models agree or disagree?)

### Why I Think This Happened
(Your explanation. Connect it to training data, model design, categories, etc.)

### Limitations
(What couldn't you test? What might change with different inputs or models?)

### What I Want to Try Next
(Where is your curiosity pulling you? What would you investigate if you had more time?)
```

Don't worry about getting it "right." This is a research journal, not a test. The goal is to start building the habit of documenting what you find and thinking about why.

---

## Part 3: Grow Your Collection + GitHub Setup

### Collection

Your Collection should have at least **4 models** and **2 Spaces** by Session 3. For each item, write a tasting note explaining what you discovered. Your Collection can include sentiment models, emotion models, OR anything else you're exploring.

### Notebook

Finish the experiments in today's notebook. The key question for each experiment: **which model do you agree with most, and why?**

Try to find:

- Text where all three models agree about the feeling
- Text where they completely disagree
- A feeling you've had that none of the three models can name

### SpaceCraft Resource

This week you learned **Comparative Analysis** — testing the same question with different tools and studying where they disagree. SpaceCraft has a dedicated page for this method with steps, examples, and exercises you can try on leaderboard Spaces: [Comparative Analysis method card](https://buildlittleworlds.github.io/spaceCraft/methods/comparative-analysis.html)

### GitHub

1. Create a new repository called `my-ai-portfolio`
2. On github.com, click the **+** in the top right, then **New repository**
3. Name: `my-ai-portfolio`, keep it Public, add a README
4. Upload today's notebook: click **Add file** → **Upload files**, drag the `.ipynb` file
5. Create your research journal: click **Add file** → **Create new file**, name it `research-journal.md`, paste your Week 2 entry, and commit

### Explorer Notebook (Optional)

Want to apply this week's method in code? Open the Explorer notebook — it lets you load a model from your Collection and compare it against the three class models on your own inputs. Your results can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-02/explorer.ipynb)

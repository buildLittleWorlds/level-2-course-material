# Between Sessions 5 & 6

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Experiment with Settings

In class we did a **parameter sweep** — systematically changing one variable while holding others constant. That's **experimental design** — the foundation of any controlled experiment.

Now apply that same method to **your own interest**.

### Option A: Stay with Text Generation

1. Duplicate the Text Playground Space to your own Hugging Face profile
2. Pick **2 or 3 different writing tasks** (scary story, formal email, poem, news report — or invent your own)
3. For each task, experiment with the sliders. Change **one slider at a time** and note what happens
4. Write down your "settings recipe card" for each task: what temperature, top-p, and max length worked best?
5. **Add the Space to your Collection** with a tasting note describing what settings work for what tasks

### Option B: Explore Your Own Topic

1. Find a model or Space from your Collection that has **adjustable settings** — sliders, dropdowns, parameter controls of any kind
2. If your topic doesn't have obvious sliders, look for models on the Hub that do (image generators have guidance scale, translation models have beam width, etc.)
3. Pick one setting and **sweep it** — try low, medium, and high values on the same input
4. Document what changes: does higher always mean better? Where's the sweet spot?
5. **Update your Collection** — add a tasting note describing the parameter and what it controls

The key idea is the same either way: **changing one variable at a time while holding everything else constant is how you learn what each control actually does.** You saw it with temperature tonight. Now try it with whatever settings your topic offers.

### What to Notice

- Does the same setting work for all tasks, or do different tasks need different settings?
- Is there a "sweet spot" where the output is both creative and coherent?
- What happens at the extremes (very low or very high)?

### Bring It Back

Next session, be ready to share: what setting did you experiment with, and what did you learn?

---

## Part 2: Research Journal Entry

Add your Week 5 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 5 Entry

```markdown
## Week 5 — Parameter Sweeps and Experimental Design

### This Week's Method
(What research method did we learn? Hint: parameter sweep — changing one variable at a time while holding others constant.)

### How I Applied It
(What model or Space did you experiment with? What setting did you sweep? What values did you try?)

### What I Expected
(Before testing — what did you think would happen as you changed the setting?)

### What I Found
(What actually happened? Was there a sweet spot? What happened at the extremes?)

### Why I Think This Happened
(Your explanation. Connect it to how the model works, what the parameter controls, etc.)

### Limitations
(What couldn't you test? Would a different model respond differently to the same parameter changes?)

### What I Want to Try Next
(Are you circling a topic? What question keeps coming up in your explorations?)
```

If you're not sure what to write, start with: describe what you changed, what stayed the same, and what surprised you. That's the core of experimental design.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **7 models and 5 Spaces** by Session 6. For new items, include tasting notes — especially note any adjustable settings you discovered.

### Notebook

Finish the experiments in the Session 5 notebook:
- Fill in the "settings recipe cards" table with your best settings for each task
- Try Experiment 2 (same settings, different prompts) and Experiment 3 (extreme settings)
- Write down any surprising results

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 5 entry below the Week 4 entry, and commit

### Explorer Notebook (Optional)

Want to apply this week's method in code? Open the Explorer notebook — it lets you sweep temperature and top-p on a text generation model (or swap in your own), recording how output changes as you isolate one variable at a time. Your results can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-05/explorer.ipynb)

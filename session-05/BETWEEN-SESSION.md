# Between Sessions 5 & 6

**You built something tonight.** Whether it's the text generator, the summarizer, or a duplicate you customized — you have a working Space on Hugging Face. This is Space 1: your baseline. It works, but it's limited. Over the next several weeks, you'll build from here toward something you're proud of.

You also met Riley, the example student. Riley's portfolio is your reference point — not something to copy, but a map of where this course goes. Keep coming back to it as you work.

This week: make Space 1 yours, test it, and start thinking about what you want to build next. Plan for about 1 hour.

---

## Build Step: Get Space 1 Running and Customized (30 min)

**If your Space is working:** Customize it. Change the title, description, and example prompts to match your interests. Try adding the repetition penalty fix we discussed in class — ask your AI assistant:

> "Update my Hugging Face Space to add a Repetition Penalty slider (1.0 to 2.0, default 1.2). Pass it to the generator call as `repetition_penalty`. Also add `no_repeat_ngram_size=2` as a fixed parameter."

Experiment with the settings. Find the combination that makes your Space produce the best output for your topic.

**If your Space isn't working:** Fix it first. Compare your `app.py` and `requirements.txt` with the working code in the session materials, or duplicate `profplate/text-playground` and customize from there.

**Stuck?** Look at Riley's Space 1 code in the example student folder:
- [`example-student/space1-no-penalty/app.py`](../example-student/space1-no-penalty/app.py) — the version without repetition penalty (this is what your Space probably looks like right now)
- [`example-student/space1-with-penalty/app.py`](../example-student/space1-with-penalty/app.py) — the version WITH repetition penalty (this is what you're adding)
- Compare the two files side by side to see exactly what changed — it's one extra slider and one extra parameter in the generator call.

**Then test it on something unexpected.** Try 2–3 prompts from completely different domains — medical text, legal language, poetry, game dialogue, recipe instructions. Write down one example where the output quality dropped noticeably. Bring it to next session — we'll use it.

---

## Journal Entry (15 min)

Open `research-journal.md` in your GitHub repo (or create the repo and file now if you haven't). Add your Week 5 entry:

```markdown
## Week 5 — Add Controls

### What I Built
(Which Space did you build or customize? What does it do?)

### What I Tried
(What settings did you experiment with? What happened at the extremes?)

### What Surprised Me
(Was there a moment where the output changed in a way you didn't expect?)

### What I Want to Try Next
(What would make your Space more useful or more interesting?)
```

**Not sure what to write?** Read Riley's Week 5 journal entry in [`example-student/research-journal.md`](../example-student/research-journal.md). Notice the structure: what Riley built, what Riley tried, what surprised Riley, what Riley wants to do next. Your entry should follow the same pattern — but about YOUR project, not birds.

Also look at how Riley's earlier entries (Weeks 1–3) are shorter and more uncertain. If your entry feels tentative, that's completely normal. The confidence comes later.

---

## Portfolio Check

By Session 6, you should have:
- A GitHub repo (`my-ai-portfolio`) with `research-journal.md`
- At least 1 journal entry (tonight's)
- A running, customized Space on Hugging Face
- A Hugging Face Collection with 5+ items

**Reference:** Riley's full portfolio is in [`example-student/README.md`](../example-student/README.md). You don't need all of this yet — Riley's portfolio is what the FINISHED version looks like at Week 11. But glance at the structure: research question, journey summary, three Spaces, journal highlights, ML concepts. That's where you're headed.

---

## Your Folder

Your student folder on the course repo has prompts designed specifically for your interests — better models to try, more ambitious versions of your Space, and comparison tools you can build. **Open your folder and read through the README.** The prompts there are the starting point for your next Spaces.

**How Riley used prompts:** Riley started with generic bird prompts in Space 1, then discovered that text generation wasn't actually useful for birding — what was needed was audio classification. That pivot happened because Riley tested the limits of the text generator (see Week 6 in [`example-student/research-journal.md`](../example-student/research-journal.md)). Your "test on unexpected input" step above might reveal a similar pivot for your project.

---

## Your Personal Challenge

### Annabelle
You build fast — that's a real strength. This week, pick ONE of your Spaces and make it fully yours. Change the title, description, and examples. Write a journal entry about what you changed and why. One polished Space is worth more than four half-finished ones. **Check Riley's Space 1** ([`example-student/space1-with-penalty/app.py`](../example-student/space1-with-penalty/app.py)) — notice how it has a clear theme (birds), custom examples, and a descriptive title. Aim for that level of polish.

### Bobby
Your game development background is perfect for the text generator. Change the example prompts to game narrative — character dialogue, item descriptions, quest introductions. Experiment with temperature: what setting produces the best game writing? Write up your "settings recipe" in your journal. Then look at the prompts in your folder — Prompt 1 upgrades your Space to a better model. **Riley found that temperature 1.0 was the sweet spot for nature writing** (see Week 5 in [`example-student/research-journal.md`](../example-student/research-journal.md)) — what's the sweet spot for game writing?

### Chengry
Your DxAI project is ambitious — the runtime error is a platform issue, not your code. Don't spend time debugging it. Instead, try something different: build a Space using the biomedical NER model (`d4data/biomedical-ner-all`). It reads text and labels every disease, drug, symptom, and body part. Ask an AI assistant to write a Gradio Space using `pipeline("token-classification", model="d4data/biomedical-ner-all")`. If you get it working, bring it to Session 6. **Riley's arc shows the same pattern** — starting with a general tool, then moving to a domain-specific model. Read Riley's Week 7 entry in [`example-student/research-journal.md`](../example-student/research-journal.md) for how that transition felt.

### Emily
Tonight was your launchpad. Customize your Space: change the title to something related to news or research, swap the examples for articles that interest you. Then create your GitHub repo and write your first journal entry. Your folder has prompts for a news model comparison lab and a summarizer — look at those for next steps. **If you're unsure about the journal format**, read Riley's Week 1 entry in [`example-student/research-journal.md`](../example-student/research-journal.md) — it's short and exploratory, which is exactly where you should be right now.

### George
Your main goal: a running, customized Space. Try it on health articles and write your first journal entry about what worked and what didn't with medical text. That observation connects directly to next session. **Riley noticed the same pattern with birds** — the model "writes beautifully about birds but fabricates everything" (see Week 6 in [`example-student/research-journal.md`](../example-student/research-journal.md)). You may find something similar with medical text.

### Henry
You've been a thoughtful curator. This week, become a builder. Make sure you have a running Space, customize the prompts, and start your journal. Your folder has prompts for a scene description Space that connects to your interest in camera angles and visual AI. **Look at how Riley's Space 1** ([`example-student/space1-with-penalty/app.py`](../example-student/space1-with-penalty/app.py)) is structured — the same pattern works for a scene description generator. Same code, different prompts.

### Sevilla
Your emotion detection work and the text generator are natural partners. Try emotionally charged prompts at different temperatures. Does high temperature produce more emotionally varied text? That's a parameter sweep applied to your specific interest. Write it up. **Riley did the same kind of systematic testing** — see Week 5 in [`example-student/research-journal.md`](../example-student/research-journal.md), where Riley tested temperature settings and found an optimal range. Your optimal range for emotion text will be different.

### Shawn
Your systematic comparison methodology is ideal here. Run a proper comparison: same prompt, one slider changed at a time, results documented in a table. This is what you do with image generation models — same method, different medium. Your folder has prompts for a model comparison lab you can build. **Riley's journal shows what systematic testing looks like** — especially Weeks 3 and 5 in [`example-student/research-journal.md`](../example-student/research-journal.md). Notice how Riley documents inputs, outputs, and explanations in a structured way.

---

AI + Research Level 2 • Session 5: Add Controls

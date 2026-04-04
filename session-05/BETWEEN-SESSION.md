# Between Sessions 5 & 6

**You built something tonight.** Whether it's the text generator, the summarizer, or a duplicate you customized — you have a working Space on Hugging Face. This is Space 1: your baseline. It works, but it's limited. Over the next several weeks, you'll build from here toward something you're proud of.

This week: make Space 1 yours, test it, and start thinking about what you want to build next. Plan for about 1 hour.

---

## Build Step: Get Space 1 Running and Customized (30 min)

**If your Space is working:** Customize it. Change the title, description, and example prompts to match your interests. Try adding the repetition penalty fix we discussed in class — ask your AI assistant:

> "Update my Hugging Face Space to add a Repetition Penalty slider (1.0 to 2.0, default 1.2). Pass it to the generator call as `repetition_penalty`. Also add `no_repeat_ngram_size=2` as a fixed parameter."

Experiment with the settings. Find the combination that makes your Space produce the best output for your topic.

**If your Space isn't working:** Fix it first. Compare your `app.py` and `requirements.txt` with the working code in the session materials, or duplicate `profplate/text-playground` and customize from there.

**Then test it on something unexpected.** Try 2-3 prompts from completely different domains — medical text, legal language, poetry, game dialogue, recipe instructions. Write down one example where the output quality dropped noticeably. Bring it to next session — we'll use it.

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

---

## Portfolio Check

By Session 6, you should have:
- A GitHub repo (`my-ai-portfolio`) with `research-journal.md`
- At least 1 journal entry (tonight's)
- A running, customized Space on Hugging Face
- A Hugging Face Collection with 5+ items

---

## Your Folder

Your student folder on the course repo has prompts designed specifically for your interests — better models to try, more ambitious versions of your Space, and comparison tools you can build. **Open your folder and read through the README.** The prompts there are the starting point for your next Spaces.

---

## Your Personal Challenge

### Annabelle
You build fast — that's a real strength. This week, pick ONE of your Spaces and make it fully yours. Change the title, description, and examples. Write a journal entry about what you changed and why. One polished Space is worth more than four half-finished ones.

### Bobby
Your game development background is perfect for the text generator. Change the example prompts to game narrative — character dialogue, item descriptions, quest introductions. Experiment with temperature: what setting produces the best game writing? Write up your "settings recipe" in your journal. Then look at the prompts in your folder — Prompt 1 upgrades your Space to a better model.

### Chengry
Your DxAI project is ambitious — the runtime error is a platform issue, not your code. Don't spend time debugging it. Instead, try something different: build a Space using the biomedical NER model (`d4data/biomedical-ner-all`). It reads text and labels every disease, drug, symptom, and body part. Ask an AI assistant to write a Gradio Space using `pipeline("token-classification", model="d4data/biomedical-ner-all")`. If you get it working, bring it to Session 6.

### Emily
Tonight was your launchpad. Customize your Space: change the title to something related to news or research, swap the examples for articles that interest you. Then create your GitHub repo and write your first journal entry. Your folder has prompts for a news model comparison lab and a summarizer — look at those for next steps.

### George
Your main goal: a running, customized Space. Try it on health articles and write your first journal entry about what worked and what didn't with medical text. That observation connects directly to next session.

### Henry
You've been a thoughtful curator. This week, become a builder. Make sure you have a running Space, customize the prompts, and start your journal. Your folder has prompts for a scene description Space that connects to your interest in camera angles and visual AI.

### Sevilla
Your emotion detection work and the text generator are natural partners. Try emotionally charged prompts at different temperatures. Does high temperature produce more emotionally varied text? That's a parameter sweep applied to your specific interest. Write it up.

### Shawn
Your systematic comparison methodology is ideal here. Run a proper comparison: same prompt, one slider changed at a time, results documented in a table. This is what you do with image generation models — same method, different medium. Your folder has prompts for a model comparison lab you can build.

---

AI + Research Level 2 • Session 5: Add Controls

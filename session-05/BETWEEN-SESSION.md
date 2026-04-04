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
You build fast — that's a real strength. This week, channel that into your "Creative Story Starter." Open your folder and use Prompt 1 to upgrade to SmolLM2-360M-Instruct — it's better at following playful style directions than distilgpt2. Customize the example prompts (your README has great ones: dinosaurs in concert halls, talking animals, unexpected recipe ingredients). Then test at different temperatures — your default is 0.9, but try pushing higher and lower. Write up what happened in your journal. **Check Riley's Space 1** ([`example-student/space1-with-penalty/app.py`](../example-student/space1-with-penalty/app.py)) — notice how it has a clear theme, custom examples, and a descriptive title. Aim for that level of polish.

### Bobby
Your game development background is perfect for this. Your folder has prompts for a "Game Narrative Generator" — use Prompt 1 to build it with SmolLM2-360M-Instruct. The example prompts in your README are already tuned for game writing: dungeon exploration, legendary swords, village elder secrets, quest logs, boss reveals. Get it running, then experiment with temperature — your default is set for creative writing, but what setting produces the cleanest quest dialogue vs. the wildest lore? Write up your "settings recipe" in your journal. **Riley found that temperature 1.0 was the sweet spot for nature writing** (see Week 5 in [`example-student/research-journal.md`](../example-student/research-journal.md)) — what's the sweet spot for game writing?

### Chengry
Your folder has prompts for a "Medical Text Generator" — use Prompt 1 to build it with SmolLM2-360M-Instruct. The default temperature is set lower (0.4) because medical-style text needs to stay careful, not creative. Your example prompts cover patient symptoms, medication side effects, test results, diabetes diet, and virus vs. bacteria — get the Space running and test whether the output sounds educational or starts hallucinating medical facts. Write up what you notice in your journal. Later prompts in your folder build toward a Medical Safety Audit Lab and a Medical Summarizer. **Riley's arc shows a similar pattern** — starting with a general tool, then discovering its limits. Read Riley's Week 5 entry in [`example-student/research-journal.md`](../example-student/research-journal.md) to see how careful testing revealed what the model couldn't do.

### Emily
Your folder has prompts for a "News Draft Generator" — use Prompt 1 to build it with SmolLM2-360M-Instruct. The default temperature is lower (0.4) because news-style writing should stay factual, not drifty. Your example prompts cover breaking science news, student research reports, conference announcements, university studies, and technology roundups. Get it running, then test whether the output stays informative or starts making things up. Write up what you notice. Later prompts in your folder build toward a News Draft Model Lab (with a news-mode dropdown) and a News Summarizer. **If you're unsure about the journal format**, read Riley's Week 1 entry in [`example-student/research-journal.md`](../example-student/research-journal.md) — it's short and exploratory, which is exactly where you should be right now.

### George
Your folder has prompts for a "Health Explainer" — use Prompt 1 to build it with SmolLM2-360M-Instruct. The default temperature is lower (0.4) because health text needs to stay clear and careful. Your example prompts cover ankle sprains, first aid, the immune system, sleep for recovery, and sports injury treatment — right in your wheelhouse. Get it running, then test whether the explanations are actually helpful or just confident-sounding. Write up what you notice. Later prompts in your folder build toward a model comparison lab with audience-level options (middle school, patient handout, general adult, science class). **Riley noticed the same pattern with birds** — the model sounds confident but fabricates (see Week 6 in [`example-student/research-journal.md`](../example-student/research-journal.md)). You may find something similar with health text.

### Henry
You've been a thoughtful curator. This week, become a builder. Your folder has prompts for a "Scene Describer" — use Prompt 1 to build it with SmolLM2-360M-Instruct. Your example prompts use real cinematography language: camera pans, bird's-eye views, angle perspectives, striking visual details. Get it running and test whether the model actually produces useful visual description or just generic filler. Write up what you notice. Later prompts in your folder build toward a Camera Angle Model Lab with a viewpoint dropdown (close-up, wide shot, bird's-eye, low angle, over-shoulder). **Look at how Riley's Space 1** ([`example-student/space1-with-penalty/app.py`](../example-student/space1-with-penalty/app.py)) is structured — the same pattern works for a scene description generator. Same code, different prompts.

### Sevilla
Your folder has prompts for an "Animation Scene Writer" — use Prompt 1 to build it with SmolLM2-360M-Instruct. Your example prompts focus on motion, mood, and visual storytelling: character frame entries, opening shots, animation sequences, mood transitions, final frame reveals. Get it running and test whether the model can actually describe motion and emotional shifts, or if it just writes flat descriptions. Write up what you notice. Later prompts in your folder build toward a Motion and Mood Model Lab with scene-mode options (action, emotional, transition, character entrance, final reveal) and an emotional register dropdown. **Riley did the same kind of systematic testing** — see Week 5 in [`example-student/research-journal.md`](../example-student/research-journal.md), where Riley tested settings and found what worked. Your optimal range for animation writing will be different.

### Shawn
Your folder has prompts for an "Anime Scene Writer" — use Prompt 1 to build it with SmolLM2-360M-Instruct. Your example prompts hit the key anime registers: battlefield sword draws, transfer student academy moments, villain reveals, quiet character moments, opening sequences with cherry blossoms. Get it running and test whether the model captures anime pacing and tone, or drifts into generic fantasy. Write up what you notice — your systematic comparison instincts are ideal for this. Later prompts in your folder build toward an Anime Scene Model Lab with scene-mode options (battle, school intro, villain reveal, quiet moment, episode summary). **Riley's journal shows what systematic testing looks like** — especially Weeks 3 and 5 in [`example-student/research-journal.md`](../example-student/research-journal.md). Notice how Riley documents inputs, outputs, and explanations in a structured way.

---

AI + Research Level 2 • Session 5: Add Controls

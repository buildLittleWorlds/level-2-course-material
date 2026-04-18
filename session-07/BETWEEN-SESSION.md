# Between Sessions 7 & 8

> **Heads-up:** This week's between-session work is editing. You drafted a first-pass `PAPER.md` in class with AI assistance. This week, you write the parts an AI cannot write for you — and you fill in the citations from your Consensus search.

**Tonight you drafted a paper.** Every one of you committed (or will commit) a `PAPER.md` to your research repo — a short working paper that comments on your Hugging Face Space. The AI helped you draft §§ I, III, V, VI, X, XI and the colophon. It refused to write §§ IV and IX for you, because those are the sections where the paper becomes yours.

This is the week those sections get written.

---

## The three required tasks (in order)

### 1. Write §IV — your Δ (1–2 paragraphs)

Your paper-starter named two or three candidate Δ's — the one *tunable* in your work that encodes your personal judgment, not the math. The number of models you chose, the prompt wording you settled on, the exact list of five art styles, the three genres, the ranked-with-uncertainty output format, the reading levels you targeted — whichever one you pick, §IV is where you *commit* to it and *defend* it.

Open the Bluest Hour paper, §IV ("The local offset Δ"):
<https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md>

Notice the moves:
1. State the Δ, in a `<kbd>` tag, as a specific concrete value.
2. Admit it is not a ___ — "It is not an astronomical constant; it is the author's estimate."
3. Name why it is what it is — one paragraph explaining the reasoning.
4. Include a `> [!TIP]` alert block explaining how the Δ could, in principle, be learned or calibrated — but isn't, because ___.

Your §IV follows the same pattern. Replace "astronomical constant" with whatever *would* be the impersonal version of your choice. Replace the reasoning paragraph with yours.

**This section is one paragraph plus one alert block. That's all.** Don't over-write it. The power of §IV is that it is the one place in the paper where the author is personally present; too many words dilute that.

### 2. Write §IX — your category (1 paragraph + 1 numbered list)

Your paper-starter named two candidate categories. Pick one. §IX names it, defines it, and reads your artifact as an instance.

Structure (from the Bluest Hour paper):

```markdown
## <sub>§ IX.</sub> &nbsp; Toward [your small category]

I'd like to propose a small category.

> **Your category here** &nbsp;*n.* &nbsp; A piece of software whose primary function is
> to ______. Its success is measured in ______.

The [artifact] is an instance. Its figure of merit is ______. Every design choice
in the artifact is legible once you take this framing seriously:

1. **No ___** — because ___.
2. **Has ___** — because ___.
3. **Returns ___** — because ___.
```

Keep the definition to **one sentence**. Keep the list to **3 or 4 items**. Small, defensible, slightly surprising. Not grand. Not a paradigm. A category a reader could argue with.

### 3. Fill the footnotes (from [`WEEK-7-RESEARCH-WORK.md`](WEEK-7-RESEARCH-WORK.md))

Your first draft has `[PLACEHOLDER]` footnote markers where real citations should go. Run the Consensus searches listed in your paper-starter (and walked through in `WEEK-7-RESEARCH-WORK.md`), pick the three strongest, and write each footnote in this form:

```markdown
[^one]: Author, *Title* (Year). One sentence on why this matters to your argument.
```

Three footnotes minimum. Five maximum. Any more and the paper starts feeling like a lit review; any fewer and it floats unmoored from prior work.

---

## Optional but encouraged

**Edit your Abstract.** Your AI wrote one; read it now and ask: does it actually summarize what the paper ended up saying, or does it summarize the paper the AI *thought* you were going to write? Rewrite in your voice. Five sentences.

**Pick your epigraph.** Your paper-starter suggested domains (books, memoirs, critics). Pick a line from a real book you actually like. Replace the `[CHOOSE ONE]` placeholders the AI left at the top of the paper.

**Clean up `[FILL IN]` markers in §I.** If the AI wrote `[FILL IN: line count]` or `[FILL IN: model ID]`, go look it up and fill it in. §I is the factual inventory; it should contain no placeholders by Session 8.

---

## What the paper does not need this week

- §§ II, VII, VIII — you can edit these next week or the week after. The AI draft is enough for now.
- The Colophon — facts-only; leave the AI's draft as-is unless it's wrong.
- §§ V, X, XI — the AI draft is probably good enough. Light edit if you have time; don't stall on them.

**Only §IV, §IX, and the footnotes are required this week.** Don't let perfect be the enemy of committed.

---

## One coding task (light)

If your Space 2 is not yet built or your Space 1 is broken (SLEEPING is fine, RUNTIME_ERROR is not), spend 30 minutes this week fixing the code. This is not this week's research work; it is maintenance. A paper whose §I points at a broken Space will need to be rewritten in two weeks when the Space is down.

**Priority fixes (based on the current tracker):**
- **Chengry:** `disease_detectives` RUNTIME_ERROR. Missing Python deps for audio. Remove audio code or add the dep to `requirements.txt`.
- **Shawn:** `AnimeSceneWriter` RUNTIME_ERROR. Debug or rebuild minimally.
- **George:** `My_Health_Explainer` SLEEPING. Open it once to wake it; confirm it still works.
- **Everyone else:** check that your flagship Space is reachable; if not, fix it.

---

## Prea's Week 7 journal entry — reread it

Prea's [Week 7 entry](../example-student-prea/research-journal.md) is still the strongest example in the course of taking a class topic (bias) and realizing it is not a side note but a *limitations section* the project has to write honestly. Whisper's documented performance disparities across speaker groups became her §X.

Your §X should do the same thing. What did your Space *not* do well? Who did it fail for? What's in the training data that biases your outputs? Name it in the paper.

---

## Portfolio check (by Session 8)

- [ ] `PAPER.md` committed to your research repo — first draft present, §IV written, §IX written, 3+ footnotes filled in
- [ ] Space 1 reachable (not RUNTIME_ERROR; SLEEPING is acceptable)
- [ ] `research-journal.md` has a Week 7 entry — even a short one — reflecting on the drafting session
- [ ] Your paper-starter is still in place at `level-2-course-material/<YourName>/paper-starter.md` — you'll reference it next week

---

## Your personal focus this week

### Annabelle
Your draft probably has the three angles from your paper-starter still floating. Pick the pedagogy angle (or whichever you chose) and commit in §II. Your §IV is NYSSMA — write it. Your §IX is "pattern engines, not genre teachers" (or the quantization alternative); pick and defend.

### Bobby
If you wrote the re-entry journal entry in or before the session, great — now pick between Path A (game dev + genAI) and Path B (systematic tool evaluation). If you didn't yet, write the re-entry entry this week and pick a path. No paper pressure until re-entry.

### Chengry
Debug DxAI first. Then write §IV on the ranked-with-uncertainty output format — that's your Δ. Your §IX is "staged safety"; make the claim concrete.

### Emily
Ship your first Space this week. The simplest version: a Gradio app with a headline input and a persona dropdown (neutral, foreign-ministry briefing, regional newspaper). Even a 40-line `app.py` is fine. Once it's deployed, your paper has something to point at, and §IV and §IX become writable.

### George
Create the GitHub repo. Commit your pivot-from-music journal entry as Week 1. If you drafted a paper during class, commit that too. Your §IV is the set of reading levels you target; §IX is "lexical adaptation" or "audience-visible caution" — pick and defend.

### Henry
Consolidate your per-week repos into one `AI-Research-Level-2` repo and move `PAPER.md` there. Write §IV on the slider-extremes methodology. §IX is "lexical perspective" — name it explicitly.

### Sevilla
Write one analytical animation journal entry this week. Then edit your draft's §I to match the Space you chose, and write §IV on the motion-primitive test set. §IX is "motion continuity as evaluation axis."

### Shawn
Debug `AnimeSceneWriter`. Run the 10-prompt × 5-style comparison grid. That becomes §III. Write §IV on the three-model triad (the choice of SDXL, Animagine-XL, Playground v2.5). §IX is "specialization debt" — defend it with evidence.

---

## What Session 8 does with this

Session 8 returns to technical progression — we'll look at error cascades, pipelines, and what happens when models chain together. But you'll look at it with a paper in your hand. When the session raises a new limitation or capability, you'll ask: *does this change §III of my paper? Does it create a new §X limitation? Does it strengthen my §IX category?*

The technical content doesn't stop. It gets a frame.

---

AI + Research Level 2 • Session 7: Drafting Your First Paper

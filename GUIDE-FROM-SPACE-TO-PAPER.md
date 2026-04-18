# From Space to Paper

*How to turn what you've built into a short working paper that lives in your repo.*

---

## 1. Why a paper?

You have built Spaces. You have kept a journal. You have read some published research. The missing step is the one that makes all of it *legible to someone who wasn't there* — a short paper that reads your own artifact as if you were reading someone else's.

This is **not** a scholarly journal article. It's a **working paper** — a genre older than computer science, older than the internet, older than your sneakers. A short, numbered, footnoted commentary that sits inside the repo it describes. Academic in shape; personal in voice; aesthetically interesting within markdown's constraints.

Think "essay in a well-designed magazine" rather than "term paper."

---

## 2. The exemplar

Open **[bluest-hour-almanac/PAPER.md](../bluest-hour-almanac/PAPER.md)** ([rendered on GitHub](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md)) in another tab. Keep it open while you write yours.

Notice the moves it makes:

- **The masthead smuggles the author's one opinion in as if it were a fact.** "Δ +35m" is buried among coordinates, Julian dates, moon phase. Nobody notices it's the one non-astronomical number. That's the move.
- **§ VI treats the classifier as "just another ephemeris."** It refuses the obvious framing (*"this is a language model and here is how it works"*) in favor of one that makes the app intelligible (*"it quantizes continuous phenomena into a vocabulary, same as the almanac does with the sky"*).
- **§ IX proposes a small category** — "ephemeral interfaces." Not grand. Not universal. One defensible claim that, if agreed with, changes how the reader sees your kind of tool.
- **§ X is a task list.** Things the artifact doesn't do. That's what makes it a *probe* instead of a *product*.

Read it twice. The shape matters more than the prose.

---

## 3. From journal to paper in five steps

### Step 1 — Pick the one artifact that's most yours

You have multiple Spaces. Most papers are about *one*. Pick the Space that:

- You would defend against a skeptical reader in two minutes
- Encodes a choice you made that no one else would have made
- You can describe without apologizing for what's broken

The other Spaces go in your journal as *process*. They do not belong in the paper's §I.

### Step 2 — Find your "Δ"

Bluest Hour's "Δ" is 35 minutes — a number the author picked because the light looked right 35 minutes before the textbook midpoint. It's the one place in the app where the author is personally present. Everything else is computed.

Your Δ is the number, threshold, prompt wording, curated list, chosen baseline, or design decision that is *you*. It might be:

- The three models you chose for your comparison (and why those)
- The temperature / top-p / max-tokens you settled on
- The exact wording of your system prompt
- The ten test inputs you used for your evaluation
- The reading-level target you set for your outputs
- The one genre / style / category you excluded from your comparison

Name it. Defend it. This is § IV of the template. If you can't name your Δ, your artifact isn't ready to write about yet.

### Step 3 — Write the abstract last

The abstract is ~5 sentences. Skip it on your first pass. Write §§ I–XI first; then come back and write the abstract from what you actually said.

A good abstract has:
1. What the artifact is (one sentence).
2. The unusual choice you made (one sentence).
3. How you're reading it — 3 levels, 4 levels, pick what's honest (one sentence).
4. The small claim you end up proposing (one sentence).
5. A keyword list that would make sense on a conference poster.

### Step 4 — Find 3–5 related papers (Consensus)

You can't write a §II "why this form" or a §IX "toward a category" without knowing what's already been claimed. Open Consensus (or the [Consensus-recommended-reading-list skill](../bluest-hour-almanac/PAPER.md) — ask the instructor to run it for your topic) and search for 2–4 phrases your artifact is adjacent to.

You don't need many papers. **Three is enough.** For each one, write down:
- Title, authors, year
- One sentence on what they asked
- One sentence on how their approach differs from yours

These become your footnotes. If you cite more than five, the paper starts feeling like a lit review; keep it tight.

### Step 5 — Fill the template

Copy [`PAPER-TEMPLATE.md`](./PAPER-TEMPLATE.md) into your repo as `PAPER.md`. Read each `<!-- instructor note: -->` comment, write your content, then delete the comment. Work in this order (NOT top to bottom):

1. **§ I — the artifact** (factual; easiest)
2. **§ III — the anatomy** (your technical section)
3. **§ VI — the model** (if you have one; otherwise the data source)
4. **§ IV — your Δ** (the one opinionated section)
5. **§ V — the unit** (short)
6. **§ X — what's missing** (task list)
7. **§ II — why this form** (needs §§ I and VI first)
8. **§ VII — interface as argument** (optional)
9. **§ VIII — a reading of the opening** (optional but it's the most fun one)
10. **§ IX — toward a category** (write last; you need everything above it)
11. **§ XI — closing** (short)
12. **Colophon** (facts only)
13. **Notes / footnotes** (your 3–5 Consensus papers)
14. **Abstract** (very last)
15. **Masthead title + epigraph** (do these on the last day; they're window-dressing that needs to reflect the finished paper)

---

## 4. Aesthetic moves inside GitHub markdown's constraints

GitHub renders markdown, but it **strips most raw HTML and all CSS/JS**. The features it *does* ship are more than enough to make a paper look like a paper. Your toolbox:

| feature | example | what it's for |
|---|---|---|
| **Tables with alignment** | `\| col \| col \|\n\|---\|---\|` | Ephemeris-style fact rows |
| **Blockquotes** | `> text` | Pull quotes, epigraphs, definitions |
| **Footnotes** | `text[^1]` … `[^1]: note` | Citations and asides |
| **Alert blocks** | `> [!NOTE]` / `[!TIP]` / `[!IMPORTANT]` / `[!WARNING]` / `[!CAUTION]` | Margin asides |
| **`<kbd>` tag** | `<kbd>Δ = 35</kbd>` | Any value the reader might want to "press" |
| **`<sub>` / `<sup>`** | `<sub>§ I.</sub>` | Small-caps-feeling section markers |
| **`<details>`** | `<details><summary>…</summary>…</details>` | Fold long content (e.g. code listings) |
| **`<picture>` with `prefers-color-scheme`** | Two-image swap for dark mode | Logos/diagrams that need light + dark versions |
| **LaTeX math** | `$...$` inline, `$$...$$` block | Any formula |
| **Mermaid diagrams** | ` ```mermaid\nflowchart LR\n... ``` ` | One pipeline diagram |
| **ASCII figures in code fences** | A box drawn in unicode | Timelines, curves, distributions |
| **Unicode typographic characters** | `—` `·` `→` `◆` `§` `†` `‡` `½` | Typographic texture |
| **Emoji** | Use sparingly | One, maybe two, in the masthead |
| **Horizontal rules** | `---` | Section breaks, rhythm |
| **Centered blocks** | `<div align="center">…</div>` | Title pages and finales |
| **Task lists** | `- [ ]` / `- [x]` | § X "what's missing" |

What **NOT** to use:
- Inline `style="..."` — stripped.
- `<script>` / `<style>` — stripped.
- Custom fonts — no web fonts in rendered markdown.
- Centered / colored text via HTML — mostly stripped. Use unicode and rules instead.

---

## 5. Common failure modes

Watch for these. They're the reason first drafts of these papers feel "off."

**1. Writing a how-to instead of a reading.**
*How-to:* "In this project I used the RoBERTa model fine-tuned on GoEmotions to classify journal entries…"
*Reading:* "The classifier is, read generously, just another ephemeris."
The first describes. The second argues. A paper argues.

**2. Treating the paper as a lab report.**
Lab reports have: Hypothesis, Methods, Results, Conclusion. That's not this. You already have a research brief or will have one; the paper is a **commentary** on the artifact you built, in the voice of someone who has read around the problem. Fact-heavy sections (§ I, § III, Colophon) are the inventory. Voice-heavy sections (§§ II, IV, VI, IX, XI) are what make it a paper.

**3. Stacking all your Spaces into §I.**
Pick one. Reference the others in your journal. The paper is not a portfolio.

**4. Inventing a grand category in §IX.**
"Toward a new paradigm for human-AI collaboration" is bad. "Toward ephemeral interfaces: software whose primary function is to tell you when to stop using it" is good. Small. Defensible. Slightly surprising. One sentence of definition, three or four sentences of examples.

**5. Epigraph-from-the-internet.**
Don't grab the first quote Google gives you for "music" or "medicine." Open a book you actually like in your domain and pick a line that says something. A bad epigraph is worse than none.

**6. Writing the abstract first.**
You don't know what you're summarizing yet. Leave a placeholder. Come back.

**7. Overreaching on scope.**
This is a 2–3 screen paper. Roughly 8–15 pages if printed, but nobody will print it. GitHub renders it as one long document. Not 30 pages. Not 2 pages. Somewhere in between, and if it's good, a reader will finish it in one sitting.

---

## 6. What "done" looks like

Your paper is done when a reader who has never seen your artifact can:

1. Say what the artifact is, in one sentence, after reading § I.
2. Name your Δ (the tunable that's *you*), after reading § IV.
3. Quote one sentence from your paper back to you without looking.
4. Agree or disagree with your § IX category — either is fine; uncertainty is not.

If a draft reader can't do those four things, go back and fix the section that corresponds to the failure.

---

## 7. Sequencing this with your existing work

You already have:
- A **research journal** — this feeds into §§ III, IV, VI, VII, VIII as *prose you've already written*, now rewritten for a reader.
- A **`RESEARCH-PATH.md`** — its research-question progression (broad → medium → narrow) and Consensus searches feed directly into §§ II, IX, and your footnotes.
- **Spaces** — one of them becomes §I; the others are process.

The paper doesn't replace any of those. It consolidates them into a *form* that a reader outside your course can engage with — a college admissions reader, a science-fair judge, a future you.

You've already done the hard part.

---

*One good paper is worth three half-finished ones. Pick the one artifact you most want to defend, and write about that.*

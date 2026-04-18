# Drafting Prompts — Session 7

*Copy one of these prompts into your AI assistant (Claude, ChatGPT, Gemini — whichever you use). Paste your paper-starter and the template alongside it. Commit the result.*

---

## Before you start

You need three files open in tabs or copied onto your clipboard:

1. **Your paper-starter.** In your folder at `level-2-course-material/<YourName>/paper-starter.md` — or open it at [`github.com/buildLittleWorlds/level-2-course-material`](https://github.com/buildLittleWorlds/level-2-course-material) and click into your name.
2. **The shared template.** [`PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md).
3. **The worked example (for tone).** [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md).

You will paste the contents of files 1 and 2 into your AI. File 3 you can link to — most AI assistants will fetch it, or you can paste it if yours won't.

---

## Prompt 1 — The full-draft prompt (start here)

Copy everything between the `---` lines below into your AI assistant. Replace the `[PASTE …]` markers with the actual contents. Don't edit the instructions themselves on your first pass.

---

```
You are helping me draft a first-pass working paper that comments on a Hugging Face
Space I built. I will give you three things:

  (1) a template to follow (PAPER-TEMPLATE.md)
  (2) my paper-starter, which contains topic-specific context drawn from my project
  (3) a worked example — the Bluest Hour paper — to show the voice and shape

Your job: produce a first draft of my PAPER.md, following the template exactly.

Rules:

- Keep the exact section numbering (§§ I–XI), the colophon, and the footnotes
  structure. Don't invent a new structure.

- Fill the FACTUAL sections — §§ I (The artifact), III (The anatomy), V (The unit),
  VI (The model), X (What's missing), XI (Closing), and the Colophon — with
  specific, plausible content drawn from my paper-starter. Don't hallucinate
  model IDs, URLs, or numbers I haven't given you; if you're not sure, write
  [FILL IN: ___] as a placeholder.

- For §§ II (Why this form), VII (Interface as argument), VIII (A reading of the
  opening), draft plausibly but mark them `[DRAFTED — I will revise]` at the end
  so I remember these are AI-drafted, not mine-yet.

- For §§ IV (My Δ) and IX (Toward a category), do NOT draft the whole section.
  Instead, write ONE paragraph that names the question the section is trying to
  answer, then write `[TO FILL: I need to write this myself]`. These are the two
  sections an AI cannot honestly write — they encode my personal judgment and
  my specific claim. I will write them during the week.

- Write the Abstract LAST, after drafting §§ I–XI. Keep it to 5 sentences.

- For the epigraph at the top of the paper, suggest 2–3 candidate quotes from
  the epigraph domain listed in my paper-starter. Mark it `[CHOOSE ONE:
  candidate A / B / C]`. Don't commit; this is a choice I'll make from a book
  I actually like.

- For the Notes section, DO NOT invent citations. Instead, write 3–5 placeholder
  footnote lines like `[^one]: [PLACEHOLDER: paper from Consensus search on X]`
  using the Consensus search queries listed in my paper-starter. I will fill
  these in from WEEK-7-RESEARCH-WORK.md.

VOICE: analytical commentary, not a lab report. Closer to an essay in a
well-designed magazine than a term paper. Read the Bluest Hour paper for tone —
it is direct, slightly dry, willing to claim small things, never grand.

LENGTH: aim for a paper that would take a careful reader 10–20 minutes. Not
longer. §§ can be short; the template values tightness.

MARKDOWN CONSTRAINTS: GitHub-flavored markdown only. Tables, blockquotes,
footnotes, LaTeX (`$...$` and `$$...$$`), Mermaid diagrams, `<kbd>`, `<sub>`,
alert blocks (`> [!NOTE]`), ASCII figures in code fences, `<details>`. No raw
`style=` attributes, no `<script>`, no custom fonts — GitHub strips them.

=========================================================
HERE IS THE TEMPLATE:
=========================================================

[PASTE ENTIRE CONTENTS OF PAPER-TEMPLATE.md HERE]

=========================================================
HERE IS MY PAPER-STARTER:
=========================================================

[PASTE ENTIRE CONTENTS OF YOUR paper-starter.md HERE]

=========================================================
HERE IS THE WORKED EXAMPLE (for tone, not to copy from):
=========================================================

The Bluest Hour paper lives at
https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md .
If you can fetch a URL, fetch it. Otherwise, I'll paste it below — use it only
to calibrate voice, section shape, and typographic moves. Do NOT copy its
content; my paper is about my topic, not the blue hour.

[OPTIONAL: paste PAPER.md contents if your AI can't fetch URLs]

=========================================================

Now produce the draft. Output it as a single markdown document I can save as
PAPER.md and commit to my repo.
```

---

## Prompt 2 — If you want to work section-by-section instead

Some of you may want more control. This variant asks the AI for one section at a time.

```
Using my paper-starter (pasted below) and the template (pasted below), draft
ONLY §III ("The anatomy of [your phenomenon]") from PAPER-TEMPLATE.md.

Follow the template's instructions for §III literally:
- one paragraph introducing the phenomenon
- one piece of technical content (an ASCII figure, a LaTeX formula, or a Mermaid
  diagram — pick whichever fits my topic; do not do more than one)
- one closing sentence naming the specific fact this section gives a reader that
  no one else will tell them

Voice: Bluest Hour paper voice. Dry, specific, committed.

[PASTE PAPER-TEMPLATE.md]

[PASTE YOUR paper-starter.md]
```

Repeat for §V, §VI, §VII, §VIII, §X, §XI in any order.

Do NOT use this variant for §§ IV and IX. Those you write yourself.

---

## Prompt 3 — If you get stuck on a specific section

Paste this plus the relevant paper-starter fragment:

```
I'm drafting §IX of my PAPER.md — the section where the paper proposes a small
category. My paper-starter suggests two candidates:

  (1) [PASTE CANDIDATE #1 FROM YOUR paper-starter.md]
  (2) [PASTE CANDIDATE #2 FROM YOUR paper-starter.md]

I'm choosing candidate (1/2/something-else).

Help me draft a §IX around my choice. The section should have:
- one sentence defining the category (italic, in blockquote format)
- one short paragraph naming the figure of merit (what success looks like for
  software in this category)
- a 3- or 4-item numbered list reading each design choice in my artifact as
  evidence for the category

Read the Bluest Hour paper's §IX ("Toward ephemeral interfaces") for shape.
Keep it short. Do not be grand. Small, defensible, one-sentence definition, a
few examples. That's it.

[OPTIONAL: paste your current §I draft so the AI knows what artifact you mean]
```

This is the section of the paper that most needs your voice; the AI should give you scaffolding, not finished prose. Treat its output as a draft to argue with.

---

## After the AI responds

1. **Read it once, top to bottom.** Don't edit yet. Just read.
2. **Check the §IV and §IX markers.** They should both say `[TO FILL: I need to write this myself]`. If the AI drafted them anyway, delete what it wrote and restore the marker. These sections are the paper becoming yours; do not let an AI fake them.
3. **Check §I for hallucination.** Does it name a model that isn't yours? A Space URL that doesn't exist? A line count it made up? Fix or mark `[FILL IN]`.
4. **Save as `PAPER.md`** in your GitHub repo. Not a Google Doc. Not a text file. `PAPER.md`, at the root of your `AI-Research-Level-2` repo (or whatever your research repo is called).
5. **`git add PAPER.md && git commit -m "First draft of PAPER.md (AI-assisted, §IV/§IX pending)" && git push`.**

You should have a committed draft in your repo by the end of the 40-minute drafting block. Imperfect is fine. Incomplete is fine. Committed is required — that's what we'll pull up on screen during the share-and-discuss.

---

## During the share-and-discuss (what to listen for)

The instructor will share each draft on screen for ~3 minutes each. For every draft (including yours), listen for three things:

- **Where did the AI sound generic?** If a paragraph could be written about anyone's project, it's a paragraph the author needs to rewrite.
- **Where did the AI try to write §IV or §IX anyway?** Sometimes it ignores the `[TO FILL]` marker. That's fine — it's still a useful first pass — but the author has to notice and plan the rewrite.
- **What's the one move in this draft that's already clearly the author's?** Usually it's in §I (the artifact you built) or in the choice of epigraph. Find it; call it out; that's the anchor the rest of the paper will grow from.

---

## Between-session work

Covered in full in [`BETWEEN-SESSION.md`](BETWEEN-SESSION.md). Short version:

- Write §IV (your Δ). One paragraph. The tunable that's you, not the math.
- Write §IX (your category). One short paragraph + a numbered list of evidence.
- Fill the `[PLACEHOLDER]` footnotes from your Consensus searches (see [`WEEK-7-RESEARCH-WORK.md`](WEEK-7-RESEARCH-WORK.md)).
- Everything else — §§ II, VII, VIII — can be edited next week or the week after. Only §IV, §IX, and the footnotes are this week's required work.

The AI wrote the skeleton. You write the parts that make it yours.

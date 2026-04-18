# Session 7: Bias, Variance, and Uncertainty
*"Who Gets Hurt?"*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-07/notebook.ipynb)

## What This Session Covers

Students leave this session with a **committed first-draft `PAPER.md`** in their repo — a short working paper that comments on the Hugging Face Space they have built. The paper is drafted live, in class, using an AI assistant as a writing partner: each student pastes a provided prompt along with their personalized `paper-starter.md` and the shared `PAPER-TEMPLATE.md` into Claude / ChatGPT / Gemini, generates a draft, and commits it to GitHub. The instructor then shares each draft on screen and the group discusses what the AI got right, what it missed, and what the student has to write themselves.

The session's official topic — **bias and fairness** — is carried by the group discussion. Every student's draft lands on two sections that force them to think about bias: **§IX** (propose a small category) and **§X** (honest limitations). Emily's paper, on perspective-explicit news summarization, is the session's anchor for the formal fairness-audit discussion; the other seven encounter bias as *one lens among several* their paper has to answer to.

## Narrative Role

This session is a **pivot session**. Sessions 1–6 built technical capacity: what's a model, what's a pipeline, how does a Space run, what's domain shift, what's fine-tuning. Starting with Session 7, the course shifts register: the students already have Spaces, collections, and at least the beginnings of research journals. The question is no longer "how do I build a thing?" but **"what can I say about the thing I built?"**

The bias-and-fairness framing is load-bearing for that shift. The move from *builder* to *researcher* is, at bottom, the move from *making a tool* to *asking who the tool serves, who it fails, and what its honest limitations are*. Every paper in this course — medical, musical, animated, political — has to answer those questions. Session 7 is where we practice writing them.

## Connections

- **Builds on Session 6:** Session 6 sharpened each student's research question. Session 7 turns the question into a paper. The domain-shift vocabulary from Session 6 (external validity, generalization) is what students now use in §III, §X of their drafts.
- **Builds on the new paper-phase scaffolding:** Each student has a personalized [`paper-starter.md`](../) in their folder; the shared template lives at [`PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md); the walkthrough at [`GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md). Session 7 is where these files stop being pointers and start being used.
- **Bridges to Session 8+:** With a paper draft in each student's repo, subsequent technical sessions become *motivated*. When we return to fine-tuning, embeddings, or error cascades, each student will be able to ask: *does this technique change anything in my §III? Does it create a new §X limitation I have to acknowledge?*
- **Bonus module:** The `bonus-bert-content-moderation` module remains optional reading and is still the natural companion piece for students whose papers land on bias as the primary §IX angle.

## Session Resources

**New for Session 7 (the core of the session):**
- **[`BLUEST-HOUR-CASE-STUDY.md`](BLUEST-HOUR-CASE-STUDY.md)** — the three-stage worked example: original Space → redesigned Space (almanac edition) → paper. Read this first as a student.
- **[`DRAFTING-PROMPTS.md`](DRAFTING-PROMPTS.md)** — the exact prompts students paste into their AI assistant to generate a first-draft `PAPER.md`. Includes the full-draft prompt and a few section-specific variants.

**Session 7 — existing (unchanged in title, repositioned in use):**
- **INSTRUCTOR-GUIDE.md** — minute-by-minute lesson plan with per-student screen-share notes.
- **BETWEEN-SESSION.md** — this week's focus is **editing** the first draft, not building new code. Specifically: write §IV (your Δ) and §IX (your category). These are the two sections the AI cannot write for you.
- **[`GUIDE-fairness-audit.md`](GUIDE-fairness-audit.md)** — research method card for the official topic. Kept as the reference for the bias-and-fairness conversation; anchored in class on Emily's paper but used by any student whose §IX lands on bias-related claims.
- **[`WEEK-7-RESEARCH-WORK.md`](WEEK-7-RESEARCH-WORK.md)** — Consensus source-search guide, the 3–5 footnote pulls each student needs to anchor their paper. Still required; now the backbone for §Notes in the paper draft.

**Session 7 — supplementary (available, not required this week):**
- **slides.html** — kept for reference; the session is discussion-heavy and runs largely from the shared worked-example walkthrough.
- **app.py · requirements.txt · notebook.ipynb** — the Bias Tester Space materials. Available for students whose paper-starter angles lean on bias measurement (notably Emily) and who want to fork them as a Space 2. Not part of the in-class flow.

## Why the shift

Five students came into Session 6 behind on documentation. Asking them to build another Space this week widens the gap; asking them to draft a paper about the Space they already have closes it. The session is deliberately re-engineered for catch-up without sacrificing pedagogical range: the strong students (Annabelle, Henry) get a head start on a portfolio artifact; the stalled students (Emily, George, Chengry, Sevilla) spend the session writing about what they've already built, which is the documentation they owe themselves. The bias-and-fairness topic still lands — but it lands through the paper, not through a third Space.

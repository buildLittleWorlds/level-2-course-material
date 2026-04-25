# Parallel Example: AI News Lens

This packet is the **GitHub-public-facing version** of the project Emily has been developing in Google Drive: a personalized news newsletter that uses AI to detect political bias on a per-article basis, generate neutral summaries with side-by-side framing, collect reader sentiment, and let users journal the news that matters to them.

The Drive material — the project outline, the Week 6 pivot journal entry, and the 34-paper Consensus literature review — is the substance. This packet's job is to translate that substance into the file shapes that GitHub and Hugging Face expect, without losing what's already there.

## Core idea

The imagined Space is **AI News Lens**. A user receives a daily or weekly digest. For each story:

- the AI produces a neutral summary,
- AI-detected bias is shown on a per-article basis (not just per outlet),
- representative quotes from across the political spectrum are surfaced,
- the user can record their sentiment after reading, and
- the user can journal stories worth returning to.

This is the four-pillar concept Emily described in her project outline, with Ground News as the inspiration source.

## Research question

> Does exposure to AI-detected bias change how users perceive news?

(This is the refined version Emily settled on after the question-sharpening pass with Claude.)

## Space idea

Inputs:

- News article URL or pasted text
- Date / timeframe
- User's prior sentiment on the topic (optional)

Outputs:

- Neutral summary
- Per-article bias score with positioning on a left/center/right continuum
- 2 representative quotes from across the political spectrum
- Sentiment-collection prompt asking what the reader thought *after* reading
- Save-to-journal action

## What this packet demonstrates

- How to take a serious project that has lived in Drive and translate its surfaces (paper, journal, sources, README) into Markdown files inside a GitHub repo
- How to write a research paper that names its theoretical frame — the *machine heuristic*, *algorithm aversion*, *automation bias* — instead of treating bias as a vague concern
- How to cite a literature review you've already done, instead of starting one from scratch
- How to honor an early-stage build artifact while writing a paper grounded in real prior work

## How to use this example

Read `cover-note.md` first — it explains what's the same as the Drive work, what's new, and what the next four sessions look like. Then `PAPER.md` shows the academic shape of the final write-up; `research-journal.md` shows what the GitHub journal entries look like (your Week 1 and Week 6 entries from Drive translated, plus a worked example for what we'll do in Session 8); and `sources.md` is built directly from your Consensus lit review.

Borrow the structure. The substance is yours.

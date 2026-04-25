# Session 9: Make Your Model Fit the Human

## What This Session Covers

Session 8 had two halves: models meeting models in a technical pipeline (BLIP → sentiment), and you meeting your audience through your GitHub and Hugging Face profiles. Both halves were versions of the same question — *how do the pieces fit?*

Session 9 picks up the same question at a third scale: **how does a technical model fit the actual human who's going to use it?** The model is yours, the audience is real, and the fit is what turns a demo into a tool someone wants to use. The hands-on exercise is a redesign: take a sentiment analysis demo and rebuild the experience around one specific human — a restaurant owner reading reviews, a teacher reading student feedback, a journal-keeper tracking mood — without changing the underlying model at all. The original concept here, *Prompt Logic and Human-AI Interaction*, is exactly this work: prompt engineering and interface design are the layers between a model's raw output and a human's actual use.

Two other threads continue tonight from Session 8:

- **Your public-facing research presence keeps growing.** Your GitHub profile, your Hugging Face Collection, your three Spaces, and your linked paper repo are now living artifacts. We add the careful-paper-reading work this week to your paper, polish your interface tonight using the same audience-design move you'll apply to your own Space, and keep iterating the profile.
- **Citation verification.** AI assistants hallucinate citations. Tonight introduces a three-step verification loop you'll use on every source you plan to cite, so what your paper claims and what the cited papers actually say are the same thing. This is a fitting problem too: your paper's claims have to fit what the literature actually supports.

## The core teaching line

> A model that produces correct output is not yet a tool. The fit between the model and the human is the work.

## Why this is the same problem as Session 8

Session 8 named two systems where pieces have to fit: model-to-model (technical pipeline) and self-to-public (your research presence on GitHub and Hugging Face — themselves technical systems where humans build identities). Session 9 names the third: model-to-human, where the technical pieces (the model, the prompts, the interface) have to fit the values, goals, and judgment of the people who'll actually use them.

This isn't an analogy across the three. GitHub and Hugging Face are real code-managed systems. Your profile is real text rendered from a real repository. A model's output is real bytes shaped by real prompt engineering. At every layer, code and humans are fused — and the fit question runs through all of it.

That's why audience-design is a technical curriculum item, not a soft skill bolted on. Reinforcement Learning from Human Feedback (RLHF) is the same move at the model-training scale: align what the model produces with what humans actually want. Tonight you do the small version of that work by hand on your own demo.

## Two paired moves tonight

**Move 1 — Audience redesign (in class).** Take the sentiment analysis demo and rebuild it for one specific person. Change the title, description, examples, and output framing. Don't touch the model. The change in user experience comes entirely from the human-facing layer. Same exercise applies to your own work this week: if Space 3 isn't deployed yet, build it with these four surfaces designed up-front for one named user. If Space 3 is already live, apply the redesign to whichever existing Space is least audience-fit right now.

**Move 2 — Citation verification (begins in class, finishes between).** Pick the source from your Week 7 shortlist that you most want to cite. Use the three-step verification loop (DOI check, title search, claim check) to make sure the paper exists, the authors and year match, and the claim you plan to make is actually supported. Repeat for each citation in your `week-09-citations.md` file before Session 10.

## Session Resources

- **[`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)** — the master AI prompt for paper drafting (continued use as you revise)
- **[`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)** — paper workflow guide
- **[`BETWEEN-SESSION.md`](./BETWEEN-SESSION.md)** — what to do this week
- **[`WEEK-9-RESEARCH-WORK.md`](./WEEK-9-RESEARCH-WORK.md)** — citation verification, the most important research-hygiene work of the course
- **[`GUIDE-user-centered-design.md`](./GUIDE-user-centered-design.md)** — research method card for tonight's redesign work
- **slides.html / app.py / notebook.ipynb** — supporting material for the redesign demo

## What students should leave with

- One Space of yours redesigned for a specific real person — title, description, examples, output framing all rebuilt around them. Same model, completely different experience.
- A clear plan and momentum for getting **Space 3 deployed this week** if it isn't already — the same audience-fit move applies from the start of the build, not as polish at the end.
- Your GitHub profile README and Hugging Face Collection one round more polished than they were Sunday morning.
- One source from your Week 7 shortlist run through the three-step verification loop — start of `week-09-citations.md`.
- A clear plan for finishing citation verification and revising one paragraph of `PAPER.md` to better fit the audience you're actually writing for.

## Connections

**Builds on:** Session 8 — *Make It Public.* Tonight assumes you have a profile, your Spaces, a Collection, and a paper draft to keep working on. The audience-design move is the third scale of the fitting problem you experienced twice in Session 8.

**Bridges to:** Session 10 — *Polish, Integrate, and Tell the Portfolio Story.* By Session 10 your Space 3 should be deployed (we use this week to push it across the finish line), your citations should be verified, and your `PAPER.md` should fit your real audience one paragraph at a time. Session 10 is where you polish the ambitious build, integrate your three Spaces and your paper into one coherent project, and start drafting the portfolio narrative that ties it all together. The public-facing system keeps growing through Sessions 10–12, with Demo Day as the front door at the end.

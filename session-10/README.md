# Session 10: Polish, Integrate, and Tell the Portfolio Story
*"Make the Pieces Fit"*

## What This Session Covers

Session 10 continues the turn that began in Session 6. Students are no longer just learning AI concepts by trying tools; they are using their Spaces, journals, sources, and GitHub profiles as evidence for a real research paper.

By now each student should have some version of:

- a research question from Session 6
- a rough `PAPER.md` from Session 7
- a public GitHub/Hugging Face research presence from Session 8
- an audience-fit Space revision and verified citation work from Session 9

Tonight is the integration session. Students make the public system honest: the GitHub profile points to the right work, the Space actually runs, the research journal records what happened, and `PAPER.md` contains one specific claim supported by both a real source and a real result from the student's own Space.

## The Core Teaching Line

> A portfolio is not a list of links. It is a claim about what you are investigating, backed by a working Space, a journal trail, and a paper that tells the truth.

## The Session Flow

The session is deliberately less "new content" and more intervention time. The instructor circulates, diagnoses where each student's system is thin, and helps them make one visible improvement.

### Move 1 — Status Triage

Students open four tabs:

1. GitHub profile README
2. paper repo / `PAPER.md`
3. research journal
4. Hugging Face Space 3, or the strongest current Space if Space 3 is not live

They mark each one:

- **Green:** present, public, and aligned with the research question
- **Yellow:** present but generic, stale, broken, or disconnected
- **Red:** missing or unusable

This triage determines the live intervention. A student with a broken Space debugs the Space. A student with an empty paper writes the paper anchor. A student with strong artifacts but a confusing profile updates the public story.

### Move 2 — Space Evidence

Every student runs the same small evidence loop:

1. choose three inputs a real user would try
2. run them through the Space
3. save the outputs
4. identify one pattern and one failure case

Those outputs are not just demo material. They become evidence for `PAPER.md`: "Here is what my tool did on real inputs, and here is what that shows."

### Move 3 — Paper Integration

Students revise `PAPER.md`, not a separate throwaway draft. The minimum useful change is one paragraph that connects:

- the research question
- one verified source from `week-09-citations.md`
- one result from the student's Space test
- one honest limitation

The goal is not polish. The goal is fit: the paper should sound like it came from the student's actual build, not from a generic AI research template.

### Move 4 — Public Story

Students update the GitHub profile README so a reader can follow the trail:

research question -> paper repo -> working Space -> journal

The profile does not need to be fancy. It needs to be current, specific, and honest about what the student is building now.

### Move 5 — Journal Record

Before leaving, students add or start a Week 10 journal entry that records the integration work:

- what they tested in the Space
- what changed in `PAPER.md`
- which source or claim they used
- what still does not fit
- what they will improve before peer testing

## Where the Technical Concept Lives

The official concept remains **supervised learning and task design**, but it now appears inside the student's own system rather than as a standalone build exercise.

When students choose or revise a Space, they are also choosing:

- a model trained for one task rather than another
- labels or outputs inherited from someone else's dataset
- a user-facing frame that may or may not fit the model's actual behavior
- evidence that may or may not support the paper's claim

That is task design at the portfolio scale. The technical choice is not separate from the writing choice; the model's task shapes what the student can honestly claim.

## Session Resources

- **[`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)** — master AI prompt for paper drafting and revision
- **[`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)** — paper workflow guide
- **[`WEEK-10-RESEARCH-WORK.md`](./WEEK-10-RESEARCH-WORK.md)** — turning verified sources and Space outputs into `PAPER.md` revisions
- **[`BETWEEN-SESSION.md`](./BETWEEN-SESSION.md)** — what to finish before Session 11
- **[`GUIDE-build-planning.md`](./GUIDE-build-planning.md)** — now used as the integration checklist for Space, paper, profile, and journal
- **slides.html / app.py / templates/** — rescue materials for students whose Space still needs a working technical base

## What Students Should Leave With

Every student should leave with at least one concrete improvement in the public system:

- a working or debugged Space URL, or a precise next debugging step
- three real Space outputs saved as paper evidence
- one revised paragraph in `PAPER.md`
- one profile README update that points to the current Space/paper work
- a Week 10 journal entry started

For stronger students, the target is a coherent portfolio spine: profile -> paper -> Space -> journal all tell the same research story.

For earlier students, the target is a rescue path: one working Space, one honest paragraph in `PAPER.md`, and one journal entry that explains what is still unfinished.

## Connections

**Builds on:** Session 6's research question, Session 7's prompt-first `PAPER.md`, Session 8's public profile system, and Session 9's audience-fit and citation-verification work.

**Bridges to:** Session 11 — *Peer Review and Iteration.* Session 11 only works if there is something real for peers to read and test. Session 10 makes that real: a Space that runs, a paper paragraph that makes a claim, and a profile that lets another person find the work.

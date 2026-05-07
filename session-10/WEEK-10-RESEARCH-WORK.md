# Week 10 Research Work

Prereqs: `week-06-research-question.md`, `PAPER.md`, `research-journal.md`, your GitHub profile README, a Hugging Face Space you can test, and `week-09-citations.md`.

This week is not about starting a brand-new research brief from zero. You already have the spine of the project. Week 10 is where the pieces start fitting:

- your Space produces real outputs
- your journal explains what happened
- your verified sources support specific claims
- your `PAPER.md` uses both the sources and the Space results honestly
- your GitHub profile points a reader to the current version of the work

## The temptation

The temptation is to treat the paper, Space, journal, and profile as separate assignments. That is how the project falls apart. A reader should be able to move from your profile to your paper to your Space and feel that they are seeing one investigation from different angles.

The rule for this week:

> Every claim in `PAPER.md` should be backed by either your own Space evidence, a verified source, or both.

## The Week 10 deliverable

Revise `PAPER.md` directly. Also create a short process note called `week-10-integration-notes.md` in the same repo.

Your `week-10-integration-notes.md` is not the final paper. It is the lab record for how you revised the paper this week.

## Move 1 — Claim-Evidence-Source Chain

Open `PAPER.md` and find the main claim your paper is trying to make. If the claim is still vague, write a sharper version at the top of `week-10-integration-notes.md`:

```markdown
## My Claim

My paper argues that ...
```

Then build this chain:

```markdown
## Claim-Evidence-Source Chain

**Claim:** <one sentence your paper currently makes or should make>

**Space evidence:** <one result from my Space that supports, complicates, or challenges the claim>

**Verified source:** <one citation from week-09-citations.md that supports or frames the claim>

**Limitation:** <one reason this evidence is still not enough>
```

If you cannot fill in one of those four lines, that tells you exactly what to fix.

## Move 2 — Run Three Inputs Through Your Space

Choose three inputs a real user would try:

1. **Baseline input** — something you expect the Space to handle well
2. **Interesting input** — something close to your research question
3. **Failure-case input** — something that might confuse the model

Paste the inputs and outputs into `week-10-integration-notes.md`:

```markdown
## Space Evidence

### Input 1 — Baseline
Input:
Output:
What this shows:

### Input 2 — Research Question
Input:
Output:
What this shows:

### Input 3 — Failure Case
Input:
Output:
What this shows:
```

If your Space is broken, do not pretend it works. Make the note:

```markdown
## Space Status

The Space is currently broken. The error is:

<paste the error message>

My next debugging step is:
```

Then revise `PAPER.md` around what you can honestly say: what you intended to test, where the build failed, and what the failure reveals about the system.

## Move 3 — Revise One Paper Paragraph

Pick one paragraph in `PAPER.md` that currently sounds generic. Replace it with a paragraph that uses your chain from Move 1.

A strong Week 10 paragraph has this shape:

```markdown
My project investigates <question>. In my Space test, <specific input/result> showed <pattern>. This matters because <verified source> argues/shows <source claim>. However, my result is limited because <honest limitation>.
```

Do not ask AI to write the paragraph from scratch. You may use AI after you write your own rough version:

> Revise this paragraph for clarity, but do not add claims, do not add citations, and do not remove the limitation. Return the revised paragraph and a one-sentence note explaining what changed.

## Move 4 — Update the Limitations Section

Your limitations section should now include at least one limitation from each category that applies:

- **Model limitation:** what the model was trained to do, and what it was not trained to do
- **Data limitation:** what kinds of examples you tested, and what you did not test
- **Audience limitation:** who the Space is useful for, and who it may not serve well
- **System limitation:** any API, hosted model, Hugging Face runtime, or multi-step pipeline dependency
- **Evidence limitation:** why three Space outputs or a small test set are not enough to prove a broad claim

Use AI as a skeptical reader if it helps:

> Here is my limitations paragraph. Be a skeptical reader. What limitations am I still not admitting? Do not rewrite the paragraph. List the missing limitations.

Then you decide what belongs in the paper.

## Move 5 — Profile and Journal Fit Check

Update your GitHub profile README so the public front door matches the current project:

- research question is current
- Space link works
- paper repo link works
- "What I'm Building Now" says what you are actually doing before Session 11

Then add a Week 10 entry to `research-journal.md`:

```markdown
## Week 10 — Paper/Space Integration

### What I Tested

### What I Added or Changed in PAPER.md

### Which Source I Used

### What Still Does Not Fit

### What I Need Peer Testers to Try in Session 11
```

## What to Bring to Session 11

- Your working Space URL, or the exact error you need help debugging
- Your updated `PAPER.md`
- `week-10-integration-notes.md`
- Your Week 10 journal entry
- Your GitHub profile README with current links
- One specific thing you want a peer tester to try

## Watch Out For

- A profile that links to an old Space while the paper discusses a different project
- A `PAPER.md` that cites real sources but never mentions your actual Space results
- A journal entry that says "I improved it" without naming the input, output, or change
- A limitations section that only says "I need more time"
- AI-generated prose that sounds polished but does not match your actual evidence

## For an Example

Prea's [research journal](../example-student-prea/research-journal.md) and [research brief](../example-student-prea/research-brief.md) show the pattern this week is aiming for: a tool, a test set, a finding, and limitations that make the finding more credible rather than weaker.

---

AI + Research Level 2 • Session 10 Research Work

# Between Sessions 10 & 11

> **What this week is about:** making your public research system ready for another human to test and read. By Session 11, a classmate should be able to open your profile, click into your Space and paper, try one input, and understand what you are investigating.

Session 10 was not a restart. It was an integration checkpoint: Space, paper, journal, citations, and profile all have to fit. This week you finish the integration work and prepare for peer review.

---

## Step 1: Make the Space Testable (30-60 min)

**Goal:** A peer can open your Space, understand what it is for, and get a result.

Open your Space URL.

If it works:

1. Run three test inputs:
   - a baseline input that should work
   - an input tied directly to your research question
   - a failure-case input that might expose a limitation
2. Save the outputs in `week-10-integration-notes.md`.
3. Fix one human-facing surface:
   - title
   - description
   - examples
   - output framing

If it is broken:

1. Open the Hugging Face **Logs** tab.
2. Copy the first real error message.
3. Paste the error into `week-10-integration-notes.md`.
4. Ask an AI assistant for a debugging path.
5. Try one fix in `app.py` or `requirements.txt`.

Do not hide the failure. A broken Space with a clear error and a next step is better than a profile that pretends nothing is wrong.

---

## Step 2: Revise `PAPER.md` Around Real Evidence (45-75 min)

**Goal:** Your paper includes one paragraph that connects your research question, your Space result, one verified source, and one limitation.

Use [`WEEK-10-RESEARCH-WORK.md`](./WEEK-10-RESEARCH-WORK.md) for the full workflow.

Minimum required revision:

1. Open `PAPER.md`.
2. Find one generic paragraph.
3. Replace it with a paragraph that includes:
   - what your project investigates
   - one actual result from your Space
   - one verified citation from `week-09-citations.md`
   - one honest limitation
4. Commit the change.

If your `PAPER.md` is still extremely rough, do not wait for the perfect draft. Add one honest paragraph now. The paper grows by making real claims one at a time.

---

## Step 3: Write `week-10-integration-notes.md` (20-30 min)

**Goal:** Leave a clear record of what changed this week.

Create `week-10-integration-notes.md` in your paper repo:

```markdown
# Week 10 Integration Notes

## Current Research Question

## Space Evidence

### Baseline Input
Input:
Output:
What this shows:

### Research-Question Input
Input:
Output:
What this shows:

### Failure-Case Input
Input:
Output:
What this shows:

## Source I Used in PAPER.md

## Paragraph I Revised

## What Still Does Not Fit
```

This file helps you explain your process during peer review.

---

## Step 4: Update the GitHub Profile README (20 min)

**Goal:** Your profile is a current front door, not an old snapshot.

Open the special profile repo named after your GitHub username. Update:

- **What I'm Researching** — current research question
- **Spaces I've Built** — working Space links, with one-line descriptions
- **Paper** — link to the repo containing `PAPER.md`
- **Research Journal** — link to `research-journal.md`
- **What I'm Building Now** — what you need feedback on in Session 11

The reader should not have to guess which Space is your main project.

---

## Step 5: Week 10 Journal Entry (20 min)

Add this entry to `research-journal.md`:

```markdown
## Week 10 — Paper/Space Integration

### What I Tested

### What I Changed in PAPER.md

### What Source I Used

### What Still Does Not Fit

### What I Want Peer Testers to Try
```

Specifics matter. "I tested three anime scene prompts and the model handled mood better than motion continuity" is useful. "I tested my Space" is not.

---

## Optional Stretch

If Steps 1-5 are done:

- Add a screenshot or short output table to `PAPER.md`.
- Add one more verified source to `week-09-citations.md`.
- Ask someone outside class to try the Space and record what confused them.
- Update your Hugging Face Collection notes so the models in the Collection explain your model choice.

---

## What to Bring to Session 11

- Your GitHub profile URL
- Your main Space URL, or the exact error message if it is broken
- Your updated `PAPER.md`
- `week-10-integration-notes.md`
- Your Week 10 journal entry
- One specific peer-testing request: "Try this kind of input and tell me whether the output helps."

---

## What Session 11 Picks Up

Session 11 is peer review and iteration. Your classmates will not only test whether the Space runs; they will test whether the whole system makes sense to another person.

The question for Session 11:

> When someone else reads your profile, tries your Space, and opens your paper, do they see the same investigation you think you are doing?

That is the fitting problem again, now with a real reader.

---

AI + Research Level 2 • Session 10: Polish, Integrate, and Tell the Portfolio Story

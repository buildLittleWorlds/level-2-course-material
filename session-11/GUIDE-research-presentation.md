# Demo Day Presentation Guide

How to tell the constraint-and-move story in 5-7 minutes.

## What This Is

Demo Day is not a formal research defense. You are presenting an applied build:

> I wanted to build something. The simple version hit a wall. I made a move. The move made something possible, but it also cost something. Here is what I would try next.

This guide matches the Demo Day Presentation assignment in Google Classroom. Use that assignment as the final source of truth.

## The Five-Part Format

You do not need fancy slides. You need a clear walkthrough and real artifacts.

### 1. What I Wanted to Build (45 seconds)

Name the user, task, and more-interesting version.

Use this pattern:

```text
I wanted to build <tool> for <specific user> so they could <specific task>.
```

Examples:

- I wanted to build a tool for a NYSSMA student that gives rubric-aware music practice feedback.
- I wanted to build a tool for a Model UN delegate that preserves competing perspectives in news summaries.
- I wanted to build a tool for an anime fan-artist that compares how different models handle sub-genre style.

### 2. The Constraint (1 minute)

Show the wall. Be concrete.

Good evidence:

- a Space 2 output that is too generic
- a runtime error
- a slow inference time
- a missing or failed API secret
- a model that does not fit on free CPU
- a user-facing output that is technically correct but unusable

Use this pattern:

```text
The rudimentary version could <X>, but it could not <Y> because <constraint>.
```

### 3. The Move (1-2 minutes)

Explain what changed. This is the core of the presentation.

The move might be:

- API delegation
- smaller model
- hybrid pipeline
- different deployment surface
- caching or pre-computing
- task cropping
- runtime repair
- prompt and output redesign

Use this pattern:

```text
The move was to <decision>. That changed the system because <what now happens differently>.
```

Then demo Space 3 if it runs. If it does not run, show the closest evidence: code, logs, screenshot, or before/after plan.

### 4. What It Cost (1 minute)

Every move has a tradeoff. Name it honestly.

Possible costs:

- API dependency
- rate limits
- latency
- privacy concerns
- less model control
- smaller scope
- less accurate output in some cases
- still not enough compute

Use this pattern:

```text
This move made <new thing> possible, but the cost is <tradeoff>.
```

This is the part that makes the project sound real.

### 5. What Is Next (45 seconds)

Name the next wall and the next move.

Use this pattern:

```text
If I kept going, the next constraint would be <next wall>. My next move would be <next decision>.
```

## What to Show

Have these tabs or files ready:

- GitHub profile
- Space 2
- Space 3
- `PAPER.md`
- `research-journal.md`
- Hugging Face Collection
- any screenshot or error message that shows the constraint

You do not have to show everything. Choose the artifacts that make the wall and move easiest to understand.

## Simple Slide Outline

If you make slides, 8-10 slides is enough:

1. Title and one-sentence project
2. Who it is for
3. Space 2: rudimentary build
4. The wall
5. The move
6. Space 3 demo or evidence
7. What changed
8. What it cost
9. What is next
10. Links to profile, paper, journal, Collection

## Preparation Checklist

- [ ] I can say my project in one sentence.
- [ ] I can show or explain Space 2.
- [ ] I can name the wall clearly.
- [ ] I can explain the move as a decision, not just "I improved it."
- [ ] I can demo Space 3, or explain exactly why it is blocked.
- [ ] I can name the tradeoff.
- [ ] I practiced the 5-7 minute version out loud.

## What Makes a Strong Presentation

- **Specific wall.** "Free CPU could not run the image model" is stronger than "it was hard."
- **Specific move.** "I moved image generation to an API and kept Gradio as the interface" is stronger than "I used better AI."
- **Specific evidence.** Show an output, error, screenshot, or test input.
- **Honest tradeoff.** Do not hide the cost.
- **Small next step.** The next move should be believable.

## What You Are Not Being Graded On

- Having a perfect Space.
- Proving a broad claim.
- Sounding like a professional researcher.
- Hiding failures.

The project can be partial and still be strong if the wall, move, cost, and next step are clear.

---

AI + Research Level 2 - Session 11: Test the Move

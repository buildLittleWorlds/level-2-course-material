# Week 10 Research Work: The Wall and the Move

Prereqs: your end-of-course assignments in Google Classroom, one current Hugging Face Space, your paper repo, and your research journal.

This week is not about writing a formal research report. It is about making the applied project legible:

> I wanted to build X. The simple version hit wall Y. I made move Z. Here is what Z made possible and what it cost.

Use this file as a workbench for the Research Paper, Research Journal, Space 2, and Space 3 assignments.

---

## Move 1 - Name Space 2

Space 2 is the rudimentary build. It is the version that works enough to expose the wall.

Fill this in:

```markdown
## My Space 2

Name:
URL:

What it can do:

What I wanted it to do next:

What it cannot do yet:

Why not:
```

If the Space is broken, that can still be the wall. Write:

```markdown
The Space is currently broken. The error is:

My best guess about the cause:

The next fix I will try:
```

---

## Move 2 - Write the Wall Sentence

Write one sentence:

```markdown
This Space can <what it currently does>, but it cannot <the more interesting thing I wanted> because <constraint>.
```

This sentence belongs in three places:

- Space 2 assignment submission comment
- Week 10 journal entry
- Paper section 3, "The constraint"

Good wall sentences are specific:

- "This Space can summarize a short article, but it cannot preserve competing Model UN perspectives because the small summarizer flattens disagreement into one neutral summary."
- "This Space can produce anime scene prompts, but it cannot generate images on free CPU because SDXL-class models exceed the compute available in a free Space."
- "This Space can give a generic health explanation, but it cannot reliably produce parent-friendly guidance because the local model ignores reading-level and safety instructions."

---

## Move 3 - Choose the Move

Pick one move. Do not pick five.

```markdown
## My Move

The move I am trying:

Why this move fits the wall:

What I expect it to make possible:

What it might cost:
```

Common moves:

- Move the heavy step to an API.
- Use a smaller model.
- Split the task into local and hosted steps.
- Change deployment surface.
- Cache or pre-compute expensive outputs.
- Crop the task to one useful version.
- Fix the runtime error blocking the current Space.
- Redesign the prompt and output so a real user can use the result.

Use AI as a planning assistant if helpful:

```text
I am a high school student building a Hugging Face Space. My current Space can [X], but it cannot [Y] because [Z]. Give me three possible engineering moves to get beyond this constraint. Keep them realistic for free Hugging Face Spaces. For each move, name what it would make possible and what it would cost.
```

---

## Move 4 - Run a Tiny Before/After Test

If you have both Space 2 and Space 3 working, test the move.

Use one to three inputs:

```markdown
## Before/After Test

### Input 1

Input:

Space 2 output:

Space 3 output:

What changed:

Did the move help? Why or why not?

What did the move cost:
```

If Space 3 is not working yet, test the debugging path instead:

```markdown
## Space 3 Status

What I tried:

What happened:

Error message or output:

What this tells me:

Next move:
```

The failure is not wasted time. It is evidence of the wall.

---

## Move 5 - Draft the Paper from the Build Record

Open `PAPER.md` and use the Research Paper assignment structure.

Rough notes are fine:

```markdown
# [Title naming the user, the task, and the constraint]

## 1. What I wanted to build

## 2. The rudimentary baseline (Space 2)

## 3. The constraint

## 4. What I tried first

## 5. The move that worked (Space 3)

## 6. What the move cost me

## 7. What I'd do next
```

Use your Week 10 notes to fill sections 2-6. This paper is not a survey of the field. It is a focused record of one wall and one move.

### Where sources fit

If you verified citations in Week 9, use one source to frame the problem or the move. Keep it small:

```markdown
One related source:

What it helps me explain:

One sentence I might use in PAPER.md:
```

The source should support your thinking, not replace your build evidence.

---

## Move 6 - Update the Journal

Add or revise your Week 10 journal entry:

```markdown
## Week 10 - The Wall and the Move

### What I wanted to build

### What Space 2 can do

### The wall I hit

### The move I chose

### What changed when I tried the move

### What the move costs

### What I need peer feedback on
```

---

## What to Bring to Session 11

- Space 2 URL
- Space 3 URL, or a clear blocked-status note
- wall sentence
- move sentence
- one before/after input if possible
- Week 10 journal entry
- rough Paper sections 2-6

---

## Watch Out For

- Saying "it is better" without explaining what changed.
- Hiding a broken Space instead of documenting the error.
- Treating the paper as a literature review instead of a build record.
- Choosing a huge move when a small one would make the project clearer.
- Forgetting to name the tradeoff.

The tradeoff is not a weakness. It is the part that makes the move real.

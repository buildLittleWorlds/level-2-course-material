# Session 10: Find the Wall, Choose the Move
*"Build beyond the constraint"*

## What This Session Covers

Session 10 is not a new assignment and not a formal research reset. The end-of-course assignments in Google Classroom are the guide now. They already name the work correctly:

- Space 1 is where you started in your domain.
- Space 2 is the rudimentary build where the wall becomes visible.
- Space 3 is the post-move build after you decide how to get past the wall.
- The journal, paper, presentation, profile, and Collection all explain the same arc.

Tonight we make that arc concrete for each student. The goal is to leave with a clear sentence:

> My Space 2 can do X, but it cannot do Y because Z. My Space 3 move is to do W.

That is the center of the rest of the course.

## The Core Teaching Line

> Research = managing a constraint. You hit a wall, name it honestly, make a move, and explain what the move made possible and what it cost.

## The Session Flow

This session is mostly live coaching and build time. The assignment posts already tell students what to submit; tonight helps them understand how the pieces fit.

### Move 1 - Open the Assignment Map

Start with the end-of-course assignments in Google Classroom. Students should see that the assignments are not separate chores. They are one story:

1. Space 1 - First Domain Build
2. Space 2 - The Rudimentary Build
3. Space 3 - The Post-Move Build
4. Research Journal
5. Research Paper
6. Demo Day Presentation
7. GitHub Profile
8. Hugging Face Collection

The rest of class is about locating where each student is in that story.

### Move 2 - Identify Space 2 as the Wall

Students open their current strongest or most relevant Space. In many cases this is Space 2. It does not need to be impressive. It needs to reveal a constraint.

The guiding sentence:

```markdown
This Space can <what it currently does>, but it cannot <the more interesting thing I wanted> because <constraint>.
```

Examples:

- This Space can generate generic medical explanations, but it cannot reliably explain at a parent-friendly reading level because the small model does not follow safety and audience instructions consistently.
- This Space can describe a scene, but it cannot make the description change meaningfully by camera angle because the prompt and model mostly swap surface words.
- This Space can generate anime prompts, but it cannot generate images on free CPU because modern image models need more compute than the Space has.

This sentence becomes the submission comment for the Space 2 assignment and the seed of the paper.

### Move 3 - Choose the Move

Students choose one move that could get beyond the wall.

Common moves:

- **API delegation:** Gradio stays on free CPU, but Gemini, Claude, OpenAI, or the HF Inference API handles the heavy step.
- **Smaller model:** use a smaller, distilled, or quantized model that fits where the larger one did not.
- **Hybrid pipeline:** free CPU handles the interface or light classification; an API handles generation, image, speech, or other heavy work.
- **Different deployment surface:** move part of the project to a tool that fits the task better.
- **Caching or pre-computing:** avoid repeating expensive work live.
- **Task cropping:** make the task smaller so the tool can do one useful thing well.
- **Runtime repair:** diagnose the build/runtime error and fix the dependency, secret, or model-loading problem that blocked the Space.

The move does not have to be dramatic. It has to be deliberate.

### Move 4 - Start or Stabilize Space 3

Space 3 is the post-move build. It should do something Space 2 could not do, or it should make one blocked piece work.

During class, students either:

- build the first version of Space 3,
- repair Space 3 so it runs,
- write the README section that explains the move,
- or document exactly why the move is still blocked and what the next debugging step is.

A broken Space with a clear diagnosis is better than a vague claim that everything is fine.

### Move 5 - Record the Decision

Before leaving, students write or start a Week 10 journal entry:

```markdown
## Week 10 - The Wall and the Move

### What I wanted Space 2 to do

### The wall I hit

### The move I chose

### What this move makes possible

### What this move costs

### What I need to test before Session 11
```

This is not formal research prose. It is the build record. The paper grows from this.

## Where Literature and Sources Fit

Sources can help students name the kind of move they are making, but Session 10 is not a literature-review session.

Use literature lightly:

- LoRA, distillation, quantization, caching, and small-model work are examples of making models cheaper or easier to run.
- API delegation is a common production move when local compute is not enough.
- Human-facing redesign can be a real move when the constraint is usability rather than compute.

One verified source from `week-09-citations.md` can frame the paper, but the center is still the student's own wall and move.

## Session Resources

- **Google Classroom end-of-course assignments** - the fixed guide for what students submit
- **[`level-2-sp-26/END-OF-COURSE-ASSIGNMENTS.md`](../level-2-sp-26/END-OF-COURSE-ASSIGNMENTS.md)** - local copy of the assignment structure
- **[`WEEK-10-RESEARCH-WORK.md`](./WEEK-10-RESEARCH-WORK.md)** - notes for naming the wall, move, cost, and next test
- **[`BETWEEN-SESSION.md`](./BETWEEN-SESSION.md)** - what to finish before Session 11
- **[`GUIDE-build-planning.md`](./GUIDE-build-planning.md)** - in-class checklist for Space 2, Space 3, paper, journal, profile, and Collection
- **`app.py` / `templates/`** - rescue materials for students who need a simple working base

## What Students Should Leave With

Every student should leave with at least:

- a Space 2 candidate, or an honest note that the current Space is missing or broken
- one sentence naming what Space 2 cannot do
- a chosen move for Space 3
- a Week 10 journal entry started
- a clear next step for Space 3 before Session 11

Stronger students should also leave with:

- a working Space 3 URL
- a README note explaining the move and tradeoff
- one Paper section revised around the constraint-and-move template
- a GitHub profile update pointing to the current project

## Connections

**Builds on:** Session 8's paper/profile work, Session 9's audience-fit and citation verification, and the end-of-course assignments now live in Google Classroom.

**Bridges to:** Session 11 - peer testing the move. Next session, classmates will test whether Space 3 actually gets beyond the wall Space 2 exposed.

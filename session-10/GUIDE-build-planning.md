# Constraint-and-Move Checklist

How to make Space 1, Space 2, Space 3, the paper, the journal, the profile, and the Collection tell one applied research story.

## Start Here

The end-of-course assignments in Google Classroom are the guide. This checklist helps you work on them during Session 10.

Mark each section:

- **Green:** present and specific
- **Yellow:** present but vague, stale, broken, or disconnected
- **Red:** missing or unusable

The goal is not to make everything perfect tonight. The goal is to name the wall and choose the move.

---

## 1. Space 1 - Where I Started

Space 1 is your first domain build. It shows where your project began.

**Check:**

- [ ] I have a Space 1 URL.
- [ ] It is tied to my interest area.
- [ ] It has a title and description that are not just "test."
- [ ] It can be submitted for the Space 1 assignment, or I know what must be fixed first.

**One-sentence role:**

```markdown
Space 1 shows that I started by exploring <topic/domain> with <basic tool/model>.
```

---

## 2. Space 2 - The Wall

Space 2 is the rudimentary build. It does something real, but it exposes a constraint.

**Check:**

- [ ] I have a Space 2 URL, or I know the exact reason it is missing or broken.
- [ ] I can say what it does.
- [ ] I can say what I wanted it to do next.
- [ ] I can name why it cannot do that yet.
- [ ] Its README or description names the limitation.

**Wall sentence:**

```markdown
This Space can <what it does>, but it cannot <what I wanted next> because <constraint>.
```

**Common constraints:**

- free CPU too slow
- model too large
- weak instruction following
- generic output
- missing domain knowledge
- runtime error
- dependency problem
- missing API secret
- output hard for user to use
- task too broad

---

## 3. The Move

The move is the decision that gets beyond the wall. It can be technical, architectural, or scope-based.

**Check:**

- [ ] I chose one main move.
- [ ] The move directly answers the wall.
- [ ] I can name what it makes possible.
- [ ] I can name what it costs.

**Move sentence:**

```markdown
My move is to <decision>, so that <new thing becomes possible>. The cost is <tradeoff>.
```

**Move menu:**

- API delegation
- smaller model
- hybrid local/API pipeline
- different deployment surface
- caching or pre-computing
- task cropping
- runtime repair
- prompt/output redesign for a named user

---

## 4. Space 3 - The Post-Move Build

Space 3 is the build after the move.

**Check:**

- [ ] Space 3 URL exists, or I know the exact next build step.
- [ ] It does something Space 2 could not do.
- [ ] The README explains the constraint and move.
- [ ] It names the tradeoff.
- [ ] I have at least one input to test in Session 11.

**README note:**

```markdown
## Constraint and Move

The earlier version hit this wall:

The move in this Space is:

What it makes possible:

What it costs:
```

---

## 5. Research Journal

The journal is the running record of attempts and decisions.

**Check:**

- [ ] Week 10 entry exists or is started.
- [ ] It names Space 2.
- [ ] It names the wall.
- [ ] It names the move.
- [ ] It names what the move costs.
- [ ] It says what I need peer feedback on.

**Entry starter:**

```markdown
## Week 10 - The Wall and the Move

I wanted to build...

The rudimentary version can...

The wall is...

The move I chose is...

This makes possible...

The tradeoff is...
```

---

## 6. Research Paper

The paper is a focused write-up of one constraint and one move. It is not a broad literature review.

**Check:**

- [ ] `PAPER.md` uses the seven-section assignment structure.
- [ ] Section 2 names Space 2.
- [ ] Section 3 names the constraint.
- [ ] Section 5 names Space 3 or the planned move.
- [ ] Section 6 names the cost.
- [ ] At least one detail comes from my real build: output, error, timing, model, API, or user-facing failure.

**Paper spine:**

```markdown
Wanted build:

Rudimentary baseline:

Constraint:

Attempted first:

Move:

Cost:

Next:
```

---

## 7. GitHub Profile

The profile is the front door. It should point to the current arc.

**Check:**

- [ ] Profile names the project in one specific sentence.
- [ ] It links to Space 1, Space 2, and Space 3 if available.
- [ ] It links to the paper and journal.
- [ ] It links to the Hugging Face profile and Collection.
- [ ] "What I'm Working On" mentions the wall and move.

**Minimal current section:**

```markdown
## What I'm Working On

- Space 2 showed that <wall>.
- Space 3 tests the move: <move>.
- I am revising my paper around what this move made possible and what it cost.
```

---

## 8. Hugging Face Collection

The Collection is the toolbox you considered.

**Check:**

- [ ] Collection URL exists.
- [ ] It has models or Spaces related to my project.
- [ ] Notes explain why each item mattered.
- [ ] It includes at least one item I considered but did not use.
- [ ] It helps a reader understand the move I chose.

**Tasting-note pattern:**

```markdown
I considered this because...

It helped / did not help because...

Its role in my project is...
```

---

## 9. Peer Testing Request

Before Session 11, write one request for a classmate:

```markdown
Please test this input:

I want to know whether Space 3 does this better than Space 2:

Tell me:
- what changed
- whether the move helped
- what still feels confusing
- what tradeoff you notice
```

---

## Rescue Paths

**If Space 2 is missing:** choose the closest current Space and write the wall from that.

**If Space 2 is broken:** the error is the wall. Copy the log and diagnose one next move.

**If Space 3 is not built:** write the move and build the smallest version.

**If the paper is empty:** fill the seven headings with rough notes.

**If the profile is empty:** add only the current project sentence and links to paper, journal, HF profile, and current Space.

**If citations are weak:** use one verified source lightly. The build evidence carries the paper.

---

## What Good Looks Like

> "My Space 2 generates generic game dialogue, but it cannot keep an NPC voice consistent because the prompt gives no character memory or scene constraints. My Space 3 move is to turn the free Space into an orchestrator: the interface collects genre, role, scene, and tone, then sends a structured prompt to a stronger API model. This makes copy-ready dialogue more likely. The cost is dependency on the API and possible rate limits. In Session 11, I want a classmate to test whether the same NPC sounds consistent across three lines."

That is the story: wall, move, what changed, what it cost, what to test next.

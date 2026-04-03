# Session 11: Iteration, Testing, and Refinement
*Student-Facing Title: "Iterate and Polish"*

**Concept reinforcement:** THE EXPERIMENTATION LOOP
**Narrative Role:** The refinement. Students take their Session 10 builds and make them better through peer feedback and systematic testing. Session 10 ended with: "Next week is about making it better. You'll swap Spaces with someone else. They'll try to break yours — the way we broke models back in Session 3. You'll get feedback you didn't expect. And then you'll iterate. Build, test, improve. That's the experimentation loop — and it's the difference between a prototype and a product." This is that week.
**Space:** No new Space — students improve their Session 10 projects
**Pre-session prep:** Open each student's Space URL in a browser tab. Have the Session 10 rescue templates ready for anyone who doesn't have a working Space. Pull up SpaceCraft and pick a Space that improved dramatically between versions (or a polished Space whose quality clearly comes from iteration).

---

## Time Breakdown (2 hours)

### 0:00–0:03 — SpaceCraft Check-In

Pull up SpaceCraft. Show a Space that clearly improved through iteration — either one with visible version history, or a polished Space whose quality comes from many small refinements.

**Say:** "I added this Space to SpaceCraft. Look at the little things — the examples are specific, the output is formatted for humans, there's a clear description of who it's for. This didn't happen in one draft. This is what iteration looks like. That's what tonight is about — taking what you built and making it better through feedback and real testing."

### 0:03–0:06 — Story So Far

**Scripted bridge (say something like this):**

"Let's step back for a second. Think about where you started. Session 1 — you fed text to a model and it guessed whether the words were happy or sad. Sessions 2 and 3 — you discovered that different models see different things, and that all of them break. Sarcasm, mixed emotions, context they weren't trained on. That was Act I — The Old Way. Small models that sort text into buckets. Brittle."

"Then Act II — the breakthrough. Session 4, you crossed the fork from classification to generation. Session 5, you added the controls — temperature, top-p — the same knobs on ChatGPT. Session 6, you hit the wall: models can't generalize beyond their training data. The breakthrough was training on everything. Session 7, you saw the cost — training on everything means training on every bias. Session 8, you chained two models into a pipeline and watched errors cascade. That's how every AI product you use actually works."

"Act III — you flipped it. Session 9, you stopped studying the machine and started designing for humans. Session 10, you built your own from scratch. And tonight — you iterate. You swap Spaces. You try to break each other's work — the same way you broke models back in Session 3. But this time, it's not to expose limits. It's to make things better. That's the experimentation loop."

"This is how every real AI product ships. Not in one draft. Through loops of testing and feedback. OpenAI didn't ship ChatGPT and walk away — they tested it, got feedback, iterated. That's what you're doing tonight."

### 0:06–0:21 — Quick Demos

Each student shows their Space to the group. ~2 minutes per student.

> **Narrative note:** During compliments and suggestions, connect to course concepts when you can: "You chose a generation model — that's the Session 4 fork." "Your examples test for domain shift — that's Session 6." Students won't always notice the connections themselves. Name them.

**Format for each demo:**
1. What does it do? (one sentence)
2. Show it working (one example input)
3. What's one thing you'd improve?

**Instructor role:** After each demo, lead the group in:
- One compliment ("I like that you...")
- One suggestion ("What if you tried...")

Keep it positive and fast. The goal is to give everyone a moment in the spotlight, not deep critique.

**If a student doesn't have a working Space:**
- No judgment. "That's okay — we'll get you set up in the next block."
- Pair them with the rescue templates from Session 10 (`session-10/templates/`)
- They'll fork a template and customize it during the 1-on-1 time

### 0:21–0:33 — Research Journey Review

Before diving into 1-on-1 feedback, have students review their own research artifacts. This prepares them for the research-framed presentation in session 12.

**Say:** "You've written 9 journal entries and collected 12+ models in your HF Collection. Before we polish the Space, let's look at the research journey that got you here."

**Activity (each student, ~2 min):**
1. Open your HF Collection. How many items? Scroll through — what topic keeps coming back?
2. Open your `research-journal.md` on GitHub. Skim your entries. What question were you circling by Week 9-10?
3. Think about the thread: early entries were exploring broadly, later entries were focusing. Where did that shift happen?

**Instructor prompts while students review:**
- "Look at your Week 2 entry and your Week 10 entry side by side. How different are they?"
- "Can you name your topic in one sentence now?"
- "What method did you use most — comparing models? Testing on different data? Breaking things?"

**Say:** "Next week, you're not just showing a Space — you're presenting a research journey. Your Collection shows breadth. Your journal entries tell the story. Your Space is the artifact that came from all of that."

### 0:33–1:13 — 1-on-1 Feedback and Improvement

~8 minutes per student. Instructor shares screen and works on each student's Space together.

**Rotation plan (5 students):**
| Slot | Time | Student | Others doing... |
|------|------|---------|----------------|
| 1 | 0:33–0:41 | Student A | Testing each other's Spaces |
| 2 | 0:41–0:49 | Student B | Testing each other's Spaces |
| 3 | 0:49–0:57 | Student C | Testing each other's Spaces |
| 4 | 0:57–1:05 | Student D | Testing each other's Spaces |
| 5 | 1:05–1:13 | Student E | Testing each other's Spaces |

**For each student, check this improvement list:**

1. **Title and description** — Does the title make sense to someone who's never seen it? Does the description explain what it does?
2. **Examples** — Are there at least 2-3 example inputs? Do they showcase what the Space does well?
3. **Output formatting** — Is the output readable? Should it include labels, percentages, explanations?
4. **Input validation** — What happens with empty input? Very long input? Weird characters?
5. **Model choice** — Is the model appropriate for the task? Is it fast enough on free CPU?
6. **Model card link** — Add a link to the model card in the description so users can learn more.

**Common fixes to make live:**
- Improve the `placeholder` text in `gr.Textbox` to guide users
- Add more `examples` to the `gr.Interface`
- Add input length checking (`text[:512]`) to prevent timeouts
- Improve the function's return string to be more human-readable
- Fix the README.md to accurately describe the Space

**For students without a working Space:**
1. Pick a rescue template from Session 10
2. Fork it to their account
3. Change the title, description, model, and examples
4. Deploy and verify it works
5. They'll have a working Space for demo day even if it's simpler

### 1:13–1:28 — Peer Testing

Students swap and try each other's Spaces. Share the peer feedback form (see `peer-feedback-form.md`).

**Instructions to students:**
1. Open another student's Space URL
2. Try 3-4 inputs — at least one "normal" input and one "weird" input
3. Fill out the feedback form for each Space you test
4. Be specific — "the output was confusing" is less helpful than "I didn't know what POSITIVE (87%) meant"

**Instructor role:** Float between students, help with any technical issues, encourage specific feedback.

**If time allows:** Have each student read their feedback aloud to the Space owner. This creates accountability and surfaces the best suggestions.

### 1:28–1:43 — Notebook Time

Share the Colab notebook link in the Zoom chat. Students open it and try the debug challenges.

**What they do:**
- Run the setup cell
- Review the improvement checklist and common bugs table
- Try to find and fix the bug in Debug Challenge 1 (result is a list, not a dict — needs `result[0]`)
- Try to find and fix the bug in Debug Challenge 2 (empty string crashes the model — needs an `if not text` check)
- Fill in the "My Improvements" section with what they changed tonight

**Instructor role:** Let students struggle for a couple minutes before giving hints. The goal is recognizing error patterns, not speed.

**Hints if stuck:**
- Challenge 1: "What type is `result`? Try printing it before the return line."
- Challenge 2: "What happens when you pass an empty string to the model? How would you check for that?"

**GitHub skill:** Show how to edit a file directly on github.com (pencil icon). Have each student update their README or another file in their repo.

### 1:43–1:55 — Prep for Demo Day

Explain the format for next week. This is a research presentation, not just a demo.

**Say:** "Next week isn't just about showing your Space. It's about telling the story of your investigation — the question you were circling, the methods you used, what you found. Your Collection, your journal entries, and your Space all come together."

**Demo Day format (5-7 minutes per student):**

```
1. MY QUESTION (30 seconds)
   - What topic did you investigate? What question were you circling?

2. MY JOURNEY (1-2 minutes)
   - Show your HF Collection — how many items? What's the focus?
   - Highlight 2-3 key journal entries. What methods did you use?
   - How did your question evolve from Week 2 to Week 10?

3. MY ARTIFACT (2 minutes)
   - Live demo of your Space with 2-3 inputs
   - Show one input where it works great
   - Show one input where it struggles

4. WHAT I FOUND (1-2 minutes)
   - What did you learn? What surprised you?
   - What are the limitations?

5. WHAT'S NEXT (30 seconds)
   - If you kept going, what would you investigate?
```

**Tips for presenting:**
- Practice with a friend or family member before next session
- Have your inputs ready — don't search for examples during the demo
- Open your Collection and journal before you start — you'll want to show them
- It's okay to show something that doesn't work perfectly. Talking about what broke is more interesting than a flawless demo.
- You're not being graded. This is about showing what you built and what you learned.

**Say:** "You've all built something real that lives on the internet. But you've also done something harder — you followed a question for 10 weeks, documented what you found, and built a tool around it. Next week you get to tell that story."

### 1:55–2:00 — Bridge Forward

**Scripted bridge (say something like this):**

"Eleven sessions. You started by feeding text to a mood-reading model and watching it guess. You broke models with sarcasm. You crossed the fork from classification to generation. You added controls, hit the wall, saw the breakthrough, confronted the cost, chained models into pipelines. You designed for humans and built from scratch. Tonight you iterated — the same way every real product gets better."

"Next week is Demo Day — our last session. You're not just showing a Space. You're telling the story of an eleven-week investigation. Your Collection shows what you explored. Your journal tells how your thinking evolved. Your Space is the artifact that came from all of it. Bring all three."

"One more thing. When you present, think about this: how does your project connect to the bigger story we've been telling? Which concepts from this course showed up in your work? That's not a trick question. It's the whole point."

"Three things before next session: polish your Space, practice your research presentation, and write your final journal entry — the one that ties everything together. Details in the between-session doc."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| Student doesn't have a working Space | Use rescue templates from Session 10. Fork, customize, deploy. |
| 8 minutes per student isn't enough | Prioritize the biggest impact fix (usually title + description + examples). Save code-level fixes for after session. |
| Research Journey Review feels awkward | Students may not have kept up with journals. Don't shame — just help them see the thread: "Even if you only wrote 3 entries, what topic kept coming up?" |
| Peer feedback is too vague ("it's good") | Model specific feedback first: "I like that the examples show different use cases. I'd add a line explaining what the confidence percentage means." |
| Student is discouraged by feedback | Reframe: "Every suggestion is a chance to make it better. Professional developers get code reviews every day." |
| Spaces are asleep (cold start) | Open all student Space URLs 15 minutes before session to wake them up. |
| Student finished early during 1-on-1 rotation | Have them help test another student's Space or add more examples to their own. |
| Students overwhelmed by 5-part presentation | Reassure: "It's 5-7 minutes. Most of it is showing things you already have — your Collection, your journal, your Space." |

---

## Key Vocabulary (reinforce from previous sessions)

- **Iteration** — improving something through repeated cycles of testing and fixing
- **User testing** — having someone who didn't build it try to use it
- **Edge case** — an unusual input that the builder didn't think of
- **UX (user experience)** — how easy and clear the Space is to use
- **Research journey** — the arc from initial exploration to focused investigation to finished artifact

---

## Concept Review (Sessions 1–11)

| # | Session Title | Concept |
|---|--------------|---------|
| 1 | Can a Computer Tell How You Feel? | Input → Model → Output |
| 2 | Not All Feelings Are the Same | Training Data and Representation |
| 3 | What Models Can't Do | Adversarial Testing and the Limits of Classification |
| 4 | What If AI Could Create? | Classification vs. Generation |
| 5 | Add Controls | Hyperparameters |
| 6 | Same Space, Different Worlds | Overfitting and Domain Shift |
| 7 | Who Gets Hurt? | Bias in AI |
| 8 | Chain Two Models Together | Multi-Model Systems and Error Cascades |
| 9 | Make It Actually Useful | Prompt Engineering and Human-AI Interaction |
| 10 | Build Your Own from Scratch | Supervised Learning and Task Design |
| 11 | Iterate and Polish | The Experimentation Loop |

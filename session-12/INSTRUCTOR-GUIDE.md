# Session 12: Demo Day

**Concept:** REFLECTION AND PORTFOLIO
**Narrative role:** The payoff. Students present their research journeys and compile portfolios. This is the culmination of the entire three-act arc — the last thing students do in the course.
**Space:** No new Space — student research presentations and portfolio compilation
**Pre-session prep:** Wake ALL student Spaces 30+ minutes before session. Load each Space URL in a browser tab. Have screenshots of each Space as backup in case any fail to load. Prepare the portfolio template (see `portfolio-template.md`). Have each student's HF Collection URL ready to show.

---

## Time Breakdown (2 hours)

### 0:00–0:03 — Story So Far

This is the last time you walk the arc. Make it land.

**Say:** "Before we start presentations, let me say this one time. Twelve sessions ago, you fed a sentence to a mood-reading model and watched it guess. That was the whole trick — input, model, output. You swapped models and saw different answers. You broke models with sarcasm and learned they don't understand language — they pattern-match. That was Act I: The Old Way."

"Then you crossed the fork. You changed one line of code and a classifier became a generator. You added controls — temperature, top-p — the same knobs on ChatGPT. You hit the wall where models couldn't generalize, and you learned the breakthrough: train on everything. You saw the cost — bias baked into the data — and you chained models into pipelines where errors cascade. That was Act II: The Breakthrough."

"Then you designed for humans, built from scratch, and iterated through peer feedback. That was Act III. Tonight is the last beat. You're not just showing a Space. You're telling the story of a twelve-session investigation."

### 0:03–0:13 — Setup and Tech Check

Open each student's Space URL in tabs. Quick check:
- Does each Space load?
- Is the student ready to present?
- Can they access their HF Collection and research-journal.md?

**If a Space won't load:**
- Check if it's still building (Files tab → check build log)
- If the Space was deleted or broken, use a screenshot and let the student talk through what it did
- Don't let a tech issue derail the session — the story matters more than a live demo

**Order of presentations:** Let students volunteer, or go in reverse alphabetical order (so the same students don't always go first/last). Have the order ready before session starts.

**Say:** "Tonight is your night. Each of you has been investigating a topic for eleven weeks — collecting models, writing journal entries, and building a working AI tool. Let's hear what you found."

### 0:13–1:13 — Student Presentations

5-7 minutes per student. With 5-6 students, this takes 25-42 minutes, leaving buffer for transitions and group testing.

**Presentation format (share this on screen):**

```
1. MY QUESTION (30 seconds)
   - What topic did you investigate?
   - What question were you circling?

2. MY JOURNEY (1-2 minutes)
   - Show your HF Collection — how many items? What's the focus?
   - Highlight 2-3 key journal entries. What methods did you use?
   - How did your question evolve from Session 2 to Session 11?

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

**After each presentation:**
- Group tries the Space with their own inputs (1-2 minutes)
- One round of applause (seriously — they built this)
- Instructor highlights one specific thing they did well — try to highlight something from their research journey, not just the Space itself

**Instructor notes during presentations:**
- Write down each student's research question, Collection URL, Space URL, and one highlight for the portfolio
- Note any research methods the student demonstrates understanding of
- If a student is nervous, prompt them: "Tell us about your Collection — what was the first model you added?"
- If a student skips the journey section, gently redirect: "Before the demo — what question brought you here?"
- If a student finishes early, ask: "What was the most surprising thing you found in your investigation?"

### 1:13–1:38 — Reflection

Group discussion. Go around the room (screen) for each question.

**Reflection questions:**

1. **"What concept surprised you most?"**
   - Prompt: "We covered 11 concepts — from input-model-output all the way to the experimentation loop. Which one changed how you think about AI?"

2. **"What research method was most useful?"**
   - Prompt: "You used 9 different research methods across the course. Which one taught you the most about your own topic?"

3. **"How has your understanding of AI changed since Session 1?"**
   - Prompt: "Remember Session 1? You fed a sentence to a mood-reading model and watched it guess. What do you know now that you didn't know then?"

4. **"What would you investigate next?"**
   - Prompt: "If you had unlimited time and any model on the Hub, what question would you pursue?"

**The 11 ML Concepts:**

| # | Concept | Session | How They Learned It |
|---|---------|---------|-------------------|
| 1 | Input → Model → Output | 1 | Built their first Space |
| 2 | Training Data & Representation | 2 | Swapped models, got different answers |
| 3 | Adversarial Testing & the Limits of Classification | 3 | Broke models with adversarial stories — sarcasm, mixed emotions, no humans |
| 4 | Classification vs. Generation | 4 | Crossed the fork — changed one line from classification to generation |
| 5 | Hyperparameters | 5 | Added sliders, saw output change |
| 6 | Overfitting & Domain Shift | 6 | Same model, different text types |
| 7 | Bias in AI | 7 | Paired sentences, different scores |
| 8 | Multi-Model Systems | 8 | Chained image captioning + sentiment |
| 9 | Prompt Engineering & UX | 9 | Redesigned a Space for a real audience |
| 10 | Supervised Learning & Task Design | 10 | Built from scratch, chose their own model |
| 11 | The Experimentation Loop | 11 | Iterated through peer feedback and systematic testing |

**The 9 Research Methods:**

| # | Research Method | Session | What They Did |
|---|----------------|---------|---------------|
| 1 | Comparative Analysis | 2 | Compared multiple models on same inputs |
| 2 | Adversarial Testing | 3 | Found inputs that break models |
| 3 | Baseline Comparison | 4 | Evaluated models side by side with ground truth |
| 4 | Parameter Sweep | 5 | Systematically changed one variable at a time |
| 5 | Generalization Testing | 6 | Tested models outside their training domain |
| 6 | Fairness Audit | 7 | Designed paired tests for algorithmic bias |
| 7 | Error Propagation | 8 | Measured how errors cascade in multi-model systems |
| 8 | User-Centered Design | 9 | Shifted from "does it work?" to "can someone use it?" |
| 9 | End-to-End System Design | 10 | Chose a question, a method, and built a research prototype |

**Say:** "You didn't learn these from a textbook. You learned them by running into them. Eleven concepts tell you what AI does. Nine methods tell you how to investigate it. You know both now."

### 1:28–1:38 — Reflection Notebook

Share the Colab notebook link in the Zoom chat. Students open it and fill in their portfolio and reflections.

**What they do:**
- Fill in the portfolio table (HF profile, GitHub profile, Collection URL, Spaces they built)
- Answer the reflection questions (concept that surprised them, most useful method, what they'd investigate next)
- Check the GitHub portfolio checklist

**Instructor role:** Help students remember their Space URLs and Collection URLs. Screen-share each student's HF profile page so they can see all their Spaces listed. This is a quiet, reflective moment — give it space.

**If time is short:** Just have them fill in the portfolio table. The reflection questions can be done after the session.

### 1:38–1:55 — Portfolio Consolidation

Help each student compile their portfolio. Use the portfolio template (`portfolio-template.md`).

**What to collect for each student:**
1. Their HF profile URL (huggingface.co/username)
2. Their HF Collection URL with item count
3. URLs for every Space they built or forked
4. Their GitHub repo URL with link to `research-journal.md`
5. A one-sentence description of their research question
6. A one-sentence description of their final Space
7. Which research methods they used most

**How to compile:**
- Screen-share the portfolio template
- Fill it in together for each student (takes ~3 minutes per student)
- Save as a PDF or share the markdown with Bing as the deliverable

**Deliverable for Bing:** One document per student with their Space URLs, Collection URL, research journal link, research question, descriptions, and reflection. This is the consolidated portfolio showing research readiness for Level 3.

**If time is short:** At minimum, collect the Space URLs, Collection URL, and research question. The rest can be added later.

### 1:55–2:00 — Course Closer

This is the last thing students hear in the entire course. Deliver it like a closing statement — not rushed, not casual.

**Say:** "Let me tell you what just happened over twelve sessions. You started in Act I — you fed text to a model and watched it guess. You swapped engines. You broke things with sarcasm and learned that classical models don't understand — they sort."

"Then you crossed into Act II. You changed one line of code and a classifier became a generator. You added controls — the same knobs on ChatGPT. You hit the wall where narrow training couldn't go further, and you learned the breakthrough: train on everything. You saw the cost — bias — and you chained models into pipelines where errors cascade."

"That's the story of how we got from models that sort text into buckets to models that write essays and generate images."

"In Act III, you took all of that and built something. You designed for humans. You built from scratch. You iterated. And tonight, you presented."

"These Spaces are yours. These Collections are yours. This investigation is yours. You didn't just learn about AI. You traced the path that got us here — and you built something along the way."

Thank the students. Thank Bing (program director). Congratulate everyone.

**Final moment:** Open each student's Space one more time on the shared screen. One URL per student, visible to the group. "These are yours."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| Student's Space won't load (asleep/broken) | Have screenshots ready. Let them present from the screenshot and talk through what it did. |
| Student is too nervous to present | Offer to co-present: you share the screen and drive, they narrate. |
| Student skips the research journey parts | Gently prompt: "Before the demo — show us your Collection. What was the first model you added?" |
| Presentations run long | Gently time-keep. "That's great — let's save the rest for Q&A. Who's next?" |
| Presentations run short | Fill with group testing of the Space. "Let's all try it — give me an input!" |
| Student didn't finish their project | Celebrate what they DID build. Even a forked template with customized labels counts. They still have a Collection and journal entries. |
| Student didn't keep up with journal entries | Focus on what they have. Even 3-4 entries show an arc. The Collection alone demonstrates exploration. |
| Portfolio compilation takes too long | Collect just the URLs, Collection link, and research question during session. Fill in descriptions async. |
| Bing (program director) joins the session | Great! Let students present directly to the stakeholder. The research framing makes presentations more impressive. |
| Emotional moment (student proud/upset) | Let it breathe. These kids built something real. That matters. |

---

## Pre-Session Checklist

- [ ] Wake all student Spaces 30+ minutes before session
- [ ] Load each Space URL in a browser tab — verify they work
- [ ] Take screenshots of each Space as backup
- [ ] Have each student's HF Collection URL ready
- [ ] Prepare presentation format slide/screen to share
- [ ] Have portfolio template ready
- [ ] Know the presentation order
- [ ] Have the 11-concept and 9-method recap tables ready for the reflection section

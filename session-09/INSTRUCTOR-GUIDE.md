# Session 9 — Make It Actually Useful

## Concept: PROMPT ENGINEERING AND HUMAN-AI INTERACTION

**Key idea:** The same model can be a confusing demo or a useful tool — the difference is design. Today students learn that *how you present AI output* matters as much as the model itself.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell: Demos vs. Tools

Open the Sentiment Showdown from Session 4. Run a restaurant review through it.

> "Every Space we've built so far is a demo. It says 'POSITIVE 0.97' and... so what? Today we turn a demo into something someone would actually *use*."

Show the Restaurant Review Analyzer side by side. Same model, same review — but the output says "Happy Customer 😊" with a suggested action.

**Talking points:**
- Same model underneath — zero new AI knowledge needed
- The difference is all in how we frame the input, label the output, and explain the result
- This is what "prompt engineering" really means: designing the *human* side of AI

### 0:10–0:30 — Live Redesign Demo

Walk through the transformation step by step on screen:

1. **Title:** "Sentiment Analysis" → "Restaurant Review Analyzer"
2. **Description:** technical jargon → plain English for a restaurant owner
3. **Examples:** random sentences → real restaurant reviews
4. **Output:** "POSITIVE / NEGATIVE" → "Happy Customer / Unhappy Customer" + advice
5. **Visual confidence bar** instead of a bare decimal

Ask students to suggest improvements as you go:
- "What would a restaurant owner want to know?"
- "Is '0.97 confidence' useful to someone who isn't a programmer?"
- "What should the tool *suggest they do*?"

### 0:30–0:50 — Students Brainstorm Their Redesign

Each student picks a direction. They answer three questions:

1. **Who is this for?** (specific person, not "everyone")
2. **What problem does it solve?** (one sentence)
3. **What should the output say?** (not labels — advice)

**Pre-prepared templates** (students can pick one or invent their own):

---

#### Template 1: Restaurant Review Analyzer
- **Audience:** Restaurant owners
- **Title:** "Restaurant Review Analyzer"
- **Description:** "Paste a customer review and get instant feedback on how the customer felt, plus a suggested response."
- **Example inputs:**
  1. "The pasta was absolutely divine and the service was impeccable."
  2. "Waited 45 minutes for cold food. The waiter was rude."
  3. "Food was okay, nothing special. Overpriced for what you get."
- **Output reframe:** "Happy Customer 😊 / Unhappy Customer 😟" + suggested action

#### Template 2: Email Tone Checker
- **Audience:** Students or professionals writing emails
- **Title:** "Email Tone Checker"
- **Description:** "Paste your email draft and check if it sounds professional, friendly, or might come across wrong."
- **Example inputs:**
  1. "Hi Professor, I was wondering if I could get an extension on the assignment?"
  2. "Per my last email, the deadline was yesterday. Please advise."
  3. "Hey! Just wanted to check in and see how things are going with the project 😊"
- **Output reframe:** "Tone: Professional ✅ / Tone: May Need Revision ⚠️" + suggestion

#### Template 3: Journal Mood Tracker
- **Audience:** Someone keeping a daily journal
- **Title:** "Journal Mood Tracker"
- **Description:** "Paste a journal entry and see what mood it reflects. Track how your writing mood changes over time."
- **Example inputs:**
  1. "Today was a really good day. I finished my project early and had lunch with friends."
  2. "I can't believe what happened today. Everything went wrong and I feel so frustrated."
  3. "Not much happened today. Went to class, came home, made dinner. Pretty average."
- **Output reframe:** "Mood: Upbeat 🌞 / Mood: Rough Day 🌧️" + reflection prompt

#### Template 4: Social Media Vibe Check
- **Audience:** Someone about to post on social media
- **Title:** "Social Media Vibe Check"
- **Description:** "Paste your draft post and check the vibe before you publish. Does it come across the way you intended?"
- **Example inputs:**
  1. "So grateful for everyone who came to my birthday party! Best night ever 🎉"
  2. "Honestly can't believe people think this is okay. We need to do better."
  3. "Just finished a 10-mile run. Not bad for a Tuesday morning 💪"
- **Output reframe:** "Vibe: Positive Energy ✨ / Vibe: Might Start Drama 🔥" + suggestion

---

### 0:50–1:20 — Build Time

**Cycling through 5–6 students (~5 min each):**

| Minute | Focus |
|--------|-------|
| 0–1 | Look at what they have so far. Read their title and description aloud. |
| 1–2 | Help them pick/refine example inputs (the examples ARE the design). |
| 2–3 | Help them rewrite the output formatting (the `analyze` function return string). |
| 3–4 | Test with one input. Does the output make sense to the *audience*? |
| 4–5 | Suggest one improvement, move on. |

**If a student is stuck:** Have them fork the Restaurant Review Analyzer and just change the title, description, and examples. That alone teaches the concept.

**If a student is ahead:** Challenge them to add a second output — e.g., a "what to do next" suggestion based on the confidence score.

### 1:20–1:40 — Test with Audience in Mind

Each student reads their Space's description aloud. Class answers:

- "Would a [restaurant owner / email writer / journal keeper] understand this?"
- "What's confusing?"
- "What's missing?"

**The key question:** "If you handed this to someone who doesn't know what AI is, would they be able to use it?"

### 1:40–1:55 — Name the Concept

> "Everything we did today has a name in the AI world: **prompt engineering** and **human-AI interaction design**."

**Talking points:**
- Prompt engineering isn't just about talking to ChatGPT — it's about designing the entire experience around an AI model
- The model doesn't change. The *interface* changes everything.
- Real AI products spend more time on UX than on the model
- This is why AI companies hire designers, not just engineers

**Concept card:**
| Concept | What It Means | What We Did |
|---------|--------------|-------------|
| Prompt Engineering | Designing inputs and framing to get useful outputs from a model | Changed examples, descriptions, and output labels |
| Human-AI Interaction | Designing how humans and AI systems communicate | Made output actionable, added confidence bars, wrote for a specific audience |

### 1:40–1:55 — Notebook Time

Share the Colab notebook link in the Zoom chat. Students open it and run the setup cell together.

**What they do:**
- Run the setup cell to load the sentiment model
- Fill in the design worksheet cells (audience, purpose, title, examples)
- Try modifying the `format_for_audience` function to match their chosen audience
- Test with a few inputs

**Instructor role:** Walk through the first couple cells together on screen, then let students work. Check in with anyone who seems stuck.

**If time is short:** Just have them fill in the design worksheet cells (markdown only — no code needed). They can run the code cells between sessions.

### 1:55–2:00 — Between-Session Suggestion

> "Have someone outside the class try your Space. Don't explain it — just give them the URL and watch. What confused them?"

---

## Pre-Session Prep

- [ ] Have the Restaurant Review Analyzer deployed and running
- [ ] Have the Sentiment Showdown (Session 4) URL ready for comparison
- [ ] Print or screen-share the four template options
- [ ] Test all example inputs to make sure they produce reasonable outputs
- [ ] Have the four template `.py` snippets ready to paste for students who want them

## Instructor Tips

- **The hardest part is scoping.** Students will want to build something new. Redirect: "Same model, new frame."
- **Examples are the design.** If a student can write three good examples, the Space is 80% designed.
- **Don't let perfect be the enemy of deployed.** A renamed Space with new examples IS the lesson.
- **The "hand it to someone" test is powerful.** If a student can't explain their Space in one sentence, the design needs work.

## Concept Review (Sessions 1–9)

| # | Session | Concept |
|---|---------|---------|
| 1 | Deploy First Space | INPUT → MODEL → OUTPUT |
| 2 | Swap Models | Training Data and Representation |
| 3 | Break It on Purpose | Data Cleaning and Feature Engineering |
| 4 | Two Models Disagree | Model Evaluation |
| 5 | Add Sliders | Hyperparameters |
| 6 | Same Space, Different Text | Overfitting and Domain Shift |
| 7 | Paired Sentence Tests | Bias in AI |
| 8 | Chain Two Models | Multi-Model Systems |
| 9 | Make It Actually Useful | Prompt Engineering and Human-AI Interaction |

# Bluest Hour — Research Path

This guide is the Session 6 bridge from "I built a thoughtful app" to "I have a research question I can actually test." The project already has the ingredients. The work now is to turn those ingredients into an investigation.

Before you start, open the two live versions side by side:

- **GitHub Pages:** [buildlittleworlds.github.io/bluest-hour](https://buildlittleworlds.github.io/bluest-hour/)
- **Hugging Face Space:** [hf.co/spaces/profplate/bluest-hour](https://hf.co/spaces/profplate/bluest-hour)

---

## Step 1: Upgrade Your Observations

Right now the Bluest Hour project invites a kind of response that sounds like:

> "I like the feeling of the app. It makes the blue hour feel special. I think the journaling feature is cool."

That is a real response, but it is not research writing yet.

Use the live app while you do this step. Click through the prediction flow, type a couple of journal entries, and notice whether the GitHub Pages version and Hugging Face version feel the same or different.

What you need to do is extract the **hidden question** from what you already built. Use the same four prompts the Session 6 slide conversation is built around:

1. **What did I expect?**
2. **What actually happened?**
3. **Why did that happen?**
4. **What question does this raise?**

### Example 1: The Journal Feature

**Descriptive version:**

> "I added a journaling box and sentiment analysis so the app could say whether the walk reflection was positive or negative."

**Analytical version:**

> "I added a journaling box expecting the sentiment model to help track mood after evening walks. But reflective writing about light, memory, or calm may not behave like ordinary opinion text. A sentence like 'The light was fading and everything felt quiet and strange' might be contemplative rather than clearly positive or negative. This raises a question: when people write reflective blue-hour journal entries, does a generic sentiment model actually capture mood, or does it flatten a more complex kind of writing?"

### Example 2: The Timing Prediction

**Descriptive version:**

> "The app predicts the best time to start the walk based on civil and nautical twilight."

**Analytical version:**

> "The app predicts the walk time from astronomical twilight data, but then shifts that prediction with a local offset based on observation. That means the app already assumes that the mathematically calculated midpoint is not the same as the perceptually 'bluest' moment. This raises a question: how much does the observed bluest moment differ from the astronomical prediction, and how consistent is that difference across dates and conditions?"

### Example 3: The Mood Claim

**Descriptive version:**

> "The app seems like it could help people feel calmer or more reflective."

**Analytical version:**

> "The app is designed to shape behavior by encouraging a specific kind of evening walk and reflection. But right now that is an intuition, not evidence. This raises a question: do journal entries written after blue-hour-timed walks differ from entries written after ordinary evening walks in mood, calmness, sensory detail, or self-reported reflection?"

**What to do now:** write 3 short bullets beginning with:

- "I expected..."
- "What happened instead..."
- "This raises the question..."

That is the first real move toward a research brief.

---

## Step 2: Sharpen a Research Question

The Session 6 slides move students from **broad** to **medium** to **narrow**. Do the same here.

### Option A: Broad

**How can a place-based AI app change the way people experience an evening walk?**

This is real, but too broad. It includes design, mood, behavior, weather, place, and reflection all at once.

### Option B: Medium

**When people journal after a blue-hour-timed walk, does the writing differ from ordinary evening journaling in a way that a generic sentiment model can detect?**

This is much better. It gives you:

- a comparison: blue-hour-timed walk vs. ordinary evening walk
- a data source: journal entries
- a model question: does sentiment analysis work in this domain?

### Option C: Narrow (Recommended)

**Across 10–20 evening journal entries written after blue-hour-timed walks and non-blue-hour evening walks, do self-reported mood and reflective quality differ, and does a generic sentiment model align with those differences or flatten them?**

This is narrow enough to actually test. It has:

- a plausible sample size
- two conditions
- two kinds of evidence: human judgment and model output
- the possibility of being wrong

### Why this is the best Session 6 model

It mirrors exactly what you want students to learn:

- the app already exists
- the student already noticed something interesting
- the interesting thing turns out not to be "can I build it?" but "does the model measure what I think it measures?"

That is a very teachable research turn.

---

## Step 3: Connect to Published Research

Once the question is sharper, the next move is to go find out who else has studied something nearby.

You do not need papers on "The Bluest Hour" specifically. You need papers that touch the parts of the question:

### Use Consensus For This Step

Go to [Consensus](https://consensus.app/).

Consensus is useful here because it is built as an academic search engine rather than a general chatbot. It searches a large database of peer-reviewed research papers, then uses AI to help synthesize the relevant findings with citations. For Session 6 purposes, that makes it a very good bridge between:

- **"I have a hunch"**
- **"I can name a research question"**
- **"I found papers that prove this is a real research area"**

### How To Use Consensus Well

Think of Consensus as a **research search engine**, not as a place to ask for final answers immediately.

#### A practical workflow for students

1. **Start with your medium or narrow question, not your broad topic.**
   - Bad: `blue hour`
   - Better: `sentiment analysis reflective writing`
   - Even better: `Does nature exposure improve mood?`

2. **Try both a natural-language question and a keyword version.**
   - Natural language often works well for finding the right conceptual neighborhood.
   - Keyword searches can help when the first results are too broad.

3. **Use yes/no style questions when they fit.**
   - Consensus can show a Consensus Meter for questions like:
     - `Does walking in nature improve mood?`
     - `Does outdoor light exposure affect mood?`
   - That is useful for quickly seeing whether the literature tends to lean one way, but students should still click into the actual papers.

4. **Use Quick first, then Pro or Deep if the question is promising.**
   - **Quick** is good for first orientation.
   - **Pro** is better once you know the direction and want a stronger synthesis.
   - **Deep** is useful if you are getting serious about a literature review and want the tool to break the topic into sub-questions.

5. **Open and save papers that feel closest to the actual project.**
   - The goal is not to collect a giant pile of papers.
   - The goal is to find 3 to 5 papers that clearly connect to the question the student is actually asking.

6. **Record the result in the journal immediately.**
   - For each useful paper, write:
     - title
     - authors
     - what question the paper asked
     - one important finding
     - how it connects to Bluest Hour

### How Consensus Helps Focus The Question

Consensus is not only for finding sources after the question is finished. It can also help sharpen the question itself.

Use it in this order:

1. **Search the broad hunch.**
   - Example: `nature exposure mood`
2. **Notice what the literature actually studies.**
   - mood?
   - calmness?
   - circadian rhythm?
   - wellbeing?
   - journaling?
3. **Rewrite the question using the language the literature uses.**
   - Instead of: "Does this app make people feel better?"
   - Move toward: "Do blue-hour-timed walks change self-reported mood or reflective quality?"

That move matters. It is how a poetic observation becomes a researchable question.

### Search directions

- **Nature exposure and mood**
  - `"nature exposure mood ecological momentary assessment"`
  - `"walking in nature positive affect study"`
- **Evening light and human wellbeing**
  - `"evening light exposure mood circadian review"`
  - `"outdoor light exposure mood study"`
- **Reflective writing and measurement**
  - `"sentiment analysis reflective writing"`
  - `"emotion classification journal entries"`
- **Digital wellbeing and journaling**
  - `"digital journaling wellbeing study"`
  - `"smartphone mood tracking nature study"`

### Good Consensus Searches For Bluest Hour

Start with these in Consensus:

- [nature exposure mood ecological momentary assessment](https://consensus.app/search/)
- [Does walking in nature improve mood?](https://consensus.app/search/)
- [evening light exposure mood circadian review](https://consensus.app/search/)
- [sentiment analysis reflective writing](https://consensus.app/search/)
- [emotion classification journal entries](https://consensus.app/search/)
- [digital journaling wellbeing study](https://consensus.app/search/)

Because Consensus search results are query-driven, students should paste the exact query into the search bar rather than expect these links to pre-fill the whole search.

### A Bluest Hour-Specific Consensus Mini-Sequence

If you were modeling this live for students, a clean sequence would be:

1. Search: `Does walking in nature improve mood?`
   - This shows the project lives in a real evidence base.
2. Search: `outdoor light exposure mood study`
   - This narrows toward evening light and timing.
3. Search: `sentiment analysis reflective writing`
   - This introduces the measurement problem.
4. Search: `emotion classification journal entries`
   - This helps test whether the model-choice question is already a research question of its own.

After those four searches, the question usually gets sharper:

- not "Is Bluest Hour a nice app?"
- but "Can a generic sentiment model validly analyze reflective writing about blue-hour walks?"

### What you're looking for

- papers on whether outdoor or nature exposure affects mood or calmness
- papers on whether light timing affects mood, sleep, or circadian rhythms
- papers on whether sentiment analysis works well on reflective or diary-like writing
- papers that use methods students could imitate on a small scale, like self-report, journaling, or experience sampling

### What to write down

For each paper:

- title and authors
- what question they asked
- how that question connects to Bluest Hour
- one finding you might cite later
- one note on method: survey, experiment, systematic review, EMA, model comparison, etc.

You are not trying to become an expert overnight. You are trying to prove that your question lives in a real research neighborhood.

---

## Step 4: What Your Three Spaces Should Look Like

Right now Bluest Hour is one project. For the portfolio, it should become three connected Spaces.

### Space 1 — Baseline

**Bluest Hour Predictor**

What it does:
- predicts the walk time from twilight data
- shows the local offset
- no AI interpretation yet, or only the minimal journaling layer

Why it matters:
- this is the clean baseline
- it proves the place-based and astronomical core of the project
- it can point back to the live versions you already have:
  - [GitHub Pages](https://buildlittleworlds.github.io/bluest-hour/)
  - [Hugging Face Space](https://hf.co/spaces/profplate/bluest-hour)

### Space 2 — The Experiment

**Blue Hour Journal Analyzer**

What it does:
- collects a short reflection after the walk
- runs one or more mood/emotion models on the same text
- lets the user compare self-rating vs. model rating

Why it matters:
- this is where the research question lives
- you are not just observing the app anymore
- you are testing whether the model is valid for this kind of writing

### Space 3 — The Full Version

**Seasonal Reflection Lab** or **Blue Hour Mood Tracker**

What it does:
- combines timing, journaling, self-rating, and model analysis
- stores entries over time
- visualizes whether blue-hour timing, season, or day length changes the pattern

Why it matters:
- this is where the project becomes a system, not just a demo
- it shows what you learned from Space 1 and Space 2

The arc should be:

1. predict the moment
2. test what the journaling/model layer is actually measuring
3. build the richer version based on what you learned

---

## Step 5: Your Unique Angle

What makes Bluest Hour interesting is not just that it uses AI. It is that it sits at the intersection of:

- astronomy
- local observation
- contemplative design
- mood/reflection measurement

Most student Spaces are general. This one is not. It is anchored to a real place, a real time of day, and a real experience.

That creates a strong **domain** for Session 6:

- the model's domain is generic sentiment text
- the student's domain is reflective writing about evening light, calmness, and perception

If those two domains do not match, that mismatch is the research question.

This is the exact Session 6 concept in miniature.

---

## Step 6: What The Research Turn Looks Like Here

You do not need to begin with a polished question. You can begin with a hunch:

> the model sees positive/negative words but not the kind of reflection this app is trying to create

That is already a strong Session 6 starting point.

The research turn in this folder looks like this:

- **Observation:** the app creates a reflective kind of writing
- **Gap:** a generic sentiment model may not measure that writing very well
- **Literature search:** use Consensus to find how researchers study mood, nature exposure, and reflective writing
- **Question:** turn the gap into one sentence that could actually be tested

You do not need to finish the whole research project tonight. You do need to leave with a question that starts with:

**"I want to find out whether..."**

---

## What Comes Next

After you choose the question:

1. write `week-06-research-question.md`
2. write a short Week 6 journal entry about what observation led you there
3. use the prompts in `SPACE-PROMPTS.md` to decide what Space 2 should actually test

If you can do those three things, Bluest Hour becomes more than a lovely app. It becomes research.

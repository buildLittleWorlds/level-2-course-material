# Session 1: From Rules to Models
*Student-Facing Title: "Can a Computer Tell How You Feel?"*

**Concept:** INPUT → MODEL → OUTPUT
**Space:** Mood Meter (pre-built demo)
**Model:** `distilbert-base-uncased-finetuned-sst-2-english` (sentiment analysis)
**Pre-built Spaces:** [profplate/mood-meter](https://huggingface.co/spaces/profplate/mood-meter) and the five bonus Spaces listed below

---

## Time Breakdown (2 hours)

### 0:00–0:25 — Introductions & Space Tour

Welcome students. Quick intros: name, grade, one thing you've used AI for.

Then tour the five Spaces you built for this course. Share your screen and visit each one live. These are all sentiment-related Spaces — students will explore them on their own devices too.

| Space | URL | What to try |
|-------|-----|-------------|
| Image Color Mood Analyzer | https://huggingface.co/spaces/profplate/image-color-mood-analyzer | Upload a photo, see what mood the colors suggest (no ML model — just color science!) |
| Emoji Mood Translator | https://huggingface.co/spaces/profplate/emoji-mood-translator | Type a sentence, see your emotions as emojis (28 emotions) |
| Audio Emotion Detector | https://huggingface.co/spaces/profplate/audio-emotion-detector | Record your voice or upload audio, hear how the AI reads your tone |
| Headline Mood Dashboard | https://huggingface.co/spaces/profplate/headline-mood-dashboard | Paste a few headlines, see the emotional profile |
| Story Emotion Arc | https://huggingface.co/spaces/profplate/story-emotion-arc | Paste a paragraph, watch the emotional arc |

**Space Explorer's Field Guide** — for each Space, ask students:
1. What goes in? (text, image, audio, etc.)
2. What comes out?
3. What model powers it? (click the Files tab to find out)
4. What happens if you give it weird input?

**Landing line:** "These are all Hugging Face Spaces. I built them for this course — and by the end, you'll understand every file inside them. But tonight, your job is to explore them like a critic."

**Feelings Beyond Words** (brief aside, ~30 seconds): "Feelings don't just live in text. Music can make you feel things. A photograph can too. Think about how a voice sounds when someone is angry versus when they're excited — you don't need the words to know. We start with words tonight, but by the end of this course, we'll have machines reading feelings from voices and faces."

Give students a few minutes to explore the Spaces on their own devices. Encourage them to try the Field Guide questions on at least two Spaces.

### 0:25–0:40 — Account Setup

Walk students through:
1. Go to [huggingface.co](https://huggingface.co) and create a free account
2. Brief hub tour:
   - **Spaces** page — browse what people have built
   - **Models** page — the library of AI models anyone can use
   - Their **profile** page — this is where their Collections and Spaces will live
   - **Collections** — briefly mention that they'll create one tonight

**Talking points:**
- "Your HF profile is your AI portfolio. Everything you build and curate here is public and yours."
- "Think of the Models page like an app store, except everything is free and open-source."

### 0:40–1:00 — Demo the Mood Meter

Open the pre-built Mood Meter: [profplate/mood-meter](https://huggingface.co/spaces/profplate/mood-meter)

**Demo flow:**
1. Paste one of the examples. Show the result.
2. Ask students to suggest inputs verbally. Try 3–4.
3. Try something that surprises the model — text where the model's reading doesn't match how a human would feel reading it.

**Key question:** "Does the model agree with how YOU feel about this text? Or is it reading something different?"

Let this question hang. Don't answer it yet.

**Pre-prepared inputs to try:**
- Something clearly happy: "I can't believe how lucky I am to have friends like you."
- Something clearly sad: "I don't know why I even bother anymore."
- Something ambiguous: "Walking into school on the first day felt like stepping onto another planet."
- A song lyric the students might know (ask them to suggest one)
- A text message that could go either way: "Thanks for letting me know."

### 1:00–1:15 — Inside the Space

Now open the Mood Meter's **Files tab** and walk students through what makes a Space work. This is a guided tour, not a coding activity — students are reading the code, not writing it.

**Open `app.py` and talk through the key pieces:**

```python
import gradio as gr
from transformers import pipeline
```
**Say:** "Two imports. `gradio` builds the web interface — that's the page you just used. `transformers` loads the AI model — that's the brain."

```python
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```
**Say:** "This one line loads the AI model. `pipeline` is like a shortcut — it handles all the complicated stuff. `sentiment-analysis` is the task. The model name tells it which brain to download."

Walk through the function briefly — input validation, running the model, formatting the result.

**Say:** "That's the whole brain of the app. When you clicked 'Submit' a few minutes ago, this is the code that ran. And `requirements.txt` just lists the three packages it needs."

**Then show the Files tab of one of the bonus Spaces** (e.g., Emoji Mood Translator). Point out:
- Same structure: `app.py` + `requirements.txt`
- Different code inside, but the same pattern: load a model, write a function, build an interface
- "Every Space you've explored tonight follows this pattern. The code is different, but the architecture is the same."
- Bonus: if you showed the Image Color Mood Analyzer, point out that it has NO `transformers` import — it uses color science instead of a neural network. "Not all AI analysis requires a neural network."

**Talking point:** "You don't need to write any of this code right now. But when you look at a Space's Files tab, you can start to see how it works — and that makes you a better critic."

### 1:15–1:35 — Name the Concept + Big Question

#### Name the Concept: INPUT → MODEL → OUTPUT (10 min)

Draw this on screen (or describe it):

```
TEXT (input) → SENTIMENT MODEL (processing) → MOOD READING (output)
```

**Talking points:**
- "Every AI tool you've ever used follows this pattern. ChatGPT: your prompt goes in, text comes out. Image generators: a description goes in, a picture comes out."
- "The Mood Meter: text goes in, a feeling comes out. The model is the engine. We didn't build the engine — we just used it."

**Quick check:** "Can someone give me the input, model, and output for the Emoji Mood Translator?"

Now show the model card for `distilbert-base-uncased-finetuned-sst-2-english`:
- https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- Point out: what it was trained on (SST-2 — movie reviews!), what task it does, who made it
- "This model learned about feelings by reading movie reviews. That's its whole world. When you paste a diary entry, it's reading your feelings through the lens of movie reviews."

#### Big Question: Can a Machine Actually Feel? (15–20 min)

**Set it up:** "The Mood Meter just told us that diary entry was NEGATIVE with 97% confidence. It 'read' the mood. But here's my question: does it actually know what sadness feels like?"

**The Chinese Room** (simplified for teenagers):

"Imagine you're locked in a room. You don't speak Chinese. But you have a giant rulebook. Someone slides a Chinese sentence under the door. You look it up in the book, find the right response, and slide it back. The person outside thinks you understand Chinese. But do you?"

"The Mood Meter is like the person in the room. It gives the right answer — NEGATIVE, 97% — but does it know what sadness is? Has it ever been sad?"

**Let students respond.** Some will say no, it's just math. Some will say maybe, it's doing something close enough. Some will say it doesn't matter if the answer is right. All of these are legitimate positions.

**Push a little further:**
- "If a friend texts you 'I'm fine,' you might know they're NOT fine — because you know them, you know what happened yesterday, you know how they usually text. The model doesn't have any of that. It just has the words."
- "Is that enough? Can you understand a feeling just from words, without ever having felt it?"

**Don't resolve this.** Tell them: "This is the question we're going to carry through the whole course. By Session 12, you'll have a much more complicated answer."

### 1:35–1:50 — Start Your Collection

This is the hands-on activity. Students create their first Hugging Face Collection.

**Walk through together:**
1. Go to your HF profile, click **+ New** → **Collection**
2. Name it "My Sentiment Space Collection" (or similar)
3. Add a short description
4. Go back to one of the Spaces from tonight's tour
5. Click the three-dot menu → **Add to Collection**
6. Write a tasting note — what did you notice? What surprised you?

**Give students 10 minutes to:**
- Add at least one Space to their Collection
- Write a note for it using the Field Guide questions
- Explore at least one more Space on their own

**Share and discuss (5 min):**
- "What Space did you add? What did you write?"
- "Did anyone find something surprising when they explored the Files tab?"
- "What does it feel like to curate rather than just scroll? What does a Collection let you do that just browsing doesn't?"

**Refer students to the PDF:** "The *Create Your First Collection* handout walks you through this step by step, with tips for writing good notes. The *Space Explorer's Field Guide* gives you a framework for evaluating any Space you find."

### 1:50–2:00 — Notebook Time

Share the Colab link in the Zoom chat. This is students' first time opening a notebook.

**Walk through together:**
1. "Click the link — it opens in your browser"
2. "See the cells with code? Hit the play button on the left of the first cell"
3. "Wait for the green check — that means it worked"
4. Run the setup cell and the first experiment cell together on the call

**Say:** "This is a notebook. It's like a document where you can run code. You'll finish the experiments on your own — they're fun, I promise."

**Notebook skill being introduced:** Opening a Colab notebook from a link, running a cell

**GitHub skill being introduced:** "Before next session, create a GitHub account at github.com if you don't have one. We'll use it starting next week."

### 2:00–2:10 — Wrap Up

Share the between-session challenge (see BETWEEN-SESSION.md). Emphasize it's optional but fun.

**Say:** "Before next week: try the Mood Meter with text you actually care about, and add at least two more Spaces to your Collection. Use the Field Guide to write your notes. Next week, we're going to discover that not all feelings are the same — same text, three different models, three completely different answers."

**SpaceCraft preview (1 min):**
If time allows, briefly show the SpaceCraft site: "One more thing — I maintain my own leaderboard of Hugging Face Spaces called SpaceCraft. Every Space on it runs on free CPU, just like the ones you're exploring. It also has a mini textbook that explains how these Spaces were built. Starting next week, I'll show you a new Space from it each session. You can browse it anytime at [buildlittleworlds.github.io/spaceCraft](https://buildlittleworlds.github.io/spaceCraft/)."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| A bonus Space is down or loading slowly | Have backup: show the Mood Meter instead. Note that free CPU Spaces can take a minute to wake up. |
| Student can't create HF account | They can explore Spaces without an account. They can create accounts between sessions. |
| Student can't find Collections | Walk them through: Profile → + New → Collection. It's also in the PDF handout. |
| Student struggles to write a tasting note | Give them the Field Guide questions as a scaffold: "Just answer these four questions about the Space." |
| Model gives unexpected results | That's a feature! "The model doesn't feel the way we do. We'll explore why all course long." |
| Big Question discussion runs too long | Time-box at 20 min. Say: "We're going to come back to this question every single session. We've got 11 more weeks to figure it out." |
| Big Question discussion falls flat | Have a backup: show two model results that disagree with each other (positive text that gets NEGATIVE, or vice versa). "The model was wrong. But HOW was it wrong? What did it miss?" |
| Not enough time for Collection activity | Students can finish between sessions. The PDF has complete step-by-step instructions. |

---

## Session Resources (PDFs)

- **Space Explorer's Field Guide** — framework for evaluating any Hugging Face Space
- **Create Your First Collection** — step-by-step guide to building and annotating a Collection

---

## Key Vocabulary (introduce casually, don't drill)

- **Space** — a web app on Hugging Face
- **Model** — an AI brain trained on data
- **Pipeline** — a shortcut that loads a model and makes it easy to use
- **Sentiment analysis** — the task of reading whether text feels positive or negative
- **Confidence score** — how sure the model is about its answer (0–100%)
- **Collection** — a curated playlist of Spaces and models on your HF profile
- **Gradio** — the Python library that builds the web interface

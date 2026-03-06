# Session 1: Can a Computer Tell How You Feel?

**Concept:** INPUT → MODEL → OUTPUT
**Space:** Mood Meter
**Model:** `distilbert-base-uncased-finetuned-sst-2-english` (sentiment analysis)
**Pre-built fallback:** [profplate/mood-meter](https://huggingface.co/spaces/profplate/mood-meter)

---

## Time Breakdown (2 hours)

### 0:00–0:15 — Introductions & Space Tour

Welcome students. Quick intros: name, grade, one thing you've used AI for.

Then tour 3–4 deployed Spaces. Share your screen and visit each one live. Pick Spaces that connect to emotion and feeling:

| Space | URL | What to try |
|-------|-----|-------------|
| Text to Emotion | https://huggingface.co/spaces/Elegbede/Text_to_emotion_classifier | Type a sentence, see the emotion |
| Sentiment Analysis | https://huggingface.co/spaces/cardiffnlp/twitter-roberta-base-sentiment-latest | Paste a tweet, see positive/negative/neutral |
| ACE-Step Music Gen | https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5 | Generate a short clip — does AI music make you feel anything? |
| Background Removal | https://huggingface.co/spaces/KenjieDec/RemBG | Upload a photo, watch the background vanish |

**Space Observation Card** — for each Space, ask students:
1. What goes in? (text, image, audio, etc.)
2. What comes out?
3. What happens if you give it weird input?

**Landing line:** "These are all Hugging Face Spaces. By the end of tonight, you'll have one too — and yours will try to read how you feel."

**Feelings Beyond Words** (brief aside, ~30 seconds): "Feelings don't just live in text. Music can make you feel things. A photograph can too. Think about how a voice sounds when someone is angry versus when they're excited — you don't need the words to know. We start with words tonight, but by the end of this course, we'll have machines reading feelings from voices and faces."

### 0:15–0:30 — Account Setup

Walk students through:
1. Go to [huggingface.co](https://huggingface.co) and create a free account
2. Brief hub tour:
   - **Spaces** page — browse what people have built
   - **Models** page — the library of AI models anyone can use
   - Their **profile** page — this is where their Spaces will live

**Talking points:**
- "Your HF profile is your AI portfolio. Everything you build here is public and yours."
- "Think of the Models page like an app store, except everything is free and open-source."

### 0:30–0:45 — Show the Finished Space

Open the pre-built fallback: [profplate/mood-meter](https://huggingface.co/spaces/profplate/mood-meter)

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

### 0:45–1:15 — Build It Live

Create a new Space on HF from scratch:

1. Click **New Space** on HF
2. Name it `mood-meter`
3. Select **Gradio** as SDK
4. Choose **Public** and **Free CPU**
5. Click **Create Space**

Now open the Files tab and create `app.py`. Type the code line by line. Explain each piece as you go:

```python
import gradio as gr
from transformers import pipeline
```
**Say:** "We're importing two tools. `gradio` builds the web interface — that's the page people see. `transformers` loads the AI model — that's the brain."

```python
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```
**Say:** "This one line loads the AI model. `pipeline` is like a shortcut — it handles all the complicated stuff. `sentiment-analysis` is the task — we're telling it: your job is to read feelings. The model name tells it which brain to download."

```python
def check_mood(text):
```
**Say:** "Now we write a function. Text goes in, a mood reading comes out."

Walk through the rest of the function:
- Input validation ("what if someone clicks with no text?")
- Running the model (`analyzer(text)[0]` — one line does all the work)
- Getting the label and score ("the model gives us two things: a label — POSITIVE or NEGATIVE — and a confidence score — how sure it is")
- Adding emoji ("we add a face to make the output friendlier")
- Formatting the return string

**Say:** "That's the whole brain of our app. Five lines of real logic. The model does the hard part."

Then the Gradio interface:
```python
demo = gr.Interface(
    fn=check_mood,
    inputs=gr.Textbox(lines=8, placeholder="Paste any text here..."),
    outputs=gr.Textbox(label="Mood Reading"),
    title="Mood Meter",
    description="Paste any text and this AI will tell you whether it feels POSITIVE or NEGATIVE...",
    examples=[...],
)
demo.launch()
```
**Say:** "`gr.Interface` connects your function to a web page. `fn` is the function, `inputs` is what the user types, `outputs` is what they see. The `examples` give people something to try right away."

Also create `requirements.txt`:
```
transformers
torch
gradio
```
**Say:** "This tells HF what packages to install. Without it, the Space won't know it needs transformers."

Commit and watch the Space build.

**Note:** The build is technically simpler than the original Session 1 (no sentence splitting, no scoring loop — just a single pipeline call). This is an advantage: less time on code means more time for testing and the Big Question. If you want to fill the coding time, add output formatting — emoji logic based on score, or a confidence bar.

### 1:15–1:40 — Test It

Once the Space is live, this is where the session comes alive. Feed the model text that teenagers care about.

**Testing rounds:**

**Round 1 — The Obvious Ones** (5 min)
- "Today was the best day of my life!" → Should be clearly POSITIVE
- "I feel terrible and nothing is going right." → Should be clearly NEGATIVE
- "I went to the store." → What does it say? (Neutral text, but the model has to pick a side)

**Round 2 — Text They Actually Write** (10 min)
- A text message: "k." → Is that positive or negative? (Students will have opinions.)
- A diary-style entry: "I don't know why I even bother anymore. Nothing I do seems to matter."
- A hopeful but uncertain text: "Dear future me, I hope you figured it out."
- Ask students: "Give me something you'd actually text a friend." Try it live.

**Round 3 — Song Lyrics and Quotes** (10 min)
- Ask students to suggest a song lyric. Try it.
- Try a breakup song that sounds positive: lyrics about always loving someone (the words are warm, the context is heartbreak)
- Try something sarcastic: "Oh, I'm having the time of my life right now."
- Try a movie quote students know

**After each result, ask:** "Do you agree? What would YOU say the mood is?"

The gap between the model's reading and the students' reading is the whole point. Don't explain it away — let them notice it.

### 1:40–2:00 — Name the Concept + Big Question

#### Name the Concept: INPUT → MODEL → OUTPUT (10 min)

Draw this on screen (or describe it):

```
TEXT (input) → SENTIMENT MODEL (processing) → MOOD READING (output)
```

**Talking points:**
- "Every AI tool you've ever used follows this pattern. ChatGPT: your prompt goes in, text comes out. Image generators: a description goes in, a picture comes out."
- "Our Space: text goes in, a feeling comes out. The model reads the words and makes a prediction about the mood."
- "The model is the engine. We didn't build the engine — we just told it what to do."

**Quick check:** "Can someone give me the input, model, and output for that emotion classifier Space we saw earlier?"

Now show the model card for `distilbert-base-uncased-finetuned-sst-2-english`:
- https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- Point out: what it was trained on (SST-2 — movie reviews!), what task it does, who made it
- "This model learned about feelings by reading movie reviews. That's its whole world. When you paste a diary entry, it's reading your feelings through the lens of movie reviews."

#### Big Question: Can a Machine Actually Feel? (15–20 min)

**Set it up:** "Our Mood Meter just told us that diary entry was NEGATIVE with 97% confidence. It 'read' the mood. But here's my question: does it actually know what sadness feels like?"

**The Chinese Room** (simplified for teenagers):

"Imagine you're locked in a room. You don't speak Chinese. But you have a giant rulebook. Someone slides a Chinese sentence under the door. You look it up in the book, find the right response, and slide it back. The person outside thinks you understand Chinese. But do you?"

"Our Mood Meter is like the person in the room. It gives the right answer — NEGATIVE, 97% — but does it know what sadness is? Has it ever been sad?"

**Let students respond.** Some will say no, it's just math. Some will say maybe, it's doing something close enough. Some will say it doesn't matter if the answer is right. All of these are legitimate positions.

**Push a little further:**
- "If a friend texts you 'I'm fine,' you might know they're NOT fine — because you know them, you know what happened yesterday, you know how they usually text. The model doesn't have any of that. It just has the words."
- "Is that enough? Can you understand a feeling just from words, without ever having felt it?"

**Don't resolve this.** Tell them: "This is the question we're going to carry through the whole course. By Session 12, you'll have a much more complicated answer."

### 2:00–2:10 — Notebook Time

Share the Colab link in the Zoom chat. This is students' first time opening a notebook.

**Walk through together:**
1. "Click the link — it opens in your browser"
2. "See the cells with code? Hit the play button on the left of the first cell"
3. "Wait for the green check — that means it worked"
4. Run the setup cell and the first experiment cell together on the call

**Say:** "This is a notebook. It's like a document where you can run code. You'll finish the experiments on your own — they're fun, I promise."

**Notebook skill being introduced:** Opening a Colab notebook from a link, running a cell

**GitHub skill being introduced:** "Before next session, create a GitHub account at github.com if you don't have one. We'll use it starting next week."

### 2:10 — Wrap Up

Share the between-session challenge (see BETWEEN-SESSION.md). Emphasize it's optional but fun.

**Say:** "Next week, we're going to discover that not all feelings are the same. Same text, three different models — three completely different answers about how it feels."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| HF Space takes 3–5 min to build | Fill time by showing the code in the Files tab. Explain what's happening: "It's downloading the model and installing packages." |
| Student can't create HF account | Use profplate/mood-meter as shared demo. They can create accounts between sessions. |
| Space crashes on deploy | Check `requirements.txt` exists and has all three packages. Check for typos in `app.py`. |
| Model gives unexpected results | That's a feature! "The model doesn't feel the way we do. We'll explore why all course long." |
| Student falls behind during live build | They'll catch up via the pre-built Space. The live build is instructor-led on shared screen. |
| Big Question discussion runs too long | Time-box at 20 min. Say: "We're going to come back to this question every single session. We've got 11 more weeks to figure it out." |
| Big Question discussion falls flat | Have a backup: show two model results that disagree with each other (positive text that gets NEGATIVE, or vice versa). "The model was wrong. But HOW was it wrong? What did it miss?" |

---

## Key Vocabulary (introduce casually, don't drill)

- **Space** — a web app on Hugging Face
- **Model** — an AI brain trained on data
- **Pipeline** — a shortcut that loads a model and makes it easy to use
- **Sentiment analysis** — the task of reading whether text feels positive or negative
- **Confidence score** — how sure the model is about its answer (0–100%)
- **Gradio** — the Python library that builds the web interface

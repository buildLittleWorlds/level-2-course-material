# Session 4: Introduction to Supervised Learning — Classification vs. Generation
*Student-Facing Title: "What If AI Could Create?"*

## Concept: CLASSIFICATION VS. GENERATION

**Space:** Text Generator (distilgpt2 — no controls, just raw generation)
**Narrative role:** The fork in the road. Everything in Sessions 1–3 was classification: sorting inputs into buckets. Session 4 asks: what if the model didn't choose a label but instead produced something new? This is the single biggest conceptual distinction in ML, and it's the one that leads directly to generative AI.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell + SpaceCraft

Ask: "Last week we broke four emotion models three different ways. Did anyone try the adversarial stories on their own? Did you find anything new?"

If yes: share it. Which failure mode was it — tone deafness, emotional flattening, or anthropomorphic projection?

If no: quickly replay one memorable failure from the Session 3 Story Arc demos. Keep it to 2 minutes. The point is to keep the failures fresh — we're about to explain what kind of AI produces them.

**SpaceCraft check-in (2–3 min):**
Pull up SpaceCraft briefly. This week, feature a *text generation* Space from the CPU-only leaderboard — something that writes, not something that classifies. Say: "Notice something different about this Space. It doesn't sort your input into a category. It writes something new. That's what today is about."

> **SpaceCraft textbook link for this session:** [Chapter 3: GPU vs CPU](https://buildlittleworlds.github.io/spaceCraft/gpu-vs-cpu.html) explains why some models run on free CPU and others need expensive GPUs. The short version: small, specialized models work on CPU. That's why we're using distilgpt2 tonight, not GPT-4.

**Transition:** "For three weeks, we've been feeding text to models and watching them sort it into buckets — positive, negative, angry, joyful. Today we meet a completely different kind of AI. One that doesn't sort. It creates."

### 0:10–0:30 — The Wall and the Question (20 min)

**This is the narrative bridge from Act I to Act II. Take your time here.**

**Step 1: Replay the story so far (5 min)**

Say something like: "Let me tell you the story of what we've done so far."

"Session 1: we fed a sentence to a model and it said 'positive' or 'negative.' That's classification — sorting into buckets from a fixed menu. Session 2: we compared different models on the same text and learned that what a model can see depends on what it was trained to see. Different training data, different labels, different answers. Session 3: we tried to break four models with adversarial stories, and we succeeded — three different ways. Tone deafness. Emotional flattening. Anthropomorphic projection. We even wrote code to clean the input, and it helped with formatting but couldn't fix the real problems."

"That's what AI looked like for most of its history. Small models. Narrow tasks. Humans doing enormous work to make them function. And even after all that work, the models don't understand what they're reading. They match patterns in words."

**Step 2: Name the wall (3 min)**

"There's a wall here. Classification models — the kind we've been using — can only choose from a fixed menu. A 3-label model can say positive, negative, or neutral. A 28-label model can say 'admiration' or 'grief' or 'curiosity.' But it's still just choosing from a list someone else created. More labels doesn't mean more understanding."

**Step 3: The spam detector (7 min)**

Read this scenario to students:

> Imagine you built a spam detector for email. You test it on 1,000 emails. 950 are real mail, 50 are spam. Your model predicts "NOT SPAM" for every single email — all 1,000.
>
> **Question 1:** What's the accuracy? (Answer: 95% — it got 950 out of 1,000 correct!)
>
> **Question 2:** Is this a good spam detector? (Answer: No! It never catches any spam.)
>
> **Question 3:** Would you ship this? Why not?

**Discussion points:**
- Accuracy alone can be misleading.
- **False positives** (real email marked as spam) vs. **false negatives** (spam that gets through) — which is worse? Depends on context.
- A missed spam email is annoying. A missed fraud alert is dangerous.
- "This spam detector is a classification model. It sorts emails into two buckets: spam or not spam. And even at 95% accuracy, it's useless. That's the wall."

**Step 4: The question (5 min)**

"So here's the question: what if we stopped sorting into buckets entirely? What if instead of asking a model to choose a label, we asked it to write something new?"

"What if a spam detector didn't just say 'spam' or 'not spam' but could explain: 'This email is suspicious because it asks for your password and the sender's address doesn't match the company domain'?"

"What if instead of labeling a paragraph as 'sad,' a model could write the next paragraph of the story?"

"That's the fork in the road. And that's what we're going to explore today."

### 0:30–1:00 — Build and Explore: The Text Generator Space (30 min — centerpiece)

**This is the session's main event: students see text generation for the first time — and they see where it comes from in the code.**

> **What we're building and why:** You're going to build a new Hugging Face Space live — a simple text generator using distilgpt2. The build is short (about 10 minutes) because the code is simple. That simplicity IS the point. Students will see that the code structure is almost identical to Session 1's Mood Meter — same imports, same pipeline, same Gradio interface — except for one critical change: `pipeline("sentiment-analysis")` becomes `pipeline("text-generation")`. That one-line difference is the fork in the road. The rest of the segment (about 20 minutes) is exploration: feeding the adversarial stories from Session 3 into the generator and comparing what generation does vs. what classification did. The completed code is in `session-04/app.py`.

#### Part 1: The Build (10 min)

**Setup:** Open Hugging Face. Create a new Space called something like `text-generator` (SDK: Gradio, Hardware: Free CPU).

**Show the Session 1 code first.** Pull up the Mood Meter's `app.py` (or show it on screen). Point at the key line:

```python
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```

**Say:** "This is the line that made every Space in Sessions 1 through 3 work. It loads a classification model — a model that sorts text into buckets. We've been living with this line for three weeks. Now watch what happens when we change it."

**Open the new Space's `app.py` in the Files editor. Write (or paste) the code:**

```python
from transformers import pipeline
import gradio as gr

generator = pipeline("text-generation", model="distilbert/distilgpt2")
```

**Pause here.** Point at the screen. Say: "Look at that. Same library. Same `pipeline()` function. But instead of `'sentiment-analysis'`, it says `'text-generation'`. And instead of a model that sorts, we loaded a model that writes. That's the fork."

**Finish the code:**

```python
def generate_text(prompt):
    if not prompt or not prompt.strip():
        return "Type a sentence and watch the model try to continue it."
    result = generator(prompt, max_new_tokens=80, do_sample=True, truncation=True)
    return result[0]["generated_text"]

demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=4, placeholder="Type a sentence or the beginning of a story..."),
    outputs=gr.Textbox(label="What the Model Wrote", lines=8),
    title="Text Generator",
    description="This model doesn't classify — it creates.",
)
demo.launch()
```

**Point out the differences from Session 1:**
- The function returns *generated text*, not a label and a confidence score.
- The output box isn't "POSITIVE (92%)" — it's a paragraph the model wrote.
- There's no fixed menu. The model can write anything.

**Add `requirements.txt`:** Same as Sessions 1–3: `transformers`, `torch`, `gradio`.

**Commit and deploy.** While the Space rebuilds (1–2 minutes), say: "Same two files. Same workflow. `app.py` and `requirements.txt`. But we changed the task type in one line, and the Space does something completely different. That's the power of the pipeline pattern — the architecture stays the same, the task changes."

#### Part 2: Explore the Generator (20 min)

Once the Space is live, open it. Also have the Session 3 adversarial stories handy (ADVERSARIAL-STORIES.md in bonus-hugging-face-spaces).

**Round 1: The sarcastic narrator (7 min)**

Take the opening line of the sarcastic narrator story: *"Monday morning arrived like a gift from the universe — truly, what better way to start the week than with a dead phone alarm and a shower that had apparently decided today was the day to experiment with arctic temperatures."*

Paste it into the text generator. Watch what comes out.

Ask: "What did the model do with this?"

Key observations to draw out:
- The model didn't say "POSITIVE" or "NEGATIVE." It wrote MORE words.
- It probably didn't continue the sarcastic tone — small models struggle with sustained voice.
- But it's doing something classification *can't do at all.* It's creating new text.

**Round 2: The mixed-emotion story (7 min)**

Take the opening of the mixed-emotion story. Paste it in. Watch.

"Last week, the classification models flattened this into one emotion. What did the generator do?"

The generator might produce something tonally inconsistent or weird — that's fine. The point is it's *attempting* to continue a complex emotional narrative, not reducing it to a label.

**Round 3: Student prompts (6 min)**

Let students suggest prompts. Try:
- A simple factual sentence ("The capital of France is")
- Something creative ("Once upon a time, in a city made of glass,")
- Something from their own interests
- Something absurd or unexpected

After each one, ask: "Is this good? Is this useful?" The answer is usually "not really." That's important.

**Land the observation:**

"This model is tiny — 82 million parameters. It's not great. But look at what it's doing that's fundamentally different from everything we've used before. Every model in Sessions 1–3 chose from a menu. This model writes the next word. And the next. And the next. It doesn't have a menu. It has the entire vocabulary of the English language as its possibility space."

"Next week, we'll put our hands on the controls and see what happens when you turn up the temperature on a model like this. Today, we just need to understand what it's doing and how it's different."

### 1:00–1:25 — The Fork in the Road (25 min — core teaching)

**This is the conceptual heart of the session. Use the whiteboard, slides, or screen share for the two-column comparison.**

**The two-column framework:**

| | Classification | Generation |
|---|---|---|
| **What it does** | Sorts input into categories | Creates new content |
| **Output** | One label from a fixed menu | A sequence of new words |
| **Training data** | Input + label pairs (someone decided each label) | Just text — billions of words, no labels |
| **Example** | "This movie is great" → POSITIVE | "Once upon a time" → "there was a small village..." |
| **How it learns** | "When text looks like THIS, the label is THAT" | "After these words, the next word is probably..." |
| **The catch** | Labels are expensive — humans must create every one | Text is everywhere — the entire internet is training data |

**Walk through each row.** Don't rush this. Let students ask questions.

**The training data revelation (key moment):**

"Here's the thing that changed everything. Classification models need labeled data. That means a human being sat down and decided, for every single piece of training data, what the correct label is. 'This tweet is positive.' 'This review is 3 stars.' 'This email is spam.' For the Twitter sentiment model we used, someone labeled 124 million tweets. That's an enormous amount of human work."

"Generation models need... just text. No labels. No humans deciding anything. The model reads a sentence and tries to predict the next word. Then it checks: did it get it right? It adjusts. It reads another sentence. Predicts. Checks. Adjusts."

"When you don't need labels, what can you use as training data?"

Wait for it. Someone will say it: "Everything."

"Everything. Every book. Every website. Every article, every Reddit post, every Wikipedia entry. That's exactly what happened. And that single insight — that you could train a model on *all the text* instead of carefully labeled samples — is what led to ChatGPT, Claude, and every generative AI tool you've ever used."

**Model card comparison (5 min):**

Pull up two model cards side by side:
- Classification: `cardiffnlp/twitter-roberta-base-sentiment-latest` (from Session 2/3)
- Generation: `openai-community/gpt2` or `distilbert/distilgpt2`

Point out differences:
- **Task type:** "text-classification" vs. "text-generation"
- **Training data:** 124M labeled tweets vs. 8M web pages (WebText) — no labels
- **Output:** Fixed labels vs. open-ended text
- **Intended use:** "Sentiment analysis" vs. "Text generation"

"Same platform. Same model card format. Completely different kinds of AI."

### 1:25–1:40 — Name the Concept + Bridge Forward (15 min)

**Name the Concept: CLASSIFICATION VS. GENERATION**

"Everything in Sessions 1–3 was on one side of this fork. Classification. Sorting into buckets. From here forward, we're following what happened when people chose the other path — generation."

"The story of generative AI is the story of what happens when you stop needing labels. When text is your training data, the internet is your classroom. You can train on everything. And when you train on everything, the model gets better at everything — but it also learns every bias, every stereotype, every error in the data. That's the story we're going to follow for the rest of this course."

**Bridge to Session 5:**

"Today we saw a tiny model try to write text. It wasn't great. The outputs were choppy, sometimes nonsensical, sometimes repetitive. But here's the thing — the model we used has 82 million parameters. GPT-4 has over a trillion. Same idea, vastly different scale."

"But scale isn't the only thing that matters. Even with a small model, there are controls — knobs you can turn that change what the model produces. One of them is called *temperature.* Turn it down, and the model plays it safe. Turn it up, and the model takes risks. That's what we do next week."

"Is creativity just controlled randomness? We'll find out."

### 1:40–1:50 — Between-Session Preview + Research Journal (10 min)

Walk through the between-session challenge (see BETWEEN-SESSION.md).

**Key assignment:** Students will explore both sides of the fork. Find a classification model AND a generation model in their Collection. Test them on the same input. Write about what each one does and what the difference reveals.

**Research Journal:** Week 4 entry — what's the difference between classification and generation, in their own words, with examples from today's session.

### 1:50–2:00 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. Run the setup cell (installs transformers)
2. Load distilgpt2
3. Generate text from a simple prompt
4. Try different prompts and observe the variety

**Say:** "The notebook lets you run the same model we just used. Try your own prompts. Notice how the same prompt can produce different outputs each time — that's randomness in the generation process. Next week, we'll learn how to control that randomness."

**Notebook skill being introduced:** Using a text generation pipeline (vs. the classification pipeline from Sessions 1–3)

**GitHub skill being introduced:** Same as before — upload the notebook to `my-ai-portfolio`.

### 2:00 — Wrap Up
- Share the between-session challenge (see BETWEEN-SESSION.md).

---

## Materials Checklist

Before class, have the following open/ready:

- [ ] Hugging Face account logged in, ready to create a new Space for the live build
- [ ] Session 4 `app.py` code open in a text editor or ready to paste (in case the live build hits a snag — you can paste the complete code instead of typing it)
- [ ] Session 1 Mood Meter `app.py` open in a tab (to show the `pipeline("sentiment-analysis")` line for comparison)
- [ ] ADVERSARIAL-STORIES.md open (for the sarcastic narrator and mixed-emotion story openings)
- [ ] Two model cards open in browser tabs:
  - Classification: `cardiffnlp/twitter-roberta-base-sentiment-latest`
  - Generation: `openai-community/gpt2` or `distilbert/distilgpt2`
- [ ] Session 4 slides loaded
- [ ] Colab notebook link ready to paste in Zoom chat
- [ ] SpaceCraft: one CPU-only text generation Space bookmarked for the check-in (browse the leaderboard at buildlittleworlds.github.io/spaceCraft/)

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Space build fails after committing | Check for syntax errors — most common are missing closing parentheses or indentation issues. If stuck, paste the complete `app.py` from the session folder and commit. Say: "Same thing happens to professional developers. You check the error, fix the typo, and rebuild." |
| Space takes too long to build in class | Have a pre-built backup: deploy the Space before class and keep the URL ready. If the live build stalls, switch to the pre-built version. "I deployed this earlier — same code, already running. Let's explore it while the live one catches up." |
| distilgpt2 generates gibberish | Normal for a small model. Frame it: "This is what generation looks like at the smallest scale. Imagine this x10,000." |
| Students ask "but ChatGPT is way better" | "Exactly. Same concept, vastly different scale. ChatGPT uses the same next-word-prediction idea, but with 10,000x more parameters and 1,000x more training data. We'll talk about scale later." |
| Students confused about next-word prediction | Use an analogy: autocomplete on their phone. "Your phone predicts the next word when you text. GPT does the same thing — just with much more context and much more training." |
| The HF Space is slow or down | Use the HF Inference Widget directly on the model page: `huggingface.co/distilbert/distilgpt2`. Or run the notebook live. |
| Student asks "can it do images/music/code?" | "Same idea, different kinds of data. Image generators predict the next pixel (roughly). Code generators predict the next token of code. The concept of generation vs. classification applies across all of them." |
| Student asks about how the model picks the next word | "Great question — that's literally what next week is about. Short answer: it has a probability for every possible next word, and it picks one. HOW it picks is what temperature controls." |

---

## Concept Connections

- **Sessions 1–3:** Classification — sorting inputs into buckets. Students experienced the limits.
- **Session 4 (this session):** The fork. Classification vs. generation. Why generation's training data requirements enabled scale.
- **Session 5 (next):** Hyperparameters — the controls on generation. Temperature, top-p, max length.
- **Session 6 (upcoming):** Domain shift — what happens when models leave their training world. The breakthrough: "train on everything."

---

## Key Vocabulary

- **Classification** — A type of AI that sorts inputs into categories from a fixed menu (positive/negative, spam/not-spam, angry/sad/joyful).
- **Generation** — A type of AI that creates new content by predicting the next word (or pixel, or token) in a sequence.
- **Labeled data** — Training data where a human has decided the correct answer for each example. Required for classification.
- **Next-word prediction** — How text generation models learn: read a sequence, predict what comes next, check, adjust.
- **Parameters** — The internal numbers a model adjusts during training. More parameters = more capacity to learn patterns. distilgpt2 has 82M; GPT-4 has over 1T.
- **False positive / False negative** — Errors in classification. A false positive is a false alarm; a false negative is a missed detection. Which is worse depends on the task.
- **Accuracy** — Percentage of correct predictions. Can be misleading when the data is imbalanced (as in the spam detector example).

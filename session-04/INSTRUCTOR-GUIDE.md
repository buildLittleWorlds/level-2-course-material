# Session 4: Two Models, One Space — Instructor Guide

## Concept: MODEL EVALUATION

**Space:** Sentiment Showdown
**Models:** 3 sentiment models with different training data, compared side by side

---

## Time Breakdown (2 hours)

### 0:00–0:08 — Show-and-Tell

Ask: "Last week you tried to break a model with sarcastic and messy text. Did anyone find an input that surprised them?"

If yes: share it. What was the failure? Was it a noise problem or a meaning problem?

If no: quickly show a failure you found between sessions. Keep it to 2 minutes.

**SpaceCraft check-in (2-3 min):**
Pull up SpaceCraft briefly. Show two Spaces you've been comparing — two that do the same task but with noticeably different quality. For example, two text-to-speech Spaces, or two image generators. Say: "These both do the same thing. Which one is better? How would you decide? That's model evaluation — exactly what we're about to do with sentiment models."

**Transition:** "Today we're putting three sentiment models side by side on the same text. When three judges disagree about how something feels, who's right?"

### 0:08–0:20 — Big Question: When Models Disagree, Who's Right?

**This is the centerpiece discussion for this session. Run it before the build, while energy is high.**

**Read this aloud in two tones of voice:**

> "Thanks for getting back to me."

Read it once sincerely — warm, grateful, like you genuinely appreciate the response.

Read it again passive-aggressively — clipped, icy, like you've been waiting three weeks and you're furious.

**Ask:** "Same words. Completely different feeling. Which one is the real meaning?"

**Let students respond.** They'll say it depends on context, on who's saying it, on what happened before.

**Push further:**
- "If two smart humans can disagree about the feeling behind a sentence, what does it mean for a model to be 'wrong'?"
- "Maybe the model isn't broken — maybe feelings are just genuinely ambiguous."
- "Think bigger: this isn't just about feelings. Any time an AI classifies something — spam vs. not spam, cat vs. dog, positive vs. negative — there are borderline cases where reasonable people would disagree. So what does 'accurate' even mean?"

**The deeper point:** "When we put three models side by side today, they're going to disagree. That disagreement isn't a bug — it's information. It tells us the text is genuinely ambiguous, or that the models learned from different worlds."

**Don't resolve this.** Let it hang. The build will bring it back to life when they see the models actually disagree.

### 0:20–0:30 — The Hook: Watch Models Disagree
- Open the finished Sentiment Showdown Space.
- Type: **"The service was slow but the food was amazing."**
- Watch the three models give different answers.
- Ask: "Which model is right?" (Trick question — they all are, from their own perspective.)
- Try: **"lol this is SO bad it's actually good 😂"** — sarcasm breaks things.

### 0:30–1:05 — Live Build (35 minutes)
This is the most complex build so far — three models in one Space. Budget extra time.

1. **Create new Space on Hugging Face** — "Sentiment Showdown"
2. **Write requirements.txt** — `transformers`, `torch`, `gradio`
3. **Build app.py step by step:**
   - Import libraries
   - Load first model, test it alone
   - Add second model, test both
   - Add third model, write the comparison function
   - Wire up Gradio with 3 output boxes
   - Add examples
4. **Deploy and test**

**Pacing note:** If running long, skip the third model during live build and add it after testing the first two. Students can see the "add another model" pattern.

### 1:05–1:20 — Test and Explore (15 minutes)
Students suggest inputs. Chase disagreements.

**Key teaching moments:**
- "High confidence doesn't mean correct." A model can be 98% sure and still wrong.
- Sarcasm is hard for all three models.
- Mixed-sentiment text ("slow but amazing") forces models to pick a side.

### 1:20–1:30 — Spam Detector Thought Experiment (10 minutes)

**Read this scenario to students:**

> Imagine you built a spam detector for email. You test it on 1,000 emails. 950 are real mail, 50 are spam. Your model predicts "NOT SPAM" for every single email — all 1,000.
>
> **Question 1:** What's the accuracy? (Answer: 95% — it got 950 out of 1,000 correct!)
>
> **Question 2:** Is this a good spam detector? (Answer: No! It never catches any spam.)
>
> **Question 3:** Would you ship this? Why not?

**Discussion points:**
- Accuracy alone can be misleading.
- What matters depends on the task: a missed spam email is annoying, but a missed fraud alert is dangerous.
- **False positives** (real email marked as spam) vs. **false negatives** (spam that gets through) — which is worse? Depends on context.
- "How do we decide if a model is actually good?" → This is MODEL EVALUATION.

### 1:30–1:40 — Read the Model Cards (10 minutes)
Pull up model cards on Hugging Face for all three models. Point out:

- **Training data size and source** — this is WHY they disagree.
- **Intended use** — each model was built for a specific domain.
- **Limitations** — the model creators already know what fails.

**Model Card URLs:**
- Movie Review Model: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
- Twitter Model: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
- Product Review Model: https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment

**Key takeaway:** "The Twitter model was trained on 124 million tweets. The default model was trained on movie reviews. That's WHY they disagree — they learned language from different worlds."

### 1:40–1:52 — Name the Concept + Research Lens

#### Name the Concept: MODEL EVALUATION (7 min)

- We've been doing model evaluation this whole session.
- Evaluation isn't just "is it right?" — it's "right for what? For whom? Measured how?"
- Different metrics for different tasks. Accuracy is just one number.
- "When three judges disagree about how a text feels, the interesting question isn't which judge is right. It's: what does their disagreement reveal about the text?"

#### Research Lens (5 min)

**Say:** "Let me name what we just did in research terms. We ran a **model evaluation** — same inputs, three judges. This is a **baseline comparison**. In research, when you want to know if a tool works, you don't just test it alone — you compare it against other tools on the same data."

**Frame the shared research question:** "Here's the research question we were investigating tonight: *Which sentiment model is most accurate across diverse inputs?* We tested three models side by side, using human judgment as our ground truth. That's model evaluation."

**Bridge to their own work:** "In class, we applied model evaluation to sentiment. For your homework, you'll apply the same method to your own topic — find two or more models that do similar things, test them on the same inputs, and decide which one you trust more. Same method, your question."

### 1:52–2:00 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. Run the setup cell
2. Load the three models one at a time — warn them "this takes a minute, be patient"
3. Run the first showdown comparison together
4. Show them the score table in the notebook — they'll fill it in during experiments

**Say:** "The notebook has all three models ready to go. Try the experiments — especially the sarcasm one. See if you can find the input that causes maximum disagreement."

**Notebook skill being introduced:** Installing packages with `!pip` (first cell), patience with long-running cells

**GitHub skill being introduced:** "Upload this notebook to your `my-ai-portfolio` repo — same as last time."

### 2:00 — Wrap Up
- Share the between-session challenge (see BETWEEN-SESSION.md).

---

## Pre-Prepared Inputs That Cause Disagreement

Use these to demonstrate. Each one triggers interesting model behavior:

| Input | What Happens |
|-------|-------------|
| "The service was slow but the food was amazing." | Mixed sentiment — models pick different sides |
| "lol this is SO bad it's actually good 😂" | Sarcasm + emoji — confuses most models |
| "The movie was fine. Nothing special but not bad either." | Neutral/ambiguous — models handle neutrality differently (movie model has no neutral label!) |
| "I can't believe how terrible this is. Just kidding, it's great!" | Negation + reversal — tests understanding of context |
| "The product arrived on time and works as described." | Factual/neutral — but product model may read it as positive |
| "meh whatever i guess its ok lol" | Casual/informal — Twitter model handles this better |
| "This establishment has consistently failed to meet even the most basic standards of customer service." | Formal negative — all should agree, but confidence levels differ |
| "10/10 would not recommend" | Internet sarcasm — "10/10" looks positive, "would not recommend" is negative |

---

## Technical Notes

- **Memory:** Three models total ~1.5–2GB. This should fit on free HF CPU Spaces (16GB RAM), but models are loaded sequentially at startup to avoid memory spikes.
- **Speed:** First run after deploy is slow (downloading models). Subsequent runs are faster.
- **Token limit:** Input is truncated to 512 characters to stay within model limits.
- **If memory issues occur:** Move model loading inside the function so only one model is in memory at a time (slower but safer). Or replace the largest model with a smaller one.

---

## Concept Connections

- **Session 1–3:** Students learned INPUT → MODEL → OUTPUT with one model at a time.
- **Session 4 (this session):** Same input, multiple models — now we need to evaluate which one is better.
- **Session 6 (upcoming):** Same models, different input domains — domain shift.

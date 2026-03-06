# Session 2: Not All Feelings Are the Same

**Concept:** TRAINING DATA AND REPRESENTATION
**Space:** Emotion Spectrum
**Models used this session:**
1. `distilbert-base-uncased-finetuned-sst-2-english` (binary: POSITIVE/NEGATIVE — Session 1's model)
2. `j-hartmann/emotion-english-distilroberta-base` (7 emotions — trained on tweets)
3. `valhalla/distilbart-mnli-12-3` (zero-shot — students choose their own feeling labels)

**Pre-built fallback:** Have the Emotion Spectrum deployed under profplate/ before class.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell

Ask: "Last week you tried the Mood Meter with text you actually care about. What did you try? Did the model agree with you?"

If students share: celebrate it. Ask follow-up questions:
- "What text did you use?"
- "Did the model's reading match how YOU felt?"
- "Were you surprised by any result?"

If nobody modified anything: that's fine. Show a result you prepared — e.g., a song lyric that the model reads as POSITIVE but is actually from a breakup song. "The model said this is positive. But listen to the context..."

**Transition:** "Last week the Mood Meter only knew two feelings: POSITIVE and NEGATIVE. That's like saying music is either loud or quiet. Tonight we're going to see what happens when we give the model more words for feelings."

### 0:10–0:25 — "What If We Change the Lens?"

Open Session 1's Mood Meter. Remind students how it works — paste text, get POSITIVE or NEGATIVE.

Now the question: "This model sees the world in black and white — good mood or bad mood. But are feelings really that simple? When you're anxious about a test, is that positive or negative? When you're nostalgic about something you lost, which box does that go in?"

Open `app.py` in the Files tab and talk through the change:

**Before (Session 1):**
```python
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```

**After (new model):**
```python
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
```

**Say:** "Same structure, different brain. This model was trained on tweets that people labeled with 7 emotions: anger, disgust, fear, joy, neutral, sadness, surprise. Instead of just positive or negative, it has a bigger vocabulary for feelings."

Commit. Wait for rebuild. Try the same text from last week.

**Talking points:**
- "This model was trained on tweets — so it thinks everything is a tweet. That's its whole world."
- "It knows 7 emotions because someone decided there are 7 emotions worth labeling. We'll come back to that."
- Try: "I stayed up until 4am thinking about what I said to her." Watch what emotion it picks. Ask students: "Is that the right one? What would YOU call that feeling?"

### 0:25–0:40 — Try the Zero-Shot Model

Now swap again:

```python
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")
```

**Say:** "This model is different — it doesn't come with pre-set emotion labels. YOU tell it what feelings to look for. You could say 'check for love, grief, anxiety, hope' and it will score each one."

Demo it with student-suggested feeling labels. Ask: "What feelings should we test for? Give me 4-5."

**The punchline:** Same text, three models, three completely different kinds of answers. One says POSITIVE. One says JOY. One says HOPE. "They all read the same words. Why do they see different feelings?"

**Answer to build toward:** They were trained on different data, with different labels. The binary model only learned positive/negative because that's all its training data had. The emotion model learned 7 feelings because that's how the tweets were labeled. The zero-shot model can look for anything because it was trained on general language understanding.

### 0:40–0:55 — Model Card Reading Activity

Open the model cards for all three models:
- https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
- https://huggingface.co/valhalla/distilbart-mnli-12-3

Give students structured questions to answer for each model:

| Question | Model 1 (binary) | Model 2 (emotion) | Model 3 (zero-shot) |
|----------|------------------|--------------------|---------------------|
| What was it trained on? | | | |
| How many emotion categories? | | | |
| What language(s)? | | | |
| Who labeled the training data? | | | |
| What feelings can it NOT see? | | | |

Go through answers together. Frame the last question: **"Who labeled this training data, and what feelings did they recognize?"**

**Say:** "The people who labeled 50,000 movie reviews only used two labels: thumbs up, thumbs down. The people who labeled tweets decided there are exactly 7 emotions. That means every feeling that doesn't fit into those 7 boxes is invisible to the model."

### 0:55–1:15 — Labeling Challenge

**The activity:** Show 5–6 emotionally complex texts on screen, one at a time. Students call out what emotion they think each one expresses. Write down their answers.

**Pre-prepared texts:**

1. "Just got my test results back... I literally can't even right now"
   - Could be: joy (good results), fear (bad results), surprise (unexpected)
   - Students will disagree — that's the point

2. "I stayed up until 4am reading and I have zero regrets"
   - Could be: joy, surprise (at themselves), neutral
   - The word "zero regrets" is interesting — the model may read the negation differently

3. "lol my flight got cancelled for the third time this week"
   - Could be: anger (frustrated), joy (sarcastic lol), sadness
   - The "lol" throws every model off

4. "Found my childhood diary today. I was a weird kid."
   - Could be: joy (nostalgia), surprise, neutral
   - Nostalgia is not one of the 7 emotions — what happens?

5. "They said they were 'fine' but the way they said it... I know they're not."
   - Could be: sadness, fear, neutral
   - This is about reading between the lines — something the model can't do

6. "My grandmother used to make this recipe. Now I make it for my kids."
   - Could be: joy, sadness, neutral
   - Bittersweet — another feeling that doesn't have a single-word label

After going through them:

**Say:** "You all disagreed on at least some of these. Here's the thing — the people who labeled the training data disagreed too. When the model gets it 'wrong,' sometimes it's because the humans who taught it couldn't agree either."

Then run the same texts through all three models and compare to student answers. "Which model did you agree with most? Which one surprised you?"

### 1:15–1:30 — Build the Emotion Spectrum

Now build the final version of the Space together — the `app.py` that compares all three models side by side.

Walk through the key parts:
- Loading three different pipelines (three different brains, three different training histories)
- The `analyze_feelings()` function that runs each sentence through all three
- The custom labels input for the zero-shot model — "this one lets you define the feelings"
- The Gradio interface with three output boxes

**Say:** "The code is almost the same as last week. We just run the text through three functions instead of one. The structure is identical — `pipeline()` loads a model, a function processes the text, Gradio shows the result."

Commit. Test with student-suggested inputs.

### 1:30–1:45 — Name the Concept + Big Question

#### Name the Concept: TRAINING DATA AND REPRESENTATION (8 min)

**Key points:**
- "Training data is the textbook the model studied from. It can only know the feelings it's been shown."
- "Representation means: what categories did the data use? Positive/negative is a representation. Seven emotions is a different representation. Love/grief/anxiety/hope is yet another."
- "Same text, different representation, different answer. The model doesn't 'understand' feelings — it matches patterns from its training data."

**Quick check:** "If you wanted a model that detects nostalgia, what kind of training data would you need? Who would you ask to label it?"

#### Big Question: Who Decided There Are 6 Basic Emotions? (10–15 min)

**Set it up:** "The 7-emotion model uses categories based on a famous theory by Paul Ekman. In the 1960s and 70s, he traveled the world showing people photographs of facial expressions. He concluded that there are 6 basic emotions that every human recognizes: anger, disgust, fear, happiness, sadness, surprise."

**Voice aside** (~30 seconds): "Here's something interesting — Ekman studied facial expressions, not words. And think about this: when someone says 'I'm fine' in a flat voice, you know they're not fine. You're reading tone of voice, not words. A text model only has the words. What if we had a model that could hear the voice? We'll build that in a few weeks."

"For decades, this was the accepted answer. The tweet model added 'neutral' as a 7th category, but it's basically Ekman's list."

**The challenge:**

"But here's the thing — Ekman's theory has been seriously challenged."

- Lisa Feldman Barrett's research suggests emotions aren't hardwired — they're constructed by your brain based on context, culture, and experience.
- Some cultures have emotions that don't have English translations:
  - German: *Schadenfreude* — pleasure at someone else's misfortune
  - Japanese: *amae* — the sweet feeling of depending on someone who loves you
  - Portuguese: *saudade* — deep longing for something or someone absent
  - Filipino: *gigil* — the urge to squeeze something unbearably cute
- The tweet model was trained on English tweets from mostly American users. What feelings might be invisible to it?

**Ask students:** "Can you think of a feeling you've had that doesn't have a single word for it in English? Something the model's 7 categories would miss?"

Students from different cultural backgrounds will have different examples. Let them share. This is one of the richest discussion moments in the course.

**Don't resolve this.** Say: "The point isn't whether Ekman was right or wrong. The point is: someone chose the categories. And when you build an AI system, the categories you choose determine what feelings are visible and what feelings are invisible."

### 1:45–1:55 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. "Click the link — same as last week"
2. Run the setup cell together
3. Run the cell that loads all three models — point out that this takes a minute
4. Run the first comparison together and look at the three different outputs

**Say:** "The notebook has all three models you just saw. For each experiment, you'll run the same text through all three and record which one you agree with most. There's a cell at the end where you test your own text."

**Notebook skill being introduced:** Running cells in order, reading output from multiple cells, editing code to change inputs

**GitHub skill being introduced:** "Create a repo called `my-ai-portfolio` on GitHub, then upload this notebook to it."

### 1:55–2:00 — Wrap Up

Share the between-session challenge (see BETWEEN-SESSION.md).

**Say:** "Next week, we're going to find out what happens when the model reads text that means the opposite of what it says. Sarcasm, irony, passive aggression — the stuff that starts fights in your group chat. The model has the same problem you do."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| Loading three models exceeds free CPU memory | Load models sequentially in the live demo. The deployed Space loads all three at startup — if it fails, reduce to two models and demo the third separately. |
| Sentiment model output format confuses students | Show the raw output: `[{"label": "POSITIVE", "score": 0.98}]`. Compare to the emotion model output. Point out: same structure, different labels. |
| Model card is too technical | Focus on just the 5 questions in the table. Skip the technical details. |
| Students can't find the model card | Show them: go to huggingface.co, search the model name, click the model page. |
| Emotion model gives odd results on long text | It was trained on tweets (short text). That's a feature of this lesson, not a bug. "This model thinks everything is a tweet." |
| Big Question discussion falls flat | Have a backup: ask students to name a feeling they've had this week. Then check if any of the three models have a label for it. |
| Big Question discussion runs too long | Time-box at 15 min. Say: "We'll come back to this — the question of who defines emotions comes up again when we talk about bias in Session 7." |
| Zero-shot model is slow | It's the largest of the three. If it takes too long, skip it in the live demo and show it in the notebook instead. |

---

## Key Vocabulary (introduce casually)

- **Training data** — the examples a model learned from
- **Representation** — the categories or labels the training data uses
- **Sentiment** — positive or negative feeling
- **Emotion categories** — the specific feelings a model was trained to recognize
- **Model card** — documentation that describes what a model does and how it was trained
- **Fine-tuned** — a model further trained on specific data for a specific task
- **Zero-shot** — a model that can classify text into categories it wasn't specifically trained on

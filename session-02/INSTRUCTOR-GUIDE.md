# Session 2: Not All Feelings Are the Same

**Concept:** TRAINING DATA AND REPRESENTATION
**Spaces used this session:** Emoji Mood Translator (28 emotions) and Headline Mood Dashboard (7 emotions) for live comparison; Emotion Spectrum (session notebook) for 3-model side-by-side
**Models used this session:**
1. `distilbert-base-uncased-finetuned-sst-2-english` (binary: POSITIVE/NEGATIVE — Session 1's model)
2. `j-hartmann/emotion-english-distilroberta-base` (7 emotions — trained on tweets)
3. `valhalla/distilbart-mnli-12-3` (zero-shot — students choose their own feeling labels)

**Pre-built Spaces:** [profplate/emoji-mood-translator](https://huggingface.co/spaces/profplate/emoji-mood-translator) (28 emotions, GoEmotions), [profplate/headline-mood-dashboard](https://huggingface.co/spaces/profplate/headline-mood-dashboard) (7 emotions, DistilRoBERTa)

---

## Time Breakdown (2 hours)

### 0:00–0:15 — Show-and-Tell

Two rounds of sharing:

**Round 1 — Mood Meter results:**
Ask: "Last week you tried the Mood Meter with text you actually care about. What did you try? Did the model agree with you?"

If students share: celebrate it. Ask follow-up questions:
- "What text did you use?"
- "Did the model's reading match how YOU felt?"
- "Were you surprised by any result?"

If nobody tried it: show a result you prepared — e.g., a song lyric that the model reads as POSITIVE but is actually from a breakup song.

**Round 2 — Collections:**
Ask: "Show us a Space you added to your Collection. What did you write in your note?"

If students share: ask what they noticed. "What made you pick that Space? What surprised you when you tested it?"

If nobody grew their Collection: that's fine. They'll have time to work on it tonight.

**SpaceCraft check-in (2-3 min):**
Show SpaceCraft on screen ([buildlittleworlds.github.io/spaceCraft](https://buildlittleworlds.github.io/spaceCraft/)). Say: "I've been doing my own version of what I'm asking you to do. Every week I explore Spaces on Hugging Face and rate the ones that do the most with the least — Spaces that run on free CPU and are still genuinely impressive. I rate them on resourcefulness, usefulness, and craft."

Show two CPU Spaces from the leaderboard that do the same task differently — for example, Kokoro TTS vs. Edge TTS (both do text-to-speech, but one runs a local model and the other calls a free API). Point out: "Same task, completely different approach. Sound familiar? That's what we're about to do with sentiment models."

> **SpaceCraft textbook link for this session:** [Chapter 6: Finding Spaces to Study](https://buildlittleworlds.github.io/spaceCraft/finding-spaces.html) teaches students how to scout for Spaces worth comparing — the same skill they're practicing with their Collections.

**Transition:** "Last week the Mood Meter only knew two feelings: POSITIVE and NEGATIVE. That's like saying music is either loud or quiet. Tonight we're going to see what happens when we give the model more words for feelings."

### 0:15–0:35 — "What If We Change the Lens?"

Open two bonus Spaces side by side (two browser tabs):
- **Emoji Mood Translator**: [profplate/emoji-mood-translator](https://huggingface.co/spaces/profplate/emoji-mood-translator) — uses GoEmotions (28 emotion categories)
- **Headline Mood Dashboard**: [profplate/headline-mood-dashboard](https://huggingface.co/spaces/profplate/headline-mood-dashboard) — uses DistilRoBERTa (7 emotion categories)

These two Spaces use different models with different emotion taxonomies, so they WILL produce different results on the same text.

**Demo flow:**
1. Paste a sentence the Mood Meter read last week into both Spaces. Show the different readings side by side.
2. Point out: the Emoji Mood Translator sees 28 emotions (admiration, amusement, annoyance, etc.), while the Headline Dashboard only sees 7 (anger, disgust, fear, joy, neutral, sadness, surprise). Different training data, different categories, different answers.
3. Try: "I stayed up until 4am thinking about what I said to her." Watch what each Space says. Ask students: "Which one do you agree with? Which one surprised you?"

**Now open the Files tab** of the Emoji Mood Translator:

**Say:** "Let's look at how this works. Same pattern as last week — `app.py` and `requirements.txt`. Same structure as the Mood Meter, but with a different model."

Show the key difference — a different model in the `pipeline()` call:

```python
# Emoji Mood Translator uses GoEmotions (28 emotions)
classifier = pipeline("text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=5)

# Headline Mood Dashboard uses a different model (7 emotions)
classifier = pipeline("text-classification",
    model="j-hartmann/emotion-english-distilroberta-base")
```

**Say:** "Same structure as the Mood Meter — just a different model name. The model is the lens. Change the lens, change what feelings you can see."

**Talking points:**
- "The Mood Meter's model was trained on movie reviews — so it thinks everything is a movie review, and only knows POSITIVE or NEGATIVE."
- "The Emoji Mood Translator's model was trained on Reddit comments with 28 emotion labels — so it can see admiration, confusion, gratitude, and more."
- "The Headline Dashboard's model was trained on tweets with 7 emotion labels — anger, disgust, fear, joy, neutral, sadness, surprise."
- "Same text in, different feelings out — because they studied different textbooks."

### 0:35–0:50 — Model Card Reading Activity

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

### 0:50–1:15 — Labeling Challenge

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

Then run the same texts through the Emoji Mood Translator and the Headline Mood Dashboard and compare to student answers. "Which Space did you agree with most? Which one surprised you?"

### 1:15–1:30 — Name the Concept + Big Question

#### Name the Concept: TRAINING DATA AND REPRESENTATION (8 min)

**Key points:**
- "Training data is the textbook the model studied from. It can only know the feelings it's been shown."
- "Representation means: what categories did the data use? Positive/negative is a representation. Seven emotions is a different representation. Love/grief/anxiety/hope is yet another."
- "Same text, different representation, different answer. The model doesn't 'understand' feelings — it matches patterns from its training data."

**Quick check:** "If you wanted a model that detects nostalgia, what kind of training data would you need? Who would you ask to label it?"

#### Research Lens (5 min)

**Say:** "Let me name what we just did in research terms. We did a **comparative analysis** using different **operationalizations** of emotion. That's a fancy way of saying: we took the same question — 'how does this text feel?' — and tested it with three different tools that each define 'feeling' differently. Binary, seven categories, and open-ended."

**Frame the shared research question:** "Here's the research question we were investigating tonight: *How does the choice of emotion taxonomy affect sentiment classification?* Three models, three taxonomies, three different answers on the same text. That's comparative analysis."

**Bridge to their own work:** "In class, we applied comparative analysis to sentiment. For your homework, you'll apply the same method to your own topic — find two models or Spaces that do similar things but differently, test them on the same inputs, and see where they diverge. Same method, your question."

#### Big Question: Who Decided There Are 6 Basic Emotions? (10–15 min)

**Set it up:** "The 7-emotion model uses categories based on a famous theory by Paul Ekman. In the 1960s and 70s, he traveled the world showing people photographs of facial expressions. He concluded that there are 6 basic emotions that every human recognizes: anger, disgust, fear, happiness, sadness, surprise."

**Voice aside** (~30 seconds): "Here's something interesting — Ekman studied facial expressions, not words. And think about this: when someone says 'I'm fine' in a flat voice, you know they're not fine. You're reading tone of voice, not words. A text model only has the words. What if we had a model that could hear the voice? We'll explore that in a few weeks."

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

### 1:30–1:45 — Curate Your Model Collection

This is the hands-on activity. Students create their second Collection — this time focused on models, not just Spaces.

**Walk through together:**
1. Go to your HF profile, click **+ New** → **Collection**
2. Name it "My Sentiment Model Lineup" (or similar)
3. Go to [huggingface.co/models](https://huggingface.co/models), search for "sentiment" or "emotion"
4. Click on a model, read the model card briefly
5. Test it using the **Inference Widget** on the model page (type a sentence, see the result)
6. Add it to your Collection (three-dot menu → Add to Collection)
7. Write a tasting note — use the template from the *Model Tasting Notes* handout

**Give students 10 minutes to:**
- Add at least one model they tested via the Inference Widget
- Write a tasting note for it
- Optionally add one of the bonus Spaces from tonight's demo (Emoji Mood Translator, Headline Mood Dashboard)

**Share and discuss (5 min):**
- "What model did you find? What does it classify?"
- "Did anyone find a model that detects feelings our three models can't?"
- "What did you learn from reading the model card?"

**Refer students to the Markdown guides:** "The *Grow Your Collection* guide has step-by-step instructions for building your Collection. The *Research Journal* guide gives you a framework for writing notes and journal entries — including a template and a worked example. And the *Comparative Analysis* method card explains the research method we just used. All three are Markdown files in the session folder on GitHub — you can also paste them into Claude or ChatGPT and ask questions."

### 1:45–1:55 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. "Click the link — same as last week"
2. Run the setup cell together
3. Run the cell that loads all three models — point out that this takes a minute
4. Run the first comparison together and look at the three different outputs

**Say:** "The notebook has all three models you just saw. For each experiment, you'll run the same text through all three and record which one you agree with most. Use your results to write better tasting notes for your Collection."

**Notebook skill being introduced:** Running cells in order, reading output from multiple cells, editing code to change inputs

**GitHub skill being introduced:** "Create a repo called `my-ai-portfolio` on GitHub, then upload this notebook to it. Your public Collections on Hugging Face are part of your portfolio too."

### 1:55–2:00 — Wrap Up

Share the between-session challenge (see BETWEEN-SESSION.md).

**Say:** "Before next week: find a model on the Hub that sees feelings the current ones miss. Add it to your Model Collection with a tasting note. Your Collection should have at least 4 models and 2 Spaces by Session 3. Next week, we're going to find out what happens when the model reads text that means the opposite of what it says — sarcasm, irony, passive aggression."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| A bonus Space is slow to load | Free CPU Spaces take a minute to wake up. Have the Mood Meter open as backup. You can also demo with the Inference Widget on model pages. |
| A bonus Space is down | Use the Colab fallback notebooks in `bonus-hugging-face-spaces/` — each Space has a `colab_demo.ipynb` that runs the same functionality. Or demo models one at a time using the Inference Widget on each model's page. |
| Model card is too technical | Focus on just the 5 questions in the table. Skip the technical details. |
| Students can't find the model card | Show them: go to huggingface.co, search the model name, click the model page. The README is the model card. |
| Students can't find the Inference Widget | It's on the right side of the model page, labeled "Hosted inference API." Not all models have it — if one doesn't, try another. |
| Emotion model gives odd results on long text | It was trained on tweets (short text). That's a feature of this lesson, not a bug. "This model thinks everything is a tweet." |
| Students struggle with tasting notes | Point them to GUIDE-research-journal.md — it has the five-step tasting process, a template, and a worked example. |
| Big Question discussion falls flat | Have a backup: ask students to name a feeling they've had this week. Then check if any of the three models have a label for it. |
| Big Question discussion runs too long | Time-box at 15 min. Say: "We'll come back to this — the question of who defines emotions comes up again when we talk about bias in Session 7." |
| Not enough time for Model Collection activity | Students can finish between sessions. GUIDE-grow-your-collection.md has complete step-by-step instructions. |

---

## Session Resources (Markdown Guides)

- **GUIDE-grow-your-collection.md** — step-by-step guide to building and maintaining a model-focused Collection, with growth targets and notes guidance
- **GUIDE-research-journal.md** — Research Journal companion guide with weekly template, annotated example, five-step tasting process, challenge prompts, and vocabulary
- **GUIDE-comparative-analysis.md** — research method card for comparative analysis (this session's Research Lens method)

> **Note for instructors:** These guides are Markdown files, not PDFs. Students can open them on GitHub, paste them into an LLM for help, or copy templates directly into their own files. When distributing, point students to the session folder on GitHub.

---

## Key Vocabulary (introduce casually)

- **Training data** — the examples a model learned from
- **Representation** — the categories or labels the training data uses
- **Sentiment** — positive or negative feeling
- **Emotion categories** — the specific feelings a model was trained to recognize
- **Model card** — documentation that describes what a model does and how it was trained
- **Fine-tuned** — a model further trained on specific data for a specific task
- **Zero-shot** — a model that can classify text into categories it wasn't specifically trained on
- **Inference Widget** — the test box on a model's HF page that lets you try it without code

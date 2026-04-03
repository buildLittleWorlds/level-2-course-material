# Session 10: System Integration — Independent Build
*Student-Facing Title: "Build Your Own from Scratch"*

## Concept: SUPERVISED LEARNING AND TASK DESIGN

**Key idea:** Students choose a task, pick a model, and build a complete Space from scratch. The act of choosing — *what task? what model? what audience?* — teaches how supervised learning works: someone decided what the labels should be, what the training data looked like, and what "correct" means.
**Narrative Role:** The synthesis. Students build something using everything they've learned. Session 9 ended with "Next week, you pick a model, you pick a task, you design the whole thing, and you deploy it." This is that week. Every concept from Sessions 1–9 is embedded in the choices students make: what task (classification vs. generation), what model (training data, labels), what audience (human-AI interaction), what could go wrong (bias, domain shift, error cascades).

---

## Time Breakdown (2 hours)

### 0:00–0:07 — Show-and-Tell + Recap

Quick share: who did you redesign for last week? What did you learn from watching someone else try your Space?

Then recap every Space built so far:

| Session | Title | Space | Concept |
|---------|-------|-------|---------|
| 1 | From Rules to Models | Mood Meter | Input → Model → Output |
| 2 | Data Collection and Representation | Emotion Spectrum | Training data and representation |
| 3 | Data Cleaning and Feature Engineering | Sarcasm Breaker | Adversarial testing / limits of classification |
| 4 | Introduction to Supervised Learning | Text Generator | Classification vs. generation |
| 5 | Model Training and Parameters | Text Playground | Hyperparameters |
| 6 | Model Evaluation and Generalization | *(no Space — Domain Safari)* | Overfitting and domain shift |
| 7 | Bias, Variance, and Uncertainty | Bias Tester | Bias in AI |
| 8 | From Single Models to Systems | Image Story Pipeline | Multi-model systems and error cascades |
| 9 | Prompt Logic and Human-AI Interaction | Restaurant Review Analyzer | Prompt engineering and human-AI interaction |

> "Eight Spaces. Nine concepts. Every one used a model someone else trained, with labels someone else chose, on data someone else collected. Today you make those choices yourself."

### 0:07–0:10 — Story So Far

**Narrative bridge (~3 min — don't skip this):**

"Let me tell you where we are in the story."

"Act I — Sessions 1 through 3 — we had models that sort text into buckets. They were impressive but brittle. Sarcasm broke them. Ambiguity confused them. They only worked on the exact kind of text they were trained on. That was the old way."

"Act II — Sessions 4 through 8 — we traced the breakthrough. The fork from classification to generation. The controls — temperature, top-p. The wall — domain shift — and the answer: train on everything. The cost — bias. The pipeline — chain models together, watch errors cascade."

"Act III started last week. You designed for humans. Tonight is the synthesis. You pick a model, you pick a task, you build the whole thing. Every choice you make tonight — what task, what model, what audience, what could go wrong — comes from something we learned in those nine sessions."

### 0:10–0:13 — SpaceCraft Check-In

Pull up SpaceCraft. Show a CPU-only Space from the leaderboard where the builder clearly chose a specific audience and designed everything around that person.

**Say:** "Look at this Space on SpaceCraft. Notice how the title tells you exactly what it does. The examples are realistic. The output gives you something to act on. This person didn't just pick a model — they designed a complete experience. And they did it on free CPU. That's what you're doing tonight. Look at your Collections — you've been exploring for 9 weeks. The model you pick tonight should come from that exploration."

> **SpaceCraft textbook link for this session:** [Chapter 5: Build Your First Space](https://buildlittleworlds.github.io/spaceCraft/build.html) has three complete starter Spaces — a classifier, an API tool, and a data dashboard. If students get stuck on setup, point them here. They can pick the pattern closest to what they want to build and modify it.

### 0:13–0:25 — Hub Browsing Demo

**Live demo: Browsing the Hub**

1. Go to [huggingface.co/models](https://huggingface.co/models)
2. Show the task filter (left sidebar)
3. Click "Text Classification" — point out the download counts
4. Click on a model card — show: task, training data, labels, size
5. Show how to check if it's free-CPU-compatible (look at model size)

### 0:25–0:45 — Students Browse and Pitch

Each student spends 10 minutes browsing (encourage them to start from their Collection), then pitches in 1–2 sentences:

- "I want to build a _____ that uses _____ model."

**Instructor helps scope:**
- Too ambitious? → "Start with just text classification, add features later."
- Can't find a model? → Show the pre-screened list below.
- Stuck on ideas? → Hand them a rescue template from `templates/`.

### 0:45–1:25 — Build Time (40 minutes)

**Cycling through 5–6 students (~6 min each):**

| Minute | Focus |
|--------|-------|
| 0–2 | Check their model choice. Does it load? Is it CPU-compatible? |
| 2–4 | Help them get the basic pipeline working (`pipeline("task", model="...")`) |
| 4–5 | Help with the Gradio interface — inputs, outputs, title, description |
| 5–6 | Test with one example. Does it produce reasonable output? |

**Rescue plan:** If a student can't get their model working after 10 minutes, hand them a rescue template:
- `templates/text-classifier.py` — emotion detection (always works)
- `templates/text-generator.py` — text generation with temperature
- `templates/zero-shot.py` — zero-shot classification (most flexible)
- `templates/summarizer.py` — summarization

**Common issues and fixes:**
| Problem | Fix |
|---------|-----|
| Model too large, Space crashes | Switch to a `distil-` variant |
| Pipeline task name wrong | Check model card for correct task |
| Output is gibberish | Check `max_length`, `temperature` settings |
| Space won't build | Check `requirements.txt` has all dependencies |
| Gradio error | Make sure function returns a string |

### 1:25–1:40 — Test and Iterate + Peer Testing

Students test their own Spaces:
- Try 5 different inputs
- Find one that breaks or gives a weird result
- Fix it or add a note about limitations

**Peer quick-test:** Each student tries the Space of the person next to them (or the person before/after in the Zoom gallery).

### 1:40–1:48 — Name the Concept

> "You just did something specific: you picked a *task*, picked a *model trained on labeled data*, and designed an interface around it. That's **supervised learning** — and the choices you made (what labels? what data? what task?) are **task design**."

**Talking points:**
- Every model you used today was trained on data where humans provided the "right answers" — that's supervised learning
- The person who created the training data made choices: what counts as "positive"? What emotions to include? How to label translations?
- When you picked a model, you inherited those choices
- Task design = deciding what question to ask and what answers are possible

**Real-world connection:** "Here's the thing: every AI product you've ever used started exactly like this. Someone chose a task, chose a model trained on labeled data, and designed an interface. The person who built the autocomplete on your phone made these same choices — what should the labels be, what data to train on, who's going to use it. You just did what they did."

**Concept card:**
| Concept | What It Means | What We Did |
|---------|--------------|-------------|
| Supervised Learning | Training a model on labeled examples (input → correct output) | Used models trained on human-labeled datasets |
| Task Design | Choosing what question to ask and what categories/outputs to support | Picked a task type, chose a model, designed the interface |

### 1:48–1:53 — Research Lens (5 minutes)

**Say:** "Let's name what you just did in research terms."

"You just did **end-to-end system design** — choosing a question, a method, and building a tool to answer it. That's a **research prototype**. In a research lab, you don't just run experiments — you build tools that let you run experiments. That's what you built today."

**Research question:** Each student should be able to articulate their own: "I built a tool that [does what] for [whom] using [which model]. The question I'm investigating is [what]."

**The method (applies to any topic):** Choose a problem, select a model that addresses it, design an interface, and test with real inputs. This is the full research cycle: question → method → prototype → evaluation.

**Bridge to homework:** "Your Research Journal entry this week is the most important one yet. You chose a question, a model, and built something. Write about *why* you made those choices — that's research methodology."

### 1:53–1:57 — Notebook Time

Share the Colab notebook link in the Zoom chat. Students open it and start experimenting with their chosen model.

**What they do:**
- Run the setup cell
- Uncomment the pipeline line that matches their model choice (or write their own)
- Test with 5 different inputs
- Fill in the "Plan your Space" section

**Instructor role:** Help anyone whose model isn't loading. If a student can't decide, point them to the pre-screened list in the notebook. The notebook has commented-out lines for each model — they just uncomment one.

**GitHub skill:** Show how to download the notebook from Colab and upload it to their `my-ai-portfolio` repo on GitHub. This is their first time pushing a notebook they wrote.

### 1:57–2:00 — Bridge Forward

**Scripted bridge (say something like this):**

"You just built something from scratch. And right now, it works — mostly. Some inputs give weird results. Some outputs don't quite make sense for your audience. That's normal. That's exactly where every real AI product starts."

"Next week is about making it better. You'll swap Spaces with someone else. They'll try to break yours — the way we broke models back in Session 3. You'll get feedback you didn't expect. And then you'll iterate. Build, test, improve. That's the experimentation loop — and it's the difference between a prototype and a product."

"Three things before next session: get your Space working, write your most important Research Journal entry yet, and grow your Collection. Details in the between-session doc."

---

## Pre-Screened Models for Free CPU

### Zero-Shot Classification (most flexible — students pick their own labels)
| Model | Notes | Size |
|-------|-------|------|
| `valhalla/distilbart-mnli-12-3` | Fast, good quality | 890 MB |
| `facebook/bart-large-mnli` | Better quality, slower | 1.6 GB |

### Text Generation
| Model | Notes | Size |
|-------|-------|------|
| `distilgpt2` | Fast, short outputs | 330 MB |

### Summarization
| Model | Notes | Size |
|-------|-------|------|
| `sshleifer/distilbart-cnn-12-6` | Good for news/articles | 1.2 GB |

### Named Entity Recognition (NER)
| Model | Entities | Size |
|-------|----------|------|
| `dslim/bert-base-NER` | Person, Org, Location, Misc | 430 MB |

### Text Classification
| Model | Task | Labels | Size |
|-------|------|--------|------|
| `j-hartmann/emotion-english-distilroberta-base` | Emotion | anger, disgust, fear, joy, neutral, sadness, surprise | 330 MB |
| `SamLowe/roberta-base-go_emotions` | Emotion | 28 emotions | 500 MB |
| `distilbert-base-uncased-finetuned-sst-2-english` | Sentiment | POSITIVE / NEGATIVE | 260 MB |
| `cardiffnlp/twitter-roberta-base-sentiment-latest` | Sentiment | negative, neutral, positive | 500 MB |

### Translation
| Model | Direction | Size |
|-------|-----------|------|
| `Helsinki-NLP/opus-mt-en-fr` | English → French | 300 MB |
| `Helsinki-NLP/opus-mt-en-es` | English → Spanish | 300 MB |
| `Helsinki-NLP/opus-mt-en-de` | English → German | 300 MB |
| `Helsinki-NLP/opus-mt-fr-en` | French → English | 300 MB |

### Image Classification (advanced — needs `Pillow` in requirements)
| Model | Labels | Size |
|-------|--------|------|
| `google/vit-base-patch16-224` | 1000 ImageNet classes | 350 MB |

### Image Captioning (advanced — needs `Pillow` in requirements)
| Model | Notes | Size |
|-------|-------|------|
| `Salesforce/blip-image-captioning-base` | Generates captions for photos | 990 MB |

### Models to AVOID (too large for free CPU)
- Anything with `large`, `xl`, `xxl` in the name (except bart-large-mnli which barely fits)
- `meta-llama/*` — all Llama models
- `mistralai/*` — all Mistral models
- `tiiuae/falcon-*` — all Falcon models
- `bigscience/bloom-*` — all BLOOM models
- Any model over 2 GB

---

## Hub Browsing Tips (share with students)

1. **Filter by task** — Use the left sidebar on huggingface.co/models
2. **Sort by downloads** — Popular models are popular for a reason (they work)
3. **Check the model card** — Look for: task description, training data, labels, model size
4. **Look at Spaces using this model** — Scroll down on the model page to see examples
5. **Test before building** — Many model pages have an "Inference API" widget. Try it first!

---

## Pre-Session Prep

- [ ] Deploy the starter template as a Space (students will duplicate it)
- [ ] Test all four rescue templates — make sure they run on free CPU
- [ ] Have the pre-screened model list ready to screen-share
- [ ] Test Hub browsing — make sure the task filters work as expected
- [ ] Pre-load a few model cards to show if the network is slow

## Instructor Tips

- **Let them struggle (a little).** The point is choosing and building, not getting it perfect.
- **The rescue templates are not failure.** Frame them as "starting points everyone can use."
- **Image models are harder.** If a student wants image classification/captioning, help them add `Pillow` to requirements.txt and use `gr.Image()` input — but only if they're comfortable.
- **"It doesn't work" is the lesson.** When a model doesn't do what they expected, that's task design in action. The model was trained for a specific task — using it for something else won't work.

## Concept Review (Sessions 1–10)

| # | Session | Concept |
|---|---------|---------|
| 1 | From Rules to Models | Input → Model → Output |
| 2 | Data Collection and Representation | Training Data and Representation |
| 3 | Data Cleaning and Feature Engineering | Adversarial Testing and the Limits of Classification |
| 4 | Introduction to Supervised Learning | Classification vs. Generation |
| 5 | Model Training and Parameters | Hyperparameters |
| 6 | Model Evaluation and Generalization | Overfitting and Domain Shift |
| 7 | Bias, Variance, and Uncertainty | Bias in AI |
| 8 | From Single Models to Systems | Multi-Model Systems and Error Cascades |
| 9 | Prompt Logic and Human-AI Interaction | Prompt Engineering and Human-AI Interaction |
| 10 | Build Your Own from Scratch | Supervised Learning and Task Design |

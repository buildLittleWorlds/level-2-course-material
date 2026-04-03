# Your Research Journal

How to document what you find, what you think, and where your curiosity leads.

## What Is a Research Journal?

Scientists, designers, and engineers keep research journals — running records of what they tried, what happened, and what they think it means.

Your journal isn't a report you write after the fact. It's a thinking tool you use WHILE you're investigating. Each entry captures a snapshot of your process: what method you applied, what you expected, what surprised you, and where your curiosity is pulling you next.

You'll write one entry per week, 300-500 words. Over 10 weeks, that's a substantial record of your intellectual journey — and it becomes the backbone of your final presentation.

## The Template

Use this template every week. Copy it into your `research-journal.md` file and fill it in.

```markdown
## Week [X] — [Topic from Class]

### This Week's Method
(What research method did we learn in class? e.g., comparative analysis, adversarial testing)

### How I Applied It
(What did I test? What model/Space from my Collection did I use? What inputs did I try?)

### What I Expected
(My prediction before testing)

### What I Found
(Key observations — what happened?)

### Why I Think This Happened
(My explanation — connect it to training data, model design, domain, etc.)

### Limitations
(What couldn't I test? What might be different with other data/models/topics?)

### What I Want to Try Next
(Where is my investigation going? What question am I circling?)
```

## Section by Section: What Each Part Is For

**This Week's Method** — Name the research method from class. This grounds your entry in the course's shared vocabulary. Don't just say "we compared stuff" — say "comparative analysis" or "adversarial testing." Using the real term is part of learning it.

**How I Applied It** — This is the most important section. Be specific: what model or Space did you test? What inputs did you use? What did you actually DO? Vague entries ("I tested some models") are useless to your future self. Specific entries ("I ran the same three Spanish sentences through Google Translate and DeepL") are gold.

This is where the tasting process helps. When you're stuck on what to do:

1. **Read the label** — check the model card before you test
2. **Start with the obvious** — give it an easy input first
3. **Test the middle ground** — try ambiguous or mixed inputs
4. **Push the edges** — try something designed to break it
5. **Compare side by side** — run the same input through multiple tools

**What I Expected** — Write your prediction BEFORE you look at the results. This is hard. Scientists call it a "pre-registration" — you commit to your hypothesis before seeing the data. It's okay to be wrong. In fact, the most interesting journal entries are the ones where your prediction was wrong and you had to figure out why.

**What I Found** — Report what actually happened. Include specific outputs if you can — "the model said POSITIVE with 94% confidence" is better than "the model got it wrong." If you're comparing models, a small table works well here.

**Why I Think This Happened** — This is where you connect your observation to what you know about training data, model design, domain, and categories. Don't just describe — explain. "I think this happened because the model was trained on product reviews, and my input was a poem" is the kind of reasoning that builds real understanding.

**Limitations** — What COULDN'T you test? What might be different with other data, other models, another language, more time? This section is where you practice intellectual honesty — every investigation has boundaries. Naming yours shows sophistication, not weakness.

**What I Want to Try Next** — Where is your curiosity pulling you? This section is the thread that connects one week's entry to the next. Over time, it's what turns a collection of isolated experiments into a line of inquiry.

## An Annotated Example: Week 2 Entry

Here's what a solid journal entry looks like. This student chose Option B and explored translation models, applying comparative analysis.

---

### Week 2 — Training Data and Representation

**This Week's Method**
In class we learned about comparative analysis — testing the same question with different tools and seeing where they disagree. We compared three sentiment models that each define "feelings" differently because of their training data.

> *What works here: Names the method using the real term, connects it to what happened in class.*

**How I Applied It**
I'm interested in translation, so I found two translation models on the Hub: Helsinki-NLP/opus-mt-en-es (English to Spanish) and facebook/mbart-large-50-many-to-many-mmt (translates between 50 languages). I tested both with the same five English sentences, including a slang phrase ("that test was a piece of cake"), a sentence with sarcasm ("oh great, another group project"), and a simple factual sentence ("the store closes at 9pm").

> *What works here: Specific model names you could look up. Specific inputs described. Clear about what was held constant (the five sentences).*

**What I Expected**
I thought the bigger model (mbart, 50 languages) would be better at everything since it knows more languages. I expected the idiom and sarcasm to be hard for both.

> *What works here: Honest prediction written before testing. Reasonable reasoning behind it.*

**What I Found**
The Helsinki model actually produced more natural-sounding Spanish for simple sentences — my Spanish teacher confirmed this. But it translated "piece of cake" literally (pedazo de pastel) instead of using the Spanish idiom. The mbart model handled the factual sentence fine but produced awkward phrasing on the slang. Neither model caught the sarcasm — both translated "oh great" as though the speaker was genuinely happy.

> *What works here: Specific results. Outside verification (asked a Spanish teacher). Honest about both models' failures.*

**Why I Think This Happened**
The Helsinki model was trained specifically on English-Spanish pairs, so it's a specialist. The mbart model is a generalist — 50 languages means less depth in any one pair. This is like what we saw in class: the binary sentiment model (specialist) vs. the 28-emotion model (generalist). More categories (or more languages) doesn't always mean better at any single task.

> *What works here: Connects the finding back to the class concept. Draws a parallel between translation and sentiment.*

**Limitations**
I only tested five sentences, and I only checked Spanish. The mbart model might be much better for languages the Helsinki model doesn't even support. Also, I'm not fluent in Spanish — I asked my teacher to check, but a native speaker might judge differently.

> *What works here: Real limitations, not performative ones. Acknowledges what would change the conclusion.*

**What I Want to Try Next**
I want to find out if there's a translation model specifically trained on informal/slang text. Also, I want to try the same comparison with Japanese, since that's a very different language structure from Spanish.

> *What works here: Clear thread for next week. Specific enough to act on.*

---

## How Your Journal Evolves

Your early entries will be all over the place — and that's exactly right.

| Weeks | What your journal looks like | What's happening |
|---|---|---|
| 1-3 | Different topic each week, broad exploration, scattered interests | You're casting a wide net. This is the browsing phase. |
| 4-6 | A topic starts recurring, entries reference earlier ones, "What I Want to Try Next" keeps pulling you back to something | Your thread is emerging. Lean into it. |
| 7-9 | Entries build on each other, you're going deeper on one area, limitations from earlier weeks become this week's experiments | You're doing sustained investigation. This is research. |
| 10+ | Your journal IS the rationale for what you build from scratch | "I've been investigating X for 9 weeks. Here's what I've learned. Here's what I'm building." |

If you're in Week 2 and you don't have a topic yet — perfect. You're not behind. The journal's job right now is to help you figure out what you're interested in.

## The Five-Step Tasting Process (Your Testing Toolkit)

Whenever you're testing a model or Space for your journal, this process gives you a systematic approach:

1. **Read the label** — Check the model card. What was it trained on? What is it designed to do? A model trained on tweets will behave differently from one trained on legal documents.
2. **Start with the obvious** — Give it an easy input where you know the right answer. Does it get the basics right?
3. **Test the middle ground** — Try ambiguous, mixed, or borderline inputs. This is where models start to diverge.
4. **Push the edges** — Try inputs designed to be hard: sarcasm, very short text, other languages, domain mismatches, contradictions. Edge cases reveal real capabilities.
5. **Compare side by side** — Run the exact same input through multiple models. The differences teach more than any single result.

## Challenge Prompts for Sentiment Models (This Session)

These are designed for the sentiment models we used in class. For your own topic, invent your own challenge prompts using the same logic: what's an easy input? A hard one? An unfair one?

- **Sarcasm:** "Oh great, another group project. Just what I needed."
- **Mixed feelings:** "The movie was visually stunning but the plot made no sense."
- **Understatement:** "I suppose winning the lottery was mildly pleasant."
- **Cultural reference:** "That test was a piece of cake."
- **Question:** "Do you think this restaurant is worth trying?"
- **Very short:** "meh"
- **Non-English:** "C'est magnifique!" (French: "It's magnificent!")

> **Pro tip:** Keep a running document with your results. When you test the same sentence across 3-4 models, you'll start to see patterns — which models are cautious, which are confident, and which just get it wrong.

## The Model Spectrum

Sentiment models range from simple to nuanced. Knowing where a model sits on this spectrum helps you understand its strengths and limitations:

| Level | What It Does | Example Model |
|---|---|---|
| Binary | Positive or Negative — that's it | `distilbert-sst-2` |
| Ternary | Positive, Negative, or Neutral | `twitter-roberta-sentiment` |
| 5-Star | Rates text on a 1-5 scale, like a review | `nlptown/bert-multilingual` |
| 7 Emotions | Detects anger, disgust, fear, joy, neutral, sadness, surprise | `j-hartmann/emotion-distilroberta` |
| 28 Emotions | Multi-label: can detect multiple feelings at once | `SamLowe/roberta-go-emotions` |

> **Key insight:** More categories doesn't always mean better. A binary model might be more accurate at its job than a 28-emotion model is at its. The right model depends on what you need it to do.

## Vocabulary

| Term | What It Means |
|---|---|
| Model Card | A README for a model — explains what it does, how it was trained, and its limitations |
| Training Data | The examples the model learned from (tweets, reviews, news articles, etc.) |
| Fine-tuning | Taking a general model and training it further on a specific task |
| Multi-label | A model that can assign multiple labels at once (e.g., both "joy" and "surprise") |
| Confidence Score | How certain the model is about its prediction (higher = more sure) |
| Edge Case | An unusual or tricky input that tests the limits of a model |
| Inference | The moment when a model processes an input and produces an output |
| Comparative Analysis | Testing the same question with different tools and observing divergence |
| Operationalization | The specific way you define and measure a concept (e.g., "emotion" as 2 categories vs. 28) |
| Research Journal | A running record of what you tried, what happened, and what you think it means |

## Explore the Training Data

Your journal entries will be stronger when you understand what your models learned from. You can browse these datasets directly on Hugging Face — no code required. Open the dataset page and click the viewer to scroll through real rows.

- **[stanfordnlp/sst2](https://hf.co/datasets/stanfordnlp/sst2)** — 67K movie review sentences, POSITIVE or NEGATIVE. The training data behind the binary model we used in class.
- **[dair-ai/emotion](https://hf.co/datasets/dair-ai/emotion)** — 20K tweets labeled with 6 emotions. The training data behind the 7-emotion model.
- **[google-research-datasets/go_emotions](https://hf.co/datasets/google-research-datasets/go_emotions)** — 58K Reddit comments labeled for 27 emotions. The training data behind the 28-emotion model. Notice that a single comment can have multiple labels — that's multi-label classification.

When you write "Why I Think This Happened" in your journal, these datasets give you something concrete to point at. "The model missed the sarcasm because its training data was product reviews, not conversations" is more convincing when you've actually scrolled through the data yourself.

---

AI + Research Level 2 • Session 2: Data Collection and Representation

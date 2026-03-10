# Baseline Comparison

Session 4 Research Method

## What It Is

Baseline comparison means testing multiple tools on the same data so you can compare them fairly. Instead of asking "does this model work?" you ask "how does this model compare to that one — and to my own judgment?" You need at least two things to compare: two models, or one model and a human baseline. The comparison only works if the input is identical.

## When Researchers Use It

- A teacher gives the same essay to three different grading rubrics — not to find the "right" grade, but to see what each rubric prioritizes (grammar vs. argument vs. creativity).
- A sports analyst compares two quarterbacks by looking at their stats on the same types of plays — completions on third down, accuracy under pressure, performance against the same defense. Same situation, different players, fair comparison.
- A medical researcher compares a new drug to an existing treatment AND to a placebo. The existing treatment is the baseline — it's the thing you already know works. The new drug has to beat the baseline, not just beat nothing.

## How to Apply It

1. **Pick your models.** Find at least two models or Spaces that do the same task — two sentiment classifiers, two image generators, two translation tools, whatever your Collection includes.
2. **Pick your inputs.** Choose at least 5 inputs that cover a range: some easy (where you know the right answer), some hard (where the answer is genuinely ambiguous), and some adversarial (designed to trip models up).
3. **Record everything.** For each input, write down what each model says AND what you think the right answer is. Your judgment is the human baseline — the standard you're comparing the models against.

## Evaluation Concepts

Baseline comparison introduces a few ideas about how to think critically about model performance. You don't need formulas — you need the reasoning.

### Accuracy can be misleading

Imagine a spam detector tested on 1,000 emails. 950 are real mail, 50 are spam. The model predicts "NOT SPAM" for every single email — all 1,000. Its accuracy? 95%. Is it a good spam detector? No. It never catches any spam. High accuracy doesn't mean a model is useful — it depends on what it's getting right and what it's getting wrong.

### False positives vs. false negatives

When a model makes a mistake, the type of mistake matters.

- A **false positive** is a false alarm — the model says something is there when it isn't. A spam filter that sends your friend's email to the junk folder.
- A **false negative** is a missed detection — the model says something isn't there when it is. A spam filter that lets a phishing email through to your inbox.

Which is worse? It depends on the task. For spam, a false negative (dangerous email gets through) is more dangerous than a false positive (you fish a real email out of junk). For a medical test, a false negative (telling a sick person they're healthy) could be life-threatening. There's no universal answer — the cost of each type of error depends on context.

### High confidence does not mean correctness

A model that says "POSITIVE, 98% confidence" is not more likely to be right than one that says "POSITIVE, 72% confidence." Confidence scores tell you how sure the model is, not how correct it is. A model can be 98% sure and completely wrong — especially on inputs that look nothing like its training data. Think of it this way: confidence measures certainty, not accuracy. A very confident wrong answer is still wrong.

## Key Vocabulary

- **Baseline comparison** — Testing multiple tools on the same data to compare their performance fairly.
- **Baseline** — The standard you compare against. Could be another model, human judgment, or even a simple rule (like "predict the most common answer every time").
- **False positive** — A false alarm. The model says yes when the answer is no.
- **False negative** — A missed detection. The model says no when the answer is yes.
- **Confidence score** — How sure the model is about its prediction. Not the same as how correct it is.
- **Model evaluation** — The broader practice of measuring how well a model performs — and asking "good for what? For whom? Measured how?"

## This Week's Shared Example

In class, we put three sentiment models side by side — one trained on movie reviews, one on tweets, and one on product reviews. We fed them the same inputs and watched them disagree. The disagreements showed us that training data shapes what a model "sees" — the Twitter model handles slang better, the movie model handles formal language better, and none of them handle sarcasm well. We used our own judgment as the human baseline.

## Apply It to Your Own Topic

- Find 2+ models or Spaces in your Collection that do similar things.
- Choose 5 inputs that cover a range: easy, hard, and adversarial.
- For each input, record what each model says AND what you think the right answer is.
- Where do the models agree? Where do they disagree? Where do YOU disagree with all of them?
- Can you explain the disagreements by reading the model cards? (Training data, intended use, limitations?)
- Is one model consistently better, or does it depend on the type of input?

See `GUIDE-research-journal.md` for how to structure your comparison as a journal entry.

## Explore the Training Data

The three models we compared in class were trained on three very different datasets. Browsing them helps you understand why the models disagree. No code required — open the dataset page and click the viewer.

- **[stanfordnlp/sst2](https://hf.co/datasets/stanfordnlp/sst2)** — 67K movie review sentences. Clean, literary, single sentences. This is what the movie-review model learned from.
- **[cardiffnlp/tweet_eval](https://hf.co/datasets/cardiffnlp/tweet_eval)** — The sentiment subset is the training data behind the Twitter model. Short, informal, full of slang and abbreviations. Compare these rows to SST-2 and the difference is obvious.
- **[cornell-movie-review-data/rotten_tomatoes](https://hf.co/datasets/cornell-movie-review-data/rotten_tomatoes)** — 10K Rotten Tomatoes reviews, perfectly balanced (5K positive, 5K negative). Clean and confident — and a model trained only on this will be confused by anything that doesn't sound like a movie review.
- **[stanfordnlp/imdb](https://hf.co/datasets/stanfordnlp/imdb)** — 50K full movie reviews (not single sentences). Same domain as SST-2 but much longer. Does length matter for sentiment? Browse both and compare.

Three datasets, same task, completely different data. That's why baseline comparison matters — you're not just comparing models, you're comparing the worlds they grew up in.

---

AI + Research Level 2 • Session 4: Sentiment Showdown

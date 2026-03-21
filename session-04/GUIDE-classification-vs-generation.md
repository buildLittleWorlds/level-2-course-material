# Classification vs. Generation

Session 4 Core Concept

## The Fork

There are two fundamentally different things AI can do with input:

**Classification** sorts the input into a category. You give it text, it picks a label from a fixed menu. "Positive." "Spam." "Angry." The menu was decided before the model ever saw your input. No matter how smart the model is, it can only choose from the options it was given.

**Generation** creates new content. You give it text, it writes more text — word by word, each word chosen from the entire vocabulary. There's no menu. There's no fixed set of answers. The model produces something that didn't exist before.

Every AI tool you've ever used falls on one side of this fork, or combines both.

## How They Learn

The difference between classification and generation isn't just what they output — it's what they need to learn.

### Classification needs labeled data

To train a classification model, you need pairs: an input and the correct label for that input. "This tweet is positive." "This email is spam." "This review is 3 stars." A human being decided every one of those labels. That's expensive, slow, and limited. The Twitter sentiment model we used in Sessions 2 and 3 was trained on 124 million tweets — and someone labeled every single one.

### Generation needs just text

To train a generation model, you need text. That's it. No labels. No human decisions. The model reads a sentence, tries to predict the next word, checks whether it was right, and adjusts. Read. Predict. Check. Adjust. Billions of times.

### Why this matters

When you need labels, you're limited to however many labels humans can create. When you need just text, your training data is... the internet. Every book, every article, every Reddit post, every Wikipedia entry. That's the insight that led to generative AI: remove the need for labels, and suddenly you can train on everything.

## When Researchers Use Each One

- **Classification** is used when you need a definite answer from a fixed set. Medical diagnosis (healthy / at-risk / diagnosed). Content moderation (safe / unsafe). Spam filtering (spam / not spam). Whenever the question is "which category does this belong to?" — that's classification.

- **Generation** is used when you need something new. Writing assistance. Code completion. Translation. Summarization. Chatbots. Image creation. Whenever the question is "what should come next?" — that's generation.

- **Many real systems use both.** When you ask ChatGPT a question and it refuses to answer, a classification model (content filter) decided your input was unsafe *before* the generation model ever saw it. The classification model sorts; the generation model creates. They work together in a pipeline. (We'll explore this in Session 8.)

## Evaluation Concepts

These ideas from earlier in the course still apply — and they'll keep coming back.

### Accuracy can be misleading

A spam detector tested on 1,000 emails (950 real, 50 spam) that predicts "NOT SPAM" for every email is 95% accurate — and completely useless. High accuracy doesn't mean a model is useful. It depends on what it's getting right and what it's getting wrong.

### False positives vs. false negatives

When a classification model makes a mistake, the *type* of mistake matters.

- A **false positive** is a false alarm — the model says something is there when it isn't. A spam filter that sends your friend's email to junk.
- A **false negative** is a missed detection — the model says something isn't there when it is. A spam filter that lets phishing through to your inbox.

Which is worse? It depends on the task. For spam, a false negative (dangerous email gets through) is scarier than a false positive (you fish a real email out of junk). For a medical test, a false negative (telling a sick person they're healthy) could be life-threatening.

### Evaluating generation is harder

Classification models can be graded: the model said "positive," the correct answer was "positive," so it's right. But how do you grade a generated paragraph? There's no single correct answer. Is the output coherent? Creative? Factual? Appropriate? Evaluation in generation is an open problem — and it's one reason AI safety is so complex.

## Key Vocabulary

- **Classification** — AI that sorts inputs into categories from a fixed menu.
- **Generation** — AI that creates new content by predicting the next word (or pixel, or token).
- **Labeled data** — Training data where a human decided the correct answer for each example. Required for classification.
- **Next-word prediction** — How generation models learn: read a sequence, predict what comes next, check, adjust.
- **Parameters** — The internal numbers a model adjusts during training. More parameters = more capacity. distilgpt2 has 82 million; GPT-4 has over 1 trillion.
- **False positive** — A false alarm. The model says yes when the answer is no.
- **False negative** — A missed detection. The model says no when the answer is yes.
- **Accuracy** — Percentage of correct predictions. Can be misleading when data is imbalanced.

## This Week's Shared Example

In class, we replayed the story of Sessions 1–3: classification models that sort text into buckets, hit a wall, and can't truly understand what they're reading. Then we met distilgpt2 — a tiny text generation model. We fed it the same adversarial stories from Session 3 and watched it try to *continue* the stories instead of *labeling* them. It wasn't great — 82 million parameters doesn't buy you much — but it was doing something classification can't do at all: creating new text, word by word, from the entire vocabulary.

The key insight: classification needs labeled data (expensive and limited). Generation needs just text (the entire internet). That difference in training data requirements is what made scale possible — and scale is what led to ChatGPT, Claude, and every generative AI tool.

## Apply It to Your Own Topic

- Find a **classification model** in your Collection. Test it on 3–5 inputs. Record the labels.
- Find a **generation model** or Space. Give it the same inputs as prompts. Record what it writes.
- For each input: what does classification tell you that generation doesn't? What does generation produce that classification can't?
- Try an adversarial input on both. How does each type of model handle it?
- Read the model cards for both. How is the training data different? How is the task description different?

---

AI + Research Level 2 · Session 4: What If AI Could Create?

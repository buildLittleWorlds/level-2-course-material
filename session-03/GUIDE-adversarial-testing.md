# Adversarial Testing
**Session 3 Research Method**

## What It Is

Adversarial testing means deliberately trying to break a system to find its limits. Instead of asking "does this work?" you ask "how can I make this fail?" It's a way to find out what a model actually does—not what you think it does.

## When Researchers Use It

- **Security researchers** test encryption by trying to crack it. They deliberately look for weak points.
- **Linguists** test translation models by feeding them idioms, sarcasm, and cultural references—things that trip up word-by-word translation.
- **Game testers** play badly on purpose: they jump where you can't jump, they stack objects in weird ways, they try to break the game world.

When stakes are high (security, medical AI, moderation systems), adversarial testing isn't optional—it's required.

## How to Apply It

**Step 1: Start with a working example.**
Pick something the model handles well. If you're testing a sentiment model on news, start with a headline it clearly gets right: "Olympic athlete wins gold medal" → positive.

**Step 2: Craft an adversarial input.**
Change one thing. What if the headline is "Olympic athlete wins gold medal for country amid food crisis"? What if it's all caps? What if it's "GOLD MEDAL SHOCKER"? What if it has emoji?

**Step 3: Record what happens.**
Did the model fail? If so: is this a noise problem or a meaning problem?

## Noise vs. Meaning

This distinction matters.

**Noise** is fixable. It's:
- Clickbait formatting ("This One Weird Trick...")
- ALL CAPS HEADLINES
- Sensationalist punctuation ("Markets PLUNGE!!!")
- Emoji in social media news
- Extra whitespace or bad formatting

Models can learn to ignore noise. You can preprocess it away. It's a technical problem.

**Meaning** is not fixable at the classification level. It's:
- Editorial framing (what the writer chose to emphasize)
- Implied context (what you need to know to understand why this matters)
- Metaphorical language ("markets panic"—but markets aren't people)
- The story behind the headline
- Complex situations that are both good AND bad
- Cultural or political context

When you hit a meaning problem, you're not finding a bug—you're finding a limit.

The key question: **Is this a noise problem or a meaning problem?**

## The CLEAR Framework

Use this to set up your own adversarial test:

**C:** I have a Hugging Face Space that fetches news headlines from an API and displays them on a dashboard.

**L:** Python, using gradio, requests, and transformers libraries.

**E:** I want to add sentiment analysis to each headline so users can see whether the model reads the news the same way a person would.

**A:** Can you add a function that runs each headline through a sentiment model and shows a colored badge next to it?

**R:** Use distilbert-base-uncased-finetuned-sst-2-english. Show green for positive, red for negative, gray for neutral. Display the confidence score (0-1).

## Three Failure Modes in News

When you test a sentiment or classification model on news, you'll likely see these three patterns:

**Tone deafness:** The model misses meaning that IS there.
- "Rescue crews locate survivors in flood zone" → Model reads "survivors" and scores positive, completely missing that this is disaster coverage. Journalism about terrible events uses measured, calm language, but that doesn't make it positive.

**Emotional flattening:** The model oversimplifies complex meaning.
- "Peace deal signed amid ongoing border tensions" → This is genuinely hopeful AND worrying at the same time. The model picks one. It can't hold both truths.

**Anthropomorphic projection:** The model inverts meaning that isn't there.
- "Markets panic as trade talks stall" → The model reads "panic" and scores negative. But markets don't panic—they're numbers. This is journalistic metaphor, not literal emotion.

All three failures point to the same limit: **classification models match patterns in words, not meaning.**

## This Week's Shared Example

We tested a sentiment model on live news headlines and watched it misread disaster coverage, flatten complex geopolitical stories, and project human emotion onto market metaphors. Then we tried a zero-shot classification model and let users define their own labels. Same wall. Even when we got rid of predefined sentiment classes, the model still couldn't separate the noise from the meaning.

## Apply It to Your Own Topic

1. Pick a sentiment or classification model from your Collection (or find one on Hugging Face).
2. Find 3 news headlines that break it. Write them down.
3. For each failure, ask: noise or meaning?
4. What does this tell you about how the model "reads"?

## Explore the Training Data

Where was your model trained?

- **cardiffnlp/tweet_eval (irony subset):** Trained on tweets. Notice that irony is hard—the model probably fails on headlines that are technically sad but meant to be funny.
- **distilbert-base-uncased-finetuned-sst-2-english (SST-2):** Trained on movie reviews, not news. Movie reviews are subjective and emotional. News is factual and complex. What differences would you expect?

Think about this: What would be different if the model had been trained on news headlines instead of movie reviews?

---

**AI + Research Level 2 • Session 3: Data Cleaning and Feature Engineering**

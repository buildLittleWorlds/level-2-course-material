# Adversarial Testing

Session 3 Research Method

## What It Is

Adversarial testing means deliberately trying to break a system to find its limits. Instead of asking "does this work?" you ask "how can I make this fail?" The failures tell you more than the successes — they reveal what the model actually understands and what it only appears to understand.

## When Researchers Use It

- A security researcher tries to trick a bank's fraud detection system by making small, unusual transactions. The failures reveal which patterns the system watches for — and which ones slip through.
- A linguist feeds translation software sentences full of slang, idioms, and double meanings to find out what the model translates literally vs. what it actually understands.
- A game tester doesn't just play a game normally — they walk into walls, try to leave the map, and enter impossible inputs. They're looking for the cracks the designers didn't anticipate.

## How to Apply It

1. **Start with a working example.** Give the model an input where you already know the right answer. Confirm it works.
2. **Craft an adversarial input.** Change something about the input that you think might confuse the model — add sarcasm, mix signals, use slang, switch languages, remove context, add noise.
3. **Record what happens.** What did the model say? What should it have said? Is the failure a noise problem (fixable with preprocessing) or a meaning problem (a fundamental limitation)?

## Noise vs. Meaning

This is the most important distinction you'll learn this session.

When a model fails on an input, the failure falls into one of two categories:

**Noise problems** are about formatting — junk in the input that the model can't parse. Extra spaces, repeated characters ("sooooo"), emoji, ALL CAPS. These are fixable. You can write a `clean_text()` function that strips them out before the model ever sees the input. After cleaning, the model often does better.

**Meaning problems** are about understanding — the model doesn't grasp what the input actually means. Sarcasm, irony, understatement, passive aggression, cultural references, context that isn't in the text. These are NOT fixable with preprocessing. No amount of cleaning will teach the model that "Oh great, another Monday" is not a celebration.

| Noise (fixable) | Meaning (not fixable) |
|---|---|
| Extra spaces | Sarcasm |
| Repeated characters ("sooooo") | Irony |
| Emoji | Understatement |
| ALL CAPS | Passive aggression |
| Weird formatting | Context / backstory |
| | Cultural tone differences |

When you test a model and it fails, always ask: **is this a noise problem or a meaning problem?** That question is the heart of adversarial testing.

## The CLEAR Framework

Session 3 also introduces a tool you'll use for the rest of the course: the CLEAR Framework for prompting AI coding assistants.

When you ask Claude, ChatGPT, or another AI assistant to help you write or fix code, a structured prompt gets much better results than "fix my code." CLEAR gives you the structure:

| Letter | Meaning | What to Write |
|---|---|---|
| **C** | Context | What are you building? What does it do? |
| **L** | Language | What programming language and libraries are you using? |
| **E** | Explain | What's going wrong? What's the current behavior? |
| **A** | Ask | What specific change do you want? |
| **R** | Requirements | What constraints or details should the solution include? |

### Example CLEAR Prompt

> **Context:** I have a Hugging Face Space that uses a sentiment analysis model to read the mood of text.
>
> **Language:** Python, using gradio, transformers, and re.
>
> **Explain:** When users paste sarcastic or messy text (emoji, ALL CAPS, repeated characters like "sooooo", mixed signals), the model misreads the tone.
>
> **Ask:** Add a `clean_text()` function that preprocesses the input before the model sees it.
>
> **Requirements:** Strip whitespace, collapse repeated characters, remove emoji, normalize ALL CAPS. Show the user the before and after versions.

You don't have to label each section when you write your prompt — once you get comfortable, you can fold them into a natural paragraph. But when you're stuck on how to ask for help, CLEAR gives you a starting point.

## Key Vocabulary

- **Adversarial testing** — Deliberately trying to break a system to find its limits.
- **Adversarial input** — An input specifically designed to confuse or break a model.
- **Data cleaning / preprocessing** — Transforming raw input to remove noise before the model processes it.
- **Feature engineering** — Transforming raw input into something a model can work with better.
- **Noise** — Formatting junk in the input that confuses the model (emoji, extra spaces, weird characters).
- **Tone** — The way something is said, as opposed to what is said. Meaning that lives between the words, not in them.

## This Week's Shared Example

In class, we fed sarcastic and adversarial inputs to a sentiment model and watched it fail. We categorized the failures as noise problems or meaning problems, then built a `clean_text()` function to preprocess the input. The before/after comparison showed that cleaning fixes noise but not meaning — the model still can't detect sarcasm, even with perfectly formatted input.

## Apply It to Your Own Topic

- Pick a model or Space from your Collection — any topic, not just sentiment.
- Try to find 3 inputs that break it. Think about what might confuse it: edge cases, ambiguity, mixed signals, domain mismatches, unusual formatting.
- For each failure, ask: is this a noise problem or a meaning problem?
- If it's a noise problem, try cleaning the input by hand (simplify, remove junk, reformat) and re-test. Did the result change?
- If it's a meaning problem, ask: what would the model need to "know" to get this right? Where would that knowledge come from?
- Use the CLEAR framework to ask an AI coding assistant for help if you want to automate any of your preprocessing.

See `GUIDE-research-journal.md` for how to structure your observations as a journal entry.

## Explore the Training Data

Understanding why a model fails at sarcasm is easier when you can see what it was trained on. You can browse these datasets directly on Hugging Face — no code required.

- **[cardiffnlp/tweet_eval](https://hf.co/datasets/cardiffnlp/tweet_eval)** — This dataset includes an **irony subset**: thousands of tweets labeled as ironic or not ironic. Someone built an entire labeled dataset just to teach models about sarcasm — and it's still one of the hardest problems in NLP. Browse the irony examples and see if you agree with the labels.
- **[stanfordnlp/sst2](https://hf.co/datasets/stanfordnlp/sst2)** — The binary sentiment model's training data. Scroll through it and look for sarcasm. You won't find much — movie review sentences tend to be direct. That's why the model trained on this data doesn't understand indirect language.

The gap between what's in the training data and what you're testing with — that's exactly the gap adversarial testing is designed to find.

---

AI + Research Level 2 • Session 3: When Sarcasm Breaks Everything

# Fairness Audit / Algorithmic Bias

Session 7 Research Method

## What It Is

A fairness audit is a systematic test for whether a system treats different groups of people differently when it shouldn't. You design paired inputs that are identical except for one demographic variable — a name, a gender, a role — and check whether the output changes. If it does, you've found bias. The method is simple: change one thing about who the sentence is about, hold everything else constant, and measure the difference.

## When Researchers Use It

- A journalist sends identical resumes to 100 job listings — same qualifications, same experience, same cover letter — but half have traditionally white-sounding names and half have traditionally Black-sounding names. The callback rates reveal hiring bias that no single applicant could see from their own experience.
- A sociologist analyzes courtroom sentencing data and finds that defendants with similar charges and histories receive different sentences depending on their zip code. Same crime, different outcome — the variable that shouldn't matter does.
- A playwright writes the same monologue for two characters — one wealthy, one poor — and watches how audiences react differently to the exact same words. The text didn't change. The audience's assumptions did.

## How to Apply It

1. **Write a base sentence.** Start with a clear, simple sentence that the model handles well. Confirm you get a clean result.
2. **Swap one variable.** Change a name, a pronoun, a job title, or another demographic detail. Keep every other word the same. This is the controlled variable — the only thing that differs between your two inputs.
3. **Compare the outputs.** Did the label change? Did the confidence shift? If the outputs are different, the model is responding to the variable you swapped — and that variable shouldn't matter.

## The Paired-Sentence Technique

This is your main tool for fairness auditing. Here's how to design good pairs:

**Name swaps** test whether the model associates certain names with different sentiments. Keep the sentence structure identical:

> "James is a brilliant surgeon." / "Jamila is a brilliant surgeon."

**Gender swaps** test whether pronouns or gendered words shift the model's output:

> "He is a natural leader." / "She is a natural leader."

**Role swaps** test whether the model associates certain jobs with different sentiments:

> "The doctor made a confident decision." / "The nurse made a confident decision."

For each pair, you're asking the same question: **does the model treat these the same?** If not, the difference came from the training data — the model learned that certain names, genders, or roles appear in different contexts, and it carries those associations into every prediction.

> **Important:** When a pair produces the same result, that's data too. Not every model is biased on every dimension. Documenting where a model IS fair is just as valuable as documenting where it isn't.

## Key Vocabulary

- **Fairness audit** — A systematic test for whether a model treats different demographic groups differently on identical inputs.
- **Algorithmic bias** — When an algorithm systematically produces different outcomes for different groups, not because of relevant differences in the input, but because of patterns in the training data.
- **Paired testing** — Comparing two inputs that are identical except for one controlled variable. The gold standard for detecting bias.
- **Training data bias** — The model didn't invent these patterns. It learned them from text written by humans — text that reflects the world's existing inequalities.

## This Week's Shared Example

In class, we built a Bias Tester Space and ran paired sentences through a sentiment model. We swapped names (James/Jamila), pronouns (he/she), and roles (doctor/nurse) while keeping every other word identical. The model gave different confidence scores — and sometimes different labels — for sentences that should have been treated the same. The bias came from the training data: movie reviews written by humans who carry the same associations the model learned.

## Apply It to Your Own Topic

- Pick a model from your Collection — any topic, not just sentiment. Translation models, image classifiers, text generators, and summarizers can all show bias.
- Design 3-5 paired inputs. What demographic variables make sense for your model? For a translation model, try names from different cultures. For an image classifier, try photos of people from different backgrounds doing the same activity. For a text generator, try the same prompt with different character names.
- For each pair, record both outputs and note any differences. If the outputs differ, ask: what patterns in the training data could have caused this?
- Think about stakes: if this model were used for something important (screening applications, recommending treatments, grading essays), would the bias you found cause real harm? To whom?
- If you don't find bias — that's a valid result too. Document what you tested and why the model passed.

See `GUIDE-research-journal.md` for how to structure your fairness audit as a journal entry.

## Explore the Training Data

Bias detection datasets exist because someone decided this problem was worth measuring — and someone had to label every example by hand. Browsing them shows you what goes into building a fairness benchmark. No code required — open the dataset page and click the viewer.

- **[cardiffnlp/tweet_eval](https://hf.co/datasets/cardiffnlp/tweet_eval)** — The **hate speech** and **offensive language** subsets. Thousands of tweets labeled as hateful, offensive, or neither. Browse the rows and think about who had to read and label these. Notice the edge cases — tweets where reasonable people would disagree on the label. Building a bias detection dataset forces you to define exactly where the line is, and that definition is itself a human judgment.

How do you build a dataset for detecting bias? Someone had to read every example and make a call. The labels in these datasets aren't objective facts — they're human judgments about language, and those judgments carry their own assumptions.

---

AI + Research Level 2 • Session 7: Bias, Variance, and Uncertainty

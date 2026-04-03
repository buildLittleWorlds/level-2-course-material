# Plan Your Build

How to turn your research thread into something you can actually build

## Where You Are Right Now

You've spent nine weeks exploring. You've tested models, compared tools, broken things on purpose, audited for bias, traced errors through pipelines, and redesigned a demo for a real person. Your Collection has 10+ items. Your Research Journal has 8-9 entries. Somewhere in all of that, a thread emerged — a topic you kept coming back to, a question you kept refining.

Tonight you turn that thread into an artifact: a Hugging Face Space that you design, build, and deploy from scratch.

## The Three Questions

Before you write a single line of code, answer these:

**1. What is my question?**

This is the question your Research Journal has been circling. Not a vague interest — a specific question you can build a tool to investigate.

- Too vague: "I'm interested in translation."
- Specific: "Do translation models handle informal slang differently than formal text?"
- Too vague: "I like image models."
- Specific: "Can an image captioning model describe artwork the same way it describes photos?"

Look at your last three journal entries. What question keeps appearing in "What I Want to Try Next"? That's probably your question.

**2. What model does this need?**

Your Collection is your shortlist. You've already tested these models — you know what they can and can't do.

Pick a model that:
- Addresses your question directly
- Runs on free CPU (under 2 GB — check the model card)
- Has a clear model card so you understand what it was trained on
- You've already tested, so you know its strengths and limits

If none of your Collection models fit, browse the Hub. Use the task filter on the left sidebar. Sort by downloads — popular models are popular because they work. Check the pre-screened list in the notebook if you're stuck.

**3. Who is this for?**

Session 9 taught you that the same model can be a confusing demo or a useful tool. Name one specific person:
- A teacher who wants to check student writing tone
- A music fan who wants to classify songs by mood
- A bilingual student who wants to compare translations
- A writer who wants feedback on the emotional arc of a story

"Everyone" is not an audience. "My Spanish teacher" is.

## From Answers to Blueprint

Once you have your three answers, fill in this blueprint. You can copy-paste this into a markdown cell in your notebook or into a file in your repo:

```
## My Build Plan

**My question:** [one sentence]

**My model:** [model name from HF Hub]
- Task type: [text classification / generation / translation / etc.]
- Why this model: [one sentence about why you chose it]

**My audience:** [one specific person]

**Space design:**
- Title: [what you'd call it — plain language, not jargon]
- Description: [2-3 sentences explaining what it does, written for your audience]
- Example inputs:
  1. [an easy input where you know the model works well]
  2. [an interesting input that tests something specific]
  3. [a tricky input that might challenge the model]
- Output format: [what the output should say — not raw labels, but something your audience understands]

**What I expect to find:**
- [a prediction about what the model will do well]
- [a prediction about where it will struggle]

**Connection to my research:**
- [which journal entries led to this build]
- [which method(s) from the course am I using — comparative analysis, adversarial testing, parameter sweep, etc.?]
```

## Tips for Choosing Well

**Start small.** One model, one task, one audience. You can always add features later — you can't un-complicate a confusing Space.

**Steal from your journal.** Your best experiment from the last nine weeks? That's your Space. The model you tested, the inputs you used, the question you asked — wrap an interface around it.

**Check the model card before committing.** The model card tells you the training data, the intended task, and the limitations. If the model was trained on English product reviews and your question is about Japanese poetry, you already know it won't generalize — and that's actually an interesting thing to show.

**Plan your failure case.** Every Space should have at least one input where the model struggles. That's not a bug — it's the most interesting part of your demo. "Here's what it does well, and here's where it breaks" is more impressive than a flawless demo.

## What Good Looks Like

A good build plan connects your question, your model choice, and your audience into a single thread:

> "I've been investigating whether translation models handle slang differently from formal text (my question from Weeks 3, 5, and 7). I'm using Helsinki-NLP/opus-mt-en-es because I tested it in Week 2 and it translated idioms literally. My Space is for my Spanish teacher — she can paste English slang and see how the model translates it, then compare to what a natural Spanish speaker would say. I expect formal sentences to translate well and slang to translate badly."

Notice: the question came from the journal, the model came from the Collection, and the audience is a real person. Everything connects.

---

AI + Research Level 2 • Session 10: System Integration — Independent Build

# Your Research Presentation

How to tell the story of your investigation in 5-7 minutes

## What This Is

Next session is demo day. But you're not just showing a Space — you're presenting a research journey. Your Collection, your journal entries, and your Space are three parts of the same story. This guide helps you pull them together into a 5-7 minute presentation that shows what you investigated, what you built, and what you found.

## The Five-Part Format

Every presentation follows the same structure. You don't need slides — you'll show your actual artifacts (Collection, journal, Space) live.

### Part 1: My Question (30 seconds)

Open with the question you've been investigating. One or two sentences. Not the question you started with in Week 2 — the question you ended up with by Week 10.

> "I've been investigating whether translation models handle informal language — slang, idioms, sarcasm — differently from formal text."

> "My question is about image captioning bias: does the captioning model describe people differently based on what they look like?"

> "I wanted to know if sentiment models trained on English can understand emotion in Spanish text."

If your question changed over the course — and it probably did — that's part of the story. You can say: "I started out interested in X, but by Week 6 I realized the real question was Y."

### Part 2: My Journey (1-2 minutes)

Show your Collection and your journal. You're walking the audience through your investigation.

**Your Collection:** Open it on Hugging Face. Scroll through it. Point out:
- How many items you collected
- How your focus narrowed over time (early items are scattered, later items cluster around your topic)
- One or two models that were especially important to your investigation

**Your journal:** Open your `research-journal.md` on GitHub. You don't need to read whole entries — just highlight:
- An early entry where you were still exploring broadly
- A turning-point entry where your topic emerged
- A later entry where you went deep on something specific
- The methods you used most (comparative analysis? adversarial testing? parameter sweeps? fairness auditing?)

The journey section is about showing how your thinking evolved. The early entries are supposed to be messy and exploratory. The later entries are supposed to be focused. That progression IS the story.

### Part 3: My Artifact (2 minutes)

Demo your Space live. Have your inputs ready — don't search for examples during the presentation.

Show three things:
1. **One input where it works well.** This establishes what your tool can do.
2. **One input where it struggles.** This is the most interesting part. Talk about why — connect it to what you know about the model's training data, domain, or limitations.
3. **One thing about the design.** Why did you choose this title, these examples, this output format? Who is it for?

### Part 4: What I Found (1-2 minutes)

This is your findings section. What did you learn across the whole investigation — not just from the Space, but from all ten weeks?

Talk about:
- What surprised you
- What you expected that turned out to be wrong
- What limitations you discovered (in the models, in the datasets, in your own methods)
- What connects your findings to the course concepts (domain shift, bias, error propagation, etc.)

Be honest. "I thought the bigger model would always be better, but it wasn't" is a more interesting finding than "everything worked great."

### Part 5: What's Next (30 seconds)

If you kept going, what would you investigate? This is your "What I Want to Try Next" from the journal — but zoomed out to the whole project.

> "If I had more time, I'd test these translation models on five more languages to see if the slang problem is universal or just a Spanish thing."

> "I'd want to find a captioning model trained on more diverse images and see if the bias I found goes away."

> "I'd chain my sentiment model with a summarizer so it could analyze a whole batch of reviews at once instead of one at a time."

## Preparation Checklist

Before demo day, make sure you have these ready:

- [ ] Your question — one or two sentences, practiced out loud
- [ ] Your Collection URL — open in a browser tab, ready to show
- [ ] Your journal — open on GitHub, with 2-3 entries you want to highlight
- [ ] Your Space URL — open, warmed up (visit it 15 minutes early so it's not sleeping)
- [ ] Three test inputs typed out somewhere you can copy-paste from (don't type live)
- [ ] One thing you found that surprised you — practiced out loud

## What You're NOT Being Graded On

- Perfection. A Space that breaks on one input is more interesting than one that works flawlessly if you can explain why it breaks.
- Polish. The presentation doesn't need to be slick. It needs to be honest.
- Length. Five minutes is plenty. Seven is the maximum. Don't pad.
- Having the "right" answer. You investigated a question. You might not have a clean conclusion. That's research.

## What DOES Make a Presentation Good

- **Specificity.** Name the models. Name the datasets. Quote a confidence score. Show a specific journal entry. The details are what make it real.
- **Honesty about surprises.** The moments where your expectations were wrong are the most interesting moments.
- **Connection between the parts.** The question led to the journal entries, which led to the Collection, which led to the Space. If the audience can follow that thread, you've told a research story.
- **Talking about limitations.** Every investigation has boundaries. Naming yours shows sophistication, not weakness.
- **Connection to the course story.** How does your project connect to the bigger story we've been telling — from models that sort text into buckets to models that write essays and generate images? Which concepts — adversarial testing, the fork, hyperparameters, domain shift, bias, pipelines, prompt engineering, task design, the experimentation loop — showed up in your work? Naming those connections shows you understand not just your project but the ideas behind it.

---

AI + Research Level 2 • Session 11: Iterate and Polish

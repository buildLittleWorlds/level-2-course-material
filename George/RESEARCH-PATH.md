# Your Research Path — George

This document is a step-by-step roadmap from where you are now (one working Space, no journal, no repos) to where you're headed (three Spaces, a research journal, a research brief). Each section builds on the last.

---

## Step 1: Get on GitHub and Start Your Journal

**What you need to do:**

1. **Create a GitHub repo** for your portfolio. Call it something like `ai-health-communication` or just `george-portfolio`. It can be public or private for now.
2. **Create a `research-journal.md` file** in the root of that repo.
3. **Write your first journal entry** (you're aiming for 300–500 words).

**What your first entry should cover:**

- **The shift.** When did you come into this course thinking about music, and when did medical/health AI grab you? Was there a specific moment or assignment that made the switch happen? Or was it more gradual?
- **What drew you.** What is it about explaining health concepts that feels different or interesting compared to music? Is it the clarity challenge? The real-world usefulness? The combination of precision and empathy needed?
- **What you've noticed so far.** Look at your My_Health_Explainer Space. What did you notice when you tested it? Which prompts gave you clear, useful explanations? Which ones made you go "wait, that's not quite right"?
- **A question you're sitting with.** You don't need to answer it yet, but write down what you're curious about. Is it "Can small models explain this clearly?" or "How does reading level matter in health explanations?" or something else?

**Why this matters:** Writing down where your thinking is *right now* makes it way easier to see how it changes as you build Spaces and read research. In a few weeks, you'll look back at this entry and be surprised by what you didn't know then.

---

## Step 2: Sharpen a Research Question

You have a general direction: health and diagnostic AI, communication angle. Now you need a specific question to drive your Spaces.

**Three candidates at different levels of specificity:**

**Broad:** Can AI tools explain health topics at the right reading level for different audiences?

**Medium:** Do small language models adjust their medical explanations meaningfully when you ask them to write for different audiences — like middle school vs. patient handout vs. clinical note?

**Narrow:** Test three small models (distilgpt2, SmolLM2-360M-Instruct, Qwen2.5-0.5B-Instruct) on the same five health topics, each explained at four different audience levels (middle school, high school, patient, clinical). Measure whether the models actually change the reading level or just swap surface vocabulary. Compare using readability metrics and a rubric.

**Pick one.** The broad version fits in a single Space and lets you explore freely. The medium version fits into two Spaces and requires a design choice. The narrow version is a full experiment with measurable results.

**Our recommendation:** Start with medium. It's specific enough to drive the design of Space 2, but not so rigid that you can't adjust if you discover something interesting along the way.

**Your prompt for Space 2 (if you pick medium):**

Use this as a starting point when you ask an AI to code it:

```
Write me a Hugging Face Space using Gradio that tests how well small language models adjust their medical explanations for different audiences.

The Space should be called "Health Explainer Model Lab" (or a similar name).

I want a dropdown that lets me choose between three models:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

And a second dropdown for audience level:
- Middle school explanation
- High school biology explanation
- Patient handout
- Clinical/medical explanation

Use the same health topic for all comparisons (or let the user paste in a topic).

For each model and audience combo, generate an explanation and show:
- The raw text output
- A note on whether the language actually changed or just the vocabulary

Make it run on free CPU and keep it simple for a student to understand.
```

---

## Step 3: Connect to Published Research

This is the part where you stand on other people's shoulders instead of reinventing alone. Look for research on:

- **Health communication and AI** — How should AI tools explain medical concepts?
- **Medical literacy and reading level** — What makes a health explanation effective for different audiences?
- **Plain language in medical communication** — This is a whole field. Insurance companies, hospitals, and government agencies all struggle with making medical text clear.
- **Readability metrics** — Flesch-Kincaid, SMOG, Gunning Fog — these are tools for measuring whether text is understandable.

**How to find it:**

Use **Consensus** (just like Prea did). Start with searches like:
- "health communication reading level"
- "medical explanation clarity AI"
- "plain language medical documents"
- "health literacy patient explanations"

Read the abstracts. Skim the conclusions. You're looking for papers that either:
1. Test how different audiences understand health information at different reading levels, or
2. Use AI to generate or evaluate health explanations, or
3. Study what makes medical writing effective for patients.

**What to write in your journal:** Jot down three papers you found, one sentence on why each one matters to your question, and any findings that surprise you. You'll cite these in your research brief later.

---

## Step 4: What Your Three Spaces Should Look Like

You already have Space 1: **My_Health_Explainer** — a working tool for generating health explanations using a small model. That's your baseline.

**Space 2** should test your research question. If you picked "medium" specificity above, Space 2 is the **Health Explainer Model Lab** that compares models across audience levels. This is where you gather data.

**Space 3** — the combination Space — is where you synthesize what you learned. Some options:

- **Best-of comparison:** Show the clearest, most useful explanation from each model for a given health topic and audience. Let the user rate which one is best.
- **Audience-adapted explainer:** Use the best-performing model from Space 2, but add a control that lets users dial the reading level up or down and see the explanation adapt in real time.
- **Health article simplifier:** Instead of generating explanations from scratch, take health articles or medical text and simplify or adapt them to an audience level using your best model.

The pattern: Space 1 explores, Space 2 tests, Space 3 demonstrates what you learned.

**Note:** The SPACE-PROMPTS.md file already has ready-made prompts for Health Explainer builds. Use Prompt 1 for Space 1 (you may already have done this). Use Prompt 2 for Space 2 (the model lab). Use Prompt 3 or Prompt 6 (audience adaptation) for Space 3.

---

## Step 5: Your Unique Angle

Here's something important: your shift from music to medical is itself interesting. It's not a defect in your portfolio. It's a data point.

**Why this matters:** Every student in this class is working on something slightly different. Chengry is working on diagnostic accuracy and fairness. You're working on *communication* — on how to help people understand health concepts clearly. That's different. It's the education side of health AI, not the detection side.

**The music connection:** You don't have to use it, but notice it. Good teachers understand their subject deeply *and* understand how to explain it to people who don't. Musicians learn this all the time — how to explain a musical idea to someone who has never heard it before. That skill might actually transfer to health explanation. You could write about that in your journal. You could even test it: does explaining a health concept in "story" form (the way a musician might build a narrative) make it clearer than a straight clinical explanation?

---

## What Prea Did That You Should Notice

Prea's portfolio is a good model for what you're building, but it's not a template you have to copy.

**What Prea did:**

- Started with a hunch (delivery matters in debate, not just content).
- Tested the hunch against existing sentiment models and found they failed in specific ways.
- Did a Consensus search and found peer-reviewed papers on prosody and persuasion.
- Built a formal hypothesis that combined the two ideas.
- Built three Spaces that tested the hypothesis (baseline, single-factor, two-factor).
- Ran a small experiment (n=20 clips) and reported the results honestly.
- Wrote a research brief that explained the whole arc.

**What's applicable to you:**

- The journal entries come first. Prea wrote about what she was thinking and what she noticed *before* she had a fully formed project.
- The research brief is not a lab report — it's a story of discovery. It shows the wrong turns, the surprises, and the learnings.
- The three Spaces serve the question, not the other way around. Prea didn't build three random Spaces. Each one was part of testing her hypothesis.

**What's different for you:**

- Prea's project is about combining two modalities (text + audio). Yours is about how the same information is explained differently across audiences. That's a different kind of complexity, but it's still testable.
- Prea had a clear "wrong approach" (text-only sentiment) that motivated the pivot. Your wrong approach might be "models explain the same way to everyone" — and Space 2 is where you test that.

---

## Next Steps (After This Week)

1. **Week 2:** Submit your first journal entry. Start Space 2 design (use Prompt 2 from SPACE-PROMPTS.md).
2. **Week 3:** Do your Consensus search. Find three papers. Write a journal entry about what you learned from the research.
3. **Week 4:** Space 2 is live and you're testing it. What are you noticing? What surprises you?
4. **Weeks 5–7:** Run your comparisons. Gather data. Write in your journal about patterns you're seeing. Plan Space 3.
5. **Weeks 8–10:** Space 3 is live. Synthesize your findings. Start drafting your research brief.
6. **Week 11:** Polish the brief. Clean up the journal. You're done.

---

*Build at your own pace. This is a roadmap, not a deadline.*

# Sevilla — Research Path

This file is your guide from "I'm interested in animation" to a real research question, a proper journal, and a written brief. It is modeled on what Prea did for debate speeches — read [her journal](../example-student-prea/research-journal.md) and [her research brief](../example-student-prea/research-brief.md) to see the end product.

---

## Step 1: Catch Up Your Journal (Do This First)

Your journal has one entry from Week 2, and it's about emotion detection — not your real topic. You need to get your journal to reflect what you've actually been doing and thinking. Here's what to write, working backwards from where you are now:

**Week 2 (keep what you have).** The emotion detection entry is fine as a record of what you did that week. Add one sentence at the end: *"Looking back, the emotion detection work was interesting but it's not the direction I want to pursue. My real interest is in animation and how AI can help build animated scenes."*

**Weeks 3–5 (write these now, from memory).** For each week, write a short entry (even just a few paragraphs) about what you actually did and what you noticed. Use these questions to prompt your memory:

- What did you build or test that week?
- What surprised you or didn't work the way you expected?
- What did you try in class that connected to your animation interest?
- Did you use multiple AI tools? Did they give you different results?

You don't have to remember exact dates or outputs. Prea's journal entries are detailed, but she wrote them the week they happened. Yours are being reconstructed — that's fine. Be honest about it. You can write: *"I'm writing this a few weeks late. What I remember is..."* That kind of honesty is a research skill, not a weakness.

**Week 6 (write this after tonight's class).** This is where you start writing in real time. From now on, write your journal entry the same week.

---

## Step 2: Sharpen a Research Question

You are interested in animation. That is a topic, not a research question. A research question has to be something you can *investigate* — something with an answer you don't yet know.

Here is how your topic connects to the kind of question that could drive a research brief:

**Your observation so far:** You've built Spaces that generate animation scene descriptions and mood-based animation scripts. You've noticed that AI models handle some kinds of animation directions better than others. You switch between five different AI tools and get different results from each.

**The move from observation to question:** Prea noticed that sentiment models could read *what* she said but not *how* she said it. That gap became her research question. You need to find your equivalent gap. Here are three candidate questions at different levels of specificity, written for your topic:

**Broad:** "How well do small text-generation models handle animation-specific writing tasks like motion description, scene transitions, and emotional shifts?"

**Medium:** "When a small instruct model is given animation scene prompts, does changing the emotional register of the scene (joyful → tense → sad) produce meaningfully different outputs, or do the models flatten emotional range in animation writing?"

**Narrow:** "On a set of 15 animation scene prompts tested across three models (distilgpt2, SmolLM2-360M, Qwen2.5-0.5B), which model produces the most distinguishable outputs when the scene's emotional register is systematically varied, and does instruction-tuning improve emotional range in animation writing more than it improves factual coherence?"

Notice the structure: the broad question is a conversation starter. The medium question identifies a specific gap you could test. The narrow question describes an experiment you could actually run with your existing Spaces.

**Your exercise for this week:** Run a question-sharpening conversation with one of your AI tools. Paste this into Claude, ChatGPT, Gemini, or whichever you prefer:

```text
I'm a high school student taking an applied AI course. I'm building Hugging Face Spaces that generate animation scene descriptions and scripts. I've tested multiple small text-generation models and noticed they handle some kinds of animation writing better than others. I'm particularly interested in how models handle motion, mood shifts, and scene transitions in animation.

I want to write a short research brief about this but I don't have a research question yet — I just have observations. Can you help me sharpen this into a researchable question? Don't give me the answer. Give me three candidate questions at different levels of specificity, and explain what would count as evidence for each one.
```

Save the conversation and the question you pick in your journal as your Week 6 entry.

---

## Step 3: Connect to Published Research

After you have a question, the next step is finding out if anyone else has studied something related. This is where Consensus comes in (we'll cover this in Session 7). But here are some search directions that connect to your animation interest:

- *"text generation for animation storyboards"* — Are there papers about using language models for animation pre-production?
- *"emotional tone in AI-generated creative writing"* — Does the literature say anything about whether language models can control emotional register?
- *"comparing language models on creative writing tasks"* — How do researchers evaluate creative-writing quality in model outputs?
- *"AI tools for animation production"* — What's the state of the field for AI in professional animation workflows?

You don't need to read full papers yet. Just find 3–5 that seem relevant and note their titles and what they seem to be about. Prea found her first sources in Week 3 and didn't read them carefully until Week 8. The point right now is to know the territory exists.

---

## Step 4: What Your Three Spaces Should Look Like

Right now you have AnimationwithMoods (RUNTIME_ERROR) and MoodAnimation2 (SLEEPING). For the research brief, you want three Spaces that tell a story together — not just three separate experiments, but a sequence that builds:

**Space 1 (baseline):** Your simplest animation writer. One model, basic prompts. This is the "before" picture. Prea's Space 1 was intentionally limited — it existed to show what *didn't* work.

**Space 2 (the experiment):** This is where your research question lives. If your question is about emotional range, this is the Space where you systematically test different emotional registers. If your question is about model comparison, this is the comparison lab.

**Space 3 (the full version):** The Space that combines what you learned from Space 1 and Space 2 into something more complete. Prea's Space 3 was a full pipeline that combined both modalities she'd been testing separately.

You don't have to start from scratch. Your existing Spaces might become Space 1 and Space 2 with some adjustments. The key is that each Space has a *reason* — it's not just a thing you built, it's a step in an argument.

---

## Step 5: Your Unique Angle — Multi-AI Comparison

Here's something no other student in this cohort can do as well as you: you use five different AI tools regularly. That habit could become a real research contribution. If you document how Claude, Gemini, ChatGPT, Deepseek, and Copilot handle the same animation prompt differently, you have a comparison study that's genuinely interesting. Think about whether your research question could leverage this — "how do different AI assistants compare as tools for generating animation scene descriptions?" is a question that plays directly to your working style.

---

## What Prea Did That You Should Notice

Read [Prea's journal](../example-student-prea/research-journal.md), especially:

- **Week 1** — Notice how she tested the class tools on *her own material* (debate transcripts), not generic inputs. Do the same: test models on animation prompts that matter to you, not example prompts from a tutorial.
- **Week 3** — Notice the Consensus detour. She went from "I think prosody matters" to "here are three papers that say it does" in one search session. Your version of this is finding out what the literature says about AI and animation writing.
- **Week 4** — Notice how she committed to a specific hypothesis. You don't need one yet, but you need to be working toward one.
- **Weeks 5–7** — Notice the architectural pivot. She tried something, it failed, and the failure became the most interesting part of her story. If AnimationwithMoods has a runtime error, that's not a problem for your journal — it's material.

The voice matters as much as the content. Prea cites sources, hedges her claims, and is explicit about what counts as evidence versus what counts as a hunch. That's the voice to aim for.

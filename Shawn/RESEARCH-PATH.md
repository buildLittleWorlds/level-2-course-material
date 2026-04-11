# Your Research Path — Image Generation and Art Styles

This guide walks you through the next five weeks. Work through these steps in order, and by the end you'll have a research journal, three working Spaces, and a research brief ready.

---

## Step 1: Fix and Continue Your Research Journal

You have research already — but it's scattered and missing a week.

**Current state:**
- Week 1 entry in README
- Week 3 entry in a file called "week 3"
- Week 2 is missing
- Files are in an unusual structure

**Your move:**
1. Create a single file called `research-journal.md` in this folder.
2. Write it as a chronological journal with one section per week (Week 1, Week 2, Week 3, etc.).
3. **For Weeks 1–3**, consolidate what you already have. Add the missing Week 2 entry from memory — even if it's just 5 bullet points on what you tried that week.
4. **For Weeks 4–5 (now)**, write new entries covering:
   - Week 4: "I built/tested X. I learned that Y about models or styles. Here's what surprised me."
   - Week 5 (this week): "I'm fixing AnimeSceneWriter OR rebuilding it. Here's my testing approach for the next stage."

Keep it brief — 200–300 words per week. The goal is a record of what you actually did, not a polished narrative yet.

**Example structure:**

```markdown
# Research Journal — Shawn, Spring 2026

## Week 1: Getting Started

I set up my GitHub portfolio and created my first Spaces. I was testing whether I could call the Hugging Face Inference API from Gradio without hosting a model locally...

## Week 2: First Tests

I tried X model. It was slow / didn't follow the prompt / great at anime but bad at surrealism. I learned that...

## Week 3: Diving Into Styles

I started testing how different models respond to style modifiers in the prompt...

[etc.]
```

---

## Step 2: Sharpen a Research Question

You have an interest ("image generation with art styles") but a research question is more specific.

**Broad version** (too vague):
"How do text-to-image models respond to art style instructions in prompts?"

**Medium version** (testable):
"When the same text prompt is processed with different art style instructions (anime, surrealist, watercolor, etc.), do specialized fine-tuned models like Animagine-XL produce more style-accurate results than general-purpose models like SDXL?"

**Narrow version** (what you'll actually test):
"Test 3 image models (SDXL, Animagine-XL, Playground v2.5) on 10 base prompts across 5 art styles (anime, surrealist, watercolor, photorealistic, oil painting). For each output, score style accuracy (does it actually look like that style?), visual quality, and prompt-following on a 1–5 scale. Ask: which model+style combinations are strongest? Does fine-tuning for a specific style (Animagine for anime) generalize to related styles? Does combining styles in one prompt (e.g., 'photorealistic anime') produce meaningful results?"

**Pick a version** — or write your own between these. It should:
- Be answerable with the three Spaces you'll build.
- Connect to your 12-model collection (you're not starting from scratch; you're comparing models you already care about).
- Lead to something you can document in 10–15 experiments.

**For your brief, you'll use a prompt like this:**

> I hypothesize that [your research question in statement form]. To test this, I will [describe your method: which models, how many prompts, what styles, what you'll measure]. I expect to find [your prediction based on what you know about the models].

---

## Step 3: Connect to Published Research

You don't have to find papers to do good work, but knowing what's already out there helps you frame your own findings.

**Research areas that touch your question:**

1. **Style transfer in deep learning** — How do neural networks learn to transfer one style onto content? (Classic papers: Gatys et al. 2016 on neural style transfer.)
2. **Text-to-image generation evaluation** — How do you measure whether a model does what the prompt asks? (Recent: CLIP-based scoring, human evaluation studies on Stable Diffusion variants.)
3. **Art style classification** — How do machine learning models classify what art style an image is in? (Useful for scoring your outputs.)
4. **Prompt engineering for image generation** — What kinds of text modifications make the biggest difference in model outputs? (Emerging area; lots of blog posts, fewer peer-reviewed papers yet.)
5. **Diffusion model fine-tuning** — How do models like Animagine get trained on specific styles, and does that training generalize? (E.g., Animagine blog post or papers on LoRA fine-tuning for diffusion.)

**Your move:**
- Do *not* go down a research rabbit hole yet. You're in week 5 of 11.
- Instead, pick one or two areas that sound closest to your question and skim the abstracts. Consensus.app is good for this (search "prompt engineering image generation" or "diffusion model fine-tuning").
- Take 3–5 notes. You'll cite these in your research brief later.
- The goal is: when you write your brief, you can say "Prior work shows X. My test contributes Y because Z."

---

## Step 4: What Your Three Spaces Should Look Like

You have three deliverable Spaces. Here's what each one can do:

**Space 1: Basic image generator** (foundation)
- User types a prompt.
- User picks one art style from a dropdown.
- The Space modifies the prompt with a style prefix and calls the API.
- Output: an image.
- Learning: "Does the model follow the style instruction in the prompt?"
- Use **Prompt 1** from SPACE-PROMPTS.md to scaffold this in 10 minutes.
- *Salvage candidate: Is AnimeSceneWriter close to this? If so, debug and reuse it.*

**Space 2: Style comparison lab** (experiment)
- User types a prompt.
- User picks multiple styles OR the Space shows the same prompt across multiple styles automatically.
- User picks one or more models to compare.
- Output: a grid of images (same prompt, different styles; or same style, different models).
- Learning: "Which model handles which styles best? Do styles work differently on different models?"
- Use **Prompt 2** from SPACE-PROMPTS.md.
- *This is where your systematic testing happens.*

**Space 3: Full art style image generator** (synthesis)
- User types a prompt.
- Dropdown for art style (anime, surrealist, watercolor, etc.).
- Dropdown for model (SDXL, Animagine, Playground, etc.).
- Optional: a slider to adjust how strongly the style modifier is applied to the prompt (e.g., "highly detailed watercolor" vs. "subtle watercolor hint").
- Output: a single image.
- Learning: "Given a style and a model, what's the best way to encode that preference in the prompt?"
- Use **Prompt 1** or **Prompt 2** from SPACE-PROMPTS.md as a starting point, then combine them.
- *This is the tool you'd actually want to use if you were generating images for a project.*

**Timing:**
- Space 1: This week (fix or rebuild).
- Space 2: Weeks 6–7 (while you're running experiments).
- Space 3: Weeks 8–9 (after you know what works).

---

## Step 5: Your Unique Angle

Here's what makes your work more than just "I built some Spaces":

You have a **systematic testing approach** and a **curated collection of models**.

You already think like a researcher: you've selected 12 models based on what each one is good at. That's not casual collecting. That's instrumentation — you're setting up a toolkit to test a hypothesis.

Your research brief should emphasize this. When you write it, lead with:

> "To understand how image generation models respond to art style instructions, I chose three representative models: Animagine-XL (specialized for anime), SDXL (general-purpose), and Playground v2.5 (focused on aesthetic quality). For each model, I tested five art styles on ten base prompts, scoring the outputs on style accuracy, visual quality, and prompt-following. This gives me a 3 × 5 × 10 = 150-image dataset to analyze."

That's a real experiment. Your three Spaces are the three layers of that experiment (baseline, comparison, full tool). Your journal documents the process.

---

## What Prea Did That You Should Notice

Prea's portfolio works because of three things:

1. **She had a genuine problem.** ("Debate judges rate my delivery inconsistently, and I want to know why.") Your problem is the same quality: "I want to understand how art style instructions change image generation outputs."

2. **She built in public, in her journal, so you can see the thinking.** Week 3 is the "aha moment" where a blog post and some papers turned her hunch into a hypothesis. Week 5–7 show the failure, the pivot, and the rebuild. Her brief cites those moments. That's what makes it believable.

3. **She chose models strategically.** She didn't say "let me try every ASR model." She said "I need transcription with word-level timestamps, and I need small instruction-tuned models. Here are my three picks, and here's why." You can do the same thing with image models and art styles.

---

## Checklist: Weeks 5–6

- [ ] Create research-journal.md and fill in Weeks 1–5.
- [ ] Write or refine your research question (narrow, medium, or broad — you pick).
- [ ] Get Space 1 working (fix AnimeSceneWriter or scaffold a new one from Prompt 1).
- [ ] Skim 3–5 papers or blog posts on prompt engineering or diffusion model fine-tuning.
- [ ] Start a table for Space 2 results (you'll use this in weeks 6–7 when you run your actual experiments).

---

Questions? Read SPACE-PROMPTS.md for technical scaffolding, or ask during office hours.

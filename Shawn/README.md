# Shawn — AI + Research Level 2 Portfolio

I'm interested in image generation and art styles. My goal is to build a tool where someone types a text prompt and can adjust the visual style — anime, surrealist, watercolor, photorealistic, and others — to see how the same idea looks across different artistic approaches.

## Your Topic

**Image generation with art style controls.** You want to build Spaces that let users generate images from text prompts and then see how those images change when you adjust the style instruction. This is a rich territory for testing how text-to-image models respond to style modifiers, and it's a natural hook for comparing different models (general-purpose SDXL vs. specialized models like Animagine, which you already have in your curated collection).

## Where You Are Now

**Strengths:**
- You have a systematic testing approach. Your collection of 12 image generation models shows real curation — you've already identified what models exist and what each one is good at.
- You've built two Spaces already and know the basic Gradio and Inference API workflow.
- You have clear examples to learn from in SPACE-PROMPTS.md.

**Gaps:**
- **AnimeSceneWriter is runtime-erroring** (6 days). This is your priority this week: either debug it or rebuild it using one of the prompts in SPACE-PROMPTS.md, which will take 30 minutes with a coding AI.
- **Your Test Space is sleeping.** It's still useful to keep around (it's a baseline), but wake it up or document what it was testing.
- You haven't yet written a research journal. This is also a priority: Weeks 1–5 entries should cover what you've learned so far, what broke, and what your testing approach actually is.

## Where You're Headed

Three deliverables:

1. **Research journal** (research-journal.md) — Weeks 1–5, tracking your builds, what you've tested, and the research question you're settling on.
2. **Three working Spaces** — Your best image generation tool (one of the prompts in SPACE-PROMPTS.md is a good start), a style comparison lab or prompt rewriter, and something closer to the full vision: a single Space where you input text, pick a style, pick a model, and see the result side-by-side or compared.
3. **Research brief** (research-brief.md) — A short ~4-page write-up on what you learned about how image models respond to art style instructions. Similar structure to Prea's: hypothesis, methods, results, limitations, what's next.

## What's In This Folder

- **SPACE-PROMPTS.md** — Reference guide for building Spaces and detailed prompts you can paste directly into Claude, ChatGPT, or Gemini to scaffold three different approaches (basic image generator, style comparison lab, prompt rewriter).
- **README.md** — This file. Your portfolio overview.
- **RESEARCH-PATH.md** — Step-by-step guidance on fixing your journal structure, refining your research question, and understanding what the three Spaces should teach you.
- **research-journal.md** — You'll create this, Week 1 through Week 11.
- **research-brief.md** — You'll create this, a short research paper-like writeup of your findings on art styles in image generation.
- **Three Space folders** — space1-*, space2-*, space3-* containing app.py, requirements.txt, and a README for each.

## This Week's Priority

1. **Read RESEARCH-PATH.md** — It walks you through the next steps in order.
2. **Fix AnimeSceneWriter or replace it** — Take one of the prompts in SPACE-PROMPTS.md, paste it into Claude, and scaffold a new working Space in 30 minutes. Or debug the current one if you can identify the error quickly.
3. **Start your research journal** — Write Weeks 1–5 as a single research-journal.md file (not scattered in README + separate files). Focus on: what you built, what you tested, what broke, and what you learned about the models in your collection.

---

*Built during AI + Research Level 2 at Youth Horizons Learning, Spring 2026. This is a student portfolio for the course.*

# Parameter Sweep / Experimental Design

Session 5 Research Method

## What It Is

A parameter sweep means systematically changing one variable while holding everything else constant, then observing how the output changes. It's the foundation of experimental design — the practice of isolating variables so you can tell what actually caused a difference. If you change two things at once, you can't know which one mattered.

## When Researchers Use It

- A sound engineer adjusts the reverb on a vocal track from 0% to 100% while keeping volume, EQ, and compression identical. By isolating reverb, she hears exactly what it contributes to the mix — rather than guessing while tweaking everything at once.
- A biologist grows the same plant strain under five different light levels, with identical soil, water, and temperature. The only thing that varies is light. Any difference in growth can be attributed to that one variable.
- A film editor tests the same scene with five different background music tracks — all other edits locked. The emotional shift the audience feels is caused by the music, not the acting or the camera angle, because those stayed the same.

## How to Apply It

1. **Pick your variable.** Choose one setting you can change — a slider, a dropdown, a number you can type in. Temperature, top-p, guidance scale, beam width, number of results — whatever your model or Space offers.
2. **Lock everything else.** Use the same model, the same input, and the same values for every other setting. If you change two things between runs, you won't know which one caused the difference.
3. **Sweep the range.** Try your variable at low, medium, and high values — and at the extremes. Record the output at each step. Look for the pattern: does the output change gradually or suddenly? Is there a sweet spot? What happens when you push past it?

## Key Vocabulary

- **Parameter sweep** — Systematically testing a range of values for one variable while holding all others constant.
- **Experimental design** — The practice of structuring an experiment so that you can isolate the effect of one variable. The core rule: change one thing at a time.
- **Hyperparameter** — A setting you control at runtime that changes how a model behaves without changing what it knows. The model's internal weights are fixed; hyperparameters are the knobs you turn.
- **Temperature** — A hyperparameter that controls randomness in text generation. Low temperature = predictable, safe output. High temperature = creative, chaotic output. Very high = gibberish.
- **Top-p (nucleus sampling)** — A hyperparameter that controls how many candidate words the model considers. Low top-p = only the most likely words. High top-p = more variety.
- **Isolating variables** — Changing only one thing at a time so you can attribute any difference in the output to that specific change.

## This Week's Shared Example

In class, we built a Text Playground Space with temperature, top-p, and max-length sliders. We typed the same prompt and changed one slider at a time — temperature from 0.1 to 2.0, then top-p from 0.1 to 1.0, then max length from 20 to 200. Low temperature gave us flat, repetitive text. High temperature gave us wild, surprising text. Very high temperature gave us gibberish. The pattern was clear because we only changed one variable per run.

## Apply It to Your Own Topic

- Does your model or Space have adjustable settings? Sliders, dropdowns, numeric inputs — anything you can change counts.
- If it does: pick one setting, lock everything else, and sweep it from low to high. Document what changes at each step.
- If your tools don't have obvious sliders, look for models on the Hub that do. Image generators have guidance scale. Translation models have beam width. Audio models have sampling rate. The principle is the same everywhere.
- After you sweep one variable, try a second sweep with a different variable (still one at a time). Do the two variables interact? Does the "best" value for one depend on where the other is set?
- Can you write a "settings recipe card" — the best combination of settings for a specific task? Different tasks may need different recipes.

See `GUIDE-research-journal.md` for how to structure your experiment as a journal entry.

---

## Apply It to Your Project — Personal Starter Prompts

The "Apply It to Your Own Topic" section above gives the general method. Here's a more specific starting point based on the work you've been doing so far. Find your name and use the prompt as a jumping-off point — you don't have to follow it exactly.

**Annabelle** — You've been evaluating models by testing them and writing tasting notes ("works but I don't think it's very useful for me"). That's the instinct behind a parameter sweep — you're already comparing outputs. This week, try making those comparisons more controlled: same prompt, one setting changed at a time. Your music generation tools (DiffRhythm, Tencent's tools) likely have adjustable parameters. Can you find them?

**Bobby** — Your game development tools (Qwen3-Coder-WebDev, HunYuan-Motion1.0) are full of parameters you can sweep. Guidance scale on 3D generators, style settings on web builders, resolution controls on image tools. Pick one and document the sweep the way you documented your Qwen3-Coder evaluation — structured, with specific observations at each setting.

**Chengry** — The Claude API behind your DxAI tool has explicit hyperparameters: temperature, max_tokens, top_p, system prompt wording. Think of your parameter sweep as a safety audit: what temperature produces the most medically responsible output? Is there a setting that balances thoroughness with reliability? Your SHIFT framework analysis shows you already think about how presentation affects usefulness — apply that lens here.

**Emily** — Start with the Text Playground from class. Swap in prompts related to your interests — news headlines, research summaries, information filtering. Sweep the temperature from 0.1 to 1.5 on the same news-style prompt and notice where the output shifts from "useful summary" to "creative fiction." That boundary is where parameter control matters most for information tools.

**George** — Medical AI needs low randomness — you don't want a diagnostic tool improvising. Sweep the temperature on medical-style prompts ("The patient presents with headache and fever") and find the setting where the output feels reliable versus where it starts hallucinating. Even if distilgpt2 isn't a medical model, the principle of "right settings for the task" transfers directly.

**Henry** — LoRA adapters are parameter control applied to image generation. The Qwen Camera Angles model in your collection adjusts a small set of parameters to change how images are rendered. See if the space exposes any user-facing controls (guidance scale, number of inference steps). If it does, you have your sweep. If not, write about what you think those controls would change — that's still valuable reasoning about parameters.

**Sevilla** — Your emotion detection models likely have confidence thresholds or sensitivity settings. If you can find those controls, sweep them: at what threshold does the model start labeling neutral text as emotional? At what point does it miss genuine emotion? That boundary is the emotion-detection equivalent of the "sweet spot" we found with temperature in text generation.

**Shawn** — Image generation models expose some of the richest parameter sets on the Hub: guidance scale, inference steps, CFG scale, sampler type, seed. Pick one model from your collection of 12 and sweep one parameter while keeping the prompt and all other settings locked. Your comparative journal methodology is already strong — this week, apply it within a single model instead of across models.

---

AI + Research Level 2 • Session 5: Model Training and Parameters

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

## Explore the Training Data

The text generation model we used in class (distilgpt2) is a language model, not a classifier — so its "training data" is a different kind of thing than the labeled datasets from earlier sessions. But the SST dataset has a version that connects to this week's theme. No code required — open the dataset page and click the viewer.

- **[SetFit/sst5](https://hf.co/datasets/SetFit/sst5)** — The 5-label version of the Stanford Sentiment Treebank: very negative, negative, neutral, positive, very positive. Same movie review sentences as SST-2, but graded on a 5-point scale instead of a binary split. What if sentiment were a number on a dial, not a label? That's the same question we're asking about temperature — what happens when you turn a dial instead of flipping a switch?

Browse the rows and compare them to the binary SST-2 labels from Session 2. A sentence labeled "POSITIVE" in SST-2 might be "neutral" or only "slightly positive" in SST-5. The finer the scale, the more you see — just like the finer you set your sweep intervals, the more you learn about what a parameter actually does.

---

AI + Research Level 2 • Session 5: Text Playground

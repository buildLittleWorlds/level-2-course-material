# Shawn — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`. Fill in the blanks; delete what doesn't fit.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md).

---

## Your paper in one sentence (proposed)

> *Three image-generation models (SDXL, Animagine-XL, Playground v2.5), asked to render the same ten prompts in five art styles, reveal whether "style transfer" in modern diffusion is a learned aesthetic vocabulary or a deep stylistic re-composition — with implications for how art students should (and shouldn't) use these tools as references.*

Change it. That's the shape.

---

## Pre-filled § I — The artifact

Your curation is genuinely unusual — 12 image generation models selected and annotated on purpose. Most builders pick one model; you pick the ones you'd compare. Your §I should describe the Space that does the comparison.

Of your two deployed Spaces (`Test` and `AnimeSceneWriter`), **fix any runtime errors in `AnimeSceneWriter` before publishing the paper** — it's the natural §I if it runs, and debugging is typically a short job.

| | |
|---|---|
| **Title** | AnimeSceneWriter — a Style-Specificity Probe Across General-Purpose and Fine-Tuned Diffusion Models |
| **Medium** | Gradio Space (Python) — text-to-image with style controls |
| **Deployments** | [huggingface.co/spaces/ffffww/AnimeSceneWriter](https://huggingface.co/spaces/ffffww/AnimeSceneWriter) |
| **Curated model set** | FLUX.1-dev · Stable Diffusion XL · Qwen-Image · IP-Adapter-FaceID · animagine-xl · playground-v2.5 *(from your HF collection)* |
| **Models actually compared in paper** | Pick 3: **SDXL** (general-purpose baseline) · **Animagine-XL** (anime-fine-tuned) · **Playground v2.5** (aesthetic-fine-tuned) |
| **Reading time** | Twelve image grids |

## Three candidate research angles (pick one)

1. **Fine-tuning trades generality for style-specificity — and the trade is measurable.** Your journal already documents that SDXL "excelled at detailed scene composition" but that specialized models do better at their genre. The paper's contribution: **measure the trade**, not just describe it. For the same 10 prompts across 5 styles, where does Animagine beat SDXL, and where does it lose? Centerpiece claim: **fine-tuning improves style fidelity within one genre at the cost of competence in all others** — and the loss is larger than practitioners usually admit.

2. **Style prompts are auxiliary training data.** When you ask SDXL to produce "in the style of Studio Ghibli," the quality depends on whether "Studio Ghibli" was a distinct cluster in the training data. You can probe this: style names that are *canon-famous* work; style names that are *technically precise but less famous* fail. Centerpiece claim: **diffusion style controls are not control — they are retrieval**, and the illusion of control comes from the volume of style-labeled training data.

3. **What art students should (and shouldn't) use these tools for.** Your curation discipline suggests you're thinking about this as a practitioner. The paper could argue — from your model-comparison evidence — that AI art tools are useful for *reference* and *composition sketching* but unsuitable for *style study* because they collapse stylistic nuance into prompt-keyword averages. Centerpiece claim: **AI art tools are good for what they're bad at, and bad for what they're sold as.**

My guess: **#1** — it's the most concrete, testable, and closest to your existing methodology. #2 is the sharper paper but harder to defend without more evidence. #3 is the most personal.

## Suggested § II genre contrast

Your artifact's genre is a **comparative aesthetic probe**. The default genre of an image-gen Space is a *generator* — prompt in, art out, share. You are building something different:

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| image generator | magical, capable, surprising | prompt-and-marvel | one image to post |
| comparative probe | diagnostic, symmetric, disenchanting | compare three images | evidence about what "style" means in diffusion |

## Your Δ

Candidate Δs:

- **The 12-model curation.** You chose which models to *consider*, and which to ignore. Your `Cool Image Generation Models` collection is already an editorial act.
- **The three models you shortlisted for the comparison.** Not FLUX, not Qwen-Image, not Playground-only, not SDXL-only — the *triad* is yours.
- **The five art styles.** "Anime, surrealist, etc." — the "etc." is not good enough; the exact list of five is your research signal. Likely candidates: anime, photorealistic, Studio Ghibli, oil painting, watercolor. Pick five you can defend.

The **three-model triad** is the strongest candidate for your Δ. That's where your curation turns into research.

## Suggested epigraph domain

Pull from:
- An art critic on style (Susan Sontag, *On Style*; Clement Greenberg, *Avant-Garde and Kitsch*)
- An animator / illustrator on technique (Hayao Miyazaki interviews; Chris Ware; Lynda Barry, *What It Is*)
- A photographer on the studio (Diane Arbus's notebooks)
- A technical writer on image generation, carefully chosen

Sontag's *On Style* is the obvious one but therefore slightly lazy. Miyazaki interviews are richer and more specific to anime/animation, if that's your primary style axis.

## Consensus searches to run

- `"diffusion model style transfer evaluation"`
- `"stable diffusion fine-tuning domain specialization"`
- `"text-to-image style control benchmark"`
- `"ControlNet style conditioning"`
- `"aesthetic quality image generation evaluation"`

Keep three. Look for any that specifically compares fine-tuned to base models.

## Your § IX candidate category

1. **Retrieval-flavored generation.** *Generative systems whose apparent "control" is better explained as retrieval from training clusters than as compositional synthesis.* Claim: **diffusion style controls are retrieval in generation's clothing, and this reframing makes their failure modes predictable.**

2. **Specialization debt.** *The phenomenon wherein a model fine-tuned for one style category loses measurably more competence outside that category than is reported in the model's card or release announcement.* Claim: **specialization debt is systematically under-reported in model release materials** — and you have evidence.

Either works. #2 is more specific and more defensible if your comparison data actually shows the effect.

---

## Before drafting: journal audit

Your journal has Week 1 (README), Week 3 (separate file). This will hurt the paper because §§ III–VII draw directly on journal prose. Either reconstruct missing weeks from memory (honest: "reconstructing from memory because I did not journal on time") or consolidate what you have into a single `research-journal.md` and note the gaps. Either is fine; silently skipping them is not.

---

## Questions to answer before drafting §§ III–XI

1. Which of the three angles is your angle?
2. Can `AnimeSceneWriter` be debugged in one session, or do you rebuild as a new Space?
3. What are the exact three models in your comparison?
4. What are the exact five styles?
5. Miyazaki, Sontag, or a different epigraph source entirely?

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md) — copy into your `Research-Journal` repo (or a new repo) as `PAPER.md`
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) — the exemplar
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md)

Your instinct for curation is a research instinct in disguise. The paper is where you make that instinct legible.

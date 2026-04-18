# Henry — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`. Fill in the blanks; delete what doesn't fit.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md). Then come back.

---

## Your paper in one sentence (proposed)

> *Two Spaces — one text-side (Scene_describer), one image-side (Camera_angle_model_lab) — probe the same question from opposite directions: do language and vision models contain genuinely perspective-aware representations, or do they do surface-level "angle" substitution on top of a perspective-flat prior?*

Change it. Sharpen it. That's the shape.

---

## Pre-filled § I — The artifact

You have two Spaces that pair. This is unusual and worth leveraging. Most projects have three unrelated Spaces; you have two on the same problem, approached from two modalities. Your §I should describe **the pair**, not one of them.

| | |
|---|---|
| **Title** | Scene Describer + Camera Angle Lab — a Two-Modality Probe for Perspective Reasoning |
| **Medium** | Two Gradio Spaces (Python) — one text, one image |
| **Deployments** | [huggingface.co/spaces/hrnry/Scene_describer](https://huggingface.co/spaces/hrnry/Scene_describer) · [huggingface.co/spaces/hrnry/Camera_angle_model_lab](https://huggingface.co/spaces/hrnry/Camera_angle_model_lab) |
| **Dependencies** | `distilgpt-2` (text) · `fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA` (image) |
| **Next model probed** | `SmolLM2-135M-Instruct` (named in your Week 5 journal) |
| **Reading time** | Ten minutes — one each |

## Three candidate research angles (pick one)

1. **Perspective is lexical, not spatial.** Your slider experiments in Week 5 suggest that `distilgpt-2` doesn't "rotate the scene" when you change perspective instructions — it swaps a thin layer of *perspective-coded vocabulary* ("looming," "bird's-eye," "intimate") onto an unchanged underlying scene. The image-side test (Qwen angles LoRA) is the counter-check: does an image model do the same lexical-swap, or does it actually re-compose? Centerpiece claim: **LLM "perspective" is a vocabulary feature, not a spatial one — and you can prove it with a side-by-side text/image test.**

2. **The pairing is the point.** The reason you have two Spaces is not duplication — it's triangulation. A single-modality probe can't distinguish "perspective-aware model" from "perspective-vocabulary model." Only the pair can. Centerpiece claim: **multi-modal probes aren't about fusion; they're about falsification.** You run the same test twice so that a confounding factor in one modality fails to show up in the other.

3. **Slider-extreme methodology.** Your Week 5 journal tested temperature, top-p, max_tokens at extremes. Most builders accept defaults. Your paper could read as a *methods paper* on probing small models: how to design a test that separates surface change from structural change. Centerpiece claim: **slider extremes are the only honest way to test small-model behavior** — and the framework generalizes beyond perspective.

My guess: **#1** because it's the most concrete, testable, and domain-specific claim. **#2** is more ambitious but harder to land. **#3** is a good paper but a different paper.

## Suggested § II genre contrast

Your artifact's genre is a **probe pair**. The default genre in "AI art generation" is a showcase — prompt in, picture out, post on Twitter. You are doing something different:

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| art-gen showcase | wow-factor, aesthetic, shareable | double-take and share | an impressive output |
| probe pair | diagnostic, symmetric, unflattering-to-the-model | read both outputs side-by-side | evidence about what the model is doing under the hood |

## Your Δ

Candidate Δs:

- **Your slider-extremes methodology.** The exact temperature / top-p / max_tokens values you pushed to extremes in Week 5 — these are your experimental signature.
- **The choice of `distilgpt-2`.** It's a small, old, honest model. A larger model would mask the phenomenon you're studying. You chose it on purpose.
- **The perspectives you test** (close-up, bird's-eye, low-angle, worm's-eye, side — which set did you land on?). The taxonomy is yours.

The slider-extremes methodology is the strongest candidate because your Week 5 journal already defends it clearly.

## Suggested epigraph domain

Pull from:
- A film-theory text on camera and point of view (Mitry, *Aesthetics and Psychology of the Cinema*; Bordwell on camera movement)
- An art-history text on perspective (Panofsky, *Perspective as Symbolic Form* — a classic choice)
- A cognitive-science writer on visual imagination (Stephen Kosslyn; Elaine Scarry, *Dreaming by the Book*)
- A photographer on angle (Henri Cartier-Bresson, *The Decisive Moment*)

Panofsky is the obvious move for your topic — "perspective as a symbolic form" is precisely what you're testing whether models have. Be careful not to overload the paper with art history; you need one line, not a thesis statement.

## Consensus searches to run

- `"spatial reasoning large language models"`
- `"perspective taking natural language processing"`
- `"novel view synthesis evaluation"`
- `"multi-modal probing vision language models"`
- `"camera angle image generation control"`

Keep the three strongest. Zero123, SV3D, DepthAnything will likely surface; engage with one if it's close to your test design.

## Your § IX candidate category

1. **Lexical perspective.** *The property of a language-model output wherein perspective markers are substituted in the vocabulary layer without any corresponding change in the underlying scene representation.* Claim: **most "perspective control" in small LLMs is lexical, not spatial, and the distinction is detectable by looking at which nouns stay put when the viewpoint changes.**

2. **Probe pair.** *Two artifacts testing the same hypothesis across modalities, deliberately constructed to disagree if the hypothesis is wrong.* Claim: **the probe pair is a better research unit than the single probe for small-model capability studies, because it rules out modality-specific confounds.**

Both work. #1 is more specific; #2 is more generalizable. Pick #1 if your paper is about perspective; #2 if your paper is about methodology.

---

## Before drafting: consolidate your repos

You have per-week repos (`AI-Research-Level-2-Week-4`, `AI-Research-Level-2-Week-5`). Your paper lives in *one* repo — pick a name (`AI-Research-Level-2` is fine), copy the template into it as `PAPER.md`, and migrate your best journal entries. The per-week repos can stay as archives; link to them from your main README.

---

## Questions to answer before drafting §§ III–XI

1. Which of the three angles is your angle?
2. Is your §I the **pair** or just one Space? (The pair is the recommendation.)
3. What set of perspectives did you test — list them exactly.
4. Did the slider-extreme tests give you a specific, quotable result? (If yes, that's §III or §IV gold.)
5. Panofsky-as-epigraph — yes or no?

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md) — copy into your consolidated repo
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) — read § 3 before starting
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) — worked exemplar
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md)

Your Week 5 journal is already closer to a §III than most finished paper drafts. The paper is mostly a consolidation, not a composition.

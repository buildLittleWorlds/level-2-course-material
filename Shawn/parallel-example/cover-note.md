# Cover Note — Shawn

This packet is a **starter draft** of your paper, built from your `paper-starter.md`. It is not a model answer and it is not the final version. Your job over the next four sessions is to make it yours. Three moves do that.

---

## Anchor

Your `AnimeSceneWriter` Space is currently SLEEPING and was previously RUNTIME_ERROR. That is fine for the paper — the project does not require a working hosted Space of your own. What it requires is **one real prompt grid you actually ran**, with outputs you can point at.

The cleanest path uses Hugging Face's hosted demo Spaces — every model in your `Cool Image Generation Models` collection has a public Space someone has already deployed, with the model loaded and the GPU paid for. You don't need Colab, you don't need to install anything, and you don't need to debug environments. You type prompts and save images.

- Pick three models from your collection that give you the comparison: a strong general-purpose one (FLUX.1-dev or SDXL), a style-tuned one (animagine-xl), and one more of your choice. Find each one's hosted demo Space on Hugging Face — most popular models have one linked from their model card.
- Pick **two scenes** and **three styles** — your choice, but the example grid in `PAPER.md` section 3 is a reasonable starting shape (train station at midnight, market street after rain; styles like anime, surrealist, noir).
- Run each prompt through each model's hosted Space. Screenshot or download the outputs. Pick the two or three clearest examples of the **specialization tradeoff** — places where the style-tuned model did better inside its lane but worse outside it.
- Replace the example outputs in `PAPER.md` section 4 with your real ones (described or linked, since this is a Markdown paper). Keep your real model names and your real prompts.

This is real evidence and it's gathered with tools you already know how to use. No setup tax.

## Stretch — the build-vs-use gap

This is your tier's third bullet, and it's where your `AnimeSceneWriter` Space stops being a limitation and becomes a research finding.

The hosted demos let you compare models on output quality. But they can't tell you what a *student-builder* can put on a public Space. That's a different question, and it's one your own work has already started answering: you tried to build a style-tuned Space, and on free CPU it ran into a runtime error. That gap — between what the hosted demos can do (paid GPUs, optimized inference, full model weights) and what you can deploy on free Hugging Face hardware — is itself a real finding worth reporting.

The move:

- Pick one prompt from your grid and run it through a hosted demo. Save the output.
- Try to run the same prompt through a small style-tuned model that *will* run on free CPU — something like a smaller animagine variant, a quantized SDXL, or a distilled image model. (We can pick one together.)
- Compare the outputs. Compare the wait times. Compare what broke.
- Add a third axis to the paper's findings: **fidelity (general vs. style-tuned), flexibility (in-style vs. out-of-style), and accessibility (hosted demo vs. student build).** One paragraph in section 4 reporting what the gap actually looks like at a student level.

That third axis is the part of the paper nobody else in the cohort can write. The hosted-demo work is what every reader of an image-generation paper would do; the build-vs-use comparison is what *you* can write because you tried to build it.

If time runs short, skip the stretch. The Anchor work — three models, two scenes, three styles, real outputs — is the priority and stands on its own.

## Voice

Three paragraphs to rewrite in our working session:

1. **Section 1 introduction.** Your real motivation is the curation work — you've been collecting style-relevant models since March, and the project came out of noticing differences between them. Say that. The introduction should sound like a curator who started running tests, not like a generic study of image generation.
2. **Section 3 method.** Your existing journal already shows methodological care (you talk about training data quality, model architecture differences, and prompt engineering challenges). Bring that voice into the paper — explain *why* you're comparing a general-purpose model with a style-tuned one, in your own words.
3. **Section 5 limitations.** Real limitations to name in your voice: small prompt grid (you tested a handful of scene/style combinations, not dozens), single rater (you, eyeballing the outputs), no automated style-similarity scoring, and the gap in your journal between Week 2 and Week 3. The AnimeSceneWriter instability does *not* belong in limitations any longer — it's a finding now, reported in section 4 as the build-vs-use gap. Naming what didn't go smoothly makes the paper more credible.

Tell me each one out loud first, then we rewrite together.

## Optional second extension — prompt complexity

If the Anchor work goes smoothly and you have appetite for one more move beyond the Stretch above, run the same scene at two prompt-complexity levels — "a noir alley at night" vs. "a noir alley at night, low-key lighting, wet pavement reflecting neon, two figures in silhouette under a streetlamp" — and see whether the style-tuned model's specialization advantage grows or shrinks with prompt complexity. One paragraph in section 4. This is a real but optional extension; the build-vs-use stretch above is the higher-priority move because nobody else in the cohort can write it.

---

## Two housekeeping nudges

**Journal continuity.** Your journal currently skips Week 2 (you have Week 1 in the README and Week 3 in a separate file). Either backfill Week 2 with a short entry, or restructure the journal so the gap doesn't show. An admissions reader looking at the repo will notice missing weeks.

**Source verification.** The candidate references in `PAPER.md` are abstract-checked only, via Consensus. Verify each one before you keep it: title, authors, venue, and what the paper actually claims. The image-generation literature changes fast; some of these may already have updated versions you'd rather cite.

---

AI + Research Level 2 • Paper Phase

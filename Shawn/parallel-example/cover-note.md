# Cover Note — Shawn

This packet is a **starter draft** of your paper, built from your `paper-starter.md`. It is not a model answer and it is not the final version. Your job over the next four sessions is to make it yours. Three moves do that.

---

## Anchor

Your `AnimeSceneWriter` Space is currently SLEEPING and was previously RUNTIME_ERROR. That is fine for the paper — the project does not require a working hosted Space. What it requires is **one real prompt grid you actually ran**, with outputs you can point at.

The cleanest path:

- Open Colab and load two or three models from your `Cool Image Generation Models` collection. A general-purpose one (FLUX.1-dev or SDXL) and a style-tuned one (animagine-xl). That's the comparison the paper already wants.
- Pick **two scenes** and **three styles** — your choice, but the example grid in `PAPER.md` section 3 is a reasonable starting shape (train station at midnight, market street after rain; styles like anime, surrealist, noir).
- Generate the outputs, screenshot or save the images, and pick the two or three clearest examples of the **specialization tradeoff** — places where the style-tuned model did better inside its lane but worse outside it.
- Replace the example outputs in `PAPER.md` section 4 with your real ones (described or linked, since this is a Markdown paper). Keep your real model names and your real prompts.

If you can't run it in Colab in time, the second-best path is to use Hugging Face's hosted demo Spaces for these models — same prompts through their public Spaces, screenshots saved. That's still a real test.

The **AnimeSceneWriter** instability becomes part of the limitations paragraph. Say plainly that you tested through Colab/hosted demos because your own Space was unstable. That is honest, and it is also a real finding about the difficulty of building reliable style-tuned Spaces.

## Voice

Three paragraphs to rewrite in our working session:

1. **Section 1 introduction.** Your real motivation is the curation work — you've been collecting style-relevant models since March, and the project came out of noticing differences between them. Say that. The introduction should sound like a curator who started running tests, not like a generic study of image generation.
2. **Section 3 method.** Your existing journal already shows methodological care (you talk about training data quality, model architecture differences, and prompt engineering challenges). Bring that voice into the paper — explain *why* you're comparing a general-purpose model with a style-tuned one, in your own words.
3. **Section 5 limitations.** Two real limitations belong here in your voice: (a) the AnimeSceneWriter instability, and (b) the gap in your journal between Week 2 and Week 3. Don't hide either. The paper is more credible if you name what didn't go smoothly.

Tell me each one out loud first, then we rewrite together.

## Stretch

If you finish Anchor and Voice with time, one extension move:

Add a third comparison axis: **prompt complexity**. Run the same scene at a "simple" prompt level ("a noir alley at night") and a "complex" prompt level ("a noir alley at night, low-key lighting, wet pavement reflecting neon, two figures in silhouette under a streetlamp"). See whether the style-tuned model's specialization advantage grows or shrinks with prompt complexity. One paragraph reporting what you found.

Skip if no time. Anchor + Voice is the priority.

---

## Two housekeeping nudges

**Journal continuity.** Your journal currently skips Week 2 (you have Week 1 in the README and Week 3 in a separate file). Either backfill Week 2 with a short entry, or restructure the journal so the gap doesn't show. An admissions reader looking at the repo will notice missing weeks.

**Source verification.** The candidate references in `PAPER.md` are abstract-checked only, via Consensus. Verify each one before you keep it: title, authors, venue, and what the paper actually claims. The image-generation literature changes fast; some of these may already have updated versions you'd rather cite.

---

AI + Research Level 2 • Paper Phase

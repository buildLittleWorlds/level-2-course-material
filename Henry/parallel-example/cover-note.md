# Cover Note — Henry

This packet is a **starter draft** of your paper, built from your `paper-starter.md`. It is not a model answer and it is not the final version. Your job over the next four sessions is to make it yours. Three moves do that.

---

## Anchor

You have something most students in this cohort don't: a real *pair* of Spaces approaching the same question from two sides. That pairing — `Scene_describer` (text) + `Camera_angle_model_lab` (image) — is the strongest structural feature of your paper, and the parallel-example draft already treats it that way.

The adjustment work is to swap the imagined scene tests for ones you actually run:

- Pick **two scenes** that have clear viewpoint consequences. The "dog under a kitchen table" example in `PAPER.md` section 4 is a good shape for one of them — pick a second one of your own. Something where occlusion and visibility *should* change a lot when the camera moves.
- For each scene, run the five-viewpoint set (close-up, wide shot, bird's-eye, low angle, over-the-shoulder) through both Spaces. Save the text outputs from `Scene_describer` and the image outputs from `Camera_angle_model_lab`.
- Replace the example outputs in section 4 with your real ones. Keep two or three of the clearest cases where the model used viewpoint *vocabulary* but missed the spatial *consequence*. That gap is the paper's finding.
- Update the limitations paragraph: name the actual prompt count, the actual models, and what you couldn't evaluate (probably: no human raters comparing image consistency).

Once that's done, the paper is grounded in two real Spaces you built. That's the artifact.

## Voice

Three paragraphs to rewrite in our working session:

1. **Section 1 introduction.** Your real story is interesting and not in the draft: you started with a curation interest in camera-angle LoRAs, and you ended up building two Spaces that approach perspective from the text side and the image side independently. That biographical move — "I tested it from two directions because I didn't trust either one alone" — is what the introduction should say.
2. **Section 3 method.** Make this paragraph about *your* methodological instinct. Your Week 5 journal already shows it (testing slider values at extremes, naming specific next models). Bring that into the paper. Say plainly that you tested at extremes because that's where models tend to break.
3. **Section 5 limitations.** Your honest limitation is probably specific: small test set, no expert raters, the Camera_angle_model_lab uses a LoRA that's tuned on certain object types more than others. Name what *you* actually couldn't do.

Tell me each paragraph out loud first, then we rewrite together.

## Stretch

You're the strongest stretch candidate in the cohort. One real extension move:

Add a small **agreement test** — for one or two scenes, run the same viewpoint set through both Spaces and ask whether the text description and the image output agree about what's visible. This is a real research move (do two modalities corroborate each other?) and it makes the two-Space pairing earn its place in the paper. Even three or four well-documented cases would be enough. Add a short subsection at the end of section 4 reporting what you found.

If you don't have time, skip it. Anchor + Voice is the priority.

---

## Two housekeeping nudges

**Repo organization.** Your work is currently spread across three GitHub repos (`The-Research-Paper-`, `week-06-research-question.md`, `AI-Research-Level-2-Research-Journals-`). For portfolio purposes, consolidate into one repo before Session 12 — call it something like `perspective-probe` or `ai-perspective-research`. The story reads cleaner when an admissions reader can find everything in one place.

**Source verification.** The candidate references in `PAPER.md` are abstract-checked only, via Consensus. Before you keep any of them in your final paper, verify title, authors, venue, and what each paper actually claims. The novel-view-synthesis literature is real and active, but the specific papers in the draft are placeholders until you've checked them.

---

AI + Research Level 2 • Paper Phase

# Research Journal: Perspective Probe

## Week 1 - Perspective words are easy

I started with one scene:

> A child standing beside a red bicycle in front of a small library.

Then I asked for descriptions from five viewpoints: close-up, wide shot, bird's-eye view, low angle, and over-the-shoulder.

The outputs used the right words. Bird's-eye view said "from above." Low angle said "towering." Close-up said "details." But the actual objects stayed in almost the same relationship. The model often added camera language without changing what could be seen.

Question raised: Is the model reasoning about space, or just using camera-angle vocabulary?

## Week 2 - What should change?

I made a checklist for each viewpoint:

- Which objects should be visible?
- Which objects should be hidden?
- What should look larger or smaller?
- What relationship should change?
- Does the description include impossible information?

The impossible-information problem was interesting. In an over-the-shoulder view, the model still described the child's facial expression in detail. That might be possible from some angles, but usually the face would be partly hidden.

Perspective is partly about what you cannot see.

## Week 3 - Source detour

Consensus searches on novel view synthesis and camera control showed that real viewpoint change is technically hard. The papers were about image models, not classroom text descriptions, but they helped me name the issue: **spatial consistency**.

My project is not doing true novel view synthesis. It is testing a smaller question:

> When tools are asked for different viewpoints, do the outputs preserve spatial logic?

That is a test I can run with text and image prompts.

## Week 4 - Text plus image comparison

I compared text descriptions and image prompts. The text model was good at naming viewpoint. The image prompt sometimes produced more visible change because it included visual cues like "camera low to the ground" or "looking down from above."

But both modes had shallow failures. The bird's-eye version sometimes kept front-facing details. The close-up sometimes still described the whole street. The low-angle version made the library "towering" even when the original scene said it was small.

This made me think the strongest paper claim should be about shallow versus genuine perspective change.

## Week 5 - Concrete test

The best test case was:

> A dog under a kitchen table while a person reaches for a glass of water.

From a dog's-eye low angle, the table legs and underside should matter. From bird's-eye view, the tabletop and layout should matter. From over-the-shoulder, the person's arm should partly block the glass.

The model got some of this right, but it also kept describing all objects equally. It did not consistently understand occlusion.

## Week 6 - Paper direction

The paper should say:

> In this small probe, the model handled viewpoint labels better than occlusion and visibility changes.

That is a useful claim because it separates vocabulary from spatial reasoning. A real next step would use saved image outputs and ask human raters to score whether the viewpoint actually changed.

# Research Journal: Style Fidelity Grid

## Week 1 - Style words are powerful

I started with one prompt:

> A lonely train station at midnight with one person waiting under a broken clock.

Then I added style words: anime, surrealist, watercolor, noir, and realistic. The outputs changed immediately. Anime made larger eyes and brighter lighting. Noir made shadows and contrast. Watercolor softened the edges.

At first this seemed like style control worked. But I was not sure whether the models were changing style deeply or just adding the most obvious markers.

Question raised: What counts as real style fidelity?

## Week 2 - Same prompt, different models

This week I compared a general-purpose image model and a style-tuned model on the same prompts. The style-tuned model performed better inside its lane. For anime prompts, it produced more consistent character design and composition.

But outside that lane, it was less flexible. When I asked for noir realism, it still pushed the image toward anime-like faces. That suggested a tradeoff: specialization improves fidelity for one style but may reduce flexibility.

## Week 3 - Source detour

Consensus searches on text-to-image prompting, style transfer, and LoRA helped me frame the project. Style is not just an adjective. It can include color palette, line quality, composition, texture, proportions, lighting, and subject treatment.

That changed my scoring rubric. Instead of asking "does it look cool?" I started asking:

- Does the style affect color?
- Does it affect line/texture?
- Does it affect composition?
- Does it preserve the original subject?
- Does the model overfit to one style?

## Week 4 - Prompt grid

I made a prompt grid with three scenes and four styles. The most useful prompt was the train station because it had mood, setting, object, and character.

The general-purpose model handled broad styles but sometimes used cliches. Surrealist meant melting clocks. Noir meant rain and streetlights. Anime meant large eyes and dramatic glow.

The style-tuned model was more consistent for anime, but it sometimes ignored non-anime style requests. This gave me a real comparison: fidelity inside the style versus flexibility across styles.

## Week 5 - Concrete example

The prompt "train station at midnight in surrealist style" showed the difference. The general model added impossible architecture and a distorted clock, which fit the prompt. The style-tuned anime model made a beautiful image but turned the scene into an anime poster. It looked polished, but the surrealist logic was weaker.

That example helped me make the claim:

> Style-tuned models may improve style fidelity inside their specialty while reducing flexibility outside it.

## Week 6 - Paper direction

The paper should not rank one model as simply better. It should describe a tradeoff.

The honest limitation is that style scoring is subjective. A stronger version would use multiple raters and a larger prompt grid, and maybe compare human judgments with automated image-text similarity scores.

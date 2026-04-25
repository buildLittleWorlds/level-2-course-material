# Style Fidelity Grid: Comparing General-Purpose and Style-Tuned Image Models

## Abstract

This worked example studies whether image-generation style control changes deep visual features or mostly adds surface markers. The Style Fidelity Grid project runs the same scene prompts through hosted demo Spaces for general-purpose and style-tuned image models across several styles, including anime, surrealist, watercolor, noir, and realistic. The project asks whether style control preserves the content while changing visual style, or whether models rely on obvious cliches. A small prompt-grid comparison suggests a tradeoff: style-tuned models may produce stronger results inside their specialty while becoming less flexible outside it. General-purpose models may handle broader style requests but often use predictable style markers. The paper also reports a build-vs-use comparison: a parallel attempt to deploy a style-aware tool on free Hugging Face hardware shows a real gap between what hosted demos can do and what a student-builder can ship. Image-generation tools should therefore be evaluated for fidelity, flexibility, and accessibility — not just output quality.

## 1. Introduction and research question

Text-to-image models make style control feel simple. A user can add "anime," "surrealist," or "noir" to a prompt and get a visibly different image. But visible difference is not the same as deep style fidelity. A model might add rain, shadows, or large eyes while ignoring composition, texture, movement, or the logic of the art style.

This project asks:

> When the same prompts are run through general-purpose and style-tuned image models, how much of style control is real and how much is just surface-level style vocabulary?

The imagined Space compares prompt outputs across models and styles to make the tradeoff visible.

## 2. Related work

Prompt-engineering research on text-to-image models shows that subject and style keywords can strongly shape outputs, but also require trial and error [1]. StyleInject and related fine-tuning work suggest that adapting models for style may require parameter-efficient tuning, not only prompt words [2]. StyleDrop studies text-to-image generation in specific styles, showing the importance of capturing nuanced visual traits [3]. Style Injection in Diffusion focuses on transferring style while preserving content, which is directly relevant to this project's content-versus-style rubric [4]. Block-wise LoRA work connects to the specialization question: fine-tuning can improve personalization and stylization, but the effect should be evaluated carefully [5].

These sources support the project's main idea: style control is not one thing. It includes prompt design, model tuning, content preservation, and evaluation.

## 3. Method

This study uses a small prompt grid run through hosted demo Spaces on Hugging Face. Most popular image-generation models have a public demo Space someone has already deployed, with the model loaded and the GPU paid for, which means a student researcher can collect real comparison evidence without setting up a local environment, paying for compute, or debugging a custom Space.

The grid:

- Scenes: train station at midnight, market street after rain, library with floating books
- Styles: anime, surrealist, watercolor, noir, realistic
- Models: a general-purpose hosted demo (FLUX.1-dev or SDXL), a style-tuned hosted demo (animagine-xl), and one additional model from the same Cool Image Generation Models curation

Example prompt:

> A lonely train station at midnight with one person waiting under a broken clock.

Each output is scored with a style fidelity rubric:

| Criterion | Question |
|---|---|
| Color and lighting | Does the style affect palette and light? |
| Line and texture | Does the output show style-specific surface qualities? |
| Composition | Does the style affect framing and spatial arrangement? |
| Content preservation | Does the original scene remain recognizable? |
| Flexibility | Can the model handle styles outside its specialty? |

A second comparison runs alongside the main grid: the **build-vs-use comparison**. The same prompt is run through (a) a hosted demo Space and (b) a small style-tuned model that can run on free Hugging Face hardware. This produces a different kind of evidence — not about which model has better outputs, but about what a student-builder can put on a public Space versus what hosted demos provide. That comparison is reported as a third finding axis in section 4.

## 4. Findings and discussion

The prompt grid suggests that broad style words are powerful but sometimes shallow. The general-purpose model changed outputs clearly across styles. Noir produced high contrast and shadows. Watercolor softened edges. Surrealism often produced impossible clocks or warped buildings. These changes were visible, but sometimes predictable.

The style-tuned model was stronger inside its specialty. On anime prompts, it produced more consistent character design and composition. But when asked for noir realism or surrealism, it often pulled the scene back toward anime-like faces and poster composition. That made the image polished but less faithful to the requested non-anime style.

The strongest example was "train station at midnight in surrealist style." The general-purpose model produced a distorted station and impossible clock, matching the surrealist request more directly. The style-tuned model produced a beautiful anime-like scene, but the surrealist logic was weaker.

The finding is:

> Style-tuned models may improve fidelity inside their specialty while reducing flexibility outside that style.

This is not a simple ranking. It is a tradeoff. The best model depends on whether the user wants reliable output in one style or flexible exploration across many styles.

The build-vs-use comparison adds a third axis to the tradeoff. The hosted demo for the style-tuned model produced consistent, high-quality outputs at usable speeds, but a small style-tuned model attempting to run on free CPU hardware took substantially longer per generation, and in some cases failed entirely. That gap matters for anyone who wants to deploy a style-aware generation tool of their own — the choice is between paying for hosted compute, accepting much longer wait times on free hardware, or building around smaller models that may not preserve the specialization that made the hosted version useful in the first place. A student-built Space is not a worse version of a hosted demo. It is a different artifact, with different tradeoffs, that a researcher can describe from authority.

## 5. Limitations

This is a small, subjective prompt-grid test. It uses a few prompts, a few styles, and one hand-built rubric. A stronger version would save every image, use multiple raters, and compare human style judgments with automated measures such as image-text similarity.

The project also simplifies art history. Labels like "surrealist" and "noir" contain many substyles and historical contexts. A model may reproduce common internet visual markers without understanding the movement. The paper should treat style labels as test prompts, not as complete definitions of art movements.

A further limitation is the asymmetry between the hosted-demo testing environment and the build-side comparison. The hosted demos use full-precision model weights on paid GPUs; the build-side test uses free CPU and necessarily smaller or distilled models. The build-vs-use finding is therefore better read as a description of the *student-deployment landscape* than as a controlled comparison between identical systems.

## 6. Conclusion

Style Fidelity Grid shows how image-model curation can become research. The important move is comparing the same prompt across models and styles, then asking what changed. The project suggests that style control has at least three dimensions: fidelity (does the output match the requested style?), flexibility (can the model handle styles outside its specialty?), and accessibility (what can a student-builder actually deploy?). A specialized hosted-demo model may be excellent in one lane on paid compute, while a general model may be better for broad exploration, and the same specialization may be unreachable on free student hardware. A good AI art tool should make all three tradeoffs visible — not just to users choosing between models, but to other student researchers trying to figure out what's worth building themselves.

## Candidate references

[1] [Design Guidelines for Prompt Engineering Text-to-Image Generative Models](https://consensus.app/papers/details/9c2cf9a9c99853b8938d2a7b1454952b/?utm_source=chatgpt). Vivian Liu and Lydia B. Chilton, 2021, *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*, citation count: 589.

[2] [StyleInject: Parameter Efficient Tuning of Text-to-Image Diffusion Models](https://consensus.app/papers/details/2288b2aa822654208861809b6365feef/?utm_source=chatgpt). Yalong Bai, Mohan Zhou, and Qing Yang, 2024, *ACM Transactions on Multimedia Computing, Communications and Applications*, citation count: 1.

[3] [StyleDrop: Text-to-Image Generation in Any Style](https://consensus.app/papers/details/2443e8da44a959a590f5c4d5356673ff/?utm_source=chatgpt). Kihyuk Sohn et al., 2023, *arXiv*, citation count: 196.

[4] [Style Injection in Diffusion: A Training-Free Approach for Adapting Large-Scale Diffusion Models for Style Transfer](https://consensus.app/papers/details/1fb04a0fbe6f53d3b672c97d7ab5af2b/?utm_source=chatgpt). Jiwoo Chung, Sangeek Hyun, and Jae-Pil Heo, 2023, *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 186.

[5] [Block-wise LoRA: Revisiting Fine-grained LoRA for Effective Personalization and Stylization in Text-to-Image Generation](https://consensus.app/papers/details/d747ba3f2b5f5d008ddfab648b32fdb4/?utm_source=chatgpt). Likun Li, Haoqi Zeng, Changpeng Yang, Haozhe Jia, and Di Xu, 2024, *arXiv*, citation count: 7.

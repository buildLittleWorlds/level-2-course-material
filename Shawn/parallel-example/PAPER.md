# Style Fidelity Grid: Comparing General-Purpose and Style-Tuned Image Models

## Abstract

This worked example studies whether image-generation style control changes deep visual features or mostly adds surface markers. The imagined Hugging Face Space, Style Fidelity Grid, runs the same scene prompts through general-purpose and style-tuned image models across several styles, including anime, surrealist, watercolor, noir, and realistic. The project asks whether style control preserves the content while changing visual style, or whether models rely on obvious cliches. A small prompt-grid comparison suggests a tradeoff: style-tuned models may produce stronger results inside their specialty while becoming less flexible outside it. General-purpose models may handle broader style requests but often use predictable style markers. The paper argues that image-generation tools should be evaluated for both style fidelity and flexibility.

## 1. Introduction and research question

Text-to-image models make style control feel simple. A user can add "anime," "surrealist," or "noir" to a prompt and get a visibly different image. But visible difference is not the same as deep style fidelity. A model might add rain, shadows, or large eyes while ignoring composition, texture, movement, or the logic of the art style.

This project asks:

> When the same prompts are run through general-purpose and style-tuned image models, how much of style control is real and how much is just surface-level style vocabulary?

The imagined Space compares prompt outputs across models and styles to make the tradeoff visible.

## 2. Related work

Prompt-engineering research on text-to-image models shows that subject and style keywords can strongly shape outputs, but also require trial and error [1]. StyleInject and related fine-tuning work suggest that adapting models for style may require parameter-efficient tuning, not only prompt words [2]. StyleDrop studies text-to-image generation in specific styles, showing the importance of capturing nuanced visual traits [3]. Style Injection in Diffusion focuses on transferring style while preserving content, which is directly relevant to this project's content-versus-style rubric [4]. Block-wise LoRA work connects to the specialization question: fine-tuning can improve personalization and stylization, but the effect should be evaluated carefully [5].

These sources support the project's main idea: style control is not one thing. It includes prompt design, model tuning, content preservation, and evaluation.

## 3. Method

The imagined Space uses a small prompt grid:

- Scenes: train station at midnight, market street after rain, library with floating books
- Styles: anime, surrealist, watercolor, noir, realistic
- Model types: general-purpose model and style-tuned model

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

## 4. Findings and discussion

The prompt grid suggests that broad style words are powerful but sometimes shallow. The general-purpose model changed outputs clearly across styles. Noir produced high contrast and shadows. Watercolor softened edges. Surrealism often produced impossible clocks or warped buildings. These changes were visible, but sometimes predictable.

The style-tuned model was stronger inside its specialty. On anime prompts, it produced more consistent character design and composition. But when asked for noir realism or surrealism, it often pulled the scene back toward anime-like faces and poster composition. That made the image polished but less faithful to the requested non-anime style.

The strongest example was "train station at midnight in surrealist style." The general-purpose model produced a distorted station and impossible clock, matching the surrealist request more directly. The style-tuned model produced a beautiful anime-like scene, but the surrealist logic was weaker.

The finding is:

> Style-tuned models may improve fidelity inside their specialty while reducing flexibility outside that style.

This is not a simple ranking. It is a tradeoff. The best model depends on whether the user wants reliable output in one style or flexible exploration across many styles.

## 5. Limitations

This is a small, subjective prompt-grid test. It uses a few prompts, a few styles, and one hand-built rubric. A stronger version would save every image, use multiple raters, and compare human style judgments with automated measures such as image-text similarity.

The project also simplifies art history. Labels like "surrealist" and "noir" contain many substyles and historical contexts. A model may reproduce common internet visual markers without understanding the movement. The paper should treat style labels as test prompts, not as complete definitions of art movements.

## 6. Conclusion

Style Fidelity Grid shows how image-model curation can become research. The important move is comparing the same prompt across models and styles, then asking what changed. The project suggests that style control has at least two dimensions: fidelity and flexibility. A specialized model may be excellent in one lane, while a general model may be better for broad exploration. A good AI art tool should make that tradeoff visible to users.

## Candidate references

[1] [Design Guidelines for Prompt Engineering Text-to-Image Generative Models](https://consensus.app/papers/details/9c2cf9a9c99853b8938d2a7b1454952b/?utm_source=chatgpt). Vivian Liu and Lydia B. Chilton, 2021, *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*, citation count: 589.

[2] [StyleInject: Parameter Efficient Tuning of Text-to-Image Diffusion Models](https://consensus.app/papers/details/2288b2aa822654208861809b6365feef/?utm_source=chatgpt). Yalong Bai, Mohan Zhou, and Qing Yang, 2024, *ACM Transactions on Multimedia Computing, Communications and Applications*, citation count: 1.

[3] [StyleDrop: Text-to-Image Generation in Any Style](https://consensus.app/papers/details/2443e8da44a959a590f5c4d5356673ff/?utm_source=chatgpt). Kihyuk Sohn et al., 2023, *arXiv*, citation count: 196.

[4] [Style Injection in Diffusion: A Training-Free Approach for Adapting Large-Scale Diffusion Models for Style Transfer](https://consensus.app/papers/details/1fb04a0fbe6f53d3b672c97d7ab5af2b/?utm_source=chatgpt). Jiwoo Chung, Sangeek Hyun, and Jae-Pil Heo, 2023, *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 186.

[5] [Block-wise LoRA: Revisiting Fine-grained LoRA for Effective Personalization and Stylization in Text-to-Image Generation](https://consensus.app/papers/details/d747ba3f2b5f5d008ddfab648b32fdb4/?utm_source=chatgpt). Likun Li, Haoqi Zeng, Changpeng Yang, Haozhe Jia, and Di Xu, 2024, *arXiv*, citation count: 7.

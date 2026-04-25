# Perspective Probe: Testing Whether AI Tools Change Viewpoint or Only Use Viewpoint Language

## Abstract

This worked example studies how AI text and image tools respond to viewpoint instructions. The imagined Hugging Face Space, Perspective Probe, asks a model to describe or prompt the same scene from close-up, wide shot, bird's-eye view, low angle, and over-the-shoulder perspectives. The project asks whether the outputs change spatial relationships or mostly add perspective-coded words. A small set of scene tests suggests that models can often name a viewpoint but struggle with occlusion, visibility, and object relationships. For example, an over-the-shoulder view may still describe a face that should be hidden, and a bird's-eye view may preserve front-facing details. The paper argues that testing perspective requires checking what changed spatially, not just whether the output uses camera-angle vocabulary.

## 1. Introduction and research question

Perspective sounds simple: ask for a different camera angle and expect the scene to change. But real viewpoint change is spatial. Some objects become larger, some disappear, and some relationships become clearer or harder to see.

This project asks:

> When language and image tools are asked to change perspective, do they actually change the scene in a spatial way, or do they mostly swap in perspective-coded words and visuals?

The question matters because many creative AI tools accept camera language. A user might say "low angle" or "bird's-eye view" and assume the model understands the spatial consequences. This project tests that assumption at a small scale.

## 2. Related work

Computer-vision research shows that viewpoint control is a difficult problem. TOSS studies text-guided novel view synthesis from a single image and emphasizes plausibility and control [1]. SPAD focuses on spatially aware multi-view diffusion and cross-view consistency [2]. Viewpoint Textual Inversion asks whether pretrained 2D diffusion models contain usable 3D viewpoint structure [3]. Generative Photography and PreciseCam both focus on more explicit camera control, suggesting that prompt-only camera wording may not be enough for precise, scene-consistent changes [4, 5].

This worked example does not implement those systems. It borrows the central idea that genuine perspective change requires spatial consistency.

## 3. Method

The imagined Space tests a small set of scene prompts across five viewpoints:

- Close-up
- Wide shot
- Bird's-eye view
- Low angle
- Over-the-shoulder

Example scene:

> A dog under a kitchen table while a person reaches for a glass of water.

Each output is checked with a spatial consistency rubric:

| Criterion | Question |
|---|---|
| Visibility | Which objects should be visible from this view? |
| Occlusion | What should be partly hidden? |
| Scale | What should look larger or smaller? |
| Relationship | Did object positions change logically? |
| Viewpoint vocabulary | Did the model only add camera words? |

The project compares text descriptions and image-prompt outputs, treating both as evidence.

## 4. Findings and discussion

The strongest pattern is that viewpoint vocabulary is easier than viewpoint reasoning. For the library-and-bicycle scene, the model used words such as "from above," "towering," and "close-up," but the objects often stayed in the same relationship.

The dog-under-table scene revealed the clearest failure. From a dog's-eye low angle, table legs and the underside of the table should become important. From a bird's-eye view, the tabletop and room layout should matter. From an over-the-shoulder view, the person's arm might block part of the glass. The model sometimes mentioned these changes, but it did not apply them consistently.

The finding is:

> In this small probe, the model handled viewpoint labels better than occlusion and visibility changes.

That finding is useful because it gives a way to evaluate perspective tools. The test should not ask only, "Did it say bird's-eye view?" It should ask, "What can and cannot be seen from that view?"

## 5. Limitations

This is a paper-lite pilot with a small number of prompts. It does not generate or evaluate true 3D scenes. It uses a hand-built rubric and does not include multiple human raters. A stronger study would save image outputs, compare multiple models, and ask raters to judge whether the viewpoint is spatially plausible.

The project also simplifies a complex computer-vision problem. Novel view synthesis research uses models, geometry, camera parameters, and specialized evaluation methods that go far beyond this classroom Space. This example only tests surface behavior in accessible tools.

## 6. Conclusion

Perspective Probe turns a creative camera-angle idea into a research question. The important distinction is between naming a viewpoint and reasoning from that viewpoint. AI tools may produce fluent viewpoint language while missing occlusion, visibility, and spatial relationship changes. That limitation is not a reason to stop using the tools. It is a reason to test them more honestly.

## Candidate references

[1] [TOSS: High-quality Text-guided Novel View Synthesis from a Single Image](https://consensus.app/papers/details/1806f71b4f755908862a6b3028842ee9/?utm_source=chatgpt). Yukai Shi et al., 2023, *arXiv*, citation count: 27.

[2] [SPAD: Spatially Aware Multi-View Diffusers](https://consensus.app/papers/details/75cec52719be5596b5a8399fdb22c427/?utm_source=chatgpt). Yash Kant et al., 2024, *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 49.

[3] [Viewpoint Textual Inversion: Unleashing Novel View Synthesis with Pretrained 2D Diffusion Models](https://consensus.app/papers/details/243459944e7f5895b32a60bc5a8b23c7/?utm_source=chatgpt). James Burgess, Kuan Wang, and Serena Yeung, 2023, *arXiv*, citation count: 15.

[4] [Generative Photography: Scene-Consistent Camera Control for Realistic Text-to-Image Synthesis](https://consensus.app/papers/details/4c70b23ca44953209cf0dea2431d5c08/?utm_source=chatgpt). Yu Yuan, Xijun Wang, Yichen Sheng, Prateek Chennuri, Xingguang Zhang, and Stanley Chan, 2024, *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 9.

[5] [PreciseCam: Precise Camera Control for Text-to-Image Generation](https://consensus.app/papers/details/785e5e0873365198b5fc8da2c569bddc/?utm_source=chatgpt). Edurne Bernal-Berdun, Ana Serrano, B. Masia, Matheus Gadelha, Yannick Hold-Geoffroy, Xin Sun, and Diego Gutierrez, 2025, *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 4.

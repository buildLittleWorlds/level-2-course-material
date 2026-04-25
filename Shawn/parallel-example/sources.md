# Sources: Style Fidelity Grid

These are Consensus-backed candidate sources. They are **abstract-checked only** in this worked example. Before using any source in a real paper, verify the title, authors, venue, DOI if available, and the exact claim the source supports.

## Exact Consensus searches used

- `text to image generation art style fidelity prompt engineering fine tuning LoRA diffusion models style transfer`
- `prompt engineering text to image generative models style keywords evaluation`
- `diffusion models style transfer LoRA fine tuning style consistency text image`

## Candidate sources

1. [Design Guidelines for Prompt Engineering Text-to-Image Generative Models](https://consensus.app/papers/details/9c2cf9a9c99853b8938d2a7b1454952b/?utm_source=chatgpt)  
   Vivian Liu and Lydia B. Chilton, 2021, *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*, citation count: 589.  
   Relevance: Useful background on how subject and style keywords affect text-to-image outputs.

2. [StyleInject: Parameter Efficient Tuning of Text-to-Image Diffusion Models](https://consensus.app/papers/details/2288b2aa822654208861809b6365feef/?utm_source=chatgpt)  
   Yalong Bai, Mohan Zhou, and Qing Yang, 2024, *ACM Transactions on Multimedia Computing, Communications and Applications*, citation count: 1.  
   Relevance: Useful for explaining why style adaptation may require more than prompt words.

3. [StyleDrop: Text-to-Image Generation in Any Style](https://consensus.app/papers/details/2443e8da44a959a590f5c4d5356673ff/?utm_source=chatgpt)  
   Kihyuk Sohn et al., 2023, *arXiv*, citation count: 196.  
   Relevance: Useful as a source direction on capturing nuanced style from limited reference material.

4. [Style Injection in Diffusion: A Training-Free Approach for Adapting Large-Scale Diffusion Models for Style Transfer](https://consensus.app/papers/details/1fb04a0fbe6f53d3b672c97d7ab5af2b/?utm_source=chatgpt)  
   Jiwoo Chung, Sangeek Hyun, and Jae-Pil Heo, 2023, *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 186.  
   Relevance: Useful background on style transfer and the challenge of preserving content while transferring style.

5. [Block-wise LoRA: Revisiting Fine-grained LoRA for Effective Personalization and Stylization in Text-to-Image Generation](https://consensus.app/papers/details/d747ba3f2b5f5d008ddfab648b32fdb4/?utm_source=chatgpt)  
   Likun Li, Haoqi Zeng, Changpeng Yang, Haozhe Jia, and Di Xu, 2024, *arXiv*, citation count: 7.  
   Relevance: Useful for the specialization angle: fine-tuning can improve style fidelity, but the project should test flexibility outside the tuned style.

## How these sources would support the paper

- Source 1 supports the prompt-engineering part of the project.
- Sources 2, 3, and 5 support the fine-tuning and style-specialization angle.
- Source 4 supports the content-versus-style tradeoff.

## Citation caution

Do not cite these sources as proof that a specific image model understands a named art movement. A safer claim is: "Research on text-to-image prompting and style transfer shows that style control is measurable but difficult."

# Motion Continuity Lab: Evaluating AI Animation Helpers Across Scene Beats

## Abstract

This worked example studies whether AI animation helpers preserve motion continuity across a short scene. The imagined Hugging Face Space, Motion Continuity Lab, asks a model to turn a character, object, and three-beat action into storyboard beats or animator notes. The project asks whether outputs support animation or merely describe attractive still frames. A small prompt comparison suggests that visually rich outputs can still fail as animation plans when characters, props, or causes change between beats. More practical "animator note" outputs may be less beautiful but more useful because they track physical motion and continuity. The paper argues that AI animation tools should be evaluated across sequences, not just by the quality of one generated image or scene description.

## 1. Introduction and research question

Animation is not just a series of pretty frames. It depends on continuity: a character moves, an object changes position, a mood shifts, and one beat causes the next. AI tools that generate vivid descriptions may help with inspiration, but they can still fail if they do not preserve motion logic.

This project asks:

> Which AI tools are best at helping with animation scene generation when the real challenge is motion continuity instead of a single pretty frame?

The imagined Space focuses on short scene planning rather than full video generation. It asks whether AI-generated beats can help an animator think through action across time.

## 2. Related work

Text-to-video research treats temporal consistency and motion quality as major evaluation challenges. EvalCrafter evaluates video generation across visual, content, motion, and alignment measures [1]. Work on LLMs as frame-level directors suggests that language models can help plan time-varying content for video generation [2]. Free-Bloom similarly uses an LLM director and diffusion animator to support semantic coherence over time [3]. T2V-CompBench and TC-Bench both focus on compositional and temporal challenges in generated video, including action, motion, and transitions [4, 5].

This classroom example does not generate full video, but it uses the same principle: animation tools should be judged by what happens across time.

## 3. Method

The imagined Space asks for:

- Character description
- Key object
- Three-beat action: start, change, end
- Mood shift
- Output mode: cinematic description, storyboard panels, or animator notes

Example prompt:

> A paper lantern floats away from a child during a rainy festival, then returns glowing brighter.

The outputs are scored with a continuity checklist:

| Criterion | Question |
|---|---|
| Character consistency | Does the character stay recognizable? |
| Object consistency | Do key props stay present and stable? |
| Motion cause | Does one beat cause the next? |
| Mood transition | Does emotion shift gradually? |
| Scene continuity | Does the setting stay coherent? |

## 4. Findings and discussion

The first outputs were visually appealing but weak as animation plans. They described a child with a lantern, then a lantern in rain, then a glowing lantern. The moments were pretty, but the movement between them was underdeveloped.

The three-beat prompt improved the structure, but continuity problems remained. In one output, the umbrella disappeared in the second beat and returned in the third. In another, the lantern changed color without explanation. These are small details, but animation depends on small details.

The most useful output mode was not the most poetic. The animator-notes style included concrete motion details: the lantern string stretches, the child steps forward, the umbrella tilts in the wind, and the lantern drifts behind a sign before returning. Those details made the sequence feel animate instead of static.

The finding is:

> For animation planning, outputs should be judged by continuity across beats, not by the beauty of individual frames.

## 5. Limitations

This is a small written-output test. It does not evaluate rendered animation or actual video. The rubric is hand-built and the example uses only a few scenes. A stronger study would compare multiple AI tools, save generated storyboards or clips, and ask animators or viewers to rate continuity.

The project also simplifies "animation quality." Real animation includes timing, spacing, squash and stretch, staging, acting, visual style, and sound. This example focuses only on continuity because it is a manageable starting point.

## 6. Conclusion

Motion Continuity Lab shows how an animation interest can become a research question. The central move is evaluating sequences rather than isolated outputs. AI tools can be impressive at mood and image language, but animation requires cause, change, and continuity. A student project can reveal that gap by testing whether characters, objects, and actions survive across beats.

## Candidate references

[1] [EvalCrafter: Benchmarking and Evaluating Large Video Generation Models](https://consensus.app/papers/details/5e8686725b6c5518a89bef0978df1266/?utm_source=chatgpt). Yaofang Liu et al., 2023, *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 205.

[2] [Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation](https://consensus.app/papers/details/2ce0ab5d61f950ffb6a1d8f0da490ff6/?utm_source=chatgpt). Susung Hong, Junyoung Seo, Sung-Jin Hong, Heeseong Shin, and Seung Wook Kim, 2023, *arXiv*, citation count: 49.

[3] [Free-Bloom: Zero-Shot Text-to-Video Generator with LLM Director and LDM Animator](https://consensus.app/papers/details/2ef4bf5dc82c58ecb6436c9a8bd39ff1/?utm_source=chatgpt). Hanzhuo Huang, Yufan Feng, Cheng Shi, Lan Xu, Jingyi Yu, and Sibei Yang, 2023, *arXiv*, citation count: 93.

[4] [T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-video Generation](https://consensus.app/papers/details/b27412def02b5982b774c0f80fb01bc9/?utm_source=chatgpt). Kaiyue Sun et al., 2024, *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, citation count: 77.

[5] [TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation](https://consensus.app/papers/details/c703a7222be5596d9eaacf867a2f8d5c/?utm_source=chatgpt). Weixi Feng, Jiachen Li, Michael Stephen Saxon, Tsu-Jui Fu, Wenhu Chen, and William Yang Wang, 2024, *arXiv*, citation count: 23.

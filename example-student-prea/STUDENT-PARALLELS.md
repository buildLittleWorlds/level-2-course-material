# Prea ↔ Student Parallels Guide

This document maps specific moments in Prea's example portfolio to each real student's interests and current work. Use it to point students to the parts of Prea's materials that are most directly relevant to what they're doing.

---

## Annabelle (Music — Opera & Jazz)

**Prea's research question progression (Journal Weeks 1–4)** is the most important parallel. Annabelle has observations and building experience but hasn't formulated a question. Prea went from "sentiment analysis misses something about debate" (Week 1) to a formal two-factor hypothesis (Week 4) across four weeks. Annabelle needs to go from "AI and music" to something like "do small models distinguish opera vocabulary from jazz vocabulary, or do they flatten both into generic music words?" — and Prea's journal shows exactly how that sharpening happens week by week.

**Journal Week 3 — The Consensus Detour.** Prea told Dr. Plate she had a hunch about prosody and he showed her Consensus. Three searches, three papers, one evening. Annabelle has domain expertise in opera and jazz but hasn't connected it to published research yet. She should read Week 3 and then run parallel searches: *"AI music genre classification,"* *"language models creative writing genre,"* *"computational musicology opera jazz."*

**Journal Week 5 — Building a broken Space on purpose.** Prea's Space 1 (distilgpt2 debate content scorer) was intentionally bad. Its job was to prove that text generation alone can't evaluate arguments. Annabelle has 7 Spaces but hasn't selected which three tell a research story. She should notice that Prea's first Space existed to be wrong — to motivate everything that came after. Annabelle's Space 1 should be a simple genre-agnostic music generator that produces generic output, setting up the question of whether models can do better when given genre-specific instructions.

**Research brief — Limitations section.** Annabelle's writing is descriptive but doesn't yet hedge claims or name limitations. Prea's brief (Section 5) is a masterclass in honest limitation-naming: single rater, n=20, ASR bias, hand-tuned weights. Annabelle should read that section specifically to understand what "writing like a researcher" means.

---

## Henry (Visual Perspectives & Camera Angles)

**The two-modality architecture** is the strongest parallel in the entire cohort. Prea built two separate approaches (text-side content scoring and audio-side prosodic analysis) and then connected them into a unified pipeline in Space 3. Henry has the exact same structure: Scene_describer (text-side) and Camera_angle_model_lab (image-side). Prea's Weeks 7–10 show how to connect two modalities into one pipeline. Henry should read those entries with the specific question: "How did Prea combine her two directions?"

**Journal Week 5 — The Mistral blog post.** Prea read an industry blog post and extracted an architectural pattern (thin client over API) that she couldn't afford, then rebuilt it with free components. Henry doesn't need this specific architecture, but the *move* — reading something from industry and adapting the pattern to free tools — is exactly the kind of thinking that separates a school project from research. Henry should notice how Prea cites a non-peer-reviewed source (the blog post) as an architectural reference while being clear it's not empirical evidence.

**Journal Week 10 — The correlation analysis.** Henry's experimental methodology is already strong (slider experiments, systematic variation). Prea's Week 10 shows what happens when you take that kind of systematic testing and add a quantitative analysis. Henry's version could be a scoring rubric for viewpoint-specific detail: does the model actually produce different spatial language for close-up vs. bird's-eye, or just swap a few words? Prea's Spearman correlation approach is a template.

**Research brief — Methods section (3.2, Dataset).** Prea describes her test set precisely: 20 clips, 10 TED, 10 WSDC, median length, range, speaker composition. Henry should model his own methods section on this: 10 scenes × 5 viewpoints × 3 models, with a clear description of what he measured and how.

---

## Sevilla (Animation)

**Journal Week 3 — Finding published research.** Sevilla uses five different AI tools but hasn't connected her animation interest to any literature. Prea's Week 3 Consensus searches are the template: three targeted searches in one sitting, each returning something useful. Sevilla's version: *"text generation animation storyboards,"* *"emotional tone AI creative writing,"* *"comparing language models creative writing."*

**Journal Weeks 5–7 — The architectural pivot.** Prea tried something (local wav2vec2), it failed (OOM on free tier), and the failure became the most interesting part of her story. Sevilla's AnimationwithMoods has a RUNTIME_ERROR. That error isn't a problem for the journal — it's material. Prea's journal shows how to write about failure as evidence: "I tried X, it broke because Y, which told me Z about the constraints I'm working under."

**The multi-AI comparison angle.** Sevilla already uses Claude, Gemini, ChatGPT, Deepseek, and Copilot. Prea compared models too (distilgpt2 vs. cardiffnlp twitter-roberta in Week 2, multiple Whisper variants in Week 7), but Sevilla's natural workflow of switching between five commercial AI tools is a richer comparison study than Prea attempted. The key is making it systematic. Prea's Week 2 side-by-side comparison (same inputs, two models, observe disagreement) is the minimal template.

---

## Emily (Politics, International Relations, Ethics)

**Prea's domain expertise driving everything.** Prea's debate experience shaped her entire project — she tested models on her own material, not generic inputs. Emily has Model UN experience and an interest in political news. She should notice that Prea never tested models on random text; she tested them on her own debate speeches. Emily should test models on her own material: Model UN position papers, news articles about topics she knows, political arguments she can evaluate from domain knowledge.

**Journal Week 3 — Adversarial testing.** Prea deliberately fed models sentences designed to confuse them (performative debate rhetoric that sentiment models misread). Emily's version: feed a bias-detection or sentiment model politically charged statements and see if the model's scoring reveals anything about its training data. Prea's adversarial testing approach (Week 3, lines 46–58) is the direct template.

**Journal Week 7 — Bias in AI.** Prea's Week 7 is about ASR racial bias, but the structure of her thinking applies to Emily's domain: "My project depends on Tool X. Tool X has documented biases. Those biases affect my results in the following specific way." Emily's version: "My project depends on a news summarizer / bias classifier. These models may have political biases baked in. Here's how I tested for that."

**Research brief — Related Work (Section 2).** Prea found six papers and organized them into three categories (prosody+persuasion, automated assessment, ASR bias). Emily should notice the organizational structure: not just a list of papers, but papers grouped by what question they address. Emily's categories might be: media bias detection, political NLP, AI ethics in news.

---

## Chengry (Medical & Diagnostic AI)

**Prea's three-Space progression.** Chengry has built real medical Spaces but they don't yet tell a story. Prea's three Spaces were: (1) intentionally limited baseline, (2) one-modality working prototype, (3) full pipeline. Chengry should map his existing Spaces onto this arc: disease_detectives as a baseline, medical_text_generator as the experiment, and a third Space that combines what he learned.

**Journal Week 4 — Committing to a hypothesis.** Chengry has the technical skill but hasn't stated a research question. Prea's Week 4 is where she wrote down a single-sentence testable hypothesis. Chengry's version might be: "When a small instruction-tuned model is asked to explain a medical condition to a patient vs. to a clinician, does the output use appropriately different vocabulary and reading level, or does the model produce the same explanation regardless of audience?" Writing it as one sentence is the key move.

**Research brief — Limitations section on domain expertise.** Prea acknowledged that SmolLM2 "has no idea what the WSDC format actually is" (Week 9). Chengry should notice this honesty: the model isn't a medical expert, and saying so explicitly is a research strength, not a weakness. Any medical AI project needs a prominent limitations section about the difference between what a small model generates and what a medical professional would say.

**Journal Week 9 — Asking real users.** Prea asked two teammates what they'd want from the tool. Chengry could do the equivalent: ask a family member, a friend, or a teacher what they'd want from a medical explanation tool. The answers Prea got ("tell me which ten seconds to listen to again" and "tell me what I did wrong") reshaped her entire interface design.

---

## George (Medical/Health AI — shifted from music)

**The topic pivot.** George came in interested in music and shifted to medical/health AI. Prea didn't pivot topics, but she pivoted *architecturally* in Weeks 5–7 (from local model loading to API-based thin client). The journal structure around a pivot is the same: name what you were doing, name what changed, name why. George should read Prea's pivot narrative and use the same structure to document his own shift from music to medical.

**Journal Week 1 — Testing with your own material.** Prea tested sentiment models on her own debate speeches. George should test health explanation models on health topics he actually cares about or has questions about, not generic examples. The specificity of using your own material is what makes the observations real.

**Space 3 design — The pipeline.** George has My_Health_Explainer running. Prea's Space 3 combined two modalities. George's Space 3 could combine: input a health topic + target audience (child, teen, adult, medical professional) → generate explanation → score readability → show comparison. The pipeline structure of Prea's Space 3 (input → two processing stages → combined output) is the template.

---

## Shawn (Image Generation & Art Styles)

**Prea's model comparison methodology.** Prea compared distilgpt2 and cardiffnlp twitter-roberta on the same inputs in Week 2. Shawn already has 12 image generation models in his collection. Prea's comparison structure (same prompt, different models, document what changes) is exactly what Shawn should be doing with his art style experiments: same text prompt, same style instruction, different models, compare outputs.

**Journal Week 5 — Temperature experiments.** Prea tested distilgpt2 at five temperature settings and documented what happened at each. Shawn should notice the methodology: systematic variation of one parameter while holding others constant. Shawn's version: same prompt, same model, vary the style instruction (anime → surrealist → watercolor → photorealistic) and document what actually changes in the output.

**Research brief — Results table format.** Prea presented her results in a clean table (clip set × three score types). Shawn's version could be a table of (prompt × style × model) showing some quality or style-adherence rating. The table format makes the comparison visible and analyzable.

**The "broken Space as material" lesson.** Shawn's AnimeSceneWriter has a RUNTIME_ERROR. Prea's entire Week 6 is about a Space that broke (OOM on wav2vec2). She documented the failure, explained why it happened, and used it to justify her architectural pivot. Shawn should do the same with AnimeSceneWriter: what went wrong, why, and what does that teach about the constraints of free-tier image generation?

---

## Bobby (Direction Uncertain — Game Dev / Generative AI background)

**Prea's entire arc as a road map.** Bobby went quiet but had strong early work. If he re-engages, he needs to see that Prea's project wasn't a straight line — it had detours (the Consensus search in Week 3), failures (the OOM crash in Week 6), and pivots (the architectural redesign in Week 7). Bobby's journal gap (20+ days silent) can be written about honestly, just as Prea was honest about her limitations. A re-entry journal entry that says "I stopped for three weeks, here's what I'm thinking now" is legitimate research documentation.

**Journal Week 4 — Picking a direction.** Bobby's immediate need is choosing a topic. Prea's Week 4 is where she committed to a specific hypothesis. Bobby should read it to see what "committing" looks like — not certainty, but specificity. "I'm going to test X using Y" is enough.

**The creative + technical blend.** Bobby's strongest early work blended narrative and game dev (the "One Last Bird" concept). Prea blended debate expertise and technical building. The parallel is: your existing domain interest (game dev, narrative) isn't separate from the research project — it *is* the research project. Bobby should look at how Prea's debate experience wasn't a side detail; it was the reason her project existed.

---

## How to Use This Document

This is an instructor reference. Don't hand the whole thing to students — point individual students to the specific Prea journal weeks or brief sections listed under their name. The most useful move is usually: "Read Prea's Week [X] entry. Notice [specific thing]. Now think about how that applies to what you're doing."

The universal parallels (relevant to everyone):

- **Week 3 (Consensus searches)** — Every student needs to find published research. Prea's Week 3 is the template.
- **Week 4 (committing to a hypothesis)** — Every student needs a research question. Prea's single-sentence hypothesis is the model.
- **Weeks 5–7 (the pivot)** — Every student has a failure or a gap. Prea shows how to write about it.
- **Week 10 (honest limitations)** — Every student needs a limitations section. Prea's is exemplary.
- **Research brief structure** — Every student will write one. Prea's brief is the format template.

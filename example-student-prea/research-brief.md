# Two-Factor Scoring of Short Debate Speeches Using Free Hugging Face Components

**Prea Callahan**
*AI + Research Level 2, Youth Horizons Learning, Spring 2026*

## Abstract

I describe a small pilot study on automated feedback for short persuasive speeches, motivated by my own experience as a World Schools (WSDC) debater. I hypothesized that combining acoustic-prosodic features (extracted from ASR word-level timestamps) with LLM-based content scoring would predict listener ratings of persuasiveness better than either modality alone. I built a free Hugging Face Spaces pipeline that uses Whisper-small (via the Hugging Face Inference API) for transcription with word-level timestamps, extracts four prosodic features in pure Python, and uses SmolLM2-1.7B-Instruct (also via the Inference API) for rubric-based content scoring. I tested the combined tool on 20 clips (10 TED openings and 10 student WSDC practice speeches) and computed Spearman rank correlations between the tool's three output scores and my own 1–5 persuasiveness ratings. The combined two-factor score correlated with my ratings more strongly (ρ = 0.63) than either the prosody-only score (ρ = 0.57) or the content-only score (ρ = 0.38). The improvement was larger on student debate clips (where content scoring was weakest) than on TED clips. This is a pilot with n=20, a single rater, and known ASR bias; the findings should not be generalized. The contribution of this brief is a reproducible, free-tools architecture that high school students can use to study prosody and content as separable, measurable components of persuasive speech.

## 1. Introduction

Debate judges in the WSDC format are asked to evaluate speeches on *content*, *style*, and *strategy*. In practice, style — the delivery of a speech — is where novice debaters get their most variable ballots. I have lost rounds I thought I should have won and won rounds I thought I had lost, and the difference has usually come down to a judge's note about pacing, emphasis, or confidence. This project asks whether a small AI tool, built by a student using only free components, can make delivery measurable in a way that is useful for practice.

The hypothesis I committed to in Week 4 of my course was that acoustic-prosodic features of a short persuasive speech — speaking rate, pause frequency, pause duration, and speaking-rate variance across sections — correlate with listener ratings of persuasiveness at least as strongly as content features do, and that a pipeline combining the two produces more useful feedback than either alone. The contribution of this brief is not a novel result about prosody; the prosody-persuasion connection is well established in the literature. It is instead a report on whether a high school student can actually build and test this pipeline on a free Hugging Face account and get correlations that at least hint at the published effects.

## 2. Related work

**Prosody and persuasion.** Kišiček (2018) reviews the role of prosodic features — pitch, loudness, tempo, pauses — in argumentation and concludes that prosodic choices carry persuasive weight independent of propositional content. Pejčić, Trajković, and Janković (2015) studied acoustic-prosodic features in Serbian and English political speech and found correlations between persuasiveness ratings and both pause duration and within-unit speaking-rate variance. These two papers were the closest match to the experiment I imagined, and they are the reason I chose pause-based and rate-based features over pitch or energy features (which are harder to compute reliably on phone audio).

**Automated assessment of speaking.** Gomes et al. (2023) describe automated assessment of public-speaking performance using a combination of acoustic and text features and report that multi-modal approaches outperform text-only or audio-only baselines on persuasiveness prediction. That paper directly motivated the two-factor (prosody + content) design of my Space 3.

**ASR bias.** Koenecke et al. (2020) document substantial racial disparities in the word error rates of commercial ASR systems in the United States, with error rates for Black speakers roughly twice those for white speakers. Li et al. (2024) show that similar disparities exist across accented English speakers more broadly in recent open ASR models. Since my downstream prosodic features depend on Whisper's word-boundary timestamps, and two of the five students whose clips I used are non-native English speakers, the findings of Koenecke et al. and Li et al. are directly relevant limitations of my project. I cite both and discuss the implications in Section 5.

**Architectural reference (non-peer-reviewed).** Mistral AI (2025) published a blog post titled *Designing a speech-to-speech assistant* that describes the Voxtral pipeline: a thin, stateful client that routes audio through a speech-to-text stage, an LLM reasoning stage, and a text-to-speech stage as cleanly separated services. I do not cite this as empirical evidence, but the architectural pattern — transcription with timestamps, then LLM reasoning over the transcript — is the pattern I ended up implementing with free Hugging Face components after discovering that the Mistral API was not free and that loading a local audio model into a free-tier Space exceeded available memory.

## 3. Methods

### 3.1 Pipeline architecture

Space 3 of my portfolio implements the full pipeline as a Gradio interface that makes two calls to the Hugging Face Inference API per speech:

1. **Transcription.** The audio file is sent to `openai/whisper-small` with the `return_timestamps='word'` parameter. The response contains a list of words with start and end times in seconds.
2. **Prosodic feature extraction.** In pure Python, I compute four features from the word-level timestamps: (i) words per minute over the whole clip, (ii) the number of pauses longer than 400 ms (defined as gaps between `word[i].end` and `word[i+1].start`), (iii) the population variance of those pause durations, and (iv) the population variance of words-per-minute across the first, middle, and final thirds of the speech.
3. **Content scoring.** The transcript is sent to `HuggingFaceTB/SmolLM2-1.7B-Instruct` with a rubric prompt that asks for JSON-formatted scores from 1 to 5 on three dimensions (claim clarity, evidence quality, rebuttal strength) plus a short coaching note.
4. **Score combination.** The four prosodic features are mapped to a 0–100 delivery score by a hand-tuned normalization (see Section 3.3). The three content sub-scores are averaged and rescaled to 0–100. The combined score is the arithmetic mean of delivery and content.

No model weights are loaded locally. The Space itself holds no state beyond a single HF access token in an environment variable. The round-trip latency for a 90-second clip is approximately 15 seconds total (8 seconds for Whisper, 6 seconds for SmolLM2, and effectively instant for the Python feature extraction).

### 3.2 Dataset

I tested the pipeline on 20 short clips (median length 97 seconds, range 42–180 seconds):

- **TED set (n=10).** Openings of ten TED and TEDx talks on English-language channels, clipped to the first coherent argument. I selected talks from a range of speakers and topics and avoided clips with music beds.
- **Student WSDC set (n=10).** Practice speeches recorded by five members of my school WSDC team (myself included), two clips per speaker. Recordings were made on phone microphones in classroom settings and saved as WAV files at 16 kHz mono.

Of the five student speakers, three were native English speakers and two were non-native English speakers (first language Mandarin for one; first language Tagalog for the other). This composition is relevant to the limitations discussion.

### 3.3 Scoring normalization

The mapping from prosodic features to a 0–100 delivery score is hand-tuned, not learned. The mapping rewards speaking rates in the 155–190 wpm range, pause counts of 5–12, and higher values of pause-duration variance and speaking-rate variance across thirds. The weights (0.30 speaking rate, 0.25 pause count, 0.20 pause-duration variance, 0.25 speaking-rate variance) are my own guesses. This is a pilot-grade choice and is one of the reasons the results in Section 4 should be interpreted cautiously.

### 3.4 Evaluation

Before running any clip through the tool I listened to each of the 20 clips and assigned a subjective persuasiveness rating on a 1–5 scale, recording each rating in a CSV before seeing any tool output. I then ran every clip through Space 3 and recorded the delivery, content, and combined scores. I computed Spearman rank correlations between my ratings and each of the three tool scores, overall and separately for the TED and student WSDC subsets.

## 4. Results

| Clip set          | n  | Delivery ↔ rating | Content ↔ rating | Combined ↔ rating |
|-------------------|----|-------------------|------------------|-------------------|
| TED               | 10 | 0.52              | 0.48             | 0.61              |
| Student WSDC      | 10 | 0.63              | 0.24             | 0.58              |
| **Overall**       | 20 | **0.57**          | **0.38**         | **0.63**          |

Three observations stood out.

**First**, the combined two-factor score was the best predictor of my own ratings overall (ρ = 0.63), marginally better than the prosody-only score (ρ = 0.57) and substantially better than the content-only score (ρ = 0.38). This is consistent with the prediction from Gomes et al. (2023) that multi-modal scoring outperforms single-modality approaches on persuasiveness prediction, although my sample is far too small to make that comparison quantitatively.

**Second**, on the student WSDC subset specifically the content score collapsed (ρ = 0.24). I believe this is because SmolLM2-1.7B-Instruct has no specialized training on debate and the rubric prompt can only do so much; on WSDC clips, where arguments are structured by WSDC conventions that the model does not know, its scoring was close to random. The delivery score, by contrast, held up on WSDC clips (ρ = 0.63), possibly because prosodic differences are larger in practice recordings made by novice debaters than in polished TED performances.

**Third**, on the TED subset the two modalities were roughly balanced (ρ = 0.52 vs 0.48). This is also plausible: TED speakers are already polished in delivery, so prosodic variance across the set is smaller, and the content of a TED talk opening is closer to the register SmolLM2 has presumably seen in its training data.

## 5. Limitations

**Pilot scale (n=20).** The sample is far too small to support any general claims. The Spearman correlations are informative only about the pipeline's behavior on this specific set of 20 clips. A real evaluation would need a larger, more diverse test set, a held-out validation split, and ideally a comparison against a random-scoring baseline.

**Single rater.** I rated all 20 clips myself. A real study would use multiple raters and report an inter-rater agreement metric (e.g., Krippendorff's alpha). I also cannot rule out rating drift over the course of the session, since I listened to all 20 clips in one sitting.

**Hand-tuned scoring normalization.** The delivery-score mapping is not learned from data; it is a hand-crafted function whose weights reflect my own sense of what good WSDC delivery sounds like. Different weighting schemes would produce different delivery scores and different correlations. A better study would learn the mapping from ratings on a training set.

**ASR bias on non-native speakers.** Whisper has documented performance disparities across speaker groups (Koenecke et al. 2020; Li et al. 2024). Two of the five student speakers in my dataset are non-native English speakers, and their clips make up four of the ten WSDC recordings. Any word-boundary error in Whisper's transcription propagates directly into my pause-count and variance features. I did not correct for this and did not stratify my analysis by speaker origin.

**Small-model content scoring.** SmolLM2-1.7B-Instruct is a general-purpose small language model. It is not an expert on WSDC or on debate more broadly. A better pipeline would use a larger model, or preferably a model fine-tuned on a corpus of real debate judge ballots.

**Single cultural tradition.** The prosodic patterns Kišiček (2018) identifies as persuasive are specific to argumentative traditions that value certain styles of pause, emphasis, and tempo. WSDC is itself a particular tradition, heavily shaped by British and Commonwealth debate conventions. A tool trained or tuned on WSDC will not generalize to other persuasive speech traditions, and I do not claim that it should.

**Rubric prompt fragility.** The SmolLM2 rubric prompt I use asks the model to return strict JSON. In about 10% of the clips I tested during development, the model returned non-JSON text and my parser fell back to zero scores. Space 3 includes a fallback branch for this case but it is not a stable production behavior.

## 6. Conclusion and future work

The pilot study described here produced a modest but encouraging result: a two-factor scoring pipeline built entirely from free Hugging Face components can reach a Spearman rank correlation of 0.63 with a single student rater's persuasiveness judgments on a 20-clip test set, with the combined score outperforming either modality alone. The more interesting finding, I think, is that the pipeline architecture — a thin Gradio client that makes API calls to a transcription model and a small instruction-tuned LLM — is reproducible by a high school student with no local GPU, no paid API, and no specialized infrastructure. That architecture is the one Mistral AI described in their Voxtral blog post, translated into free components.

Future work I would pursue if I continued this project past the course:

1. **Larger and more diverse test set.** At least 60 clips drawn from multiple tournaments, with stratified sampling by speaker origin and clip length.
2. **Multiple raters and inter-rater agreement.** Ideally three raters including at least one experienced WSDC judge.
3. **Learned scoring weights.** Replace the hand-tuned delivery normalization with a small regression trained on a held-out rating set.
4. **Fine-tuned content scoring model.** Collect anonymized WSDC judge ballots and fine-tune a small instruction-tuned model on real rubric evaluations.
5. **ASR bias audit.** Stratify all results by native-speaker status and report separately. If the tool is worse on non-native speakers it should not be deployed until that gap is addressed.
6. **Practice-mode integration.** Turn the tool into a real team-practice loop: record, score, drill the three longest pauses the "Coach" tab flags, re-record, compare.

## References

Gomes, J., Pimentel, A., & Silva, H. (2023). Automatic assessment of public speaking performance using multi-modal features. *Proceedings of Interspeech 2023*, 4802–4806.

Kišiček, G. (2018). The persuasive power of prosodic features. *Informal Logic*, 38(2), 209–225. https://doi.org/10.22329/il.v38i2.5098

Koenecke, A., Nam, A., Lake, E., Nudell, J., Quartey, M., Mengesha, Z., Toups, C., Rickford, J. R., Jurafsky, D., & Goel, S. (2020). Racial disparities in automated speech recognition. *Proceedings of the National Academy of Sciences*, 117(14), 7684–7689. https://doi.org/10.1073/pnas.1915768117

Li, R., Patel, T., & Wang, J. (2024). Evaluating bias in automatic speech recognition on accented English. *Proceedings of NAACL 2024*, 4210–4222. https://aclanthology.org/2024.naacl-long.246/

Mistral AI. (2025). *Designing a speech-to-speech assistant* [Blog post]. https://mistral.ai/news/designing-a-speech-to-speech-assistant

Pejčić, A., Trajković, G., & Janković, D. (2015). Acoustic-prosodic features of persuasive political discourse: A comparative study. *Govor*, 32(2), 115–138.

---

*Brief prepared as the capstone written artifact for AI + Research Level 2, Youth Horizons Learning, Spring 2026. All code is available in the sibling `space1-content-scorer/`, `space2-delivery-analyzer/`, and `space3-speech-judge-assistant/` folders. Portfolio: [README.md](README.md). Full research journal: [research-journal.md](research-journal.md).*

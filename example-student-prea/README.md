# Prea Callahan — AI + Research Level 2 Portfolio

I'm a Grade 11 student in the Greater Toronto Area. I debate in the World Schools (WSDC) format and I want to study something at the intersection of linguistics, cognitive science, and computer science in university. Over 11 weeks in AI + Research Level 2, I built a free-tools tool that helps debaters see what their delivery is actually doing — and wrote a short research brief about whether it works.

## The Question

Can a free, student-built AI tool give useful feedback on a debate speech — not just on *what was said*, but on *how it was said*? And if I combine prosodic features (from the audio) with content scoring (from the transcript), do the two signals together predict persuasiveness better than either one alone?

## The Hypothesis

> Acoustic-prosodic features of a short persuasive speech — specifically speaking rate, pause frequency, pause duration, and speaking-rate variance across sections of the speech — correlate with listener ratings of persuasiveness at least as strongly as content features do, and a pipeline that combines the two kinds of features produces more useful feedback than either modality alone.

## The Journey

I came into this course thinking I could build a debate feedback tool by running debate transcripts through a sentiment model. Weeks 1–3 proved that was hopeless: text-based sentiment classifiers read *what* I said but had no idea *how* I said it, which is the entire variable I cared about. In Week 3 I found my first peer-reviewed sources on prosody and persuasion via Consensus, which turned my hunch into a formal hypothesis in Week 4.

Weeks 5–7 were the interesting stretch. I built a distilgpt2 text baseline (Space 1), read a Mistral blog post about the Voxtral speech-to-speech pipeline, got excited about the architecture, and then realized the Mistral API wasn't free. I tried to run a local audio emotion model directly on a Hugging Face Space instead and hit the free-tier compute wall on a 90-second clip. That failure was the pivot. I realized the architectural *pattern* from the Mistral blog post — transcription with timestamps, then LLM reasoning over the transcript — was correct, but I needed free components. From Week 7 on I rebuilt everything as a thin Gradio client that calls the Hugging Face Inference API for Whisper-small transcription, computes prosodic features in pure Python from Whisper's word-level timestamps, and scores content through SmolLM2-1.7B-Instruct. No local model weights. Boots in seconds. Free.

Weeks 8–10 were the experiment. I recorded five of my own and my teammates' WSDC practice speeches, collected ten TED Talk openings from YouTube, and tested the combined tool on all 20. Week 11 was the writing.

## Three Spaces

| Space | What It Does | What I Learned |
|-------|--------------|----------------|
| [**Debate Content Scorer (Baseline)**](space1-content-scorer/) | distilgpt2 text playground framed as a "continue this debate speech" generator | Text generators are not evaluators. This Space's job in my portfolio is to be the *wrong* approach that motivated the audio pivot. |
| [**Delivery Analyzer**](space2-delivery-analyzer/) | Thin-client Space: audio → Whisper-small (via HF Inference API) → prosodic features in pure Python | The Mistral Voxtral architectural pattern works perfectly well with free HF components. No local model loading means no compute wall. |
| [**WSDC Speech Judge Assistant**](space3-speech-judge-assistant/) | Full two-factor pipeline: delivery score + content score from SmolLM2-1.7B-Instruct, with Score / Breakdown / Coach tabs | Combined two-factor scoring (prosody + content) correlated with my persuasiveness ratings better than either modality alone (Spearman ρ = 0.63 on n=20). |

## Results (Week 10, n=20)

I tested Space 3 on 20 clips (10 TED, 10 student WSDC) and computed Spearman rank correlations between my own 1–5 persuasiveness ratings and each of the tool's three scores:

| Clip set         | Delivery ↔ rating | Content ↔ rating | Combined ↔ rating |
|------------------|-------------------|------------------|-------------------|
| TED (n=10)       | 0.52              | 0.48             | 0.61              |
| WSDC (n=10)      | 0.63              | 0.24             | 0.58              |
| **Overall (n=20)** | **0.57**        | **0.38**         | **0.63**          |

n=20 is a pilot, single-rater, small-scale. None of this would survive a real evaluation. But three things came out that surprised me enough to write up:

1. **On student debate clips, the delivery (prosody) score is more than twice as informative as the content score** — which makes sense because SmolLM2-1.7B-Instruct is not a debate expert and because novice debaters make more delivery mistakes than content mistakes.
2. **On TED clips the two modalities roughly match**, which also makes sense — TED speakers are polished and prosody differences become subtler.
3. **Combining the two always helps**, even when one modality is weak. The combined score beats both individual scores in both subsets.

## Research Journal

My [research journal](research-journal.md) tracks all 11 weeks in detail. The entries I'd recommend reading first:

- **Week 3** — The Consensus detour. How I went from "I think prosody matters" to "here are three peer-reviewed papers that say it does."
- **Weeks 5–7** — The architectural pivot. Mistral Voxtral blog post → local wav2vec2 compute wall → thin-client Inference API rebuild.
- **Week 10** — The end-to-end evaluation and the honest limitations I can't design around.

## Research Brief

The distinctive artifact of my portfolio is a [short research brief](research-brief.md) ([.docx version](research-brief.docx)) — about four pages in the format of a miniature research paper, with an abstract, related work, methods, results, limitations, and references. It cites six peer-reviewed papers I found through Consensus plus the Mistral blog post as a non-peer-reviewed architectural reference.

## Sources I found via Consensus

- Kišiček, G. (2018). The persuasive power of prosodic features.
- Pejčić, A., Trajković, G., & Janković, D. (2015). On acoustic-prosodic features of political speeches.
- Gomes, J., et al. (2023). On automatic assessment of public speaking performance.
- Koenecke, A., et al. (2020). Racial disparities in automated speech recognition. *PNAS*.
- Li, R., et al. (2024). Evaluating bias in ASR on accented English. *NAACL*.
- Mistral AI. (2025). Designing a speech-to-speech assistant (blog post — architectural reference, not peer-reviewed).

## ML Concepts I Used

- **Classification vs. generation.** Text generators cannot evaluate arguments. Week 5.
- **Architecture as a transferable idea.** The Mistral Voxtral blog post described an architecture I could not afford, but I could copy the pattern with free components. Weeks 5–7.
- **Thin client over inference API.** The trick that made this project possible on a free Hugging Face account: don't hold model weights; make HTTP calls instead.
- **Prosodic feature extraction from ASR timestamps.** Pauses and speaking-rate variance are computable from Whisper's word-level timestamp output in pure Python.
- **LLM-as-judge with a rubric prompt.** SmolLM2-1.7B-Instruct returns constrained JSON when given a rubric. Useful, not expert.
- **Spearman rank correlation** for validating a scoring tool against subjective ratings on a small sample.
- **ASR bias.** Per Koenecke et al. and Li et al., Whisper is not equally accurate across speaker groups, and the downstream prosodic features inherit that.

## What I'd Do Next

- Collect a larger test set (at least 60 clips) with multiple raters and compute inter-rater agreement.
- Fine-tune a content-scoring model on real WSDC judge ballots instead of rubric-prompting SmolLM2.
- Add forced alignment (something like `wav2vec2-forced-alignment` via the Inference API) to get more reliable pause boundaries than Whisper's word timestamps on non-native speakers.
- Stratify the analysis by speaker origin and see whether the tool is systematically worse on clips from non-native English speakers — it almost certainly is.
- Turn the tool into a practice mode for my team: record, score, drill the specific moments the "Coach" tab flags, re-record.

## Hugging Face Collection

14 models and 9 Spaces, curated across 11 weeks. Early items are sentiment and emotion classifiers I tested in Weeks 1–3. Middle items are the Whisper variants and small instruction-tuned models I evaluated for the pipeline. Later items are my three Spaces and four comparable Spaces other people built for speech analysis, each with a tasting note on what I took from looking at them.

---

*Built during AI + Research Level 2 at Youth Horizons Learning, Spring 2026. This is an example student portfolio for the course.*

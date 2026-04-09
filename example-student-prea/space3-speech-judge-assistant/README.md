---
title: WSDC Speech Judge Assistant
emoji: ⚖️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: true
---

# Space 3 — WSDC Speech Judge Assistant

*Part of Prea Callahan's AI + Research Level 2 portfolio. See the full [research journal](../research-journal.md) and the [research brief](../research-brief.md) for context.*

## What this Space does

This is the full two-factor pipeline. You upload a short WSDC-style speech clip (10 seconds to about 4 minutes) and the Space returns three scores plus two kinds of feedback:

- **Delivery score** (0–100), derived from four prosodic features computed from Whisper-small word-level timestamps
- **Content score** (0–100), derived from SmolLM2-1.7B-Instruct's rubric evaluation of the transcript on three dimensions (claim clarity, evidence quality, rebuttal strength)
- **Combined score** (simple average of the two)
- **"Moments that mattered"** — the three longest pauses in the clip with timestamps, so a debater can listen back to those exact seconds
- **Coaching note** — a short paragraph from the LLM, constrained to 2–3 sentences by the rubric prompt

## Three tabs

1. **Score.** Just the three numbers. The use case Teammate B asked for — one glance, one number, one sentence.
2. **Breakdown.** The four prosodic features listed individually, the LLM's rubric output on all three dimensions, and the full transcript. The use case for someone who wants to dig in.
3. **Coach.** The longest-pause timestamps and the LLM's coaching paragraph. The use case Teammate A asked for — pointers back to specific moments in the clip.
4. **Raw JSON.** For debugging. For me.

See research-journal.md, Week 9, for the interview notes that shaped this tab structure.

## The architecture, in one diagram

```
  audio file
      │
      ▼
  Hugging Face Inference API
    openai/whisper-small         ──► transcript + word-level timestamps
      │                               │
      │                               ▼
      │                         Python prosodic features:
      │                           - words per minute
      │                           - pause count (>400ms)
      │                           - pause-duration variance
      │                           - speaking-rate variance (thirds)
      │                               │
      ▼                               ▼
  Hugging Face Inference API     Hand-tuned normalization
    SmolLM2-1.7B-Instruct         (features → 0–100 delivery score)
    + WSDC rubric prompt                  │
      │                                   │
      ▼                                   ▼
  rubric JSON                         Combined score (average)
    - claim clarity
    - evidence quality
    - rebuttal strength
    - coaching note
```

The whole pipeline is a thin client over the Hugging Face Inference API. No local model weights, no OOMs on free-tier CPU. The round trip for a 90-second clip is about 15 seconds end to end: 8 seconds for Whisper, 6 seconds for SmolLM2, and the Python feature extraction is effectively instant.

This is the free-tools translation of the Mistral Voxtral pipeline pattern described in *Designing a speech-to-speech assistant* (Mistral AI, 2025). That blog post is the architectural ancestor of this Space. See research-journal.md, Week 5, for the pivot story.

## Results from Week 10

I tested Space 3 on 20 clips (10 TED Talk openings and 10 student WSDC practice speeches). I rated each clip on a 1–5 persuasiveness scale before running it through the tool, then computed Spearman rank correlations between my ratings and each of the three scores the tool produces.

| Clip set                   | Delivery ↔ rating | Content ↔ rating | Combined ↔ rating |
|----------------------------|-------------------|------------------|-------------------|
| TED (n=10)                 | 0.52              | 0.48             | 0.61              |
| Student WSDC (n=10)        | 0.63              | 0.24             | 0.58              |
| **Overall (n=20)**         | **0.57**          | **0.38**         | **0.63**          |

The combined score was the best predictor of my intuitive rating. On student debate clips, the delivery score is substantially more useful than the content score — SmolLM2 is not a debate expert and the rubric prompt can only push it so far. On TED clips, the two modalities roughly match.

**n=20 is a pilot study.** These numbers would not survive a real evaluation. See the research brief for the honest limitations discussion.

## Running this Space

You need a Hugging Face access token with read-level permissions. Add it as a Space secret:

1. **Settings → Variables and secrets → New secret**
2. Name: `HF_TOKEN`
3. Value: a read token from your [Hugging Face settings page](https://huggingface.co/settings/tokens)

The free Inference API tier is rate-limited but works fine for demo use.

## Known limitations

- **Small test set (n=20).** Everything above the Spearman table is either hand-tuning or extrapolation.
- **Single rater.** I rated all 20 clips myself. A real evaluation would need multiple raters and an inter-rater agreement metric.
- **ASR bias on non-native speakers.** Per [Koenecke et al. (2020)](https://www.pnas.org/doi/10.1073/pnas.1915768117) and [Li et al. (2024)](https://aclanthology.org/2024.naacl-long.246/), Whisper has documented performance disparities across speaker groups. Two of my five teammate sources are non-native English speakers. I did not correct for this.
- **Small-model content scoring.** SmolLM2-1.7B-Instruct is not a debate expert. A better study would fine-tune a content-scoring model on actual judge ballots.
- **Hand-tuned delivery normalization.** The mapping from prosodic features to a 0–100 delivery score is not learned from data. It is hand-tuned to a small n and reflects my own sense of what "good delivery" looks like in WSDC, which is itself one cultural tradition among many ([Kišiček 2018](https://doi.org/10.22329/i.v0i0.5098)).

## Files

- `app.py` — Gradio Blocks interface with four tabs and the full pipeline.
- `requirements.txt` — Just `gradio` and `requests`.

## Course

Built for AI + Research Level 2, Youth Horizons Learning, Spring 2026.

---
title: Delivery Analyzer
emoji: 🎤
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Space 2 — Delivery Analyzer

*Part of Prea Callahan's AI + Research Level 2 portfolio. See the full [research journal](../research-journal.md) for context.*

## What this Space does

You upload a short speech clip (10 seconds to about 4 minutes) and this Space returns two things:

1. A transcript produced by Whisper-small, and
2. Four prosodic features computed from Whisper's word-level timestamps:
   - **Speaking rate** (words per minute over the whole clip)
   - **Pause count** (number of silences longer than 400 ms)
   - **Pause-duration variance** (how uneven those pauses are)
   - **Speaking-rate variance across thirds** (whether the speaker changes pace between the opening, middle, and closing of the speech)

Those four numbers are the "delivery" half of the two-factor scoring pipeline in Space 3.

## The architecture, and why it looks this way

This is where my project made its biggest turn. Originally I planned to load an audio emotion-recognition model directly into this Space. That failed on free-tier CPU — see research-journal.md, Week 6, for the compute wall write-up. Around the same time my instructor shared Mistral's "Designing a speech-to-speech assistant" blog post, which describes their Voxtral pipeline: transcription with timestamps, then LLM reasoning over the transcript, cleanly separated. The architectural idea is the right one. The components they named aren't free.

So this Space is a **free-tools translation of the Mistral pattern**:

| Mistral pipeline     | My free-tools pipeline                                       |
|----------------------|--------------------------------------------------------------|
| Voxtral-small (STT)  | `openai/whisper-small` via Hugging Face Inference API        |
| Mistral LLM          | `HuggingFaceTB/SmolLM2-1.7B-Instruct` via Inference API (Space 3) |
| Mistral TTS          | Not needed for my project — I only need feedback, not a voice reply |

The Space itself holds no model weights. It boots in under five seconds on free-tier CPU and the heavy lifting happens on Hugging Face's servers. This is what "thin client over API" means in practice.

## Running this Space

The Space needs a Hugging Face access token to call the Inference API. Add one as a Space secret:

1. Go to **Settings → Variables and secrets → New secret**
2. Name: `HF_TOKEN`
3. Value: a read-level token from your [Hugging Face settings page](https://huggingface.co/settings/tokens)

The free Inference API tier is rate-limited but more than sufficient for demo use. A typical 90-second clip round-trips in about 8 seconds.

## Interpreting the features

The features are deliberately simple. I did not try to compute pitch or energy contours — both are noisy on phone recordings and neither is cleanly derivable from the Whisper API response. The four features I chose are all computable from word-level start/end timestamps alone, which makes the whole pipeline robust to bad mic conditions (and also makes it cheap).

Rough reference ranges from my own Week 8 data (n=5 — these are **not** generalizable, they are just reference values for a single student team's recordings):

| Feature                                   | Low        | Mid        | High        |
|-------------------------------------------|------------|------------|-------------|
| Speaking rate (wpm)                       | ~150       | ~170       | ~200        |
| Pauses > 400 ms                           | 2          | 5–8        | 12+         |
| Pause-duration variance                   | 0.05       | 0.20       | 0.40+       |
| Speaking-rate variance (across thirds)    | 3          | 10–20      | 25+         |

Higher pause-duration variance and higher speaking-rate variance both track with my intuitive judgment that a speech "landed." See research-journal.md, Week 10, for the correlation analysis.

## Known limitations

- **ASR bias.** Whisper has documented performance disparities across speaker groups ([Koenecke et al. 2020](https://www.pnas.org/doi/10.1073/pnas.1915768117); [Li et al. 2024](https://aclanthology.org/2024.naacl-long.246/)). Two of the five student sources in my Week 8 data are non-native English speakers. I did not correct for this and the prosodic features are only as reliable as the word-boundary timestamps Whisper returns.
- **Single-speaker assumption.** If there are two speakers on the clip, the word-level timestamps will span both and the features will be garbage. I did not add diarization.
- **Short clips.** Clips with fewer than 20 transcribed words get a warning instead of scores. Variance features are unstable below that threshold.

## Files

- `app.py` — Gradio interface and feature extraction.
- `requirements.txt` — Dependencies (just `gradio` and `requests`; no model weights).

## Course

Built for AI + Research Level 2, Youth Horizons Learning, Spring 2026.

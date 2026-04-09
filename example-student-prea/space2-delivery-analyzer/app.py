"""
Space 2 — Delivery Analyzer.

Thin-client architecture (the free-tools version of the Mistral Voxtral
pipeline pattern described in research-journal.md, Weeks 5–7):

    audio upload
        -> Hugging Face Inference API: openai/whisper-small
           (return_timestamps='word' for word-level start/end times)
        -> pure-Python prosodic feature extraction
        -> Gradio output

No local model loading. The Space boots in seconds on free-tier CPU because
it doesn't hold any weights in memory — Whisper runs on Hugging Face's
servers via the Inference API and this Space just formats the request and
reads the response.

Requires a Hugging Face token in the HF_TOKEN Space secret (read access is
enough; the free Inference API tier is rate-limited but sufficient for
demo use).

See research-journal.md, Week 8, for the first real numbers table and
Week 10 for the end-to-end evaluation.
"""

import json
import os
import statistics
from typing import Any

import gradio as gr
import requests

HF_TOKEN = os.environ.get("HF_TOKEN", "")
WHISPER_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
PAUSE_THRESHOLD_SECONDS = 0.4
MIN_WORDS_FOR_RELIABLE_FEATURES = 20


def transcribe_with_word_timestamps(audio_path: str) -> dict[str, Any]:
    """Send audio file to the HF Inference API and ask for word-level timestamps."""
    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Add it as a Space secret "
            "(Settings -> Variables and secrets -> New secret)."
        )
    with open(audio_path, "rb") as f:
        data = f.read()
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "audio/wav",
    }
    params = {"return_timestamps": "word"}
    response = requests.post(
        WHISPER_URL,
        headers=headers,
        params=params,
        data=data,
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Inference API error {response.status_code}: {response.text[:500]}"
        )
    return response.json()


def extract_words_with_times(api_response: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize the Whisper API response into a list of {word, start, end} dicts."""
    chunks = api_response.get("chunks") or api_response.get("words") or []
    words: list[dict[str, Any]] = []
    for c in chunks:
        word = c.get("text") or c.get("word") or ""
        ts = c.get("timestamp") or (c.get("start"), c.get("end"))
        if not word or ts is None:
            continue
        start, end = ts if isinstance(ts, (list, tuple)) else (ts, None)
        if start is None or end is None:
            continue
        words.append({"word": word.strip(), "start": float(start), "end": float(end)})
    return words


def compute_prosodic_features(words: list[dict[str, Any]]) -> dict[str, float]:
    """Compute the four features Prea's journal defines in Week 6.

    1. Words per minute over the whole clip.
    2. Number of pauses longer than PAUSE_THRESHOLD_SECONDS.
    3. Variance of the durations of those pauses.
    4. Variance of words-per-minute across the first, middle, and last
       thirds of the speech.
    """
    if len(words) < MIN_WORDS_FOR_RELIABLE_FEATURES:
        raise ValueError(
            f"Only {len(words)} words transcribed. "
            f"Need at least {MIN_WORDS_FOR_RELIABLE_FEATURES} for reliable features."
        )

    total_duration = words[-1]["end"] - words[0]["start"]
    if total_duration <= 0:
        raise ValueError("Clip has zero or negative duration after transcription.")

    wpm_overall = len(words) / (total_duration / 60.0)

    # Pauses: gaps between word[i].end and word[i+1].start.
    pause_durations = [
        words[i + 1]["start"] - words[i]["end"]
        for i in range(len(words) - 1)
        if words[i + 1]["start"] - words[i]["end"] > PAUSE_THRESHOLD_SECONDS
    ]
    pause_count = len(pause_durations)
    pause_variance = (
        statistics.pvariance(pause_durations) if len(pause_durations) >= 2 else 0.0
    )

    # Speaking-rate variance across thirds.
    n = len(words)
    third = n // 3
    if third < 2:
        rate_variance = 0.0
    else:
        thirds = [words[0:third], words[third : 2 * third], words[2 * third :]]
        rates = []
        for section in thirds:
            dur = section[-1]["end"] - section[0]["start"]
            if dur > 0:
                rates.append(len(section) / (dur / 60.0))
        rate_variance = statistics.pvariance(rates) if len(rates) >= 2 else 0.0

    return {
        "wpm_overall": round(wpm_overall, 1),
        "pause_count_over_400ms": pause_count,
        "pause_duration_variance": round(pause_variance, 3),
        "speaking_rate_variance_across_thirds": round(rate_variance, 1),
        "num_words": len(words),
        "total_duration_seconds": round(total_duration, 1),
    }


def analyze(audio_path: str):
    if not audio_path:
        return "Please upload or record an audio clip.", "", ""
    try:
        api_response = transcribe_with_word_timestamps(audio_path)
        words = extract_words_with_times(api_response)
        if not words:
            return (
                "Whisper returned no word-level timestamps. Try a longer clip or "
                "check that the audio is a recognizable language.",
                "",
                "",
            )
        features = compute_prosodic_features(words)
    except ValueError as e:
        return f"Short-clip warning: {e}", "", ""
    except Exception as e:
        return f"Error: {e}", "", ""

    transcript = " ".join(w["word"] for w in words)
    feature_lines = [
        f"Speaking rate (wpm):                {features['wpm_overall']}",
        f"Pauses longer than 400 ms:          {features['pause_count_over_400ms']}",
        f"Pause-duration variance:            {features['pause_duration_variance']}",
        f"Speaking-rate variance (thirds):    {features['speaking_rate_variance_across_thirds']}",
        f"Words transcribed:                  {features['num_words']}",
        f"Clip length (s):                    {features['total_duration_seconds']}",
    ]
    return transcript, "\n".join(feature_lines), json.dumps(features, indent=2)


demo = gr.Interface(
    fn=analyze,
    inputs=gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Debate or speech clip (10 seconds to 4 minutes)",
    ),
    outputs=[
        gr.Textbox(label="Transcript (Whisper-small)", lines=6),
        gr.Textbox(label="Prosodic features", lines=8),
        gr.Code(label="Raw feature JSON", language="json"),
    ],
    title="Delivery Analyzer — Space 2",
    description=(
        "This is Prea's Space 2 — the thin-client delivery analyzer. "
        "Uploads audio to the Hugging Face Inference API for Whisper-small "
        "transcription with word-level timestamps, then computes four prosodic "
        "features in pure Python: words per minute, pause count above 400 ms, "
        "pause-duration variance, and speaking-rate variance across thirds of "
        "the clip. No local model weights are loaded in this Space, so it "
        "boots in seconds on free-tier CPU. See research-journal.md, Weeks "
        "7–8, for the architectural pivot that led to this design."
    ),
    allow_flagging="never",
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()

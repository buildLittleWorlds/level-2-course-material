"""
Space 3 — WSDC Speech Judge Assistant.

The full two-factor pipeline. Audio goes in; three things come out:

    1. Delivery score (derived from four prosodic features computed from
       Whisper-small word-level timestamps)
    2. Content score (from SmolLM2-1.7B-Instruct rubric evaluation of the
       transcript on three dimensions: claim clarity, evidence quality,
       rebuttal strength)
    3. Combined score (simple average of the two)

Architecture is the same thin-client-over-API pattern as Space 2 — no local
model weights, everything heavy happens on Hugging Face's Inference API
servers. See research-journal.md, Weeks 9-10, for the design notes and the
Spearman correlation analysis on 20 test clips.

Three tabs:
    - Score:     just the three numbers
    - Breakdown: prosodic features and the LLM's rubric output in detail
    - Coach:     longest-pause timestamps and a one-paragraph coaching note
"""

import json
import os
import statistics
from typing import Any

import gradio as gr
import requests

HF_TOKEN = os.environ.get("HF_TOKEN", "")
WHISPER_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
LLM_URL = (
    "https://api-inference.huggingface.co/models/HuggingFaceTB/SmolLM2-1.7B-Instruct"
)

PAUSE_THRESHOLD_SECONDS = 0.4
MIN_WORDS_FOR_RELIABLE_FEATURES = 20

RUBRIC_PROMPT = """You are an experienced WSDC (World Schools Debate) judge giving short, constructive feedback on a short speech transcript. Score the speech on each of three dimensions, from 1 (weak) to 5 (strong), and write one sentence of feedback for each dimension. At the end, write one short paragraph of overall coaching advice. Respond ONLY in strict JSON with these exact keys:

{
  "claim_clarity": {"score": <int 1-5>, "comment": "<one sentence>"},
  "evidence_quality": {"score": <int 1-5>, "comment": "<one sentence>"},
  "rebuttal_strength": {"score": <int 1-5>, "comment": "<one sentence>"},
  "coaching_note": "<one short paragraph, 2-3 sentences>"
}

TRANSCRIPT:
\"\"\"
{transcript}
\"\"\"
"""


def _auth_headers(content_type: str | None = None) -> dict[str, str]:
    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is not set. Add it as a Space secret "
            "(Settings -> Variables and secrets -> New secret)."
        )
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    if content_type:
        headers["Content-Type"] = content_type
    return headers


# ---------- Whisper ----------


def transcribe_with_word_timestamps(audio_path: str) -> dict[str, Any]:
    with open(audio_path, "rb") as f:
        data = f.read()
    response = requests.post(
        WHISPER_URL,
        headers=_auth_headers("audio/wav"),
        params={"return_timestamps": "word"},
        data=data,
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Whisper API error {response.status_code}: {response.text[:400]}"
        )
    return response.json()


def extract_words_with_times(api_response: dict[str, Any]) -> list[dict[str, Any]]:
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


# ---------- Prosodic features ----------


def compute_prosodic_features(words: list[dict[str, Any]]) -> dict[str, Any]:
    if len(words) < MIN_WORDS_FOR_RELIABLE_FEATURES:
        raise ValueError(
            f"Only {len(words)} words transcribed. "
            f"Need at least {MIN_WORDS_FOR_RELIABLE_FEATURES} for reliable features."
        )
    total_duration = words[-1]["end"] - words[0]["start"]
    if total_duration <= 0:
        raise ValueError("Clip has zero or negative duration.")

    wpm_overall = len(words) / (total_duration / 60.0)

    # Pauses and which word-index gaps they live in (so we can point at them later).
    pauses = []
    for i in range(len(words) - 1):
        gap = words[i + 1]["start"] - words[i]["end"]
        if gap > PAUSE_THRESHOLD_SECONDS:
            pauses.append(
                {
                    "gap_seconds": gap,
                    "after_word_index": i,
                    "after_word": words[i]["word"],
                    "start_time": words[i]["end"],
                    "end_time": words[i + 1]["start"],
                }
            )
    pause_durations = [p["gap_seconds"] for p in pauses]
    pause_variance = (
        statistics.pvariance(pause_durations) if len(pause_durations) >= 2 else 0.0
    )

    # Speaking-rate variance across thirds.
    n = len(words)
    third = n // 3
    rates = []
    if third >= 2:
        for section in (words[0:third], words[third : 2 * third], words[2 * third :]):
            dur = section[-1]["end"] - section[0]["start"]
            if dur > 0:
                rates.append(len(section) / (dur / 60.0))
    rate_variance = statistics.pvariance(rates) if len(rates) >= 2 else 0.0

    # Find the three longest pauses for the Coach tab.
    top_pauses = sorted(pauses, key=lambda p: -p["gap_seconds"])[:3]

    return {
        "wpm_overall": round(wpm_overall, 1),
        "pause_count_over_400ms": len(pauses),
        "pause_duration_variance": round(pause_variance, 3),
        "speaking_rate_variance_across_thirds": round(rate_variance, 1),
        "num_words": len(words),
        "total_duration_seconds": round(total_duration, 1),
        "top_pauses": top_pauses,
        "rates_by_third": [round(r, 1) for r in rates],
    }


def normalize_delivery_score(features: dict[str, Any]) -> float:
    """Map the four prosodic features onto a 0-100 delivery score.

    This is a simple hand-crafted normalization based on the reference
    ranges from Week 8 data. It is not learned, not validated, and should
    not be treated as ground truth. See research-journal.md, Week 10,
    for the honest limitations discussion.
    """
    wpm = features["wpm_overall"]
    # Speaking rate: reward 155-190 wpm, penalize extremes.
    if 155 <= wpm <= 190:
        rate_score = 1.0
    elif 140 <= wpm < 155 or 190 < wpm <= 210:
        rate_score = 0.7
    else:
        rate_score = 0.4

    # Pause count: reward 5-12 strategic pauses, penalize too few or far too many.
    pc = features["pause_count_over_400ms"]
    if 5 <= pc <= 12:
        pause_count_score = 1.0
    elif 3 <= pc < 5 or 12 < pc <= 18:
        pause_count_score = 0.7
    else:
        pause_count_score = 0.4

    # Pause variance: higher is better (signals strategic emphasis).
    pv = features["pause_duration_variance"]
    pause_var_score = min(1.0, pv / 0.35)

    # Rate variance across thirds: higher is better (signals dynamic pacing).
    rv = features["speaking_rate_variance_across_thirds"]
    rate_var_score = min(1.0, rv / 20.0)

    combined = 0.30 * rate_score + 0.25 * pause_count_score + 0.20 * pause_var_score + 0.25 * rate_var_score
    return round(combined * 100, 1)


# ---------- LLM content scoring ----------


def score_content_with_llm(transcript: str) -> dict[str, Any]:
    prompt = RUBRIC_PROMPT.replace("{transcript}", transcript)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 350,
            "temperature": 0.2,
            "return_full_text": False,
        },
    }
    response = requests.post(
        LLM_URL,
        headers=_auth_headers("application/json"),
        json=payload,
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(f"LLM API error {response.status_code}: {response.text[:400]}")
    data = response.json()
    raw = data[0].get("generated_text", "") if isinstance(data, list) else str(data)
    # Find the first JSON object in the response.
    try:
        start = raw.index("{")
        end = raw.rindex("}") + 1
        parsed = json.loads(raw[start:end])
    except (ValueError, json.JSONDecodeError):
        parsed = {
            "claim_clarity": {"score": 0, "comment": "LLM returned unparseable JSON."},
            "evidence_quality": {"score": 0, "comment": "LLM returned unparseable JSON."},
            "rebuttal_strength": {"score": 0, "comment": "LLM returned unparseable JSON."},
            "coaching_note": f"Raw LLM output: {raw[:500]}",
        }
    return parsed


def content_score_out_of_100(rubric: dict[str, Any]) -> float:
    keys = ("claim_clarity", "evidence_quality", "rebuttal_strength")
    scores = [int(rubric.get(k, {}).get("score", 0) or 0) for k in keys]
    if not any(scores):
        return 0.0
    mean_out_of_5 = sum(scores) / len(scores)
    return round((mean_out_of_5 / 5.0) * 100, 1)


# ---------- Gradio glue ----------


def format_seconds(s: float) -> str:
    minutes = int(s // 60)
    seconds = s - minutes * 60
    return f"{minutes}:{seconds:05.2f}"


def analyze(audio_path: str):
    if not audio_path:
        msg = "Please upload or record an audio clip."
        return msg, msg, msg, msg, msg, msg, msg

    try:
        api_response = transcribe_with_word_timestamps(audio_path)
        words = extract_words_with_times(api_response)
        if not words:
            raise RuntimeError("Whisper returned no word-level timestamps.")
        features = compute_prosodic_features(words)
        transcript = " ".join(w["word"] for w in words)
        rubric = score_content_with_llm(transcript)
    except ValueError as e:
        msg = f"Short-clip warning: {e}"
        return msg, msg, msg, msg, msg, msg, msg
    except Exception as e:
        msg = f"Error: {e}"
        return msg, msg, msg, msg, msg, msg, msg

    delivery_score = normalize_delivery_score(features)
    content_score = content_score_out_of_100(rubric)
    combined = round((delivery_score + content_score) / 2.0, 1)

    # ---- Score tab ----
    score_summary = (
        f"Delivery:  {delivery_score} / 100\n"
        f"Content:   {content_score} / 100\n"
        f"Combined:  {combined} / 100"
    )

    # ---- Breakdown tab ----
    prosodic_block = (
        f"Speaking rate (wpm):                {features['wpm_overall']}\n"
        f"Pauses longer than 400 ms:          {features['pause_count_over_400ms']}\n"
        f"Pause-duration variance:            {features['pause_duration_variance']}\n"
        f"Speaking-rate variance (thirds):    {features['speaking_rate_variance_across_thirds']}\n"
        f"Words transcribed:                  {features['num_words']}\n"
        f"Clip length (s):                    {features['total_duration_seconds']}"
    )
    rubric_lines = []
    for key, label in (
        ("claim_clarity", "Claim clarity"),
        ("evidence_quality", "Evidence quality"),
        ("rebuttal_strength", "Rebuttal strength"),
    ):
        entry = rubric.get(key, {})
        rubric_lines.append(
            f"{label}: {entry.get('score', 0)}/5 — {entry.get('comment', '')}"
        )
    rubric_block = "\n".join(rubric_lines)

    # ---- Coach tab ----
    top = features["top_pauses"]
    if top:
        pause_lines = [
            f"  {i+1}. {format_seconds(p['start_time'])}–{format_seconds(p['end_time'])} "
            f"({p['gap_seconds']:.2f}s) — after '{p['after_word']}'"
            for i, p in enumerate(top)
        ]
        pauses_text = "Three longest pauses — worth listening back to:\n" + "\n".join(pause_lines)
    else:
        pauses_text = "No pauses longer than 400 ms were detected."

    coaching_note = rubric.get("coaching_note", "")

    return (
        score_summary,
        prosodic_block,
        rubric_block,
        pauses_text,
        coaching_note,
        transcript,
        json.dumps({"features": {k: v for k, v in features.items() if k != "top_pauses"}, "rubric": rubric}, indent=2),
    )


with gr.Blocks(theme=gr.themes.Soft(), title="WSDC Speech Judge Assistant") as demo:
    gr.Markdown(
        "# WSDC Speech Judge Assistant — Space 3\n"
        "Upload a short debate or speech clip. This Space transcribes it with Whisper-small "
        "(via the Hugging Face Inference API), computes four prosodic delivery features from "
        "the word-level timestamps, and sends the transcript to SmolLM2-1.7B-Instruct with a "
        "WSDC-style rubric prompt for content scoring. Tested on 20 clips; see "
        "[research-journal.md Week 10](../research-journal.md) for the correlation analysis "
        "and limitations. — Prea Callahan, AI + Research Level 2, Spring 2026."
    )
    audio_in = gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Speech clip (10 seconds to 4 minutes)",
    )
    go = gr.Button("Score the speech", variant="primary")

    with gr.Tabs():
        with gr.TabItem("Score"):
            score_out = gr.Textbox(label="Summary", lines=4)
        with gr.TabItem("Breakdown"):
            prosodic_out = gr.Textbox(label="Prosodic features", lines=8)
            rubric_out = gr.Textbox(label="Content rubric (SmolLM2)", lines=6)
            transcript_out = gr.Textbox(label="Transcript (Whisper-small)", lines=6)
        with gr.TabItem("Coach"):
            pauses_out = gr.Textbox(label="Moments worth listening back to", lines=6)
            coaching_out = gr.Textbox(label="Coaching note", lines=4)
        with gr.TabItem("Raw JSON"):
            raw_out = gr.Code(label="All features and rubric output", language="json")

    go.click(
        analyze,
        inputs=audio_in,
        outputs=[
            score_out,
            prosodic_out,
            rubric_out,
            pauses_out,
            coaching_out,
            transcript_out,
            raw_out,
        ],
    )

if __name__ == "__main__":
    demo.launch()

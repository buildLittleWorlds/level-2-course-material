---
title: Debate Content Scorer (Baseline)
emoji: 📝
colorFrom: gray
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# Space 1 — Debate Content Scorer (Baseline)

*Part of Prea Callahan's AI + Research Level 2 portfolio. See the full [research journal](../research-journal.md) for context.*

**Live Space:** [https://huggingface.co/spaces/profplate/space1-content-scorer](https://huggingface.co/spaces/profplate/space1-content-scorer)

## What this Space is

This is the **intentionally bad baseline** for my research project on automated feedback for debate speeches. It uses **distilgpt2**, a small generic text-generation model, to "continue" the opening of a debate speech. My original plan in Week 5 was to use a text generator as a kind of content scorer — if the model's continuation matched what I would say next, I reasoned, the opening was probably strong. Within about twenty minutes of testing this on real WSDC openings I knew it was the wrong idea.

## Why it doesn't work (and why that matters)

Text generators are not evaluators. distilgpt2 will:

1. Fabricate evidence ("in 2023 alone, 47% of Canadian schools…").
2. Misquote statistics it invented one sentence earlier.
3. Drift off the motion entirely after a few dozen tokens.
4. Produce something that is grammatical and confident and completely unusable as debate feedback.

I kept this Space in my portfolio because it's the reason my project pivoted. If a text-only, generator-based approach had worked, I would not have gone hunting for a way to analyze audio, and I would not have run into the architectural pattern in the Mistral Voxtral blog post that ended up shaping Spaces 2 and 3.

## How to read this Space

Try the examples. Notice:

- At **temperature 0.3–0.5**, the model produces repetitive, cliché continuations.
- At **temperature 0.7–1.0**, it produces more interesting prose but invents citations.
- At **temperature 1.3+**, it produces things that are factually false but sometimes funny.

**Nowhere in the temperature range does it produce anything you could hand to a debater as useful feedback.** That is the point.

## What comes next

- **Space 2** ([Delivery Analyzer](https://huggingface.co/spaces/profplate/space2-delivery-analyzer)) — the pivot. Uses the Hugging Face Inference API to transcribe audio with Whisper-small, then computes prosodic features in pure Python.
- **Space 3** ([WSDC Speech Judge Assistant](https://huggingface.co/spaces/profplate/space3-speech-judge-assistant)) — the full two-factor WSDC Speech Judge Assistant, which combines prosody with LLM-based content scoring.

## Files

- `app.py` — Gradio interface wrapping the distilgpt2 pipeline.
- `requirements.txt` — Dependencies.

## Course

Built for AI + Research Level 2, Youth Horizons Learning, Spring 2026.

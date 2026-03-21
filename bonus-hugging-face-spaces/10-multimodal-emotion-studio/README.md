---
title: Multimodal Emotion Studio
emoji: ✦
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: "4.44.1"
app_file: app.py
pinned: false
license: mit
---

# ✦ Multimodal Emotion Studio

A showcase Hugging Face Space that chains **three** transformer models in a
visual pipeline, demonstrating what's possible when you push Gradio's UI
capabilities.

## Pipeline

```
Image ──► BLIP (caption) ──► DistilRoBERTa (7 emotions) ──► BART-MNLI (zero-shot)
                                     ▲
Text  ──────────────────────────────┘
```

## Models used

| Step | Model | Task |
|------|-------|------|
| 1 | `Salesforce/blip-image-captioning-base` | Image → caption |
| 2 | `j-hartmann/emotion-english-distilroberta-base` | Text → 7 Ekman emotions |
| 3 | `facebook/bart-large-mnli` | Text → custom zero-shot labels |

## Features beyond the basics

- **Dark glassmorphism theme** with gradient backgrounds and frosted-glass cards
- **Animated SVG radar chart** with per-emotion colored vertices
- **Live pipeline tracker** showing which model is running
- **Animated bar charts** with CSS keyframe transitions
- **Floating hero result** with pulsing glow effects
- **Responsive grid layout** that adapts to mobile
- **Custom zero-shot labels** — students can type any emotion vocabulary

## Deploy to Hugging Face Spaces

1. Create a new Space at [huggingface.co/new-space](https://huggingface.co/new-space)
2. Choose **Gradio** as the SDK
3. Upload `app.py`, `requirements.txt`, and this `README.md`
4. The Space will install dependencies and launch automatically

## Local development

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:7860 in your browser.

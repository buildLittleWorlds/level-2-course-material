---
title: Image Story Pipeline
emoji: 🔗
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Image Story Pipeline

Upload an image. Model 1 describes it. Model 2 analyzes the tone of that description. Two models, connected.

## The Models

| Step | Model | What it does |
|------|-------|-------------|
| 1 | `Salesforce/blip-image-captioning-base` | Looks at an image and writes a caption |
| 2 | `distilbert-base-uncased-finetuned-sst-2-english` | Reads the caption and judges its sentiment |

## Why it matters

Most real AI systems chain multiple models together. A self-driving car uses one model to detect objects and another to decide what to do. A content moderation system uses one model to transcribe audio and another to flag harmful content.

When models are chained, errors cascade. If the captioner misreads your image, the sentiment model gets garbage input — and produces garbage output. Understanding where a pipeline breaks is a core AI skill.

## Try it

Upload a photo and see what story the pipeline tells. Then try to break it — find an image where the caption is wrong and watch the sentiment analysis become meaningless.

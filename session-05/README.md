---
title: Text Playground
emoji: 🎛️
colorFrom: green
colorTo: purple
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Text Playground

Type a prompt and use sliders to control how the AI writes.

## The Controls

| Slider | What It Does | Low Value | High Value |
|--------|-------------|-----------|------------|
| Temperature | Controls randomness | Predictable, repetitive | Creative, chaotic |
| Top-p | Controls word diversity | Fewer word choices | More word choices |
| Max Length | Controls output length | Short responses | Longer responses |

## The Model

This Space uses `distilgpt2`, a small text generation model (~80MB). It's not as powerful as GPT-4 or Claude, but it's fast, free, and perfect for learning how generation controls work. The same sliders exist on every text generation model — including the big ones.

## Try It

Start with the same prompt and change one slider at a time. Watch how the output changes. Can you find the best settings for a scary story? A formal letter? A news report?

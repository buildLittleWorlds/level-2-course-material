---
title: Silly Phrase Finder with Cleaning
emoji: 🧹
colorFrom: green
colorTo: yellow
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Silly Phrase Finder (with Cleaning)

Same Silly Phrase Finder from Session 1, but now with a `clean_text()` function that preprocesses messy input before sending it to the model.

## What the cleaner does

1. Strips extra whitespace
2. Collapses repeated characters ("sooooo" → "soo")
3. Expands abbreviations (Dr., Rep., Mr., etc.)
4. Removes emoji
5. Normalizes ALL CAPS to Title Case

## Why this matters

Real-world text is messy. Models trained on clean data struggle with emoji, slang, ALL CAPS, and weird formatting. Cleaning the input before it reaches the model can improve results — but it can't fix everything. Sarcasm, cultural context, and meaning are beyond what a text cleaner can handle.

## Try it

Paste the messiest text you can find — tweets, texts, ALL CAPS rants — and see how the cleaning changes the model's output.

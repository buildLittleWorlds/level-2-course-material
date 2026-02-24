---
title: Silly Phrase Finder
emoji: 🤪
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Silly Phrase Finder

Paste any text and this AI picks out the silliest phrase.

## How it works

1. Your text gets split into sentences
2. A zero-shot classifier scores each sentence as "silly and ridiculous," "serious and important," or "ordinary and boring"
3. The sentence with the highest silliness score wins

## What's zero-shot classification?

The model (`valhalla/distilbart-mnli-12-3`) was never trained on the word "silly." It was trained to understand whether two sentences are related — and that general language understanding is enough for it to figure out what "silly" means on its own. No custom training needed.

## Try it

Paste a paragraph from a news article, a story, an email — anything with a few sentences. The model will find the goofiest one.

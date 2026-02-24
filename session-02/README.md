---
title: Emotion Detector
emoji: 🎭
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Emotion Detector

Paste any text and see what emotion the AI detects in each sentence.

## How it works

1. Your text gets split into sentences
2. An emotion classifier labels each sentence (anger, disgust, fear, joy, neutral, sadness, surprise)
3. You see the emotion and confidence score for every sentence

## The big idea: Training Data matters

This model (`j-hartmann/emotion-english-distilroberta-base`) was trained on tweets. It learned what emotions look like from how people write on Twitter. That means it's great at short, punchy text — but what happens when you give it a news article? A poem? A legal document?

Same text, different model, different answer. The training data shapes what the model "sees."

## Try it

Paste different kinds of text and see how the model reacts. Where does it get it right? Where does it struggle?

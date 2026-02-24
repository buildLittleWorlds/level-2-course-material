---
title: Bias Tester
emoji: ⚖️
colorFrom: purple
colorTo: orange
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Bias Tester

Type two sentences that are identical except for one detail — a name, a gender pronoun, a job title — and see if a sentiment model treats them the same.

## How it works

1. You enter two sentences that differ by one word or phrase
2. The same sentiment model (`distilbert-base-uncased-finetuned-sst-2-english`) scores both
3. The app compares the results and highlights any difference

## Why it matters

This model was trained on movie reviews (the SST-2 dataset). It learned patterns from real human text — including the biases embedded in that text. When the model treats "James" differently from "Jamila" in an otherwise identical sentence, that difference came from the training data, not from any intentional design choice.

## Try it

Swap names, swap pronouns, swap job titles. See what the model treats differently.

---
title: Sentiment Showdown
emoji: ⚔️
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
license: mit
---

# Sentiment Showdown

Three sentiment models read the same text. Do they agree?

## The Models

| Model | Trained On | Labels |
|-------|-----------|--------|
| `distilbert-base-uncased-finetuned-sst-2-english` | Movie reviews (SST-2) | POSITIVE / NEGATIVE |
| `cardiffnlp/twitter-roberta-base-sentiment-latest` | 124M tweets | negative / neutral / positive |
| `nlptown/bert-base-multilingual-uncased-sentiment` | Product reviews | 1 star – 5 stars |

## Why They Disagree

Each model was trained on different data from different domains. A sentence that sounds positive in a movie review might read as neutral on Twitter. The same words mean different things in different contexts — and models inherit those biases from their training data.

## Try It

Type any sentence and see how three different AI models interpret it. Try sarcasm, mixed feelings, or text from unusual domains to find where they disagree most.

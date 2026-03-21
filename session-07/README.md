# Session 7: Who Gets Hurt?

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-07/notebook.ipynb)

## What This Session Covers

Students build a Bias Tester Space that compares paired sentences — swapping names, gender, or roles while keeping everything else the same. They observe how sentiment scores change based on identity alone, discovering bias in AI systems through direct experimentation. The concept: Bias in AI. The Big Question: if the model treats people differently, where did it learn that?

## Narrative Role

This is the cost of scale. Session 6 revealed the breakthrough — train on everything, pretrain on the whole internet, then fine-tune — and this session reveals its price. When you train on the entire internet, you train on every bias, stereotype, and inequality in human history. The bigger the model, the bigger the bias problem. This session sits at the heart of Act II ("The Breakthrough"): every advance creates new problems.

## Connections

- **Builds on Session 6:** The breakthrough (pretraining on everything) directly causes the problem in this session (bias at scale). Session 6's bridge forward sets this up explicitly.
- **Bridges to Session 8:** Bias is one cost of scale; error cascades are another. When models chain together, bias from model one cascades into model two.
- **Bonus module:** The `bonus-bert-content-moderation` module (optional reading between Sessions 6 and 7) bridges from domain shift into bias, showing how BERT's power also meant absorbing every pattern in the training data.

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **app.py** — Bias Tester Space (Gradio app)
- **requirements.txt** — Space dependencies
- **notebook.ipynb** — Google Colab notebook for hands-on bias-testing experiments
- **GUIDE-fairness-audit.md** — research method card: Fairness Audit / Algorithmic Bias
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

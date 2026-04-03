# Session 6: Model Evaluation and Generalization
*"Same Space, Different Worlds"*

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-06/notebook.ipynb)

## Narrative Role

This is the pivot point of Act II. Students take the generative models they built in Session 5 — the text generator and the summarizer — and test them outside their training domains. Medical text, poetry, legal language, game dialogue: the same model produces different quality depending on the world of the input. Students hit the wall the field hit for years. Then they learn about the breakthrough: pretraining on everything. BERT (2018) showed that a single model trained on massive general text could handle any domain. That idea is behind ChatGPT, Claude, and every modern AI system. The session bridges to Session 7: training on everything solved the domain problem but created a new one — bias.

## What This Session Covers

Students build a domain-adapted text generator (same distilgpt2 model, different prompt templates for different domains) and test the Session 5 summarizer across domains — news, poetry, legal, medical, game narrative. They discover that models trained on one kind of text struggle with another, learning firsthand about overfitting and domain shift. Students also continue building and customizing their own Spaces.

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **domain-generator.py** — demo Space code (text generator with domain presets)
- **requirements.txt** — dependencies for the domain generator
- **notebook.ipynb** — Google Colab notebook for hands-on domain-testing experiments
- **GUIDE-external-validity.md** — research method guide for cross-domain testing
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

## Connections

- **Builds on:** Session 5's text generator and summarizer, plus the closing bridge ("What happens when you take a model outside the world it was trained in?")
- **Bridges to:** Session 7 ("Training on everything solved the domain problem. But it created a new one.")

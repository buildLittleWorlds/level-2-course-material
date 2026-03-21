# Session 6: Same Space, Different Worlds

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-06/notebook.ipynb)

## Narrative Role

This is the pivot point of Act II. Students take sentiment models out of their training domains and watch them fail — hitting the same wall the field hit for years. Then they learn about the breakthrough that solved it: pretraining on everything. BERT (2018) showed that a single model trained on massive general text could be fine-tuned for any specific task. That idea is behind ChatGPT, Claude, and every modern AI system. The session bridges forward to Session 7: training on everything solved the domain problem, but it created a new one — bias.

## What This Session Covers

Students take the Sentiment Showdown models from Session 4 and test them on different text domains — medical, legal, social media, poetry, product reviews, news, and more. They discover that models trained on one kind of text fail on another, learning firsthand about overfitting and domain shift. After experiencing the wall, they learn how the field broke through it. No new Space this session; students reuse the Session 4 Showdown Space.

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **notebook.ipynb** — Google Colab notebook for hands-on domain-testing experiments
- **GUIDE-external-validity.md** — research method guide for cross-domain testing
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

## Connections

- **Builds on:** Session 5's closing bridge ("What happens when you ask a model about something it's never seen?")
- **Bridges to:** Session 7 ("Training on everything solved the domain problem. But it created a new one.")
- **Supplementary:** `bonus-bert-content-moderation` — optional deeper dive on BERT and pretraining

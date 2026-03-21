# Session 3: What Models Can't Do

[![Open Notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/notebook.ipynb)
[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/explorer.ipynb)

## What This Session Covers

Students test adversarial inputs on a sentiment model, build a `clean_text()` preprocessing function, and then run three adversarial stories through four different emotion models (3-sentiment, 6-emotion, 7-Ekman, 28-GoEmotions) to discover three failure modes: tone deafness, emotional flattening, and anthropomorphic projection. The session closes Act I of the course by summing up "The Old Way" — three weeks of evidence that classification models sort text into buckets but don't understand what they're reading. The concept: Adversarial Testing and the Limits of Classification. The bridge forward: what if models could create, not just classify?

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **GUIDE-adversarial-testing.md** — research method card for adversarial testing, the noise vs. meaning distinction, three failure modes, and the CLEAR framework for prompting AI coding assistants
- **GUIDE-intro-to-markdown.md** — optional Markdown reference
- **app.py** — Sarcasm Breaker Space (Gradio app with `clean_text()`)
- **requirements.txt** — Space dependencies
- **notebook.ipynb** — Google Colab notebook: walks through the full Sessions 1–3 arc, demonstrates all three failure modes (tone deafness, emotional flattening, anthropomorphic projection), tests whether cleaning or more labels help, and frames "The Old Way" as real work that hits a wall
- **explorer.ipynb** — optional between-session notebook: test the three failure modes on a model from your own Collection and build a failure profile
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

## Story Arc Spaces (used in class demo)

The centerpiece demo uses four Story Arc Spaces from `bonus-hugging-face-spaces/`. Three adversarial stories are pasted into all four to demonstrate the three failure modes. See `bonus-hugging-face-spaces/ADVERSARIAL-STORIES.md` for the ready-to-paste stories and teaching notes.

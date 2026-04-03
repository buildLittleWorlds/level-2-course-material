# Session 3: Data Cleaning and Feature Engineering
*"What Models Can't Do"*

[![Open Notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/notebook.ipynb)
[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/explorer.ipynb)

## What This Session Covers

Students test sentiment and zero-shot classification models on real news headlines, discovering three failure modes: tone deafness (the model misreads measured language about disasters), emotional flattening (complex stories get forced into single labels), and anthropomorphic projection (the model reads emotion into market metaphors and weather). Students build a World Headlines Space live in class, learning the API-calling pattern, and experiment with a Zero-Shot News Analyzer that lets them define their own classification categories — proving that even custom labels hit the same wall. The session closes Act I of the course by summing up "The Old Way" — three weeks of evidence that classification models sort text into buckets but don't understand what they're reading. The concept: Adversarial Testing and the Limits of Classification. The bridge forward: what if models could create, not just classify?

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **GUIDE-adversarial-testing.md** — research method card for adversarial testing, the noise vs. meaning distinction, three failure modes, and the CLEAR framework for prompting AI coding assistants
- **GUIDE-intro-to-markdown.md** — optional Markdown reference
- **app.py** — World Headlines Space (Gradio app that calls GNews API)
- **requirements.txt** — Space dependencies
- **notebook.ipynb** — Google Colab notebook: tests sentiment and zero-shot models on pre-selected news headlines, demonstrates all three failure modes, experiments with custom categories, and frames "The Old Way" as real work that hits a wall
- **explorer.ipynb** — optional between-session notebook: test the three failure modes on a model from your own Collection and build a failure profile
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

## News Spaces (used in class demo)

The session uses three Spaces, all powered by the GNews API:

| Space | What It Does | Model |
|-------|-------------|-------|
| World Headlines | Fetches headlines from 10 countries (built live in class) | None — data display only |
| News Sentiment Analyzer | Labels each headline as good/bad news | distilbert-base-uncased-finetuned-sst-2-english |
| Zero-Shot News Analyzer | Classifies headlines with user-defined categories | facebook/bart-large-mnli |

All three use the same `GNEWS_API_KEY` secret. Free API keys are available at [gnews.io](https://gnews.io).

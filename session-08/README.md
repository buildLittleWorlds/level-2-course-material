# Session 8: Chain Two Models Together

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-08/notebook.ipynb)

## What This Session Covers

Students chain BLIP image captioning with sentiment analysis — upload an image, generate a caption, then analyze the caption's sentiment. They learn how multi-model systems work and discover error cascades: when the first model gets it wrong, everything downstream goes wrong too. The concept: Multi-Model Systems and Error Cascades. The Big Question: can you read emotion from a photograph?

## Narrative Role

The final piece of Act II. This is the culmination: students now know classification, generation, controls, domain shift, pretraining, bias, and pipelines — the full stack of ideas that make modern AI work. The session closes Act II by connecting pipelines to real products (ChatGPT's content filter, Siri's speech chain) and bridging forward to Act III, where students design for humans rather than studying models.

## Connections

**Builds on:** Session 7 (bias cascading through connected models — Session 7's bridge forward explicitly sets up tonight's error cascade demo)

**Bridges to:** Session 9 (from what's inside the machine to what's outside it — prompt engineering and human-AI interaction)

**Act II arc:** Session 4 (the fork) → Session 5 (controls) → Session 6 (domain shift / pretraining breakthrough) → Session 7 (bias as cost of scale) → **Session 8 (pipelines as how products actually work)**

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **app.py** — Image Story Pipeline Space (Gradio app)
- **requirements.txt** — Space dependencies
- **notebook.ipynb** — Google Colab notebook for hands-on model-chaining experiments
- **GUIDE-error-propagation.md** — research method card: Error Propagation / Systems Testing
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

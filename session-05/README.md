# Session 5: Model Training and Parameters
*"Add Controls"*

[![Open Notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-05/notebook.ipynb)
[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-05/explorer.ipynb)

## What This Session Covers

Session 4 built a text generator with no controls. Session 5 adds the controls — and builds a second generative Space. Students build a text generator with temperature, top-p, and max-length sliders, then discover a missing control (repetition penalty) that explains why their small model gets stuck in loops. They fix it live, then build a summarizer with length controls. Two kinds of generation (creating from scratch vs. condensing), both with hyperparameters. Students duplicate, customize, and deploy their own Spaces. The concept: Hyperparameters — controls on model behavior at runtime, including the ones you don't see. The narrative connection: these are the same controls behind ChatGPT, Claude, and every generative AI tool.

## Narrative Role

This is the second session in Act II (The Breakthrough). Session 4 introduced the classification-to-generation fork. Session 5 puts students' hands on the controls and gets them building. Session 6 will show what happens when a model leaves its training domain.

## Session Resources

- **slides.html** — presentation slides
- **INSTRUCTOR-GUIDE.md** — full lesson plan with time breakdown
- **app.py** — Text Playground Space (Gradio app with temperature/top-p/max-length sliders)
- **summarizer.py** — Quick Summarizer Space (Gradio app with max/min-length sliders)
- **requirements.txt** — Space dependencies
- **notebook.ipynb** — Google Colab notebook for hands-on hyperparameter experiments (optional)
- **explorer.ipynb** — extended Colab notebook for deeper exploration (optional)
- **GUIDE-parameter-sweep.md** — research method card: Parameter Sweep / Experimental Design
- **BETWEEN-SESSION.md** — challenge and homework for between sessions

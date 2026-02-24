# Roots: Iterative Space Building

A 12-week hands-on AI course for grades 7-11. Students learn machine learning concepts by building, breaking, and iterating on Hugging Face Spaces -- starting with a silly phrase finder and ending with a project they design themselves.

## How It Works

Each week follows the same rhythm:

1. **Live demo** -- the instructor builds on a shared Zoom screen while students suggest inputs and ideas
2. **Notebook time** -- students open the session notebook in Google Colab and experiment on their own
3. **Between sessions** -- optional challenges to extend what was built, plus progressive GitHub skills

No prior coding experience required. Students learn to read, modify, and remix Python code with the help of AI coding assistants (ChatGPT, Claude). The goal is understanding what AI can do, not memorizing syntax.

## Delivery

- **Live sessions**: Zoom (2 hours weekly, Monday evenings)
- **Course management**: Google Classroom (assignments, announcements, notebook links)
- **Student work**: Hugging Face Spaces (deployed AI apps) + GitHub repos (notebooks, portfolio)
- **Materials source**: This repository (instructor references, slides, notebooks)

Colab notebook links will be shared through Google Classroom each week. Students who miss a session can catch up using the notebook and between-session guide.

## Sessions

| #  | Session              | Concept                                  | Notebook |
|----|----------------------|------------------------------------------|----------|
| 01 | Your First Space     | INPUT --> MODEL --> OUTPUT                | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-01/notebook.ipynb) |
| 02 | Swap the Engine      | Training Data & Representation           | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-02/notebook.ipynb) |
| 03 | Break It on Purpose  | Data Cleaning & Feature Engineering      | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-03/notebook.ipynb) |
| 04 | Sentiment Showdown   | Model Evaluation                         | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-04/notebook.ipynb) |
| 05 | Text Playground      | Hyperparameters                          | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-05/notebook.ipynb) |
| 06 | Domain Safari        | Overfitting & Domain Shift               | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-06/notebook.ipynb) |
| 07 | Bias Tester          | Bias in AI                               | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-07/notebook.ipynb) |
| 08 | Image Pipeline       | Multi-Model Systems & Error Cascades     | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-08/notebook.ipynb) |
| 09 | Make It Useful       | Prompt Engineering & Human-AI Interaction | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-09/notebook.ipynb) |
| 10 | Build Your Own       | Supervised Learning & Task Design        | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-10/notebook.ipynb) |
| 11 | Iterate and Polish   | The Experimentation Loop                 | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-11/notebook.ipynb) |
| 12 | Demo Day             | Reflection & Portfolio                   | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-12/notebook.ipynb) |

Session 12's notebook is a reflection and portfolio worksheet rather than a coding exercise.

## Course Arcs

The 12 sessions follow four arcs:

**Exploration (Sessions 1-3)** -- Start with one model and learn the basics. Students build a Silly Phrase Finder Space, swap its model, then deliberately break it to understand how data flows through a pipeline.

**Evaluation (Sessions 4-6)** -- Compare models and understand differences. Students pit sentiment models against each other, experiment with hyperparameters, and discover what happens when a model meets text from outside its training domain.

**Advanced (Sessions 7-8)** -- Tackle harder questions. Students build a tool that tests AI models for bias, then chain multiple models together into an image-captioning pipeline to see how errors cascade.

**Project (Sessions 9-12)** -- Build and showcase something original. Students redesign a Space for a real audience, then build their own from scratch, iterate on it with peer feedback, and present at Demo Day.

## Progressive Skills

Beyond ML concepts, students build two practical skill tracks across the course:

**Colab notebooks**: Run cells (1) --> read output (2) --> edit code (3) --> install packages (4) --> use widgets (5) --> write markdown (6) --> compare outputs (7) --> upload images (8) --> create from scratch (10) --> debug (11)

**GitHub (web UI only)**: Create account (1) --> create repo (2) --> upload files (3-4) --> write README (6) --> fork a repo (9) --> push custom work (10) --> update files (11) --> curate portfolio (12)

## What You'll Need

- A [Hugging Face](https://huggingface.co/) account (free)
- A Google account for [Google Colab](https://colab.research.google.com/) (free)
- A [GitHub](https://github.com/) account (free)

All tools used in this course run on free tiers. No downloads or installations required.

## Session Materials

Each session folder contains:

- `app.py` / `requirements.txt` -- the Hugging Face Space code built during the live demo
- `slides.html` -- Reveal.js presentation for the session
- `INSTRUCTOR-GUIDE.md` -- timing, talking points, troubleshooting
- `BETWEEN-SESSION.md` -- optional challenges for students between sessions
- `notebook.ipynb` -- companion Colab notebook for hands-on experimentation
- `README.md` -- Hugging Face Space metadata

## Future Plans

- Push this repo to GitHub for Colab badge links to work
- Set up Google Classroom and link notebook URLs from assignments
- Explore whether students can submit notebook work through Classroom

## About This Course

Roots: Iterative Space Building is part of Youth Horizons, a program that teaches AI literacy to middle and high school students through guided discovery and hands-on projects. Students finish the course with a portfolio of working AI applications published to their own Hugging Face profiles and GitHub repos.

# AI + Research Level 2: Applied Machine Learning

**12 sessions | 2 hours each | grades 7–11**

A 12-session applied ML course for grades 7–11, built around **Hugging Face Spaces** and a **research-and-paper trajectory**. Students build, test, and iterate AI tools as Spaces; develop a real research question grounded in their own work; write a short research paper they can show in a college application or portfolio; and assemble a public-facing research presence on GitHub linked to their Hugging Face profile.

The course assumes no prior Python experience. Everything students need to do happens in a browser — at github.com, on huggingface.co, and in chat windows with AI assistants.

## Why GitHub + Hugging Face

In the AI world, a GitHub profile linked to a Hugging Face profile is the standard public face of someone doing research and applied work.

- **GitHub** is where the writing lives — the paper, the project READMEs, the journal, the explanations.
- **Hugging Face** is where the experiments live — Spaces, Collections, model comparisons.

Linking them turns a scatter of repos and Spaces into a coherent research identity. By the end of the course, every student has both, with their paper, their Spaces, and their Collection visible from one starting page.

Two worked examples students reference throughout the course:

- **Hugging Face profile:** [huggingface.co/profplate](https://huggingface.co/profplate) — what an active HF presence looks like (Spaces, Collections, model contributions).
- **GitHub research profile:** [github.com/buildLittleWorlds](https://github.com/buildLittleWorlds) — what a focused profile README looks like (research areas, current work, coding experiments, publications, "what I'm building now").

These are the patterns. Student profiles will look different in content but follow the same shape.

## What students produce

By the end of the 12 sessions, every student walks away with five linked artifacts:

1. **A Hugging Face Collection** — a curated set of models and Spaces in their domain of interest.
2. **A series of Spaces they built themselves** — a baseline Space (Sessions 1–3), a domain-specific Space (Sessions 4–6), and an ambitious Space (Sessions 7–10).
3. **A research journal** in their GitHub portfolio with weekly entries documenting what they tested, noticed, and changed.
4. **A research paper** (`PAPER.md`) grounded in their own Space work — anchored to a real test, written in their own voice, with honest limitations.
5. **A GitHub profile README** that links to all of the above and to their Hugging Face profile. The public front door for everything else.

## Course arc

The course is organized into four arcs:

- **Exploration (Sessions 1–3)** — Discover AI tools, learn the inference pipeline, investigate how training data and input quality shape model behavior.
- **Evaluation (Sessions 4–6)** — Distinguish classification from generation, control models through hyperparameters, test across domains, then pivot from building to investigating with a real research question.
- **Paper (Sessions 7–8)** — Draft a rough `PAPER.md` from journal evidence; adapt a per-student parallel-example packet (Anchor / Voice / Stretch) to make the paper genuinely the student's; absorb multi-model error cascades into the paper's limitations section; start a GitHub profile README.
- **Project (Sessions 9–12)** — Continue paper revision, read one source carefully enough to cite, redesign for real audiences, build the ambitious Space, iterate through peer feedback, present at Demo Day.

## Session map

| # | Session | Theme |
|---|---------|-------|
| 01 | From Rules to Models | Can a computer tell how you feel? Build your first Space, start a Collection. |
| 02 | Data Collection and Representation | Comparative analysis — three sentiment models, identical inputs, different worlds. |
| 03 | Data Cleaning and Feature Engineering | What models can't do. Adversarial testing. |
| 04 | Supervised Learning: Classification vs. Generation | The fork in the road. Build a generator. |
| 05 | Model Training and Parameters | Add controls. Sweep parameters and watch behavior change. |
| 06 | Finding Your Research Question | The pivot from building to investigating. |
| 07 | Bias, Variance, and Uncertainty — and the Paper Draft | Who gets hurt? Draft a rough `PAPER.md` from your journal. |
| 08 | Make the Paper Yours — Anchor, Voice, Stretch | Real Space, real test, your voice. Start your GitHub profile README. |
| 09 | Prompt Logic and Human-AI Interaction | Make it actually useful. Read one source carefully. |
| 10 | System Integration — Independent Build | Build your ambitious Space. |
| 11 | Iteration, Testing, and Refinement | Iterate, polish, prepare to present. |
| 12 | Methodological Reflection and Portfolio Presentation | Demo Day. |

Each `session-XX/` folder contains a `README.md`, a `BETWEEN-SESSION.md`, slides, and a `GUIDE-*.md` research method card. Sessions 6–10 also include a `WEEK-N-RESEARCH-WORK.md` student-facing guide. For the full concept-by-session breakdown, see [`CURRICULUM.md`](CURRICULUM.md).

## The paper-writing workflow

Starting in Session 7, the course shifts toward producing a research paper grounded in each student's Space work. The materials supporting this phase live at the root of the repository:

- **[`PAPER-TEMPLATE.md`](PAPER-TEMPLATE.md)** — the master AI prompt students paste into their assistant to generate a first draft from their journal and Space evidence.
- **[`GUIDE-FROM-SPACE-TO-PAPER.md`](GUIDE-FROM-SPACE-TO-PAPER.md)** — how the prompt-first paper workflow works, end to end.
- **[Bluest Hour exemplar](https://github.com/buildLittleWorlds/bluest-hour)** — the running worked example: a real project README, a real `research-journal.md`, and a real `PAPER.md`. Students see how a journal becomes a paper.

For Sessions 8–12, each enrolled student also receives a **parallel-example packet** — a five-file starter draft (`README.md`, `cover-note.md`, `sources.md`, `research-journal.md`, `PAPER.md`) built around their own research question. Students copy it into their own GitHub account via "Use this template," then adapt it through three moves named in their cover note: **Anchor** (swap in their real Space and one real test), **Voice** (rewrite the introduction and limitations in their own words), and **Stretch** (one specific extension named per student). The parallel-example packets are cohort-specific scaffolding, not part of these public materials.

## Colab notebooks as enrichment

Each session folder includes a `notebook.ipynb`. The notebooks are **enrichment for projects that benefit from a notebook walkthrough** — a student whose Space is a model-comparison tool, an embedding visualizer, or a fine-tuning experiment will get more out of running the notebook than a student whose Space is a writing tool or a UI iteration. The instructor pulls notebook material into class on a per-student, per-need basis. The default activity is building Spaces, writing in the GitHub portfolio, and iterating on the paper.

A handful of sessions (2–5) also include `explorer.ipynb` files that apply each week's research method (Comparative Analysis, Adversarial Testing, Baseline Comparison, Parameter Sweep) to models from a student's Collection — useful for students whose questions land naturally inside a notebook, optional for those whose work doesn't.

## Bonus content

- **[`bonus-hugging-face-spaces/`](bonus-hugging-face-spaces/)** — annotated build guides, cheat sheets, a leaderboard of example Spaces by topic (mood/emotion analyzers, story arcs, multimodal demos), and showcase pages. Useful when students need inspiration for what to build next.

## Repository structure

```
session-01/ ... session-12/   # 12 session folders (README + BETWEEN-SESSION + slides + supporting files)
PAPER-TEMPLATE.md              # master AI prompt for paper drafting
GUIDE-FROM-SPACE-TO-PAPER.md   # paper workflow guide
CURRICULUM.md                  # concept-by-session breakdown
bonus-hugging-face-spaces/     # build guides, cheat sheets, leaderboard, showcase
```


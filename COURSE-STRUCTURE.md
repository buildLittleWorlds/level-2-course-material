# Course Structure: AI + Research Level 2

This is the definitive reference for how the course is organized. It describes what every folder and file does, how the sessions are structured, and where to find things. If you're editing the course, start here.

---

## Top-Level Layout

```
level-2-course/
├── README.md                    # Course overview (public-facing, renders on GitHub)
├── COURSE-STRUCTURE.md          # This file
├── supplementary-datasets.md    # Curated HF datasets organized by session
├── start-here/                  # Onboarding guides for students (platforms & tools)
├── session-01/ through session-12/   # One folder per session
├── bonus-hugging-face-spaces/   # Extra Spaces for SpaceCraft leaderboard demos
├── _archive/                    # Historical planning docs and replaced files (not distributed)
```

Only two Markdown files live at the root: this structure guide and `supplementary-datasets.md`. Everything else is inside a folder.

---

## How a Session Folder Works

Every session folder follows the same pattern. The instructor guide is the source of truth; all other files must stay in sync with it.

### Core files (every session has these)

| File | Audience | Purpose |
|------|----------|---------|
| `INSTRUCTOR-GUIDE.md` | Instructor | Full 2-hour session plan: time breakdown, scripted talking points, demo inputs, discussion questions, troubleshooting tables. **Source of truth** for what happens in class. |
| `slides.html` | Instructor + Students | Reveal.js slide deck for live Zoom delivery. Served via GitHub Pages. Students can review after class. |
| `notebook.ipynb` | Students | Google Colab companion for the last ~20 minutes of class. Hands-on experiments tied to the session's concept. |
| `README.md` | Anyone browsing GitHub | Session title, Colab badge link, brief description of what the session covers, resource list. |

### Session-specific files (present in most but not all sessions)

| File | Which sessions | Purpose |
|------|---------------|---------|
| `BETWEEN-SESSION.md` | Sessions 1-11 | Homework: Hub Challenge (Option A/B), Research Journal entry prompt, Collection growth target. Session 12 has no between-session work. |
| `app.py` + `requirements.txt` | Sessions 1-5, 7-10 | The Hugging Face Space built live in class. Session 6 reuses Session 4's Space. Sessions 11-12 have no new Space. |
| `GUIDE-*.md` | Sessions 2-11 | Student-facing Markdown guides. Method cards for Sessions 2-9; build-planning guide for Session 10; presentation guide for Session 11. See "The Guide System" below. |
| `explorer.ipynb` | Sessions 2-5 | Optional between-session notebook for applying the week's research method to a student's own model. |
| `templates/` | Session 10 | Starter template files (text-classifier, text-generator, zero-shot, summarizer) for students building from scratch. |
| `peer-feedback-form.md` | Session 11 | Structured form for giving and receiving feedback during peer testing. |
| `portfolio-template.md` | Session 12 | Template for the final research portfolio that ties together Collection, journal, and Space. |
| `sentiment_models_comparison.ipynb` | Session 1 | Bonus notebook comparing six sentiment approaches. |

### Files that should NOT be in session folders

Old PDFs and SPACE-BUILDER.docx files have been moved to `_archive/`. The only PDFs still in a session folder are Session 1's two procedural guides (`Session-1-Create-Your-First-Collection.pdf` and `Session-1-Space-Explorers-Field-Guide.pdf`), which were already distributed to students and remain valid.

---

## The Guide System

Student-facing Markdown guides use the `GUIDE-` prefix and live inside their session folder. There are three types:

### 1. Method cards (Sessions 2-9)

One per session, following a standard structure. Students accumulate these as a portable reference deck.

| Session | File | Method | Key concept |
|---------|------|--------|-------------|
| 2 | `GUIDE-comparative-analysis.md` | Comparative Analysis | Testing same question with different tools |
| 3 | `GUIDE-adversarial-testing.md` | Adversarial Testing | Breaking models to find limits; noise vs. meaning; CLEAR framework |
| 4 | `GUIDE-baseline-comparison.md` | Baseline Comparison | Evaluating models against each other and against human judgment |
| 5 | `GUIDE-parameter-sweep.md` | Parameter Sweep / Experimental Design | Changing one variable while holding others constant |
| 6 | `GUIDE-external-validity.md` | External Validity / Generalization | Testing whether results hold outside the training domain |
| 7 | `GUIDE-fairness-audit.md` | Fairness Audit / Algorithmic Bias | Systematic paired testing for differential treatment |
| 8 | `GUIDE-error-propagation.md` | Error Propagation / Systems Testing | Tracing how errors cascade through multi-model pipelines |
| 9 | `GUIDE-user-centered-design.md` | User-Centered Design / Usability | Shifting from "does it work?" to "can someone use it?" |

Every method card has: What It Is, When Researchers Use It (3 examples from different fields), How to Apply It (3 steps), Key Vocabulary, This Week's Shared Example, Apply It to Your Own Topic, and (where datasets are curated) Explore the Training Data.

### 2. Companion guides (Session 2)

Session 2 has two additional guides beyond the method card:

| File | Purpose |
|------|---------|
| `GUIDE-grow-your-collection.md` | Procedural scaffold for building and maintaining a Hugging Face Collection as an evolving portfolio. Includes growth targets by session. |
| `GUIDE-research-journal.md` | Introduces the Research Journal: template, section-by-section explanation, annotated example entry, five-step tasting process, challenge prompts, vocabulary. |

### 3. Project guides (Sessions 10-11)

| File | Purpose |
|------|---------|
| `GUIDE-build-planning.md` (Session 10) | The three questions (What is my question? What model? Who is this for?), a copy-paste build blueprint template, tips for connecting Collection/journal/Space. |
| `GUIDE-research-presentation.md` (Session 11) | The 5-part presentation format (My Question, My Journey, My Artifact, What I Found, What's Next), preparation checklist, what makes a presentation good. |

### Style rules for all guides

- Voice: direct, second person, conversational. Students are grades 8-10.
- No emoji unless quoting model output.
- Templates in fenced code blocks for easy copy-paste.
- Cross-references by filename (e.g., "see `GUIDE-research-journal.md`").
- Footer: `AI + Research Level 2 • Session X: [Session Title]`
- Method cards are ~1 page; companion and project guides can be longer.

---

## Supplementary Datasets

`supplementary-datasets.md` at the course root is the curated list of browseable Hugging Face datasets organized by session. Method cards reference these in their "Explore the Training Data" sections. The quick reference:

| Session | Datasets | Teaching hook |
|---------|----------|---------------|
| 2 | sst2, sst5, dair-ai/emotion, go_emotions, nostalgic YouTube | "Here's what each model actually learned from." |
| 3 | tweet_eval (irony subset) | "Someone built a whole dataset just for sarcasm detection." |
| 4 | sst2, rotten_tomatoes, imdb | "Three movie review datasets — different sizes, lengths, sources." |
| 5 | sst5 | "What if sentiment were a number, not a label?" |
| 6 | financial_phrasebank, poem_sentiment, twitter-financial-news | "Same word, different world." |
| 7 | tweet_eval (hate/offensive subsets) | "How do you build a bias detection dataset?" |
| 9 | yelp_review_full, amazon_polarity | "This is the real data your tool would process." |

Sessions 8, 10, 11, and 12 do not have dataset recommendations yet. Add them to `supplementary-datasets.md` as the course develops, then add matching "Explore the Training Data" sections to the corresponding guides.

---

## The 12 Sessions at a Glance

### Exploration Arc (Sessions 1-3)

**Session 1: Can a Computer Tell How You Feel?** — Students explore Hugging Face Spaces that read mood from text, learn the INPUT-MODEL-OUTPUT pattern, and start their first Collection. Space: Mood Meter. Concept: the basic AI pipeline.

**Session 2: Not All Feelings Are the Same** — Students compare three sentiment models (binary, 7-emotion, 28-emotion) and discover that training data shapes what a model can "see." Space: Emotion Spectrum. Concept: Training Data and Representation. Research method: Comparative Analysis. Introduces the Research Journal and Collection-as-portfolio.

**Session 3: When Sarcasm Breaks Everything** — Students feed adversarial inputs to a sentiment model and learn to distinguish noise problems (fixable with code) from meaning problems (fundamental limitations). Space: Sarcasm Breaker. Concept: Data Cleaning and Feature Engineering. Research method: Adversarial Testing. Introduces the CLEAR framework for prompting AI coding assistants.

### Evaluation Arc (Sessions 4-6)

**Session 4: Sentiment Showdown** — Three sentiment models side by side on the same inputs. Students use their own judgment as a human baseline. Space: Sentiment Showdown. Concept: Model Evaluation. Research method: Baseline Comparison.

**Session 5: Text Playground** — Students build a Space with temperature, top-p, and max-length sliders. They learn what hyperparameters do by systematically sweeping one variable at a time. Space: Text Playground. Concept: Hyperparameters. Research method: Parameter Sweep / Experimental Design.

**Session 6: Domain Safari** — Students test the Session 4 models on text from six different domains (news, poetry, legal, medical, social media, code comments) and discover overfitting and domain shift. No new Space. Concept: Overfitting and Domain Shift. Research method: External Validity / Generalization.

### Advanced Arc (Sessions 7-8)

**Session 7: Who Gets Hurt?** — Students build a Bias Tester that compares paired sentences with name, gender, or role swaps. They observe how sentiment scores change based on identity alone. Space: Bias Tester. Concept: Bias in AI. Research method: Fairness Audit / Algorithmic Bias.

**Session 8: Chain Two Models Together** — Students chain BLIP image captioning with sentiment analysis. They learn about multi-model pipelines and discover error cascades when the first model gets it wrong. Space: Image Story Pipeline. Concept: Multi-Model Systems and Error Cascades. Research method: Error Propagation / Systems Testing.

### Project Arc (Sessions 9-12)

**Session 9: Make It Actually Useful** — Students redesign a sentiment demo into a tool for a real audience (restaurant owner, journal keeper, email writer). Same model, completely different experience. Space: Restaurant Review Analyzer. Concept: Prompt Engineering and Human-AI Interaction. Research method: User-Centered Design / Usability.

**Session 10: Build Your Own from Scratch** — Students choose a model, design a task, and build a complete Space independently. Space: student's own. Concept: Supervised Learning and Task Design. No new method card — the build plan IS the method.

**Session 11: Iterate and Polish** — Students improve their Session 10 projects through peer feedback and systematic testing. No new Space. Concept: The Experimentation Loop. Students prepare their 5-part research presentation for demo day.

**Session 12: Demo Day** — Students present their research journey: question, Collection, journal highlights, live Space demo, findings, and what's next. No new Space. Concept: Reflection and Portfolio.

---

## Recurring Structures Across Sessions

### Research Lens (Sessions 2-10)

A 5-minute segment near the end of each session where the instructor names the formal research method students just used. Each method gets a student-facing GUIDE card. By Session 10, students have accumulated 8 method cards.

### Big Questions (Sessions 4-9)

An opening discussion question that anchors the session's theme before any building or testing. Run while energy is high, left unresolved — the session's activities bring the question to life.

### SpaceCraft Check-In (Sessions 2-11)

The instructor briefly shows a Hugging Face Space (curated on the SpaceCraft leaderboard) and frames it through the session's research lens. Takes 3-5 minutes at the top of each session.

### Between-Session Homework (Sessions 1-11)

Three recurring components: a Hub Challenge (Option A stays with sentiment, Option B explores the student's own topic), a Research Journal entry applying the week's method, and Collection growth (adding models and Spaces with notes). Never prerequisite — students who miss a week can catch up.

### Collection Growth Targets

Students build a Hugging Face Collection as an evolving portfolio across the course:

| By Session | Target |
|------------|--------|
| 2 | 2 models + 2 Spaces |
| 5 | 6 models + 4 Spaces |
| 8 | 9 models + 5 Spaces |
| 11 | 12 models + 7 Spaces |

---

## Sync Rule

When editing any file in a session folder, check that all files in that folder still agree. The instructor guide is the source of truth. Specifically:

1. Do the slides reflect the same segments, vocabulary, and activities as the instructor guide?
2. Does the between-session homework match what the instructor guide and slides say?
3. Do the GUIDE files reference the same vocabulary, templates, and Collection targets?
4. If a method card exists, does it name the same method as the Research Lens segment?
5. Does the README list all current files (no references to deleted PDFs or SPACE-BUILDER.docx)?

---

## Supporting Folders

### `start-here/`

Onboarding guides for students setting up their tools: `course-overview.md`, `hugging-face.md`, `github.md`, `google-colab.md`, `gradio.md`.

### `bonus-hugging-face-spaces/`

Five extra Spaces used for SpaceCraft leaderboard demonstrations, plus build guides and cheat sheets. These are instructor resources for the SpaceCraft check-in segments.

### `_archive/`

Everything that was part of earlier course revisions and is no longer active:

| Subfolder | Contents |
|-----------|----------|
| `planning-docs/` | The revision planning documents: `enhancing-formal-research-framing.md`, `replacing-session-pdfs-with-markdown-guides.md`, `reviewing-non-revised-files.md`, `NEXT-SESSION-PROMPT.md`. These document the design decisions behind the current course but are not needed for teaching. |
| `classroom-setup/` | Google Classroom setup tracking: `GC-AUDIT.md`, `GOOGLE-CLASSROOM-STATUS.md`, `SESSION-STATUS.md`, `SLIDES-AND-LINKS-GUIDE.md`. These tracked the initial Classroom build and link migrations. |
| `reference-guides/` | Original per-session reference guide PDFs and their Markdown conversions. Replaced by `GUIDE-*.md` files in each session folder. |
| `space-builder-guides/` | Original per-session space-builder guide PDFs and their Markdown conversions. Replaced by instructor guides and in-class live builds. |
| `obsolete-session-files/` | Old PDFs and SPACE-BUILDER.docx files removed from session folders. |
| `extra/` | Miscellaneous early-stage materials (module plans, rubrics, QED Nano prototype). |

Nothing in `_archive/` is distributed to students or referenced by active course files. It exists for historical context if you need to understand why the course is structured the way it is.

---

## Delivery Infrastructure

- **GitHub repo:** `buildLittleWorlds/level-2-course-material` — this folder is the repo root.
- **GitHub Pages:** Enabled on `main` branch. Slides are served at `https://buildlittleworlds.github.io/level-2-course-material/session-XX/slides.html`.
- **Google Colab:** Notebooks open via `https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-XX/notebook.ipynb`.
- **Google Classroom:** AI + Research Level 2 Class 1, 2026 Spring Term. Each session has a Topic with Materials (notebook link, slides link) and an ungraded Assignment (between-session challenge).
- **Hugging Face:** Instructor Spaces deployed under `profplate/`. Students duplicate and build their own.
- **Zoom:** Saturday evenings 8-10 PM EST. Instructor screen-shares slides and live builds.

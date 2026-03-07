# Bonus Hugging Face Spaces — Change Log

**Date:** March 7, 2026
**Context:** The original 5 bonus Spaces had persistent runtime errors (3 of 5 failing). Factory rebuilds only worked temporarily. Root cause: memory pressure from loading large models at startup, especially the Sentiment Battle Arena (4 models simultaneously). Decision: delete all 5, rebuild from scratch with minimal memory footprint, learn Gradio 6 HTML features along the way.

---

## Summary of Changes

| What Happened | Old | New |
|---------------|-----|-----|
| Total Spaces | 5 | 5 |
| Spaces kept (rebuilt) | — | 3 (Emoji Mood, Headline Dashboard, Story Arc) |
| Spaces removed | 2 (Battle Arena, Review Star Guesser) | — |
| Spaces added | — | 2 (Image Color Mood, Audio Emotion Detector) |
| Max models per Space | 4 (Battle Arena) | 1 |
| Heaviest memory | ~3-4GB (Battle Arena) | ~1.5GB (any model-based Space) |
| Gradio version | ≥4.0 | ≥6.0 (new HTML features) |
| Ordering | Unordered | Simplest → most complex |

---

## What Was Removed and Why

### 1. Sentiment Battle Arena (01-sentiment-battle-arena) — REMOVED

**What it did:** Loaded 4 sentiment models simultaneously (VADER, DistilBERT binary, DistilRoBERTa 7-emotion, GoEmotions 28-class) and compared their outputs side-by-side on the same text.

**Why removed:** This was the primary source of runtime errors. Loading 4 transformer models at once consumed ~3-4GB of RAM, frequently exceeding free-tier HF Space limits. Factory rebuilds temporarily fixed it, but any concurrent usage or network hiccup during model downloads would crash the container. The architecture was fundamentally too heavy for free Spaces.

**Pedagogical impact:** This Space was referenced in:
- **Session 1 INSTRUCTOR-GUIDE.md** (lines 18-24): Listed in the "Space Tour" table during the 25-minute exploration phase
- **Session 2 INSTRUCTOR-GUIDE.md** (lines 10, 41): Used in the 0:15-0:35 demo to show models disagreeing on the same text
- **Session 1 slides.html**: May reference the Battle Arena by name
- **Session 2 slides.html**: May reference the Battle Arena in the comparison demo

**What replaces it pedagogically:** The concept of "different models give different results on the same input" is already taught in Session 4 (Sentiment Showdown), where students build a 3-model comparison Space themselves. For Sessions 1-2, the remaining Spaces (especially Emoji Mood Translator with 28 emotions vs. Headline Dashboard with 7 emotions) still demonstrate that different models see different things. The Audio Emotion Detector adds a new dimension: same concept (sentiment), different *modality* (voice vs. text).

### 2. Review Star Guesser (04-review-star-guesser) — REMOVED

**What it did:** An interactive game. Students read product reviews, guessed the star rating (1-5), then competed against a sentiment model's prediction. Tracked human vs. model scores.

**Why removed:** While pedagogically fun, it was the least connected to the other Spaces thematically and the game-state management added complexity without teaching core ML concepts. Replaced with the Audio Emotion Detector, which introduces a new modality (audio) and teaches students that sentiment analysis isn't limited to text.

**Pedagogical impact:** Referenced only in Session 1's Space Tour table. Not used in any other lesson.

---

## What Was Added

### 1. Image Color Mood Analyzer (new 01) — ADDED

**What it does:** Upload any image; the app extracts dominant colors using KMeans clustering and maps them to emotional associations via color psychology (warm reds = passionate, cool blues = calm, etc.).

**Why added:**
- **Zero ML model** — uses only PIL + scikit-learn. Memory ~150MB. Cannot crash from model loading.
- **Baseline test:** If this Space works, your HF environment is healthy. If it doesn't, the problem is your account setup, not your code.
- **New modality:** Introduces image input without the memory cost of a vision transformer.
- **Teaches:** That "sentiment analysis" doesn't require AI — algorithmic approaches can extract meaning too.

**Dependencies:** gradio, Pillow, scikit-learn, numpy (NO torch, NO transformers)

### 2. Audio Emotion Detector (new 03) — ADDED

**What it does:** Record your voice or upload an audio clip. A speech emotion recognition model detects whether the voice sounds happy, sad, angry, or neutral. Responds to vocal characteristics (pitch, energy, pace), not word content.

**Why added:**
- **New modality:** Students see that emotion detection works on audio, not just text. A flat "I'm happy" might register as neutral if said in a monotone voice.
- **Completes the modality set:** The 5 Spaces now cover text (Emoji Mood, Headlines, Story Arc), images (Color Mood), and audio (this one).
- **Low memory:** wav2vec2-base is only ~360MB.

**Model:** `superb/wav2vec2-base-superb-er` (base-sized, 4 emotions, IEMOCAP dataset)
**Dependencies:** gradio, transformers, torch, librosa

---

## What Was Kept (Rebuilt from Scratch)

All three kept Spaces are rebuilt with:
- Lazy model loading (load on first use, not startup)
- Gradio ≥6.0 (new `html_template`, `css_template`, `js_on_load` features)
- Clean, phased build guides

### 1. Emoji Mood Translator → now Space 02 (was 03)
- Same model: `SamLowe/roberta-base-go_emotions` (28 emotions)
- Same concept: text → emoji display
- **New:** Uses Gradio 6 `html_template` with Handlebars for data/presentation separation
- **New:** Lazy model loading

### 2. Headline Mood Dashboard → now Space 04 (was 05)
- Same model: `j-hartmann/emotion-english-distilroberta-base` (7 emotions)
- Same concept: paste headlines → aggregate mood + individual cards
- **New:** Uses `js_on_load` for click-to-expand cards and hover tooltips
- **New:** Lazy model loading

### 3. Story Emotion Arc → now Space 05 (was 02)
- Same model: `j-hartmann/emotion-english-distilroberta-base` (7 emotions)
- Same concept: paste paragraphs → emotion line chart
- **New:** Phase 4 replaces matplotlib with pure SVG (drops a dependency, adds interactivity)
- **New:** Legend-hover highlights individual emotion lines
- **New:** Lazy model loading

---

## New Ordering (Simplest → Most Complex)

| # | Space | Memory | # Models | Key Gradio 6 Feature |
|---|-------|--------|----------|---------------------|
| 01 | Image Color Mood Analyzer | ~150MB | 0 | `css_template` |
| 02 | Emoji Mood Translator | ~1.5GB | 1 | `html_template` + Handlebars |
| 03 | Audio Emotion Detector | ~1.5GB | 1 | CSS animations + `js_on_load` |
| 04 | Headline Mood Dashboard | ~1.5GB | 1 | Event delegation in `js_on_load` |
| 05 | Story Emotion Arc | ~1.5GB | 1 | SVG in templates, multi-target hover |

The build guides are in `build-guides/` and each has 4 phases, going from a 3-line hello-world to the full Gradio 6 app.

---

## Files Affected in Lessons

### Session 1 — Must Update

**INSTRUCTOR-GUIDE.md (lines 18-24):** The "Space Tour" table lists all 5 old Spaces with URLs. Needs to be replaced with the 5 new Spaces.

Old table:
| Space | URL |
|-------|-----|
| Sentiment Battle Arena | profplate/sentiment-battle-arena |
| Emoji Mood Translator | profplate/emoji-mood-translator |
| Review Star Guesser | profplate/review-star-guesser |
| Headline Mood Dashboard | profplate/headline-mood-dashboard |
| Story Emotion Arc | profplate/story-emotion-arc |

New table should be:
| Space | URL |
|-------|-----|
| Image Color Mood Analyzer | profplate/image-color-mood-analyzer |
| Emoji Mood Translator | profplate/emoji-mood-translator |
| Audio Emotion Detector | profplate/audio-emotion-detector |
| Headline Mood Dashboard | profplate/headline-mood-dashboard |
| Story Emotion Arc | profplate/story-emotion-arc |

> Note: The "What to try" column also needs updating. The Image Color Mood Analyzer doesn't use an ML model — this is actually a great teaching moment ("Not all AI analysis requires a neural network").

**slides.html:** Check for any references to "Battle Arena" or "Review Star Guesser" by name. Replace with new Space names. The slides may show screenshots or demo URLs.

**notebook.ipynb:** Check if any cells reference the old Space URLs or names.

### Session 2 — Must Update

**INSTRUCTOR-GUIDE.md (lines 10, 41):** The Sentiment Battle Arena is used in the 0:15-0:35 demo to show models disagreeing on the same text.

**Replacement approach:** Since the Battle Arena is gone, Session 2's "models disagree" demo can be done by:
1. Running the same text through the **Emoji Mood Translator** (28-class GoEmotions) and the **Headline Mood Dashboard** (7-class DistilRoBERTa) — they use different models with different emotion taxonomies, so they WILL produce different results
2. Or simply noting that Session 4's Sentiment Showdown is where students build this comparison themselves

**slides.html:** Check for Battle Arena references. Update accordingly.

### Session 3 — Check

**slides.html and INSTRUCTOR-GUIDE.md:** Probably no references to the bonus Spaces (Session 3 focuses on the Sarcasm Breaker), but worth scanning.

### Sessions 4-12 — Likely No Changes

The bonus Spaces are not referenced after Session 2. These sessions have students building their own Spaces.

---

## Build Guides Created

Located in `bonus-hugging-face-spaces/build-guides/`:

| File | Space |
|------|-------|
| `01-image-color-mood-analyzer.md` | New — image color extraction + mood mapping |
| `02-emoji-mood-translator.md` | Rebuilt — text → 28 emoji emotions |
| `03-audio-emotion-detector.md` | New — voice → 4 emotions |
| `04-headline-mood-dashboard.md` | Rebuilt — headlines → aggregate mood profile |
| `05-story-emotion-arc.md` | Rebuilt — paragraphs → emotion arc chart |

Each guide has 4 phases:
- Phase 1: Hello World (3-5 lines, proves the input type works)
- Phase 2: Add the core feature (model or algorithm, text output)
- Phase 3: HTML output (classic approach — Python returns HTML strings)
- Phase 4: Gradio 6 (html_template, css_template, js_on_load)

---

## HF Space URLs (Once Deployed)

Old URLs to delete:
- `https://huggingface.co/spaces/profplate/sentiment-battle-arena`
- `https://huggingface.co/spaces/profplate/review-star-guesser`

Old URLs that will be rebuilt in place:
- `https://huggingface.co/spaces/profplate/emoji-mood-translator`
- `https://huggingface.co/spaces/profplate/headline-mood-dashboard`
- `https://huggingface.co/spaces/profplate/story-emotion-arc`

New URLs to create:
- `https://huggingface.co/spaces/profplate/image-color-mood-analyzer`
- `https://huggingface.co/spaces/profplate/audio-emotion-detector`

---

## Cheat Sheets (Unchanged)

The `cheat-sheets/` folder contains Gradio 6 reference materials that remain valid:
- `01-GRADIO-HTML-QUICK-REFERENCE.md` — Core API reference
- `02-PATTERNS-AND-RECIPES.md` — Copy-paste patterns
- `03-GRADIO-6-VS-CLASSIC-COMPARISON.md` — Decision framework
- `more-gradio-docs-info.md` — Comprehensive Gradio 6 spec from Gemini

---

## March 7, 2026 (evening) — Replaced Space Folders + Added Colab Fallbacks

Replaced the 5 existing space folders with folders matching the build guides. The old folders (01-sentiment-battle-arena, 02-story-emotion-arc, 03-emoji-mood-translator, 04-review-star-guesser, 05-headline-mood-dashboard) were removed and replaced with:

| # | Folder | Contents |
|---|--------|----------|
| 01 | `01-image-color-mood-analyzer/` | `app.py`, `requirements.txt`, `colab_demo.ipynb` |
| 02 | `02-emoji-mood-translator/` | `app.py`, `requirements.txt`, `colab_demo.ipynb` |
| 03 | `03-audio-emotion-detector/` | `app.py`, `requirements.txt`, `colab_demo.ipynb` |
| 04 | `04-headline-mood-dashboard/` | `app.py`, `requirements.txt`, `colab_demo.ipynb` |
| 05 | `05-story-emotion-arc/` | `app.py`, `requirements.txt`, `colab_demo.ipynb` |

Each `app.py` uses the Phase 4 (final) version from the corresponding build guide. Each `colab_demo.ipynb` replicates the same functionality as a standalone Colab notebook, so the demos can be shown to students even if Hugging Face Spaces is slow or unavailable.

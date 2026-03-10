# Replacing Session PDFs with Markdown Student Guides

## Context

The original Level 2 course included two types of PDF support documents:

- **Reference Guides** (`reference-guides/Session-XX-Reference-Guide.pdf`) — one per session, covering concepts, vocabulary, and technical details
- **Space-Builder Guides** (`space-builder-guides/Space-Builder-Session-XX.pdf`) — step-by-step instructions for building each session's Hugging Face Space

These PDFs are **no longer in sync** with the revised course. The course underwent a major overhaul (documented in `enhancing-formal-research-framing.md`) that added:

- Research Lens segments naming formal research methods each session
- Between-session Research Journal entries with a weekly template
- Option A/B homework structure (stay with sentiment OR explore your own topic)
- SpaceCraft leaderboard as instructor-modeled curation
- Big Questions for sessions 4-9
- Collections as evolving portfolios (not one-time assignments)
- Individual inquiry threads branching from the shared sentiment example

Sessions 1 and 2 currently have student-facing PDFs in their session folders. Sessions 3-12 have none. Session 1's PDFs still work for the revised course (they're procedural and topic-agnostic). Session 2's PDFs conflict with the revised course in several ways and need to be replaced.

This document plans the replacement of Session 2's PDFs and establishes the framework for student support materials across all sessions going forward.

---

## The Shift from PDF to Markdown

### Why Markdown instead of PDF

The original student guides were created as styled PDFs. Going forward, all new student support materials will be created as **Markdown (.md) files** instead. The reasons are pedagogical and practical:

1. **LLM compatibility.** Students in this course are learning to work with AI tools. Markdown files are directly readable by LLMs — students can paste a guide into Claude or ChatGPT and ask questions about it, ask the AI to help them apply a framework, or use the guide as context for their research journal entries. PDFs require extraction and lose formatting. Teaching students to work with Markdown-native documents is itself a transferable skill.

2. **GitHub integration.** Students are maintaining a `my-ai-portfolio` GitHub repo. Markdown renders beautifully on GitHub with no extra tooling. Students can keep their guides in their repo alongside their notebooks and research journal. PDFs sit as opaque blobs in a repo.

3. **Maintainability.** The course sync rule (see `enhancing-formal-research-framing.md`) requires that all files in a session folder stay in sync. Markdown files can be diffed, edited, and version-controlled. PDFs cannot. When the course changes — and it will — Markdown guides can be updated in the same commit as the instructor guide and slides.

4. **Student editing.** Some guides include templates (tasting notes, journal entries, method application). In Markdown, students can copy the template directly into their own files. With PDFs, they have to retype everything.

5. **Progressive skill building.** Students are already writing Markdown in their research journals and GitHub READMEs. Using Markdown for course materials reinforces the format as a standard professional tool rather than a classroom novelty.

### What about Session 1's existing PDFs?

Session 1's two PDFs — `Session-1-Create-Your-First-Collection.pdf` and `Session-1-Space-Explorers-Field-Guide.pdf` — have already been distributed to students. They are procedural, topic-agnostic, and don't conflict with the revised course. **Leave them as-is.** If the course is taught again in a future cycle, they can be converted to Markdown at that time.

### Naming convention for new guides

All new student-facing Markdown guides live in their session folder and follow this pattern:

```
session-XX/GUIDE-short-descriptive-name.md
```

The `GUIDE-` prefix distinguishes student-facing support documents from other Markdown files in the folder (`INSTRUCTOR-GUIDE.md`, `BETWEEN-SESSION.md`, `README.md`). Examples:

- `session-02/GUIDE-grow-your-collection.md`
- `session-02/GUIDE-research-journal.md`
- `session-02/GUIDE-comparative-analysis.md`
- `session-03/GUIDE-adversarial-testing.md`
- `session-04/GUIDE-baseline-comparison.md`

### How to tell students about the format

**In class (Session 2):** "From now on, your course guides are Markdown files. You already know Markdown — it's what your research journal is written in. These guides live in the session folders on GitHub, and you can open them right there. You can also paste them into Claude or ChatGPT and ask questions. Try it — paste the Research Journal guide and ask the AI to help you brainstorm your first entry."

---

## Session 2: What Exists and What's Wrong With It

### Current PDFs

| PDF | What it does | What's wrong |
|---|---|---|
| `Session-2-Curate-a-Model-Collection.pdf` | Step-by-step Collection building focused on sentiment models | Assumes all students are building "My Sentiment Model Lineup." Doesn't acknowledge Option B (explore your own topic). Treats Collection as a one-time deliverable, not an evolving portfolio. No mention of Research Journal. |
| `Session-2-Model-Tasting-Notes.pdf` | Framework for comparing sentiment models, with template and example | All examples and prompts are sentiment-specific. The tasting process (read the label, start with obvious, test middle, push edges, compare) is excellent but locked into sentiment framing. No connection to Research Journal or research methods vocabulary. |

### What needs to be preserved from the old PDFs

The old PDFs contain genuinely good material that should be absorbed into the new guides, not discarded:

**From "Curate a Model Collection":**
- The Models vs. Spaces comparison table (what is it, URL pattern, why include it)
- Step-by-step instructions for finding models, using the Inference Widget, adding to Collection, writing notes
- The "Writing Notes for Models vs. Spaces" section (different focus areas for each)
- The starter models table (binary through 28-emotion)
- Submission checklist format

**From "Model Tasting Notes":**
- The five-step tasting process (read the label → start with obvious → test middle → push edges → compare side by side)
- The tasting notes template (model name, what it classifies, trained on, easy test, interesting test, strength, weakness, overall impression)
- The worked example (nlptown multilingual model)
- Challenge prompts (sarcasm, mixed feelings, understatement, cultural reference, question, very short, non-English)
- The "Model Spectrum" table (binary → ternary → 5-star → 7 emotions → 28 emotions)
- The "Key insight: More categories doesn't always mean better" callout
- Vocabulary table

### What's new that the old PDFs don't cover

- The Research Journal (introduced in Session 2's between-session homework)
- The Option A/B homework structure (sentiment OR your own topic)
- Collections as evolving portfolios with weekly growth targets
- Research methods vocabulary (comparative analysis, operationalization)
- The idea that students are developing their own line of inquiry, not just completing assignments

---

## Session 2: The Three New Markdown Guides

### Guide 1: `GUIDE-grow-your-collection.md`

**Replaces:** `Session-2-Curate-a-Model-Collection.pdf`

**Purpose:** Procedural scaffold for building and maintaining a Hugging Face Collection. Reduces cognitive load during the hands-on activity so the instructor can focus on concepts.

**Key changes from the old PDF:**
- Topic-agnostic framing (not locked to "My Sentiment Model Lineup")
- Collection as evolving portfolio, not one-time assignment
- Growth targets showing the trajectory across all sessions
- Notes guidance generalized beyond sentiment

**Outline:**

```
# Grow Your Collection
Your Hugging Face Collection is a portfolio that grows with you

## What Is a Collection?
- Brief reminder (they learned this in Session 1)
- Reframe: "Your Collection is your research portfolio. It documents what you've explored, what you've tested, and what you've learned. It grows every week."

## From Spaces to Models
- Absorb the Models vs. Spaces table from the old PDF
- "In Session 1, you collected Spaces. Now you're adding the engines that power them."

## Name Your Collection
- NOT "My Sentiment Model Lineup" for everyone
- "Name it after your focus area: 'Sentiment Model Lineup,' 'Translation Tools I've Tested,' 'Image Generators Compared,' 'Code Assistants Ranked' — whatever fits YOUR interest."
- "If you're still exploring and don't have a focus yet, that's fine. Name it something broad like 'My AI Explorations' and rename it later when your topic emerges."

## Step-by-Step: Add a Model
1. Go to huggingface.co/models
2. Search for models in your area of interest
3. Click a model and read the Model Card (brief explanation of what to look for)
4. Test it in the Inference Widget
5. Add to your Collection via three-dot menu
6. Write a note (see "Writing Good Notes" below)

## Step-by-Step: Add a Space
1. Go to huggingface.co/spaces
2. Search or browse for Spaces related to your topic
3. Test it — try the same inputs you used on the model
4. Add to your Collection
5. Write a note that mentions which model the Space uses

## Writing Good Notes
### For a model:
- What does it take in and produce?
- What was it trained on? (Check the model card)
- How did it handle your test inputs?
- Where does it struggle?
- How does it compare to other models you've tested?

### For a Space:
- Which model does this Space use?
- Does the design help you understand the output?
- Does it add anything beyond the raw model? (visualizations, comparisons, interactivity?)
- Would you recommend it to someone exploring your topic?

## Your Collection Grows Every Week
| By Session | Target |
|---|---|
| Session 2 | 2 models + 2 Spaces (minimum to start) |
| Session 3 | 4 models + 2 Spaces |
| Session 4 | 5 models + 3 Spaces |
| Session 5 | 6 models + 4 Spaces |
| Session 6 | 7 models + 4 Spaces |
| Session 7 | 8 models + 5 Spaces |
| Session 8 | 9 models + 5 Spaces |
| Session 9 | 10 models + 6 Spaces |
| Session 10 | 11 models + 6 Spaces |
| Session 11 | 12 models + 7 Spaces |

"By the end of the course, your Collection tells the story of your investigation. The early entries show you casting a wide net. The later entries show you going deep on something specific."

## Starter Models (for Sentiment — this session's shared example)
- Absorb the starter models table from the old PDF (binary through 28 emotions)
- Add: "These are the models we're using in class. For your own Collection, search the Hub for models related to YOUR topic."

## Checklist
- [ ] Collection has a clear name related to your focus area
- [ ] At least 2 models added
- [ ] At least 2 Spaces added
- [ ] Every item has a note explaining what you discovered
- [ ] Collection is set to Public
```

---

### Guide 2: `GUIDE-research-journal.md`

**Replaces:** `Session-2-Model-Tasting-Notes.pdf`

**Purpose:** Introduces the Research Journal as a weekly practice, provides the template with section-by-section explanation, gives an annotated example, and absorbs the best analytical frameworks from the old tasting notes PDF.

**Why this replaces Model Tasting Notes:** The tasting notes template was the course's first attempt at structured analytical writing. The Research Journal template is its evolution — it has the same DNA (observe, predict, test, reflect) but adds "What I Expected," "Limitations," and "What I Want to Try Next," which are the sections that build research thinking. The five-step tasting process from the old PDF becomes advice within this guide for *how* to generate observations for your journal entry.

**Outline:**

```
# Your Research Journal
How to document what you find, what you think, and where your curiosity leads

## What Is a Research Journal?
- "Scientists, designers, and engineers keep research journals — running records of what they tried, what happened, and what they think it means."
- "Your journal isn't a report you write after the fact. It's a thinking tool you use WHILE you're investigating."
- "You'll write one entry per week, 300-500 words. Over 10 weeks, that's a substantial record of your intellectual journey — and it becomes the backbone of your final presentation."

## The Template
(Reproduce the weekly template from BETWEEN-SESSION.md)

### Section-by-section: what each part is for

**This Week's Method**
"Name the research method from class. This grounds your entry in the course's shared vocabulary. Don't just say 'we compared stuff' — say 'comparative analysis' or 'adversarial testing.' Using the real term is part of learning it."

**How I Applied It**
"This is the most important section. Be specific: what model or Space did you test? What inputs did you use? What did you actually DO? Vague entries ('I tested some models') are useless to your future self. Specific entries ('I ran the same three Spanish sentences through Google Translate and DeepL') are gold."

This is where the tasting process helps. When you're stuck on what to do:
1. Read the label — check the model card before you test
2. Start with the obvious — give it an easy input first
3. Test the middle ground — try ambiguous or mixed inputs
4. Push the edges — try something designed to break it
5. Compare side by side — run the same input through multiple tools

**What I Expected**
"Write your prediction BEFORE you look at the results. This is hard. Scientists call it a 'pre-registration' — you commit to your hypothesis before seeing the data. It's okay to be wrong. In fact, the most interesting journal entries are the ones where your prediction was wrong and you had to figure out why."

**What I Found**
"Report what actually happened. Include specific outputs if you can — 'the model said POSITIVE with 94% confidence' is better than 'the model got it wrong.' If you're comparing models, a small table works well here."

**Why I Think This Happened**
"This is where you connect your observation to what you know about training data, model design, domain, and categories. Don't just describe — explain. 'I think this happened because the model was trained on product reviews, and my input was a poem' is the kind of reasoning that builds real understanding."

**Limitations**
"What COULDN'T you test? What might be different with other data, other models, another language, more time? This section is where you practice intellectual honesty — every investigation has boundaries. Naming yours shows sophistication, not weakness."

**What I Want to Try Next**
"Where is your curiosity pulling you? This section is the thread that connects one week's entry to the next. Over time, it's what turns a collection of isolated experiments into a line of inquiry."

## An Annotated Example: Week 2 Entry

(Provide a complete example entry — a student who chose Option B and explored translation models, applying comparative analysis. The example should be good-but-not-perfect: specific, honest about surprises, with a clear thread in "What I Want to Try Next." Annotate it with marginal notes explaining what makes each section work.)

### Example:

---

## Week 2 — Training Data and Representation

### This Week's Method
In class we learned about comparative analysis — testing the same question with different tools and seeing where they disagree. We compared three sentiment models that each define "feelings" differently because of their training data.

### How I Applied It
I'm interested in translation, so I found two translation models on the Hub: Helsinki-NLP/opus-mt-en-es (English to Spanish) and facebook/mbart-large-50-many-to-many-mmt (translates between 50 languages). I tested both with the same five English sentences, including a slang phrase ("that test was a piece of cake"), a sentence with sarcasm ("oh great, another group project"), and a simple factual sentence ("the store closes at 9pm").

### What I Expected
I thought the bigger model (mbart, 50 languages) would be better at everything since it knows more languages. I expected the idiom and sarcasm to be hard for both.

### What I Found
The Helsinki model actually produced more natural-sounding Spanish for simple sentences — my Spanish teacher confirmed this. But it translated "piece of cake" literally (pedazo de pastel) instead of using the Spanish idiom. The mbart model handled the factual sentence fine but produced awkward phrasing on the slang. Neither model caught the sarcasm — both translated "oh great" as though the speaker was genuinely happy.

### Why I Think This Happened
The Helsinki model was trained specifically on English-Spanish pairs, so it's a specialist. The mbart model is a generalist — 50 languages means less depth in any one pair. This is like what we saw in class: the binary sentiment model (specialist) vs. the 28-emotion model (generalist). More categories (or more languages) doesn't always mean better at any single task.

### Limitations
I only tested five sentences, and I only checked Spanish. The mbart model might be much better for languages the Helsinki model doesn't even support. Also, I'm not fluent in Spanish — I asked my teacher to check, but a native speaker might judge differently.

### What I Want to Try Next
I want to find out if there's a translation model specifically trained on informal/slang text. Also, I want to try the same comparison with Japanese, since that's a very different language structure from Spanish.

---

(Annotations alongside each section pointing out: specific model names and URLs, honest about a prediction that was wrong, connected the finding back to the class concept, limitations are real not performative, "What I Want to Try Next" sets up a clear thread for next week.)

## How Your Journal Evolves

"Your early entries will be all over the place — and that's exactly right."

| Weeks | What your journal looks like | What's happening |
|---|---|---|
| 1-3 | Different topic each week, broad exploration, scattered interests | You're casting a wide net. This is the browsing phase. |
| 4-6 | A topic starts recurring, entries reference earlier ones, "What I Want to Try Next" keeps pulling you back to something | Your thread is emerging. Lean into it. |
| 7-9 | Entries build on each other, you're going deeper on one area, limitations from earlier weeks become this week's experiments | You're doing sustained investigation. This is research. |
| 10+ | Your journal IS the rationale for what you build from scratch | "I've been investigating X for 9 weeks. Here's what I've learned. Here's what I'm building." |

"If you're in Week 2 and you don't have a topic yet — perfect. You're not behind. The journal's job right now is to help you figure out what you're interested in."

## The Five-Step Tasting Process (Your Testing Toolkit)

(Absorb the full five-step process from the old Model Tasting Notes PDF, but generalized beyond sentiment)

"Whenever you're testing a model or Space for your journal, this process gives you a systematic approach:"

1. **Read the label** — Check the model card. What was it trained on? What is it designed to do? A model trained on tweets will behave differently from one trained on legal documents.
2. **Start with the obvious** — Give it an easy input where you know the right answer. Does it get the basics right?
3. **Test the middle ground** — Try ambiguous, mixed, or borderline inputs. This is where models start to diverge.
4. **Push the edges** — Try inputs designed to be hard: sarcasm, very short text, other languages, domain mismatches, contradictions. Edge cases reveal real capabilities.
5. **Compare side by side** — Run the exact same input through multiple models. The differences teach more than any single result.

## Challenge Prompts for Sentiment Models (This Session)

(Absorb the challenge prompts from the old PDF — sarcasm, mixed feelings, understatement, cultural reference, question, very short, non-English)

"These are designed for the sentiment models we used in class. For your own topic, invent your own challenge prompts using the same logic: what's an easy input? A hard one? An unfair one?"

## Vocabulary

(Absorb the vocabulary table from the old PDF: Model Card, Training Data, Fine-tuning, Multi-label, Confidence Score, Edge Case, Inference)

Add: Comparative Analysis, Operationalization, Research Journal
```

---

### Guide 3: `GUIDE-comparative-analysis.md`

**New document — first in a series of research method cards**

**Purpose:** One-page reference for the research method introduced in Session 2's Research Lens. Students hear the term "comparative analysis" for five minutes in class and then are expected to apply it independently in their homework. This card gives them a portable, reusable reference.

**Design principle for all method cards:** Same structure every time. Students learn to expect the format. By Session 5 they have four cards and can flip through them. By Session 10 they have nine.

**Standard method card structure (used for all sessions):**

```
# [Method Name]
Session [X] Research Method

## What It Is
(2-3 sentence plain-language definition)

## When Researchers Use It
(2-3 real-world examples from different fields — not all from AI/ML, at least one from humanities or social science to connect to these students' backgrounds)

## How to Apply It
(3-step process, concrete and actionable)

## Key Vocabulary
(1-3 terms introduced with this method)

## This Week's Shared Example
(How we applied it in class to sentiment analysis — brief, 2-3 sentences)

## Apply It to Your Own Topic
(Prompts to help students transfer the method to whatever they're exploring)

## Explore the Training Data
(2-3 browseable HF datasets relevant to this session's method or models. No code required — students open the dataset viewer directly. One-sentence framing line, then a bulleted list of datasets with URLs and one-line descriptions. See `supplementary-datasets.md` for the curated dataset list organized by session.)
```

**Session 2 content:**

```
# Comparative Analysis
Session 2 Research Method

## What It Is
Comparative analysis means testing the same question with different tools and observing where they agree, where they disagree, and why. The goal isn't to find the "best" tool — it's to understand what each tool can and can't see.

## When Researchers Use It
- A linguist compares how Google Translate, DeepL, and a human translator render the same poem — not to pick a winner, but to understand what each approach prioritizes (literal accuracy vs. emotional tone vs. cultural context).
- A doctor compares three different diagnostic tests for the same condition to understand when each one gives false positives or misses cases entirely.
- A film critic watches the same story told as a Hollywood blockbuster, an indie film, and an anime series — same plot, different lenses, different things made visible.

## How to Apply It
1. **Pick your question.** What are you trying to understand? ("How well can AI detect sarcasm?" "Which translation model handles slang better?" "Do image classifiers see the same thing in this photo?")
2. **Pick your tools.** Find at least two models or Spaces that address your question but differ in some way — different training data, different architectures, different output categories.
3. **Hold the input constant.** Run the EXACT same inputs through each tool. The comparison only works if the input is identical. Record what each tool says.

## Key Vocabulary
- **Comparative analysis** — Testing the same question with different tools and observing divergence
- **Operationalization** — The specific way you define and measure a concept. "Emotion" operationalized as 2 categories (positive/negative) vs. 7 categories vs. 28 categories produces different results — not because the text changed, but because the definition changed.

## This Week's Shared Example
In class, we compared three sentiment models on the same text: a binary model (positive/negative), a 7-emotion model, and a 28-emotion model. Same input, three different lenses. The disagreements showed us that "how does this text feel?" depends entirely on how you define "feeling."

## Apply It to Your Own Topic
- What two models or Spaces in your Collection do similar things?
- What input would let you test them fairly against each other?
- If they disagree, can you figure out WHY by reading their model cards?
- What does the disagreement teach you about the models — or about the task itself?
```

---

## The Full Series: Research Method Cards for Sessions 3-10

Each session introduces one research method in the Research Lens segment. Each gets a method card following the same structure. Here is the planned content for each:

| Session | Method Card Filename | Method | Key Concept |
|---|---|---|---|
| 2 | `GUIDE-comparative-analysis.md` | Comparative Analysis | Testing same question with different tools |
| 3 | `GUIDE-adversarial-testing.md` | Adversarial Testing | Deliberately breaking models to find limits; noise vs. meaning |
| 4 | `GUIDE-baseline-comparison.md` | Baseline Comparison | Evaluating models against each other and against human judgment |
| 5 | `GUIDE-parameter-sweep.md` | Parameter Sweep / Experimental Design | Changing one variable while holding others constant |
| 6 | `GUIDE-external-validity.md` | External Validity / Generalization | Testing whether results hold outside the training domain |
| 7 | `GUIDE-fairness-audit.md` | Fairness Audit / Algorithmic Bias | Systematic paired testing for differential treatment |
| 8 | `GUIDE-error-propagation.md` | Error Propagation / Systems Testing | Tracing how errors cascade through multi-model pipelines |
| 9 | `GUIDE-user-centered-design.md` | User-Centered Design / Usability | Shifting from "does it work?" to "can someone use it?" |
| 10 | No new method card | End-to-End System Design | Students articulate their own method — the card IS their build plan |

### Additional notes for specific method cards:

**Session 3 — Adversarial Testing:** Should include the noise vs. meaning distinction (what's fixable with code vs. what's a fundamental limitation). Should also include the CLEAR framework for prompting AI coding assistants, since that's introduced in Session 3 and students use it from then on. This card may be 2 pages instead of 1.

**Session 4 — Baseline Comparison:** Should introduce evaluation concepts at a conceptual level: accuracy is misleading without context (the spam detector thought experiment), false positives vs. false negatives matter differently for different tasks, high confidence ≠ correctness. Not mathematical — just the reasoning.

**Session 7 — Fairness Audit:** Should include the paired-sentence testing technique (change one variable — a name, a gender, a dialect — and see if the model's output changes). Sensitive topic; the card should be matter-of-fact about why this matters.

### Supplementary datasets in method cards

Every method card includes an "Explore the Training Data" section at the end — a standalone block with 2-4 browseable Hugging Face datasets relevant to that session. The section is positioned after "Apply It to Your Own Topic" and before the footer. Students open the dataset viewer directly on HF; no code is required.

The curated dataset list is maintained in `supplementary-datasets.md` at the course root. When building a new method card, consult that file's "Quick Reference: Datasets by Session" table for which datasets to include. The mapping:

| Session | Datasets for "Explore the Training Data" section | Teaching hook |
|---|---|---|
| 2 | sst2, sst5, dair-ai/emotion, nostalgic YouTube (in comparative analysis card); sst2, dair-ai/emotion, go_emotions (in research journal guide) | "Here's what each model actually learned from." |
| 3 | tweet_eval (irony subset), sst2 | "Someone built a whole dataset just for sarcasm — and it's still hard." |
| 4 | sst2, tweet_eval (sentiment subset), rotten_tomatoes, imdb | "Three datasets, same task, completely different data." |
| 5 | sst5 | "SST has a 5-point scale. What if sentiment were a number, not a label?" |
| 6 | financial_phrasebank, poem_sentiment, twitter-financial-news | "Same word, different world. 'Positive' means profit here and beauty there." |
| 7 | tweet_eval (hate/offensive subsets) | "How do you build a bias detection dataset? Someone had to label these." |
| 9 | yelp_review_full, amazon_polarity | "This is the real data your tool would process." |

Sessions 8, 10, 11, and 12 do not have dataset recommendations yet. Add them to `supplementary-datasets.md` as the course develops.

---

## Session 2: Changes to Existing Files

### Files to remove

| File | Action |
|---|---|
| `session-02/Session-2-Curate-a-Model-Collection.pdf` | Delete. Replaced by `GUIDE-grow-your-collection.md`. |
| `session-02/Session-2-Model-Tasting-Notes.pdf` | Delete. Replaced by `GUIDE-research-journal.md`. |

### Files to create

| File | Action |
|---|---|
| `session-02/GUIDE-grow-your-collection.md` | Create. Procedural guide for building Collections. |
| `session-02/GUIDE-research-journal.md` | Create. Research Journal companion guide with template, example, and tasting process. |
| `session-02/GUIDE-comparative-analysis.md` | Create. First research method card. |

### Files to update

| File | What changes | Details |
|---|---|---|
| `session-02/INSTRUCTOR-GUIDE.md` | Update PDF references | Line ~207: change "Refer students to the PDFs" to reference the three new Markdown guides by name. Line ~250-254: update "Session Resources (PDFs)" section to "Session Resources" listing the three Markdown guides. Add a brief note about the Markdown format for instructor awareness. |
| `session-02/slides.html` | Update any slides referencing PDFs | Check for any slide that mentions "handout," "PDF," or the old document names. Update to reference Markdown guides. Consider adding a brief slide about the Markdown format if the instructor guide mentions explaining it to students. |
| `session-02/BETWEEN-SESSION.md` | Minor update | The current between-session homework doesn't reference the old PDFs by name, but check for any implicit references. Add a note in Part 1 pointing students to `GUIDE-grow-your-collection.md` for step-by-step instructions. Add a note in Part 2 pointing students to `GUIDE-research-journal.md` for guidance on writing their entry. |
| `session-02/README.md` | Update resources list | Replace PDF filenames with Markdown guide filenames. |

---

## Session Folder Sync Rule: Extension for Guides

The sync rule in `enhancing-formal-research-framing.md` should be extended to include student guides:

### Updated files per session folder

| File | What it is | Sync concern |
|---|---|---|
| `app.py` + `requirements.txt` | The HF Space build | Only changes if the build changes |
| `INSTRUCTOR-GUIDE.md` | Detailed instructor script with timing, talking points, activities | **Source of truth** for session content and flow |
| `slides.html` | Reveal.js slide deck shown on Zoom screen share | Must reflect the same segments, vocabulary, activities, and between-session homework as the instructor guide |
| `BETWEEN-SESSION.md` | Homework / between-session challenge | Must match what the instructor guide and slides say about homework |
| `GUIDE-*.md` | Student-facing support documents | Must be consistent with instructor guide content; vocabulary must match; any templates must match what the between-session homework references |
| `notebook.ipynb` | Colab companion notebook for last ~20 min | Only changes if the hands-on activity changes |
| `README.md` | Session summary | Update if session title, concept name, or key vocabulary changes |

### Additional sync check

After editing any file in a session folder, also verify:
5. Do the GUIDE files reference the same vocabulary, templates, and Collection targets as the instructor guide and between-session homework?
6. If a method card exists for this session, does it name the same method as the Research Lens segment in the instructor guide?

---

## Implementation Priority

### Phase 1: Session 2 (before teaching Session 2)

1. Create `session-02/GUIDE-grow-your-collection.md`
2. Create `session-02/GUIDE-research-journal.md`
3. Create `session-02/GUIDE-comparative-analysis.md`
4. Update `session-02/INSTRUCTOR-GUIDE.md` (references to guides)
5. Update `session-02/slides.html` (references to guides)
6. Update `session-02/BETWEEN-SESSION.md` (references to guides)
7. Update `session-02/README.md`
8. Delete old PDFs from session-02 folder

### Phase 2: Session 3 (before teaching Session 3)

1. Create `session-03/GUIDE-adversarial-testing.md` (method card + CLEAR framework + noise vs. meaning)
2. Update `session-03/INSTRUCTOR-GUIDE.md` if it references any PDFs
3. Update `session-03/slides.html` if needed
4. Update `session-03/BETWEEN-SESSION.md` to reference the new guide

### Phase 3: Session 4 (before teaching Session 4)

1. Create `session-04/GUIDE-baseline-comparison.md` (method card + evaluation concepts)
2. Remove `session-04/SPACE-BUILDER.docx` (old format, out of sync)
3. Update session-04 files as needed

### Phase 4: Sessions 5-9 (can be done week by week)

1. Create one method card per session following the standard structure
2. Update session files as needed

### Phase 5: Sessions 10-12 (when approaching those sessions)

- Session 10: Consider a `GUIDE-build-planning.md` (how to turn your research thread into a buildable artifact)
- Session 11: Consider a `GUIDE-research-presentation.md` (the 5-part format: My question → My journey → My artifact → What I found → What's next)
- Session 12: No new guide needed — the `portfolio-template.md` already exists

---

## What About the Original Reference Guides and Space-Builder Guides?

The `reference-guides/` and `space-builder-guides/` folders at the course root contain the original PDF guides and their Markdown conversions. These are **archival** — they document what the course originally planned. They should not be deleted (they're useful reference for understanding the original design intent), but they should not be distributed to students. The new `GUIDE-*.md` files in each session folder are the replacements.

If a future revision needs to consult what the original course covered for a specific session, the Markdown conversions in these folders are the place to look.

---

## Content Mapping: What Went Where

This table maps content from the old Session 2 PDFs to its new home, ensuring nothing valuable is lost:

| Old PDF Content | New Home | Notes |
|---|---|---|
| Models vs. Spaces comparison table | `GUIDE-grow-your-collection.md` | Preserved as-is |
| Step-by-step Collection instructions | `GUIDE-grow-your-collection.md` | Updated for topic-agnostic framing |
| "Writing Notes for Models vs. Spaces" | `GUIDE-grow-your-collection.md` | Generalized beyond sentiment |
| Starter models table | `GUIDE-grow-your-collection.md` | Kept as "this session's shared example," not the only option |
| Submission checklist | `GUIDE-grow-your-collection.md` | Updated to include growth targets |
| Five-step tasting process | `GUIDE-research-journal.md` | Repositioned as a testing toolkit within the journal workflow |
| Tasting notes template | `GUIDE-research-journal.md` | Evolved into the Research Journal template (same DNA, more sections) |
| Worked example (multilingual model) | `GUIDE-research-journal.md` | Replaced with a full annotated journal entry example |
| Model Spectrum table | `GUIDE-research-journal.md` | Kept as context for "this session's sentiment example" |
| "More categories ≠ better" callout | `GUIDE-research-journal.md` | Preserved |
| Challenge prompts | `GUIDE-research-journal.md` | Preserved with note to invent your own for your topic |
| Vocabulary tables | `GUIDE-research-journal.md` | Combined and extended with research vocabulary |
| Comparative analysis (implicit) | `GUIDE-comparative-analysis.md` | Made explicit with its own dedicated method card |
| Bonus challenge (find a model not in class) | `GUIDE-grow-your-collection.md` | Absorbed into the Collection growth framing — now it's the default, not a bonus |

---

## Style Notes for Writing the Guides

These notes ensure consistency across all student-facing Markdown guides:

1. **Voice:** Direct, second person ("you"), conversational but not dumbed down. Match the tone of the existing Session 1 PDFs — the "Space Explorer's Field Guide" is the benchmark. Students are 8th-10th graders.

2. **Length:** The Collection guide and Research Journal guide can be 3-4 pages equivalent. Method cards should be 1 page equivalent (1.5 max for Session 3 which has extra content).

3. **Structure:** Use headers, but not excessively. Short paragraphs. Tables where they clarify. Callout blocks (blockquotes) for key insights and pro tips.

4. **Templates:** Any template (journal entry, tasting notes) should be in a fenced code block so students can copy-paste it directly into their own Markdown files.

5. **Examples:** Every guide that asks students to write something should include at least one worked example. Examples should be good-but-not-perfect — specific, honest, with visible reasoning. Don't make examples so polished that students feel they can't match them.

6. **Footer:** Every guide ends with a single line: `AI + Research Level 2 • Session X: [Session Title]`

7. **No emoji** unless quoting model output that contains emoji.

8. **Cross-references:** Guides can reference other guides by filename (e.g., "see GUIDE-comparative-analysis.md for how to structure your comparison"). This teaches students to navigate a document ecosystem — a transferable skill.

9. **Supplementary datasets:** Every method card ends with an "Explore the Training Data" section linking to 2-4 browseable HF datasets. Consult `supplementary-datasets.md` for the curated list. Keep each entry to one sentence of framing + a URL + a one-line teaching hook. The section header, framing line, and closing line should follow the same pattern across all guides for consistency.

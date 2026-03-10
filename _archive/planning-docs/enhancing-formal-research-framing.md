# Enhancing Formal Research Framing in Level 2

## Context

Bing's detailed Level 2 teaching outline ("AI + Research Level 2") was designed as a conceptual ML curriculum that serves as an on-ramp to Level 3 research projects. Key expectations from correspondence:

- **Jan 26, 2026**: Bing asked to "intentionally embed some preparatory elements into Level 2 — for example, foundational tools, ways of thinking, or light technical exposure that would help students transition more smoothly into Level 3 research projects."
- **Session 12 of Bing's outline**: "Methodological Reflection & Level 3 Preparation" — hypothesis, experimental design, research framing.
- **Mar 9, 2026**: Bing said one reason for Shawn to complete Level 2 is "so that he can gradually build some foundational understanding of research methods and how academic work is actually done."

The level-2-course as built is hands-on and building-focused. It teaches the same concepts as Bing's outline but through applied work rather than theoretical framing. The gap is in **research vocabulary, formal evaluation, and structured documentation**.

---

## Session Folder Sync Rule

Each session folder contains files that must stay in sync with each other. When revising any file in a session folder, **all files in that folder must be checked and updated to reflect the same content.**

### Files per session folder

| File | What it is | Sync concern |
|---|---|---|
| `app.py` + `requirements.txt` | The HF Space build | Only changes if the build changes |
| `INSTRUCTOR-GUIDE.md` | Detailed instructor script with timing, talking points, activities | **Source of truth** for session content and flow |
| `slides.html` | Reveal.js slide deck shown on Zoom screen share | Must reflect the same segments, vocabulary, activities, and between-session homework as the instructor guide |
| `BETWEEN-SESSION.md` | Homework / between-session challenge | Must match what the instructor guide and slides say about homework |
| `notebook.ipynb` | Colab companion notebook for last ~20 min | Only changes if the hands-on activity changes |
| `README.md` | Session summary | Update if session title, concept name, or key vocabulary changes |

### The rule

**When a revision adds, removes, or changes a segment in the INSTRUCTOR-GUIDE.md, the same change must be reflected in slides.html.** Specifically:

- If a new segment is added to the instructor guide (e.g., Research Lens, Big Question), a corresponding slide or slide group must be added to slides.html in the same position in the deck.
- If the between-session homework is rewritten, the "Between Sessions" slide in slides.html must be updated to match the new homework structure.
- If vocabulary changes, the vocabulary slide must be updated.
- The instructor guide is the source of truth. The slides are the student-facing projection of it. They don't need to contain every detail, but they must not contradict or omit major segments.

### How to check

After editing any file in a session folder, read all other files in the folder and verify:
1. Do the slides cover every named segment in the instructor guide?
2. Does the "Between Sessions" slide match BETWEEN-SESSION.md?
3. Does the vocabulary slide match the "Key Vocabulary" section of the instructor guide?
4. Does the README still accurately describe the session?

---

## What Already Maps

| Bing's Outline Topic | Our Session | Current Framing |
|---|---|---|
| S1: Rules vs Models | S1: Silly Phrase Finder | Building a thing |
| S2: Data Collection & Representation | S2: Not All Feelings Are the Same | Training data, model cards, emotion taxonomies |
| S3: Data Cleaning & Feature Engineering | S3: When Sarcasm Breaks Everything | Already uses this exact concept name |
| S4: Supervised Learning | S10: Build from Scratch | Choosing tasks, labels, training data |
| S5: Model Training & Parameters | S5: Text Playground | Already teaches hyperparameters |
| S6: Model Evaluation & Metrics | S4: Sentiment Showdown | Three models compared, no formal metrics |
| S7: Overfitting & Generalization | S6: Domain Shift | Already teaches this concept |
| S8: Bias, Variance, Uncertainty | S7: Bias Tester | Already teaches bias |
| S9: Single Models to Systems | S8: Image Pipeline | Multi-model chaining, error cascades |
| S10: Prompt Logic & Human-AI Interaction | S9: Make It Actually Useful | Prompt engineering, UX design |
| S11: Mini System Integration | S10: Build from Scratch | End-to-end system design |
| S12: Methodological Reflection | S11-12: Iterate + Demo Day | No research framing currently |

---

## Three Gaps to Fill

### 1. Research Vocabulary and Framing
Sessions teach concepts through doing but never name them in research terms. Bing's outline uses: *hypothesis*, *experimental design*, *evaluation metrics*, *baseline comparison*, *methodology*, *limitations*.

### 2. Formal Evaluation / Metrics
Session 4 compares models but doesn't introduce precision, recall, accuracy, or confusion matrices even at a basic level. Session 6 compares performance but doesn't quantify it.

### 3. Structured Documentation / Research Write-up Skills
Students upload notebooks to GitHub but never write explanations of what they found and why.

---

## Core Design: Shared Example + Individual Inquiry

### The Pattern

**In class:** Everyone works on sentiment analysis together. It's the shared case study for learning research methods — the "textbook example" the instructor teaches with.

**Between sessions:** Students apply that week's research method to whatever AI topic *they* find interesting, building a personal HF Collection that becomes an evolving portfolio of their explorations.

### Why This Works

- Sentiment analysis is the instructor's worked example. Students see a method demonstrated on a known problem.
- Students' own Collections are their individual research threads. They apply the same method to image classifiers, translation models, music generators, code assistants — whatever caught their attention.
- By session 10, when students build from scratch, they've been circling their own topic for 9 weeks. The final artifact comes from their Collection, not from thin air.
- This mirrors how research labs work: shared methodology, individual questions. Exactly the pattern Bing's Level 3 uses.

### The Branching Timeline

| Session | In Class (shared, sentiment) | Homework (individual, student's choice) |
|---|---|---|
| 1 | Build Mood Meter together | Start HF Collection — explore Spaces that interest you |
| 2 | Compare 3 emotion models | Find a model on the Hub related to YOUR interest. Add to Collection with tasting note. Apply: how does training data shape what your model can do? |
| 3 | Break the model with sarcasm | Find an input that breaks a model in YOUR Collection. Is it a noise problem or a meaning problem? |
| 4 | Three models side by side | Find 2+ models for YOUR topic and compare them. Which one do you trust more? Why? |
| 5 | Temperature and hyperparameters | If your topic has controllable parameters, experiment. What settings work best for what task? |
| 6 | Domain shift | Test a model from YOUR Collection on data it wasn't trained on. Does it generalize? |
| 7 | Bias testing | Design a paired test for a model in YOUR Collection. Does it treat different groups fairly? |
| 8 | Multi-model pipeline | Can you chain two models from YOUR Collection? What happens when the first one is wrong? |
| 9 | Redesign for a real user | Pick your best model/Space and redesign it for a specific person. Who would use this? |
| 10 | Build from scratch | Build YOUR artifact — the topic you've been exploring for 9 weeks |
| 11-12 | Iterate and present | Polish, document, and present your artifact + research journey |

### What the Portfolio Looks Like at the End

Each student has:
1. **HF Collection** — curated models and Spaces they explored, with notes
2. **GitHub repo** — notebooks from class + their own experiments + Research Journal entries
3. **One finished Space** (session 10-12) — built on a topic they chose
4. **Research Journal** (9 entries) — documenting their individual line of inquiry
5. **Presentation** (session 12) — explaining what they investigated and what they found

The instructor has:
6. **SpaceCraft leaderboard** — a growing, public portfolio of curated HF Spaces rated on craft, innovation, and delight. Models the same curation behavior students are doing with their Collections. Grows visibly each week, demonstrating that exploration is ongoing.

Parents see: code, writing, a working AI tool, and a narrative of intellectual development.
Bing sees: research methods, structured documentation, portfolio artifacts, Level 3 readiness.

---

## The SpaceCraft Leaderboard: Instructor-Led Curation as Model

### What It Is

SpaceCraft (`bonus-hugging-face-spaces/spaces-leaderboard/index.html`) is the instructor's own curated leaderboard of Hugging Face Spaces, rated on Visual Craft, Feature Innovation, and Delight Factor (each scored 1-10, total out of 30). It currently includes 25 Spaces across categories (Image, Video, Audio, Chat, Code, Data, Document, 3D).

### Why It Matters for the Course

The five bonus Spaces the instructor built (Emoji Mood Translator, Headline Mood Dashboard, etc.) are useful teaching tools but they're simple — single-model wrappers on free CPU tier. SpaceCraft shows students the broader ecosystem: real Spaces built by Tencent, Microsoft, Black Forest Labs, OpenAI, and independent developers that are polished, complex, and sometimes stunning. This reframes sentiment analysis and AI tools in general as having serious, rigorous applications — not just classroom exercises.

### The Parallel Curation Pattern

SpaceCraft models the same curation behavior students are learning:

| | Instructor (SpaceCraft) | Students (HF Collection) |
|---|---|---|
| **What they curate** | HF Spaces across the whole ecosystem | Models and Spaces related to their topic |
| **How they evaluate** | Visual Craft / Innovation / Delight (scored) | Tasting notes (descriptive) |
| **How it grows** | Instructor adds entries week by week | Students add items week by week |
| **What it demonstrates** | Ongoing exploration as a practice | Individual line of inquiry developing |
| **Where it lives** | Public leaderboard page | Public HF Collection |

The instructor adding a new SpaceCraft entry each week is the visible demonstration that curation is ongoing, not a one-time assignment. Students see the instructor doing the same thing they're asked to do — exploring, evaluating, documenting.

### How to Use SpaceCraft in Sessions

**Show-and-Tell warm-up (2-3 min):** Each week, briefly show a new Space you added to SpaceCraft since last session. Frame it through that week's research method:

| Session | SpaceCraft connection | Example framing |
|---|---|---|
| 2 | Show a Space that does the same task as another but differently | "I added two image Spaces this week. Same task, different approaches — comparative analysis, just like what we did with sentiment models." |
| 3 | Show a Space and try to break it with adversarial input | "I found this OCR Space. Watch what happens when I give it a blurry photo — that's adversarial testing." |
| 4 | Show two Spaces and compare quality | "These two TTS Spaces both do speech synthesis. Which sounds more natural? That's model evaluation." |
| 5 | Show a Space with adjustable parameters | "This image generator has a guidance scale slider. Watch what happens when I change it — parameter sweep." |
| 6 | Show a Space tested outside its training domain | "This document OCR was trained on English. What happens with Japanese? Domain shift." |
| 7 | Show a Space and ask who it might not work for | "This voice cloning Space — whose voice does it handle well? Whose might it struggle with? Bias." |
| 8 | Point out a Space that chains multiple models | "This video Space runs detection + tracking + annotation. Three models in a pipeline — error propagation." |
| 9 | Show a Space with great vs. poor UX | "Both these Spaces do the same thing. One is a joy to use, the other is confusing. User-centered design." |

This takes almost no prep — the instructor is already exploring Spaces for the leaderboard. It just requires narrating the connection to the week's method.

### Sentiment and Emotion in SpaceCraft

The leaderboard currently has no sentiment or emotion-focused Spaces. As the course progresses, the instructor should actively seek and add Spaces that demonstrate sentiment analysis in serious, applied contexts — not just classroom demos. Examples to look for:

- Spaces that analyze customer reviews, social media, or news sentiment at scale
- Emotion detection in speech, music, or video
- Multimodal sentiment (text + image, text + audio)
- Sentiment-powered dashboards or monitoring tools
- Spaces that visualize emotion arcs in stories, conversations, or audio

Adding these to SpaceCraft over the course of the 12 weeks reinforces the message: sentiment analysis isn't a toy problem, it's a real field with real applications. The simple Spaces we build in class are entry points to a much larger ecosystem.

### Student-Facing Framing

**Don't present SpaceCraft as an assignment.** It's the instructor's thing — a portfolio project the instructor is building in parallel. Students see it, they see the instructor adding to it, and it normalizes the idea that curation and evaluation are ongoing intellectual activities. Some students may want to make their own version. That's great. But it's not required.

**What to say:** "Every week I explore Spaces on Hugging Face and add the ones I think are exceptional to my SpaceCraft leaderboard. I rate them on three things: how they look, what they invent, and how fun they are to use. You're doing something similar with your Collection — but yours is focused on your topic, and your tasting notes are your evaluation criteria."

---

## Addition A: In-Session "Research Lens" (5 min)

Added after "Name the Concept" in each session. Names what students just did in research language. The research question is framed using the shared sentiment example, but the method is general.

| Session | Research Lens | Shared Research Question (sentiment) | Method (applies to any topic) |
|---|---|---|---|
| 2 | "We did a **comparative analysis** using different **operationalizations** of emotion." | "How does the choice of emotion taxonomy affect sentiment classification?" | Compare multiple models on same inputs, observe divergence |
| 3 | "We tested **adversarial inputs** and performed **data preprocessing** — cleaning noise vs. signal." | "What types of text input cause sentiment models to fail, and can preprocessing fix them?" | Controlled before/after comparison |
| 4 | "We ran a **model evaluation** — same inputs, three judges. This is a **baseline comparison**." | "Which sentiment model is most accurate across diverse inputs?" | Side-by-side evaluation with human ground truth |
| 5 | "We did a **parameter sweep** — systematically changing one variable while holding others constant. That's **experimental design**." | "How does temperature affect text generation quality for different writing tasks?" | Controlled experiment, one variable at a time |
| 6 | "We tested **generalization** — does the model work on data it wasn't trained on? This is about **external validity**." | "How well do sentiment models generalize across domains?" | Cross-domain testing |
| 7 | "We designed a **fairness audit** — a systematic test for **algorithmic bias**." | "Does this model treat different demographic groups differently?" | Paired-sentence testing, controlled variable swaps |
| 8 | "We built a **pipeline** and studied **error propagation** — when one component fails, does the whole system fail?" | "How do errors cascade in a multi-model system?" | Inject errors at stage 1, measure impact at stage 2 |
| 9 | "We did **user-centered design** — the research question shifts from 'does the model work?' to 'can a person use it?'" | "How does output framing affect the usefulness of AI predictions?" | Redesign and user testing |
| 10 | "You just did **end-to-end system design** — choosing a question, a method, and building a tool to answer it. That's a **research prototype**." | Students articulate their own | Student-chosen |

**Key framing line each week:** "In class, we applied [method] to sentiment analysis. For your homework, you'll apply the same method to your own topic."

---

## Addition B: Between-Session Research Journal (1-2 hours)

Each week, students write a short journal entry applying the week's method to their own topic. The journal entry goes in their GitHub repo alongside their notebooks.

### Template (same every week, builds the habit)

```markdown
## Week [X] Research Journal — [Student's Topic]

### This Week's Method
(What research method did we learn in class? e.g., comparative analysis, bias testing, domain shift)

### How I Applied It
(What did I test? What model/Space from my Collection did I use? What inputs did I try?)

### What I Expected
(My prediction before testing)

### What I Found
(Key observations — what happened?)

### Why I Think This Happened
(My explanation — connect it to training data, model design, domain, etc.)

### Limitations
(What couldn't I test? What might be different with other data/models/topics?)

### What I Want to Try Next
(Where is my investigation going? What question am I circling?)
```

### How This Evolves

- **Weeks 1-3:** Students are still exploring. Journals may cover different models/Spaces each week. That's fine — they're casting a wide net.
- **Weeks 4-6:** A topic should start emerging. The "What I Want to Try Next" section pulls them forward. Instructor can nudge: "I notice you keep coming back to translation models — lean into that."
- **Weeks 7-9:** Students are applying methods to a specific line of inquiry. Journals build on each other. The Collection has a clear focus area.
- **Week 10:** The journal entries collectively form the rationale for what they build from scratch. "I've been investigating X for 9 weeks. Here's what I've learned. Here's what I'm building."

### Word Count

300-500 words per entry. Age-appropriate for 8th-10th graders. Over 9 weeks, that's 2,700-4,500 words of structured research writing — a substantial portfolio artifact in itself.

---

## Addition C: Big Questions from Sentiment Course (Sessions 4-10)

The level-2-sentiment course has Big Questions for sessions 4-9 that haven't been merged into the main course yet. These are 10-15 minute discussions that anchor the session's research theme. They should be added to sessions 4-9 of the main course.

| Session | Big Question (from sentiment course) |
|---|---|
| 4 | "When humans disagree about feelings, who's right?" — frames model evaluation as inter-rater reliability |
| 5 | "Can AI create writing that makes you feel something?" — frames hyperparameters as emotional control |
| 6 | "Is 'positive' the same thing in a product review and a love poem?" — frames domain shift through emotional meaning |
| 7 | "If a school used voice analysis to detect angry students, whose voices would it get wrong?" — frames bias through real stakes |
| 8 | "Can you read emotion from a photograph?" — frames multi-model systems through competing evidence |
| 9 | "When is it helpful to have a machine read your feelings — and when is it creepy?" — frames UX as ethics |

These can be added without changing the builds. They're discussion segments that deepen the research framing.

---

## Implementation Status (updated 2026-03-10)

### Already Done

| File | What was done |
| --- | --- |
| `session-01/BETWEEN-SESSION.md` | Restructured into 3 parts. Added framing that Collection follows student's own curiosity, not just sentiment. Added time estimate (1-2 hrs). |
| `session-02/BETWEEN-SESSION.md` | Full rewrite. Option A/B hub challenge (sentiment OR own topic). Research Journal template with Week 2 entry. GitHub instructions for creating `research-journal.md`. |
| `session-02/INSTRUCTOR-GUIDE.md` | Research Lens added after Name the Concept. SpaceCraft check-in added to Show-and-Tell (comparative analysis framing). Already had Big Question and sentiment framing from earlier merge. |
| `session-03/INSTRUCTOR-GUIDE.md` | Research Lens added after Name the Concept. SpaceCraft check-in added to Show-and-Tell (adversarial testing framing). Already had Big Question and multimodal voice aside from earlier merge. |
| `session-03/BETWEEN-SESSION.md` | Full rewrite matching session 2 format. Option A/B (break a model on purpose), Research Journal Week 3 template, Collection targets (5 models + 3 Spaces by Session 4), GitHub upload + journal edit instructions. |
| `session-01/INSTRUCTOR-GUIDE.md` | Already has Big Question ("Can a Machine Actually Feel?") and sentiment framing from earlier sentiment course merge. |

| `session-02/slides.html` | Research Lens slide added. "Between Sessions" rewritten as 3-slide group. SpaceCraft check-in slide added after Show-and-Tell (comparative analysis framing). |
| `session-03/slides.html` | Research Lens slide added. "Between Sessions" rewritten as 3-slide group. SpaceCraft check-in slide added after Show-and-Tell (adversarial testing framing). |
| `session-04/INSTRUCTOR-GUIDE.md` | Research Lens added after Name the Concept (baseline comparison framing). SpaceCraft check-in added to Show-and-Tell (model evaluation framing). Big Question added ("When Models Disagree, Who's Right?" — adapted from sentiment session 4). Timings adjusted. |
| `session-04/BETWEEN-SESSION.md` | Full rewrite matching session 2 format. Option A/B (compare models side by side), Research Journal Week 4 template, Collection targets (6 models + 4 Spaces by Session 5), GitHub upload + journal edit instructions. |
| `session-04/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. |
| `session-05/INSTRUCTOR-GUIDE.md` | Research Lens added after Name the Concept (parameter sweep / experimental design framing). SpaceCraft check-in added to Show-and-Tell (adjustable parameters framing). Big Question added ("Can a Machine Write Something That Makes You Feel?" — adapted from sentiment session 5). Timings adjusted. |
| `session-05/BETWEEN-SESSION.md` | Full rewrite matching session 2 format. Option A/B (experiment with settings), Research Journal Week 5 template, Collection targets (7 models + 5 Spaces by Session 6), GitHub upload + journal edit instructions. |
| `session-05/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. |
| `session-06/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added to Show-and-Tell (domain shift framing). Big Question added ("Is 'Positive' the Same Thing Everywhere?" — adapted from sentiment session 6). Research Lens added after Name the Concept (generalization / external validity framing). Timings adjusted for all new segments. |
| `session-06/BETWEEN-SESSION.md` | Full rewrite matching session 5 format. Option A/B (cross-domain testing), Research Journal Week 6 template, Collection targets (8 models + 5 Spaces by Session 7), GitHub upload + journal edit instructions. |
| `session-06/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. External validity added to Vocabulary slide. |
| `session-07/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added to Show-and-Tell (bias framing). Big Question added ("If AI Screens Your Application, Does Your Name Matter?" — adapted from sentiment session 7). Research Lens added after Name the Concept (fairness audit / algorithmic bias framing). Timings adjusted for all new segments. |
| `session-07/BETWEEN-SESSION.md` | Full rewrite matching session 6 format. Option A/B (test for bias), Research Journal Week 7 template, Collection targets (9 models + 6 Spaces by Session 8), GitHub upload + journal edit instructions. |
| `session-07/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. Algorithmic bias added to Vocabulary slide. |
| `session-08/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added to Show-and-Tell (multi-model pipeline framing). Big Question added ("Can You Read Emotion from a Photograph?" — adapted from sentiment session 8). Research Lens added after Name the Concept (error propagation / systems testing framing). Timings adjusted for all new segments. |
| `session-08/BETWEEN-SESSION.md` | Full rewrite matching session 6 format. Option A/B (chain two models / break the pipeline), Research Journal Week 8 template, Collection targets (10 models + 6 Spaces by Session 9), GitHub upload + journal edit instructions. |
| `session-08/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. Error propagation added to Vocabulary slide. |
| `session-09/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added to Show-and-Tell (UX comparison framing). Big Question added ("When Is It Helpful vs. Creepy?" — adapted from sentiment session 9). Research Lens added after Name the Concept (user-centered design / usability testing framing). Timings adjusted for all new segments. |
| `session-09/BETWEEN-SESSION.md` | Full rewrite matching session 8 format. Option A/B (redesign for a real person), Research Journal Week 9 template, Collection targets (11 models + 7 Spaces by Session 10), GitHub upload + journal edit instructions. |
| `session-09/slides.html` | SpaceCraft check-in slide added. Big Question slide group added (3 slides). Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. User-centered design and usability testing added to Vocabulary slide. |
| `session-10/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added to Show-and-Tell (complete experience / Collection connection framing). Research Lens added after Name the Concept (end-to-end system design / research prototype framing). No Big Question (build-from-scratch session). Timings adjusted for all new segments. |
| `session-10/BETWEEN-SESSION.md` | Full rewrite matching session 8 format. Option A/B (get your Space working + test with 5 inputs), Research Journal Week 10 template, Collection targets (12 models + 7 Spaces by Session 11), GitHub upload + journal edit instructions. |
| `session-10/slides.html` | SpaceCraft check-in slide added. Research Lens slide added. "Between Sessions" rewritten as 3-slide group with Option A/B and journal. Research prototype added to Vocabulary slide. |
| `session-11/INSTRUCTOR-GUIDE.md` | SpaceCraft check-in added (iteration framing). Research Journey Review segment added (replaces Big Question). Demo Day Prep rewritten with 5-part research presentation format. Timings adjusted for all new segments. |
| `session-11/BETWEEN-SESSION.md` | Full rewrite in 3-part format. Part 1: Final polish + practice research presentation (with 5-part format). Part 2: Research Journal Week 11 entry ("The Thread" — ties narrative together). Part 3: Final Collection check (12 models + 7 Spaces), notebook upload, journal entry. |
| `session-11/slides.html` | SpaceCraft check-in slide added. Research Journey Review slide group added (2 slides). Demo Day Prep slide rewritten with research presentation format. Demo Tips updated to mention Collection and journal. "Between Sessions" rewritten as 3-slide group. "Research journey" added to Vocabulary slide. |
| `session-11/peer-feedback-form.md` | Added "Research Connection" question: "What topic has this person been exploring? Can you tell from their Space?" |
| `session-12/INSTRUCTOR-GUIDE.md` | Presentation format rewritten with research framing (My question → My journey → My artifact → What I found → What's next). Reflection section expanded with "What research method was most useful?" question. 9 Research Methods recap table added alongside 10 ML Concepts table. Portfolio Consolidation rewritten to include Collection URL, research journal link, research question, and methods used. Pre-session checklist updated. |
| `session-12/slides.html` | Presentation format slide rewritten with research framing. Tonight's Goal updated to emphasize research journey. Tech Check updated to include Collection and journal access. 9 Research Methods recap added as 2-slide vertical group alongside 10 Concepts. Reflection slide updated with research method question. Portfolio slide expanded with Collection, GitHub repo, research question, and methods. "What You Know Now" and closing slides updated to reference concepts + methods + individual inquiry. |
| `session-12/portfolio-template.md` | Added: Research Question section, HF Collection section (URL + item count + focus area), Research Journal section (repo link + journal link + entry count + investigative thread summary), Research Methods Used checklist (all 9 methods with session numbers), "Most useful research method" reflection question. |

### Still To Do — Sessions 11-12

Complete. All sessions 1-12 now have research framing.

### Implementation Priority

1. ~~**Session 6**~~ — DONE: BETWEEN-SESSION.md rewrite, Research Lens, SpaceCraft check-in, Big Question, slides sync
2. ~~**Session 7**~~ — DONE: BETWEEN-SESSION.md rewrite, Research Lens, SpaceCraft check-in, Big Question, slides sync
3. ~~**Session 8**~~ — DONE: BETWEEN-SESSION.md rewrite, Research Lens, SpaceCraft check-in, Big Question, slides sync
4. ~~**Session 9**~~ — DONE: BETWEEN-SESSION.md rewrite, Research Lens, SpaceCraft check-in, Big Question (adapted from sentiment session 9), slides sync
5. ~~**Session 10**~~ — DONE: BETWEEN-SESSION.md rewrite, Research Lens, SpaceCraft check-in, slides sync (no Big Question — build-from-scratch session)
6. ~~**Sessions 11-12**~~ — DONE: Research presentation framing, SpaceCraft check-in (S11), Research Journey Review (S11), 3-part between-session (S11), research presentation format (S11+S12), 9 Research Methods recap (S12), portfolio template expanded (S12), peer feedback form updated (S11), slides sync (S11+S12)

---

## What This Looks Like to Parents and Bing

**To parents:** "Your child will build AI tools hands-on every week, maintain a curated portfolio of AI models they've investigated, write weekly research journal entries documenting their findings, and present a final project with both a working prototype and a written account of their research process."

**To Bing:** The course teaches research methods (comparative analysis, experimental design, bias auditing, domain generalization, user-centered design) through applied building. Students develop individual lines of inquiry documented in structured research journals. The final portfolio includes working code, written analysis, and a research presentation — direct preparation for Level 3.

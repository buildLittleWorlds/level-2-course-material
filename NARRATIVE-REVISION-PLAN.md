# Narrative Revision Plan: How We Got to Generative AI

**Created:** March 20, 2026
**Last updated:** March 21, 2026
**Status:** Sessions 3–11 revised. Session 12 pending.
**Context:** This is the first time through the Level 2 course (Spring 2026, Saturday evenings). It will be taught two more times over the summer. The goal is to get the narrative right now so the summer sections benefit from a coherent story arc.

---

## The Problem

The current course teaches strong ML concepts, but each session stands alone. Students learn adversarial testing in Session 3, model evaluation in Session 4, hyperparameters in Session 5 — but there's no connective thread that explains why these concepts matter together or how they build toward the AI systems students already use every day.

Meanwhile, the students live in a world shaped by generative AI. They use ChatGPT, they see AI-generated images, they hear about AI in the news constantly. The course teaches them the building blocks that made all of that possible, but it never says so. That's a missed opportunity.

## The Narrative

The story across Sessions 1-10 is: **How did we get from models that sort text into buckets to models that write essays and generate images?**

Every concept in the course is a stepping stone in that story. Students aren't learning abstract ML topics — they're learning the exact ideas, in roughly the order the field discovered them, that got us from "a computer can sort email" to "a computer can write a novel." By Session 10, they know enough to build something themselves and to understand why it works, why it breaks, and who it affects.

The narrative has three acts:

### Act I: The Old Way (Sessions 1-3)

These sessions represent the classical ML paradigm. Small, narrow models that do one thing. Humans do enormous manual work to make them function: choosing features, cleaning data, hand-tuning inputs. Even after all that effort, the models are brittle — sarcasm breaks them, ambiguity confuses them, and they only work within the narrow domain they were trained on.

**The feeling students should have by the end of Act I:** "These models are impressive but limited. They can sort things into buckets, but they don't understand anything."

### Act II: The Breakthrough (Sessions 4-8)

These sessions trace the ideas that enabled generative AI. Each session is a piece of the puzzle. The order matters — each concept sets up the next:

- **Classification vs. Generation (Session 4)** — The fork in the road. Generation doesn't need labeled data, just text. That made scale possible.
- **Hyperparameters (Session 5)** — The control knobs on generation. Temperature and top-p are literally the controls on ChatGPT and Claude.
- **Domain shift (Session 6)** — The wall that classification couldn't get past. The breakthrough: "train on everything."
- **Bias (Session 7)** — The cost of training on everything. Scale amplifies every pattern in the data, including harmful ones.
- **Pipelines (Session 8)** — How modern AI products actually work. Not one model, but chains of models where errors cascade.

**The feeling students should have by the end of Act II:** "I can see how each of these problems pushed the field to try something bigger. And I can see why that bigger thing brought new problems."

### Act III: Building and Reflecting (Sessions 9-12)

Students take what they've learned and build. Session 9 is prompt engineering — the human interface to AI. Session 10 is building their own Space. Sessions 11-12 are iteration and presentation.

**The feeling students should have by the end of Act III:** "I built something real, and I understand the ideas behind it well enough to explain what it can and can't do."

---

## Revision Status by Session

### Session 1: Can a Computer Tell How You Feel? — NO CHANGES NEEDED
**Concept:** THE AI PIPELINE (input → model → output)
**Narrative role:** The starting point. Students see AI do something for the first time.
**Status:** Works as-is. Add a brief framing line at the end: "This is the simplest version of what AI does — take an input, run it through a model, give an output. Everything we do for the next 11 weeks builds on this."
**Files to change:** Minor addition to instructor guide closing. Not urgent.

### Session 2: Not All Feelings Are the Same — NO CHANGES NEEDED
**Concept:** TRAINING DATA AND REPRESENTATION
**Narrative role:** The first insight — the model's world is shaped by its training data. Different training data = different model = different answers.
**Status:** Works as-is. Already well-structured. The comparative analysis across three models naturally demonstrates that what a model can see depends on what it was trained to see.
**Files to change:** None. Already strong.

### Session 3: What Models Can't Do — REVISED ✅
**Concept:** ADVERSARIAL TESTING AND THE LIMITS OF CLASSIFICATION
**Narrative role:** The culmination of Act I. Closes "The Old Way" by demonstrating three failure modes (tone deafness, emotional flattening, anthropomorphic projection) across four models. Ends with a named summary of Sessions 1–3 and a forward bridge to generation.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Complete rewrite. New 2-hour structure: Break the Mood Meter (warmup), Build the Sarcasm Breaker Space (live HF Space build with clean_text(), framed as emblem of old paradigm), Story Arc Adversarial Demo (30-min centerpiece, three stories across four models), Sum Up The Old Way (Act I closer with scripted monologue), CLEAR Framework, Student Topic Elicitation, Notebook Time.
- ✅ `slides.html` — Complete rewrite. New slides for each adversarial story, three failure mode reveals, "The Old Way" recap, forward bridge to generation.
- ✅ `GUIDE-adversarial-testing.md` — Added Three Failure Modes section. Updated shared example. Updated footer.
- ✅ `BETWEEN-SESSION.md` — Updated to reference three failure modes. "Bring It Back" bridges to Session 4's classification vs. generation concept.
- ✅ `README.md` — Rewritten for new session scope.
- ✅ `notebook.ipynb` — Complete rewrite. Act I capstone notebook: walks through full Sessions 1–3 arc, tests all three failure modes with two models, proves cleaning can't fix meaning problems, proves more labels don't help, "The Old Way" summary with bridge to Session 4.
- ✅ `explorer.ipynb` — Complete rewrite. Students test all three failure modes on a model from their own Collection, build a failure profile, bridge to Session 4.
- ✅ `app.py` — Unchanged (Sarcasm Breaker with clean_text()). Still fits: it's the live build artifact for the 0:25–0:45 segment.
- ✅ `requirements.txt` — Unchanged. Still correct.
- ✅ `GUIDE-intro-to-markdown.md` — Unchanged. Still relevant.

**Archived:** Original instructor guide moved to `_archive/obsolete-session-files/session-03-INSTRUCTOR-GUIDE-original.md`.

### Session 4: What If AI Could Create? — REVISED ✅
**Concept:** CLASSIFICATION VS. GENERATION
**Narrative role:** The fork in the road. Act II opener. Everything in Sessions 1–3 was classification; Session 4 introduces generation. The key insight: classification needs labeled data (expensive), generation needs just text (everywhere). That difference made scale — and generative AI — possible.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Complete rewrite. New 2-hour structure: Show-and-Tell + SpaceCraft (text generation Space), The Wall and the Question (replay Sessions 1–3, spam detector thought experiment, name the fork), Build and Explore the Text Generator Space (live HF Space build — the `pipeline("sentiment-analysis")` → `pipeline("text-generation")` change IS the lesson, then explore with adversarial stories), The Fork in the Road (two-column classification vs. generation comparison, training data revelation, model card comparison), Name the Concept + Bridge Forward, Between-Session Preview, Notebook Time.
- ✅ `slides.html` — Complete rewrite. New slides for: story so far, the wall, spam detector, the question, demo with three test stories, the fork comparison table, training data difference, the insight that changed everything, model card comparison, naming the concept, road ahead (three-act overview).
- ✅ `GUIDE-classification-vs-generation.md` — New file (replaces old GUIDE-baseline-comparison.md). Covers the fork, how each type learns, when researchers use each, evaluation concepts (accuracy trap, false positives/negatives, evaluating generation is harder).
- ✅ `BETWEEN-SESSION.md` — Complete rewrite. Students explore both sides of the fork: find a classifier and a generator, test on same inputs, compare. Bridges to Session 5 (temperature).
- ✅ `README.md` — Rewritten for new session scope.
- ✅ `app.py` — Rewritten. Simple distilgpt2 text generator (no controls — Session 5 adds temperature/top-p). Used in live build during class.
- ✅ `requirements.txt` — Unchanged. Still correct (transformers, torch, gradio).
- ✅ `GUIDE-intro-to-markdown.md` — Unchanged. Still relevant.
- ✅ `notebook.ipynb` — Complete rewrite. Loads both a classifier and distilgpt2 generator side by side. Tests all three adversarial stories from Session 3 on both models (connecting back to the three failure modes). Demonstrates variability (run the generator 3 times, get 3 different outputs). Includes a next-word probability peek (top 10 most likely next words) to set up Session 5's temperature concept.
- ✅ `explorer.ipynb` — Complete rewrite. Students load a classifier and a generator from their own Collection, design 5 test inputs, run both models on each, compare outputs side by side. Includes variability test and research journal draft.

**Archived:** Original instructor guide, app.py (Sentiment Showdown), and GUIDE-baseline-comparison.md moved to `_archive/obsolete-session-files/`.

### Session 5: Add Controls — REVISED ✅
**Concept:** HYPERPARAMETERS
**Narrative role:** The knobs on the machine. Temperature and top-p are literally the controls on ChatGPT and Claude. Students first touch generative AI directly.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Updated Show-and-Tell to reference Session 4's classification vs. generation homework. Added "Story So Far" narrative bridge connecting Session 4's generator to Session 5's controls, including the real-world API connection ("Right now, somewhere, a developer is setting temperature to 0.7 on an API call to Claude. That's this slider."). Reframed live build as "adding controls to the Session 4 generator" rather than building from scratch. Added real-world connection beat to Name the Concept section (ChatGPT, Claude API, hidden sliders). Added scripted Bridge Forward to Session 6 (domain shift teaser). Updated Concept Connections to reflect revised Sessions 3–4.
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act II · The Breakthrough." Updated Show-and-Tell to reference Session 4 homework. Added "Story So Far" slide with real-world API connection. Reframed build slides as "adding controls to last week's generator." Added "Behind the Curtain" real-world connection slide after Name the Concept. Replaced vague "Next Week" with Session 6 domain shift bridge.
- ✅ `notebook.ipynb` — Updated title cell to "Add Controls" with narrative connection to Session 4. Updated "What We Built Tonight" cell to reference the Session 4 → Session 5 progression and the real-world API connection.
- ✅ `BETWEEN-SESSION.md` — Added "Looking ahead" forward bridge to Session 6 in the Bring It Back section.
- ✅ `GUIDE-parameter-sweep.md` — Updated footer from "Text Playground" to "Add Controls."
- ✅ `README.md` — Rewritten with "Add Controls" title, narrative role section, and updated description connecting hyperparameters to real-world AI tools.
- ✅ `explorer.ipynb` — No changes needed. Already well-scaffolded.
- ✅ `app.py` — No changes needed. Already has temperature/top-p/max-length sliders on distilgpt2.
- ✅ `requirements.txt` — No changes needed.

### Session 6: Same Space, Different Worlds — REVISED ✅
**Concept:** OVERFITTING AND DOMAIN SHIFT
**Narrative role:** The wall that classification couldn't get past. This is the narrative pivot point — the breakthrough: "train on everything."

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added "Story So Far" narrative bridge connecting Session 5's controls to Session 6's domain wall. Added scripted "Breakthrough" moment in Name the Concept section: the pivot from specialized models to pretraining on everything, naming BERT (2018). Added BERT connection to Research Lens (pretraining as solving external validity). Added scripted Bridge Forward to Session 7 (bias as the cost of scale). Updated Concept Connections to reflect revised Sessions 3–5 and bonus-bert-content-moderation module. Added note pointing interested students to bonus module.
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act II · The Breakthrough." Added "Story So Far" slide recapping Sessions 1–5. Added two-slide "The Wall / The Breakthrough" sequence after Name the Concept (domain wall → pretraining on everything → BERT 2018). Added "Pretraining" to Vocabulary slide. Replaced vague "Next Week" with scripted bridge forward connecting training on everything to bias.
- ✅ `notebook.ipynb` — Updated title cell to "Same Space, Different Worlds" with narrative connection to Session 5. Updated "What We Built Tonight" cell with breakthrough narrative (pretraining on everything, BERT). Added "Pretraining" to Vocabulary table.
- ✅ `BETWEEN-SESSION.md` — Updated "Bring It Back" with forward bridge to Session 7's bias topic. Added "Looking Ahead" section pointing to bonus-bert-content-moderation as optional deeper reading. Updated journal heading to match session title.
- ✅ `README.md` — Rewritten with "Same Space, Different Worlds" title, narrative role section, connections section (builds on Session 5, bridges to Session 7, links to bonus module).
- ✅ `GUIDE-external-validity.md` — Updated footer from "Domain Safari" to "Same Space, Different Worlds."
- ✅ `notebook.ipynb` — No structural changes to experiments. Framing updates only.

**Unchanged (already strong):**
- Domain Safari activity and all 11 domain text samples
- Big Question ("Is positive the same thing everywhere?")
- Pattern Recognition and Student Challenge segments
- Notebook experiments and helper function
- No app.py (correct — no new build this session)

### Session 7: Who Gets Hurt? — REVISED ✅
**Concept:** BIAS IN AI
**Narrative role:** The cost of scale. Training on everything means training on all of humanity's biases.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added "Story So Far" narrative bridge after Show-and-Tell connecting Sessions 1–6 arc to tonight's cost-of-scale theme, including reference to bonus-bert-content-moderation module. Added "Connect back to the breakthrough" beat in Name the Concept section linking bias explicitly to Session 6's pretraining breakthrough. Added scripted Bridge Forward to Session 8 (bias cascading through multi-model pipelines → error cascades). Updated header with Narrative Role. Shifted SpaceCraft to 0:08–0:11 and Big Question to 0:11–0:23 to accommodate Story So Far.
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act II · The Breakthrough." Added "Story So Far" slide recapping Sessions 1–6 arc. Added breakthrough-cost fragment to Name the Concept slide. Updated "Next Week" slide with bridge forward connecting bias to error cascades.
- ✅ `notebook.ipynb` — Updated title cell to "Who Gets Hurt?" with Act II subtitle and narrative connection to Session 6's breakthrough. Updated "What We Built Tonight" cell with breakthrough-cost framing. Added "Looking ahead" bridge to Session 8 in Challenge cell.
- ✅ `BETWEEN-SESSION.md` — Added "Looking Ahead" section bridging to Session 8's error cascades concept.
- ✅ `README.md` — Rewritten with "Who Gets Hurt?" title, narrative role section, connections section (builds on Session 6, bridges to Session 8, links to bonus module).
- ✅ `GUIDE-fairness-audit.md` — No changes needed. Footer already correct ("Session 7: Who Gets Hurt?").
- ✅ `app.py` — No changes needed. Space name "Bias Tester" is correct (it's the Space name, not the session name).
- ✅ `requirements.txt` — No changes needed.
- ✅ Google Classroom — Topic renamed from "Session 7: Bias Tester" to "Session 7: Who Gets Hurt?". Material titles updated: "Session 7 Slides: Who Gets Hurt?", "Session 7 Notebook: Who Gets Hurt?".

**Unchanged (already strong):**
- Big Question, demo, live build sequence, paired-sentence testing activity
- "This Matters" segment, Research Lens, teaching sensitivity notes
- Pre-tested paired sentences and "What Could Go Wrong" table
- All code (app.py, notebook experiments, helper function)

### Session 8: Chain Two Models Together — REVISED ✅
**Concept:** MULTI-MODEL SYSTEMS AND ERROR CASCADES
**Narrative role:** The final piece of Act II. How modern AI products actually work — not one model, but a pipeline. This is the culmination: students now know classification, generation, controls, domain shift, bias, and pipelines.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added Narrative Role to header. Added "Story So Far" narrative bridge after Show-and-Tell connecting Sessions 1–7 arc to tonight's pipeline concept, including recap of Session 7's bias cost. Shifted SpaceCraft Check-In to 0:08–0:11 and Big Question to 0:11–0:23 to accommodate Story So Far. Added real-world product connection to Name the Concept section (ChatGPT content filter, Midjourney safety classifier — "Every AI product you use is a pipeline like this one"). Replaced generic wrap-up with scripted Act II closer: "You now know what's inside the machine. Next week: what's outside it. That's Act III."
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act II · The Breakthrough." Added "Story So Far" slide recapping Sessions 1–7 arc. Added real-world product connection fragment to Name the Concept slide. Replaced "Next Week" slide with Act II closer: "The Full Stack" concept chain, "You now know what's inside the machine," bridge to Act III.
- ✅ `notebook.ipynb` — Updated title cell to "Chain Two Models Together" with Act II subtitle and narrative connection to Session 7's bias cost. Updated "What We Built Tonight" cell with pipeline-as-product framing. Added "What You Know Now" section to Challenge cell with Act II summary and bridge to Session 9.
- ✅ `BETWEEN-SESSION.md` — Added "Looking Ahead" section bridging to Session 9's human-centered design concept. Frames the Act II → Act III transition.
- ✅ `README.md` — Rewritten with "Chain Two Models Together" title, narrative role section, connections section (builds on Session 7, bridges to Session 9, Act II arc summary).
- ✅ `GUIDE-error-propagation.md` — No changes needed. Footer already correct ("Session 8: Chain Two Models Together").
- ✅ Google Classroom — Topic renamed from "Session 8: Image Pipeline" to "Session 8: Chain Two Models Together". Material titles updated: "Session 8 Slides: Chain Two Models Together", "Session 8 Notebook: Chain Two Models Together".

**Unchanged (already strong):**
- Big Question, demo, live build sequence, error cascade demo
- Test with Images segment, Research Lens, all teaching moments
- Memory and Performance Notes, What Could Go Wrong table
- All code (app.py, notebook experiments, helper function)

### Session 9: Make It Actually Useful — REVISED ✅
**Concept:** PROMPT ENGINEERING AND HUMAN-AI INTERACTION
**Narrative role:** The Act III opener. After eight sessions understanding the machine, this is about designing the interface. The shift from studying models to designing for humans.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added Narrative Role to header. Added "Story So Far" narrative bridge at 0:05–0:08 connecting the full Act I / Act II arc to tonight's Act III opener, including the shift from "what's inside the machine" to "who is this for?" Shifted SpaceCraft Check-In to 0:08–0:11 and Big Question to 0:11–0:23 to accommodate Story So Far. Added real-world connection beat to Name the Concept section ("This is the most accessible skill in AI — you can't retrain GPT-4, but you can redesign how people interact with it"). Replaced Between-Session Preview with scripted Bridge Forward to Session 10 ("That's everything except one thing: building your own from scratch"). Updated Concept Review table to match all revised session titles (Sessions 1–9).
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act III · Building and Reflecting." Added "Story So Far" slide with three-act overview (Act I → Act II → Act III, "Tonight you design for humans"). Replaced "Next Week" slide with Bridge Forward ("Nine Sessions" arc summary, bridge to Session 10).
- ✅ `notebook.ipynb` — Updated title cell to "Make It Actually Useful" with Act III subtitle and narrative connection to Session 8. Updated "What We Built Tonight" cell with full-arc framing and bridge to Session 10.
- ✅ `BETWEEN-SESSION.md` — Added "Looking Ahead" section bridging to Session 10's independent build. Frames the nine-session arc and what's left.
- ✅ `README.md` — Rewritten with "Make It Actually Useful" title, narrative role section, connections section (builds on Session 8, bridges to Session 10).
- ✅ `GUIDE-user-centered-design.md` — No changes needed. Footer already correct ("Session 9: Make It Actually Useful").
- ✅ Google Classroom — Topic renamed from "Session 9: Make It Useful" to "Session 9: Make It Actually Useful". Material titles updated: "Session 9 Slides: Make It Actually Useful", "Session 9 Notebook: Make It Actually Useful".

**Unchanged (already strong):**
- Show-and-Tell, Big Question, live redesign demo, student brainstorm + build
- Four redesign templates, build time, usability testing segment
- Research Lens, Notebook Time, all teaching moments
- All code (app.py, notebook experiments, design worksheet)
- Pre-session prep, instructor tips, "What Could Go Wrong" content

### Session 10: Build Your Own from Scratch — REVISED ✅
**Concept:** SUPERVISED LEARNING AND TASK DESIGN
**Narrative role:** The synthesis. Students build something using everything they've learned. Every choice they make — what task, what model, what audience, what could go wrong — embeds a concept from Sessions 1–9.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added Narrative Role to header. Added "Story So Far" narrative bridge at 0:07–0:10 connecting the full three-act arc to tonight's synthesis. Shifted SpaceCraft Check-In to 0:10–0:13 to accommodate. Updated recap table at 0:00–0:07 with correct revised Space names (Mood Meter, Emotion Spectrum, Sarcasm Breaker, Text Generator, Text Playground, Bias Tester, Image Story Pipeline, Restaurant Review Analyzer) and session concepts. Added real-world connection beat to Name the Concept ("Every AI product you've ever used started exactly like this"). Replaced generic wrap-up with scripted Bridge Forward to Session 11 (the experimentation loop — swap, break, iterate). Added Concept Review table (Sessions 1–10).
- ✅ `slides.html` — Matching narrative updates. Updated title to "Build Your Own from Scratch." Updated subtitle to "Act III · Building and Reflecting." Updated "Everything We've Built" slide with correct Space names and concepts. Added "Story So Far" slide with three-act overview (matching Session 9 pattern). Added real-world connection fragment to Name the Concept slide. Replaced "Next Week" slide with Bridge Forward ("The Experimentation Loop").
- ✅ `notebook.ipynb` — Updated title cell to "Build Your Own from Scratch" with Act III subtitle and narrative connection to Sessions 1–9. Updated framing cell with Space build progression. Added "Looking ahead" bridge to Session 11 in Challenge cell.
- ✅ `BETWEEN-SESSION.md` — Added "Looking Ahead" section bridging to Session 11's experimentation loop concept.
- ✅ `README.md` — Rewritten with "Build Your Own from Scratch" title, narrative role section, connections section (builds on Session 9, bridges to Session 11).
- ✅ `GUIDE-build-planning.md` — No changes needed. Footer already correct ("Session 10: Build Your Own from Scratch").
- ⏳ Google Classroom — Page failed to load during revision session. **Manual update needed:** Rename topic to "Session 10: Build Your Own from Scratch." Update material titles: "Session 10 Slides: Build Your Own from Scratch", "Session 10 Notebook: Build Your Own from Scratch".

**Unchanged (already strong):**
- Hub Browsing Demo, Students Browse and Pitch, Build Time, Peer Testing
- Pre-Screened Models list, rescue templates, common issues table
- Research Lens, Notebook Time, all teaching moments
- All code (app.py, templates/, requirements.txt)
- Pre-session prep, instructor tips, Hub browsing tips

### Session 11: Iterate and Polish — REVISED ✅
**Concept:** THE EXPERIMENTATION LOOP
**Narrative role:** The refinement. Students take their Session 10 builds and make them better through peer feedback and systematic testing. The Session 3 adversarial testing mindset returns — but now directed at improving each other's work rather than exposing model limits.

**All files revised:**
- ✅ `INSTRUCTOR-GUIDE.md` — Narrative framing additions (not a structural rewrite). Added Narrative Role to header. Added "Story So Far" narrative bridge at 0:03–0:06 connecting the full three-act arc to tonight's experimentation loop, including Session 3 callback ("Back in Session 3, you broke models to find their limits. Tonight you break each other's Spaces — to make them better") and real-world connection ("OpenAI didn't ship ChatGPT and walk away — they tested it, got feedback, iterated"). Shifted all subsequent times by +3 min. Added narrative note to Quick Demos encouraging instructor to name course concepts during feedback. Replaced generic between-session preview with scripted Bridge Forward to Session 12 (eleven-session arc summary, narrative prompt: "How does your project connect to the bigger story?"). Added Concept Review table (Sessions 1–11).
- ✅ `slides.html` — Matching narrative updates. Updated subtitle to "Act III · Building and Reflecting." Added "Story So Far" slide with three-act recap and Session 3 callback. Replaced "Next Week" slide with two-slide Bridge Forward sequence: eleven-session arc summary + narrative prompt for Demo Day presentations.
- ✅ `notebook.ipynb` — Updated title cell to "Iterate and Polish" with Act III subtitle and narrative connection to Session 10. Updated Challenge cell with arc framing and bridge to Session 12 ("Which concepts from this course showed up in your work?").
- ✅ `BETWEEN-SESSION.md` — Added "Looking Ahead" section bridging to Session 12's Demo Day with narrative prompt (which course concepts showed up in your work?). Updated "Bring It Back" with stronger narrative framing.
- ✅ `README.md` — Rewritten with "Iterate and Polish" title, narrative role section, connections section (builds on Session 10, calls back to Session 3, bridges to Session 12).
- ✅ `GUIDE-research-presentation.md` — Added fifth bullet to "What DOES Make a Presentation Good": connection to the course story (which concepts showed up in your work?). Footer already correct.
- ✅ `peer-feedback-form.md` — Added second prompt to Research Connection section: "Can you spot any course concepts in this Space?" with concept list.
- ✅ Google Classroom — Already correct. Topic name "Session 11: Iterate and Polish", material titles "Session 11 Slides: Iterate and Polish" and "Session 11 Notebook: Iterate and Polish" — no changes needed.

**Unchanged (already strong):**
- SpaceCraft Check-In, Quick Demos, Research Journey Review, 1-on-1 Feedback rotation
- Peer Testing workflow, Notebook Time debug challenges, Prep for Demo Day format
- All code (notebook debug challenges, improvement checklist)
- What Could Go Wrong table, Key Vocabulary
- Demo Day 5-part presentation format (structure unchanged; narrative prompt added to guide)

### Session 12: Demo Day — PENDING
**What needs to happen:**
- Add narrative framing to presentation and reflection session
- Ensure the narrative prompt ("How does your project connect to the bigger story?") is reflected in the session materials

---

## The Space Build Progression

Each session has an `app.py` and `requirements.txt` that can be deployed as a Hugging Face Space. These builds serve a dual purpose: (1) teach the Space-building pattern students will use in Session 10, and (2) create a working artifact that demonstrates the session's concept.

| Session | Space Built | What It Demonstrates | Build Type |
|---------|------------|---------------------|------------|
| 1 | Mood Meter | Input → Model → Output (classification) | Instructor pre-builds, shows Files tab |
| 2 | Emotion Spectrum | Different models = different outputs | Instructor shows multi-model comparison |
| 3 | Sarcasm Breaker | Cleaning fixes noise, not meaning (the old paradigm) | **Live build**: add clean_text() to Session 1 code |
| 4 | Text Generator | Classification → Generation (the fork) | **Live build**: change one line from Session 1 |
| 5 | Text Playground | Hyperparameters control generation (temperature, top-p) | **Live build**: add sliders to Session 4 code |
| 7 | Bias Tester | Bias in classification | TBD |
| 8 | Image Story Pipeline | Multi-model pipeline + error cascades | TBD |
| 9 | Restaurant Review Analyzer | Prompt engineering + UX design | TBD |
| 10 | Student's own Space | Everything they've learned | **Student build** |

The progression: Sessions 1–2 show pre-built Spaces (students observe). Sessions 3–5 build Spaces live (students watch and learn the pattern). Sessions 7–9 build more complex Spaces. Session 10 is where students build their own.

---

## The Narrative Arc as Students Experience It

| Session | What Students Do | What They Learn | Narrative Beat |
|---------|-----------------|-----------------|----------------|
| 1 | Feed text to a mood-reading model | Input → Model → Output | "Here's what AI can do." |
| 2 | Compare three emotion models | Training data shapes what a model can see | "Different models see different things." |
| 3 | Break models with adversarial stories | Classical ML has fundamental limits | "These models don't understand. They pattern-match." |
| 4 | Build a text generator, compare to classifiers | Classification vs. Generation; labels vs. text | "There are two kinds of AI: sorting and creating." |
| 5 | Build a text generator with sliders | Hyperparameters control generation | "These are the same knobs on ChatGPT." |
| 6 | Test models outside their training domain | Models can't generalize beyond their data | "This was the wall. The breakthrough was training on everything." |
| 7 | Test a model for bias with name/gender swaps | Scale amplifies bias | "Training on everything means training on every bias too." |
| 8 | Chain two models into a pipeline | Errors cascade through multi-model systems | "Every AI product you use is a pipeline like this." |
| 9 | Redesign a demo into a useful tool | The human layer matters as much as the model | "You can't retrain GPT-4, but you can design how people use it." |
| 10 | Build their own Space from scratch | Supervised learning and task design | "Now you build. Everything you learned is in here." |
| 11 | Peer testing and iteration | The experimentation loop | "Good AI products come from testing and improving." |
| 12 | Present their research journey | Reflection and portfolio | "Here's the story of what I built and what I learned." |

---

## Connections to Existing Bonus Materials

### bonus-bert-content-moderation
BERT (2018) is the bridge between classical ML and generative AI. It introduced pretraining + fine-tuning. The content moderation angle connects to Session 7 (bias). Consider assigning as optional reading between Sessions 6 and 7.

### bonus-fine-tuning
The nostalgia fine-tuning notebook demonstrates supervised learning (Session 10). Also shows the old paradigm (fine-tune a small model on labeled data) vs. the generative paradigm (prompt a massive pre-trained model).

### bonus-hugging-face-spaces
The Story Arc Spaces (3-sentiment, 6-emotion, 7-Ekman, 28-GoEmotions) are central to the revised Session 3. Other bonus Spaces (Image Color Mood, Emoji Mood Translator, Audio Emotion Detector, Headline Dashboard) can be used for SpaceCraft check-ins throughout the course.

### ADVERSARIAL-STORIES.md (in bonus-hugging-face-spaces)
Three adversarial test stories (sarcastic narrator, mixed emotions, nature with no humans) are ready to paste into Story Arc Spaces for Session 3. Also reused in Session 4's text generation exploration.

---

## Open Questions

1. **How explicit to make the history.** Should the narrative name specific milestones (BERT 2018, GPT-2 2019, ChatGPT 2022) or keep it conceptual? For middle/high schoolers, dates and names might feel like a history lecture. The concepts might land better as a story: "People tried X, it hit a wall, so they tried Y."

2. **Student topics.** Session 3 now includes topic elicitation. How do student-chosen topics interact with the narrative? If a student wants to explore image generation and another wants to explore translation, the narrative needs to be flexible enough to accommodate both.

3. **Pacing.** The revised Sessions 3 and 4 are tight. The narrative framing lives in the 2-3 minutes of framing at the start and end of each segment, not in new activities. Sessions 5–9 revisions should follow the same principle: add narrative framing to existing segments, don't add new segments.

4. **Session 4 notebooks.** The notebook.ipynb and explorer.ipynb still reflect the old Sentiment Showdown concept. They need to be rewritten for text generation experiments. Not urgent — the instructor guide and slides are what drive the live session.

5. **COURSE-STRUCTURE.md.** Needs to be rewritten to reflect the narrative arc. Should happen after Sessions 3–4 are tested live.

---

## Next Steps

1. ~~Revise Session 3 folder~~ ✅ Complete.
2. ~~Decide on Session 4~~ ✅ Classification vs. Generation confirmed and built.
3. **Teach Session 3 on Saturday (March 22)** — test the adversarial stories live. Take notes on student topics. Note what works and what doesn't in the new 2-hour structure.
4. **Rewrite Session 4 notebooks** — notebook.ipynb and explorer.ipynb need to match the new classification vs. generation concept.
5. **Teach Session 4 the following Saturday** — test the live build (classification → generation code change). Note whether students grasp the fork.
6. ~~Revise Session 5~~ ✅ Complete. Narrative framing added; live build reframed as Session 4 → Session 5 progression; bridge forward to Session 6 added.
7. ~~Revise Session 6~~ ✅ Complete. Narrative framing added: "Story So Far" bridge from Session 5, breakthrough moment (pretraining on everything, BERT 2018), bridge forward to Session 7 (bias as cost of scale). Bonus-bert-content-moderation linked as supplementary reading.
8. ~~Revise Session 7~~ ✅ Complete. Narrative framing added: "Story So Far" bridge from Session 6, breakthrough-cost connection in Name the Concept, bridge forward to Session 8 (error cascades). Google Classroom updated to match local files.
9. ~~Revise Session 8~~ ✅ Complete. Narrative framing added: "Story So Far" bridge from Session 7, real-world product connection (ChatGPT content filter, Midjourney safety classifier), Act II closer ("You now know what's inside the machine"). Google Classroom updated to match local files.
10. ~~Revise Session 9~~ ✅ Complete. Act III opener framing added: "Story So Far" three-act bridge, real-world connection ("most accessible skill in AI"), Bridge Forward to Session 10. Google Classroom updated to match local files.
11. ~~Revise Session 10~~ ✅ Complete. Synthesis framing added: "Story So Far" three-act bridge, updated recap table with correct Space names, real-world connection ("every AI product started like this"), Bridge Forward to Session 11 (experimentation loop). Google Classroom needs manual update (page failed to load during revision).
12. ~~Revise Session 11~~ ✅ Complete. Narrative framing added: "Story So Far" three-act bridge with Session 3 callback, real-world connection (iteration in shipping products), Bridge Forward to Session 12 (narrative prompt: "How does your project connect to the bigger story?"). Concept Review table added (Sessions 1–11). Presentation guide and peer feedback form updated with narrative prompts. Google Classroom already correct.
13. **Revise Session 12** — Add narrative framing to Demo Day. Ensure the narrative prompt is reflected in session materials.
14. **Update Google Classroom for Session 10** — Rename topic to "Session 10: Build Your Own from Scratch." Update material titles to match.
15. **Rewrite COURSE-STRUCTURE.md** after the first 4–5 sessions are tested live.

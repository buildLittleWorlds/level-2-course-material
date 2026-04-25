# AI + Research Level 2: Applied Machine Learning Concepts

**12 Sessions | 2 Hours Each | Grades 7-11**

Students learn machine learning concepts through guided interaction with pre-trained AI models. Each session pairs conceptual framing with hands-on model experimentation using Hugging Face pipelines and Gradio interfaces. Students also learn a formal research method each week, building a portable methodology toolkit across the course.

Alongside the technical content, students develop a public-facing research presence. In the AI world, a GitHub profile linked to a Hugging Face profile is the standard public face of someone doing research and applied work. **GitHub** is where the writing, the paper, and the project READMEs live; **Hugging Face** is where the experiments live — Spaces, Collections, model comparisons. Linking them turns a scatter of repos and Spaces into a coherent research identity.

Students maintain five ongoing artifacts: a **Hugging Face Collection** (curated models and Spaces), a series of **Spaces they built** (baseline → domain-specific → ambitious), a **Research Journal** with weekly entries, a **research paper** grounded in their Space work, and a **GitHub profile README** that links it all together.

---

## Course Structure

The course is organized into four arcs:

**Exploration Arc (Sessions 1-3):** Students discover AI tools, learn the basic inference pipeline, and begin investigating how training data and input quality shape model behavior.

**Evaluation Arc (Sessions 4-6):** Students encounter the distinction between classification and generation, learn to control model behavior through hyperparameters, and test model performance across domains to reveal overfitting and generalization limits. Session 6 is the pivot from building to investigating: students formulate a real research question grounded in their own work and domain.

**Bias, Systems, and Paper Arc (Sessions 7-8):** Students investigate bias in AI systems through systematic paired testing, then build multi-model pipelines that reveal how errors cascade through chained systems. These technical investigations feed directly into a research paper: Session 7 introduces the prompt-first paper-drafting workflow, and Session 8 has students adapt a parallel-example packet to make the paper genuinely their own (Anchor / Voice / Stretch). Session 8 also begins the GitHub profile README — students start building the public-facing research-presence page that will host their paper, Spaces, and Collection by the end of the course.

**Project Arc (Sessions 9-12):** Students redesign AI tools for real audiences, read one source carefully enough to cite, build an independent ambitious Space, iterate through peer feedback, and present their research journey at Demo Day with their full GitHub + Hugging Face profile as the front door.

---

## Session Descriptions

### Session 1: From Rules to Models

*The INPUT → MODEL → OUTPUT pattern and why rule-based systems fail at scale.*

Students explore working AI tools (sentiment analysis, image captioning, audio emotion detection) and discover that hand-written rules cannot capture the complexity these models handle. Introduces the basic inference pipeline and model-as-abstraction. Students set up Hugging Face accounts and begin their first Collection.

**ML Concepts:** Deterministic vs. probabilistic systems, model inputs/outputs, inference pipeline
**Hands-On:** Explore 6 pre-built AI Spaces, examine `app.py` source code, run first Colab notebook

---

### Session 2: Data Collection and Representation

*How training data composition determines what a model can and cannot detect.*

Students run three sentiment models on identical inputs and discover that different training datasets (movie reviews, tweets, product reviews) produce fundamentally different label taxonomies and behaviors. Introduces model cards as documentation of data provenance. Students read and compare model cards, then begin a Research Journal and model-focused Collection.

**ML Concepts:** Structured vs. unstructured data, encoding choices, representation and label taxonomy, data provenance
**Research Method:** Comparative Analysis
**Hands-On:** Side-by-side model comparison Space, model card analysis, Colab multi-pipeline exercises

---

### Session 3: Data Cleaning and Feature Engineering

*What happens when models receive messy, ambiguous, or adversarial inputs — and what that reveals about feature limitations.*

Students feed deliberately problematic inputs to sentiment models and classify failures into three categories: tone deafness (model misses meaning present in the input), emotional flattening (model oversimplifies complex meaning), and anthropomorphic projection (model invents meaning not present). Introduces AI-assisted coding via the CLEAR prompting framework.

**ML Concepts:** Data quality, noise vs. signal, missing context, edge cases, adversarial inputs, feature limitations
**Research Method:** Adversarial Testing
**Hands-On:** Live-build a news headline analysis Space (API integration), zero-shot classification with custom categories, Colab adversarial testing exercises

---

### Session 4: Introduction to Supervised Learning — Classification vs. Generation

*The fundamental distinction between discriminative and generative models, and why it matters.*

Students change one line of code — `pipeline("sentiment-analysis")` to `pipeline("text-generation")` — and encounter a fundamentally different kind of model. The session teaches how classification requires labeled training data (expensive, limited) while generation requires only raw text (abundant), and why this difference enabled the development of large language models. Includes the accuracy paradox (95% accuracy, 0% recall) to introduce false positives/negatives.

**ML Concepts:** Labels and supervision, classification vs. generation, training data requirements, false positives/negatives, next-word prediction, parameter counts
**Research Method:** Baseline Comparison (classifier output vs. generator output vs. human judgment)
**Hands-On:** Live-build a text generator Space (distilgpt2), model card comparison (classification vs. generation), Colab pipeline switching exercises

---

### Session 5: Model Training and Parameters

*Hyperparameters as runtime controls on model behavior, and systematic experimentation to understand their effects.*

Students add temperature, top-p, and max-length controls to their text generator and conduct controlled experiments — changing one variable at a time and documenting results. Connects directly to how commercial AI APIs (ChatGPT, Claude) expose the same parameters to developers. Introduces the distinction between learned parameters (weights) and user-controlled hyperparameters.

**ML Concepts:** Hyperparameters vs. parameters, temperature and sampling, top-p (nucleus sampling), model complexity, optimization intuition
**Research Method:** Parameter Sweep / Experimental Design
**Hands-On:** Live-build a controlled text generator Space with sliders, systematic parameter sweeps, Colab experimentation notebook

---

### Session 6: Model Evaluation, Generalization, and the Research Question

*Testing model performance across domains to reveal overfitting and the limits of training data — and using that work to formulate a real research question.*

Students test sentiment models on text from 11 different domains (news, tweets, legal, medical, poetry, code comments, memes, etc.) and discover systematic failures when models encounter text outside their training distribution. Introduces overfitting and domain shift. Includes the key historical insight: pretraining on large diverse corpora (BERT, 2018) as the field's response to the generalization problem. Session 6 is also the pivot point of the course: students move from building to investigating, formulating a research question grounded in their own interests and the domain boundary their tools live inside. Every research question lives in a domain, and the boundary between a model's domain and a student's domain is where the interesting findings live.

**ML Concepts:** Overfitting, domain shift, memorization vs. learning, generalization, distribution mismatch, pretraining
**Research Method:** External Validity / Generalization Testing
**Hands-On:** Domain Safari (structured multi-domain evaluation), model-to-training-data analysis, pattern recognition across 11 domain types, research-question formulation, Colab evaluation notebook

---

### Session 7: Bias, Variance, and Uncertainty — and the Paper Draft

*Systematic testing for differential treatment across populations and the sources of bias in training data — and turning that evidence into a rough paper draft.*

Students build a tool that runs paired sentences through sentiment models — changing only a name, gender, or demographic marker — and measure whether scores shift based on identity alone. Connects dataset bias to real-world consequences (resume screening, healthcare allocation, loan decisions). Introduces `gr.Blocks` layout for more complex interface design. The session closes with the prompt-first paper-drafting workflow: students use the master `PAPER-TEMPLATE.md` AI prompt to generate a rough `PAPER.md` from their journal evidence and Space outputs, with the fairness audit becoming the natural seed for the paper's limitations section — *who might this tool work less well for, and what part of training data or design is shaping that?*

**ML Concepts:** Dataset bias, model bias, systematic unfairness, variance across populations, confidence without accuracy
**Research Method:** Fairness Audit / Algorithmic Bias Testing
**Hands-On:** Live-build a paired-sentence bias testing Space, systematic name/gender/role swap experiments, Colab bias analysis notebook, prompt-first paper drafting from journal evidence (`PAPER.md` v1)

---

### Session 8: From Single Models to Systems — Make the Paper Yours and Start a Profile

*Multi-model pipelines, component dependencies, and how errors propagate through chained systems — and the move from a generic paper draft to one anchored in the student's own work and a public-facing GitHub research profile.*

Students chain an image captioning model (BLIP) with an emotion/sentiment detection model and discover error cascades: when the captioner generates an incorrect description, the second model confidently analyzes the wrong text. This is the most complex build in the course — two models, image input, multi-step processing. Students diagram pipeline dependencies and identify failure points. The error-propagation work feeds directly into the paper's limitations section: if a student's project chains anything, that's where errors compound silently. Each student also receives a parallel-example packet (a five-file starter draft built around their own research question), copies it into their own GitHub account via "Use this template," and begins the **Anchor** move — opening their actual Space, running one real test, and swapping the result into section 4 of `PAPER.md`. Session 8 closes with a walk through a worked-example GitHub research profile, framing the GitHub-and-Hugging-Face linkage as the standard public face of someone doing AI work and starting students on their own profile README.

**ML Concepts:** Multi-model pipelines, system dependencies, error propagation, failure points, modular architecture
**Research Method:** Error Propagation / Systems Testing (applied to the paper's limitations section)
**Hands-On:** Live-build an image-to-emotion pipeline Space (BLIP + sentiment detector), deliberate pipeline breaking with abstract/ambiguous images, Colab systems analysis notebook, parallel-example template-copy walkthrough, in-class Anchor work on `PAPER.md`, GitHub profile README starter

---

### Session 9: Prompt Logic and Human-AI Interaction

*How interface design and prompt structure transform the same model into different tools for different audiences — and reading one source carefully enough to cite it.*

Students take a bare sentiment analysis demo and redesign it for a specific audience (restaurant owner, journal keeper, email writer, social media manager). The underlying model does not change; the prompts, labels, examples, and output framing change everything. Teaches that human design decisions are a critical layer in any AI system. Session 9 also begins the careful-paper-reading work: students pick one source from their Week 7 shortlist and read it with AI as a guarded reading partner — abstract and methods walked through with AI assistance, results and limitations read independently — producing a one-paragraph claim they could actually cite in their paper.

**ML Concepts:** Prompt engineering, instruction framing, interaction design, context shaping model behavior
**Research Method:** User-Centered Design / Usability Testing; Careful Reading
**Hands-On:** Live interface redesign demonstration, students build audience-specific tool from templates, Colab prompt experimentation notebook, structured paper-reading exercise

---

### Session 10: System Integration — Independent Build

*Students select a model, define a task, and build a complete AI tool independently — the ambitious Space.*

Students choose from a curated list of CPU-compatible models spanning text classification, zero-shot classification, text generation, summarization, named entity recognition, translation, image classification, and image captioning. They define the problem, audience, and evaluation criteria, then build and deploy a working Hugging Face Space. Continued paper revision and profile-README iteration run in parallel.

**ML Concepts:** Task design, model selection, supervised learning in practice, deployment considerations
**Hands-On:** Hub browsing and model evaluation, student project pitches, independent build time, Space deployment, paper revision check-in

---

### Session 11: Iteration, Testing, and Refinement

*Systematic improvement through peer feedback, edge-case testing, and the experimentation loop.*

Students exchange Spaces with peers, attempt to break each other's tools (applying Session 3's adversarial testing methods), and improve through structured feedback. The session reinforces that building is iterative — no system works correctly on the first attempt. Students finalize their paper revisions, polish their profile READMEs, and prepare their research presentations.

**ML Concepts:** The experimentation loop, edge-case analysis, iterative refinement, debugging as methodology
**Research Method:** Peer Review / Systematic Testing
**Hands-On:** Peer testing rotation, structured feedback forms, debugging and improvement cycle, presentation preparation, profile-README polish

---

### Session 12: Methodological Reflection and Portfolio Presentation

*Students present their research journey, demonstrate their tools, and compile a portfolio of work.*

Each student delivers a 5-part research presentation: My Question, My Journey, My Artifact (live Space demo), What I Found, and What's Next. The session synthesizes all 11 ML concepts and 9 research methods covered across the course. The student's GitHub profile README serves as the front door — linking the paper, the Spaces, the Collection, and the Hugging Face profile into a single coherent research presence.

**Deliverables:** Research presentation, working AI tool (Hugging Face Space), curated Hugging Face Collection, research journal, research paper, GitHub profile README linked to Hugging Face profile

---

## Research Methods Across the Course

| Session | ML Concept | Research Method |
|---------|-----------|----------------|
| 1 | Inference Pipelines | — |
| 2 | Training Data & Representation | Comparative Analysis |
| 3 | Data Cleaning & Feature Engineering | Adversarial Testing |
| 4 | Classification vs. Generation | Baseline Comparison |
| 5 | Hyperparameters | Parameter Sweep |
| 6 | Overfitting, Domain Shift, & Research-Question Formulation | Generalization Testing |
| 7 | Bias in AI / Paper Drafting | Fairness Audit |
| 8 | Multi-Model Systems / Anchor-Voice-Stretch / Profile-README Start | Error Propagation |
| 9 | Prompt Engineering & Human-AI Interaction / Careful Reading | User-Centered Design |
| 10 | Task Design & Model Selection | End-to-End System Design |
| 11 | The Experimentation Loop | Peer Review |
| 12 | Reflection & Portfolio | — |

---

## Delivery

- **Format:** Live Zoom sessions, 2 hours each
- **Platforms:** Hugging Face (models, Spaces, Collections), GitHub (paper, profile, journal, code), Google Classroom (assignments and materials)
- **Instructor tools:** Reveal.js slide decks served via GitHub Pages, live-coded Gradio demos, pre-built Hugging Face Spaces under `profplate/`
- **Student tools:** Free Hugging Face account, GitHub account, AI assistant (Claude or ChatGPT), Google account (for Classroom)
- **Colab notebooks:** Each session folder includes a `notebook.ipynb` as enrichment for projects that benefit from a notebook walkthrough — model comparisons, embedding visualizations, fine-tuning experiments. Pulled into class on a per-student, per-need basis.

## What Students Produce

By the end of the course, each student has:

- A **Hugging Face Collection** of 12+ models and Spaces with annotations explaining what each does and why it was selected
- **Spaces they built** — a baseline Space, a domain-specific Space, and an ambitious Space, all deployed and linked from their profile
- A **Research Journal** with entries applying 9 formal research methods to AI tools
- A **research paper** (`PAPER.md`) grounded in their own Space work, anchored to a real test, written in their own voice, with honest limitations
- A **GitHub profile README** linked to their Hugging Face profile — the public-facing research-presence page that hosts the paper, Spaces, Collection, and "what I'm building now"
- A **research presentation** connecting their question, methodology, tool, findings, and next steps

## File Organization

This repository contains everything needed to teach the course:

- `CURRICULUM.md` — This document (course overview for stakeholders)
- `README.md` — Public-facing overview
- `PAPER-TEMPLATE.md` — Master AI prompt students paste to generate a paper draft from their journal and Space evidence
- `GUIDE-FROM-SPACE-TO-PAPER.md` — End-to-end paper workflow guide
- `session-01/` through `session-12/` — Complete session materials (READMEs, slides, notebooks, between-session work, method guides, Space code)
- `bonus-hugging-face-spaces/` — Build guides, cheat sheets, leaderboard of example Spaces, showcase pages

The Bluest Hour project at <https://github.com/buildLittleWorlds/bluest-hour> serves as the running exemplar — students see how a real journal becomes a real paper. Per-cohort student materials (parallel-example packets, instructor planning) live outside the public repo.

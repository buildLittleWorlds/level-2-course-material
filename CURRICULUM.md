# AI + Research Level 2: Applied Machine Learning Concepts

**12 Sessions | 2 Hours Each | Grades 7-11**

Students learn machine learning concepts through guided interaction with pre-trained AI models. Each session pairs conceptual framing with hands-on model experimentation using Hugging Face pipelines, Gradio interfaces, and Google Colab notebooks. Students also learn a formal research method each week, building a portable methodology toolkit across the course.

Students maintain three ongoing artifacts: a Hugging Face Collection (curated models and Spaces), a Research Journal (weekly entries documenting their investigations), and a GitHub portfolio of notebooks and code.

---

## Course Structure

The course is organized into four arcs:

**Exploration Arc (Sessions 1-3):** Students discover AI tools, learn the basic inference pipeline, and begin investigating how training data and input quality shape model behavior.

**Evaluation Arc (Sessions 4-6):** Students encounter the distinction between classification and generation, learn to control model behavior through hyperparameters, and test model performance across domains to reveal overfitting and generalization limits.

**Advanced Arc (Sessions 7-8):** Students investigate bias in AI systems through systematic paired testing and build multi-model pipelines that reveal how errors cascade through chained systems.

**Project Arc (Sessions 9-12):** Students redesign AI tools for real audiences, build an independent project from scratch, iterate through peer feedback, and present their research journey.

---

## Session Descriptions

### Session 1: From Rules to Models

*The INPUT → MODEL → OUTPUT pattern and why rule-based systems fail at scale.*

Students explore working AI tools (sentiment analysis, image captioning, audio emotion detection) and discover that hand-written rules cannot capture the complexity these models handle. Introduces the basic inference pipeline and model-as-abstraction. Students set up Hugging Face accounts and begin their first Collection.

**ML Concepts:** Deterministic vs. probabilistic systems, model inputs/outputs, inference pipeline
**Hands-On:** Explore 6 pre-built AI Spaces, examine app.py source code, run first Colab notebook

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

### Session 6: Model Evaluation and Generalization

*Testing model performance across domains to reveal overfitting and the limits of training data.*

Students test three sentiment models on text from 11 different domains (news, tweets, legal, medical, poetry, code comments, memes, etc.) and discover systematic failures when models encounter text outside their training distribution. Introduces overfitting and domain shift. Includes the key historical insight: pretraining on large diverse corpora (BERT, 2018) as the field's response to the generalization problem.

**ML Concepts:** Overfitting, domain shift, memorization vs. learning, generalization, distribution mismatch, pretraining
**Research Method:** External Validity / Generalization Testing
**Hands-On:** Domain Safari (structured multi-domain evaluation), model-to-training-data analysis, pattern recognition across 11 domain types, Colab evaluation notebook

---

### Session 7: Bias, Variance, and Uncertainty

*Systematic testing for differential treatment across populations and the sources of bias in training data.*

Students build a tool that runs paired sentences through sentiment models — changing only a name, gender, or demographic marker — and measure whether scores shift based on identity alone. Connects dataset bias to real-world consequences (resume screening, healthcare allocation, loan decisions). Introduces `gr.Blocks` layout for more complex interface design.

**ML Concepts:** Dataset bias, model bias, systematic unfairness, variance across populations, confidence without accuracy
**Research Method:** Fairness Audit / Algorithmic Bias Testing
**Hands-On:** Live-build a paired-sentence bias testing Space, systematic name/gender/role swap experiments, Colab bias analysis notebook

---

### Session 8: From Single Models to Systems

*Multi-model pipelines, component dependencies, and how errors propagate through chained systems.*

Students chain an image captioning model (BLIP) with a sentiment analysis model and discover error cascades: when the captioner generates an incorrect description, the sentiment model confidently analyzes the wrong text. This is the most complex build in the course — two models, image input, multi-step processing. Students diagram pipeline dependencies and identify failure points.

**ML Concepts:** Multi-model pipelines, system dependencies, error propagation, failure points, modular architecture
**Research Method:** Error Propagation / Systems Testing
**Hands-On:** Live-build an image-to-sentiment pipeline Space (BLIP + sentiment), deliberate pipeline breaking with abstract/ambiguous images, Colab systems analysis notebook

---

### Session 9: Prompt Logic and Human-AI Interaction

*How interface design and prompt structure transform the same model into different tools for different audiences.*

Students take a bare sentiment analysis demo and redesign it for a specific audience (restaurant owner, journal keeper, email writer, social media manager). The underlying model does not change; the prompts, labels, examples, and output framing change everything. Teaches that human design decisions are a critical layer in any AI system.

**ML Concepts:** Prompt engineering, instruction framing, interaction design, context shaping model behavior
**Research Method:** User-Centered Design / Usability Testing
**Hands-On:** Live interface redesign demonstration, students build audience-specific tool from templates, Colab prompt experimentation notebook

---

### Session 10: System Integration — Independent Build

*Students select a model, define a task, and build a complete AI tool independently.*

Students choose from a curated list of CPU-compatible models spanning text classification, zero-shot classification, text generation, summarization, named entity recognition, translation, image classification, and image captioning. They define the problem, audience, and evaluation criteria, then build and deploy a working Hugging Face Space.

**ML Concepts:** Task design, model selection, supervised learning in practice, deployment considerations
**Hands-On:** Hub browsing and model evaluation, student project pitches, 40 minutes of independent build time, Space deployment

---

### Session 11: Iteration, Testing, and Refinement

*Systematic improvement through peer feedback, edge-case testing, and the experimentation loop.*

Students exchange Spaces with peers, attempt to break each other's tools (applying Session 3's adversarial testing methods), and improve through structured feedback. The session reinforces that building is iterative — no system works correctly on the first attempt. Students prepare their research presentations.

**ML Concepts:** The experimentation loop, edge-case analysis, iterative refinement, debugging as methodology
**Research Method:** Peer Review / Systematic Testing
**Hands-On:** Peer testing rotation, structured feedback forms, debugging and improvement cycle, presentation preparation

---

### Session 12: Methodological Reflection and Portfolio Presentation

*Students present their research journey, demonstrate their tools, and compile a portfolio of work.*

Each student delivers a 5-part research presentation: My Question, My Journey, My Artifact (live Space demo), What I Found, and What's Next. The session synthesizes all 11 ML concepts and 9 research methods covered across the course.

**Deliverables:** Research presentation, working AI tool (Hugging Face Space), curated model Collection, research journal, GitHub portfolio

---

## Research Methods Across the Course

| Session | ML Concept | Research Method |
|---------|-----------|----------------|
| 1 | Inference Pipelines | — |
| 2 | Training Data & Representation | Comparative Analysis |
| 3 | Data Cleaning & Feature Engineering | Adversarial Testing |
| 4 | Classification vs. Generation | Baseline Comparison |
| 5 | Hyperparameters | Parameter Sweep |
| 6 | Overfitting & Domain Shift | Generalization Testing |
| 7 | Bias in AI | Fairness Audit |
| 8 | Multi-Model Systems | Error Propagation |
| 9 | Prompt Engineering & Human-AI Interaction | User-Centered Design |
| 10 | Task Design & Model Selection | End-to-End System Design |
| 11 | The Experimentation Loop | Peer Review |
| 12 | Reflection & Portfolio | — |

---

## Delivery

- **Format:** Live Zoom sessions, Saturday evenings 8-10 PM EST
- **Platforms:** Google Classroom (assignments and materials), Google Colab (notebooks), Hugging Face (models and Spaces), GitHub (code portfolios)
- **Instructor tools:** Reveal.js slide decks served via GitHub Pages, live-coded Gradio demos, pre-built Hugging Face Spaces under `profplate/`
- **Student tools:** Free Hugging Face account, Google account (for Colab and Classroom), GitHub account

## What Students Produce

By the end of the course, each student has:

- A **Hugging Face Collection** of 12+ models and 7+ Spaces with annotations explaining what each does and why it was selected
- A **Research Journal** with entries applying 9 formal research methods to AI tools
- A **working AI tool** (Hugging Face Space) designed, built, tested, and presented independently
- A **GitHub portfolio** of Colab notebooks documenting experiments across the course
- A **research presentation** connecting their question, methodology, tool, findings, and next steps

## File Organization

This folder contains everything needed to teach the course:

- `CURRICULUM.md` — This document (course overview for stakeholders)
- `COURSE-STRUCTURE.md` — Detailed reference for how sessions and files are organized
- `README.md` — Public-facing overview with Colab notebook links
- `supplementary-datasets.md` — Curated Hugging Face datasets organized by session
- `start-here/` — Student onboarding guides (Hugging Face, GitHub, Colab, Gradio)
- `session-01/` through `session-12/` — Complete session materials (instructor guides, slides, notebooks, student guides, homework, Space code)
- `bonus-fine-tuning/` — Optional fine-tuning example
- `bonus-bert-content-moderation/` — Optional BERT supplement
- `bonus-hugging-face-spaces/` — Extra Spaces for demonstrations and build guides

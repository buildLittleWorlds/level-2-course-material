# Phase 4: Build Your Own Research Space — Project Briefs

## Overview

You have read the QED-Nano paper, explored the artifacts on the Hub, and experimented with the Proof Explorer Space. Now you build something of your own.

Each project below requires you to understand a specific aspect of the research and build a Hugging Face Space that investigates it. Choose one. Your finished Space should be something another person can use to learn something about how AI handles mathematical reasoning.

**What "done" looks like:** A deployed Hugging Face Space with a working interface, a clear purpose, and at least a short description (in the Space or in the About tab) explaining what the Space does and what it helps users understand.

---

## Project A: Before-and-After Comparison

**Difficulty:** Moderate

### The Research Question

QED-Nano was built by fine-tuning Qwen3-4B-Thinking — a general-purpose model — on mathematical proof data. The base model scored about 20% on proof benchmarks; QED-Nano scored 40%. What exactly did the training change? Can you *see* the difference?

### What You Build

A Space that takes a math problem and sends it to **both** QED-Nano and its base model (Qwen3-4B-Thinking) via the Inference API. The Space displays both outputs side by side so the user can compare them.

### Technical Requirements

- Two Inference API calls per problem (one for each model)
- Side-by-side display of outputs (use Gradio columns or tabs)
- A dropdown or text box for entering problems
- At least 4 example problems at different difficulty levels
- A brief explanation in the interface telling the user what they're looking at and why the comparison matters

### What You Need to Understand

You need to understand what fine-tuning does — that it changes a model's behavior without changing its size. You should be able to explain, based on what users see in your Space, what the QED-Nano training actually improved.

### Level 2 Skills Used

- Inference API calls (like the Proof Explorer, but now two models)
- Model comparison pattern (Session 4)
- Gradio layout with columns or tabs (Sessions 5, 9)
- Writing clear interface text (Session 9)

### Getting Started

1. Look at the Proof Explorer `app.py` to see how it calls the Inference API
2. Set up a second `InferenceClient` for `Qwen/Qwen3-4B-Thinking`
3. Create a function that calls both models and returns both results
4. Build a Gradio interface that shows the results side by side

---

## Project B: Proof Rubric Tool

**Difficulty:** Moderate to Ambitious

### The Research Question

The QED-Nano researchers didn't just check whether proofs were right or wrong. They built a detailed rubric that scores proofs on multiple criteria: logical structure, step validity, completeness, and notation. This rubric-based approach was a key innovation. Can you build a tool that does something similar?

### What You Build

A Space where a user pastes a mathematical proof (or generates one from QED-Nano) and evaluates it on a rubric. The evaluation can be:

- **Human only:** Checkboxes and rating scales the user fills in themselves
- **AI-assisted:** The Space sends the proof to an LLM and asks it to evaluate each rubric criterion
- **Both:** The user scores it AND the AI scores it, and the Space shows where they agree or disagree

### Technical Requirements

- A text input for the proof (or integration with QED-Nano to generate one)
- A rubric with at least 3 evaluation criteria (you design these)
- A display showing the scores and any explanations
- A brief description explaining what the rubric measures and why this approach matters

### What You Need to Understand

You need to understand why rubric-based evaluation is better than pass/fail for training. Read the "Training Prompts and Grading Schemes" section of the paper. Think about how this connects to how your own writing gets evaluated — a teacher doesn't just say "right" or "wrong"; they give feedback on specific aspects.

### Level 2 Skills Used

- Gradio form elements: sliders, checkboxes, radio buttons (Sessions 5, 9)
- Inference API for AI-assisted scoring
- UI design for evaluation tools (Session 9)
- The "LLM-as-judge" pattern — using one model to evaluate another's output

### Getting Started

1. Design your rubric first. Start with 3 criteria. Here are suggestions (but you can choose your own):
   - **Does each step follow logically from the previous one?** (1–5 scale)
   - **Is the proof complete, or are there gaps?** (1–5 scale)
   - **Does the proof reach a clear conclusion?** (Yes / Partially / No)
2. Build the Gradio interface with the rubric inputs
3. If doing AI-assisted scoring, write a prompt that asks the AI to evaluate the proof on each criterion and explain its reasoning

---

## Project C: Training Data Explorer

**Difficulty:** Accessible

### The Research Question

The researchers carefully curated their training data — filtering out problems with diagrams, discarding trivial entries, and checking for quality. What does AI training data actually look like? Can you make it browsable and understandable?

### What You Build

A Space that loads the FineProofs dataset from the Hub and lets users browse it interactively — searching, filtering, and reading individual entries.

### Technical Requirements

- Load the dataset using the `datasets` library from Hugging Face
- Display entries in a readable format (not raw JSON)
- Include at least one way to filter or search (by keyword, by difficulty if available, or by topic)
- A brief explanation telling users what this dataset is, where it comes from, and why training data matters

### What You Need to Understand

You need to understand why data quality matters for AI training. The paper explains their multi-stage filtering process — removing problems with diagrams, discarding trivial entries, filtering for quality with a secondary AI pass. Your Space helps users see what the result of that filtering looks like.

### Level 2 Skills Used

- Loading data in a Space (similar to how you loaded models, but with `datasets` instead of `pipeline`)
- Gradio data display: tables, textboxes, search bars
- Information design — presenting data in a way that teaches (Session 9)

### Getting Started

1. Install the `datasets` library: add `datasets` to your `requirements.txt`
2. Load the dataset:
   ```python
   from datasets import load_dataset
   ds = load_dataset("lm-provers/FineProofs-RL", split="train")
   ```
3. Explore what fields each entry has (problem statement, solution, difficulty, etc.)
4. Build a Gradio interface that lets users browse through entries

---

## Project D: Difficulty Tester

**Difficulty:** Moderate

### The Research Question

QED-Nano doesn't solve every problem. On easy problems, it performs well. On hard problems, it often fails. Where exactly is the boundary? Can you systematically test the model and map out what it can and can't do?

### What You Build

A Space that feeds QED-Nano a curated set of problems at different difficulty levels, records whether it succeeds or fails (based on your evaluation), and displays the results as a chart or table.

### Technical Requirements

- A predefined set of at least 8–10 problems spanning multiple difficulty levels
- The ability to run QED-Nano on each problem via the Inference API
- A results display showing success/failure by category (chart, table, or both)
- Your criteria for what counts as "success" — write this down in the interface

### What You Need to Understand

You need to understand what an ablation study is — the researchers systematically tested different components of their system to see what contributed to performance. You are doing something similar: systematically testing the model across different difficulty levels to understand its capabilities.

### Level 2 Skills Used

- Inference API (same as Proof Explorer)
- Systematic evaluation methodology (Session 6)
- Data visualization in Gradio (charts, tables)
- Experimental design — choosing test problems and defining success criteria

### Getting Started

1. Create your problem set. Organize problems into categories:
   - Basic (algebra, simple number theory — things you can verify yourself)
   - Intermediate (requires techniques like AM-GM, proof by contradiction)
   - Advanced (Olympiad-level problems from competitions)
2. Define your success criteria. Options include:
   - You read the proof and judge it yourself (most educational but slower)
   - You send the proof to another AI to evaluate (faster, more automated)
   - You check whether the proof reaches a conclusion (simplest)
3. Run QED-Nano on each problem and record results
4. Build a display that shows the pattern

---

## Project E: Reasoning Trace Analyzer

**Difficulty:** Ambitious

### The Research Question

The QED-Nano paper describes "Think-Summarize-Act" cycles: the model periodically pauses its reasoning, summarizes what it has figured out, and then continues. Can you build a tool that makes this reasoning structure visible?

### What You Build

A Space that takes a proof output from QED-Nano and parses it to identify the reasoning structure — highlighting where the model is exploring, where it summarizes, where it tries a new approach, and where it reaches conclusions.

### Technical Requirements

- Generate proof output from QED-Nano (or accept pasted text)
- Parse the output to identify structural elements (reasoning steps, summaries, conclusions, topic shifts)
- Visual display that makes the structure clear — this could be color coding, section labels, a flowchart, or an outline view
- A brief explanation of what "Think-Summarize-Act" cycles are and why they help

### What You Need to Understand

You need to understand how the reasoning cache works — read the relevant section of the paper carefully. The key insight is that long proofs require the model to manage its own reasoning, and the researchers trained it to do this by periodically summarizing. Your Space makes this internal process visible.

### Level 2 Skills Used

- Text parsing in Python (splitting text into sections, identifying patterns)
- Advanced Gradio layout (highlighted text, multiple display panels)
- Inference API for generating proofs
- Understanding of model reasoning processes

### Getting Started

1. Generate several long proof outputs from QED-Nano (use harder problems and high max-token settings)
2. Read the outputs carefully. Look for patterns: does the model use phrases like "So far we have shown..." or "Let us now consider..."? Does it summarize before starting a new approach?
3. Write Python code that identifies these patterns using keyword matching or simple heuristics
4. Build a Gradio interface that displays the parsed structure with visual markers

---

## General Advice for All Projects

**Start small.** Get the simplest possible version working first — even if it's ugly. Then improve.

**Test with real inputs.** Don't assume your Space works until you've tried it with several different problems.

**Write for your audience.** Someone who hasn't read the paper should be able to use your Space and learn something from it. Include enough explanation in the interface that a visitor understands what they're seeing.

**Ask for help.** Use AI assistants to help you debug code, understand error messages, or brainstorm design ideas. That's not cheating — it's the same skill you practiced in Phase 1.

---

*Phase 4 of the "From Paper to Project" module — AI + Research Level 2, Youth Horizons Learning*

# How I Built the Proof Explorer Space

## An Instructor Walkthrough — From Paper to Deployed Space

*This document traces my process building the QED-Nano Proof Explorer, step by step. It's meant to show students (and anyone evaluating this course) what the build process looks like when you apply Level 2 skills to an ambitious project.*

---

## Step 1: Finding the Paper

I came across the QED-Nano blog post on Hugging Face in mid-February 2026. The headline caught my attention: a 4-billion-parameter model approaching the performance of models 30-150x its size on Olympiad-level mathematical proofs.

What interested me wasn't just the technical achievement — it was the *pedagogical* angle. This paper is about teaching a model to reason through arguments. That's what I do as an English and writing professor: I teach students to construct and evaluate arguments. A mathematical proof is just an argument with strict rules.

**The key insight:** This model sits at the intersection of AI, logic, and argumentation — exactly where several intellectual traditions I care about converge.

---

## Step 2: Reading the Model Card

Before writing any code, I went to the model's page on Hugging Face: `lm-provers/QED-Nano`.

Here's what I checked (the same things we teach in Session 2):

- **What task is it trained for?** Text generation — specifically, generating mathematical proofs
- **What was it trained on?** The FineProofs-RL dataset (curated Olympiad problems)
- **What's the base model?** Qwen3-4B-Thinking, fine-tuned in two stages
- **What license?** Apache 2.0 (open, free to use)
- **How big is it?** ~4 billion parameters — too large for a free CPU Space, but available through the Inference API

That last point is important. In Sessions 1-9, we loaded models directly using `pipeline()`. This model is too large for that approach on free hardware. Instead, I used the Hugging Face **Inference API** — which runs the model on Hugging Face's servers and sends back the results. This is the same pattern used by many production applications.

---

## Step 3: Choosing the Approach

I had two options:

**Option A: Load the model locally with `pipeline()`**
- Pro: Simple, follows the exact pattern from Sessions 1-9
- Con: Model is 4B parameters — won't run on free CPU Spaces. Would need a GPU Space (paid).

**Option B: Use the Inference API via `huggingface_hub`**
- Pro: Works on free Spaces, no GPU needed
- Con: Depends on the API being available; slightly different code pattern

I chose **Option B**. This introduced one new concept — calling an API instead of loading a model locally — but everything else (Gradio interface, deployment, testing) stayed the same as what students learn in the course.

---

## Step 4: Writing the Code

The structure follows the pattern from Sessions 5 and 9:

```
app.py
├── Import libraries
├── Set up the model connection (InferenceClient instead of pipeline)
├── Define example inputs
├── Write the generation function
├── Build the Gradio interface with tabs and controls
└── Launch
```

### Key decisions I made:

**1. Example problems at different difficulty levels.**
I curated 8 problems ranging from accessible (divisibility by 6) to hard (Olympiad combinatorics). This matters because students need to be able to follow at least some of the proofs to evaluate them. If every problem is IMO-level, the output is unreadable for most students.

**2. Temperature and max-token sliders.**
Just like Session 5 (the Text Playground), I added controls so users can experiment with how the model generates. Lower temperature produces more focused, conservative proofs. Higher temperature produces more creative but riskier reasoning. This connects directly to the hyperparameters concept from Session 5.

**3. Three tabs, not one.**
- Tab 1: The actual proof generator
- Tab 2: A guide on how to read and evaluate proofs
- Tab 3: Background on what QED-Nano is and why it matters

This follows the Session 9 lesson: a good Space isn't just a model running behind a button — it's designed for an audience. The evaluation guide and background context make this a teaching tool, not just a demo.

**4. Pedagogical framing in the UI text.**
Every label, description, and info tooltip is written to teach, not just to describe. The temperature slider says "Lower = more focused reasoning. Higher = more creative (but riskier)" — not just "Controls randomness."

---

## Step 5: Testing

I tested with the example problems first:

- **Divisibility problem:** The model produced a clean proof using factoring (n³ - n = n(n-1)(n+1), product of three consecutive integers). This is correct and students can follow it.
- **Inequality problem:** The model applied AM-GM correctly. The reasoning was clear.
- **Irrationality of √2:** The model set up a proof by contradiction. The structure was right, though one step was a bit compressed.
- **Harder problems:** Results varied. Some proofs had logical gaps; others were impressively complete.

This is exactly the educational point. The model isn't perfect. Students can find the gaps.

---

## Step 6: What I'd Improve

If I were iterating on this (the Session 11 lesson), here's what I'd change:

- **Add a "Proof Evaluation" mode** where the Space displays a proof and asks the user to identify the flaw (if any). This would make it more interactive than just reading output.
- **Side-by-side comparison** with a second model (like we did in Session 4). Feed the same problem to QED-Nano and a general-purpose model like a smaller Qwen variant. Compare the proof quality.
- **A rubric tool** that scores the proof on specific criteria (logical flow, completeness, notation). The QED-Nano researchers actually built rubrics like this for training — a student could build a simplified version.

---

## What This Project Demonstrates

This Space uses skills from almost every session in the course:

| Session Skill | How It's Used Here |
|--------------|-------------------|
| Session 1: pipeline → Interface pattern | Same structure, different model source |
| Session 2: Reading model cards | Chose QED-Nano based on its card |
| Session 3: Handling unexpected output | Testing with problems the model struggles on |
| Session 5: Hyperparameter controls | Temperature and max-token sliders |
| Session 9: Designing for an audience | Tabs, evaluation guide, pedagogical framing |
| Session 10: Building from scratch | New task type, new model, new purpose |

The one new thing is the Inference API call instead of `pipeline()`. That's one additional concept beyond what Level 2 covers. Everything else is applying what students already know to a more ambitious target.

**That's the point.** The course gives you tools. What you build with them is up to you. This Space applies those tools to the frontier of AI research — mathematical reasoning — and turns it into something you can explore, question, and learn from.

---

*Dr. Daniel Plate — AI + Research Level 2, Youth Horizons Learning*

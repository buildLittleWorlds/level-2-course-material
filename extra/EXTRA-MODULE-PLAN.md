# Extra Module: From Paper to Project — AI and Mathematical Proof

## Overview

This is an optional bonus module for the Level 2 course. It takes students from reading a cutting-edge research paper to building their own experimental Hugging Face Space — a full learning arc that teaches how to engage with real research using the skills built throughout the course.

The module is built around the QED-Nano paper (February 2026, CMU/Hugging Face/ETH Zurich/Numina), which describes training a 4B-parameter model to write Olympiad-level mathematical proofs.

---

## Four-Phase Structure

### Phase 1: Read the Paper with AI Assistance
**Material:** `phase-1-guided-reading.md`

Students read key sections of the QED-Nano paper using an AI assistant as a reading partner. The guided reading document provides specific prompts for each section, teaching students how to decode dense academic writing with AI help.

**Duration:** 45–60 minutes (independent work)

### Phase 2: Explore the Artifacts on Hugging Face
**Material:** `phase-2-hub-exploration.md`

Students visit the actual models, datasets, and Spaces the researchers published on the Hub. They browse training data, compare model cards, and examine the researchers' own blog post Space.

**Duration:** 30–45 minutes (independent work)

### Phase 3: Experiment with the Proof Explorer
**Materials:** `student-guide.md` + deployed Space

Students feed math problems to QED-Nano via the Proof Explorer Space and evaluate the model's proof attempts. The student guide provides three problems at different difficulty levels and reflection questions connecting proof evaluation to argumentation skills.

**Duration:** 30–45 minutes (session or independent work)

### Phase 4: Build Your Own Research Space
**Materials:** `phase-4-project-briefs.md` + `project-evaluation-rubric.md`

Students choose one of five project options and build a Hugging Face Space that investigates a specific aspect of the research. Projects range from accessible (Training Data Explorer) to ambitious (Reasoning Trace Analyzer).

**Duration:** 2–4 hours of build time across multiple sessions

---

## Google Classroom Setup

### Topic Name
**Bonus: Can AI Prove Theorems?** *(created — needs to be positioned after Session 12)*

### Materials to Post (in order)

1. **"Phase 1: Reading a Research Paper with AI"**
   - Source: `phase-1-guided-reading.md`
   - The guided reading document with AI prompts for each paper section

2. **"Phase 2: Exploring the Research on Hugging Face"**
   - Source: `phase-2-hub-exploration.md`
   - Hub exploration activities with links to models, datasets, and Spaces

3. **"Can AI Prove Theorems? — Student Guide"**
   - Source: `student-guide.md`
   - Introduction to QED-Nano + guided activity with the Proof Explorer Space

4. **"Proof Explorer — Try It Yourself"**
   - Link: `https://huggingface.co/spaces/profplate/qed-nano-proof-explorer`
   - The deployed Space

5. **"Build Your Own Research Space — Project Briefs"**
   - Source: `phase-4-project-briefs.md`
   - Five project options with technical requirements and getting-started guides

6. **"How I Built This Space — Instructor Walkthrough" (optional)**
   - Source: `instructor-walkthrough.md`
   - Step-by-step narrative of building the Proof Explorer

---

## Files in This Directory

| File | Phase | Purpose |
|------|-------|---------|
| `phase-1-guided-reading.md` | 1 | AI-assisted paper reading guide with section-by-section prompts |
| `phase-2-hub-exploration.md` | 2 | Hub exploration activities: models, datasets, Spaces |
| `student-guide.md` | 3 | Student-facing intro + guided activity with the Proof Explorer |
| `qed-nano-space/app.py` | 3 | The Proof Explorer Space code |
| `qed-nano-space/requirements.txt` | 3 | Python dependencies for the Space |
| `phase-4-project-briefs.md` | 4 | Five project options with requirements and starter guidance |
| `project-evaluation-rubric.md` | 4 | Rubric for evaluating student projects (5 criteria) |
| `instructor-walkthrough.md` | All | How-I-built-this narrative mapping build to course skills |
| `qed-nano-teaching-a-tiny-model-to-prove-hard-theorems.pdf` | Ref | The original QED-Nano paper |
| `EXTRA-MODULE-PLAN.md` | — | This file |

---

## How to Use This in a Session

### Option A: Brief Taste (15–20 minutes)
During any session from Session 9 onward:
1. Pull up the Proof Explorer Space
2. Try an accessible problem (divisibility by 6), read the proof together
3. Ask: "Is this a valid argument? How would you check?"
4. Point students to the bonus topic for more

### Option B: Extended Module (2–3 sessions)
For the summer intensive or as an enrichment arc:
- **Session A:** Phase 1 (guided reading) + Phase 2 (Hub exploration) — mostly independent with check-ins
- **Session B:** Phase 3 (Proof Explorer activity) + choose Phase 4 project
- **Session C:** Build time + project presentations

### Option C: Between-Session Challenge
Post the materials and let motivated students work through them independently:
- Phases 1–3 as self-paced exploration
- Phase 4 as an optional alternative final project (Sessions 10–12)

---

## Deployment Checklist

- [ ] Deploy Space to Hugging Face (`profplate/qed-nano-proof-explorer`)
- [ ] Test with all 8 example problems
- [ ] Convert markdown materials to Google Docs or host via GitHub Pages
- [ ] Populate Google Classroom topic with materials in order
- [ ] Reposition topic below Session 12 on Classwork page
- [ ] Test all links from student perspective

---

## Pedagogical Goals

1. **Teach research literacy.** Students learn to read, question, and engage with real academic work — not textbook summaries.

2. **Extend model evaluation into reasoning.** Students have evaluated sentiment models; now they evaluate logical reasoning, the hardest kind of evaluation.

3. **Show AI as tutor, object of study, and research tool.** The module shifts AI's role across phases — from reading partner to thing being investigated to tool being built around.

4. **Produce college-level work.** The Phase 4 projects are genuinely experimental. A finished Space that systematically tests a research model is impressive work at any level.

5. **Bridge to Level 3.** Students who complete this module are natural candidates for a deeper course in AI reasoning and mathematical argumentation.

---

## Correspondence

- PDF overview for Bing: `correspondence-and-research/from-paper-to-project-qed-nano-module.pdf`
- Email draft to Bing: `correspondence-and-research/email-draft-reply-bing-summer-and-proof-module-2026-02-26.md`

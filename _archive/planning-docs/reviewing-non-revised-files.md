# Reviewing Non-Revised Files: app.py, notebook.ipynb, README.md

## Context

The `enhancing-formal-research-framing.md` revision updated INSTRUCTOR-GUIDE.md, BETWEEN-SESSION.md, slides.html, peer-feedback-form.md, and portfolio-template.md across all 12 sessions. Three file types were **not touched**: `app.py`, `requirements.txt`, `notebook.ipynb`, and most session `README.md` files. This plan reviews whether those files still fit the revised course and identifies what might need to change.

---

## Current State of Each File Type

### app.py + requirements.txt

These are the instructor-built HF Spaces deployed before each session. Students watch the instructor build live, then interact with the deployed Space.

| Session | Space Name | What It Does | Status |
|---------|-----------|-------------|--------|
| 01 | Mood Meter | Visual sentiment gauge with emoji | Works as-is |
| 02 | Emotion Spectrum | Three models (binary/7-emotion/zero-shot) side by side | Works as-is |
| 03 | Sarcasm Breaker | Before/after cleaning comparison | Works as-is |
| 04 | Sentiment Showdown | Three sentiment models side by side | Works as-is |
| 05 | Text Playground | Text generation with temperature/top-p sliders | Works as-is |
| 06 | *(none — reuses S04)* | Domain shift testing on the Showdown Space | N/A |
| 07 | Bias Tester | Paired sentence comparison | Works as-is |
| 08 | Image Story Pipeline | BLIP captioning → sentiment analysis chain | Works as-is |
| 09 | Restaurant Review Analyzer | Audience-redesigned sentiment output | Works as-is |
| 10 | *(template only)* | Starter template for student Spaces | Works as-is |
| 11 | *(none)* | Students polish their own | N/A |
| 12 | *(none)* | Demo day | N/A |

**Assessment:** The Spaces don't need revision. They serve as the shared in-class build — the sentiment "textbook example" the instructor teaches with. The research framing was added around them (Research Lens, Big Question, SpaceCraft check-in), not inside them. The code is correct and the Spaces run on free CPU.

**One thing to watch:** As you teach, you may want to add a model card link to each Space's description (the improvement checklist from Session 11 asks students to do this). But this is a minor polish, not a structural change.

### notebook.ipynb

These are the ~20-minute Colab companions used at the end of each live session. Students run experiments hands-on after watching the instructor demo.

| Session | Notebook Focus | Alignment with Revised Guide |
|---------|---------------|------------------------------|
| 01 | Run sentiment model, test 5 inputs | Good — matches revised guide |
| 02 | Compare 3 models, design custom labels | Good — experiments match Research Lens (comparative analysis) |
| 03 | Test sarcasm, learn clean_text(), before/after | Good — experiments match Research Lens (adversarial testing) |
| 04 | 3 models side by side, find disagreement | Good — experiments match Research Lens (baseline comparison) |
| 05 | Temperature and top-p sliders, extreme settings | Good — experiments match Research Lens (parameter sweep) |
| 06 | 6 domains, find what breaks all models | Good — experiments match Research Lens (generalization testing) |
| 07 | Name/gender/role swaps, design custom tests | Good — experiments match Research Lens (fairness audit) |
| 08 | BLIP + sentiment chain, find error cascades | Good — experiments match Research Lens (error propagation) |
| 09 | Pick audience, redesign output format | Good — experiments match Research Lens (user-centered design) |
| 10 | Choose model, test 5 inputs, plan Space | Good — experiments match Research Lens (end-to-end system design) |
| 11 | Debug challenges, improvement checklist | Good — matches revised guide |
| 12 | Portfolio table, reflection questions | **Needs update** — doesn't include Collection, Research Journal, or research methods |

**Assessment:** Sessions 1-11 notebooks are well-aligned. The experiments already do what the Research Lens names — they just don't use the research vocabulary explicitly. That's fine; the Research Lens segment in the instructor guide provides the naming, and the notebook provides the hands-on doing.

**Session 12 notebook needs updating** to include:
- Collection URL and item count
- Research Journal link and entry count
- Research question field
- "Most useful research method" reflection question
- Research Methods checklist (matching portfolio-template.md)

### README.md (per session)

| Session | Current README Content |
|---------|----------------------|
| 01 | Detailed — title, description, resource list, session overview |
| 02 | Detailed — title, description, resource list |
| 03-12 | Minimal — just title and Colab badge |

**Assessment:** Most READMEs are placeholder stubs. They're not wrong, but they don't describe what the session actually covers. This is low priority — the INSTRUCTOR-GUIDE.md is the source of truth and the README is only visible to someone browsing the GitHub repo.

---

## The Bigger Question: SpaceCraft Exploration Notebooks

The revised course introduces SpaceCraft check-ins at the top of sessions 2-11. Each week, the instructor shows a new HF Space and frames it through that week's research method. But there's no **student-facing notebook** for exploring SpaceCraft Spaces or the student's own Collection items through code.

### What's missing

Right now, students explore Spaces by visiting URLs in a browser. They explore models by running them in the session notebook. But there's a gap: **students never write code to investigate a Space or model from their own Collection.** The between-session Research Journal asks them to apply the week's method to their own topic — but they do this by visiting Spaces in a browser, not by writing code.

### Proposal: Weekly SpaceCraft Explorer Notebook

A supplementary notebook (one per session, sessions 2-10) that gives students a code scaffold for applying the week's research method to **any model they choose** — including ones from their Collection or ones the instructor added to SpaceCraft.

#### How it differs from the existing notebook

| | Existing Session Notebook | SpaceCraft Explorer Notebook |
|---|---|---|
| **When used** | Last ~20 min of live session | Between sessions (homework) |
| **Models** | Fixed models tied to the session's build | Student's choice — from their Collection |
| **Focus** | Reproduce what the instructor demoed | Apply the week's method to a new model |
| **Output** | Observations in markdown cells | Structured output matching Research Journal template |
| **Complexity** | Guided (uncomment, run, observe) | Semi-guided (fill in model name, write your own inputs) |

#### What each Explorer notebook contains

1. **Setup cell** — install transformers, load pipeline
2. **Model loader** — student fills in their own model name from their Collection (with a commented-out example)
3. **Method scaffold** — 3-5 cells that walk through the week's research method applied to the student's model:
   - Session 2: Load two models, run same inputs, compare outputs (comparative analysis)
   - Session 3: Feed adversarial inputs, apply cleaning, compare before/after (adversarial testing)
   - Session 4: Load 2-3 models, run same test set, tabulate results (baseline comparison)
   - Session 5: Sweep one parameter across values, record output changes (parameter sweep)
   - Session 6: Test on 3 different text domains, record accuracy (generalization testing)
   - Session 7: Design 5 paired inputs, run model, record differences (fairness audit)
   - Session 8: Chain two models, inject errors at step 1, observe step 2 (error propagation)
   - Session 9: Write `format_for_audience()` for a chosen audience (user-centered design)
   - Session 10: No explorer — students are building their own Space
4. **Research Journal draft cell** — markdown cell pre-filled with the week's Research Journal template headers, so students can draft their entry right in the notebook
5. **Collection note cell** — prompt to add a tasting note about the model they tested

#### Naming and location

```
level-2-course/
├── session-02/
│   ├── notebook.ipynb              # existing (in-class, last 20 min)
│   ├── explorer.ipynb              # NEW (between-session, homework)
│   ├── app.py, requirements.txt    # unchanged
│   ├── INSTRUCTOR-GUIDE.md, ...    # revised
```

The BETWEEN-SESSION.md for each session would add a line: "Use the Explorer notebook to apply this week's method to a model from your Collection."

#### Why this works

- Students currently do between-session work by browsing Spaces in a browser. The Explorer notebook adds a code path — they're **writing code** to investigate their own question, not just observing.
- The Research Journal asks students to document "How I Applied It" and "What I Found." The Explorer notebook generates those observations through code.
- By Session 10, students have written code in 8 Explorer notebooks investigating their own topic. The transition to "build from scratch" is much smoother — they already have a library of investigation code.
- The Explorer notebooks become portfolio artifacts themselves — evidence of applied research methods.

#### Why this might not work

- **Time burden.** Students already have between-session work: Hub Challenge (Option A/B), Research Journal entry, Collection + GitHub. Adding another notebook could feel like too much.
- **Model compatibility.** Not every model a student picks from their Collection will work with `pipeline()`. Some will need custom loading code the student can't write yet.
- **Duplicate effort.** Some students may use the Explorer notebook to generate their Research Journal entry, making the two feel redundant rather than complementary.

#### Recommendation

**Build Explorer notebooks for sessions 2-5 first.** These cover the simplest methods (comparative analysis, adversarial testing, baseline comparison, parameter sweep) and use text models that reliably work with `pipeline()`. See how students use them in practice. If the notebooks are adding value, continue building for sessions 6-9. If they feel like busywork, stop.

---

## Implementation Plan

### Phase 1: Assessment and Quick Fixes (before Session 2)

1. **Update Session 12 notebook** to include Collection URL, Research Journal link, research question, and research methods checklist (matching portfolio-template.md).
2. **Expand session README.md files** (sessions 3-12) from stubs to short descriptions matching the instructor guide. Low priority but easy to do.
3. **Verify all notebook Colab badges** still point to the correct GitHub repo path.

### Phase 2: Explorer Notebook Prototype (before Session 2)

4. **Build `explorer.ipynb` for Session 2.** This is the test case. It should:
   - Let students load any text-classification model by name
   - Compare it against the session's 3 models on 5 inputs
   - Include a Research Journal draft cell with Week 2 headers
   - Include a Collection tasting note cell
5. **Update Session 2 BETWEEN-SESSION.md** to reference the Explorer notebook as an optional tool for the Research Journal entry.
6. **Test the Explorer notebook** on Colab free tier with 3-4 different models to verify it works.

### Phase 3: Explorer Notebooks for Sessions 3-5 (rolling, before each session)

7. **Build `explorer.ipynb` for Session 3** — adversarial testing scaffold
8. **Build `explorer.ipynb` for Session 4** — baseline comparison scaffold
9. **Build `explorer.ipynb` for Session 5** — parameter sweep scaffold
10. Update each session's BETWEEN-SESSION.md to reference the Explorer notebook.

### Phase 4: Evaluate and Continue (after Session 5)

11. **Check with students:** Are Explorer notebooks useful? Are they using them? Are they generating Research Journal content?
12. **Decision point:** Build explorers for sessions 6-9, or stop if they're not adding value.
13. If continuing, build for sessions 6-9 (generalization testing, fairness audit, error propagation, user-centered design).

### Phase 5: README and Portfolio Polish (any time)

14. **Expand session READMEs** to match instructor guides.
15. **Add model card links** to Space descriptions (app.py files) if desired.
16. **Update course-level README.md** to mention research framing, Collection, and Research Journal.

---

## Decision Matrix

| File Type | Change Needed? | Priority | When |
|-----------|---------------|----------|------|
| app.py | No structural changes | Low | Optional polish any time |
| requirements.txt | No changes | None | — |
| notebook.ipynb (S1-11) | No changes | None | Already aligned |
| notebook.ipynb (S12) | Update for research framing | Medium | Before Session 12 |
| README.md (S3-12) | Expand from stubs | Low | Any time |
| README.md (course-level) | Update for research framing | Low | Any time |
| **explorer.ipynb (NEW)** | **Build for S2-S5, then evaluate** | **High** | **Before each session** |

---

## Open Questions

1. **Should Explorer notebooks be separate files or folded into the existing notebook?** Separate keeps the in-class notebook short and focused. Combined means one fewer file to manage. Recommendation: separate, because the in-class notebook is used live on screen-share and shouldn't have homework-only sections.

2. **Should Explorer notebooks be optional or required?** The BETWEEN-SESSION.md currently frames everything as optional ("never prerequisite"). The Explorer notebook should follow the same pattern — it's a tool for students who want to go deeper, not a requirement.

3. **Where should Explorer notebooks live in the GitHub repo?** In the same session folder (`session-02/explorer.ipynb`) or in a separate `explorers/` folder? Recommendation: same session folder, to keep everything co-located.

4. **Do Explorer notebooks need their own Colab badges in the README?** Yes — students need a one-click link. The session README and BETWEEN-SESSION.md should both include the badge.

5. **What about students who pick image or audio models for their Collection?** Sessions 2-7 Explorer notebooks should focus on text models (pipeline-compatible). Session 8+ can introduce image handling. Students whose Collections lean toward non-text models may not be able to use every Explorer notebook. That's fine — the notebook is optional, and they can still write their Research Journal entry from browser-based exploration.

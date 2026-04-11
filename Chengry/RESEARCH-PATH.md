# Your Research Path — Medical and Diagnostic AI

This guide walks you from "medical AI" (a direction) to a focused research question, through published research, to three Spaces and a research brief. Follow these five steps.

---

## Step 1: Catch Up Your Journal — Weeks 3–5 From Memory

You have material that hasn't made it into the journal yet. Write it now, while it's fresh (or freshish):

- **Week 3:** When did you decide to shift from WorldCup work to medical AI? What was the moment? What model or tool first excited you? (Your Week 2 entry about WorldCup is fine as-is. Just add a note here: "After exploring WorldCup summarization, I pivoted to medical AI as my focus for the remaining weeks.")
- **Week 4:** What was the first thing you built or tested? (disease_detectives, medical_text_generator, or something else?) What worked? What broke?
- **Week 5:** What did you learn from Week 4? Any model comparisons? Any architectural decisions (e.g., why you chose Claude Opus for disease_detectives, why you picked SmolLM2 for medical_text_generator)?

Use this template for each entry:

```markdown
## Week X

**What I Did**
- [1–2 things you built, tested, or researched]

**What I Learned**
- [One key insight or failure]

**Next**
- [What you're trying next]
```

Your journal doesn't need to be polished. It's a working record. One or two paragraphs per week is enough. The key is that your actual work is documented before you move on.

---

## Step 2: Sharpen Your Research Question

"Medical AI" is a direction. A research question is specific.

You have three candidates, from broad to narrow:

### Option A: Broad
**How well do general-purpose large language models (GPT, Claude, Mistral, Qwen) handle medical text compared to specialized medical language models?**

This is broad because it's asking about performance across many models. But it's focused on one variable: general vs. specialized.

**What this looks like:**
- Pick 4–5 models (mix of general and medical-specific)
- Give them the same 10 prompts across different medical registers (patient handout, clinical note, research abstract, classroom explanation)
- Score each output on clarity, accuracy, and caution
- Compare scores by model

**Your three Spaces:**
1. Disease detection baseline (disease_detectives)
2. A general-purpose medical text generator (medical_text_generator)
3. A comparison dashboard: same prompt, side-by-side outputs from 3–4 models

---

### Option B: Medium (My Recommendation)
**Do instruction-tuned smaller models (SmolLM2, Qwen) produce safer, more cautious, and more audience-appropriate medical explanations when given audience-level instructions than they do without them?**

This is medium because it's focused: one variable (instructions), one signal (safety/caution/audience-fit), one constraint (small models on free CPU).

**What this looks like:**
- Pick one model (SmolLM2-360M or Qwen2.5-0.5B)
- Write four instruction variants: "explain this for a patient with no medical background," "explain this for a high school biology class," "explain this for a clinical audience," "explain this as a medical safety warning"
- Test on 5–8 medical topics (diabetes, asthma, COVID-19, etc.)
- Score outputs on: clarity for the target audience, whether the model includes appropriate disclaimers or cautions, reading-level appropriateness, usefulness
- Compare instruction-tuned vs. baseline (no instructions)

**Your three Spaces:**
1. Disease detection baseline (disease_detectives)
2. Medical text generator with audience-level instructions (medical_text_generator, enhanced with SPACE-PROMPTS.md Prompt 6)
3. A medical safety audit lab (medical_text_generator upgraded to compare the same prompt across audience levels)

**Why I recommend this:** It's specific enough to measure, narrow enough to finish in the remaining weeks, and it directly touches a real problem: medical AI that talks differently to patients vs. doctors vs. classrooms. You already understand this — you've built Claude systems that change tone by audience. This is that idea formalized as a research question.

---

### Option C: Narrow (The Hardest)
**How do small instruction-tuned medical text generators compare across four medical registers (patient handout, clinical note, research abstract, classroom explanation) and three readability constraints (8th grade, high school, college), and does instruction-tuning improve the match between the model's output reading level and the target level?**

This is narrow because it's very specific: three models, four registers, three reading levels = 36 outputs to score. You'd measure how well each model's output matches the target audience reading level using a tool like FRES (Flesch Reading Ease Score) or a rubric.

**What this looks like:**
- Pick 3 models (distilgpt2 as baseline, SmolLM2, Qwen)
- Pick 3 medical topics
- Generate 3×4×3 = 36 outputs
- Score each on reading-level appropriateness and factual caution
- Compute a correlation between instruction specificity and reading-level match

**Your three Spaces:**
1. Disease detection baseline (disease_detectives)
2. Medical text generator with audience-level instructions (medical_text_generator)
3. A reading-level analyzer that shows FRES score + audience match for medical text (new Space)

**Why this is hard:** 36 outputs to evaluate by hand is tedious. But if you automate the FRES scoring and use a rubric for caution, it's doable.

---

## Step 3: Connect to Published Research

Once you've picked your research question, find papers that already touched it. Here are the consensus directions in medical AI and NLP:

- **AI safety in clinical NLP** — Papers on hallucination, bias, and reliability of language models in healthcare settings. Look for: "hallucination medical AI," "clinical NLP safety," "biomedical language models"
- **Medical text generation** — Papers on whether small models can generate medical explanations safely. Look for: "medical text generation," "patient education AI," "automated medical writing"
- **Domain shift in healthcare AI** — Papers on whether models trained on general text (Wikipedia, web text) work well on medical text. Look for: "medical domain adaptation," "healthcare NLP transfer learning"
- **Readability of AI-generated health information** — Papers on whether AI-generated health text is actually readable by patients. Look for: "health literacy AI," "readability AI-generated text," "patient comprehension medical AI"
- **Responsible AI in healthcare** — Papers on disclaimers, warnings, and ethical frameworks for medical AI. Look for: "medical AI ethics," "responsible AI healthcare," "AI clinical decision support"

**How to find these papers:**
1. Go to https://consensus.app (you used it in Week 3)
2. Search for your research question. For Option B, try: "instruction-tuning medical text generation" or "medical explanation readability"
3. Download 3–4 papers that match your question
4. Skim the related work section in each — those sections will point you to more papers
5. Grab the most relevant 4–6 papers and add them to a "Related Work" section in your research brief

---

## Step 4: What Your Three Spaces Should Look Like

You already have the building blocks. Frame them as deliverables:

### Space 1: The Baseline (disease_detectives)
**What it does:** Diagnostic reference tool. User describes symptoms or a medical concept; the tool returns information using Claude or another model.

**Why it's in your portfolio:** It's the foundation. It shows you know how to build a real diagnostic pipeline and ship it on Hugging Face. The fact that it currently has a RUNTIME_ERROR doesn't matter once you fix it — and you probably already know how to fix it (dependency issue, or API call error).

**What to focus on before you ship it again:**
- Make sure the Claude API call is working (or whatever model you're using)
- Add a clear disclaimer: "This tool is for educational exploration only and does not provide medical advice. Always consult a real doctor."
- Make sure the code is clean and readable

---

### Space 2: The Experiment (medical_text_generator)
**What it does:** Generates medical explanations at different audience levels, with controllable parameters (temperature, top-p, max_new_tokens).

**Why it's in your portfolio:** It's where you test your research question. If your question is about instruction-tuning, this Space shows what happens when you change the instructions. If your question is about model comparison, this Space is where you compare SmolLM2 vs. Qwen vs. distilgpt2.

**What to do with it:**
- Use Prompt 2 or Prompt 6 from SPACE-PROMPTS.md to rebuild it or enhance it
- Add an "Audience Level" dropdown with at least two options: patient-friendly, clinical-style
- Add a second-generation "Medical Safety Audit Lab" version that lets you compare models side-by-side on the same prompt

---

### Space 3: Either Enhanced medical_text_generator or a New Space
**Option 1:** Medical_Entity_Extractor fully deployed. If you built this already, this is Space 3 — named entity recognition on medical text. Ship it, document it.

**Option 2:** A medical safety audit lab or reading-level analyzer. This is the space where you *compare* things — either model outputs side-by-side, or reading-level scores, or safety scores across prompts.

Pick whichever one better matches your research question.

---

## Step 5: Your Unique Angle — Medical Ethics and Responsible AI

Here's what sets you apart from most high school students building medical AI: you're thinking about responsibility, not just capability.

Your disease identification tool with Claude Opus 4.5 is technically impressive. But what makes it *interesting as research* is the ethics dimension:

- **How do you know when a model is confident enough to speak vs. when it should defer to a doctor?**
- **What disclaimers matter? "Not medical advice" is too generic. What specific warnings do patients need?**
- **When does instruction-tuning make medical text safer (more cautious, clearer about limitations) vs. less useful (too vague)?**
- **Does the same explanation that works for a patient handout actually work for a clinician or a classroom?**

These are the questions that make medical AI hard in the real world. Most researchers are focused on accuracy. You can be focused on responsibility.

**How to bring this into your research brief:**
- Choose one responsible-AI paper from your related work (e.g., a paper on clinical decision-support ethics or hallucination in medical AI)
- Frame your research question as a piece of that larger problem
- In your brief's discussion section, connect your results back to responsible deployment: *"If instruction-tuning improved caution in our test, what does that mean for rolling out this tool to real patients?"*

---

## What Prea Did That You Should Notice

Prea's portfolio is the model for the course. Here are the specific weeks where she did things you should study:

- **Week 3 (Consensus detour):** Prea went from intuition ("prosody matters for persuasion") to published papers in one week. She used Consensus to find the papers. You did this in Week 2 with WorldCup papers; now do it again with medical papers.
- **Week 4 (Research hypothesis):** Prea wrote a formal hypothesis and linked it to published work. Look at her README under "The Hypothesis" — it's specific and measurable. Your research question should be similarly specific.
- **Weeks 5–7 (Architecture pivot):** Prea ran into a technical wall (audio compute on Hugging Face) and pivoted to a different architecture (thin client over API). When disease_detectives has a RUNTIME_ERROR, you'll do the same: diagnose it, fix it, and document what you learned.
- **Week 8–10 (Evaluation):** Prea designed a small, fair test (20 clips, Spearman correlation) and reported limitations honestly. Your three Spaces should be similarly testable. Can you score 10–20 medical explanations on clarity and caution?
- **Week 11 (Brief):** Prea's brief is four pages, has five sections (abstract, related work, methods, results, limitations), and cites both papers and a blog post. Yours will be similar: you'll cite 4–6 medical AI papers + your own Spaces as the evidence.

---

## Your Customized Prompt Template

When you're ready to build or enhance your Spaces, use this template with Claude or ChatGPT:

```
I'm building a medical AI education tool as part of a research project. 
I want to test whether [YOUR RESEARCH QUESTION].

I have three Spaces to build:

1. [Space 1 description]
2. [Space 2 description]
3. [Space 3 description]

For Space 2, I want to experiment with [YOUR VARIABLE: e.g., "instruction-tuning for different audience levels"].

Please help me:
- Design the code so I can easily change [YOUR VARIABLE]
- Add clear disclaimers that this is educational only
- Pick models that work on free Hugging Face CPU
- Make the results easy to compare

Here's my research question: [YOUR QUESTION]
Here are example test prompts: [LIST 3–5 MEDICAL TOPICS]

Give me the complete app.py and requirements.txt for Space 2.
```

Fill in the bracketed parts with your specific question and details.

---

## Next Steps

1. **This week:** Pick Option A, B, or C above. (Option B is what I'd recommend.)
2. **Next:** Catch up your journal with Weeks 3–5.
3. **Then:** Find 4–6 published papers using Consensus.
4. **Finally:** Write a one-paragraph research question and a one-sentence hypothesis. Send it to your instructor for feedback before you build Space 2.

You have the technical depth to do this. The work is just waiting to be written down and connected to research.

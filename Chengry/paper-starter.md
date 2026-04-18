# Chengry — Paper Starter

Use this with the shared `PAPER-TEMPLATE.md` and `GUIDE-FROM-SPACE-TO-PAPER.md`.

Your paper should come from the actual design choices in DxAI, not from sounding formal.

## Best direction

**Recommended research question**

When a medical AI tool is built for ordinary users, does a ranked-and-cautious interface communicate uncertainty better than a single-answer style interface?

**Good backup question**

Is responsible medical AI mostly a model problem, or is it also an interface-design problem?

## Best artifact to write about

Write about **DxAI / Disease Identification** first.

If the runtime error is still live, say so honestly in the limitation section. Do not wait for perfection before drafting.

## Pull these things from your journal or notes

- the disclaimer language you chose
- why the output is ranked possibilities instead of one answer
- one test case you ran
- why you used Claude or the model you chose
- one honest limit: runtime issues, safety limits, medical uncertainty, or overconfidence risk

## Suggested paper map

### 1. What I built

I built a medical AI Space that takes symptoms and returns possible conditions with caution and disclaimers.

### 2. My research question

Your question should come from the design choice to show uncertainty instead of pretending the tool knows one answer.

### 3. Why This Matters to Me

This is where you explain why medical AI feels important to you and why honesty matters more than sounding certain.

### 4. What I Tried

Use one concrete input or comparison:

- a symptom test case
- what you expected
- what the output actually looked like

### 5. What I Learned

Your strongest likely finding is that the interface matters as much as the model when the domain is high-stakes.

### 6. What Still Needs Work / Who It Might Fail For

Possible limits:

- the tool is not a doctor
- runtime instability or missing dependencies
- medical input ambiguity
- risk of false confidence

### 7. Sources to add or cite

- medical AI safety
- communicating uncertainty to patients
- model card / API documentation for your deployed model

## Prompt to sharpen the question

```text
I am writing a short paper about my medical AI Space.

My main observation is that the design feels more honest when it returns ranked possibilities and strong disclaimers instead of pretending to diagnose perfectly.

Help me turn that into one clear research question and one backup question.

Do not invent tests or results.
```

## Prompt to draft from your notes

```text
Help me draft a short student paper from my own notes about DxAI.

Use only the notes I give you. Do not invent symptoms, outputs, or sources.

Follow this structure:
- What I built
- My research question
- Why this matters to me
- What I tried
- What I learned
- What still needs work / who it might fail for
- Sources to add or cite

Keep the writing plain and honest.
```

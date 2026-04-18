# Shawn — Paper Starter

Use this with the shared `PAPER-TEMPLATE.md` and `GUIDE-FROM-SPACE-TO-PAPER.md`.

Your curation work is already research. The paper makes that visible.

## Best direction

**Recommended research question**

When the same prompts are run through general-purpose and style-tuned image models, how much of "style control" is real and how much is just surface-level style vocabulary?

**Good backup question**

Does fine-tuning for one style improve style fidelity at the cost of flexibility outside that style?

## Best artifact to write about

Write about **AnimeSceneWriter** if it is the cleanest comparison Space. If that runtime issue still matters, say so honestly and keep the paper anchored to the comparison idea itself.

## Pull these things from your journal or notes

- the exact models you want to compare
- the exact styles or prompt set
- one example where a model looked impressive but did not really follow the style in a deep way
- one example where a specialized model did better inside its lane
- one honest limit: runtime issues, missing weeks in the journal, or still-small test grid

## Suggested paper map

### 1. What I built

I built or curated a comparison tool for testing style-specific image generation across different models.

### 2. My research question

Your question should come from the gap between "this looks stylish" and "this really understands style."

### 3. Why This Matters to Me

This is where you explain why image-generation curation and art-style comparison became your main thread.

### 4. What I Tried

Use one concrete comparison:

- same prompt
- same style request
- multiple models
- what you expected
- what happened

### 5. What I Learned

Your strongest likely finding is that specialization helps, but often in a narrower and more brittle way than the model cards suggest.

### 6. What Still Needs Work / Who It Might Fail For

Possible limits:

- runtime/debugging issues
- missing journal weeks
- style is hard to score cleanly without a stronger rubric

### 7. Sources to add or cite

- diffusion style control
- fine-tuning and specialization
- evaluation of text-to-image style adherence

## Prompt to sharpen the question

```text
I am writing a short paper about comparing image-generation models across styles.

My main observation is that some models look stylistically impressive without really showing deep style control, while specialized models may work well only inside a narrow lane.

Help me turn that into one clear research question and one backup question.

Do not invent tests or results.
```

## Prompt to draft from your notes

```text
Help me draft a short student paper from my own notes about comparing image-generation models.

Use only the notes I give you. Do not invent prompts, model names, or findings.

Follow this structure:
- What I built
- My research question
- Why this matters to me
- What I tried
- What I learned
- What still needs work / who it might fail for
- Sources to add or cite

Keep the writing plain and direct.
```

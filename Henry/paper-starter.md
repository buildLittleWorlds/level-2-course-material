# Henry — Paper Starter

Use this with the shared `PAPER-TEMPLATE.md` and `GUIDE-FROM-SPACE-TO-PAPER.md`.

Your journal already has real evidence. The paper is mainly about organizing it cleanly.

## Best direction

**Recommended research question**

When language and image tools are asked to change perspective, do they actually change the scene in a spatial way, or do they mostly swap in perspective-coded words and visuals?

**Good backup question**

Is a two-modality probe better than a single tool when you want to test perspective reasoning honestly?

## Best artifact to write about

Write about the **pair**:

- `Scene_describer`
- `Camera_angle_model_lab`

That pairing is your strength. Most students have one tool. You have two tools testing the same idea from different sides.

## Pull these things from your journal or notes

- one slider-extreme test that taught you something real
- the exact perspective labels or prompts you used
- one example where the output sounded perspective-aware but was really surface-level
- why the text and image pair helped you see the problem more clearly
- one limit: small models, small test set, or still-unclear evaluation

## Suggested paper map

### 1. What I built

I built two related tools that test perspective from two modalities instead of one.

### 2. My research question

Your question should come from the gap between "this sounds like a new perspective" and "this actually represents a new perspective."

### 3. Why This Matters to Me

Use this section to explain why perspective, camera angle, and viewpoint keep pulling you back as a topic.

### 4. What I Tried

Use one clean example:

- same scene
- multiple perspective prompts
- what changed
- what did not change

### 5. What I Learned

Your strongest likely finding is that many outputs look perspective-aware while staying shallow underneath.

### 6. What Still Needs Work / Who It Might Fail For

Possible limits:

- perspective is hard to score cleanly
- smaller models may only swap surface vocabulary
- your tests still need expansion across more prompts or images

### 7. Sources to add or cite

- spatial reasoning in language models
- multi-modal probing
- novel view / perspective control in image generation

## Prompt to sharpen the question

```text
I have two related Spaces that test perspective from both text and image sides.

My main observation is that many outputs look perspective-aware on the surface, but may only be swapping words or shallow visual cues.

Help me turn that into one strong research question and one backup question.

Do not invent tests or results.
```

## Prompt to draft from your notes

```text
Help me draft a short student paper from my own journal notes about perspective and my two Spaces.

Use only the notes I give you. Do not invent prompts, models, or findings.

Follow this structure:
- What I built
- My research question
- Why this matters to me
- What I tried
- What I learned
- What still needs work / who it might fail for
- Sources to add or cite

Keep the writing clear and direct.
```

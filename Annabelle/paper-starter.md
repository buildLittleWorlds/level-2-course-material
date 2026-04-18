# Annabelle — Paper Starter

Use this with the shared `PAPER-TEMPLATE.md` and `GUIDE-FROM-SPACE-TO-PAPER.md`.

Your goal is not to sound fancy. Your goal is to pull a clear claim out of the journal work you already have.

## Best direction

**Recommended research question**

When small instruction-tuned models are asked to write in opera, jazz, and classical styles, do they actually produce genre-specific writing, or do they mostly recycle generic music words?

**Good backup question**

Can AI music tools help with music learning, or are they better at inspiration than at teaching real genre distinctions?

## Best artifact to write about

Write about **Music-Starter-Opera-Jazz** first. It is the cleanest place where your question becomes visible.

You can mention `nyssma-trainer` in the "Why this matters to me" section, because that is where your real music background becomes part of the paper.

## Pull these things from your journal or notes

- one prompt where the output felt clearly too generic
- one moment where opera and jazz sounded less different than they should have
- the exact models you compared
- why NYSSMA or real music training gives you a different standard than a casual user would have
- one honest limitation: maybe the test set is small, maybe the models are tiny, maybe style is showing up mostly at the vocabulary layer

## Suggested paper map

### 1. What I built

I built a Space that compares small instruction-tuned models on music-writing tasks across different genres.

### 2. My research question

My question grew out of noticing that the outputs often used "music words" without really sounding like different genres.

### 3. Why This Matters to Me

This is where you mention your real music background, opera/jazz knowledge, and why "genre-specific" means more to you than it might mean to someone outside music.

### 4. What I Tried

Use one clear comparison:

- same prompt
- same three models
- different genre instructions
- what you expected versus what happened

### 5. What I Learned

Your strongest likely finding is that prompt-following improved more than true genre specificity.

### 6. What Still Needs Work / Who It Might Fail For

Possible limitation:

- the models may be useful for brainstorming but weak as teaching tools
- your evaluation still depends on expert musical judgment
- style might be easier to fake at the vocabulary level than at the structural level

### 7. Sources to add or cite

- AI music generation and pedagogy
- genre/style transfer in music generation
- model cards for the exact models you tested

## Prompt to sharpen the question

```text
I am writing a short paper from my journal notes about AI music tools.

My main observation is that small instruction-tuned models often follow the prompt but still sound genre-generic when I ask for opera, jazz, or classical writing.

Help me sharpen this into one clear research question and one backup question.

Use only that observation. Do not invent tests or results.
```

## Prompt to draft from your notes

```text
Help me draft a short student paper from my own journal notes.

My topic is: small instruction-tuned models and genre-specific music writing.

Use only the notes I give you. Do not invent models, prompts, or findings.

I want the draft to follow this structure:
- What I built
- My research question
- Why this matters to me
- What I tried
- What I learned
- What still needs work / who it might fail for
- Sources to add or cite

Make the writing plain and direct.
```

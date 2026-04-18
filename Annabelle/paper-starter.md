# Annabelle — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`, drafted from your research path, journal, and deployed Spaces. Fill in the blanks; delete what doesn't fit; keep what rings true.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then open [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) as your exemplar. Then come back here.

---

## Your paper in one sentence (proposed)

> *Three small instruction-tuned models, asked to write in opera, jazz, and classical genres, reveal that "instruction-tuning" improves prompt-following more than it improves genre-specific writing — and this has implications for AI as a pedagogical tool in classically trained musical practice.*

Change it. Sharpen it. But that's the shape.

---

## Pre-filled § I — The artifact

Pick **one** of your Spaces as your centerpiece. Your strongest candidate is **Music-Starter-Opera-Jazz** because it already contains the opera-vs-jazz comparison that's the heart of the research. `nyssma-trainer` is personally meaningful but is a different *kind* of artifact (a training/practice tool, not a comparison probe).

| | |
|---|---|
| **Title** | Music-Starter-Opera-Jazz — a Comparative Probe for Small-Model Genre-Specificity |
| **Medium** | Gradio Space (Python) |
| **Deployments** | [huggingface.co/spaces/annabelle-li/Music-Starter-Opera-Jazz](https://huggingface.co/spaces/annabelle-li/Music-Starter-Opera-Jazz) · source in your `AI-research-level-2` repo |
| **Dependencies** | The three instruct models you pick (fill in — likely one Llama-3-instruct, one Qwen-instruct, one SmolLM2-instruct or similar) |
| **Lines of code** | ≈ ___ (check your app.py) |
| **Reading time** | The length of one aria |

## Three candidate research angles (pick one)

Adapted from your [`RESEARCH-PATH.md`](./RESEARCH-PATH.md). Pick the one you actually want to defend — the paper will be stronger if you disagree with the other two.

1. **The pedagogy angle.** Small instruction-tuned models produce generic "music words" across genres; the question is not whether they can generate music, but whether they can serve as a teaching tool for students learning NYSSMA-calibrated genre distinctions. Centerpiece claim: AI music tools are currently **pattern engines, not genre teachers** — and the distinction matters for music education.

2. **The quantization angle.** Genre itself is a quantization — classical tradition has agreed to bucket an infinite continuous space of musical expression into "opera," "jazz," "lieder," etc. A small model trained on genre-labeled data is doing the same job, less well. Centerpiece claim: genre labels are a **lossy compression** of musical tradition, and models that learn them inherit that loss.

3. **The control angle.** Your `nyssma-trainer` and `Music-Starter-Opera-Jazz` both experiment with *adding controls* (sliders, structured prompts). The question is which controls actually move the output in genre-specific ways versus which just add noise. Centerpiece claim: **most controls are theatre** — and the controls that aren't theatre are the ones that encode genre-specific structural requirements.

My guess: **#1 (pedagogy)** because NYSSMA is your Δ — the domain expertise no one else in the cohort has. But pick the one you'd rather defend.

## Suggested § II genre contrast

Your artifact's genre is a **comparative probe**. The default genre of a "music AI" Space is a *demo* — press a button, hear a thing, be entertained. You're not doing that. You're asking the Space to fail, visibly and symmetrically across three genres, so that a reader can watch the failure happen.

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| music demo | fun, impressive, ambient | glance and share | an output to react to |
| comparative probe | diagnostic, symmetric, honest | read side-by-side | evidence for or against a hypothesis |

## Your Δ

Candidate Δs from your work:

- **The choice of three genres** (opera, jazz, classical — not hip-hop, not k-pop, not ambient). That list is yours.
- **The choice of three models** (which three did you pick, and why those — parameter count? tokenizer? training date? availability on HF Inference API?).
- **The prompt template** in `RESEARCH-PATH.md` Step 2 — the exact wording of "Use vocabulary specific to [GENRE]" is your editorial hand on the scale.

Pick the one you feel most defensive about. That's your Δ.

## Suggested epigraph domain

Pull from:
- A musician's memoir (Glenn Gould; Patti Smith; Joshua Bell; Leonard Bernstein's *The Joy of Music*)
- A music critic (Alex Ross, *The Rest Is Noise*; Charles Rosen, *The Classical Style*)
- NYSSMA's own published pedagogy (if there's a line worth quoting)
- A jazz figure writing on form (Miles Davis's autobiography; Wynton Marsalis)

Avoid: a composer quote pulled from the internet. Use a book.

## Consensus searches to run

Do these before finalizing §§ II and IX.

- `"genre recognition language models text generation"`
- `"music style transfer large language models evaluation"`
- `"computational creativity music generation style"`
- `"instruction tuning genre adherence"`
- `"AI music composition pedagogy classical education"` *(specific to angle #1)*

Expect 2–3 hits per query. Keep the three strongest.

## Your § IX candidate category

The template tells you to propose a small category. For your topic, two candidates:

1. **Pattern engines, not genre teachers.** *Machine-learning systems that reproduce surface statistics of a genre without encoding the pedagogical structure that a human student would be taught.* The claim: these systems are **useful for prototyping and inspiration, unsuitable for teaching, and routinely mistaken for both.**

2. **Loss-calibrated generation.** *Generation systems evaluated not on output quality but on how well their failures match the ways a domain expert would fail.* The claim: a small model that produces bad opera in the *wrong* ways is worse than one that produces bad opera in the *right* ways.

Both are small, defensible, and slightly surprising. Either is enough for §IX.

---

## Questions to answer before drafting §§ III–XI

1. Which of the three angles above is your angle?
2. Which Space is §I? (Music-Starter-Opera-Jazz is the recommendation.)
3. What are the three specific models you compared — exact names?
4. What is your Δ — name it in one sentence.
5. Do you have an epigraph candidate yet, and from what book?

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md) — copy this into your `AI-research-level-2` repo as `PAPER.md`
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) — read section 3 ("From journal to paper in five steps") before writing
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) — the worked exemplar
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md) — you've already done most of the thinking; the paper consolidates it into a form

You have the breadth and the debugging skill. The paper phase is writing the last chapter of a thing that's already mostly there.

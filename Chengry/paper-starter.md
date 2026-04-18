# Chengry — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`. Fill in the blanks; delete what doesn't fit.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md).

---

## Before drafting: three things to ship first

Your flagship Space (`DxAI — Disease Identification`) has a runtime error and your journal could use catch-up entries before the paper draws from it. Do these first, in order:

1. **Debug DxAI.** The error is missing Python dependencies for audio processing. Remove the audio code if you're not using it, or add the dep to `requirements.txt`. One session.
2. **Write two catch-up journal entries** covering what you built in the most recent weeks (DxAI, Mood Meter, the Claude Opus 4.5 integration). Honest: *"reconstructing from memory because I did not journal at the time."*
3. **Commit a clean `research-journal.md`** in a new or tidied repo — a fork of the course material is the wrong place for the portfolio centerpiece.

Once all three are done, the paper writes itself.

---

## Your paper in one sentence (proposed)

> *A disease-identification Space built on Claude Opus 4.5, with prominent medical disclaimers and a diagnostic-interface affordance pattern, is read as an intentionally over-cautious artifact — and the paper argues that over-caution is the correct design choice for consumer-facing medical AI, against the prevailing trend toward confidence-maximizing outputs.*

Change it. That's the shape.

---

## Pre-filled § I — The artifact

| | |
|---|---|
| **Title** | DxAI — A Responsible-by-Design Disease Identification Interface |
| **Medium** | Gradio Space (Python) with Claude Opus 4.5 API integration and multi-modal (text + image) input |
| **Deployments** | [huggingface.co/spaces/hsienberg/DxAI](https://huggingface.co/spaces/hsienberg/DxAI) *(fix runtime error before publishing paper — missing audio deps)* |
| **Dependencies** | Claude Opus 4.5 (Anthropic API) · Gradio · PIL · `transformers` · custom CSS (dark + green accents) |
| **Inference topology** | User input → Claude API call → ranked conditions + symptoms + recommendations, rendered with prominent medical disclaimers |
| **Reading time** | A long consultation |

## Three candidate research angles (pick one)

1. **Medical disclaimers are UI, not legal boilerplate.** Your DxAI puts disclaimers *at the top*, styled, impossible to ignore. Most medical AI puts them in the footer or TOS. The paper reads this as a *design claim*: the disclaimer is not a liability shield; it is part of the diagnostic output. Centerpiece claim: **the disclaimer is the diagnosis's margin of error, and showing it prominently is the honest move.**

2. **Responsible AI as interface, not guardrails.** The Claude integration already has safety training; your layer adds *a second, user-facing* layer of care — the disclaimers, the "possible conditions" language (not "diagnosis"), the recommended actions. The paper reads this as a deliberate layering: safety inside the model + care inside the interface. Centerpiece claim: **responsibility in medical AI is a stacked property, not a model property** — and interface designers carry a load the model designers can't.

3. **The World Cup metaphor, generalized.** Your Week 2 journal entry on the Smol AI WorldCup space — noting that the World Cup narrative made benchmark data legible — can be the seed of a paper on *narrative metaphors for technical information in healthcare*. DxAI's "Dr." persona, the disclaimer framing, the image upload UI all narrativize medical decision support. Centerpiece claim: **narrative metaphor is an under-discussed safety mechanism** in medical AI interfaces.

My guess: **#2** because it builds on the clearest evidence your Space actually offers. #1 is sharp but narrower. #3 is the most original but requires more data than you have.

## Suggested § II genre contrast

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| symptom checker / triage tool | authoritative, efficient, solution-shaped | answer-me | a conclusion |
| responsible-by-design probe | cautious, staged, aware of its limits | read carefully | a set of *possibilities* + an explicit recommendation to consult a physician |

## Your Δ

Candidate Δs:

- **The specific phrasing of your disclaimers.** The exact wording is your editorial hand.
- **The choice of Claude Opus 4.5 over a cheaper/smaller model.** Why that one? Reasoning capability? Safety training? Your answer is a paper-worthy choice.
- **The "possible conditions, ranked" output format.** Ranking with explicit uncertainty (not single-answer output) is a design decision most medical AI tools don't make.

The **ranked-with-uncertainty output format** is the strongest candidate. It's the structure that makes the tool honest.

## Suggested epigraph domain

Pull from:
- A physician-writer (Atul Gawande, *Complications* or *Being Mortal*; Oliver Sacks; Paul Kalanithi, *When Breath Becomes Air*; Siddhartha Mukherjee)
- A medical ethicist (Jerome Groopman, *How Doctors Think*)
- A history-of-medicine writer (Roy Porter)

Gawande's *Complications* has lines on diagnostic uncertainty that could be load-bearing for your paper. Groopman on clinical reasoning is another strong choice.

## Consensus searches to run

- `"large language model medical diagnosis safety"`
- `"clinical decision support AI disclaimers"`
- `"medical chatbot responsible AI interface"`
- `"diagnostic uncertainty communication patients"`
- `"multi-modal medical image text classification"`

Keep three. Look for papers on uncertainty communication in clinical AI — that's where your angle sits.

## Your § IX candidate category

1. **Staged safety.** *A design pattern in medical AI where the LLM's internal safety training is wrapped with explicit, prominent, interface-layer caution — on the premise that safety is a property of the full user-facing artifact, not of the model alone.* Claim: **staged safety is under-theorized and under-practiced, and its absence explains many consumer-facing medical AI failures.**

2. **The honest rank.** *An output pattern where ranked possibilities are returned with explicit uncertainty rather than a single-answer top pick — treating the tool as a differential-diagnosis assistant rather than an answer engine.* Claim: **ranked-with-uncertainty is a strictly more honest output format than top-1**, and it is rare because it is commercially unflattering.

Both work. #1 is broader; #2 is sharper.

---

## Questions to answer before drafting §§ III–XI

1. Which of the three angles is your angle?
2. Do you have the disease-diagnosis test inputs you ran DxAI on? Quotable outputs = §III gold.
3. Claude Opus 4.5 as the inference model — is that still what's deployed, or have you changed?
4. Gawande, Groopman, or Kalanithi — have you read any of them?
5. Can DxAI be debugged in one session?

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md)
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md)

Your technical stack (Claude API, multi-modal input, custom CSS, prominent disclaimers) is already mature. The paper is where the *design intent* behind that stack becomes legible.

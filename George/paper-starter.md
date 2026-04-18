# George — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`. Fill in the blanks; delete what doesn't fit.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md).

---

## Before drafting: three things to ship first

You have one deployed Space (`My_Health_Explainer`) and a pivot from music → medical AI that hasn't been written down. The paper needs some infrastructure under it. Do these first, in order:

1. **Create a GitHub repo** — name it `AI-Research-Level-2` or similar. Public. Seed with a README.
2. **Write your first journal entry: the pivot.** One page. *"I came into the course thinking about music. I shifted to health communication because ___. The question I now care about is ___."* Honest. First-person. This is the first draft of your §II "Why this form."
3. **Get `My_Health_Explainer` out of SLEEPING state** by opening it once. Confirm it still works. If broken, debug.

Once the repo exists and the journal has one entry, the paper has a place to live.

---

## Your paper in one sentence (proposed)

> *A health-explainer Space that adapts its output to a reader's inferred literacy level — probing whether AI tools can meaningfully shift register for different audiences, or whether "plain-language" modes are essentially the same prose with shorter sentences.*

Change it. That's the shape.

---

## Pre-filled § I — The artifact

| | |
|---|---|
| **Title** | My Health Explainer — An Audience-Adaptive Probe for Medical Plain-Language Generation |
| **Medium** | Gradio Space (Python) |
| **Deployments** | [huggingface.co/spaces/CuriousGorg/My_Health_Explainer](https://huggingface.co/spaces/CuriousGorg/My_Health_Explainer) |
| **Dependencies** | Fill in — which model powers the explainer? |
| **Reading-level targets** | Likely three: technical (physician register) · general-public (high school) · child-friendly (early-reader). Specify your exact set. |
| **Reading time** | A long conversation with a helpful stranger |

## Three candidate research angles (pick one)

1. **Register is shallow, not structural.** When an LLM is asked to explain a medical concept for a child, it shortens sentences and swaps vocabulary — but the underlying explanatory structure usually stays the same. Your paper could test this: does "plain language mode" actually re-frame the concept, or just re-word it? Centerpiece claim: **most AI "audience adaptation" is lexical, not conceptual — and this matters for whether these tools actually improve health literacy.**

2. **Why the pivot from music.** A different paper, and a personal one. You shifted from music to health mid-course. The paper uses that shift as its through-line: what about health communication felt more pressing than music generation? What is health communication *for*? Centerpiece claim: **the choice of AI application is itself a research decision** — and students who can articulate that choice produce better work.

3. **The Flesch-Kincaid lie.** Readability metrics (Flesch-Kincaid, Gunning fog) are commonly used to measure "plain language." They count syllables and sentence length. They don't measure *whether a reader understood*. Your paper could probe this: does the same output, scored "easy" by Flesch-Kincaid, actually reach a lay reader? Centerpiece claim: **readability scores are a proxy we've agreed to mistake for the real thing**, and your Space accidentally demonstrates the gap.

My guess: **#1** because it's the most concrete, testable, and close to what your Space already does. #3 is sharper but needs more methodology. #2 is the most personal — a good paper but a different genre.

## Suggested § II genre contrast

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| medical explainer (default) | authoritative, encyclopedic, full | look up a term, trust the result | a definition |
| audience-adaptive explainer | attentive to the reader, epistemically modest | ask once, read, ask again differently | an explanation *for someone* |

## Your Δ

Candidate Δs:

- **The exact reading levels you target.** "Child, general, expert" is a choice. "Early reader, ninth-grader, specialist, researcher" is a different choice. Your list is your signal.
- **The prompt wording that switches modes.** The exact phrasing of "Explain this for a 10-year-old" vs. "Explain this for a curious adult with no medical background" — that wording matters.
- **The examples you test the Space on.** If you test on *diabetes*, you get one pattern; on *rare autoimmune diseases*, a different pattern; on *mental health*, another. Your test set is your Δ.

## Suggested epigraph domain

Pull from:
- A physician-writer on patient communication (Atul Gawande; Paul Kalanithi; Danielle Ofri, *What Doctors Feel*)
- A health-literacy researcher (Rima Rudd's work)
- A science-communication text (Carl Sagan; Randall Munroe, *Thing Explainer* — directly relevant and playful)
- A patient memoir (Susan Sontag, *Illness as Metaphor*)

Munroe's *Thing Explainer* (which uses only the 1,000 most common English words) is a great and slightly surprising choice for your topic.

## Consensus searches to run

- `"health literacy large language models"`
- `"plain language medical information AI"`
- `"audience adaptation text generation evaluation"`
- `"readability metrics patient education materials"`
- `"consumer health information generation LLM"`

## Your § IX candidate category

1. **Lexical adaptation.** *The phenomenon wherein a language model rewords but does not restructure an explanation across reading levels.* Claim: **most "plain language" features in LLMs are lexical adaptation only, and the deeper conceptual reframing they promise is rarely delivered** — a gap detectable by testing on the same concept across levels.

2. **Audience-visible caution.** *A design pattern where a medical or technical explainer's uncertainty scales visibly with the inferred lay-ness of the audience.* Claim: **showing a lay audience more uncertainty is the correct design move, not less** — and your Space can demonstrate this.

Either works. #1 is more testable; #2 is closer to your music-to-health pivot's underlying concern (public understanding).

---

## Questions to answer before drafting §§ III–XI

1. Which model powers `My_Health_Explainer`?
2. Which of the three angles is yours?
3. What reading levels do you target, exactly?
4. Will you write the pivot-from-music entry as your first journal entry?
5. *Thing Explainer* — have you read it? If not, it's a short, worthwhile read and a strong epigraph source.

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md)
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md)

You have one real working Space and a genuine pivot story. That's more than enough to write about. The infrastructure (repo, journal) is what's gating you; build it, then the paper follows.

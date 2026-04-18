# Sevilla — Paper Starter

*A first pass at §§ I–II of your `PAPER.md`. Fill in the blanks; delete what doesn't fit.*

Read [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md) first. Then [the Bluest Hour paper](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md).

---

## Before drafting: two things to do first

Your Week 2 journal is on emotion detection — a course-prompted topic. Your real interest is **animation and visual storytelling**. Before the paper, you need at least one *analytical* journal entry on animation specifically:

1. **Write a catch-up entry on your animation experiments** — `AnimationwithMoods`, `MoodAnimation2`, and whatever tools you've been comparing (Claude, Gemini, ChatGPT, Deepseek, Copilot). Not descriptive ("I tried Claude, it was okay"). Analytical: *"I expected ChatGPT to handle motion-continuity better than Claude because of X, but Claude surprised me by doing Y, which suggests Z."*
2. **Pick one Space as the paper's §I.** Between `AnimationwithMoods` and `MoodAnimation2`, the second one (the iteration) is usually the better subject — it carries the lesson from the first.

Once one analytical entry exists and one Space is chosen, the paper has what it needs.

---

## Your paper in one sentence (proposed)

> *Five general-purpose AI assistants (Claude, Gemini, ChatGPT, Deepseek, Copilot) are evaluated for animation scene generation, with attention to which one handles motion continuity and temporal coherence — the qualities that separate an animation from a slideshow.*

Change it. That's the shape.

---

## Pre-filled § I — The artifact

| | |
|---|---|
| **Title** | MoodAnimation — A Cross-Assistant Comparison for Animation Scene Generation |
| **Medium** | HF Space (Python/Gradio) · uses external AI assistants for scene drafting |
| **Deployments** | Fill in — your `AnimationwithMoods` or `MoodAnimation2` URL |
| **AI assistants compared** | Claude · Gemini · ChatGPT · Deepseek · Microsoft Copilot |
| **Tools probed alongside** | WAN2.2 Animate · LTX 2.3 First-Last Frame (from your collection) |
| **Reading time** | As long as a short animated scene |

## Three candidate research angles (pick one)

1. **Motion continuity is the separator.** Most AI assistants can draft a scene. Few can draft a scene that *moves coherently* — where frame N+1 follows from frame N in a way an animator would recognize. Your paper tests this: give each of the five assistants the same motion-continuity task and compare. Centerpiece claim: **motion continuity is the axis along which general-purpose AI assistants differ most in animation workflows**, and it's the axis none of them measure themselves on.

2. **The tool-switcher's portrait.** You use Claude, Gemini, ChatGPT, Deepseek, and Copilot. This is unusual — most users settle on one. Your paper could be a *field report from the tool-switcher* — what each assistant does well for animation, where each fails, and what a working animator learns by refusing to pick one. Centerpiece claim: **the tool-switching workflow is under-documented** — and what it reveals is that different tools are tools for different *parts* of the animation pipeline, not alternative choices for the whole.

3. **Cartoonish is a stress test.** Your Week 2 observation that BLIP-based models struggle with cartoonish images is a thread worth pulling. If an AI model can't reliably classify *a cartoon*, it can't reliably *make* one either. The paper could use cartoonish-image detection failures as an *evaluation probe* for animation-generation systems. Centerpiece claim: **cartoonish content is a harder test case than photorealistic content for most vision/animation AI**, and this has implications for animation students using these tools as references.

My guess: **#1** because it's the most concrete and the most directly supported by your existing work. #2 is the most original — worth considering if you have good notes on all five tools.

## Suggested § II genre contrast

| form | claims to be | reader posture | what it returns |
|---|---|---|---|
| AI animation demo | magical, shareable, convincing | press play, be impressed | a clip |
| cross-assistant workflow probe | diagnostic, comparative, honest about failure | watch three clips side by side | evidence about where each tool breaks |

## Your Δ

Candidate Δs:

- **The five tools you use.** Not the industry-default three (ChatGPT, Claude, Gemini); your five-including-Deepseek-and-Copilot is unusual and your choice.
- **The test scenes you use.** If you test on "two characters walking," you get one thing; on "a door opening," another; on "a character turning to face the camera," another. Pick 3–5 motion primitives and test all tools on them.
- **Mood-driven animation** — the "MoodAnimation" framing is yours. Tying animation choices to a mood (not just a description) is an editorial move.

The **3–5 motion primitives you pick** is the strongest Δ candidate. That's your research instrument.

## Suggested epigraph domain

Pull from:
- A Disney animator's memoir (Glen Keane; Eric Goldberg's *Character Animation Crash Course*; Frank Thomas and Ollie Johnston, *The Illusion of Life*)
- A Japanese animation figure (Miyazaki interviews; Takahata; Mamoru Hosoda)
- A motion-theory writer (Rudolf Arnheim, *Film as Art*; Sergei Eisenstein on montage)
- A film-theory text on animation specifically (Paul Wells, *Understanding Animation*)

*The Illusion of Life* has the "twelve principles of animation" — any of them could epigraph a paper on motion continuity. Miyazaki on the *ma* (negative space) between actions is another rich source.

## Consensus searches to run

- `"text-to-video generation evaluation temporal coherence"`
- `"animation AI large language model scene generation"`
- `"motion continuity video diffusion models"`
- `"storyboard generation AI assistants"`
- `"generative video evaluation metrics"`

Keep three.

## Your § IX candidate category

1. **Motion continuity as evaluation axis.** *A test-suite genre for generative animation systems that focuses specifically on whether frame-to-frame or beat-to-beat coherence holds — distinct from scene quality, style fidelity, or prompt adherence.* Claim: **motion continuity is the under-measured axis along which generative animation tools most often fail**, and systematic probing of it is a viable research program.

2. **Tool-switching workflow.** *A working practice where a human collaborator distributes sub-tasks of a creative pipeline across multiple AI assistants, treating each as a specialist rather than a general-purpose agent.* Claim: **tool-switching is a more honest account of current AI-assisted creative work than the "which single assistant is best" framing that dominates benchmarks.**

Either works. #1 is sharper; #2 is more personal.

---

## Questions to answer before drafting §§ III–XI

1. Which of the three angles is yours?
2. Which Space — `AnimationwithMoods` or `MoodAnimation2` — is §I?
3. What are the 3–5 motion primitives in your test set?
4. Have you read *The Illusion of Life* or any Miyazaki interviews?
5. Can you get one analytical journal entry on animation (not emotion detection) written before drafting the paper?

---

## Reading list

- [`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)
- [`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)
- [Bluest Hour PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md)
- Your own [`RESEARCH-PATH.md`](./RESEARCH-PATH.md)

Your tool-switching habit is a research strength in disguise. The paper is where it becomes legible.

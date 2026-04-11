# Henry — AI + Research Level 2 Portfolio

## Your Topic

Visual perspectives and angles. Specifically: taking an image and imagining it from different vantage points—what would the same scene look like from a close-up, or from above, or from the side? Your word "camera angle" is metaphorical—you're thinking about perspective, the vantage point of the viewer, not literal 3D camera simulation. You're interested in novel view synthesis, multi-perspective generation, and how AI can reason about the same visual scene from different angles.

## Where You Are Now

You are in very good shape. You have two working independent Spaces that complement each other beautifully: one approaches the problem from the text side (Scene_describer, RUNNING), and one from the image side (Camera_angle_model_lab, SLEEPING). They are two directions into the same idea, which is architecturally smart.

Your Week 5 journal is exceptional. You tested your models at extreme slider values and documented what happened. You noticed when temperature destroyed output quality, when top-p flattened diversity, when max tokens cut off mid-thought. That is real experimental methodology. Most students observe things. You systematically probe them. You also named SmolLM2-135M-Instruct as your next candidate model based on evidence, not just guessing.

**But here is the gap:** Your repos are fragmented by week (Week 4 entry, Week 5 entry in separate places), and your writing, while detailed, hasn't yet crystallized into a research question. You are documenting experiments, but you haven't formulated the question you are investigating. You have the raw material—you just need to formalize it.

## Where You're Headed

Three deliverables:

1. **A research journal** — Consolidate your Week 4 and Week 5 entries into one cumulative journal that shows your investigation progressing. You don't need to rewrite anything. Move what you have into one place, and continue from there.

2. **A research question** — Bridge from "perspectives and camera angles" to something you can actually test. Something specific enough that you could fail to answer it. Not "Can AI understand perspectives?" but something like "When a text-generation model is given the same scene prompt but with different viewpoint instructions (close-up, bird's-eye, low angle), does the output contain meaningfully different visual details and spatial language, or does the model just swap a few surface words?"

3. **Three Spaces that tell a research story** — Scene_describer is your text-side baseline. Camera_angle_model_lab is your image-side experiment. What is Space 3? It could be a pipeline that connects the two: describe the same scene from multiple perspectives in text, then feed those descriptions as prompts into an image generator. That would be architecturally interesting—two modalities working together on the same problem.

## What's In This Folder

- **RESEARCH-PATH.md** — Your step-by-step guide to formalizing what you're already doing intuitively. Read this next.
- **SPACE-PROMPTS.md** — (Already here) Reference prompts for your Spaces and model recommendations.

## This Week's Priority

Three things, in order:

1. **Consolidate your repos.** Create one cumulative repository (instead of per-week repos) and move your Week 4 and Week 5 journal entries into a single `research-journal.md`. Don't rewrite. Just reorganize.
2. **Read RESEARCH-PATH.md** — It walks you through sharpening a research question from the experiments you've already done.
3. **Start asking the research question explicitly.** Write it down in your journal. Make it testable.

Your experimental methodology is strong. You think like a researcher. You just need to write like one — to state the question clearly and show how your experiments answer it.

---

*Built during AI + Research Level 2 at Youth Horizons Learning, Spring 2026.*

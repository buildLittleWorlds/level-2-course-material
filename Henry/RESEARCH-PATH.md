# Henry — Research Path

This is your step-by-step guide to moving from running experiments to writing about a research question. You have already done the hardest part—you have two working Spaces, detailed journal entries with real experimental methodology, and a clear vision. This is about formalizing what you already know.

---

## Step 1: Consolidate and Continue Your Journal

You have good entries scattered across per-week repositories. You need to gather them into one place.

**How:** Create a single cumulative repository (not per-week). Call it something like `AI-Research-Level-2-Final` or `Henry-Visual-Perspectives-Journal`. Move your Week 4 and Week 5 entries into a single file called `research-journal.md`.

**What to keep:** Everything. Your Week 5 slider experiments are strong—testing at extremes, documenting what breaks, what survives. Your Week 4 entry laid the groundwork. Don't rewrite it. Just reorganize it into one narrative flow:

- Week 4: Initial exploration
- Week 5: Slider experiments and findings
- Weeks 6+: Continuing from there

The point is continuity. A reader should be able to follow your thinking from "I'm curious about this" through "I tested it this way" through "Here is what I learned, and here is what I want to try next."

**Model to follow:** Prea consolidates her journal in one file across multiple weeks. You can see how she structures each entry with method, expectation, finding, reasoning, limitations, and next steps. Use her Week 3 and Week 5 entries as a template (look in `example-student-prea/research-journal.md`). You don't need to rewrite yours in her exact style. Just make sure each entry answers these questions:

- What method did I use? (Which Space? Which model? Which prompts?)
- What did I expect?
- What did I find?
- Why did this happen?
- What are the limitations of this approach?
- What do I want to try next?

---

## Step 2: Sharpen a Research Question

You have been exploring "perspectives and camera angles" for weeks. It is time to crystallize that into a question you could actually test.

### The Progression

**Broad (too broad for a portfolio):** "Can small AI models understand visual perspectives and describe scenes from different angles?"

This is real, but it is a research program, not a research question. It does not tell you what you are measuring, what counts as success, or what models you are testing.

**Medium (testable, but still diffuse):** "When a text-generation model is given the same scene prompt but with different viewpoint instructions (close-up, bird's-eye, low angle), does the output contain meaningfully different visual details and spatial language, or does the model just swap a few surface words?"

This is better. You have a clear input (viewpoint instructions in prompts), a clear comparison (different viewpoints), and two things you are measuring (visual detail and spatial language). It is concrete. But "does it or doesn't it" is still a yes/no question. Research usually asks *how much* or *in what way*.

**Narrow (specific enough to be your portfolio question):** "Testing three small instruction-tuned models (distilgpt2, SmolLM2-135M-Instruct, SmolLM2-360M-Instruct) on 10 scene prompts across 5 viewpoints (close-up, wide shot, bird's-eye, low angle, over-the-shoulder), scoring each output for viewpoint-specific visual detail, spatial language accuracy, and prompt-following, to determine whether instruction-tuned models handle perspective shifts better than base models."

This is your actual research question. It is specific about:
- Which models you are testing (three of them)
- How many prompts (10 diverse scenes)
- Which viewpoints (5 different angles)
- What you are measuring (three scoring rubrics)
- The comparison you care about (does instruction-tuning improve perspective-handling more than base models?)

### Your Customized Prompt

Once you settle on a question, you need a prompt template. Here is a skeleton:

```
You are a visual scene describer. Your task is to describe a scene 
from a specific viewpoint: [VIEWPOINT].

When describing from a [VIEWPOINT], focus on:
- What details are visible from this angle?
- What spatial relationships matter from this perspective?
- What would be in the foreground, middle ground, background?

Scene: [SCENE-DESCRIPTION]
Now describe what you see from the [VIEWPOINT]:
```

Test this on scenes like:
- "A crowded city street intersection at rush hour"
- "A forest clearing with a small stream"
- "A coffee shop interior with customers at tables"
- "A mountain vista from a valley"
- "An abstract architectural space with multiple levels"

Then vary the viewpoint and see if the model produces meaningfully different outputs or just surface-level word swaps. This is exactly what your Week 5 experiments began to probe. Now make it systematic.

---

## Step 3: Connect to Published Research

You need to know what already exists. This is not about reinventing the wheel—it is about standing on existing shoulders.

**Run these Consensus searches** and keep rough notes on what you find:

- `"novel view synthesis image generation"`
- `"multi-view image generation deep learning"`
- `"spatial reasoning language models"`
- `"visual description generation from different viewpoints"`
- `"perspective-taking in AI models"`

**What you are looking for:** Papers that ask questions adjacent to yours. You probably won't find a paper on "small text models describing scenes from camera angles"—that is too specific. But you might find papers on:
- How vision models generate novel views
- How language models capture spatial information
- How humans describe scenes from different perspectives
- How to evaluate spatial reasoning in AI
- Multi-modal approaches to perspective understanding

**Write down:**
- Paper title and authors
- What question they asked
- How their approach differs from yours (different modality? different models? different evaluation method?)
- One key finding

Three to five solid sources is enough for a portfolio research brief.

---

## Step 4: What Your Three Spaces Should Look Like

You have two strong Spaces. Now you need a third that completes the story.

**Space 1 — Text-Side Baseline:** Scene_describer (RUNNING)

What it shows: A small text-generation model describing scenes when given a basic prompt. Demonstrates the baseline behavior.

What it is good for: Showing what the model produces with minimal guidance on perspective.

**Space 2 — Image-Side Experiment:** Camera_angle_model_lab (SLEEPING)

What it shows: Image-generation models responding to perspective-aware prompts. A different modality, same idea.

What it is good for: Demonstrating that the perspective problem exists in both directions—text and image both struggle with viewpoint shifts in interesting ways.

**Space 3 — The Pipeline:** A space that connects the two.

What it could do: 
- User inputs a scene description and selects a viewpoint
- Space 1 generates text descriptions from that viewpoint across multiple models
- Space 2 takes those descriptions as prompts for image generation
- User sees the text output and the resulting images side-by-side

What it is good for: Showing an *architectural idea*—that understanding perspective in text and image generation are related problems, and that a pipeline connecting them reveals something about how both modalities handle spatial reasoning.

This mirrors what Prea did in her portfolio: two separate ideas (text-side and image-side) that eventually connect into a unified pipeline. It shows you are not just building random Spaces. You are investigating a specific problem from multiple angles.

---

## Step 5: Your Unique Angle

You have something special: **strong experimental methodology.**

Your Week 5 slider experiments aren't just "I tested some things." You tested at extremes. You documented what breaks. You noticed when a model gives up (token limit), when it gets confused (temperature too high), when it gets boring (top-p too low). That is real experimental design.

**Your unique contribution is not "I built AI tools for perspectives." Your unique contribution is "I built AI tools and tested them rigorously, using systematic variation of controls, and I can tell you what actually changes the output versus what is just noise."**

When you write up your research brief, lead with that. Not "I'm interested in how AI handles camera angles." But "I systematically tested how small language models respond to viewpoint-specific instructions, documenting how instruction-tuning, temperature, and token limits affect perspective-awareness in scene description."

That is a researcher talking. That is what a portfolio reader notices.

---

## Step 6: What Prea Did That You Should Notice

Prea's portfolio pivot happens between Week 5 and Week 7. In Week 5, she has two separate ideas (text-side and image-side). By Week 7, she connects them into a unified pipeline.

Read her Week 5 entry ("Space 1 and a Blog Post That Changed My Plan") and her Week 7 entry. Notice:

- In Week 5, she has an insight (the blog post changes her thinking) and she writes it in ALL CAPS because it matters
- She explicitly states what problem this creates for her ("Mistral's API is not free")
- She ends with a specific next step
- In Week 7, she builds the pipeline that connects her two directions

**The architectural move:** Two modalities, one question. That is exactly where you are heading.

Your two Spaces (text and image) are already two directions into the same problem. The pipeline in Space 3 is the proof that they belong together. When you write your research brief, you can say: "I investigated visual perspective-taking from two angles—text description and image generation—and built a pipeline showing how they inform each other."

That is the story Prea tells. It is also the story you are positioned to tell.

---

## What Comes Next

Once you have consolidated your journal and sharpened your research question:

1. **Run the systematic test.** Take your three models, your 10 scenes, your 5 viewpoints. Run them all. Keep a simple results table (your Week 5 methodology was already doing this). Document what you find.

2. **Research brief** — A 3-4 page document in the format of a mini research paper. Abstract, Introduction (with your research question), Related Work (from Consensus searches), Methods (what you tested and how you measured it), Results (what you found), Limitations (what you could not test or what biases might affect your findings).

3. **Space finalization** — Make sure each of your three Spaces has clear, short documentation of what it does and what it shows about your research question. Not "a tool I built." But "a component of my investigation into perspective-taking in AI."

4. **Journal completion** — Your journal should tell the story from "I wonder how models understand perspective" through "I tested it this way, using systematic controls" through "Here is what I found about how instruction-tuning and temperature affect perspective-awareness."

You have done the hard building work. The writing is the final step, and it is where you earn the "research" part of "AI + Research Level 2."

You have got this.

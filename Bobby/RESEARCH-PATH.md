# Your Research Paths

Two directions. Pick one. (If neither fits, let's talk.)

---

## PATH A: Game Development + AI — "Can small AI models write useful game content?"

You have game dev expertise that most students in this cohort don't. You know what game writing needs to *do* — it has to fit a world, guide a player, set a tone. Most students studying "generative AI" don't know that. You do. That's your angle.

### Broad Research Question

**Can small, free AI models generate useful game assets — dialogue, item descriptions, quest text — for a game developer to use or edit?**

This is wide. It includes multiple modalities (text, maybe 3D descriptions), multiple model sizes, multiple game genres. Too wide for 5 weeks, but this is the umbrella.

**Customized prompt for this level:**
> I'm a game developer interested in whether small AI language models (under 1B parameters) can help me write game content. What should I actually test to know whether a model is useful for *my* work? Give me three specific game-writing tasks that would let me compare models fairly.

### Medium Research Question

**Do instruction-tuned models produce more genre-consistent game narrative than base models? And does the choice of genre — fantasy vs. sci-fi vs. horror — change which model wins?**

Narrower. You pick one type of game writing (e.g., NPC dialogue), you test 3–4 models across 3 genres, you measure "genre consistency" somehow (prompt coherence, sentiment alignment, thematic words), you ask: does the instruction-tuning help? Does genre matter?

**Why this matters:** Most small models are either base models (like distilgpt2) or instruction-tuned (like SmolLM2). You probably think instruction-tuned is always better. Spoiler: sometimes base models are more creative because they're less rule-bound. Test it.

**Customized prompt for this level:**
> I want to test whether instruction-tuned language models (like SmolLM2-360M-Instruct) produce more genre-appropriate game writing than base models (like distilgpt2) across different genres. What's a fair way to set up this test? How would I measure "genre appropriateness" without manually reading 100 outputs?

### Narrow Research Question

**Testing protocol: Pick one game-writing task (e.g., NPC dialogue). Test 3 models (distilgpt2, SmolLM2-360M-Instruct, Qwen2.5-0.5B-Instruct) on the same 5 game-writing prompts across 5 different genres (fantasy, sci-fi, horror, mystery, cyberpunk). For each output, measure:**
- **Genre consistency** — Does the output match the genre? (Yes/No, or 1–5 rating)
- **Prompt following** — Did the model actually write dialogue (or quest text, or whatever you asked for)? (Yes/No)
- **Usefulness** — Would a game developer actually use this, or is it too generic/off-topic? (1–5)

Then: rank the models. Which one produced the most usable outputs per genre? Did instruction-tuning matter? Did genre?

**Your three Spaces would look like this:**
1. **Space 1 (Baseline):** Single-model text generator using distilgpt2 (the "old way"). Shows the raw output and why it's good enough but not great for game writing.
2. **Space 2 (Better Model):** Same interface but using SmolLM2-360M-Instruct. Let users pick genre, see how much better the instruction-tuned version is.
3. **Space 3 (Model Comparison Lab):** Side-by-side output from all 3 models on the same prompts, same genre. Let users rate which outputs they'd actually use in their game.

**Your journal would document:** Which prompts worked best? Where did models fail? Was genre actually a variable that changed things, or did all models struggle equally? Did you learn anything about how to *write prompts* so models give you game-usable output?

**Your research brief would answer:** "Across these 3 models and 5 genres, instruction-tuning improved usability by X%, and genre consistency mattered most in Y scenarios. Here's what a game developer should know."

**Customized prompt for comparison testing:**
> Write me a Hugging Face Space using Gradio that compares three language models (distilgpt2, SmolLM2-360M-Instruct, Qwen2.5-0.5B-Instruct) on game-writing prompts. I want to test whether instruction-tuned models produce better game dialogue, item descriptions, or quest text than base models. The Space should let me pick an output type (dialogue/item/quest), pick a genre (fantasy/sci-fi/horror), type a prompt, and see the three models' outputs side by side so I can compare them.

---

## PATH B: Generative AI Across Modalities — "How do AI generation tools compare across text, image, and 3D?"

Your collections show you explored code generation, image generation, 3D model generation, and text. What if that breadth is your actual question? How do these modalities *compare*?

### Broad Research Question

**How do different AI generation tools compare across modalities — text, image, 3D — when given the same creative brief?**

This is the widest umbrella. It includes text generators (GPT, Mistral, etc.), image generators (DALL-E, Stable Diffusion), 3D generators (Tripo, Meshy), and asks: when you give the same prompt to each, what do you learn about how different modalities "interpret" the same idea?

**Customized prompt for this level:**
> I'm interested in how text-to-image, text-to-3D, and code-generation models interpret the same prompt differently. What's a fair way to compare their outputs if I can't directly compare a generated image to a generated 3D model? What would I actually measure?

### Medium Research Question

**Do different generation modalities respond differently to the same creative brief? And which "modality gap" is largest — text-to-image vs. image-to-3D vs. text-to-code?**

Narrower. You write 5 detailed creative briefs (e.g., "an alien spaceship with bioluminescent panels and organic curves"). You run each brief through:
- A text generator (e.g., asking for a detailed scene description)
- An image generator (e.g., DALL-E or Stable Diffusion via free API)
- A 3D generator (e.g., Tripo or Meshy, if free tier works)

Then you measure: Do they agree on what the brief describes? Where do they diverge most? Is there a text-to-image gap bigger than an image-to-3D gap?

**Why this matters:** Most students test *one* modality. You'd be testing whether modality itself is the variable. Do all generators agree on what "bioluminescent" means? Or does the image generator interpret it one way and the 3D generator another?

**Customized prompt for this level:**
> Help me design an experiment that tests whether text-to-image, text-to-3D, and text-to-text models interpret the same creative brief differently. I want to measure "semantic consistency" across outputs. How would I score whether all three modalities "understood" the same brief the same way?

### Narrow Research Question

**Testing protocol: Write 5 detailed creative briefs (each 100–200 words). For each brief, generate:**
- A **text description** (using Claude or another LLM, asking for a detailed scene writeup)
- An **image** (using DALL-E, Stable Diffusion, or free alternative)
- A **3D model description** (using a 3D generator or asking an LLM to describe what the 3D model would look like)

Then: analyze the outputs. For each brief, score on:
- **Semantic agreement** — Do all three modalities agree on key features? (e.g., if the brief says "bioluminescent panels," did the image generator include them? Did the 3D model?)
- **Style consistency** — Do all three modalities preserve the aesthetic? (e.g., "organic curves" — did all three stick with organic vs. geometric?)
- **Modality-specific gaps** — Which pairs disagree most? (text-to-image vs. text-to-3D, etc.)

Then: rank the modalities. Which one was most faithful to the brief? Which modality gap was largest?

**Your three Spaces would look like this:**
1. **Space 1 (Text-to-Scene):** Takes a creative brief, generates a detailed text scene description using an LLM.
2. **Space 2 (Brief-to-Image):** Takes a brief, generates an image using DALL-E or Stable Diffusion (or links to them).
3. **Space 3 (Modality Comparison):** Side-by-side display of text, image, and 3D representations of the same brief. Let users see the gaps.

**Your journal would document:** Which modality was easiest to work with? Which was most unpredictable? Did you learn anything about how to *write briefs* so all modalities interpret them the same way?

**Your research brief would answer:** "Across 5 briefs and 3 modalities, images and 3D models agreed X% of the time, while text descriptions agreed Y% of the time. The largest gap was between [modality pair]. Here's what that means for creative teams using multiple AI tools."

**Customized prompt for cross-modality testing:**
> Write a Hugging Face Space or simple web app that lets me explore whether text-to-image, text-to-text, and 3D-generation models interpret the same creative brief the same way. I should be able to input a detailed brief (100–200 words), and the app should show me the text description, the generated image, and (either a 3D model or a 3D model description) side by side. This is about revealing the "modality gaps."

---

## Step 2: Pick Your Path

Read both paths above. Which one feels like the research question *you* actually want to answer?

**If it's PATH A (Game Dev + AI):** Your domain expertise is game writing. Test whether models help. Your Spaces become a testing ground. Your brief answers: "Here's which models actually work for game developers."

**If it's PATH B (Cross-Modal Generation):** Your curiosity is modality. Test whether they agree. Your Spaces become a showcase of where they diverge. Your brief answers: "Here's where text, image, and 3D generators see the world differently."

**If it's neither:** That's okay. These are suggestions, not requirements. If you're thinking about something else entirely, that's fine — just let's talk about it.

---

## Step 3: Connect to Published Research

Once you pick a path, here's what published research backs each direction:

### For PATH A (Game Dev + AI):
- **Procedural Content Generation (PCG):** Look for papers on "procedural narrative generation" and "automated game content generation." This is a real field.
- **NLP for games:** Papers on dialogue generation for NPCs, quest generation, or game-writing systems.
- **Model size vs. game utility:** Very little published work compares small models specifically for game-writing tasks. That's why your research would be novel.
- **Search terms for Consensus:** "procedural narrative generation," "dialogue generation games," "LLM game content," "small language models game writing"

### For PATH B (Cross-Modal Generation):
- **Multi-modal AI:** Papers comparing text-to-image, text-to-3D, and text-to-text models.
- **Semantic consistency across modalities:** Look for papers on "cross-modal alignment" or "multi-modal evaluation."
- **Modality gaps:** Very little published work directly compares how different modalities interpret *the same prompt*. That's your angle.
- **Search terms for Consensus:** "text-to-image evaluation," "cross-modal generation," "multi-modal consistency," "semantic alignment generative models," "modality transfer"

---

## Step 4: What Your Three Spaces Should Look Like

Whichever path you pick, your three Spaces follow a pattern:

1. **Space 1 (Baseline):** The simplest version. Proves the idea works. For game writing, that's a single-model text generator. For modalities, that's a single-modality generator. Shows: "This is the raw material."

2. **Space 2 (Better/Different):** Same idea, but with an improvement or alternative. For game writing, that's a better model. For modalities, that's a different modality. Shows: "How does this change things?"

3. **Space 3 (Comparison/Integration):** Brings both together. Side-by-side, same input, different outputs. Let users see the difference. Shows: "Here's what we learned."

All three Spaces should be **buildable in 3–4 weeks** with the tools you know. Use SPACE-PROMPTS.md if you're coding. Use free APIs and free Hugging Face compute. Keep them simple.

---

## Step 5: Your Unique Angle

Most students in this cohort are studying "AI in general." You're different: **you have real game development context.** You know what game writing needs to accomplish. You've shipped a game jam project. You understand the constraints.

That's your superpower. Don't waste it. Use it.

If you go with PATH A, your research brief will say something other students *can't* say: "Here's which models actually work for real game developers, because I've built real games and I know what matters."

If you go with PATH B, your angle is: "I explored across modalities because game development uses *all* of them — dialogue is text, visual design is images, 3D assets are models. Here's how they talk to each other."

---

## What Prea Did That You Should Notice

Prea came in wanting to build "a sentiment classifier for debate speeches." That turned out to be the wrong tool (classifiers can't evaluate). She pivoted in Week 3 to prosody + audio. Built her first Space using a wrong approach (baseline), learned from it, rebuilt with the right architecture in Weeks 5–7, tested in Weeks 8–10, wrote up in Week 11.

Her journal documents *all of that* — including the detours and the failures. That's what makes it real.

You're at a similar fork. You were exploring broad territory in Weeks 1–3. You went quiet. The next move is to decide: do you narrow down to one of the paths above, or do you see a third path we haven't talked about?

Write that down. That's your re-entry journal entry.

---

*Pick a path. Read the published research. Sharpen your question. Build your Spaces.*

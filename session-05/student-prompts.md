# Session 5: Personalized Space Prompts

Copy your prompt below and paste it into ChatGPT, Gemini, Claude, or any AI assistant. It will give you the code for two files: `app.py` and `requirements.txt`. Then create a new Hugging Face Space (Gradio SDK, Free CPU) and paste the code into those two files.

---

## Bobby

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Game Narrative Generator" and be designed for writing game stories — character dialogue, quest descriptions, item lore, and scene-setting.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.7) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "The warrior entered the dungeon and"
- "You found a legendary sword. Its description reads:"
- "The village elder whispered the secret of the forest:"
- "QUEST LOG: Your mission is to"
- "The final boss appeared, and it was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Annabelle

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Creative Story Starter" and be designed for creative writing — fun stories, music ideas, playful scenarios, and imaginative prompts.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.9) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "She opened the letter and read"
- "The dinosaur walked into the concert hall and picked up a guitar"
- "The song started with a single note that"
- "In a world where animals could talk, the cat said"
- "The most unexpected ingredient in the recipe was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Shawn

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Anime Scene Writer" and be designed for writing anime-style scene descriptions, character introductions, and episode summaries.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.8) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "The hero drew their sword as the wind swept across the battlefield and"
- "Episode 1: A transfer student arrives at the academy and discovers"
- "The villain revealed their true form, and the sky turned"
- "In a quiet moment between battles, the two characters sat together and"
- "The opening sequence begins with cherry blossoms falling over"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Emily

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "News Draft Generator" and be designed for experimenting with news-style writing — headlines, article openings, research summaries, and briefings.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "Breaking news: scientists discovered that"
- "A new report released today found that students"
- "The conference on artificial intelligence announced"
- "Researchers at the university published a study showing"
- "This week in technology: the biggest story is"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Chengry

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Medical Text Generator" and be designed for experimenting with medical and health-related text — clinical notes, symptom descriptions, patient scenarios, and health explanations.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "The patient presented with symptoms of"
- "Common side effects of this medication include"
- "The doctor examined the test results and concluded"
- "A healthy diet for someone with diabetes should"
- "The difference between a virus and a bacteria is"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## George

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Health Explainer" and be designed for generating health and wellness explanations — how the body works, what injuries do, how treatments help, and general health literacy.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "When you sprain your ankle, what happens inside is"
- "The most important thing about first aid is"
- "Your immune system works by"
- "The reason sleep is important for recovery is"
- "A sports injury should be treated by"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Henry

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Scene Describer" and be designed for generating visual scene descriptions — what a camera sees, how to describe images in words, and how angles and perspectives change a scene.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.7) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "The camera slowly panned across the scene and revealed"
- "From a bird's eye view, the city looked"
- "The photograph captured a moment where"
- "Looking at the image from a different angle, you notice"
- "The most striking detail in the picture was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Sevilla

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Animation Scene Writer" and be designed for writing animation and video scene descriptions — character actions, visual sequences, storyboard narration, and motion descriptions.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.8) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "The character stepped into the frame and began to"
- "In the opening shot, the camera zooms in on"
- "The animation sequence shows a figure who"
- "As the scene transitions, the mood shifts from"
- "The final frame of the video reveals"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Why Does the Output Sound So... Bad?

You probably noticed: the text your Space generates isn't great. It's choppy, repetitive, sometimes nonsensical. If you've used ChatGPT, Claude, or Gemini, you know AI can write much better than this. So what's going on?

### The model we're using is tiny

Our model, `distilgpt2`, has **82 million parameters** (the numbers the model learned during training). That sounds like a lot, but compare it to what you're used to:

| Model | Parameters | How it writes |
| :--- | :--- | :--- |
| **distilgpt2** (what we're running) | 82 million | Choppy, repetitive, often doesn't make sense |
| GPT-2 (the full version) | 1.5 billion | Better, but still clearly robotic |
| Llama 3 (Meta's open model) | 8–70 billion | Good quality, sounds natural |
| GPT-5.4 (OpenAI's current flagship) | Not disclosed | Very good — what you're used to |
| Claude Opus 4.6 (Anthropic) | Not disclosed | Very good — comparable to ChatGPT |

The models you use every day are roughly **1,000 to 10,000 times larger** than what we're running. That's the difference.

### Why can't we just run a bigger model?

Our Spaces run on Hugging Face's **free CPU tier** — a regular computer processor with 16 GB of memory. That's enough for distilgpt2 (82M parameters), but a model like Llama 3 8B needs a **GPU** (a specialized chip designed for AI math) with much more memory.

### The Real Cost of Compute (April 2026)

> The AI landscape moves fast. While the temperature and top-p sliders we're learning today work the same on every model, the "market rate" for running these models has real costs behind it.

#### Option 1: Run the model yourself (GPU rental on Hugging Face Spaces)

If we moved beyond the Free CPU tier to run larger models directly in a Space, we'd pay by the minute for GPU hardware:

| Hardware | Cost | What it can run |
| :--- | :--- | :--- |
| **Free CPU** (what we use) | $0/hour | distilgpt2, GPT-2, small classifiers |
| **Nvidia T4 GPU** | $0.40–0.60/hour | Medium models (up to ~7B parameters) |
| **Nvidia L4 GPU** | $0.80–3.80/hour | The current sweet spot for speed and memory |
| **Nvidia A10G GPU** | ~$1.00/hour | Large models (up to ~13B parameters) |
| **Nvidia A100 GPU** | $10–20/hour | Very large models, multi-GPU (70B+ parameters) |

If all 8 of us ran a decent model on an L4 GPU, that's roughly **$6–30/hour for the class**. And you're paying every minute the Space is running, even when nobody is using it.

#### Option 2: Call someone else's model (API pricing)

Instead of renting hardware, you can **call a model over the internet** — send text in, get text back. This is how ChatGPT and Claude actually work. You pay per token (a token is roughly 3/4 of a word).

Here's what the major APIs charge per million tokens as of April 2026:

| Tier | Model | Input (per 1M tokens) | Output (per 1M tokens) |
| :--- | :--- | :--- | :--- |
| **Flagship** | [GPT-5.4](https://openai.com/api/pricing/) (OpenAI) | $2.50 | $15.00 |
| **Flagship** | [Claude Opus 4.6](https://platform.claude.com/docs/en/about-claude/pricing) (Anthropic) | $5.00 | $25.00 |
| **Workhorse** | [Claude Sonnet 4.6](https://platform.claude.com/docs/en/about-claude/pricing) (Anthropic) | $3.00 | $15.00 |
| **Workhorse** | [Mistral Large 3](https://docs.mistral.ai/deployment/ai-studio/pricing) | $2.00 | $6.00 |
| **High Efficiency** | [GPT-4o mini](https://openai.com/api/pricing/) (OpenAI) | $0.15 | $0.60 |
| **High Efficiency** | [Mistral Small 3.1](https://docs.mistral.ai/deployment/ai-studio/pricing) | $0.20 | $0.60 |
| **Budget** | [Claude Haiku 4.5](https://platform.claude.com/docs/en/about-claude/pricing) (Anthropic) | $1.00 | $5.00 |
| **Budget** | [GPT-5 mini](https://openai.com/api/pricing/) (OpenAI) | $0.25 | $2.00 |

A million tokens is roughly 750,000 words — about 10 novels. For what we do in class (maybe 50–100 short generations per student), the cost would be **a few cents per session**. That's cheap! But it adds up fast when you're building a product that thousands of people use.

#### The bottom line: why AI companies raise billions

When you use ChatGPT for free, OpenAI is paying for the compute. Estimates suggest each conversation costs them **$0.01–0.10** depending on length. Multiply that by hundreds of millions of users, and OpenAI spends **billions of dollars per year** on compute — mostly renting massive GPU clusters.

That's why:
- ChatGPT Plus costs $20/month (they're trying to cover costs)
- Free tiers have usage limits (they can't afford unlimited compute for everyone)
- AI companies raise billions in funding (much of it goes straight to buying GPUs)

The **compute paradox**: running a dedicated GPU instance for your own "private" model (like our Spaces) is still expensive — you're paying for hardware whether anyone is using it or not. The shared "pay-as-you-go" API model is cheaper per query because the provider spreads the hardware cost across millions of users. That's the business model behind every AI company.

### So what's the point of our tiny model?

The point of Session 5 isn't to compete with ChatGPT. It's to **understand what's under the hood**. When you move the temperature slider on your Space, you're doing the exact same thing that happens inside ChatGPT — just on a model you can see, control, and run yourself. The sliders work the same way whether the model has 82 million parameters or 82 billion.

You're learning the universal controls. The model will get bigger later. The understanding stays.

# Annabelle

## Goal

Build your "Creative Story Starter" first, then turn it into a small model lab where you can compare which models actually sound playful, imaginative, musical, or weird in a good way.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer than `distilgpt2`, usually better at following a creative direction.
- `HuggingFaceTB/SmolLM2-135M-Instruct` — fastest lightweight option; good for quick experiments and lots of prompt testing.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better output, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, stay around 135M to 500M parameters when possible.
- Avoid models that need special inference servers, gated access, or GPU-only workflows.
- For your project, instruction-following matters a lot because you want the model to follow playful style directions.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-135M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better First Version

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for creative writing called "Creative Story Starter".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.9
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 120

Add these example prompts:
- "She opened the letter and read"
- "The dinosaur walked into the concert hall and picked up a guitar"
- "The song started with a single note that"
- "In a world where animals could talk, the cat said"
- "The most unexpected ingredient in the recipe was"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model writes in a playful, imaginative, slightly whimsical style
- keep the code easy for a student to read
- include a short note in the UI explaining that newer instruct models often follow style directions better than distilgpt2

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Creative Model Tasting Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same creative-writing prompt.

The Space should be called "Creative Model Tasting Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-135M-Instruct
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Creative Mode" with these options: whimsical story, music idea, silly scene, surreal image prompt, playful dialogue
- use the creative mode to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining the tradeoff between speed and quality
- use Gradio only

Include these example prompts:
- "She opened the letter and read"
- "The dinosaur walked into the concert hall and picked up a guitar"
- "The song started with a single note that"
- "In a world where animals could talk, the cat said"
- "The most unexpected ingredient in the recipe was"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for a better small text-generation model for a playful creative-writing Space that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- ideally under about 500M parameters
- good at instruction following, playful writing, or imaginative text
- realistic for a Hugging Face Space on free CPU Basic

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit playful creative writing.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 4: Turn One Space Into Several Mini Projects

Use this to help an AI coding assistant redesign the app without doing all the thinking for you:

```text
Rewrite my Hugging Face Space prompt so the same creative-writing app can switch between different output modes:
- story starter
- silly phrase generator
- music idea generator
- talking animal dialogue
- weird recipe idea

Keep it beginner-friendly and still based on a small CPU-friendly Hugging Face model.
Add one dropdown for output mode and update the hidden instruction prefix so each mode creates a different kind of effect.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## Prompt 5: Ask AI To Help You Do A Fair Comparison

This one matches the "tasting note" style you already use:

```text
Help me design a simple fair test for comparing small Hugging Face text-generation models in a creative-writing Space.

I want to compare them on:
- playfulness
- originality
- usefulness
- how well they follow the prompt
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Three prompts that are good for comparing creative models.
3. A simple table format I can paste into my GitHub journal.
4. Advice on how to keep the comparison fair by changing only one variable at a time.
```

## What To Notice While Testing

- Which model sounds the most playful without turning into nonsense?
- Which model responds best when you give it a style direction?
- Does the faster model help you experiment more, even if the output is weaker?
- At what temperature does the writing become more fun, and at what point does it just get messy?
- Which creative mode feels the most like something you would actually keep building?

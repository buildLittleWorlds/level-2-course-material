# Shawn

## Goal

Build your "Anime Scene Writer" first, then turn it into a comparison lab where you can test the same prompt across several small models and document what actually changes.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer and usually better at following anime-style scene directions than `distilgpt2`.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better quality, but slower on free CPU.
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0` — optional big stretch test; more powerful, but noticeably slower and heavier.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, models around 135M to 500M are the safest everyday choice.
- You can test a 1.1B model like TinyLlama on free CPU, but treat it as a slower experiment, not your default classroom recommendation.
- For your project, the best model is not just the strongest one. It is the one that gives the clearest improvement when everything else stays the same.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`: <https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better First Version

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for anime-style writing called "Anime Scene Writer".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.8
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 120

Add these example prompts:
- "The hero drew their sword as the wind swept across the battlefield and"
- "Episode 1: A transfer student arrives at the academy and discovers"
- "The villain revealed their true form, and the sky turned"
- "In a quiet moment between battles, the two characters sat together and"
- "The opening sequence begins with cherry blossoms falling over"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model writes in an anime episode or scene-description style
- keep the code easy for a student to read
- include a short note in the UI explaining that newer instruct models usually follow style directions better than distilgpt2

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Model Comparison Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same anime-writing prompt.

The Space should be called "Anime Scene Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct
- TinyLlama/TinyLlama-1.1B-Chat-v1.0

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Scene Mode" with these options: battle scene, school intro, villain reveal, quiet character moment, episode summary
- use the scene mode to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct or chat model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining that distilgpt2 is the baseline, SmolLM2 is the recommended upgrade, Qwen is the stronger small model, and TinyLlama is the slow stretch comparison
- use Gradio only

Include these example prompts:
- "The hero drew their sword as the wind swept across the battlefield and"
- "Episode 1: A transfer student arrives at the academy and discovers"
- "The villain revealed their true form, and the sky turned"
- "In a quiet moment between battles, the two characters sat together and"
- "The opening sequence begins with cherry blossoms falling over"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Side-By-Side Testing Version

Use this if you want the comparison to feel more like a real experiment:

```text
Write me a Hugging Face Space using Gradio and transformers that runs the same anime prompt through two selected models side by side.

I want:
- Model A dropdown
- Model B dropdown
- one shared prompt input
- shared temperature, top-p, and max_new_tokens controls
- two output boxes shown next to each other
- a short note reminding users to change only one variable at a time

Use only small CPU-friendly models:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Keep the code simple enough for a student to understand and edit later.
Give me the complete app.py and requirements.txt files.
```

## Prompt 4: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for a better small text-generation model for an anime scene writing Space that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- ideally under about 500M parameters, but I am open to one slower stretch option
- good at instruction following, storytelling, scene writing, or dialogue
- realistic for a Hugging Face Space on free CPU Basic

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit anime-style scene writing.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 5: Ask AI To Help You Design A Fair Comparison

This one fits the method you already use:

```text
Help me design a fair comparison for small Hugging Face text-generation models in an anime-writing Space.

I want to compare them on:
- style
- prompt-following
- coherence
- originality
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Three anime-style prompts that are good for comparing models.
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to keep the comparison fair by changing only one variable at a time.
5. One example of a good conclusion paragraph based on fake sample results.
```

## What To Notice While Testing

- Which model best captures anime-style pacing or tone?
- Which one follows the exact scene type you asked for instead of drifting?
- Does the stronger model improve coherence enough to justify slower speed?
- What changes more: the output when you swap the model, or the output when you change temperature?
- Which conclusion can you actually defend with evidence from repeated tests?

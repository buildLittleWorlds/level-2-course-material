# Bobby

## Goal

Build your "Game Narrative Generator" first, then rebuild it with a newer model so you can compare how model choice changes the writing.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer, stronger, and still realistic for free CPU.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; usually better output, but slower.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer models.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, stay around 135M to 500M parameters when possible.
- Avoid models that require GPU-only features, special inference servers, or gated access.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better First Version

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for game writing called "Game Narrative Generator".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and similar to a beginner class project. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.7
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 120

Add these example prompts:
- "The warrior entered the dungeon and"
- "You found a legendary sword. Its description reads:"
- "The village elder whispered the secret of the forest:"
- "QUEST LOG: Your mission is to"
- "The final boss appeared, and it was"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden prompt prefix or instruction in the generation function so the model writes like a fantasy game writer
- keep the code easy for a student to read
- include a short note in the UI that newer instruct models usually follow style directions better than distilgpt2

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Model Comparison Version

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same game-writing prompt.

The Space should be called "Game Narrative Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining that distilgpt2 is the old baseline, SmolLM2 is the recommended upgrade, and Qwen2.5-0.5B-Instruct is the more powerful but slower option
- if the selected model is an instruct model, add a simple instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- use Gradio only, not Streamlit

Include the same game-writing examples:
- "The warrior entered the dungeon and"
- "You found a legendary sword. Its description reads:"
- "The village elder whispered the secret of the forest:"
- "QUEST LOG: Your mission is to"
- "The final boss appeared, and it was"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Ask AI To Help You Search For Better Models

Use this when you want a new candidate beyond the two recommended ones:

```text
Help me search Hugging Face for a better small text-generation model for a game-writing Space that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- ideally under about 500M parameters
- good for instruction following or creative writing
- realistic for a Hugging Face Space on free CPU Basic

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit game-writing.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 4: Push The Idea In Different Directions

Use this to make the Space feel more like your project:

```text
Rewrite my Hugging Face Space prompt so the same game-writing app can switch between different output modes:
- NPC dialogue
- quest log
- item lore
- boss introduction
- scene description

Keep it beginner-friendly and still based on a small CPU-friendly Hugging Face model.
Add one dropdown for output mode and update the hidden instruction prefix so each mode produces a different style.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## What To Notice While Testing

- Which model follows the game theme best without drifting off-topic?
- Which model writes the cleanest quest text or item lore?
- At what temperature does the writing stop feeling useful?
- Does the stronger model improve quality enough to be worth the slower speed?

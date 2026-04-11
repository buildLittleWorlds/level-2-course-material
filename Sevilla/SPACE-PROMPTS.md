# Sevilla

## Goal

Build your "Animation Scene Writer" first, then turn it into a small experiment lab where you can test how different models handle motion, visual storytelling, and emotional shifts in a scene.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer and better at following animation/storyboard directions than `distilgpt2`.
- `HuggingFaceTB/SmolLM2-135M-Instruct` — fastest lightweight option; useful for quick experiments and lots of prompt testing.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better output, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, small models are the safest classroom choice.
- For your project, instruction-following matters because you want the model to respond differently to motion, mood, and scene transitions.
- The best model is not just the strongest one. It is the one that gives the clearest change when you adjust emotional tone or scene type.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-135M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better Animation Scene Writer

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for animation and video scene writing called "Animation Scene Writer".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.8
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 120

Add these example prompts:
- "The character stepped into the frame and began to"
- "In the opening shot, the camera zooms in on"
- "The animation sequence shows a figure who"
- "As the scene transitions, the mood shifts from"
- "The final frame of the video reveals"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model writes like a storyboard or animation scene writer focused on motion and visual flow
- keep the code easy for a student to read
- include a short note in the UI explaining that newer instruct models usually follow style directions better than distilgpt2

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Motion And Mood Model Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same animation-writing prompt.

The Space should be called "Motion and Mood Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-135M-Instruct
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Scene Mode" with these options: action sequence, emotional scene, transition shot, character entrance, final reveal
- use the scene mode to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining the tradeoff between speed and quality
- use Gradio only

Include these example prompts:
- "The character stepped into the frame and began to"
- "In the opening shot, the camera zooms in on"
- "The animation sequence shows a figure who"
- "As the scene transitions, the mood shifts from"
- "The final frame of the video reveals"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Test Emotional Register On Purpose

This one connects directly to your emotion-model work:

```text
Write me a Hugging Face Space using Gradio and transformers that lets me test how a small text-generation model handles emotionally different prompts.

The Space should be called "Emotion in Motion Writer".

I want:
- one model dropdown with these options: distilgpt2, HuggingFaceTB/SmolLM2-360M-Instruct, Qwen/Qwen2.5-0.5B-Instruct
- one prompt textbox
- a temperature slider
- a dropdown called "Emotional Register" with these options: joyful, tense, sad, sarcastic, neutral
- one output box

Requirements:
- use CPU only
- load models lazily and cache them
- use the emotional register to change a short hidden instruction prefix before generation
- keep the code beginner-friendly
- add a short note telling users to compare what happens when the same prompt is written with different emotional registers

Give me the complete app.py and requirements.txt files.
```

## Prompt 4: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for a better small text-generation model for an animation scene writing Space that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- realistic for a Hugging Face Space on free CPU Basic
- good at instruction following, visual storytelling, scene writing, motion description, or emotional tone

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit animation scene writing.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 5: Push The Same Scene Through Different Creative Modes

Use this to make the Space feel more connected to your broader experiments:

```text
Rewrite my Hugging Face Space prompt so the same animation-writing app can switch between different output modes:
- storyboard narration
- emotional scene beat
- character action description
- transition description
- final shot reveal

Keep it beginner-friendly and still based on a small CPU-friendly Hugging Face model.
Add one dropdown for output mode and update the hidden instruction prefix so each mode creates a different kind of effect.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## Prompt 6: Ask AI To Help You Design A Fair Comparison

This one fits the testing style already suggested in the course:

```text
Help me design a simple fair test for comparing small Hugging Face text-generation models in an animation-writing Space.

I want to compare them on:
- motion description
- emotional range
- prompt-following
- clarity
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Three prompts that are good for comparing animation scene-writing models.
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to test emotional register by using very different inputs like a breakup text, a graduation speech, a legal contract, and a children's story.
```

## What To Notice While Testing

- Which model gives the strongest sense of motion or scene transition?
- Which one handles emotional shifts best without becoming generic?
- Does the stronger model improve the writing enough to justify slower speed?
- What changes more: the output when you swap the model, or the output when you change emotional register?
- Which kinds of prompts flatten out the model's emotional range?

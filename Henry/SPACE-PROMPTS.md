# Henry

## Goal

Build your "Scene Describer" first, then turn it into a small experiment lab where you can test how different models handle camera language, visual detail, and changes in perspective.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer and better at following descriptive instructions than `distilgpt2`.
- `HuggingFaceTB/SmolLM2-135M-Instruct` — fastest lightweight option; useful for quick iterations and lots of side-by-side prompt tests.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better output, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, small models are the safest classroom choice.
- For your project, instruction-following matters because you want the model to respond differently to camera angles, framing, and description style.
- The best model is not just the strongest one. It is the one that changes in useful ways when you change the prompt or perspective.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-135M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better Scene Describer

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for visual scene description called "Scene Describer".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.7
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 100

Add these example prompts:
- "The camera slowly panned across the scene and revealed"
- "From a bird's eye view, the city looked"
- "The photograph captured a moment where"
- "Looking at the image from a different angle, you notice"
- "The most striking detail in the picture was"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model writes like a visual describer focused on framing, angle, and detail
- keep the code easy for a student to read
- include a short note in the UI explaining that newer instruct models usually follow style directions better than distilgpt2

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Camera-Angle Model Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same scene-description prompt.

The Space should be called "Camera Angle Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-135M-Instruct
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Viewpoint" with these options: close-up, wide shot, bird's-eye view, low angle, over-the-shoulder
- use the viewpoint to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining the tradeoff between speed and quality
- use Gradio only

Include these example prompts:
- "The camera slowly panned across the scene and revealed"
- "From a bird's eye view, the city looked"
- "The photograph captured a moment where"
- "Looking at the image from a different angle, you notice"
- "The most striking detail in the picture was"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Side-By-Side Perspective Tester

Use this if you want to make the experiment more controlled:

```text
Write me a Hugging Face Space using Gradio and transformers that runs the same scene-description prompt through two selected models side by side.

I want:
- Model A dropdown
- Model B dropdown
- one shared prompt input
- shared temperature, top-p, and max_new_tokens controls
- a viewpoint dropdown
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
Help me search Hugging Face for a better small text-generation model for a scene-description Space that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- realistic for a Hugging Face Space on free CPU Basic
- good at instruction following, visual description, scene writing, or caption-like detail

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit scene description.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 5: Push The Same Scene Through Different Visual Lenses

Use this to make the Space feel more connected to your vision interests:

```text
Rewrite my Hugging Face Space prompt so the same scene-description app can switch between different output modes:
- cinematic shot description
- photography caption
- storyboard note
- image prompt helper
- visual analysis paragraph

Keep it beginner-friendly and still based on a small CPU-friendly Hugging Face model.
Add one dropdown for output mode and update the hidden instruction prefix so each mode creates a different kind of effect.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## Prompt 6: Ask AI To Help You Design A Fair Comparison

This one fits your crossover between vision and text:

```text
Help me design a simple fair test for comparing small Hugging Face text-generation models in a scene-description Space.

I want to compare them on:
- visual detail
- prompt-following
- clarity
- usefulness
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Three prompts that are good for comparing scene-description models.
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to test domain shift by using scenes from different domains like nature, sports, city streets, and abstract art.
```

## What To Notice While Testing

- Which model gives the clearest sense of camera angle or framing?
- Which one notices useful visual details instead of generic filler?
- Does the stronger model improve descriptive quality enough to justify slower speed?
- What changes more: the output when you swap models, or the output when you change viewpoint?
- Which kinds of scenes seem easiest or hardest for the model to describe well?

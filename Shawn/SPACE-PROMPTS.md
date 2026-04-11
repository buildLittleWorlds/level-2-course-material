# Shawn

## Goal

Build a Space where someone can type a text prompt to generate an image, then adjust the visual style of the output — anime, surrealist, photorealistic, watercolor, and so on. Start with a single working text-to-image Space, then add style controls so you can compare how the same prompt looks across different art styles.

## Two Paths To Get There

Because image generation models are large and often need GPU, there are two realistic approaches for a free Hugging Face Space:

### Path A: API-Based (Recommended Start)

Use the Hugging Face Inference API to call larger image generation models without hosting them yourself. This is the fastest way to get a working Space that actually generates images.

- Free-tier API calls are rate-limited but work for classroom demos and testing.
- You send a text prompt, the API returns an image.
- You can switch between different models by changing the model ID.

### Path B: Prompt-Engineering A Text Description

Use a small text-generation model to *describe* what an image would look like in different art styles, then use that description as a refined prompt for an image generator. This is more experimental but teaches you about prompt engineering and style transfer at the language level.

## Best Models To Try

### For Image Generation (API-Based)

- `stabilityai/stable-diffusion-xl-base-1.0` — strong general-purpose text-to-image model. Good baseline.
- `runwayml/stable-diffusion-v1-5` — older but fast and reliable. Good for comparison.
- `Linaqruf/animagine-xl` — anime-focused SDXL fine-tune. You already have this in your collection.
- `playgroundai/playground-v2.5-1024px-aesthetic` — strong on aesthetic quality. Also in your collection.

### For Style Description (Text-Generation, CPU-Friendly)

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best small instruct model for rewriting prompts in different art styles.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger but slower on free CPU.
- `distilgpt2` — baseline for comparison.

## Quick Rules For Picking Models

- For image generation, you will almost certainly need the Inference API rather than loading the model locally — image models are too large for free CPU Spaces.
- For text-based style prompting, stay with small public `text-generation` models that run on CPU.
- Your collection already has strong picks (FLUX.1-dev, SDXL, animagine-xl, playground-v2.5) — use those as your testing shortlist.
- The interesting experiment is not just "which model makes the best image" but "how does the same prompt change across art styles."

## Reference Links

- `stabilityai/stable-diffusion-xl-base-1.0`: <https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0>
- `runwayml/stable-diffusion-v1-5`: <https://huggingface.co/runwayml/stable-diffusion-v1-5>
- `Linaqruf/animagine-xl`: <https://huggingface.co/Linaqruf/animagine-xl>
- `playgroundai/playground-v2.5-1024px-aesthetic`: <https://huggingface.co/playgroundai/playground-v2.5-1024px-aesthetic>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- Hugging Face Inference API docs: <https://huggingface.co/docs/api-inference>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Text-To-Image Space With Style Controls

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio that generates images from text prompts using the Hugging Face Inference API.

The Space should be called "Art Style Image Generator".

I want:
- a text prompt input box
- a dropdown called "Art Style" with these options: anime, surrealist, photorealistic, watercolor, oil painting, pixel art, comic book
- a "Generate" button
- an image output area

Requirements:
- use the huggingface_hub InferenceClient to call an image generation model via the API
- use "stabilityai/stable-diffusion-xl-base-1.0" as the default model
- keep the MODEL_ID as a constant near the top so I can swap models later
- when the user selects an art style, prepend a short style instruction to their prompt before sending it to the API (for example, if they type "a castle on a hill" and select "watercolor," the actual prompt sent should be something like "a castle on a hill, watercolor painting style, soft brushstrokes")
- include a short note in the UI explaining that different art styles change the prompt sent to the model
- handle API errors gracefully with a user-friendly message
- keep the code beginner-friendly and easy to read
- the Space should work on free CPU since the heavy computation happens on the API side

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK.
```

## Prompt 2: Build A Model Comparison Lab For Art Styles

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio that compares image generation across different models using the Hugging Face Inference API.

The Space should be called "Art Style Model Lab".

I want:
- a text prompt input box
- a model dropdown that lets me choose between:
  - stabilityai/stable-diffusion-xl-base-1.0
  - runwayml/stable-diffusion-v1-5
  - Linaqruf/animagine-xl
- an art style dropdown with: anime, surrealist, photorealistic, watercolor, oil painting, pixel art
- a "Generate" button
- an image output area
- a short note showing the actual prompt that was sent to the model (so I can see how the style modifier changed it)

Requirements:
- use the huggingface_hub InferenceClient
- prepend the art style as a style modifier to the user's prompt
- keep model IDs as constants near the top
- handle API errors gracefully
- keep the code beginner-friendly
- include a note in the UI encouraging users to try the same prompt across different models and styles to see what changes

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Style Prompt Rewriter

This gives you a text-based approach that runs on free CPU:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

The Space should be called "Art Style Prompt Rewriter".

I want a text-generation Space that takes a simple image description and rewrites it in the language of a specific art style — so a user types "a cat sitting on a windowsill" and the Space outputs a detailed prompt rewritten for anime style, surrealist style, watercolor style, etc.

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU.

I want:
- a prompt textbox for the base image description
- a dropdown called "Target Art Style" with: anime, surrealist, photorealistic, watercolor, oil painting, pixel art, comic book
- a Temperature slider from 0.1 to 2.0, default 0.7
- a Max New Tokens slider from 20 to 200, default 120
- an output textbox showing the rewritten prompt

Requirements:
- use a hidden instruction prefix that tells the model to rewrite the input as a detailed image-generation prompt in the selected art style
- keep MODEL_ID as a constant so I can swap models later
- keep the code beginner-friendly
- include a note that the output can be copied and pasted into an image generation tool

Give me the complete app.py and requirements.txt files.
```

## Prompt 4: Ask AI To Help You Search For Better Models

Use this when you want to explore beyond the recommended ones:

```text
Help me search Hugging Face for image generation models I can use through the Inference API for a student Space about art styles.

I want two shortlists:

1. Text-to-image models that are good at different visual styles (anime, surrealist, photorealistic, watercolor, etc.)
2. Small text-generation models that could rewrite prompts in art-style language on free CPU

Constraints for image models:
- available through the Hugging Face Inference API
- good at responding to style modifiers in the prompt
- publicly accessible

Constraints for text models:
- public and non-gated
- works with transformers
- realistic for free CPU
- good at following instructions about visual style language

Give me:
1. Five image model IDs with one sentence on what style each is strongest at.
2. Three text model IDs for prompt rewriting.
3. Your best recommendation for a model that handles multiple art styles well.
4. A revised AI prompt I can paste into a coding assistant to swap that model into my Space.
```

## Prompt 5: Ask AI To Help You Design A Fair Style Comparison

```text
Help me design a fair test for comparing how different image generation models handle art style prompts.

I want to compare:
- how well the model matches the requested art style
- visual quality and detail
- how much the output changes when I switch styles vs. switch models
- consistency (does the same prompt + style give similar results each time?)

Give me:
1. A tiny rubric I can use while testing.
2. Three base prompts that would look very different across art styles (e.g., a landscape, a portrait, an action scene).
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to document image outputs in a research journal (screenshots, side-by-side comparisons, naming conventions).
```

## What To Notice While Testing

- Which art style modifier has the biggest visual impact on the output?
- Which model responds most clearly to style changes vs. which one tends to look the same regardless?
- Does "anime" style work better on some models than others? (Your animagine-xl should dominate here — does it?)
- When you use the prompt rewriter to expand a simple description into art-style language, does the image generator produce noticeably different results?
- What happens when you combine conflicting style cues (e.g., "photorealistic anime")?
- Which combinations of prompt + style + model would you actually recommend to someone?

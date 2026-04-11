# Annabelle

## Goal

Go deeper on your music Spaces — opera and jazz in particular. You already have Opera-Generator, Music-Starter-Opera-Jazz, and nyssma-trainer running. The next step is turning these into a small experiment lab where you can compare how different models handle musical language, genre distinctions, performance instructions, and creative composition prompts.

## Best Models To Try

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade for text-generation music work; better at following genre-specific instructions than `distilgpt2`.
- `HuggingFaceTB/SmolLM2-135M-Instruct` — fastest lightweight option; useful for quick iterations when testing lots of prompt variations across opera vs. jazz.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better at maintaining musical vocabulary and structure, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

## Quick Rules For Picking Models

- Stay with public, non-gated `text-generation` models.
- Prefer `transformers` models with Apache-2.0 or MIT licenses.
- On Hugging Face free CPU Basic, stay around 135M to 500M parameters when possible.
- For your project, instruction-following matters because you want the model to respond differently to opera vs. jazz vs. other musical contexts.
- The best model is not just the strongest one. It is the one that gives the clearest change when you shift genre, mood, or musical context.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-135M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Music Genre Model Lab

You already have working music Spaces. This prompt builds a comparison lab so you can test models against each other on the same musical prompt:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same music-writing prompt.

The Space should be called "Music Genre Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-135M-Instruct
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Genre" with these options: opera, jazz, classical, musical theater, blues
- use the genre to change a short hidden instruction prefix before generation so the model writes in the style and vocabulary of that genre
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining the tradeoff between speed and quality
- use Gradio only

Include these example prompts:
- "The aria begins as the soprano steps forward and"
- "The jazz quartet opens with a piano riff that"
- "The overture builds from a single oboe note into"
- "The improvisation takes a turn when the trumpet player"
- "The final movement brings together all the voices in"

Give me the complete app.py and requirements.txt files.
```

## Prompt 2: Build An Opera vs. Jazz Comparison Space

This one is tailored to your specific interests:

```text
Write me a Hugging Face Space using Gradio and transformers that runs the same music prompt through two genre modes side by side — opera and jazz.

The Space should be called "Opera vs. Jazz Writer".

I want:
- one shared prompt input
- a model dropdown (distilgpt2, HuggingFaceTB/SmolLM2-360M-Instruct, Qwen/Qwen2.5-0.5B-Instruct)
- shared temperature, top-p, and max_new_tokens controls
- two output boxes shown next to each other, labeled "Opera Version" and "Jazz Version"
- each output should use a different hidden instruction prefix — one that tells the model to write in an operatic style (dramatic, vocal, staged) and one that tells it to write in a jazz style (improvisational, rhythmic, intimate)
- a short note reminding users that the same prompt processed through different genre instructions reveals how much the model's output depends on framing

Use only small CPU-friendly models. Keep the code simple enough for a student to understand and edit later.

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Music Practice Helper

This connects to your nyssma-trainer work:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for music students called "Music Practice Helper".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

I want:
- a prompt textbox where a student can describe what they are working on (e.g., "I am preparing an opera aria for an audition" or "I am learning a jazz standard on piano")
- a dropdown called "Help Mode" with these options: practice plan, performance tips, musical context, warm-up suggestions, listening recommendations
- a Temperature slider from 0.1 to 2.0, default 0.6
- a Max New Tokens slider from 20 to 200, default 150

Requirements:
- use a hidden instruction prefix that changes based on the help mode so the model gives different kinds of musical guidance
- keep MODEL_ID as a constant near the top so I can swap models later
- include a note in the UI that this is an educational tool and not a substitute for a music teacher
- keep the code beginner-friendly
- use return_full_text=False

Include these example prompts:
- "I am preparing Nessun Dorma for a vocal audition"
- "I am learning Take Five on alto saxophone"
- "I want to understand the structure of a jazz standard"
- "I need a warm-up routine before singing opera"
- "I am working on improvisation over a 12-bar blues"

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 4: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for a better small text-generation model for a music-focused Space (opera and jazz emphasis) that must run on free CPU.

Constraints:
- public and non-gated
- text-generation task
- works with transformers
- preferably Apache-2.0 or MIT license
- realistic for a Hugging Face Space on free CPU Basic
- good at instruction following, creative writing, musical vocabulary, or genre-specific language

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit music-focused writing.
3. One sentence on the tradeoff or risk for each model.
4. Your best recommendation for my Space.
5. A revised AI prompt I can paste into a coding assistant to swap that model into my Gradio app.
```

## Prompt 5: Push The Same Musical Idea Across Genres

Use this to make the comparison between opera and jazz more systematic:

```text
Rewrite my Hugging Face Space prompt so the same music-writing app can switch between different genre output modes:
- opera aria
- jazz standard
- classical program note
- musical theater scene
- blues lyric

Keep it beginner-friendly and still based on a small CPU-friendly Hugging Face model.
Add one dropdown for genre mode and update the hidden instruction prefix so each mode creates output in the vocabulary and style of that genre.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## Prompt 6: Ask AI To Help You Design A Fair Genre Comparison

```text
Help me design a simple fair test for comparing how small AI models handle different musical genres in a text-generation Space.

I want to compare them on:
- genre accuracy (does it sound like opera? like jazz?)
- musical vocabulary
- prompt-following
- creativity
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Three prompts that would sound very different across opera vs. jazz vs. classical (e.g., describing a performance opening, a solo moment, a finale).
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to test whether the model actually knows genre-specific language or is just using generic "music words."
5. One example of a good conclusion paragraph based on fake sample results.
```

## What To Notice While Testing

- When you give the same prompt to "opera mode" vs. "jazz mode," how different is the output? Is the model actually shifting genre or just changing a few words?
- Which model uses the most authentic musical vocabulary for each genre?
- Does the stronger model improve genre accuracy enough to justify slower speed?
- What changes more: the output when you swap the model, or the output when you change the genre?
- Which prompts are hardest for the model — ones about performance technique, composition structure, or emotional interpretation?
- How does your nyssma-trainer compare to the practice helper built from these prompts? What did you learn from building both?

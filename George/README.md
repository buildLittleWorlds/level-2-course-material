# George

## Goal

Build your "Health Explainer" first, then experiment with newer small models to see which ones give the clearest, most useful health explanations without drifting into made-up or overconfident text.

## Best Models To Try

### For Health Explanations

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer and usually better at following a careful explanatory style than `distilgpt2`.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better quality, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

### For Health Article Summaries

- `Falconsai/text_summarization` — good modern small summarization option for free CPU.
- `sshleifer/distilbart-cnn-12-6` — the class baseline summarizer, useful for comparison.

## Quick Rules For Picking Models

- Stay with public, non-gated models.
- For explanation tools, use `text-generation` models that work with `transformers`.
- For summarization tools, use `summarization` or `text2text-generation` models that work with `transformers`.
- On Hugging Face free CPU Basic, small models are the safest choice for student Spaces.
- For medical or health topics, lower randomness is usually better.
- Add a clear note that the Space is for education and does not provide medical advice.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- `sshleifer/distilbart-cnn-12-6`: <https://huggingface.co/sshleifer/distilbart-cnn-12-6>
- `Falconsai/text_summarization`: <https://huggingface.co/Falconsai/text_summarization>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better Health Explainer

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for health education called "Health Explainer".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.4
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 120

Add these example prompts:
- "When you sprain your ankle, what happens inside is"
- "The most important thing about first aid is"
- "Your immune system works by"
- "The reason sleep is important for recovery is"
- "A sports injury should be treated by"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model explains clearly, carefully, and at a simple reading level
- include a note in the UI that this tool is for educational information only and does not provide medical advice
- keep the code easy for a student to read
- include a short note in the UI explaining that lower temperature is usually better for health explanations

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A Health Model Comparison Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same health explanation prompt.

The Space should be called "Health Explainer Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "Audience Level" with these options: middle school explanation, patient handout, general adult explanation, science class explanation
- use the audience level to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- include a note that the app is for educational information only, not medical advice
- show a short model note in the UI explaining the speed vs. quality tradeoff
- use Gradio only

Include these example prompts:
- "When you sprain your ankle, what happens inside is"
- "The most important thing about first aid is"
- "Your immune system works by"
- "The reason sleep is important for recovery is"
- "A sports injury should be treated by"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Health Summarizer Version

This follows the course direction of trying the summarizer on health articles:

```text
Write me a Hugging Face Space using Gradio and transformers that summarizes pasted health articles, patient information sheets, or science text.

The Space should be called "Health Article Summarizer".

Use the model "Falconsai/text_summarization" as the default summarization model. Load it with pipeline("summarization", model="Falconsai/text_summarization"). Make it run on CPU for a free Hugging Face Space.

I want:
- a large textbox for pasted text
- a Max Summary Length slider
- a Min Summary Length slider
- a short note that this tool is best for informational text, not diagnosis

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap summarization models later
- use do_sample=False
- reject very short input with a helpful message
- trim long input if needed so the Space stays stable on free CPU
- show the original word count and summary word count
- include a note that the app is for educational information only and not medical advice
- keep the code easy for a student to read

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 4: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for better small models for a student health education Space that must run on free CPU.

I need two shortlists:

1. Small text-generation models for health explanations
2. Small summarization models for health article summaries

Constraints:
- public and non-gated
- works with transformers
- realistic for a Hugging Face Space on free CPU Basic
- preferably Apache-2.0 or MIT license
- good for clear, careful, educational output
- not specialized for giving diagnoses

Give me:
1. Three explanation model IDs.
2. Three summarization model IDs.
3. One sentence on why each model might fit.
4. One sentence on the tradeoff or risk for each model.
5. Your best explanation recommendation and your best summarization recommendation.
6. A revised AI prompt I can paste into a coding assistant for each one.
```

## Prompt 5: Ask AI To Help You Design A Fair Test

This one fits the way your course materials frame the problem:

```text
Help me design a simple fair test for comparing small AI models in a health education Space.

I want to compare them on:
- clarity
- usefulness
- caution
- reading level
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Four test prompts or texts that cover different health registers: Wikipedia-style article, medical journal abstract, patient instructions sheet, sports injury explanation.
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to detect when a model starts sounding too confident or starts hallucinating.
5. One example of a careful conclusion paragraph based on fake sample results.
```

## Prompt 6: Push The Same Topic Across Different Registers

Use this to make the model comparison more interesting:

```text
Rewrite my Hugging Face Space prompt so the same health topic can be explained in different language styles:
- middle school
- high school biology
- patient handout
- short encyclopedia entry

Keep it beginner-friendly and based on a small CPU-friendly Hugging Face model.
Add one dropdown for explanation style and update the hidden instruction prefix so each style changes the level of language.
Give me the full prompt I should paste into a coding AI so it writes the code for me.
```

## What To Notice While Testing

- Which model stays the clearest without sounding overconfident?
- At what temperature does the explanation start to feel unreliable?
- Does the model handle the same topic differently when the reading level changes?
- Which summarizer works best on patient-facing text versus more technical medical text?
- When a word like "positive" or "critical" appears, does the model seem to understand the medical meaning?

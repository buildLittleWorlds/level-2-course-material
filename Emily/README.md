# Emily

## Goal

Build your Session 5 news-style Space first, then experiment in two directions:

- better news drafting with a newer small instruct model
- better summarization for articles, research, and information filtering

## Best Models To Try

### For News Drafting

- `HuggingFaceTB/SmolLM2-360M-Instruct` — best first upgrade; newer and better at following a news-writing direction than `distilgpt2`.
- `Qwen/Qwen2.5-0.5B-Instruct` — stronger stretch option; often better quality, but slower on free CPU.
- `distilgpt2` — keep this as your baseline so you can compare old vs. newer behavior.

### For Summarization

- `Falconsai/text_summarization` — good modern small summarization option for free CPU.
- `sshleifer/distilbart-cnn-12-6` — the class baseline summarizer, useful for comparison.

## Quick Rules For Picking Models

- Stay with public, non-gated models.
- For drafting, use `text-generation` models that work with `transformers`.
- For summarization, use `summarization` or `text2text-generation` models that work with `transformers`.
- On Hugging Face free CPU Basic, small models are safer for student Spaces.
- For your project, the best model is the one that stays factual and useful when the topic changes across science, politics, entertainment, or sports.

## Reference Links

- `distilgpt2`: <https://huggingface.co/distilbert/distilgpt2>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- `Qwen/Qwen2.5-0.5B-Instruct`: <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>
- `sshleifer/distilbart-cnn-12-6`: <https://huggingface.co/sshleifer/distilbart-cnn-12-6>
- `Falconsai/text_summarization`: <https://huggingface.co/Falconsai/text_summarization>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Better News Draft Generator

Paste this into ChatGPT, Claude, Gemini, or another coding AI:

```text
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library.

I want a text-generation Space for news-style writing called "News Draft Generator".

Use the model "HuggingFaceTB/SmolLM2-360M-Instruct" as the default model. Load it with AutoTokenizer, AutoModelForCausalLM, and pipeline("text-generation"). Make it run on CPU for a free Hugging Face Space.

Keep the app simple and beginner-friendly. I want:
- a prompt textbox
- a Temperature slider from 0.1 to 2.0, default 0.5
- a Top-p slider from 0.1 to 1.0, default 0.9
- a Max New Tokens slider from 20 to 200, default 100

Add these example prompts:
- "Breaking news: scientists discovered that"
- "A new report released today found that students"
- "The conference on artificial intelligence announced"
- "Researchers at the university published a study showing"
- "This week in technology: the biggest story is"

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap models later
- use do_sample=True and num_return_sequences=1
- clamp temperature to at least 0.01
- set device=-1 so it stays on CPU
- use return_full_text=False
- add a short hidden instruction prefix so the model writes in a clear, informative, news-style tone
- keep the code easy for a student to read
- include a short note in the UI explaining that low temperature is usually better for information-style writing

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 2: Build A News Model Comparison Lab

Use this after your first version works:

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple small text-generation models on the same news-writing prompt.

The Space should be called "News Draft Model Lab".

I want a dropdown that lets me choose between:
- distilgpt2
- HuggingFaceTB/SmolLM2-360M-Instruct
- Qwen/Qwen2.5-0.5B-Instruct

Requirements:
- load models lazily and cache them so the app does not reload everything on every click
- use CPU only for a free Hugging Face Space
- keep the same controls for prompt, temperature, top-p, and max_new_tokens
- add a second dropdown called "News Mode" with these options: breaking news lead, research summary, conference briefing, technology roundup, headline plus opening paragraph
- use the news mode to change a short hidden instruction prefix before generation
- if the selected model is distilgpt2, use the raw prompt without chat formatting
- if the selected model is an instruct model, prepend a short instruction string before the user prompt
- keep the code beginner-friendly and well organized
- show a short model note in the UI explaining the speed vs. quality tradeoff
- use Gradio only

Include these example prompts:
- "Breaking news: scientists discovered that"
- "A new report released today found that students"
- "The conference on artificial intelligence announced"
- "Researchers at the university published a study showing"
- "This week in technology: the biggest story is"

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Better Summarizer Version

This follows the course direction from the Session 5 summarizer:

```text
Write me a Hugging Face Space using Gradio and transformers that summarizes pasted news articles, research blurbs, and long informational text.

The Space should be called "News and Research Summarizer".

Use the model "Falconsai/text_summarization" as the default summarization model. Load it with pipeline("summarization", model="Falconsai/text_summarization"). Make it run on CPU for a free Hugging Face Space.

I want:
- a large textbox for pasted text
- a Max Summary Length slider
- a Min Summary Length slider
- a short note that this tool is best for informational text, not creative writing

Important implementation details:
- keep MODEL_ID as a constant near the top so I can swap summarization models later
- use do_sample=False
- reject very short input with a helpful message
- trim long input if needed so the Space stays stable on free CPU
- show the original word count and summary word count
- keep the code easy for a student to read

Give me the complete app.py and requirements.txt files ready for a Hugging Face Space using Gradio SDK on free CPU.
```

## Prompt 4: Build A Summarizer Comparison Lab

Use this if you want to compare the class summarizer with a newer small model:

```text
Write me a Hugging Face Space using Gradio and transformers that compares two summarization models on the same input text.

The Space should be called "Summarizer Comparison Lab".

I want a dropdown that lets me choose between:
- sshleifer/distilbart-cnn-12-6
- Falconsai/text_summarization

Requirements:
- load models lazily and cache them
- use CPU only for a free Hugging Face Space
- include one textbox for long input text
- include max and min summary length sliders
- show the summary plus word counts
- include a short note telling users to compare across different news beats like politics, science, entertainment, and sports
- keep the code beginner-friendly

Give me the complete app.py and requirements.txt files.
```

## Prompt 5: Ask AI To Help You Search For Better Models

Use this when you want to go beyond the recommended ones:

```text
Help me search Hugging Face for better small models for a student news-and-research Space that must run on free CPU.

I need two shortlists:

1. Small text-generation models for news drafting
2. Small summarization models for article summarization

Constraints:
- public and non-gated
- works with transformers
- realistic for a Hugging Face Space on free CPU Basic
- preferably Apache-2.0 or MIT license
- good for clear, factual, information-style output

Give me:
1. Three drafting model IDs.
2. Three summarization model IDs.
3. One sentence on why each model might fit.
4. One sentence on the tradeoff or risk for each model.
5. Your best drafting recommendation and your best summarization recommendation.
6. A revised AI prompt I can paste into a coding assistant for each one.
```

## Prompt 6: Ask AI To Help You Do A Fair Test

This one matches your journal work:

```text
Help me design a simple fair test for comparing AI models in a news and summarization Space.

I want to compare them on:
- factual tone
- clarity
- usefulness
- prompt-following
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Four test texts or prompts from different beats: politics, science, entertainment, sports.
3. A simple results table I can paste into my GitHub journal.
4. Advice on how to tell when a model has drifted from useful summary into creative fiction.
```

## What To Notice While Testing

- Which drafting model stays the most grounded and informative?
- At what temperature does a “news draft” start sounding made up?
- Which summarizer handles different beats most consistently?
- Does the newer model improve quality enough to justify slower speed?
- When the topic changes, does the model stay useful or does it simplify too much?

# Bluest Hour

## Goal

Turn Bluest Hour from a single contemplative app into a three-Space research story about evening light, journaling, and whether small AI models can validly analyze reflective writing.

## Best Models To Try

### For Journal Mood / Emotion Analysis

- `distilbert-base-uncased-finetuned-sst-2-english` — simple baseline sentiment model; useful because it is narrow and easy to question.
- `j-hartmann/emotion-english-distilroberta-base` — stronger emotion labeler; useful if you want more than positive vs. negative.
- `SamLowe/roberta-base-go_emotions` — wider emotion vocabulary; helpful if reflective writing is too subtle for binary sentiment.

### For Reflection Summaries Or Follow-Up Writing

- `Falconsai/text_summarization` — good small summarization baseline for free CPU.
- `HuggingFaceTB/SmolLM2-360M-Instruct` — useful for small writing assistant or analysis tools when you want instruction-following.

## Quick Rules For Picking Models

- Stay with public, non-gated models.
- For the research question, the point is not just "stronger model = better." The point is whether the model is actually measuring the kind of writing the app produces.
- Keep at least one simple baseline model in the comparison so you can say what changed.
- Lower complexity is better for a student experiment. You want the result to be explainable.
- If you are testing reflective journaling, binary sentiment is useful precisely because it may fail in an interesting way.

## Reference Links

- `distilbert-base-uncased-finetuned-sst-2-english`: <https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english>
- `j-hartmann/emotion-english-distilroberta-base`: <https://huggingface.co/j-hartmann/emotion-english-distilroberta-base>
- `SamLowe/roberta-base-go_emotions`: <https://huggingface.co/SamLowe/roberta-base-go_emotions>
- `Falconsai/text_summarization`: <https://huggingface.co/Falconsai/text_summarization>
- `HuggingFaceTB/SmolLM2-360M-Instruct`: <https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct>
- Hugging Face Spaces hardware docs: <https://huggingface.co/docs/hub/spaces-gpus>

## Prompt 1: Build A Blue Hour Journal Analyzer

```text
Write me a Hugging Face Space using Gradio and transformers that analyzes short reflective journal entries written after evening walks.

The Space should be called "Blue Hour Journal Analyzer".

I want:
- a textbox for a short journal entry
- an optional self-rating slider for calmness or mood from 1 to 5
- a dropdown to choose between these models:
  - distilbert-base-uncased-finetuned-sst-2-english
  - j-hartmann/emotion-english-distilroberta-base
  - SamLowe/roberta-base-go_emotions
- a results area that shows the model label and score
- a second results area that explains the limitation: reflective writing may not fit ordinary sentiment labels

Requirements:
- use CPU only for a free Hugging Face Space
- keep the code beginner-friendly
- keep MODEL_ID choices easy to swap
- if the model output has multiple labels, show the top 3
- include 5 example journal entries inspired by evening light, calmness, weather, memory, and ambiguity
- use Gradio only

Give me the complete app.py and requirements.txt files.
```

## Prompt 2: Build A Mood Model Comparison Lab

```text
Write me a Hugging Face Space using Gradio and transformers that compares multiple text-classification models on the same short reflective journal entry.

The Space should be called "Blue Hour Mood Model Lab".

I want a dropdown that lets me choose between:
- distilbert-base-uncased-finetuned-sst-2-english
- j-hartmann/emotion-english-distilroberta-base
- SamLowe/roberta-base-go_emotions

Requirements:
- load models lazily and cache them
- use CPU only for a free Hugging Face Space
- accept one journal entry input
- show each model's output side by side so I can compare how the same entry is interpreted
- include a small text box where the user can describe what they intended the entry to express
- include a note in the UI asking whether the model captured the reflection accurately
- keep the code simple and readable for a student

Include example entries like:
- "The sky was darker than I expected, but everything felt calmer."
- "It was beautiful in a way that made me a little sad."
- "The light on the trees made the whole street feel unreal."
- "I felt quieter after the walk, though not exactly happier."
- "Nothing dramatic happened, but the evening felt deep and still."

Give me the complete app.py and requirements.txt files.
```

## Prompt 3: Build A Seasonal Reflection Tracker

```text
Write me a Hugging Face Space using Gradio and transformers that combines a blue-hour walk journal with simple local tracking over time.

The Space should be called "Seasonal Reflection Tracker".

I want:
- a date input
- a short journal entry textbox
- a self-rating slider for calmness from 1 to 5
- one model choice for mood analysis
- a table that stores entries in session memory or local CSV for demo purposes
- a simple plot showing date vs self-rating and date vs model score
- a short summary section that compares self-ratings to model outputs

Requirements:
- use a small CPU-friendly sentiment or emotion model
- use Gradio only
- keep the code beginner-friendly
- make it clear that this is a small student research tracker, not a mental health diagnostic tool
- structure the code so I can later swap in a different model or scoring method

Give me the complete app.py and requirements.txt files.
```

## Prompt 4: Ask AI To Help You Search For Better Models

```text
Help me search Hugging Face for better small models for a student Space that analyzes reflective journaling about evening walks and mood.

I need:
1. Small text-classification models for reflective writing
2. Small models that might do better than plain positive/negative sentiment

Constraints:
- public and non-gated
- works with transformers
- realistic for a Hugging Face Space on free CPU Basic
- preferably Apache-2.0 or MIT license
- useful for subtle emotion, reflection, or diary-like writing

Give me:
1. A shortlist of 5 model IDs.
2. One sentence on why each model might fit reflective writing.
3. One sentence on the risk for each model.
4. Your best recommendation for a baseline model and your best recommendation for a richer emotion model.
5. A revised AI coding prompt I can paste into a coding assistant to swap the model into my Gradio app.
```

## Prompt 5: Ask AI To Help You Design A Fair Test

```text
Help me design a simple fair test for comparing how AI models analyze short reflective journal entries from a project about evening walks during blue hour.

I want to compare them on:
- whether the label matches the writer's intended mood
- whether the model captures ambiguity
- whether the model flattens reflective writing into generic positive/negative labels
- speed

Give me:
1. A tiny rubric I can use while testing.
2. Six example journal entries: some clearly positive, some clearly negative, and some ambiguous or contemplative.
3. A simple results table I can paste into a GitHub journal.
4. Advice on how to compare self-rating, human judgment, and model output.
5. One example of a careful conclusion paragraph based on fake sample results.
```

## Prompt 6: Build A Reflection Writing Helper

```text
Write me a Hugging Face Space using Gradio and transformers that helps a user reflect on an evening walk instead of only labeling the mood.

The Space should be called "Blue Hour Reflection Helper".

Use a small instruction-following model like HuggingFaceTB/SmolLM2-360M-Instruct.

I want:
- a textbox where the user writes a short note about the walk
- a dropdown called "Reflection Mode" with these options:
  - sensory detail
  - mood and feeling
  - memory and association
  - place description
  - rewrite more clearly
- a result box that gives a short follow-up reflection or prompt

Requirements:
- use CPU only
- keep the app simple and beginner-friendly
- add a note that this tool is for reflection and writing support, not therapy or diagnosis
- keep the hidden instruction prefix easy to edit
- use Gradio only

Give me the complete app.py and requirements.txt files.
```

## What To Notice While Testing

- Do the models treat reflective writing as if it were ordinary review text?
- Which entries confuse the models most: sad-beautiful ones, calm-neutral ones, or highly sensory ones?
- Does a richer emotion model actually help, or just create more labels without more validity?
- How often does the writer's own self-rating disagree with the model?
- What changes more: the result when you swap the model, or the result when you rewrite the same thought in plainer language?
- Does the project become more interesting when the model works, or when it fails?

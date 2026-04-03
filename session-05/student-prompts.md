# Session 5: Personalized Space Prompts

Copy your prompt below and paste it into ChatGPT, Gemini, Claude, or any AI assistant. It will give you the code for two files: `app.py` and `requirements.txt`. Then create a new Hugging Face Space (Gradio SDK, Free CPU) and paste the code into those two files.

---

## Bobby

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Game Narrative Generator" and be designed for writing game stories — character dialogue, quest descriptions, item lore, and scene-setting.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.7) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "The warrior entered the dungeon and"
- "You found a legendary sword. Its description reads:"
- "The village elder whispered the secret of the forest:"
- "QUEST LOG: Your mission is to"
- "The final boss appeared, and it was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Annabelle

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Creative Story Starter" and be designed for creative writing — fun stories, music ideas, playful scenarios, and imaginative prompts.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.9) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "She opened the letter and read"
- "The dinosaur walked into the concert hall and picked up a guitar"
- "The song started with a single note that"
- "In a world where animals could talk, the cat said"
- "The most unexpected ingredient in the recipe was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Shawn

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Prompt Comparison Lab" and be designed for systematically testing how different settings change the output. The description should say something like: "Type one prompt, then change the sliders to see how temperature and top-p change what the AI writes."

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.7) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "The best image generation model is"
- "A photograph of a sunset should look"
- "The difference between AI art and human art is"
- "When you compare two images side by side, you notice"
- "The most realistic AI-generated image I've seen"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Emily

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "News Draft Generator" and be designed for experimenting with news-style writing — headlines, article openings, research summaries, and briefings.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "Breaking news: scientists discovered that"
- "A new report released today found that students"
- "The conference on artificial intelligence announced"
- "Researchers at the university published a study showing"
- "This week in technology: the biggest story is"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Chengry

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Medical Text Generator" and be designed for experimenting with medical and health-related text — clinical notes, symptom descriptions, patient scenarios, and health explanations.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "The patient presented with symptoms of"
- "Common side effects of this medication include"
- "The doctor examined the test results and concluded"
- "A healthy diet for someone with diabetes should"
- "The difference between a virus and a bacteria is"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## George

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Health Explainer" and be designed for generating health and wellness explanations — how the body works, what injuries do, how treatments help, and general health literacy.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.5) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "When you sprain your ankle, what happens inside is"
- "The most important thing about first aid is"
- "Your immune system works by"
- "The reason sleep is important for recovery is"
- "A sports injury should be treated by"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Henry

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Scene Describer" and be designed for generating visual scene descriptions — what a camera sees, how to describe images in words, and how angles and perspectives change a scene.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.7) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 100) — controls how much text it generates

Include these example prompts:
- "The camera slowly panned across the scene and revealed"
- "From a bird's eye view, the city looked"
- "The photograph captured a moment where"
- "Looking at the image from a different angle, you notice"
- "The most striking detail in the picture was"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

---

## Sevilla

```
Write me a Hugging Face Space using Gradio and the Hugging Face transformers library. It should be a text generator that uses the model "distilgpt2" loaded with pipeline("text-generation").

The Space should be called "Animation Scene Writer" and be designed for writing animation and video scene descriptions — character actions, visual sequences, storyboard narration, and motion descriptions.

It needs three sliders:
- Temperature (0.1 to 2.0, default 0.8) — controls how creative/wild the writing is
- Top-p (0.1 to 1.0, default 0.9) — controls word diversity
- Max Length (20 to 200, default 120) — controls how much text it generates

Include these example prompts:
- "The character stepped into the frame and began to"
- "In the opening shot, the camera zooms in on"
- "The animation sequence shows a figure who"
- "As the scene transitions, the mood shifts from"
- "The final frame of the video reveals"

The function should use do_sample=True and num_return_sequences=1. Clamp temperature to at least 0.01 to avoid division by zero.

Give me the complete app.py and requirements.txt files ready to paste into a Hugging Face Space (Gradio SDK, free CPU).
```

# Grow Your Collection

Your Hugging Face Collection is a portfolio that grows with you.

## What Is a Collection?

You already know this from Session 1 — a Collection is like a playlist for AI tools. You pick models and Spaces, group them on one page, and add notes about what you discovered.

Here's what's different now: your Collection isn't a one-time assignment. It's a **research portfolio** that you'll add to every week for the rest of this course. The early entries show you casting a wide net. The later entries show you going deep on something specific. By Session 10, your Collection tells the story of your investigation.

## From Spaces to Models

In Session 1, you collected Spaces — the apps that run models. Now you're adding the engines that power them.

Why does this matter? Because the same model can power dozens of different Spaces, and different models can make the same Space behave in completely different ways. Understanding models — not just Spaces — is what separates a user from a critic.

|  | Models | Spaces |
|---|---|---|
| **What is it?** | The trained AI brain (lives on HF Model Hub) | A web app that runs a model (lives on HF Spaces) |
| **URL pattern** | `huggingface.co/username/model-name` | `huggingface.co/spaces/username/space-name` |
| **Why include it?** | Shows you understand what's under the hood | Shows you've tested it in a real interface |

## Name Your Collection

Don't just call it "My Collection." Name it after your focus area:

- "Sentiment Model Lineup"
- "Translation Tools I've Tested"
- "Image Generators Compared"
- "Code Assistants Ranked"

Whatever fits YOUR interest.

If you're still exploring and don't have a focus yet, that's fine. Name it something broad like "My AI Explorations" and rename it later when your topic emerges.

## Step by Step: Add a Model

1. Go to [huggingface.co/models](https://huggingface.co/models)
2. Search for models in your area of interest. Try searching by task: "sentiment," "emotion detection," "text classification," "translation," or whatever topic you're exploring.
3. Click a model and **read the Model Card** (the README on its page). Look for: what data it was trained on, what labels it outputs, what languages it supports, any known limitations. This is where the real learning happens.
4. **Test it in the Inference Widget** — the "Hosted inference API" box on the right side of the model page. Type a sentence and see what the model returns. This lets you test without needing a Space.
5. **Add to your Collection** — click the three-dot menu on the model page and select "Add to collection." Choose your Collection.
6. **Write a note** explaining what you discovered (see "Writing Good Notes" below).

## Step by Step: Add a Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Search or browse for Spaces related to your topic
3. Test it — try the same inputs you used on the model
4. Add to your Collection via the three-dot menu
5. Write a note that mentions which model the Space uses and how the design affects your experience

## Writing Good Notes

Your notes are the most important part of your Collection. They show you actually tested the thing and thought about it.

### For a model:

- What does it take in and produce?
- What was it trained on? (Check the model card)
- How did it handle your test inputs?
- Where does it struggle?
- How does it compare to other models you've tested?

### For a Space:

- Which model does this Space use?
- Does the design help you understand the output?
- Does it add anything beyond the raw model? (Visualizations, comparisons, interactivity?)
- Would you recommend it to someone exploring your topic?

## Your Collection Grows Every Week

| By Session | Target |
|---|---|
| Session 2 | 2 models + 2 Spaces (minimum to start) |
| Session 3 | 4 models + 2 Spaces |
| Session 4 | 5 models + 3 Spaces |
| Session 5 | 6 models + 4 Spaces |
| Session 6 | 7 models + 4 Spaces |
| Session 7 | 8 models + 5 Spaces |
| Session 8 | 9 models + 5 Spaces |
| Session 9 | 10 models + 6 Spaces |
| Session 10 | 11 models + 6 Spaces |
| Session 11 | 12 models + 7 Spaces |

By the end of the course, your Collection tells the story of your investigation. The early entries show you casting a wide net. The later entries show you going deep on something specific.

## Starter Models (for Sentiment — This Session's Shared Example)

These are the models we're using in class. For your own Collection, search the Hub for models related to YOUR topic.

| Model | Type | What It Does |
|---|---|---|
| `distilbert-base-uncased-finetuned-sst-2-english` | Binary | Positive or Negative |
| `cardiffnlp/twitter-roberta-base-sentiment-latest` | Ternary | Positive, Negative, or Neutral |
| `nlptown/bert-base-multilingual-uncased-sentiment` | 5-Star | 1-5 star rating (6 languages) |
| `j-hartmann/emotion-english-distilroberta-base` | 7 Emotions | anger, disgust, fear, joy, neutral, sadness, surprise |
| `SamLowe/roberta-base-go_emotions` | 28 Emotions | Multi-label emotion detection (admiration, amusement, etc.) |

> **Key insight:** More categories doesn't always mean better. A binary model might be more accurate at its job than a 28-emotion model is at its. The right model depends on the task.

## Checklist

- [ ] Collection has a clear name related to your focus area
- [ ] At least 2 models added
- [ ] At least 2 Spaces added
- [ ] Every item has a note explaining what you discovered
- [ ] Collection is set to Public

---

AI + Research Level 2 • Session 2: Data Collection and Representation

# Session 3: What Models Can't Do

**Concept:** ADVERSARIAL TESTING AND THE LIMITS OF CLASSIFICATION
**Spaces:** World Headlines (live build), News Sentiment Analyzer (pre-built), Zero-Shot News Analyzer (pre-built)
**Pre-built fallback:** Have all three Spaces loaded and tested before class. Have your GNews API key working.

**Narrative role:** This session closes Act I — "The Old Way." By the end, students have three sessions of evidence that classical ML models can sort text into buckets but don't understand what they're reading. The session ends with a named summary of what Sessions 1-3 have shown and a forward bridge to Session 4's big shift from classification to generation.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell + SpaceCraft

Ask: "Last week you compared three emotion models on the same text. Did anyone try a model on their own that gave a surprising result?"

If yes: share it. What did the model get wrong? Why do they think it happened?

If no: quickly show a model you tested between sessions. Keep it to 2 minutes.

**SpaceCraft check-in (2-3 min):**
Pull up SpaceCraft. Show a CPU-only Space you tried to break with an adversarial input — something it wasn't designed for, or an edge case that confuses it. Say: "I tried to break this one. That's what we're about to do — but with real news."

> **SpaceCraft textbook link for this session:** [Chapter 4: Free APIs](https://buildlittleworlds.github.io/spaceCraft/free-apis.html) covers exactly the pattern we're about to build — using the GNews API from a Gradio Space. After the live build, consider sharing this link with students who want to try other free APIs (weather, dictionaries, translation) in their own Spaces.

**Transition:** "For two weeks we've been feeding text to models and watching what they say. Today we find out what they can't do. And we're going to use real news headlines to do it."

### 0:10–0:25 — Break the News Sentiment Analyzer

Open the News Sentiment Analyzer Space (pre-built, uses GNews API + distilbert sentiment). Pull headlines from a few different categories: Breaking News, Business, Science, Sports.

**What to look for (have these categories ready):**

| Category | What to watch for |
|----------|-------------------|
| Breaking News | Disaster coverage in measured tone — model says "Good news" because language is calm |
| Business | "Markets soar as thousands lose jobs" — model reads "soar" as positive |
| World | Complex geopolitical stories — model forced to pick one sentiment |
| Science | Nature/weather/climate stories — model projects emotion onto non-human subjects |

**For each batch of headlines, ask students:**
1. Does the "Good news / Bad news" label match YOUR reading?
2. Which headlines did the model get wrong?
3. WHY did it get them wrong — is it the words, or the meaning behind the words?

**Quick two-column exercise (on screen, 3 minutes max):**

| We CAN fix (noise) | We CAN'T fix (meaning) |
|---------------------|----------------------|
| Clickbait formatting | Editorial framing |
| ALL CAPS headlines | Implied context |
| Sensationalist punctuation | Metaphor ("markets panic") |
| Emoji in social media news | Story behind the headline |
| | Multi-faceted situations |

**Say:** "Some problems are noise — formatting junk. Some are meaning — the real situation behind the words. The model reads words. You read the story. That gap is what we're exploring tonight."

### 0:25–0:45 — Build the World Headlines Space (Live Build)

> **What we're building and why:** This segment is a live Hugging Face Space build. You'll create a Space from scratch that calls an external news API and displays headlines from 10 different countries. Students see the two-file Space pattern (app.py + requirements.txt), and they learn something new: how to connect a Space to real-world data through an API. The completed code is in `session-03/app.py`.
>
> **The Space-building pattern:** Every Space on Hugging Face is built from two files: `app.py` (the code) and `requirements.txt` (the libraries). Students have seen this pattern in Sessions 1 and 2. Tonight they watch you build a Space that reaches *outside* Hugging Face to fetch live data.

**Framing:** "Everything we've built so far has been self-contained — the model and the input all live inside Hugging Face. But real AI tools need to connect to the outside world. The news apps I showed you at the start do exactly that — they reach out to a news service, pull back headlines, and then run a model on them. Let me show you how that works. It's simpler than you think."

**Open a new Space on Hugging Face.** Name it something like `world-headlines`. Select Gradio as the SDK.

**Build `requirements.txt` first (30 seconds):**
```
gradio>=5.0.0
requests
```

"Two libraries. Gradio builds the interface. Requests talks to the internet."

**Build `app.py` step by step:**

**Step 1: Import and configure**
```python
import os
import gradio as gr
import requests

GNEWS_API_KEY = os.environ.get("GNEWS_API_KEY")
```
"We're reading the API key from a secret — it never appears in the code. I set this up in the Space's Settings tab."

**Step 2: Define the countries**
```python
COUNTRIES = {
    "United States": "us",
    "United Kingdom": "gb",
    "Canada": "ca",
    "Australia": "au",
    "India": "in",
    "Germany": "de",
    "France": "fr",
    "Nigeria": "ng",
    "Brazil": "br",
    "China": "cn",
}
```
"A dictionary that maps country names to codes. The API uses two-letter codes."

**Step 3: The API call**
```python
def fetch_headlines(country_name):
    country_code = COUNTRIES[country_name]
    params = {
        "token": GNEWS_API_KEY,
        "country": country_code,
        "max": 10,
        "lang": "en",
    }
    resp = requests.get(
        "https://gnews.io/api/v4/top-headlines",
        params=params, timeout=15
    )
    data = resp.json()
```
"Three lines do the real work. We build a dictionary of parameters, make the request, and parse the response as JSON. That's the whole API pattern — you'll see it everywhere."

**Step 4: Format the output**
```python
    articles = data.get("articles", [])
    lines = []
    for i, article in enumerate(articles, 1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown")
        url = article.get("url", "")
        lines.append(f"### {i}. {title}\n**Source:** {source}\n[Read article]({url})\n")
    return "\n".join(lines)
```

**Step 5: Gradio interface**
```python
with gr.Blocks(title="World Headlines") as demo:
    gr.Markdown("# World Headlines")
    country = gr.Dropdown(choices=list(COUNTRIES.keys()), value="United States")
    btn = gr.Button("Get Headlines", variant="primary")
    output = gr.Markdown()
    btn.click(fn=fetch_headlines, inputs=country, outputs=output)
demo.launch()
```

**Quick test:** Select a country, click the button, see live headlines appear. Students see the full cycle: code → API → live data → display.

**Land the point:** "We just built a Space that reaches out to the real world and brings data back. That's the pattern behind every AI tool that connects to external data — weather apps, stock trackers, news aggregators. Two files. One API call. Now let's go back to the question that matters: what can models actually understand about this data?"

**Deploy the Space:** Commit the files. While it rebuilds, say: "Same cycle as always: edit code, commit, rebuild, test. Now let me show you what happens when we put a sentiment model on top of real headlines."

### 0:45–1:15 — Zero-Shot News Analyzer Demo (The Centerpiece)

**Transition:** "The News Sentiment Analyzer we tested earlier uses a fixed model — it can only say 'good news' or 'bad news.' But what if you could choose your own categories? What if you could ask the model to sort headlines into whatever buckets YOU define — without retraining anything?"

**Setup:** Open the Zero-Shot News Analyzer Space. Explain briefly: "This Space uses a different kind of model — a zero-shot classifier. You type in whatever categories you want, and the model figures out which one fits best. It's never been trained on your specific labels. It uses its understanding of language to make a judgment."

#### Test 1: Good News vs. Bad News on Breaking Headlines (~8 min)

Start with the simple preset: "Good news vs. Bad news." Fetch Breaking News headlines.

**Look for tone deafness examples.** Headlines about serious events written in neutral journalistic tone: "Rescue crews locate survivors in flood zone" — the model might say "good news" because of "survivors," but the context is a disaster. Or business headlines where positive-sounding words describe negative outcomes: "Efficiency gains lead to workforce reduction across tech sector."

**Ask:** "The model says 'good news.' Do you agree? What does the model see that makes it say that? What does it miss?"

**Name it:** "This failure is **tone deafness** — the model reads the words but misses the meaning behind them. Same as sarcasm: the surface doesn't match the reality."

#### Test 2: Custom Categories — Hopeful, Worrying, Mixed (~8 min)

Switch to the preset "Hopeful vs. Worrying vs. Mixed signals." Fetch World or Business headlines.

**Look for emotional flattening examples.** Complex headlines where the story genuinely has multiple dimensions: climate policy stories (progress AND insufficient), economic stories (growth AND inequality), peace negotiations (hope AND ongoing conflict). The model has to pick its top category even when the story is genuinely all three.

**Ask:** "Look at the confidence scores. When the model says 'hopeful' at 42% and 'worrying' at 38% — what's it telling you? Is it confident, or confused? Is the headline actually one thing, or is it genuinely mixed?"

**Name it:** "This failure is **emotional flattening** — the model is forced to rank one label on top, even when the real answer is 'it's complicated.' Classification demands a winner. Reality doesn't."

#### Test 3: Neutral Reporting vs. Editorial vs. Clickbait (~8 min)

Switch to "Neutral reporting vs. Editorial opinion vs. Clickbait." Fetch the same headlines again.

**Look for anthropomorphic projection examples.** Headlines about markets ("Markets rally," "Stocks tumble in early trading"), weather ("Storm batters coastline"), or the economy ("Economy shows signs of strain"). The model reads emotional weight in these metaphors — "batters" sounds aggressive, "tumble" sounds fearful, "rally" sounds joyful — but these are standard journalistic metaphors, not descriptions of anyone's feelings.

**Push further:** "Who is feeling the fear in 'Stocks tumble'? Who is celebrating in 'Markets rally'? The model reads these like someone describing a person — but they're describing numbers on a screen."

**Name it:** "This failure is **anthropomorphic projection** — the model reads human emotion into language about non-human things. Markets don't panic. Storms don't rage with anger. But the words sound emotional, so the model treats them that way."

#### Now change the categories (~6 min)

This is the key pedagogical move. **Have students suggest new categories.** Type them in live. Try something completely different: "urgent vs. routine vs. human interest" or "local impact vs. global impact vs. celebrity."

**The discovery:** Even when students control the categories — even when they design the perfect set of labels — the model still hits the same wall. It's still picking one label. It still can't hold complexity. It still reads words, not meaning.

**Say:** "You just designed your own classification system. Custom categories. No retraining. And the model still made the same kinds of mistakes. That's because the problem isn't the categories — it's the structure of classification itself. One input, one label. That's the ceiling."

#### Wrap the demo (3 min)

Put all three failure modes on screen:

| Test | Failure Mode | What Happens |
|------|-------------|-------------|
| Good/Bad on disaster coverage | **Tone deafness** | The model misses meaning that IS there |
| Hopeful/Worrying on complex stories | **Emotional flattening** | The model oversimplifies meaning that's complex |
| Neutral/Editorial on market metaphors | **Anthropomorphic projection** | The model invents meaning that ISN'T there |

**Say:** "Three tests. Three different ways the models fail. And the most important thing: even defining your own categories didn't fix any of them. Better labels isn't better understanding."

### 1:15–1:30 — Sum Up The Old Way

**This segment is the Act I closer.**

**Say:** "Let me step back and tell you what we've been doing for three weeks. Because it's not just three random lessons — it's a story.

Session 1: we saw that a model can read a sentence and say 'positive' or 'negative.' That's called classification — sorting things into buckets. The model looks at an input, and it picks a label from a menu.

Session 2: we saw that different models have different menus. One model has two buckets: positive and negative. Another has seven. Another has twenty-eight. And they disagree with each other — because each model learned from different data. What it sees depends on what it studied.

Session 3 — tonight — we put models on real news and broke them three ways. They missed the meaning behind neutral-sounding headlines. They flattened complex stories into single labels. They projected emotions onto markets and weather. And we even tried letting you define your own categories — a model that had never been trained on your labels — and it still hit the same wall.

Here's the thing: what we just experienced tonight is what AI looked like for most of its history. For decades, this was the cycle. Build a small model for a narrow task. Clean the data. Choose your categories. Test it. Watch it fail on anything that requires real understanding. Try better categories. Hit the same wall: the model reads words, but it doesn't understand what they mean.

Every model we've seen — the Mood Meter, the Emotion Spectrum, the News Sentiment Analyzer, even the zero-shot model with your custom labels — does the same thing. It classifies. It sorts text into buckets. It picks a label. And that's genuinely useful for some tasks. But it has a ceiling. It can't read between the lines of a headline because meaning lives in context, not in words. It can't hold two truths at once because it has to pick one label. It can't tell the difference between a reporter describing a disaster and a person experiencing one.

So here's my question for next week."

**Pause. Let this land.**

"What if we stopped asking models to sort things into buckets? What if instead of giving a model a sentence and asking it to pick a label — positive, negative, hopeful, worrying — we asked it to do something completely different? What if we asked it to create something new? To write, instead of read?

That's what we're doing next week. And it changes everything."

### 1:30–1:40 — CLEAR Framework

Introduce the CLEAR Framework for prompting AI coding assistants:

| Letter | Meaning | Example |
|--------|---------|---------|
| **C** | Context | "I have a Gradio app that fetches news headlines from an API..." |
| **L** | Language | "The code is in Python, using gradio, requests, and transformers..." |
| **E** | Explain | "I want to add sentiment analysis to each headline so users can see..." |
| **A** | Ask | "Can you add a function that runs each headline through a sentiment model..." |
| **R** | Requirements | "Use distilbert sentiment. Show a colored badge next to each headline — green for positive, red for negative." |

**Live demo:** Open Claude or ChatGPT. Paste the World Headlines Space code. Write a CLEAR prompt asking it to add sentiment analysis to the headlines. Show students the response.

**Say:** "This is how you talk to an AI coding assistant. You'll use this throughout the rest of the course — especially when you build your own Space. Notice how specific the prompt is — it doesn't just say 'make it better.' It says exactly what to add and how it should look."

### 1:40–1:50 — Student Topic Elicitation

**Say:** "For the rest of this course, you're going to be developing your own research question. It can be about anything — not just sentiment, not just text. We've seen models that read emotions, models that analyze news headlines, models that classify text into any categories you define. Next week you'll see models that write text. There are models that recognize images, translate languages, generate music, detect objects, read handwriting — anything.

So right now, I want to hear from each of you: what are you curious about? What topic would you want AI to help with? Don't worry about whether it's realistic or whether a model exists for it. Just tell me what interests you."

**Go around the group. Take notes.** Write each student's topic/interest on the shared screen. These become the seeds for research plans.

**If students are stuck, prompt with:**
- "What do you wish a computer could do?"
- "What's a problem you've seen where AI might help — or might make things worse?"
- "Is there a subject you care about where you wonder how AI would handle it?"

**Don't evaluate or narrow their ideas yet.** Just collect them. You'll come back to these in later sessions.

### 1:50–2:00 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. Run the setup cell and load the models (sentiment + zero-shot)
2. Run the tone deafness test on pre-selected news headlines
3. Run the zero-shot cell with different category sets
4. Compare: did custom categories help?

**Say:** "The notebook has pre-selected news headlines so you can experiment even without an API key. Try changing the categories in the zero-shot cells — invent your own and see what happens."

**Notebook skill being introduced:** Editing code in a cell (changing category labels) and re-running

**GitHub skill being introduced:** "Upload this notebook to your `my-ai-portfolio` repo."

### 2:00 — Wrap Up

Share the between-session challenge. Encourage them to use CLEAR to ask Claude/ChatGPT for help.

**Say:** "Next week we cross a line. Everything we've done so far has been classification — models that sort things into categories. Next week, we see what happens when a model creates something instead of labeling it. It's a completely different kind of AI. And it's the idea behind every chatbot, every image generator, and every AI tool you've ever used."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| GNews API key not working or rate limited | Free tier is 100 requests/day. Use the pre-fetched headlines in the notebook as fallback. Test before class. |
| News Sentiment or Zero-Shot Spaces are slow (model cold starts) | Open all Spaces 10 min before class. Run a test query to wake the models. |
| Headlines are boring or don't show clear failures | Have 3-4 specific headlines ready that you know demonstrate each failure mode. You can type them directly into the Spaces. |
| Students fixate on one failure mode and want to discuss it at length | Great energy — but manage time. Say "We're going to see two more failure modes that are just as interesting. Hold that thought." |
| API call in live build returns an error | Have the complete `app.py` ready to paste. Most common issue: missing API key secret. |
| Zero-shot model is slow on free CPU | It takes 5-10 seconds per batch. Warn students: "This model is bigger than the sentiment model — it needs more time to think." |
| Students want to add their own countries to the headlines Space | Great instinct! "That's exactly the kind of modification you can make with CLEAR. Try it this week." |
| CLEAR demo produces different code than yours | Fine and useful. "AI assistants give different answers each time. That's why you need to understand what the code does." |
| Space rebuild fails after editing | Check for syntax errors. Most common: missing closing parenthesis, indentation errors, missing import. |
| Students don't have topic ideas during elicitation | Don't force it. Say "Think about it this week. You can message me or bring ideas next session." |
| The "Sum Up The Old Way" monologue runs long | Practice it. It should be 5-7 minutes of talking, not 15. The power is in the clarity and the pause before the forward bridge, not in length. |

---

## Key Vocabulary (introduce casually)

- **Adversarial input** — text or data deliberately chosen to confuse or break a model
- **API (Application Programming Interface)** — a way for one program to request data from another; the World Headlines Space calls the GNews API to fetch live news
- **Noise** — formatting junk that confuses the model (clickbait formatting, ALL CAPS, emoji)
- **Meaning** — the real situation behind the words — what noise removal can't fix
- **Classification** — a model that sorts inputs into predefined categories (positive/negative, good news/bad news)
- **Zero-shot classification** — classification where the model uses categories it was never trained on; you define the labels at runtime
- **Tone deafness** — when a model misses meaning that IS there (measured language about a disaster, positive words about negative outcomes)
- **Emotional flattening** — when a model oversimplifies meaning that's complex (multi-faceted stories forced into one label)
- **Anthropomorphic projection** — when a model invents meaning that ISN'T there (reading emotion into "markets panic" or "storm rages")
- **CLEAR Framework** — a structure for writing good prompts to AI coding assistants (Context, Language, Explain, Ask, Requirements)

---

## Materials Checklist

- [ ] GNews API key working and set as a Secret on all three Spaces
- [ ] World Headlines Space code ready (complete `app.py` in case live build has issues)
- [ ] News Sentiment Analyzer Space loaded and tested with multiple categories
- [ ] Zero-Shot News Analyzer Space loaded and tested with multiple preset categories
- [ ] 3-4 specific headlines noted that clearly demonstrate each failure mode (fallback if live headlines are bland)
- [ ] CLEAR Framework slide or screen-share ready
- [ ] Notebook Colab link ready to share in Zoom chat
- [ ] Paper/doc for taking notes on student topic ideas

---

## Concept Connections

- **Session 1:** Students learned INPUT → MODEL → OUTPUT. The model classifies text.
- **Session 2:** Students learned that training data shapes what the model can see. Different data = different classification.
- **Session 3 (this session):** Students learn that classification has fundamental limits — even with custom categories on real-world data, models read words, not meaning. This is "The Old Way." They also learn to connect Spaces to external APIs.
- **Session 4 (next):** The turn. Classification vs. Generation. "What if the model could create, not just sort?"

---

## Spaces Reference

| Space | What It Does | API Key Needed | Model |
|-------|-------------|----------------|-------|
| World Headlines | Fetches top headlines from 10 countries | GNEWS_API_KEY | None (data display only) |
| News Sentiment Analyzer | Fetches headlines by topic, labels each good/bad | GNEWS_API_KEY | distilbert-base-uncased-finetuned-sst-2-english |
| Zero-Shot News Analyzer | Fetches headlines, classifies with user-defined categories | GNEWS_API_KEY | facebook/bart-large-mnli |

All three Spaces use the same GNews API key. Students only need to sign up at [gnews.io](https://gnews.io) if they want to build their own.

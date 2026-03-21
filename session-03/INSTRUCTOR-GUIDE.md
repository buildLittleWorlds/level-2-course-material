# Session 3: What Models Can't Do

**Concept:** ADVERSARIAL TESTING AND THE LIMITS OF CLASSIFICATION
**Space:** Sarcasm Breaker (Session 1 Mood Meter + cleaning)
**Story Arc Spaces:** 3-Sentiment, 6-Emotion, 7-Ekman, 28-GoEmotions
**Pre-built fallback:** Have both the Sarcasm Breaker and all four Story Arc Spaces loaded and tested before class.

**Narrative role:** This session closes Act I — "The Old Way." By the end, students have three sessions of evidence that classical ML models can sort text into buckets but don't understand what they're reading. The session ends with a named summary of what Sessions 1-3 have shown and a forward bridge to Session 4's big shift from classification to generation.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell + SpaceCraft

Ask: "Last week you compared three emotion models on the same text. Did anyone try a model on their own that gave a surprising result?"

If yes: share it. What did the model get wrong? Why do they think it happened?

If no: quickly show a model you tested between sessions. Keep it to 2 minutes.

**SpaceCraft check-in (2-3 min):**
Pull up SpaceCraft. Show a Space you tried to break with an adversarial input — something it wasn't designed for, or an edge case that confuses it. For example, give an OCR Space a blurry photo, or give an image generator a contradictory prompt. Say: "I tried to break this one. That's what we're about to do with our Mood Meter — and then with something much bigger."

**Transition:** "For two weeks we've been feeding text to models and watching what they say. Today we find out what they can't do. And it's a lot."

### 0:10–0:25 — Break the Mood Meter

Open the Session 1 Space (original Mood Meter, no cleaning). Start typing adversarial inputs. Have students suggest inputs too.

**Pre-prepared adversarial inputs (6 inputs, not 10 — move quickly):**

| Input | Category | What happens |
|-------|----------|-------------|
| `Oh GREAT, another Monday. Just what I needed.` | Sarcasm | Model reads "GREAT" literally — probably POSITIVE |
| `Per my last email, as I mentioned before...` | Passive aggression | Model probably says NEUTRAL/POSITIVE — misses the venom |
| `no literally I'm deceased this is the funniest thing 💀💀💀` | Gen-Z irony | Model doesn't know "deceased" means "laughing so hard" |
| `I'm fine. Everything is fine. This is fine.` | Mixed signals | Words are positive, tone is everything-is-on-fire |
| `Worst day ever 😂🎉💀` | Emoji contradictions | Words say worst, emoji say party |
| `Yeah, I totally LOVE getting up at 5am. It's my FAVORITE thing.` | ALL CAPS sarcasm | Model reads LOVE and FAVORITE literally |

**For each input, ask students:**
1. What did you expect?
2. What did the model say?
3. How would YOU read this if a friend texted it?

**Quick two-column exercise (on screen, 3 minutes max):**

| We CAN fix (noise) | We CAN'T fix (meaning) |
|---------------------|----------------------|
| Extra spaces | Sarcasm |
| Repeated characters ("sooooo") | Irony |
| Emoji (strip them) | Understatement |
| ALL CAPS (normalize) | Passive aggression |
| | Context / backstory |

**Say:** "Some problems are noise — formatting junk. Some are meaning — the real intention behind the words. We can clean noise. We can't clean meaning. Let me show you what cleaning looks like."

### 0:25–0:45 — Fix It: Build the Sarcasm Breaker Space (Live Build)

> **What we're building and why:** This segment is a live Hugging Face Space build. You'll take the Session 1 Mood Meter Space (`app.py` + `requirements.txt`) and add a `clean_text()` function to it, creating the "Sarcasm Breaker" — a Space that shows the model's reading before and after cleaning. Students see the code, see the deploy, and see the result. The purpose is twofold: (1) they practice the Space-building pattern they'll use all course, and (2) the Space itself demonstrates the lesson — cleaning fixes noise but can't fix meaning. The completed code is in `session-03/app.py`.
>
> **The Space-building pattern:** Every Space on Hugging Face is built from two files: `app.py` (the code) and `requirements.txt` (the libraries). Students have seen this pattern in Sessions 1 and 2. Tonight they watch you modify the code live, commit, and rebuild. This is the same workflow they'll use when they build their own Spaces later in the course.

**Framing (this is new):** "What I'm about to show you isn't just a fix for our little app. For decades, this is what AI researchers spent most of their time doing. Before the AI systems you use today existed — before ChatGPT, before Claude, before any of that — people had to manually clean every input, build every feature, strip every emoji, normalize every piece of text. By hand. For every new task. Every new language. Every new domain. This function we're about to write represents years of human labor across the entire field."

**Open the Space on Hugging Face.** Go to the Files tab. Open `app.py`. Students should see the code from Session 1 — load model, check mood, Gradio interface. Say: "This is the same code from Session 1. Two files make a Space: `app.py` is the code, `requirements.txt` lists the libraries. We're going to add a cleaning function to the code and rebuild the Space."

Click **Edit** on `app.py`. Add `import re` at the top, then add the `clean_text()` function above `check_mood()`.

Build it step by step, explaining each piece:

**Step 1: Strip whitespace**
```python
text = text.strip()
```
"The simplest fix. Remove junk from the beginning and end."

**Step 2: Collapse multiple spaces**
```python
text = re.sub(r' {2,}', ' ', text)
```
"Turn five spaces into one space."

**Step 3: Limit repeated characters**
```python
text = re.sub(r'(.)\1{2,}', r'\1\1', text)
```
"Turn 'sooooo' into 'soo.' The model might understand 'soo' but definitely not 'sooooooo.'"

**Step 4: Remove emoji**
```python
text = re.sub(
    r'[\U0001F600-\U0001F64F'
    r'\U0001F300-\U0001F5FF'
    r'\U0001F680-\U0001F6FF'
    r'\U00002600-\U000026FF]+',
    ' ', text
)
```
"The model doesn't know what a skull emoji means. Strip it out so it can focus on the words."

**Step 5: Normalize ALL CAPS**
```python
if caps_count > 3:
    text = text.title()
```
"ALL CAPS might change the model's reading. Normalizing makes it cleaner but also flatter."

**Quick test:** Run 2-3 adversarial inputs through the before/after comparison. Show that cleaning helps with noise (emoji, caps) and doesn't help with meaning (sarcasm, irony).

**Land the point:** "We just spent 20 minutes writing code to fix formatting problems. The model still can't detect sarcasm. Imagine doing this for every kind of text, in every language, for every new domain. That was the old way of doing AI. It worked — sort of — but it was slow, it was manual, and it always hit the same wall: you can clean the noise, but you can't teach the model to understand what the words actually mean."

**Deploy the Space:** Click **Commit changes** at the bottom of the editor. The Space will rebuild (30–60 seconds). While it rebuilds, say: "We just changed the code and redeployed. That's the cycle: edit the code, commit, rebuild, test. Every Space on Hugging Face works this way. When you build your own Space later in this course, this is exactly the workflow."

Once the Space is live, test it with 1–2 sarcastic inputs to confirm the before/after comparison works. Then move on — the Story Arc demo is the centerpiece, not this build.

### 0:45–1:15 — Story Arc Adversarial Demo (The Centerpiece)

**Transition:** "So far we've been testing one model on single sentences. Now I want to show you something bigger. We're going to test four different models on the same stories — and we're going to break all of them."

**Setup:** Open all four Story Arc Spaces in browser tabs:
- Story Arc — 3-Class Sentiment (positive / negative / neutral)
- Story Arc — 6 Emotions (sadness, joy, love, anger, fear, surprise)
- Story Arc — 7 Ekman Emotions (anger, disgust, fear, joy, neutral, sadness, surprise)
- Story Arc — 28 GoEmotions (admiration, amusement, anger, ... 28 categories)

**Explain briefly:** "These four apps do the same thing — you paste a story, and they chart the emotions across each paragraph. But each one uses a different model with a different number of emotion categories. Three emotions. Six emotions. Seven emotions. Twenty-eight emotions. Same story, four different lenses."

#### Test 1: The Sarcastic Narrator (~8 min)

**Say:** "Our first test story is about a student having the worst Monday of their life. But every sentence sounds positive. See if you can hear the sarcasm."

Read the first paragraph aloud so students hear the tone. Then paste the full story into all four Spaces.

**While results load, ask:** "This person had a terrible day. The words all sound positive. What do you think the models will say?"

**After results:** Look at the arc charts together.

**Discussion:** "According to these four models, did this person have a good day? Every model says yes — because every model reads the words, not the tone. The 3-class model says positive. The 28-class model spreads it across joy and admiration and approval. More categories didn't help. Twenty-eight labels isn't smarter than three — it's just more specific about being wrong."

**Name it:** "This failure is **tone deafness** — the model hears the notes but misses the music."

#### Test 2: The Mixed-Emotion Story (~8 min)

**Say:** "This story is about getting into your dream college. But getting in means leaving home. Every paragraph has at least two real emotions at the same time."

Paste into all four Spaces.

**After results:** "Look at each paragraph. The narrator is feeling pride and grief and excitement and fear — all at once. What does the model show?"

Most paragraphs will collapse to a single dominant emotion. The 28-emotion model might scatter scores across several labels, but look at the confidence: is the top score 18% with five others at 12%? That's not detecting complexity — that's confusion.

**Ask:** "Is there a single paragraph in this story where the narrator is feeling only one thing?" (No.) "Does any model show two strong emotions in the same paragraph?" (Probably not.)

**Name it:** "This failure is **emotional flattening** — the model forces complex feelings into a single label. It's like being asked 'are you happy or sad?' when the real answer is both."

#### Test 3: The Earth Doesn't Feel Anything (~8 min)

**Say:** "This last story is about a volcanic eruption and what happens to the land afterward. Pay attention to who's in this story."

Paste into all four Spaces.

**After results:** "The models drew dramatic emotional arcs. Fear for the eruption. Sadness for the dead zone. Joy for the regrowth. But here's my question: who is feeling these emotions? Point to the character in this story who is afraid."

Let them realize: there are no characters. No people. No one is feeling anything. The mountain doesn't have emotions. The wildflowers aren't happy.

**Push further:** "The models are reading 'erupted' and 'destroyed' and 'consumed' and seeing anger and fear — because those words appear alongside anger and fear in the training data. But the volcano isn't angry. The fire isn't hostile. The models are projecting human emotions onto rocks and weather."

**Name it:** "This failure is **anthropomorphic projection** — the model assumes everything that sounds emotional is emotional. It finds feelings where there are none."

#### Wrap the demo (3 min)

Put all three failure modes on screen:

| Test | Failure Mode | What Happens |
|------|-------------|-------------|
| Sarcastic Narrator | **Tone deafness** | The model misses meaning that IS there |
| Mixed Emotions | **Emotional flattening** | The model oversimplifies meaning that's complex |
| Nature Story | **Anthropomorphic projection** | The model invents meaning that ISN'T there |

**Say:** "Three stories. Three different ways the models fail. And the most important thing: having more categories didn't fix any of them. The 28-emotion model failed just as badly as the 3-sentiment model. More labels isn't more understanding."

### 1:15–1:30 — Sum Up The Old Way

**This segment is new. It does not exist in the current session. It's the Act I closer.**

**Say:** "Let me step back and tell you what we've been doing for three weeks. Because it's not just three random lessons — it's a story.

Session 1: we saw that a model can read a sentence and say 'positive' or 'negative.' That's called classification — sorting things into buckets. The model looks at an input, and it picks a label from a menu.

Session 2: we saw that different models have different menus. One model has two buckets: positive and negative. Another has seven. Another has twenty-eight. And they disagree with each other — because each model learned from different data. What it sees depends on what it studied.

Session 3 — tonight — we tried to break those models. And we broke them three ways. They missed sarcasm. They flattened complex emotions into single labels. They projected feelings onto a volcano. And we tried to fix the problem by cleaning the input — stripping emoji, normalizing caps, collapsing repeated characters — and it helped a little, but it didn't solve the real problem.

Here's the thing: what we just experienced tonight is what AI looked like for most of its history. For decades, this was the cycle. Build a small model for a narrow task. Spend enormous effort cleaning the data and engineering the features. Test it. Watch it fail on anything it wasn't specifically trained for. Try to fix the failures by cleaning harder. Hit the same wall: the model reads words, but it doesn't understand what they mean.

Every model we've seen — the Mood Meter, the Emotion Spectrum, all four Story Arc models — does the same thing. It classifies. It sorts text into buckets. It picks a label. And that's genuinely useful for some tasks. But it has a ceiling. It can't detect sarcasm because sarcasm lives between the words. It can't hold two emotions at once because it has to pick one label. It can't tell the difference between a person feeling fear and a volcano erupting because it doesn't know what feelings are — it just knows which words tend to appear near which labels.

So here's my question for next week."

**Pause. Let this land.**

"What if we stopped asking models to sort things into buckets? What if instead of giving a model a sentence and asking it to pick a label — positive, negative, angry, sad — we asked it to do something completely different? What if we asked it to create something new? To write, instead of read?

That's what we're doing next week. And it changes everything."

### 1:30–1:40 — CLEAR Framework

Introduce the CLEAR Framework for prompting AI coding assistants:

| Letter | Meaning | Example |
|--------|---------|---------|
| **C** | Context | "I have a Gradio app that uses a sentiment analysis model..." |
| **L** | Language | "The code is in Python, using the transformers library..." |
| **E** | Explain | "When I paste sarcastic text, the model reads it as positive..." |
| **A** | Ask | "Can you add a text cleaning function that..." |
| **R** | Requirements | "It should handle emoji, repeated characters, and ALL CAPS." |

**Live demo:** Open Claude or ChatGPT. Paste the Space code. Write a CLEAR prompt asking it to add input cleaning. Show students the response.

**Say:** "This is how you talk to an AI coding assistant. You'll use this throughout the rest of the course — especially when you build your own Space."

### 1:40–1:50 — Student Topic Elicitation

**Say:** "For the rest of this course, you're going to be developing your own research question. It can be about anything — not just sentiment, not just text. We've seen models that read emotions. Next week you'll see models that write text. There are models that recognize images, translate languages, generate music, detect objects, read handwriting — anything.

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
1. Run the setup cell and load the model
2. Run the "before cleaning" cell — see the sarcastic input results
3. Run the `clean_text()` definition cell
4. Run the "after cleaning" cell — compare

**Say:** "The notebook has the same `clean_text()` function we built. Try the experiments — test your own texts and see what cleaning can and can't fix."

**Notebook skill being introduced:** Editing code in a cell (changing the text variable) and re-running

**GitHub skill being introduced:** "Upload this notebook to your `my-ai-portfolio` repo."

### 2:00 — Wrap Up

Share the between-session challenge. Encourage them to use CLEAR to ask Claude/ChatGPT for help.

**Say:** "Next week we cross a line. Everything we've done so far has been classification — models that sort things into categories. Next week, we see what happens when a model creates something instead of labeling it. It's a completely different kind of AI. And it's the idea behind every chatbot, every image generator, and every AI tool you've ever used."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| Story Arc Spaces need HF token or hit rate limits | Have an HF token ready. If API fails, Spaces fall back to demo data — usable but less impactful. Test all four before class. |
| Story Arc Spaces are slow (model cold starts) | Open all four tabs 10 min before class. Run the example texts to wake the models. |
| Students fixate on one failure mode and want to discuss it at length | Great energy — but manage time. Say "We're going to see two more failure modes that are just as interesting. Hold that thought." |
| Editing `app.py` in HF browser editor is fiddly | Have the complete code ready to paste. Show students how to select all, paste. |
| Regex is confusing for students | Don't explain regex syntax. Just say "this pattern finds repeated characters" and move on. The point is what it does, not how. |
| Students want to fix sarcasm detection | Great instinct! "Even humans disagree on sarcasm. There are whole PhD theses about this. But here's the interesting question: what if there were a completely different approach — not fixing classification, but doing something else entirely? That's next week." |
| CLEAR demo produces different code than yours | Fine and useful. "AI assistants give different answers each time. That's why you need to understand what the code does." |
| Space rebuild fails after editing | Check for syntax errors. Most common: missing closing parenthesis, indentation errors. |
| Students don't have topic ideas during elicitation | Don't force it. Say "Think about it this week. You can message me or bring ideas next session." |
| The "Sum Up The Old Way" monologue runs long | Practice it. It should be 5-7 minutes of talking, not 15. The power is in the clarity and the pause before the forward bridge, not in length. |

---

## Key Vocabulary (introduce casually)

- **Adversarial input** — text deliberately designed to confuse or break a model
- **Data cleaning / preprocessing** — transforming text to remove noise before the model sees it
- **Noise** — formatting junk that confuses the model (emoji, extra spaces, ALL CAPS)
- **Meaning** — the real intention behind the words — what noise removal can't fix
- **Classification** — a model that sorts inputs into predefined categories (positive/negative, angry/sad)
- **Tone deafness** — when a model misses meaning that IS there (sarcasm, irony)
- **Emotional flattening** — when a model oversimplifies meaning that's complex (mixed feelings forced into one label)
- **Anthropomorphic projection** — when a model invents meaning that ISN'T there (reading emotion in text about rocks)
- **CLEAR Framework** — a structure for writing good prompts to AI coding assistants (Context, Language, Explain, Ask, Requirements)

---

## Materials Checklist

- [ ] Session 1 Mood Meter Space loaded and working (no cleaning version)
- [ ] Sarcasm Breaker Space deployed with `clean_text()` — OR have complete `app.py` ready to paste
- [ ] All four Story Arc Spaces loaded in browser tabs and tested with example texts
- [ ] Three adversarial stories ready to paste (see `bonus-hugging-face-spaces/ADVERSARIAL-STORIES.md`)
- [ ] CLEAR Framework slide or screen-share ready
- [ ] Notebook Colab link ready to share in Zoom chat
- [ ] Paper/doc for taking notes on student topic ideas

---

## Concept Connections

- **Session 1:** Students learned INPUT → MODEL → OUTPUT. The model classifies text.
- **Session 2:** Students learned that training data shapes what the model can see. Different data = different classification.
- **Session 3 (this session):** Students learn that classification has fundamental limits — no amount of data cleaning fixes the meaning problem. This is "The Old Way."
- **Session 4 (next):** The turn. Classification vs. Generation. "What if the model could create, not just sort?"

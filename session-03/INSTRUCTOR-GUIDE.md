# Session 3: When Sarcasm Breaks Everything

**Concept:** DATA CLEANING AND FEATURE ENGINEERING
**Space:** Sarcasm Breaker
**Model:** `distilbert-base-uncased-finetuned-sst-2-english` (same as Session 1)
**Pre-built fallback:** Have a version with cleaning deployed under profplate/ before class.

---

## Time Breakdown (2 hours)

### 0:00–0:10 — Show-and-Tell

Ask: "Last week you tried finding a model that recognizes feelings our three models couldn't see. Did anyone try one? What feelings could it detect?"

If yes: share it. What model did they find? Did it work? What emotions did it recognize?

If no: quickly show a model you tried between sessions. Keep it to 2 minutes.

**SpaceCraft check-in (2-3 min):**
Pull up SpaceCraft briefly. Show a Space you added this week and try to break it with an adversarial input — something it wasn't designed for, or an edge case that confuses it. For example, give an OCR Space a blurry photo, or give an image generator a contradictory prompt. Say: "I tried to break this one too. That's what we're about to do with our Mood Meter — adversarial testing."

**Transition:** "Today we're going back to our original Mood Meter from Session 1. But instead of comparing different models, we're going to break it — on purpose. We're going to feed it the kind of text that starts fights in your group chat."

### 0:10–0:35 — Break It

Open the Session 1 Space (original Mood Meter, no cleaning). Start typing adversarial inputs. Have students suggest inputs too.

**Pre-prepared adversarial inputs (all tone/sarcasm focused):**

| Input | Category | What happens |
|-------|----------|-------------|
| `Oh GREAT, another Monday. Just what I needed.` | Sarcasm | Model reads "GREAT" literally — probably says POSITIVE |
| `I suppose getting into Harvard is okay.` | Understatement | Model may miss the irony entirely |
| `Per my last email, as I mentioned before...` | Passive aggression | Model probably says NEUTRAL/POSITIVE — misses the venom |
| `no literally I'm deceased this is the funniest thing 💀💀💀` | Gen-Z irony | Model doesn't know "deceased" means "laughing so hard" |
| `I'm fine. Everything is fine. This is fine.` | Mixed signals | Words are positive, tone is everything-is-on-fire |
| `Worst day ever 😂🎉💀` | Emoji contradictions | Words say worst, emoji say party |
| `Yeah, I totally LOVE getting up at 5am. It's my FAVORITE thing.` | ALL CAPS sarcasm | Model may read LOVE and FAVORITE literally |
| `Thanks for getting back to me :)` | Ambiguous politeness | Sincere or seething? |
| `I will always love you` | Context-dependent | Sounds positive — but it's from a breakup song |
| `lolllll sure thing bestie whatever you say 😊` | Passive agreement | The "lol" and "whatever" tell a different story than the emoji |

**For each input, ask students:**
1. What did you expect the model to say?
2. What did it actually say?
3. How would YOU read this tone if a friend texted it to you?

Write the failure categories on the shared screen as they emerge:
- **Sarcasm** — the words say one thing, the meaning is the opposite
- **Understatement** — downplaying something huge
- **Passive aggression** — polite words, hostile intent
- **Emoji contradictions** — text and emoji tell different stories
- **Gen-Z irony** — "deceased" means laughing, "literally can't" means delighted
- **Context collapse** — the words make sense, but only if you know the backstory

### 0:35–0:50 — Name the Failures

Go through the list of failures on screen. Give each category a name.

**Talking points:**
- "These aren't bugs in our code. The code works fine. The *tone* is the problem."
- "The model reads words. You read tone. That's a fundamentally different kind of reading."
- "Some of these we can fix with code. Some we can't fix at all — because the meaning isn't in the words."

Draw two columns:
| We CAN fix | We CAN'T fix |
|------------|-------------|
| Extra spaces | Sarcasm |
| Repeated characters ("sooooo") | Irony |
| Emoji (strip them) | Understatement |
| ALL CAPS (normalize) | Passive aggression |
| | Context / backstory |
| | Cultural tone differences |

**Say:** "The left column is noise — formatting junk the model can't parse. The right column is tone — meaning that lives between the words, not in them. We can clean noise. We can't clean meaning."

**Multimodal aside (30 seconds):** "Here's the thing — most of the 'Can't Fix' column? Sarcasm, irony, passive aggression — you CAN detect those if you hear the voice. Say 'Oh GREAT' out loud like you mean it. Now say it like your Monday just got ruined. Completely different, right? The model loses everything your ears would catch. Later in this course, we'll build something that actually listens."

### 0:50–1:15 — Fix It: Add clean_text()

Open `app.py` in the Files tab. Add the `clean_text()` function above `check_mood()`.

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
"The model doesn't know what 💀 means. Strip it out so it can focus on the words. But here's the thing — when you text '💀💀💀', that IS the meaning. Removing it doesn't help the model understand; it removes information the model never had."

**Step 5: Normalize ALL CAPS**
```python
if caps_count > 3:
    text = text.title()
```
"ALL CAPS might change the model's reading. But think about this: when someone texts 'I LOVE THIS,' the caps ARE the tone. Normalizing them makes the input cleaner but also flatter."

Then show the before/after comparison — run the same text through the model with and without cleaning.

Commit and rebuild.

### 1:15–1:30 — Test the Fix

Run the same adversarial inputs from earlier. Compare results.

**Questions for students:**
- Which inputs work better now?
- Which ones are still broken?
- What's in the "can't fix" column that no amount of cleaning will help with?

**Key insight:** "Data cleaning is a real job. Data scientists spend a huge amount of time cleaning data before models ever see it. But here's the catch: tone is information that gets lost when you strip text down to words. Sarcasm lives in the gap between what you say and what you mean. No amount of cleaning can close that gap."

**Test the sarcasm flag:** Show that the app detects common sarcasm markers ("Oh great," "Just what I needed") — but all it can do is flag them, not understand them. "The model can see the pattern, but it can't feel the eye-roll."

### 1:30–1:40 — Big Question: How Do YOU Detect Sarcasm in a Text Message?

**Set it up:** "We just spent an hour watching the model fail at sarcasm. But here's my question: how do YOU know when someone is being sarcastic in a text?"

**Let students respond.** They'll talk about:
- Who sent it (your best friend vs. your teacher)
- What happened before (context from the conversation)
- How they usually talk (their voice, their patterns)
- Punctuation and emoji clues ("." at the end of "fine." means not fine)

**Push further:**
- "How many fights have started because someone misread the tone of a text?"
- "You've probably done it — sent something you meant as a joke, and the other person got angry. Or received something you thought was mean, and the person said 'I was kidding.'"
- "The model has the same problem you do — it just doesn't know it. You at least know you might be misreading the tone. The model gives you 97% confidence and moves on."

**The deeper point:**
- "Is tone in the words, or between the words?"
- "The model only has the words. You have everything else — the relationship, the context, the history, the vibe. That's why you can detect sarcasm and the model can't."
- "Can a machine ever read between the lines? We'll keep coming back to this."

**Don't resolve this.** Let them sit with the tension: the model is confidently wrong about tone, and humans are sometimes wrong about tone too. The difference is that humans know they might be wrong.

### 1:40–1:50 — CLEAR Framework + Name the Concept

#### CLEAR Framework (5 min)

Introduce the CLEAR Framework for prompting AI coding assistants:

| Letter | Meaning | Example |
|--------|---------|---------|
| **C** | Context | "I have a Gradio app that uses a sentiment analysis model..." |
| **L** | Language | "The code is in Python, using the transformers library..." |
| **E** | Explain | "When I paste sarcastic text, the model reads it as positive..." |
| **A** | Ask | "Can you add a text cleaning function that..." |
| **R** | Requirements | "It should handle emoji, repeated characters, and ALL CAPS." |

**Live demo:** Open Claude or ChatGPT. Paste the Space code. Write a CLEAR prompt asking it to add input cleaning. Show students the response.

**Example CLEAR prompt:**
> **Context:** I have a Hugging Face Space that uses a sentiment analysis model to read the mood of text.
>
> **Language:** Python, using gradio, transformers, and re.
>
> **Explain:** When users paste sarcastic or messy text (emoji, ALL CAPS, repeated characters like "sooooo", mixed signals), the model misreads the tone.
>
> **Ask:** Add a `clean_text()` function that preprocesses the input before the model sees it.
>
> **Requirements:** Strip whitespace, collapse repeated characters, remove emoji, normalize ALL CAPS. Show the user the before and after versions.

**Say:** "This is how you talk to an AI coding assistant. You'll use this a lot in upcoming sessions."

#### Name the Concept: DATA CLEANING AND FEATURE ENGINEERING (5 min)

Draw this on screen:

```
MESSY INPUT → clean_text() → CLEANER INPUT → MODEL → OUTPUT
```

**Talking points:**
- "The model didn't get smarter. We just gave it better input to work with."
- "But here's what we learned tonight: cleaning helps with noise — but tone is not noise. Tone is meaning."
- "Sarcasm, irony, understatement — these aren't formatting problems. They're human problems. And the model has the same problem you do when you misread a text."
- "In data science, this is called DATA CLEANING — preparing input so the model can do its best work. And FEATURE ENGINEERING — transforming raw input into something the model can actually use."

#### Research Lens (5 min)

**Say:** "Let me name what we just did in research terms. We tested **adversarial inputs** and performed **data preprocessing** — cleaning noise vs. signal. In research, adversarial testing means deliberately trying to break a system to find its limits. And preprocessing means transforming data before the model sees it — exactly what `clean_text()` does."

**Frame the shared research question:** "Here's the research question we were investigating tonight: *What types of text input cause sentiment models to fail, and can preprocessing fix them?* We ran a controlled before/after comparison — same inputs, with and without cleaning — and found that cleaning fixes noise but not meaning."

**Bridge to their own work:** "In class, we applied adversarial testing and preprocessing to sentiment. For your homework, you'll apply the same method to your own topic — find an input that breaks a model in your Collection, figure out whether it's a noise problem or a meaning problem, and try to fix it. Same method, your question."

### 1:50–2:00 — Notebook Time

Share the Colab link in the Zoom chat.

**Walk through together:**
1. Run the setup cell and load the model
2. Run the "before cleaning" cell together — see the sarcastic input results
3. Run the `clean_text()` definition cell
4. Run the "after cleaning" cell — compare the difference

**Say:** "The notebook has the same `clean_text()` function we built. Try the experiments — test your own sarcastic texts and see what cleaning can and can't fix."

**Notebook skill being introduced:** Editing code in a cell (changing the text variable) and re-running

**GitHub skill being introduced:** "Upload this notebook to your `my-ai-portfolio` repo."

### 2:00 — Wrap Up

Share the between-session challenge. Encourage them to use CLEAR to ask Claude/ChatGPT for help.

**Say:** "Next week we're putting three models head-to-head on the same text. When three judges disagree about how something feels, who's right? Spoiler: maybe nobody."

---

## What Could Go Wrong

| Problem | Fix |
|---------|-----|
| Editing `app.py` in HF browser editor is fiddly | Have the complete code ready to paste. Show students how to select all → paste. |
| Regex is confusing for students | Don't explain regex syntax in detail. Just say "this pattern finds repeated characters" and move on. The point is what it does, not how. |
| Students want to fix sarcasm detection | Great instinct! Explain that sarcasm is an active research problem. "Even humans disagree on sarcasm. There are whole PhD theses about this." |
| CLEAR demo produces different code than yours | That's fine and even useful. "AI assistants give different answers each time. That's why you need to understand what the code does." |
| Space rebuild fails after editing | Check for syntax errors. Most common: missing closing parenthesis, indentation errors. |
| Big Question discussion gets personal (misread texts causing real fights) | That's okay — this is the kind of real connection that makes the session land. Just keep it respectful and don't let anyone share specific names or screenshots. |
| Students insist the model should be able to detect sarcasm | Acknowledge it: "You're right that it should. But think about what it would need — context, history, relationship, cultural knowledge. All it has is the words in front of it." |

---

## Key Vocabulary (introduce casually)

- **Data cleaning** — preprocessing text to remove noise before the model sees it
- **Noise** — stuff in the input that confuses the model (emoji, extra spaces, weird formatting)
- **Adversarial input** — text deliberately designed to confuse or break a model
- **Feature engineering** — transforming raw input into something a model can work with better
- **Preprocessing** — any transformation applied to data before the model processes it
- **Tone** — the way something is said (vs. what is said) — meaning that lives between the words
- **CLEAR Framework** — a structure for writing good prompts to AI coding assistants

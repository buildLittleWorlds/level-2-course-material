# Session 5: Model Training and Parameters
*Student-Facing Title: "Add Controls"*

## Concept: HYPERPARAMETERS

**Spaces Built:** Text Playground (distilgpt2 with sliders), Quick Summarizer (distilbart-cnn-12-6)
**Models:** `distilgpt2` (~80MB, fast on free CPU), `sshleifer/distilbart-cnn-12-6` (~1.2GB, works on free CPU)
**Narrative role:** Last session crossed the fork from classification to generation. This session puts controls on generation. Students leave with deployed Spaces — at least one per student, no exceptions.

---

## Materials Checklist

Before class, have the following open/ready:

- [ ] Hugging Face account logged in, ready to create Spaces for the live builds
- [ ] Session 4's `app.py` open in a tab (the simple text generator with no sliders — this is the starting point for Demo Build 1)
- [ ] Session 5's `app.py` open in a separate tab (the finished Text Playground with sliders — your fallback if the live build hits a snag)
- [ ] Session 5's `summarizer.py` open in a tab (the finished Quick Summarizer — your fallback for Demo Build 2)
- [ ] Pre-deployed backup copies of both Spaces, already running, in case live builds stall
- [ ] Three example texts ready to paste for the summarizer demo:
  - A news article paragraph (for Emily/Henry/Sevilla)
  - A medical text paragraph (for Chengry/George)
  - A game lore paragraph (for Bobby)
- [ ] SpaceCraft textbook open: [Chapter 5: Build Your First Space](https://buildlittleworlds.github.io/spaceCraft/build.html)
- [ ] Zoom chat ready with links to paste during student work time

---

## Student Status — Know Before You Walk In

| Student | Interest | Has Repos? | Has Spaces? | Session 5 Priority |
|---------|----------|------------|-------------|---------------------|
| Bobby | Game dev, creative AI | Yes | Yes | Customize Text Playground with game prompts |
| Annabelle | Creative/playful, music | Yes | Has broken Spaces | Fix broken Space FIRST, then customize |
| Shawn | Image generation comparison | Yes | Yes | Customize Text Playground, explore summarizer |
| Emily | News/research tools | NO | NO | **Get first working Space deployed** |
| Henry | News sentiment, CV | Yes | NO | **Get first working Space deployed** |
| Chengry | Medical AI, built DxAI | Yes | Has runtime error | Fix DxAI runtime error, then build summarizer with medical text |
| George | Medical/health | NO | NO | **Get first working Space deployed** |
| Sevilla | Emotion detection, news | Yes | Yes | Customize with news/emotion prompts |

**Hard goal for tonight:** Every student leaves with at least one running Space. Emily, Henry, and George are the priority cases — if they don't have a working Space by the end of Student Work 1, you are debugging with them during Student Work 2.

---

## Time Breakdown (2 hours)

### Block 1: Framing (0:00–0:12, 12 min)

#### 0:00–0:05 — Check-In: Who Has a Working Space?

Start with a direct question: "Before we do anything — who has a working Space on Hugging Face right now? Open it up and show me."

**What you're looking for:**
- Bobby, Shawn, Sevilla should have working Spaces. Quick thumbs-up and move on.
- Annabelle has broken Spaces. Note it — she'll fix during Student Work 1.
- Emily, Henry, George likely have nothing. Note it — they are your priority students tonight.
- Chengry has a DxAI Space with a runtime error. Note it — debugging during Student Work time.

**Don't fix anything now.** Just take the temperature of the room. Say: "Got it. Some of you have working Spaces, some don't. By the end of tonight, everyone will. That's the promise."

#### 0:05–0:10 — Narrative Bridge from Session 4

"Last week we crossed the fork. We went from classification — sorting into buckets — to generation — writing something new. We built a text generator. It worked. But we had no control over it. It wrote whatever it wanted."

"Think about that. A model that writes, but you can't tell it how to write. That's like having a car with no steering wheel. It moves, but you're just along for the ride."

"Today we add the steering wheel."

#### 0:10–0:12 — The Hook: Controlled vs. Uncontrolled

**Do this live.** Open a pre-deployed Text Playground Space (the one with sliders). Type this prompt:

> "The most important rule of cooking is"

Generate at **temperature 0.2** — read the output aloud. Predictable, safe, boring.

Same prompt. Generate at **temperature 1.5** — read this output aloud. Wild, surprising, possibly nonsensical.

"Same model. Same prompt. The only thing I changed was one slider. That's what we're building today — Spaces where YOU control how the AI behaves."

**Transition:** "We're going to build two Spaces together. The first one adds sliders to last week's text generator. The second one is a completely different kind of generation — summarization. By the end of tonight, you'll have deployed at least one of them. Let's go."

---

### Block 2: Demo Build 1 — Text Playground (0:12–0:37, 25 min)

**What you're building:** The text generator from Session 4, upgraded with temperature, top-p, and max-length sliders. The completed code is in `session-05/app.py`.

**The narrative frame:** This isn't a new project — it's last week's project with controls added. Students should feel this as a natural next step, not a separate thing.

#### 0:12–0:17 — Start from Session 4 Code

Pull up last week's `app.py` on screen. Say: "This is where we left off. A text generator that works, but we can't control. Watch what I add."

**Show the Session 4 code:**

```python
from transformers import pipeline
import gradio as gr

generator = pipeline("text-generation", model="distilbert/distilgpt2")

def generate_text(prompt):
    if not prompt or not prompt.strip():
        return "Type a sentence and watch the model try to continue it."
    result = generator(prompt, max_new_tokens=80, do_sample=True, truncation=True)
    return result[0]["generated_text"]

demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=4, placeholder="Type a sentence or the beginning of a story..."),
    outputs=gr.Textbox(label="What the Model Wrote", lines=8),
    title="Text Generator",
    description="This model doesn't classify — it creates.",
)
demo.launch()
```

"One input. No sliders. No control. Now watch."

#### 0:17–0:30 — Add the Controls, Step by Step

Create a new Space on Hugging Face: "Text Playground" (SDK: Gradio, Hardware: Free CPU).

**Write `requirements.txt` first:** `transformers`, `torch`, `gradio`. Same as last week — point this out. "Same ingredients. We're just adding controls."

**Build `app.py` step by step on screen. Narrate each change:**

**Step 1: Same imports, same model load.** "Nothing changes here. Same library, same model."

```python
from transformers import pipeline
import gradio as gr

print("Loading distilgpt2...")
generator = pipeline("text-generation", model="distilgpt2")
print("Model loaded!")
```

**Step 2: Change the function signature.** "Last week the function took one input — the prompt. Now it takes four."

```python
def generate_text(prompt, temperature, top_p, max_length):
    if not prompt or not prompt.strip():
        return "Type a prompt above first!"
```

**Step 3: Add the controls to the generation call.** "These three new arguments are the sliders."

```python
    result = generator(
        prompt,
        temperature=max(temperature, 0.01),  # avoid division by zero
        top_p=top_p,
        max_length=int(max_length),
        do_sample=True,
        num_return_sequences=1,
    )
    return result[0]["generated_text"]
```

**Teaching moment:** "See `max(temperature, 0.01)`? Temperature of exactly zero would break the math — you'd be dividing by zero. So we clamp it. This is the kind of tiny detail that separates working code from crashing code."

**Step 4: Build the Gradio interface with slider inputs.** "Instead of one text box, we now have a text box plus three sliders."

```python
demo = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=3, placeholder="Start your text here...", label="Prompt"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.7, step=0.1,
                  label="Temperature (creativity)"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.9, step=0.05,
                  label="Top-p (diversity)"),
        gr.Slider(minimum=20, maximum=200, value=100, step=10,
                  label="Max Length (words-ish)"),
    ],
    outputs=gr.Textbox(label="Generated Text", lines=10),
    title="Text Playground",
    description="Type a prompt and use the sliders to control how the AI writes.",
)
```

**Step 5: Add examples.** "These give users a one-click starting point."

```python
    examples=[
        ["Once upon a time in a school where robots", 0.7, 0.9, 100],
        ["The secret ingredient in the recipe was", 1.2, 0.9, 80],
        ["Dear Principal, I am writing to request", 0.3, 0.9, 100],
        ["Breaking news: scientists discover that cats", 0.9, 0.95, 120],
        ["The haunted house at the end of the street", 1.5, 0.8, 150],
    ],
```

**Step 6: Launch.**

```python
demo.launch()
```

#### 0:30–0:37 — Deploy and Test Together

Commit and deploy. While the Space rebuilds (1–2 minutes), say: "Same two files. Same pattern. But now the user has three knobs. Let's see what they do."

Once live, do a quick demo:
- Type: "The secret ingredient in the recipe was"
- Generate at temperature 0.3. Read it aloud. "Safe. Predictable."
- Crank temperature to 1.5. Same prompt. "Wild. Chaotic."
- "Same model, same prompt. The slider is the difference."

**If the build fails or stalls:** Switch to your pre-deployed backup. "I built this earlier — same code. Let's explore while the live one catches up." Don't lose time to build errors.

---

### Block 3: Student Work 1 (0:37–0:57, 20 min)

**Instruction to students:** "Your turn. Duplicate the Text Playground into your own Hugging Face account. Then customize it — change the prompts, change the examples, change the title. Make it yours."

#### Student Work Priority Table — Block 3

| Student | What they should do | Instructor note |
|---------|---------------------|-----------------|
| Bobby | Duplicate, change examples to game dev prompts ("The warrior entered the dungeon and", "The spell's secret ingredient was") | Will move fast — let him experiment |
| Annabelle | **First:** Fix broken Space from previous session. **Then:** Duplicate Text Playground with music prompts | Check her `requirements.txt` and `app.py` for copy-paste errors |
| Shawn | Duplicate, experiment with comparing outputs at different temperature settings | His comparison instinct is an asset — encourage it |
| Emily | **Duplicate the Text Playground as-is.** Don't customize yet — just get it deployed and running | **Priority student.** Walk her through Space creation step by step if needed |
| Henry | **Duplicate the Text Playground as-is.** Get it deployed and running | **Priority student.** Same as Emily — deploy first, customize later |
| Chengry | Debug DxAI runtime error first. Then duplicate Text Playground | Check his `requirements.txt` for version conflicts |
| George | **Duplicate the Text Playground as-is.** Get it deployed and running | **Priority student.** Same as Emily/Henry |
| Sevilla | Duplicate, change examples to news/emotion prompts ("Breaking: the president announced", "She felt a wave of") | Comfortable — will move at her own pace |

**Instructor movement pattern:** Spend the first 5 minutes with Emily, Henry, and George — make sure they can create a Space and paste in the code. Then circulate. Come back to check their builds are running before the block ends.

**If a student finishes early:** "Try the same prompt at five different temperature settings. Write down what you notice. We'll name what you're doing later."

**At 0:55, announce:** "Two minutes. Make sure your Space is committed and building. If it's not running yet, that's fine — it'll build while we do the next demo."

---

### Block 4: Demo Build 2 — Quick Summarizer (0:57–1:17, 20 min)

**What you're building:** A summarizer that condenses long text into short summaries. The completed code is in `session-05/summarizer.py`.

**The narrative frame:** "We just built a generator that creates text from scratch — you give it a sentence, it writes more. Now we're building a different kind of generation. This model reads a whole article and rewrites it shorter. Both are generation — both produce new text. But one creates from nothing, and this one condenses."

#### 0:57–1:02 — Set Up the Contrast

"Here's the difference." Put this on screen or whiteboard:

| | Text Generator | Summarizer |
|---|---|---|
| **Input** | A short prompt | A long article |
| **Output** | More text (creating) | Less text (condensing) |
| **Model** | distilgpt2 | distilbart-cnn-12-6 |
| **Controls** | Temperature, top-p, max length | Max length, min length |
| **What it does** | Writes the next word, and the next, and the next | Reads everything, picks the key points |

"Both are generative models. Both have hyperparameters. But the controls are different because the job is different."

#### 1:02–1:12 — Build `app.py` on Screen

Create a new Space: "Quick Summarizer" (SDK: Gradio, Hardware: Free CPU).

**Write `requirements.txt`:** `transformers`, `torch`, `gradio`. Same as always.

**Build `app.py` step by step:**

**Step 1: Imports and model load.**

```python
import gradio as gr
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
)
```

"Third task type we've seen. Session 1: `sentiment-analysis`. Session 4: `text-generation`. Now: `summarization`. Same `pipeline()` function, different job."

**Step 2: The summarize function.**

```python
def summarize(text, max_length, min_length):
    if not text or not text.strip():
        return "Paste some text above to summarize!"

    word_count = len(text.split())
    if word_count < 30:
        return "The text is too short to summarize — try pasting something longer (at least a paragraph)."

    min_length = min(min_length, max_length - 10)
    if min_length < 10:
        min_length = 10

    result = summarizer(
        text[:1024],
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
    )

    summary = result[0]["summary_text"]
    summary_words = len(summary.split())

    return (
        f"{summary}\n\n"
        f"---\n"
        f"Original: {word_count} words → Summary: {summary_words} words "
        f"({summary_words / word_count:.0%} of original)"
    )
```

**Teaching moments to hit while typing:**
- `text[:1024]` — "The model can only handle about 1,024 characters at once. If you paste a whole book, it takes the first chunk. This is a real limitation."
- `min(min_length, max_length - 10)` — "What happens if someone sets min length HIGHER than max length? The model would crash. So we fix it in code. Defensive programming."
- `do_sample=False` — "No randomness here. The summarizer picks the single best summary. Different job, different settings."
- The word count display — "We show how much compression happened. Users like knowing 'my 200-word article became a 40-word summary.'"

**Step 3: Gradio interface with sliders.**

```python
demo = gr.Interface(
    fn=summarize,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste an article, essay, or long text here...",
                   label="Text to Summarize"),
        gr.Slider(minimum=30, maximum=200, value=100, step=10,
                  label="Max Summary Length (tokens)"),
        gr.Slider(minimum=10, maximum=100, value=25, step=5,
                  label="Min Summary Length (tokens)"),
    ],
    outputs=gr.Textbox(label="Summary", lines=6),
    title="Quick Summarizer",
    description="Paste a long article or essay and get a short summary. Use the sliders to control how long or short the summary is.",
)
demo.launch()
```

**Step 4: Add examples.** Include three that speak to different students:

1. **AI in healthcare** — general enough for everyone, but speaks to Chengry and George
2. **Medical case report** — directly relevant to Chengry's DxAI work and George's health interest
3. **Game lore (Zelda)** — speaks to Bobby and gives the room a fun example

"Notice these examples aren't random. A news article. A medical report. Game lore. Same model handles all three — but how well? That's worth testing."

#### 1:12–1:17 — Deploy and Test

Commit and deploy. While building, paste one of the example texts and demonstrate.

**Key demo moment:** Same article, two different settings:
- Max length 30, min length 10 — super compressed. "Just the headline."
- Max length 150, min length 50 — fuller summary. "The executive summary."

"Same article. Same model. The sliders control how much detail you keep."

**If the build fails or stalls:** Switch to pre-deployed backup. Keep moving.

---

### Block 5: Student Work 2 (1:17–1:42, 25 min)

**Instruction to students:** "You have 25 minutes. Your job is to have at least one working Space by the time we wrap up. If your Text Playground from earlier is running, great — build the Summarizer too, or customize what you have. If you don't have anything running yet, let's fix that now."

#### Student Work Priority Table — Block 5

| Student | What they should do | Instructor note |
|---------|---------------------|-----------------|
| Bobby | Build Summarizer with game lore examples, or keep customizing Text Playground | Self-sufficient — check in once |
| Annabelle | If Space still broken: **stop and fix it with instructor help.** If fixed: build Summarizer | If she's still stuck, pair-debug now — this is the priority window |
| Shawn | Build Summarizer, compare compression ratios at different settings | His comparison instinct fits perfectly here |
| Emily | **If Text Playground isn't running: debug it now.** If it is: try the Summarizer | **Do not leave her without a working Space** |
| Henry | **If Text Playground isn't running: debug it now.** If it is: try the Summarizer | **Do not leave him without a working Space** |
| Chengry | Build Summarizer with medical text examples. This is directly useful for his DxAI vision | Connect this to his project: "Imagine this as the front end of DxAI — paste symptoms, get a summary" |
| George | **If Text Playground isn't running: debug it now.** If it is: build Summarizer with health text | **Do not leave him without a working Space** |
| Sevilla | Build Summarizer with news article examples | Connects to her news/emotion work |

**Instructor movement pattern for this block:**

1. **First 5 minutes (1:17–1:22):** Check on Emily, Henry, George. If any of them don't have a running Space, sit with them and debug. This is the last work block — if they leave without a Space, the session failed for them.
2. **Minutes 5–15 (1:22–1:32):** Check Annabelle and Chengry. Fix broken Spaces or runtime errors. Then circulate to others.
3. **Last 10 minutes (1:32–1:42):** Float. Help anyone who's stuck. Encourage students who are done to test each other's Spaces.

**Common debugging scenarios:**

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Space says "Building" for 5+ minutes | Normal for first build with large model | Wait. The summarizer model is ~1.2GB and takes time to download |
| "ModuleNotFoundError" | Missing package in `requirements.txt` | Check that `transformers`, `torch`, and `gradio` are all listed, one per line |
| "RuntimeError: CUDA" or GPU errors | Code assumes GPU but Space is CPU-only | Make sure there's no `.cuda()` or `device="cuda"` in the code |
| Summarizer returns gibberish | Input too short | Needs at least 30 words. The code checks for this — make sure the check is in place |
| "Max length must be greater than min length" | Slider values conflict | The `min(min_length, max_length - 10)` guard should prevent this — check that it's in the code |
| Space runs but output is blank | Function returns `None` | Check indentation — the `return` statement might be outside the function |
| "Model not found" | Typo in model name | Copy the exact string: `sshleifer/distilbart-cnn-12-6` |

**At 1:40, announce:** "Two minutes. Commit anything you're working on. Make sure your Space is building."

---

### Block 6: Wrap-Up (1:42–1:52, 10 min)

#### 1:42–1:46 — Quick Student Shares (4 min)

"Who wants to show what they built? Drop your Space URL in the chat."

Pick 2–3 students to share. Prioritize:
1. A student who got their first working Space tonight (Emily, Henry, or George) — celebrate this
2. A student who customized in an interesting way (Bobby's game prompts, Sevilla's news focus)
3. Anyone who discovered something surprising

Keep each share to 60–90 seconds. "Show us your Space, run one example, tell us what you noticed."

#### 1:46–1:49 — Name the Concept: HYPERPARAMETERS (3 min)

**Now — and only now — name what they've been doing.**

"You've been turning sliders for the last hour. Let me name what those sliders are."

"Every slider you touched tonight is a **hyperparameter**. 'Hyper' means above or beyond. These are parameters that sit ABOVE the model. The model has millions of internal parameters — weights it learned during training. We can't change those. But hyperparameters are the knobs WE control."

**The guitar amp analogy:** "A guitar has fixed properties — the wood, the strings, the shape. Those are like the model's weights. But you control how hard you strum, where you pick, whether you use a capo, what settings you dial on the amp. Those are hyperparameters. Same guitar, different sound."

**The real-world connection (don't skip this):**

"Every AI tool you've ever used has these same controls. When you use ChatGPT, there's a temperature setting behind the scenes. When developers build with Claude's API, they set `temperature` and `top_p` on every single call. Most products hide the sliders from you — they pick settings they think work for most people. But the sliders are always there. Tonight you saw what's behind the curtain."

#### 1:49–1:50 — Research Lens: Parameter Sweep (1 min)

"One more thing. When you tested the same prompt at different temperature settings — changing one slider at a time and watching what happened — that has a name in research. It's called a **parameter sweep**. Systematically changing one variable while holding everything else constant. That's experimental design. Same method scientists use."

#### 1:50–1:52 — Bridge to Session 6

"So now we have generators with controls. Temperature, top-p, max length, min length — you can dial in exactly what you want. But here's the thing."

"The text generator was trained on web text. Reddit, news articles, Wikipedia. The summarizer was trained on CNN and Daily Mail articles. What happens when you ask them about something they've never seen?"

"What if you feed medical jargon to a model trained on Reddit posts? What if you paste legal text into a summarizer trained on news articles? That's the wall the field hit next — and the breakthrough that solved it is what made ChatGPT and Claude possible. That's next week."

---

### Buffer (1:52–2:00, 8 min)

Use this time for:
1. **Debugging** — Any student who still doesn't have a running Space gets help now
2. **Between-session challenge** — Share the between-session challenge (see BETWEEN-SESSION.md)
3. **Overflow** — If a student is close to finishing a second Space, let them push it over the line

**Hard check before anyone leaves:** "Show me your running Space." Every student should be able to pull up at least one working URL. If someone can't, note it for follow-up before Session 6.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Space build fails after committing | Check for syntax errors — missing closing parentheses, indentation issues. If stuck, paste the complete `app.py` from the session folder. "Same thing happens to professional developers. Check the error, fix the typo, rebuild." |
| Space takes too long to build | The summarizer model is ~1.2GB and can take 3–5 minutes on first build. Have your pre-deployed backup ready. "I built this earlier — same code. Let's use mine while yours catches up." |
| distilgpt2 generates gibberish | Normal for a small model. "This is what generation looks like at the smallest scale. Same controls work on GPT-4 — just better output." |
| Summarizer output is worse than expected | The model is small and was trained on news. Non-news text will get rougher summaries. Frame this: "We'll talk about why next week — it's called domain shift." |
| Student already covered temperature in Session 4 | Good — don't re-explain from scratch. "You already know what temperature does. Now you're controlling it with a slider instead of hardcoding it." |
| Students ask "but ChatGPT is way better" | "Exactly. Same controls, vastly different scale. You're learning the universal remote — these sliders work on every model, small or large." |
| Student's Space from previous session is broken | Debug it. Most common causes: typo in `requirements.txt`, wrong file name, missing import. Have the student compare their files line-by-line against the reference code. |
| Emily/Henry/George can't create a Space at all | Walk them through it: huggingface.co → New Space → Name it → SDK: Gradio → Hardware: Free CPU → Create. Then paste in the `app.py` and `requirements.txt`. Takes under 2 minutes. |
| Chengry's DxAI runtime error | Check the Logs tab in his Space. Most likely a missing dependency or a model that's too large for free CPU. If the model is too big, suggest swapping to a smaller one for now. |
| Annabelle's broken Spaces | Check each one: open the Space, click Logs. If it's a `requirements.txt` issue, fix and rebuild. If it's a code error, compare against reference. She may have multiple Spaces with different problems — pick the easiest to fix first. |
| Student wants to use a different model | Encourage it — but only after they have one working Space with the reference model. "Get this one running first. Then swap the model name and see what happens." |

---

## Hyperparameter Reference (Instructor Knowledge)

### Temperature
- Controls the randomness of token selection.
- Mathematically: divides the logits (raw scores) before softmax.
- Low temperature (0.1–0.3): Model almost always picks the highest-probability word. Output is repetitive and "safe."
- Medium temperature (0.5–0.8): Good balance. Most common for production use.
- High temperature (1.0–1.5): More random selections. Creative but less coherent.
- Very high (>1.5): Approaches uniform random selection. Often gibberish.

### Top-p (Nucleus Sampling)
- Instead of considering all possible next words, only consider the smallest set whose cumulative probability exceeds p.
- Top-p = 0.1: Only the very top words are considered (maybe 1–3 words).
- Top-p = 0.9: Most words are considered, excluding only the very unlikely ones.
- Top-p = 1.0: All words are considered (no filtering).
- Works in combination with temperature — both affect randomness but in different ways.

### Max Length
- Maximum number of tokens in the output (including the prompt for generators; just the summary for summarizers).
- Tokens are roughly words but not exactly (roughly 1 token = 0.75 words for English).
- Model may stop before max_length if it generates an end-of-sequence token.
- Longer isn't always better — generators can lose coherence, summarizers can pad with filler.

### Min Length (Summarizer only)
- Minimum number of tokens in the summary.
- Prevents the model from producing a one-sentence summary when you want a paragraph.
- Must be less than max_length (the code enforces this).
- Useful for controlling the level of detail: low min = headline, high min = executive summary.

---

## Concept Connections

- **Sessions 1–3 (Act I):** Classification — sorting into buckets. Students experienced the limits.
- **Session 4:** The fork. Classification vs. generation. Students built a bare text generator with no controls.
- **Session 5 (this session):** The controls on generation. Students add hyperparameter sliders to two different kinds of generative models. The real-world connection: these are the same controls on ChatGPT and Claude APIs.
- **Session 6 (next):** Domain shift — what happens when a model leaves its training world. The breakthrough: "train on everything."

---

## Key Vocabulary

- **Hyperparameter** — A setting that controls how a model behaves at runtime, as opposed to the model's internal weights (which were learned during training). Temperature, top-p, max length, and min length are all hyperparameters.
- **Temperature** — A hyperparameter that controls randomness in text generation. Low = predictable, high = creative/chaotic.
- **Top-p (nucleus sampling)** — A hyperparameter that controls which words the model considers. Low top-p = only the most likely words; high top-p = wider vocabulary.
- **Max length** — A hyperparameter that sets the maximum number of tokens the model can produce.
- **Min length** — A hyperparameter (for summarization) that sets the minimum number of tokens the summary must contain.
- **Parameter sweep** — A research method where you systematically change one variable at a time while holding everything else constant, to isolate the effect of each variable.
- **Summarization** — A type of generation that condenses long text into shorter text, preserving key information.
- **Token** — The unit of text a model processes. Roughly 1 token = 0.75 words in English, but varies by language and model.

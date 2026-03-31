# Between Sessions 5 & 6

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Experiment with Settings

In class we did a **parameter sweep** — systematically changing one variable while holding others constant. That's **experimental design** — the foundation of any controlled experiment.

Now apply that same method to **your own interest**.

### Option A: Stay with Text Generation

1. Duplicate the Text Playground Space to your own Hugging Face profile
2. Pick **2 or 3 different writing tasks** (scary story, formal email, poem, news report — or invent your own)
3. For each task, experiment with the sliders. Change **one slider at a time** and note what happens
4. Write down your "settings recipe card" for each task: what temperature, top-p, and max length worked best?
5. **Add the Space to your Collection** with a tasting note describing what settings work for what tasks

### Option B: Explore Your Own Topic

1. Find a model or Space from your Collection that has **adjustable settings** — sliders, dropdowns, parameter controls of any kind
2. If your topic doesn't have obvious sliders, look for models on the Hub that do (image generators have guidance scale, translation models have beam width, etc.)
3. Pick one setting and **sweep it** — try low, medium, and high values on the same input
4. Document what changes: does higher always mean better? Where's the sweet spot?
5. **Update your Collection** — add a tasting note describing the parameter and what it controls

The key idea is the same either way: **changing one variable at a time while holding everything else constant is how you learn what each control actually does.** You saw it with temperature tonight. Now try it with whatever settings your topic offers.

### What to Notice

- Does the same setting work for all tasks, or do different tasks need different settings?
- Is there a "sweet spot" where the output is both creative and coherent?
- What happens at the extremes (very low or very high)?

### Bring It Back

Next session, be ready to share: what setting did you experiment with, and what did you learn?

**Looking ahead:** We've seen what generation can do — and now we know how to control it. But our model was trained on web text. What happens when you feed it something from a world it's never seen? Next session, we'll discover what happens when a model leaves its comfort zone — and why that wall led to the biggest breakthrough in AI.

---

## Part 2: Research Journal Entry

Add your Week 5 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 5 Entry

```markdown
## Week 5 — Parameter Sweeps and Experimental Design

### This Week's Method
(What research method did we learn? Hint: parameter sweep — changing one variable at a time while holding others constant.)

### How I Applied It
(What model or Space did you experiment with? What setting did you sweep? What values did you try?)

### What I Expected
(Before testing — what did you think would happen as you changed the setting?)

### What I Found
(What actually happened? Was there a sweet spot? What happened at the extremes?)

### Why I Think This Happened
(Your explanation. Connect it to how the model works, what the parameter controls, etc.)

### Limitations
(What couldn't you test? Would a different model respond differently to the same parameter changes?)

### What I Want to Try Next
(Are you circling a topic? What question keeps coming up in your explorations?)
```

If you're not sure what to write, start with: describe what you changed, what stayed the same, and what surprised you. That's the core of experimental design.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **7 models and 5 Spaces** by Session 6. For new items, include tasting notes — especially note any adjustable settings you discovered.

### Notebook

Finish the experiments in the Session 5 notebook:
- Fill in the "settings recipe cards" table with your best settings for each task
- Try Experiment 2 (same settings, different prompts) and Experiment 3 (extreme settings)
- Write down any surprising results

### SpaceCraft Resource

This week you learned **Parameter Sweep** — changing one setting at a time while holding everything else constant. SpaceCraft has a dedicated page for this method with steps, examples on TTS Spaces, and an exercise: [Parameter Sweep method card](https://buildlittleworlds.github.io/spaceCraft/methods/parameter-sweep.html)

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 5 entry below the Week 4 entry, and commit

### Explorer Notebook (Optional)

Want to apply this week's method in code? Open the Explorer notebook — it lets you sweep temperature and top-p on a text generation model (or swap in your own), recording how output changes as you isolate one variable at a time. Your results can feed directly into your Research Journal entry.

[![Open Explorer in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-05/explorer.ipynb)

---

## Your Personal Challenge

The homework above applies to everyone. Below is a challenge tailored to **your** specific project and interests — a way to connect this week's method (parameter sweep / experimental design) to the work you're already building.

---

### Annabelle

Your annotations in your Model Collection — "works but I don't think it's very useful for me" vs. "very useful! basically on par with ChatGPT" — are already an informal parameter sweep. You evaluated models by changing one variable (the model) and comparing outputs. This week, make that process more deliberate.

**Your challenge:** Pick one of your broken spaces (Silly Phrase Finder or Dictionary). Before you debug it, open the Text Playground and try running prompts similar to what your space is supposed to generate — silly phrases, dictionary-style definitions — at different temperature and top-p settings. Write down which settings produce the kind of output your space is going for. Understanding the controls might help you see what went wrong in the build, and it gives you something concrete to write about in your journal. Your collection annotations already show you have the instincts for this kind of evaluative writing — now apply them to a controlled experiment.

---

### Bobby

Your journal entry testing Qwen3-Coder-WebDev already uses structured evaluation — you checked buttons, links, and dynamic content and rated it "Multi-Functional." That's a parameter sweep in spirit. This week, formalize it: one variable at a time, everything else held constant.

**Your challenge:** Go back to one of your generative AI tools — image generation, 3D models, or website generation — and see if it exposes parameter controls (guidance scale, inference steps, style strength, etc.). If it does, run a systematic sweep: same prompt, one setting changed at a time. Document it in your journal the way you documented the Qwen3-Coder testing. You noticed that HunYuan reinterpreted your "monster chicken" prompt into something else — that's partly about how the model's generation parameters handled an unusual input. These are the same kind of controls we explored tonight.

---

### Chengry

Your DxAI project uses the Claude API, which has its own set of parameters — temperature, max tokens, system prompts. Tonight's session makes those choices explicit. Every API call you've been making has these controls built in, whether you've been tuning them or not.

**Your challenge:** Once you get DxAI back online (debugging those dependencies is still priority one), experiment with the Claude API's temperature setting for diagnostic outputs. How do different temperature values change the quality and safety of medical AI responses? A low-temperature response might be more reliable but miss edge cases; a high-temperature response might surface more possibilities but include noise. Write a journal entry about that tradeoff. The intersection of parameter control and medical ethics is something most people in AI don't think about carefully enough — you're in a great position to.

---

### Emily

The spaces in your collection — news recommendation, summarization, deadline tracking — all have parameters under the hood that control how they filter and present information. Tonight's session gives you hands-on experience with those kinds of controls.

**Your challenge:** Duplicate the Text Playground on Hugging Face. Change the example prompts to topics you care about — news summaries, research descriptions, anything from the information management space you've been exploring. Even just swapping the prompts and experimenting with the sliders would give you something concrete to write about in your first journal entry. The Text Playground is simple — three sliders and a text box — but it shows you how small changes in settings completely change what a model produces. That's the same principle behind the recommendation and summarization tools in your collection.

---

### George

You jumped into building spaces fast — Trial and Dictionary both went up the same day, which shows great initiative. Tonight's session is about understanding the controls inside those tools.

**Your challenge:** Think about your medical AI interests. If you were building an injury prediction tool (like the one in your collection), would you want high temperature or low temperature? Write a short paragraph about why — consider that medical tools need to be reliable, not randomly creative. That paragraph could be the start of your GitHub journal, and it connects your interests directly to what we learned tonight. Then, if you have time, try the Text Playground with medical-style prompts ("The patient presents with...") and see how different temperature settings change the output. Is there a setting that feels right for medical text?

---

### Henry

The LoRA adapter you collected — Qwen Image Edit with multiple camera angles — is one of the most interesting technical choices in the class. LoRA adapters are literally about controlling parameters: they adjust a small set of weights to customize a large model's behavior without changing the model itself.

**Your challenge:** Go back to the Qwen Camera Angles space in your collection and see if it exposes any parameter controls (like guidance scale or inference steps). If it does, try a systematic sweep: same prompt, one setting changed. If it doesn't, write a short paragraph about what you think would change if you could control the "temperature" of an image generation model — would higher temperature give you wilder camera angles, or just noisier images? Either way, that's content for your GitHub repo. The connection between tonight's text generation controls and the LoRA adapter in your collection is direct: both are about adjusting how a model behaves without changing what it knows.

---

### Sevilla

Your comparative testing of emotion detection models — finding that BLIP-based models struggle with cartoonish images while color-based models are more reliable — is exactly the kind of systematic evaluation we formalized tonight. You isolated a variable (image style) and observed how different models responded. That's a parameter sweep.

**Your challenge:** Take one of the emotion detection tools from your Spaces on Emotions collection and see if it exposes any adjustable parameters — a sensitivity threshold, a confidence cutoff, a classification boundary. If it does, sweep it: same input, one parameter changed. If it doesn't, try the Text Playground with emotionally charged prompts at different temperatures. Does a high-temperature model produce more emotionally varied text? Does low temperature flatten emotional nuance? Write about it in your journal, building on your strong Week 2 entry. You already have the methodology — this week adds the formal vocabulary.

---

### Shawn

Your comparative analysis of Stable Diffusion v1.5, DALL-E Mini, and SDXL is already a parameter sweep in structure — you held the prompt constant and changed the model, then observed how outputs differed. Tonight we did the same thing but with finer-grained controls: keeping the model constant and changing its settings.

**Your challenge:** Go back to your collection of 12 image generation models and see which ones expose adjustable parameters (guidance scale, inference steps, CFG scale, sampler type). Pick one model and try a systematic sweep: same prompt, one setting changed at a time. Compare the results the way you compared SD, DALL-E Mini, and SDXL in your journal — but this time the variable is the setting, not the model. You mentioned wanting to explore prompt engineering optimization; hyperparameters are the other half of that equation. The same prompt with different settings produces very different outputs, and understanding that interaction is where prompt engineering gets interesting.

---

AI + Research Level 2 • Session 5: Add Controls

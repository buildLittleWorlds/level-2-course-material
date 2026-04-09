# Between Sessions 7 & 8

> **Heads-up:** This is also the week the course turns toward research work. Your main research work between sessions 7 and 8 is in [`WEEK-7-RESEARCH-WORK.md`](./WEEK-7-RESEARCH-WORK.md). Read that first. The build and journal steps below support that research work.

**Tonight you found bias** — you designed paired tests, changed one variable, and watched the model treat different groups differently. That's baked into the training data, and it's worth knowing about for any model you use. For some of you, the bias you found tonight is directly relevant to what you're building, and this week's research work is going to make that connection load-bearing.

Prea's [Week 7 journal entry ("Bias, and Starting Space 2")](../example-student-prea/research-journal.md) is the clearest example in the course of a student taking a class topic and realizing it isn't a side reflection — it's a limitation her project has to name honestly. Her pipeline runs on Whisper, and Whisper is an ASR system, and ASR systems have documented performance disparities across speaker groups. Her team includes native English speakers and students for whom English is a second or third language. If Whisper transcribes non-native speakers less accurately, every downstream prosodic feature she computes is less reliable for some speakers than for others. She runs two Consensus searches, finds Koenecke et al. (2020) in PNAS and Li et al. (2024) on arXiv (the second one specifically about Whisper), and writes the honest limitations language her eventual brief needs. That's the move: *tonight's class topic is my project's limitations section.*

This week: start building Space 2, and do the Week 7 research work.

---

## Build Step: Start Your Domain Space (30 min)

It's time to build something better than Space 1. Your Space 2 should do something different — a different model, a different pipeline type, or a domain-specific feature. It should connect to the interest you've been developing since Session 5.

**How to build it:**

1. Open your student folder on the course repo. Pick the prompt that matches what you want to build.
2. Paste that prompt into a coding AI (ChatGPT, Claude, Gemini). It will give you `app.py` and `requirements.txt`.
3. Create a new Space on Hugging Face. Upload the files. Wait for the build.
4. If it works: customize the title, description, and examples. If it doesn't: paste the error back into the coding AI and ask it to fix the code.

Get Space 2 deployed this week, even if it's rough. You'll improve it after Session 8.

**If you're not sure what to build:** Use one of the upgrade prompts from your student folder. The simplest version is to take your Space 1 and swap in a better model (SmolLM2-360M-Instruct or Qwen2.5-0.5B-Instruct). That alone will show you how much model choice matters.

---

## Journal Entry (15 min)

Open `research-journal.md` and add your Week 7 entry:

```markdown
## Week 7 — Building Space 2

### What We Talked About in Class
(Quick note on the bias testing we did — what stuck with you? Will it be relevant to your project?)

### What I'm Building for Space 2
(What's your Space 2? What model or pipeline are you using? How is it different from Space 1? Why did you choose this direction?)

### How It's Going
(Did you get it deployed? What worked? What broke? What do you still need to figure out?)
```

**Not sure what to write?** Read [Prea's Week 7 journal entry](../example-student-prea/research-journal.md). Notice how she treats the class bias topic not as a side note but as a direct threat to her project, names the specific papers she found, and drafts the actual limitations sentence she will use in her eventual brief. Your entry should capture the same things: what you're building, what you're learning, and — if tonight's bias discussion is relevant to your project — the honest limitations language your project needs.

---

## Portfolio Check

By Session 8, you should have:
- Space 1 running on Hugging Face
- Space 2 deployed (even if rough)
- 3 journal entries in `research-journal.md`
- A Hugging Face Collection with 7+ items

**Reference:** Prea's Space 2 (the Delivery Analyzer) is described in her [portfolio README](../example-student-prea/README.md). Notice how it's built on a completely different model type than her Space 1 — Whisper audio transcription instead of sentiment classification — and how the feature extraction work happens in pure Python on top of the API response. That jump is the point. Your Space 2 should represent a real step forward from your baseline.

---

## Your Personal Challenge

### Annabelle
You build fast. Use that speed on Space 2 — pick one prompt from your folder, build it, and get it deployed. Then write about the difference between Space 1 and Space 2 in your journal. What changed? What's better?

### Bobby
Your folder has a model comparison lab prompt. That's a natural Space 2 — same game writing prompts, but now you can switch between distilgpt2, SmolLM2, and Qwen. Build it this week and write about what you notice when you compare the outputs.

### Chengry
If the biomedical NER Space is working, that's your Space 2. If not, try the simpler upgrade: take your text generator and swap to a better model. Focus on getting something deployed — you can refine it after Session 8.

### Emily
Your folder has a news model comparison lab and a better summarizer. Pick one for Space 2. Either direction works well — go with whichever one excites you more, and get it deployed this week.

### George
Build Space 2 around health text. Your simplest path: upgrade the model in your text generator and test it on medical content. Get it deployed and write about what the better model does differently.

### Henry
Your folder has a scene description Space prompt. That's a great Space 2 direction — it connects your visual interests to text generation. Build it this week and see what it can do.

### Sevilla
You've been exploring emotion and image models. Pick a direction for Space 2 that goes deeper into one of those interests. Your folder has prompts to help — pick the one that feels most like *your* project and build it.

### Shawn
A model comparison lab is your ideal Space 2. Build the comparison version from your folder — your systematic methodology will shine when you can compare models side by side. Get it deployed and start testing.

---

AI + Research Level 2 • Session 7: Building Space 2

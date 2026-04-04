# Between Sessions 7 & 8

**Tonight you found bias** — you designed paired tests, changed one variable, and watched the model treat different groups differently. That's baked into the training data, and it's worth knowing about for any model you use. Keep it in your back pocket. If it's relevant to what you're building, use it. If not, that's fine — what matters most this week is building.

Riley built Space 2 this week too — a bird song classifier that identifies species from audio recordings. It was a completely different kind of model from Space 1 (audio classification instead of text generation). Riley's Week 7 journal entry in [`example-student/research-journal.md`](../example-student/research-journal.md) documents the build process and a big surprise: the model only knows tropical birds, not backyard birds. The architecture worked perfectly — but the training data didn't match Riley's needs. Your Space 2 will have its own version of that discovery.

This week: start building Space 2. Plan for about 1 hour.

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

**Not sure what to write?** Read Riley's Week 7 journal entry in [`example-student/research-journal.md`](../example-student/research-journal.md). Riley describes choosing a bird audio classification model, modifying the prompt from the student folder, and discovering a major training data limitation. Your entry should capture the same things: what you're building, why, and what you're learning as you build.

---

## Portfolio Check

By Session 8, you should have:
- Space 1 running on Hugging Face
- Space 2 deployed (even if rough)
- 3 journal entries in `research-journal.md`
- A Hugging Face Collection with 7+ items

**Reference:** Riley's Space 2 (the bird song classifier) is described in [`example-student/README.md`](../example-student/README.md). Notice how it's a completely different model type from Space 1 — that jump is the point. Your Space 2 should represent a real step forward from your baseline.

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

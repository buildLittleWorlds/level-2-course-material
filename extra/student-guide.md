# Can AI Prove Theorems?

## Exploring QED-Nano — A Tiny Model That Reasons About Mathematics

---

### What You Already Know

In this course, you've built Spaces that classify text, analyze sentiment, detect bias, and chain models together. Every model you've used was trained to do a specific job: label text, generate sentences, describe images.

But here's a question: can an AI model do something harder than pattern recognition? Can it *reason*?

---

### What Is a Mathematical Proof?

A proof is an argument — the most rigorous kind of argument there is. When a mathematician proves a theorem, they start with things everyone agrees are true (axioms, definitions, previously proven results) and build a chain of logical steps that ends at a conclusion nobody can deny.

Here's what makes proofs different from other arguments:

- **Every step must follow logically from previous steps.** No appeals to emotion, authority, or popularity. Just logic.
- **The conclusion must be airtight.** Not "probably true" or "true in most cases" — *always* true, in every possible scenario.
- **Gaps are fatal.** If you skip a step that isn't obvious, the proof doesn't hold.

This is why proving theorems is one of the hardest things to do well. And it's why teaching an AI to do it is a serious challenge.

---

### Meet QED-Nano

In February 2026, a team from CMU, Hugging Face, ETH Zurich, and Numina published a remarkable result: they trained a model with only **4 billion parameters** — tiny by today's standards — to write proofs for problems from the International Mathematical Olympiad and similar competitions.

To put that in perspective:

| Model | Parameters | Proof-Writing Score |
|-------|-----------|-------------------|
| Qwen3-4B-Thinking | 4B | 20% |
| **QED-Nano** | **4B** | **40%** |
| **QED-Nano (with agent scaffold)** | **4B** | **54%** |
| GPT-OSS-120B | 120B | 43% |
| DeepSeek-Math-V2 | 685B | 58% |
| Gemini 3 Pro | Unknown (huge) | 59% |

QED-Nano, at 4 billion parameters, approaches the performance of models that are 30x to 150x larger. The researchers achieved this through a three-stage training recipe:

1. **Supervised fine-tuning:** Learn what proofs look like from high-quality examples
2. **Reinforcement learning with rubric grading:** Practice writing proofs and get scored on a detailed rubric (not just right/wrong)
3. **Reasoning cache:** Learn to break long proofs into cycles of "summarize what I've figured out so far, then keep going"

---

### Your Task: Be the Judge

Dr. Plate built a Hugging Face Space called **Proof Explorer** that lets you feed math problems to QED-Nano and read its proof attempts. Your job is to evaluate those proofs — not as a mathematician, but as a critical thinker.

**Go to the Space:** [Link will be added once deployed]

#### Activity: Try These Three Problems

**Problem 1 (Accessible):** Select "Divisibility (Accessible)" from the dropdown.
> "Prove that for every positive integer n, the number n³ - n is divisible by 6."

Read the proof attempt. You probably know enough algebra to follow this one. Ask yourself:
- Does each step make sense?
- Does the proof actually show divisibility by 6, or does it stop short?

**Problem 2 (Moderate):** Select "Inequality (Moderate)" from the dropdown.
> "Let a, b, c be positive real numbers. Prove that (a+b)(b+c)(c+a) ≥ 8abc."

This uses a classic technique called AM-GM (arithmetic mean is always ≥ geometric mean). Even if you don't know that technique, you can still evaluate:
- Does the proof state its assumptions clearly?
- Does it apply one method consistently, or does it jump around?
- Does it reach a definitive conclusion?

**Problem 3 (Hard):** Select "Irrationality (Hard — Olympiad)" from the dropdown.
> "Prove that √2 is irrational."

This is a famous proof that uses "proof by contradiction." The model should assume √2 is rational and derive a contradiction. Check:
- Does it set up the contradiction correctly?
- Is the chain of reasoning complete, or are there jumps?
- Does it actually arrive at a contradiction?

#### Reflection Questions

After trying all three, write brief answers to these questions:

1. **Did any of the proofs convince you?** Which one felt most like a solid argument, and why?

2. **Where did the model struggle?** Did you notice repeated patterns in how it makes mistakes (if it does)?

3. **How is evaluating a proof different from evaluating sentiment analysis?** In Sessions 4-6, you compared models on whether they correctly classified text. How is judging a proof different?

4. **Is the model "reasoning" or "pattern matching"?** QED-Nano was trained on thousands of proofs. When it writes a new one, is it genuinely reasoning through the logic, or assembling patterns it saw in training? How would you tell the difference?

5. **What would you need to know to build a Space like this?** Think about the skills from this course. What's the same as what you've done? What's new?

---

### Why This Matters Beyond Math

You might be thinking: "I'm not a mathematician. Why do I care about proofs?"

Here's why: the skills you use to evaluate a proof are the same skills you need to evaluate *any* argument.

- A debate opponent makes a claim → Does each step of their reasoning follow?
- A news article draws a conclusion → Are there gaps in the logic?
- An AI assistant gives you an answer → How do you know it's right?

Mathematical proof is where these skills are sharpest and clearest, because there's no ambiguity. Either the logic holds or it doesn't. Practicing on proofs makes you better at spotting weak arguments everywhere else.

And if AI models can now attempt proofs — even imperfectly — then understanding how to evaluate AI reasoning is a skill that will only become more important.

---

### Going Further (Optional)

If this interests you, here are some directions to explore:

- **Read the QED-Nano blog post** on Hugging Face: it explains the training recipe in detail
- **Try writing your own math problem** and feeding it to the model. Can you find a problem that stumps it?
- **Compare QED-Nano's output to ChatGPT or Claude** on the same problem. How do they differ?
- **Think about how you would build a Space that grades proofs** — not just generates them. What would the rubric look like? (This is actually what the QED-Nano researchers had to solve for training.)

---

*This material is part of the AI + Research Level 2 course, Youth Horizons Learning.*
*Space and guide by Dr. Daniel Plate.*

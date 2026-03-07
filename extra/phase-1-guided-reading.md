# Phase 1: Reading a Research Paper with AI

## How to Use This Guide

You are about to read a real research paper — the kind that professional AI researchers publish. It is 20 pages long, full of technical language, and includes charts, tables, and equations. That might sound intimidating. It isn't, if you have the right approach.

Your approach: **use an AI assistant as a reading partner.** Open this guide alongside the paper and a conversation with Claude, ChatGPT, or any AI assistant you have access to. You will read short sections of the paper, then ask the AI to help you understand what you just read. The prompts below tell you exactly what to ask.

This is a skill that transfers far beyond this module. Learning to decode dense writing with AI assistance is something you will use in college, in professional settings, and whenever you encounter material that's above your current level but within your reach if you have help.

**The paper:** *QED-Nano: Teaching a Tiny Model to Prove Hard Theorems*
**Authors:** LM Provers Team (CMU, Hugging Face, ETH Zurich, Numina)
**Published:** February 15, 2026

---

## Section 1: The Abstract (Page 1)

**Read** the first paragraph of the paper — the one that starts with "Can we train small language models..."

This is the **abstract**: a summary of the entire paper in one paragraph. Every research paper starts with one. If you can understand the abstract, you have the big picture.

### Ask Your AI Reading Partner

Copy the abstract into your AI conversation and try these prompts:

> "I'm a high school student reading a research paper about AI. Here's the abstract. Can you explain what the researchers are claiming in plain language?"

> "What are the three stages of their 'recipe'? Explain each one in a sentence I can understand."

> "What does 'agentic scaffolds' mean in this context?"

> "The abstract says the model 'approaches the proof-writing performance of much larger models.' Why is that surprising or important?"

### What You Should Understand Before Moving On

After this section, you should be able to answer:

- What did the researchers build? *(A small model that writes mathematical proofs)*
- Why is it impressive? *(It's much smaller than competing models but performs almost as well)*
- What are the three stages of their training method? *(Supervised learning, reinforcement learning with rubrics, reasoning cache)*

---

## Section 2: The Big Picture (Pages 2–3)

**Read** the section titled "Introducing QED-Nano: a 4B Model for Olympiad-Level Proofs."

This section explains *why* this research matters. Pay attention to the gap the researchers identify: big companies have built powerful AI systems, but they don't share how. This team built something smaller and released everything publicly.

### Ask Your AI Reading Partner

> "The paper talks about a 'gap between what is possible in principle and what the wider community can realistically build.' What does that mean? Why does it matter that this team released their work publicly?"

> "The paper says their model 'operates entirely in natural language, with no reliance on Lean or external tools.' What does that mean? What is Lean?"

> "What is the International Mathematical Olympiad (IMO)? How hard are the problems?"

### What You Should Understand Before Moving On

- Why the researchers built QED-Nano (to close the gap between closed and open AI systems)
- That the model writes proofs in regular language, not in a specialized programming language
- That IMO problems are among the hardest math competition problems in the world

---

## Section 3: The Results Table (Page 3)

**Look at Table 1.** This is one of the most important parts of the paper. It compares QED-Nano to other models on three benchmarks.

### Ask Your AI Reading Partner

Copy the table or describe it, then ask:

> "Here's a table comparing AI models on math proof benchmarks. QED-Nano has 4 billion parameters. Qwen3-235B has 235 billion parameters. QED-Nano scores 40.0 on IMO-ProofBench; Qwen3-235B scores 34.1. What does that tell us?"

> "What does the number in parentheses after each score mean? For example, '40.0 (0.6)' — what is the 0.6?"

> "QED-Nano (Agent) scores much higher than regular QED-Nano. What is the 'Agent' version doing differently?"

> "Which models beat QED-Nano? How much bigger are they?"

### What You Should Understand Before Moving On

- QED-Nano (4B parameters) outperforms many models that are 10x–60x larger
- The "Agent" version, which gives the model more time to think, pushes performance even higher
- Only the very largest models (DeepSeek-Math-V2 at 685B, Gemini 3 Pro) clearly beat it

---

## Section 4: How They Trained It (Pages 5–8)

This is the most technical part of the paper. You do not need to understand every detail. Focus on the **big ideas** behind each training stage.

### Stage 1: Supervised Fine-Tuning (SFT)

**Skim** the section on SFT. The key idea: they collected high-quality examples of mathematical proofs and showed them to the model, so it learned what proofs look like.

> "The paper says they used 'distillation from DeepSeek-Math-V2' to create training data. What does distillation mean here? They used a bigger model to generate example proofs for the smaller model to learn from — is that right?"

> "Why did they need to filter out problems with diagrams or that were 'trivially short'? What does data quality mean in this context?"

### Stage 2: Reinforcement Learning with Rubric Grading

**Read** the section on grading rubrics carefully — this is one of the paper's most interesting ideas.

> "The paper says they don't just grade proofs as right or wrong. They use a rubric. What criteria does the rubric include?"

> "Why would rubric-based grading be better than just checking if the final answer is correct? Think about it like grading a student's essay versus just checking if they got the 'right' thesis."

> "The paper calls this 'dense rewards.' What does that mean compared to 'sparse rewards'?"

### Stage 3: Reasoning Cache

**Skim** the section on the reasoning cache. The key idea: for very long proofs, the model learns to pause, summarize what it has figured out so far, and then continue.

> "The paper describes 'Think-Summarize-Act' cycles. Can you explain this like I'm a student? The model is writing a long proof and it periodically stops to summarize its progress before continuing?"

> "Why would this help? What problem does it solve?"

### What You Should Understand Before Moving On

- **Stage 1:** The model learned what proofs look like by studying examples from a bigger model
- **Stage 2:** Instead of just pass/fail grading, the model got feedback on *specific aspects* of its proofs (like a rubric for an essay)
- **Stage 3:** For long proofs, the model learned to pause and summarize before continuing (like taking notes while solving a hard problem)

---

## Section 5: The Broader Implications (Page 4)

**Read** the "Broader implications" paragraph. This is where the researchers explain why their work matters beyond just math proofs.

> "The paper says 'task-specialized small models trained for test-time adaptation can match or exceed much larger generalist systems.' What does that mean in plain language?"

> "They say their recipe is 'generalizable and can also be applied to other domains that allow for rubric-based rewards.' What other domains could this work for? What kinds of tasks have rubric-based evaluation?"

### What You Should Understand Before Moving On

- The paper isn't just about math — it's about a general principle: small, specialized models can compete with huge general-purpose ones
- The training approach could work for any task where you can define clear evaluation criteria

---

## Wrap-Up: Write Your Own Summary

Now that you've read the key sections with AI help, write a summary **in your own words**. Aim for 4–6 sentences. Cover:

1. What the researchers built
2. How they trained it (the three stages, in simple terms)
3. Why the results are impressive
4. Why this matters beyond math

**Do not ask the AI to write this for you.** The point is to check whether *you* understand the paper. You can ask the AI to check your summary afterward: "Here's my summary of the QED-Nano paper. Did I get anything wrong?"

---

## Bonus: Questions to Bring to Class

If your instructor is discussing this paper in a session, here are good questions to raise:

- "The model was trained on proofs from a bigger model. Is that like a student learning from a textbook, or is it more like copying?"
- "The rubric grades proofs on things like logical structure and completeness. Who decides what the rubric should be? Could a different rubric give different results?"
- "The model gets better when given more time to think (the Agent version). Is that similar to how humans do better on tests with no time limit?"

---

*Phase 1 of the "From Paper to Project" module — AI + Research Level 2, Youth Horizons Learning*

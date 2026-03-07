# Phase 2: Exploring the Research Artifacts on Hugging Face

## What You're Doing and Why

In Phase 1, you read the QED-Nano paper with AI assistance. Now you are going to look at the actual artifacts the researchers released — the model, the training data, and the base model it was built from. All of these are publicly available on the Hugging Face Hub, the same platform where you've been building Spaces all semester.

This matters because research papers describe what was done; the Hub shows you the evidence. You can look at the actual data the model was trained on. You can read the model card the researchers wrote. You can compare QED-Nano to the model it started as before training. This is the difference between reading about an experiment and examining the lab notebook.

---

## Activity 1: Read the QED-Nano Model Card

**Go to:** [huggingface.co/lm-provers/QED-Nano](https://huggingface.co/lm-provers/QED-Nano)

You've read model cards before in Sessions 2 and 3. This one is for a research model, so it has more technical detail than the ones you've seen. Read through it and answer the following:

### Questions

1. **What is the base model?** QED-Nano was built on top of an existing model. What was it? Write down the name and its parameter count.

2. **What task is it designed for?** In your own words, what does this model do?

3. **What license does it use?** Look for the license field. Is this model open for anyone to use? Could you build something with it?

4. **What datasets are mentioned?** The model card should reference the training data. Write down the dataset names.

5. **Compare this model card to one from earlier in the course** (like the sentiment model from Session 2). What's similar? What's different? Research model cards tend to be more detailed — why do you think that is?

---

## Activity 2: Browse the Training Data

**Go to:** [huggingface.co/datasets/lm-provers/FineProofs-RL](https://huggingface.co/datasets/lm-provers/FineProofs-RL)

This is one of the datasets used to train QED-Nano during the reinforcement learning stage. Click the "Dataset Viewer" tab to browse actual rows of data.

### What to Look For

Each row in this dataset is a math problem that was used to train the model. Browse through several rows and pay attention to:

- **The problem statements.** How are they written? Are they like the problems you see in a math textbook, or are they different?
- **The difficulty.** Can you understand any of the problems? Some will be accessible; others will be well beyond high school math. That's expected.
- **The format.** How is each entry structured? What fields does each row have?

### Questions

1. **Pick one problem you can understand** (even partially). Write it down. What mathematical concept does it involve?

2. **Pick one problem that is completely beyond you.** Write it down. What makes it hard? Can you identify the general topic even if you can't solve it?

3. **How many rows are in the dataset?** Look at the dataset statistics. Is this a lot of training data? The paper mentions they carefully filtered for quality rather than quantity. Why might fewer, better examples work better than many mediocre ones?

4. **Now go to:** [huggingface.co/datasets/lm-provers/FineProofs-SFT](https://huggingface.co/datasets/lm-provers/FineProofs-SFT)

   This is the dataset used for Stage 1 (supervised fine-tuning). Browse a few rows. **How is this dataset different from the RL dataset?** The SFT dataset includes complete proof solutions because the model is learning *what proofs look like*. The RL dataset is for *practicing and getting feedback*.

---

## Activity 3: Compare the Before and After

The researchers didn't build QED-Nano from scratch. They started with an existing model called Qwen3-4B-Thinking and trained it further. Both models are on the Hub.

**Base model:** [huggingface.co/Qwen/Qwen3-4B-Thinking](https://huggingface.co/Qwen/Qwen3-4B-Thinking)
**Trained model:** [huggingface.co/lm-provers/QED-Nano](https://huggingface.co/lm-provers/QED-Nano)

### Questions

1. **Read both model cards.** The base model (Qwen3-4B-Thinking) is a general-purpose model — it can do many things. QED-Nano is specialized. What did the researchers gain by specializing? What did they give up?

2. **Look at the parameter counts.** Both models have the same number of parameters (4 billion). The training didn't make the model bigger — it changed what the model *knows*. In your own words, what does fine-tuning do if it doesn't add more parameters?

3. **Think back to the results table from Phase 1.** The base model (Qwen3-4B-Thinking) scored 20.4% on IMO-ProofBench. QED-Nano scored 40.0%. Same size model, double the performance. What does that tell you about the importance of training data and training method versus raw model size?

---

## Activity 4: Find the Blog Post Space

**Go to:** [huggingface.co/spaces/lm-provers/qed-nano-blogpost](https://huggingface.co/spaces/lm-provers/qed-nano-blogpost)

The researchers built their own Hugging Face Space to present their findings. This is the same thing you've been doing all semester — building Spaces to share work with an audience.

### Questions

1. **How did they design their Space?** Look at the layout, the navigation, the way information is organized. What choices did they make about what to show first?

2. **Compare their Space to the ones you've built.** What's more sophisticated? What design principles from Session 9 (designing for an audience) can you identify in their work?

3. **Could you build something like this?** Seriously — look at the structure. A Gradio app with text, charts, and interactive elements. You've been building Spaces with those components since Session 5. What's the same? What would be new for you?

---

## Wrap-Up: What You Learned from the Hub

Write brief answers (2-3 sentences each) to these reflection questions:

1. **What surprised you** about looking at the actual training data? Was it what you expected?

2. **What did you learn from comparing the base model to QED-Nano** that you wouldn't have learned just from reading the paper?

3. **Why does it matter that the researchers released everything publicly?** Think about what you were able to do in this activity because the data, model, and code are open. What would be different if they had kept it private?

---

*Phase 2 of the "From Paper to Project" module — AI + Research Level 2, Youth Horizons Learning*

# Roots: Can Machines Understand Feelings? — Course Overview

## The Big Idea

This course teaches you how AI works by having you **build things with it**.

Not by memorizing definitions. Not by watching lectures about neural networks. Not by reading about what other people have built. You'll learn by building your own AI-powered tools — from scratch, session by session — and by watching what happens when you change things, break things, and try things nobody expected.

By the end of this course, you'll have a portfolio of working AI applications on your Hugging Face profile that anyone in the world can use. You'll understand the core concepts behind machine learning — not because someone told you about them, but because you ran into them while building.

## Why Building Is the Best Way to Learn

There's a version of an AI course that starts with theory: "First, let's define what a neural network is. Now let's look at this diagram of weights and biases. Now let's talk about gradient descent." That approach works for some people in some contexts. But for most of us, it puts the cart before the horse. You're memorizing answers to questions you haven't asked yet.

This course flips that. We start with a working thing — a Space that does something interesting — and then we ask: how does it work? What happens if we change this? Why did the model get that wrong? The concepts emerge from the building, not the other way around.

Here's an example. In Session 1, you'll experiment with a simple AI app called a **Mood Meter**. You paste in a sentence — something you might write in a journal, text to a friend, or say out loud — and the app tells you whether it reads as positive or negative, with a confidence score. Students try happy sentences, sad ones, angry ones, and ambiguous ones. The gap between what the model thinks and what you actually feel is where the learning starts.

But look at what's actually happening under the hood. You're using **sentiment analysis** — a technique where an AI model reads text and classifies its emotional tone. That's a real, powerful technique used in industry for things like customer feedback analysis, social media monitoring, brand reputation tracking, and mental health research tools. The Mood Meter and a professional customer insights platform use the exact same underlying technology. The difference is just the interface you wrap around it.

That pattern repeats throughout the course. Every project teaches a genuine ML concept through something you can actually build, test, and play with.

## The Story This Course Tells

The course isn't just a sequence of lessons — it's a story with a beginning, a middle, and a turn that changes how you think about what AI can do.

### Act I: The Old Way (Sessions 1–3)

You start by exploring AI tools that **classify** — they read text and sort it into categories like "positive" or "sad" or "angry." In Session 1, you'll tour AI-powered Spaces, test a Mood Meter, and start gathering evidence about whether a model can really read feelings. In Session 2, you'll swap in different models and discover that the same text gets completely different emotion readings depending on what training data the model learned from. You'll leave Session 2 wondering: if 7 emotion categories miss things, would 28 be enough? Would 100?

Session 3 answers that question — and the answer isn't what you expect. You'll try to break models with sarcasm, mixed feelings, and text that has no human characters at all. You'll discover that no amount of labels fixes the fundamental problem. Classification has a ceiling. That's the wall.

The emotional arc of Act I: **curiosity → hope → wall.**

### Act II: The Breakthrough (Sessions 4–8)

Session 4 is the turn. You'll see what happened when researchers stopped asking "which bucket does this belong in?" and started asking "what comes next?" That single shift — from classification to generation, from sorting to creating — is the biggest idea in modern AI. A model that predicts the next word can write essays, answer questions, translate languages, and do things nobody explicitly trained it to do.

From there, the course opens up. In Session 5, you'll build a text playground with sliders that control how creative or predictable the model is — and discover that "creativity" might just be controlled randomness. In Session 6, you'll take models trained on one kind of text and test them on something completely different, watching them fail in revealing ways. Session 7 is where you ask: if these models learned from human data, did they also learn human biases? (The answer is yes, and you'll build a tool to prove it.) Session 8 chains two models together — one that sees images and one that reads text — and you'll watch what happens when the first model makes a mistake and everything downstream breaks.

The emotional arc of Act II: **breakthrough → power → cost.**

### Act III: Building (Sessions 9–12)

Now you build your own. In Session 9, you'll learn that the same model becomes a completely different tool depending on who you design it for — a restaurant owner, a student, a social media manager. Session 10 is where you choose your own model from Hugging Face and build a Space from scratch. Session 11 is peer testing and iteration — the same loop that professional product teams use. And Session 12 is Demo Day: you present not just your Space, but the entire research journey that got you there.

The emotional arc of Act III: **agency → craft → ownership.**

## What You'll Actually Be Able to Do

By the end of this course, you'll be able to:

- Load and use pre-trained AI models for sentiment analysis, emotion detection, text generation, image captioning, and more — and know how to find models for tasks we never covered in class
- Build and deploy web applications powered by AI that anyone can access
- Read a model card and understand what a model was trained on, what it's good at, and where it might fail
- Compare models, test them across domains, and evaluate their performance on different kinds of data
- Identify bias in AI systems and articulate why it matters
- Chain models together into pipelines and understand how errors propagate
- Design AI tools for specific audiences — not just "does it work?" but "does it work for this person?"
- Write and run Python code in notebooks, experiment with parameters, and interpret the results
- Use GitHub to manage and share your projects
- Explain core ML concepts — classification, generation, training data, hyperparameters, domain shift, bias, pipelines, user-centered design — in your own words, because you've seen them in action

These aren't just academic skills. They're the same skills that data scientists, ML engineers, and AI researchers use every day. The difference is that you're learning them now instead of at the end of years of computer science coursework.

## The Tools

You'll use four platforms throughout the course. Each one plays a specific role in the story:

**Hugging Face** is your home base — where you find models, build Spaces, and curate your Collection. Your Collection starts as a list of interesting things you've found and gradually becomes a research portfolio that documents your journey from Act I to Act III.

**Google Colab** is your lab notebook — where you run experiments, test hypotheses, and gather evidence. Every session has a companion notebook where you push models further than the slides go.

**Gradio** is your interface builder — the Python library that turns a function into a web app. In Act I, Gradio wraps classification models. In Act II, it wraps generation models. By Act III, you're designing Gradio interfaces for specific audiences.

**GitHub** is your portfolio and archive — where your code lives, your progress accumulates, and your work becomes visible to the world.

Each tool has its own Start Here guide with more detail. You don't need to master any of them before Session 1 — you'll pick them up as you go.

## What You Don't Need to Know Coming In

You don't need to know Python. You'll pick up what you need as we go, and the notebooks are designed so you can experiment even if the code isn't fully clear to you yet.

You don't need to know anything about AI or machine learning. That's what the course is for.

You don't need to be "good at math" or "good at computers." You need to be curious and willing to try things. The models do the heavy mathematical lifting. Your job is to choose the right model, give it the right input, and figure out what to do with the output.

You do need a computer with a web browser and an internet connection. That's it. Every tool we use is free and runs in the cloud.

## Why This Matters

AI is changing how the world works. That's not hype — it's already happening in medicine, law, journalism, science, art, education, and dozens of other fields. The question isn't whether you'll interact with AI in your future career. The question is whether you'll be someone who understands it well enough to use it thoughtfully, critically, and creatively — or whether you'll just be along for the ride.

This course puts you in the first group. Not by lecturing you about the future, but by handing you the tools and saying: build something. See how it works. Break it. Fix it. Make it better. That's how real understanding happens.

Let's get started.

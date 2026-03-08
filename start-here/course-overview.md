# Roots: Can Machines Understand Feelings? — Course Overview

## The Big Idea

This course teaches you how AI works by having you **build things with it**.

Not by memorizing definitions. Not by watching lectures about neural networks. Not by reading about what other people have built. You'll learn by building your own AI-powered tools — from scratch, session by session — and by watching what happens when you change things, break things, and try things nobody expected.

By the end of this course, you'll have a portfolio of working AI applications on your Hugging Face profile that anyone in the world can use. You'll understand the core concepts behind machine learning — not because someone told you about them, but because you ran into them while building.

## Why Building Is the Best Way to Learn

There's a version of an AI course that starts with theory: "First, let's define what a neural network is. Now let's look at this diagram of weights and biases. Now let's talk about gradient descent." That approach works for some people in some contexts. But for most of us, it puts the cart before the horse. You're memorizing answers to questions you haven't asked yet.

This course flips that. We start with a working thing — a Space that does something interesting — and then we ask: how does it work? What happens if we change this? Why did the model get that wrong? The concepts emerge from the building, not the other way around.

Here's an example. In Session 1, we will experiment with a simple AI app, a **Mood Meter**. You paste in a sentence — something you might write in a journal, text to a friend, or say out loud — and the app tells you whether it reads as positive or negative, with a confidence score. Students try happy sentences, sad ones, angry ones, and ambiguous ones. The gap between what the model thinks and what you actually feel is where the learning starts.

But look at what's actually happening under the hood. You're using **sentiment analysis** — a technique where an AI model reads text and classifies its emotional tone. That's a real, powerful technique used in industry for things like customer feedback analysis, social media monitoring, brand reputation tracking, and mental health research tools. The Mood Meter and a professional customer insights platform use the exact same underlying technology. The difference is just the interface you wrap around it.

That pattern repeats throughout the course. Every project teaches a genuine ML concept through something you can actually build, test, and play with:

- **Swapping models** in Session 2 teaches you about training data and why different models see different emotions — the same concept behind choosing the right model for a business application.
- **Breaking things with sarcasm** in Session 3 teaches data cleaning and preprocessing — the work that takes up most of a real data scientist's time.
- **Comparing three models head-to-head** in Session 4 teaches evaluation — how professionals decide which model to actually deploy.
- **Testing for bias in voice emotion detection** in Session 7 is the same work that AI ethics teams do at major tech companies before releasing products to the public.

The projects get more playful and more sophisticated as the course goes on, but the underlying skills are always real and always transferable.

## The Four Arcs

The course is organized into four arcs, each building on the one before:

**Exploration (Sessions 1–3):** You build your first Spaces and learn the fundamental pattern of AI tools: input goes in, a model processes it, output comes out. You'll start with a Mood Meter, swap in different emotion models, and discover what happens when sarcasm breaks everything. Along the way, you'll get comfortable with Gradio (the library that turns Python into web apps), Hugging Face, Colab, and a bit of Python.

**Evaluation (Sessions 4–6):** Now that you can build things, you learn to judge them. You'll run three sentiment models side-by-side and watch them disagree. You'll experiment with hyperparameters that control how AI generates text. And you'll discover what happens when you take a model trained on movie reviews and feed it poetry or diary entries. These are the questions that separate someone who can run a model from someone who understands what the model is doing.

**Advanced Topics (Sessions 7–8):** You tackle harder questions: bias, fairness, and multi-modal systems. You'll build a Voice Mood Reader that detects emotion in speech — and test whether it treats all voices fairly. Then you'll build a system that reads both faces and text, and ask: when the face says happy but the words say sad, which one is telling the truth?

**Project (Sessions 9–12):** You design and build your own emotion tool from the ground up. You choose the modality — text, audio, or images — pick the model, build the interface, test it, improve it, and present it. This is where everything comes together.

## What You'll Actually Be Able to Do

By the end of this course, you'll be able to:

- Load and use pre-trained AI models for sentiment analysis, emotion detection, speech emotion recognition, and facial emotion recognition
- Build and deploy web applications powered by AI that anyone can access
- Read a model card and understand what a model was trained on, what it's good at, and where it might fail
- Compare models and evaluate their performance on different kinds of data
- Identify bias in AI systems — including whose voices and faces the models learned from — and articulate why it matters
- Work across modalities: text, audio, and images — and understand what each one captures that the others miss
- Write and run Python code in notebooks, experiment with parameters, and interpret the results
- Use GitHub to manage and share your projects
- Explain core ML concepts — sentiment analysis, training data, domain shift, hyperparameters, bias, multi-modal systems — in your own words, because you've seen them in action

These aren't just academic skills. They're the same skills that data scientists, ML engineers, and AI researchers use every day. The difference is that you're learning them now instead of at the end of years of computer science coursework.

## What You Don't Need to Know Coming In

You don't need to know Python. You'll pick up what you need as we go, and the notebooks are designed so you can experiment even if the code isn't fully clear to you yet.

You don't need to know anything about AI or machine learning. That's what the course is for.

You don't need to be "good at math" or "good at computers." You need to be curious and willing to try things. The models do the heavy mathematical lifting. Your job is to choose the right model, give it the right input, and figure out what to do with the output.

You do need a computer with a web browser and an internet connection. That's it. Every tool we use is free and runs in the cloud.

## Why This Matters

AI is changing how the world works. That's not hype — it's already happening in medicine, law, journalism, science, art, education, and dozens of other fields. The question isn't whether you'll interact with AI in your future career. The question is whether you'll be someone who understands it well enough to use it thoughtfully, critically, and creatively — or whether you'll just be along for the ride.

This course puts you in the first group. Not by lecturing you about the future, but by handing you the tools and saying: build something. See how it works. Break it. Fix it. Make it better. That's how real understanding happens.

Let's get started.

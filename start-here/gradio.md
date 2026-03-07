# Gradio

## What Is It?

Gradio is a Python library that turns a regular Python function into a web app. You write a function that takes some input and returns some output — and Gradio wraps it in a nice interface with text boxes, buttons, and a layout that anyone can use in a browser. No HTML, no CSS, no JavaScript. Just Python.

That's the core idea, and it's what makes everything in this course possible. Every Space you build — from the Mood Meter in Session 1 to the custom emotion tool you design at the end — is a Gradio app. When you see a text box where you paste a sentence and a button that says "Submit," that's Gradio. When you see the output appear below with a label and a confidence score, that's Gradio too.

Here's what a minimal Gradio app looks like:

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
```

That's it. Five lines of code, and you have a working web app with a text box, a submit button, and an output area. Gradio handles all the web stuff — you just write the function.

## Why Does This Course Use It?

Gradio is the bridge between "I wrote some Python code" and "I built something anyone can use." Without Gradio, running an AI model means writing code in a notebook and looking at raw output — useful for learning, but not something you'd show someone. With Gradio, the same model becomes an app with a real interface.

In Session 1, you'll see this in action. The Mood Meter is a Gradio app: it has a text box for input, runs a sentiment analysis model on whatever you paste in, and displays the result with an animated gauge, emoji, and confidence score. The AI model does the thinking, but Gradio is what makes it usable.

As the course goes on, you'll see Gradio do more:

- **Session 1:** A text box in, a visual gauge out — built with `gr.Blocks`, Gradio's flexible layout system
- **Session 2:** Multiple outputs side by side — three models reading the same text, each with its own output box, using `gr.Interface`
- **Later sessions:** Dropdowns, sliders, audio uploads, image displays, and layouts you design yourself

Each session introduces a little more of what Gradio can do, but you're always building on the same basic pattern: write a Python function, wrap it in a Gradio interface, launch it.

## How Does It Connect to Hugging Face?

Gradio was created by the team at Hugging Face, and the two are deeply connected. When you create a Space on Hugging Face, you're deploying a Gradio app. The `app.py` file in every Space is a Gradio script. Hugging Face's servers run your Gradio code and serve the web app to anyone who visits the Space's URL.

This means that learning Gradio isn't just learning a library — it's learning the tool that powers the entire Hugging Face Spaces ecosystem. Every time you try someone else's Space on Hugging Face, there's a good chance you're using a Gradio app. And every Space you build in this course is one too.

## How Does It Connect to GitHub?

Here's where things come together. A Hugging Face Space is really just a small collection of files:

- **`app.py`** — your Gradio code (the Python function + the interface)
- **`requirements.txt`** — the libraries your app needs (like `transformers` and `gradio`)

That's it. Two files. And those files need to live somewhere. That's where GitHub comes in.

In the early sessions, you'll work with these files directly on Hugging Face — editing them in the browser, seeing the Space update. But as the course progresses, you'll start keeping your code on GitHub too. Why? Because GitHub gives you version history (what did this file look like last week?), a portfolio (here are all the projects I've built), and a workflow that professional developers use every day.

The flow looks like this:

1. **Write** your Gradio app (the `app.py` with your function and interface)
2. **Push** the files to GitHub (your code archive and portfolio)
3. **Deploy** on Hugging Face Spaces (where the app actually runs)

You don't need to understand all three steps right now. In Session 1, you'll just see the Gradio app running on Hugging Face. By Session 3 or 4, you'll start connecting the dots between the code, GitHub, and the live Space. By the project phase, you'll be doing the full loop yourself.

## Why Is It Worth Learning?

Gradio has become the standard way to put a face on an AI model. Here's why that matters:

**It's how AI demos work.** When a researcher releases a new model, they often build a Gradio app so people can try it without writing any code. The "Try this model" buttons you see on Hugging Face model pages? Those are Gradio apps. Learning Gradio means you can build the same kind of demo for your own projects.

**It teaches you to think about users.** Writing a Python function is one skill. Wrapping it in an interface that someone else can actually use is a different skill — and an important one. What should the input look like? What should the output show? What happens when someone enters something unexpected? Gradio makes you think about these questions early.

**It's used in industry.** Data scientists and ML engineers use Gradio to build internal tools, prototype ideas for stakeholders, and create demos for clients. It's not a toy — it's a professional tool that happens to also be great for learning.

## A Bit of History

Gradio was created in 2019 by Abubakar Abid, a Stanford PhD student who was frustrated by how hard it was to share machine learning models with non-technical people. He could build a model that classified images or analyzed text, but showing it to someone meant either giving them a Jupyter notebook (which they couldn't use) or building a full web application (which took days).

His solution was Gradio: a library that lets you create a shareable interface in a few lines of code. The project took off quickly in the ML community. In 2021, Hugging Face acquired Gradio, which is why the two platforms are so tightly integrated today. Since then, Gradio has become the default way to build demos and apps on Hugging Face, with millions of Spaces built using it.

## Getting Started

You don't need to install Gradio on your own computer. In this course, Gradio runs in two places:

1. **On Hugging Face Spaces** — when you build and deploy a Space, Hugging Face installs Gradio automatically based on your `requirements.txt`
2. **In Google Colab** — when you run the companion notebooks, you'll install Gradio with `!pip install gradio` at the top of the notebook

In Session 1, you'll see your first Gradio app running live on Hugging Face. You'll read through the `app.py` code and see how a Python function becomes a web app. By Session 2, you'll be changing the code and watching the interface update. No special setup needed — just a browser and curiosity.

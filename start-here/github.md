# GitHub

## What Is It?

GitHub is a website — [github.com](https://github.com) — where people store, share, and collaborate on code. It's the largest platform of its kind in the world, home to hundreds of millions of projects ranging from tiny personal scripts to the source code of major software used by billions of people.

At its core, GitHub is built on a tool called **Git**, which tracks every change made to a set of files. Imagine a version of Google Docs, but for code — where you can see every edit anyone ever made, go back to any previous version, and work on different ideas without messing up what already works. GitHub takes that power and puts it on the web, with a profile page, social features, and a way to share your work publicly.

## How GitHub Fits Into This Course

In this course, you build AI-powered apps using **Gradio** and deploy them as **Hugging Face Spaces**. GitHub is the third piece of that puzzle — it's where your code lives as a portfolio and where you learn to manage files like a professional developer.

Here's the flow you'll build toward over the course:

1. **Gradio** — you write a Python function and wrap it in a web interface (that's your `app.py`)
2. **GitHub** — you store your `app.py` and `requirements.txt` in a repository (your code archive and portfolio)
3. **Hugging Face Spaces** — you deploy the app so anyone can use it in a browser

### Your Portfolio Grows with the Story

GitHub isn't just a filing cabinet — it's a record of your journey through the course. What accumulates there maps directly to the three-act arc:

**After Act I (Sessions 1–3),** your GitHub has your first notebooks — the ones where you tested sentiment models, compared three different emotion classifiers, and tried to break models with sarcasm. These are your evidence files. They document the wall you hit: classification has limits.

**After Act II (Sessions 4–8),** your repository grows with experiments in text generation, hyperparameter tuning, cross-domain testing, bias auditing, and multi-model pipelines. Each notebook and each Space's `app.py` captures a different concept you encountered after the breakthrough.

**After Act III (Sessions 9–12),** your GitHub contains a complete project: a Space you designed for a specific audience, built from a model you chose, tested with real users, and iterated on. Your README tells the story of what you built and why.

By Demo Day, your GitHub profile is a portfolio that shows not just what you built, but how your understanding developed over twelve weeks.

### The Gradio Connection

Every Space you build in this course is a Gradio app. And every Gradio app is really just a small set of files:

- **`app.py`** — your Gradio code (the function + the interface)
- **`requirements.txt`** — the libraries your app needs

GitHub is where you keep a copy of those files. Why not just keep them on Hugging Face? You can — and you will, at first. But GitHub adds things that Hugging Face doesn't:

- **Version history.** GitHub tracks every change. If you break your `app.py` while experimenting, you can see exactly what you changed and go back to the version that worked. On Hugging Face, you'd have to remember what the old code looked like.
- **A portfolio.** Your GitHub profile shows every project you've built, organized and browsable. When the course is over, you'll have a collection of repositories that shows your progression from Session 1's Mood Meter to your final custom project.
- **Notebooks too.** The Colab notebooks you run in each session? Those are `.ipynb` files, and they can live on GitHub as well. When you upload a notebook to GitHub, anyone can click a badge and open it directly in Colab. That's how the course materials themselves are shared.

### When You'll Use GitHub in This Course

The course introduces GitHub gradually — there's no rush.

**Sessions 1–3 (Act I):** You don't need GitHub. You'll see that the course materials live on GitHub (that's where the Colab notebook links point), but you'll be focused on exploring Spaces and gathering evidence about classification models. If you want to explore GitHub on your own, great — but it's not required.

**Sessions 4–6 (early Act II):** You'll start creating your own GitHub repositories. This means: making a repo on the GitHub website, uploading your `app.py` and notebook files, and writing a short README that describes what you built. All through the web interface — no command line. By Session 6, when you're testing models across different domains, having your code on GitHub means you can track what you changed and when.

**Sessions 7–9 (late Act II into Act III):** You'll get comfortable with the workflow of keeping your code on GitHub and your live app on Hugging Face. When you make changes, you update both places. You'll also start looking at other people's GitHub repos to see how they organized their code.

**Sessions 10–12 (Act III):** For your final project, you'll manage the full loop: write your Gradio app, store the code on GitHub, deploy on Hugging Face, and present everything with a polished README. Your GitHub repo becomes the "backstage" of your project — the code and documentation — while your Hugging Face Space is the "front of house" — the live app anyone can try.

## Why Is It Valuable?

GitHub solves a problem that everyone who writes code eventually runs into: keeping track of what you changed, when you changed it, and why. Without version control, coding projects turn into a mess of files named things like `app_final.py`, `app_final_v2.py`, `app_ACTUALLY_final.py`. Git (and GitHub) eliminates that chaos.

But GitHub is more than a filing system. It's also a **portfolio**. Your GitHub profile shows the projects you've built, the code you've written, and how active you are. For anyone interested in tech, data science, AI, or software — whether you're applying to college, an internship, or a job — a GitHub profile with real projects on it is one of the most valuable things you can have. It's proof that you can build things, not just talk about them.

GitHub is also where open-source software happens. Open-source means the code is public — anyone can read it, use it, suggest improvements, or build on top of it. Most of the AI tools we use in this course — the `transformers` library, Gradio, even many of the models on Hugging Face — are open-source projects hosted on GitHub.

## Why Is It Worth Learning?

Learning GitHub early gives you a real advantage. Here's why:

**It's a universal skill in tech.** Whether you end up in computer science, data science, biology research, digital humanities, or any field that touches code or data, you'll encounter Git and GitHub. Learning it now means you won't have to scramble to pick it up later when the stakes are higher.

**It teaches you to work like a professional.** In the real world, nobody codes alone. Teams use GitHub to coordinate: one person works on the user interface, another works on the data processing, and GitHub keeps everything organized. Even in this course, when you duplicate and customize a Space, you're practicing a simplified version of the same workflow.

**It's your public record.** Every Space you build, every notebook you upload, every project you complete — if it's on GitHub, it's visible. Over time, your GitHub profile becomes a living portfolio that grows with you.

## How Important Is It to the AI Community?

GitHub is the backbone of open-source AI development. Here's what that looks like in practice:

**Almost every major AI project lives on GitHub.** The code for PyTorch, Hugging Face's `transformers` library, Gradio, and thousands of other tools — it's all on GitHub. When researchers release a new model or technique, the code almost always ends up in a GitHub repository.

**It's how AI research becomes AI practice.** A researcher publishes a paper. They post the code on GitHub. Other researchers and engineers read the code, reproduce the results, improve on them, and share their improvements back. This cycle — enabled by GitHub — is a huge part of why AI has advanced so quickly in recent years.

**Gradio itself is open-source on GitHub.** The tool you use to build every Space in this course? Its source code is on GitHub at [github.com/gradio-app/gradio](https://github.com/gradio-app/gradio). That means anyone — including you — can see exactly how it works, report bugs, or suggest improvements.

## A Bit of History

Git was created in 2005 by Linus Torvalds — the same person who created the Linux operating system. He needed a fast, reliable way to manage the thousands of contributions that developers around the world were making to Linux. The tool he built, Git, turned out to be useful for far more than just Linux.

GitHub launched in 2008 as a website built on top of Git. It added a visual interface, user profiles, and collaboration features that made Git accessible to people who didn't want to live in the command line. GitHub grew rapidly. By the mid-2010s it had become the default home for open-source software.

In 2018, Microsoft acquired GitHub for $7.5 billion — a sign of just how central the platform had become to software development worldwide. Since then, GitHub has continued to grow and has added features like GitHub Copilot (an AI coding assistant) and GitHub Actions (automated workflows). The platform now hosts over 200 million repositories.

## Getting Started

Creating a GitHub account is free:

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Enter your email, create a password, and choose a username
4. Your username becomes your profile URL (e.g., `github.com/yourusername`), so pick something clean and professional — this could end up on a college application or a resume someday

You don't need to know Git commands to get started. In the early sessions of this course, you won't need GitHub at all — you'll be exploring Spaces and gathering evidence about classification models on Hugging Face. When we do start using GitHub, we'll use the web interface — clicking buttons, not typing commands. There's no rush, and the web interface is plenty for everything we do.

One thing to know: GitHub has a generous free tier. Everything we do in this course is completely free. You get unlimited public repositories, which means unlimited projects that anyone can see.

# Build Your GitHub Profile README

Session 8 Guide

## What This Is

Your GitHub profile README is the page someone lands on when they go to `github.com/<your-username>`. It's the first thing collaborators, teachers, admissions officers, or future internship hosts see when they look you up. Right now most of you don't have one. By the end of this week you will.

A profile README is a special trick GitHub gives you: if you create a repository named *exactly* the same as your username, GitHub displays that repo's README on your profile page. You only need to do the setup once.

## Look at Mine First

Before you draft yours, read mine carefully:

**<https://github.com/buildLittleWorlds>**

Don't copy it — your situation is different from mine. But notice what it's doing:

1. **Tagline under the name.** A bolded line that names what I do in the world before any details.
2. **Current Research, grouped.** Two named threads I'm actively working on, each with a "Start here" link and a short list of selected work. The threads aren't every paper I've ever written; they're the live ones.
3. **Coding Experiments, also grouped.** GitHub repos sorted by purpose, not by recency. Each is a one-line description of what the repo *does*, not what it *is*.
4. **What I Am Building Now.** Forward-looking. What's coming, not what's done. This signals momentum.
5. **Links out.** A handful of external profiles where the rest of my work lives.

Notice what isn't there: no badges, no animated GIFs, no streak widgets, no shields. Just structure and writing. That's deliberate. The README's job is to communicate, not decorate.

## How Yours Will Differ

You're not a faculty member with twenty years of publications. You're a student doing a first piece of real research. Your README should reflect that — and that's a strength, not a liability. The shape mine uses is for someone with a body of work behind them. Yours adapts the same shape for someone with a body of work *underway*.

The translation:

| My section | Your version |
|---|---|
| Current Research (multiple threads) | What I'm Researching (your one thread, in your voice) |
| Coding Experiments (many repos) | Spaces I've Built (your three real Spaces) |
| Books and Selected Publications | Research Journal + Paper-in-Progress |
| What I Am Building Now | What I'm Building Now (same — forward-looking) |
| Links | Hugging Face profile, Collection, school page if you have one |

## How to Build It

### Step 1: Create the special-named repo

If you didn't finish in class:

1. Click your avatar (top right of github.com) → **Your profile**.
2. Find the green **New** button to create a new repository.
3. Name it **exactly** your GitHub username. If your username is `riley-research`, the repo is `riley-research`. Capitalization has to match.
4. Make it **Public**. Check **Add a README file**. Click **Create repository**.

GitHub will show you a banner saying "you found a secret!" — that's how you know the magic worked. The README in this repo will now appear on your profile page.

### Step 2: Open the README and replace the placeholder

Click `README.md` → pencil icon (top right of the file view) → you're now in the editor.

GitHub gave you a one-line placeholder ("Hi there"). Delete it. You're starting from scratch.

### Step 3: Write your sections in order

Use this order. The reasoning behind it: a stranger reads top-down. They should know who you are, then what you're investigating, then what you've made, then where to go next — in that order, every time.

#### Header and tagline

```
# Your Name

One-line description of what you investigate.
```

Don't use a title like "About Me" — your name *is* the header. The tagline is one sentence in your own voice. Examples (don't copy these — write your own):

- *Studying how people remember dreams using small language models.*
- *Building tools to help middle-schoolers learn pottery from photographs.*
- *Investigating whether AI can identify accent variation in spoken Spanish.*

The tagline should be specific enough that two students with adjacent topics couldn't share it.

#### What I'm Researching

A paragraph in your own voice. Name the question, name why it matters to you, link to your paper repo. Don't pretend to be objective — the personal stake is part of why this is worth reading.

```
## What I'm Researching

[paragraph]

[Read the paper-in-progress](https://github.com/<your-username>/<your-paper-repo>)
```

If you only have a draft and not a finished paper, link it anyway. The label "paper-in-progress" is honest and stronger than no link.

#### Spaces I've Built

Three Spaces. Not five, not ten. The three you can stand behind right now. For each: link to it on Hugging Face, then a one-line description that ties it to your research topic.

```
## Spaces I've Built

- [Space 1 name](URL) — what it does, in one line tied to your research
- [Space 2 name](URL) — same
- [Space 3 name](URL) — same
```

Avoid generic descriptions ("a sentiment analysis demo"). Aim for ones a stranger could connect to your research thread ("a sentiment analyzer trained on opera reviews — the baseline for my opera-vs-jazz comparison").

#### Hugging Face

```
## Hugging Face

Profile: <https://huggingface.co/your-hf-username>
Collection: [your curated Collection name](URL)
```

If your Hugging Face username matches your GitHub username, mention nothing — the alignment is the signal. If they're different, that's fine; just list both.

#### Research Journal

```
## Research Journal

[research-journal.md](URL) — weekly notes on what I've tested, noticed, and changed.
```

The journal isn't decorative. It's evidence that you're working. Anyone reading the README can click in and see your actual process.

#### What I'm Building Now

Three or four bullets. What's coming this week or this month — not what you've already shipped. This is the section that shows you're alive and moving.

```
## What I'm Building Now

- A Space 3 ambitious build for [your specific user]
- Verified citations file for the Week 7 sources
- One paragraph of PAPER.md rewritten in plainer voice
```

Update this section frequently. A README with a "what I'm building now" list from three months ago tells a worse story than no list at all.

### Step 4: Commit

Scroll down in the GitHub editor. The commit field defaults to "Update README.md" — that's fine. Click **Commit changes**. Within a few seconds, your profile page will show the new content.

Visit `github.com/<your-username>` to confirm it rendered. If a section looks broken, edit again — markdown forgives almost everything except missing blank lines between blocks.

## What Counts as a v1

A v1 doesn't need to be polished. It needs to be:

- **Honest** — every link goes somewhere real, every section reflects what you've actually done.
- **Current** — no placeholder text, no `[Space 1 name]` left in.
- **Specific** — the tagline, the Spaces' descriptions, and the research paragraph all say something only *you* could say.
- **Linked** — paper repo, Hugging Face profile, Collection, journal — all clickable.

You'll iterate it through Sessions 9, 10, and 11. By Demo Day it's the page you point real visitors to.

## Common Mistakes

- **Treating it like a resume.** It's not. A resume is for jobs you've had; a profile README is for work you're doing.
- **Writing in third person.** "Daniel Plate is a researcher who…" Don't. Write in first person, or use the implied first person of the bullet style. The README is your voice.
- **Listing every Space you've ever made.** Pick three. Cut the rest. A focused profile is a stronger signal than a complete one.
- **Forgetting the tagline.** A README with just an `H1` and section headers but no one-line "what I do" loses the reader before they scroll.
- **Adding decoration before substance.** Badges, GIFs, profile views counters — none of these matter. Skip them entirely until you have something to badge.

## A Note on Iteration

Your README is not a one-time submission. It's the living front door of your research presence. After every session, after every weekend of building, after every paper revision, you'll come back to it and update something — usually the **What I'm Building Now** section, sometimes a Space description, occasionally the research paragraph itself.

Treat it the way you treat your `research-journal.md`: a thing you tend, not a thing you finish.

---

AI + Research Level 2 • Session 8: Make It Public

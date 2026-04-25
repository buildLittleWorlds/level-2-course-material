# Session 8: Make It Public — Profile, Spaces, Paper

## What This Session Covers

Tonight is where the work goes public. Up to now you've been building Spaces, taking journal notes, and drafting toward a research question in private. Tonight you start putting a public face on it: a **Hugging Face profile** with three solid Spaces and a curated Collection, and a **GitHub profile README** that links those Spaces to the paper you're writing, the research question you're investigating, and the journal you've been keeping.

In the AI world, a GitHub profile linked to a Hugging Face profile is the standard public face of someone doing research. GitHub holds the writing and the explanations; Hugging Face holds the experiments. By the end of class tonight, anyone who lands on either page should see what you're researching and how the pieces fit together.

## The session in two halves

The session has two halves, and the order matters.

**First half — public presentation.** We look at a worked-example research profile, then each of you cleans up your Hugging Face presence and starts your GitHub profile README:

- Audit your Hugging Face profile. Identify three Spaces you can stand behind. Fix what's broken. Update titles and descriptions so each Space looks like *your* tool, not a template.
- Curate your Collection so the models and Spaces in it are clearly related to your research topic. A Collection that tells a story about your research interest is a stronger signal than a long unfocused list.
- Create your GitHub profile README — the special repository named identically to your GitHub username — and draft v1 with research areas, your paper-in-progress, your Spaces, your Hugging Face profile, and "what I'm building now."

**Second half — match the substance to the front.** Once your profile says "I'm researching X," what people find when they click through has to actually be X. That's the paper, the research journal, the Spaces, and the curated Collection — all pointing at the same investigation:

- Copy your parallel-example packet into your own GitHub account via "Use this template." This becomes your `PAPER.md` repo, linked from your profile.
- Read your `cover-note.md` and start the **Anchor** move: open your real Space, run one real test, and swap the result into section 4 of `PAPER.md`. Replace the example outputs with your real ones.
- Hold a brief Gradio → Gemini API demo as a worked example of how free-tier Spaces connect to hosted models so they can do real research work — and where that connection breaks. Use the lesson to add one sentence to your paper's limitations section: when your tool talks to an upstream model (whether through your own API call or a hosted Space someone else maintains), you inherit its quirks, and the connection point is where errors propagate.

## The core teaching line

> First decide how you want to present yourself publicly. Then make sure what people find there matches what you said.

## Worked example for the profile move

We'll look at <https://github.com/buildLittleWorlds> on screen as the pattern: research areas at the top, current research with linked papers, coding experiments grouped by purpose, publications, "what I'm building now," and links out. Yours will look different in content but follow the same shape.

## Where the Session 8 technical concept lives tonight

The original Session 8 idea is multi-model systems and how errors propagate through them. We do that lesson tonight in the form your projects will actually take: a Gradio Space connected to Google's Gemini model via an API key stored in Hugging Face Secrets. The Space itself lives on free CPU; the heavy thinking happens upstream on Gemini's servers. This is the pattern that lets a free-tier Space do real research work — and it's the pattern several of you will need to ship the project you've been planning.

The takeaway is for your **paper's limitations section**: when your tool depends on an upstream model via API (or even an already-hosted Space someone else maintains), you inherit every quirk of that model — biases in its training data, occasional hallucinations, the possibility that the contract between your code and the model breaks unexpectedly. Name where that connection sits in your project, and what would happen to your findings if the upstream piece changed.

## A bigger frame: humans inside technical systems

Tonight's two halves are two versions of the same question — *how do you make the pieces fit together so the system actually works?*

1. **Models talking to models.** When your Space sends a request to Gemini and asks for a JSON-shaped response, your downstream code can only act on what Gemini actually returned. If Gemini hallucinates a result, your tool reports a confident wrong answer. If Gemini returns prose instead of JSON, your parser fails and your Space goes red. The pieces have to fit, and the contract between them is where the fitting holds or breaks.
2. **You inside a research infrastructure.** GitHub and Hugging Face are themselves technical systems — written in code, hosting code, managing code in repositories, deploying models from code. When you set up a profile, write a README, commit edits, and link a paper repo to a Hugging Face Collection, you are literally participating in a code-based system that is also where research identities get built and read. Your profile isn't a *metaphor* for a technical pipeline — it's a real one. The fitting between what your profile claims and what the linked repos actually contain is the same kind of fitting BLIP and sentiment have to do, just with a human author at one end.

Session 9 picks up the same question at a third scale: **the technical model talking to the humans it's supposed to serve.** It's not enough for a model to produce a correct output; it has to do so in a way that fits the values, goals, and judgment of the people who will use it. (Reinforcement Learning from Human Feedback — RLHF — is the move that named this problem concretely for generative AI.)

So Sessions 8 and 9 are really one argument: *humans and technical systems fit together at every scale*. Code talks to code in a pipeline. Researchers talk to the research community through code repositories. Models talk to users through interfaces. Each layer is technical, each layer is human, and the fitting question — does this piece work given what the next piece needs? — is the same question every time.

That's why what you do tonight on your profile and what you do in Session 9 on your interface aren't add-ons to the technical curriculum. They're the technical curriculum, scaled up to where you actually live as a developing researcher.

## Session Resources

- **[`../PAPER-TEMPLATE.md`](../PAPER-TEMPLATE.md)** — the master AI prompt for paper drafting
- **[`../GUIDE-FROM-SPACE-TO-PAPER.md`](../GUIDE-FROM-SPACE-TO-PAPER.md)** — how the prompt-first paper workflow works
- **`parallel-example/` folder inside your student folder** — your five-file packet (read `cover-note.md` first)
- **[`BETWEEN-SESSION.md`](./BETWEEN-SESSION.md)** — what to revise this week and how
- **[`GUIDE-error-propagation.md`](./GUIDE-error-propagation.md)** — research method card on connecting models via API; supports the limitations move
- **slides.html / app.py / notebook.ipynb** — supporting material for the Gradio → Gemini API demo

## What students should leave with

- A Hugging Face profile with three Spaces you can stand behind and a Collection curated around your research topic
- A GitHub profile README v1 — research areas, paper-in-progress, Spaces, Hugging Face link, "what I'm building now"
- Your own GitHub copy of the parallel-example packet, linked from your profile
- One real anchor move started in `PAPER.md` (your real Space, your real prompt, one real result in section 4)
- A clear next step for finishing the anchor and one paragraph of voice work this week

## Connections

**Builds on:** Session 7 (your rough `PAPER.md` draft, your `week-07-source-search.md` shortlist, the journal you've been keeping)

**Bridges to:** Session 9 — *Prompt Logic and Human-AI Interaction.* Same fitting problem, third scale. We move from "do the technical pieces fit each other" and "does your front match your substance" to "does this model fit the humans it's supposed to serve?" Continued paper revision and the start of the careful-paper-reading work travel alongside that.

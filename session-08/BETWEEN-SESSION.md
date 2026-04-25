# Between Sessions 8 & 9

> **What this week is about:** finishing what we started tonight on both halves — public presentation (Hugging Face profile, Spaces, Collection, GitHub profile README) and matching substance (paper anchor, voice work, journal entry). By Session 9, anyone who lands on your GitHub or Hugging Face profile should be able to see what you're researching and click through to find the actual research.

Tonight we framed the session as the moment the work goes public. We looked at a worked-example research profile, cleaned up your Hugging Face presence, started your GitHub profile README, copied your parallel-example packet into your own GitHub account, and began the Anchor move on `PAPER.md`. This week, finish each of those threads.

---

## Step 1: Hugging Face — three Spaces and a curated Collection (45 min)

**Goal:** A Hugging Face profile that, on its own, communicates what you're researching.

1. Go to your profile at `huggingface.co/<your-username>`. Look at it as a stranger would.
2. Identify three Spaces you can stand behind — your **baseline**, your **domain-specific**, and your **ambitious** (or whichever three are closest to ready).
3. For each of those three Spaces:
    - Make sure it actually runs. Open it, try a few inputs, fix obvious errors. If a Space is broken in a way you can't fix in 15 minutes, paste the error into Claude or ChatGPT and ask for a debugging path.
    - Update the title and description so they describe *your* tool in *your* domain — not a copy of a template.
    - Add 3–5 example inputs that a real user in your domain would actually type.
4. Open your Collection. Curate it so the models and Spaces in it are clearly related to your research topic. A focused Collection of 8–12 items that tells a story about your interest is stronger than a long list of unrelated things. Remove items that don't fit. Add a one-line annotation to each item explaining why it's there.
5. Make sure your Hugging Face username matches your GitHub username if it's available. Same name across both makes the linkage obvious.

---

## Step 2: GitHub profile README v1 (30 min)

**Goal:** A `github.com/<your-username>` page that points at your paper, your Spaces, your Collection, and your Hugging Face profile.

If you didn't finish creating the special-named repo in class:

1. From your GitHub avatar (top-right) → **Your profile** → green **New** button.
2. Repository name: **exactly your GitHub username** (e.g. `annabelle-ai`).
3. Public. Add a README file. Click **Create repository**.

Now edit `README.md`. Here's the starter shape — fill in your actual content:

```markdown
# Your Name

One-line description of what you're investigating.

## What I'm Researching

A paragraph in your own voice naming your research question and why
it matters to you. Link to your paper repo:
[my paper](https://github.com/<your-username>/<your-paper-repo>).

## Spaces I've Built

- [Space 1 name](URL) — one-line description tying it to your research topic
- [Space 2 name](URL) — one-line description
- [Space 3 name](URL) — one-line description

## Hugging Face

Profile: <https://huggingface.co/your-hf-username>
Collection: <link to your curated Collection>

## Research Journal

[research-journal.md](https://github.com/<your-username>/<your-paper-repo>/blob/main/research-journal.md)
— weekly notes on what I've tested, noticed, and changed.

## What I'm Building Now

- A short bulleted list of what's coming, not what's done.
```

Commit. That's v1. You'll keep iterating it as your paper, Spaces, and Collection grow.

---

## Step 3: Finish the Anchor in `PAPER.md` (45 min)

**Goal:** When someone clicks through from your profile to your paper, what they find is genuinely about your project.

Open your parallel-example repo (the one you forked tonight) and re-read `cover-note.md`. The cover note names the specific Anchor / Voice / Stretch moves for your project.

If we did not finish the Anchor in class:

1. Open the Space your cover note points to.
2. Run the test or comparison the cover note describes (a small prompt grid, a side-by-side comparison, two real inputs through one model).
3. Paste two or three of your real outputs — the ones that show the most interesting pattern — into section 4 of `PAPER.md`, replacing the placeholder example outputs.
4. Update the limitations paragraph (section 5) so it describes what *your* test couldn't cover.

Edit directly in your repo: click filename → pencil icon → edit → **Commit changes**.

If your cover note says your anchor isn't reachable this week (a Space is broken, a Space hasn't been built yet), follow the alternate path the cover note describes — usually a verbal walkthrough transcribed into a journal entry, or a commitment to a specific Session 9–10 build.

---

## Step 4: One paragraph of Voice work (20 min)

Pick **one** paragraph from your cover note's Voice list — usually the introduction or the "why this matters" paragraph in section 1. Don't paste the draft into Claude and ask for a smoother version. Instead:

1. Read the current paragraph aloud.
2. Say what you actually mean, in your own words, into a voice memo.
3. Write down what you said.
4. Edit it lightly for clarity. Keep your own phrasing.

Commit the change.

---

## Step 5: One sentence in your limitations (10 min)

Tonight's mini-demo showed how errors cascade through chained models. Look at your project: does it chain anything?

- Generation followed by critique?
- Transcription followed by summarization?
- Captioning followed by classification?
- Retrieval followed by answering?

If yes, add **one sentence** to section 5 of `PAPER.md` naming where errors could compound and what the downstream consequence would be. If your project doesn't chain models, skip this step.

For background, see [`GUIDE-error-propagation.md`](./GUIDE-error-propagation.md).

---

## Step 6: Journal entry (15 min)

Open your `research-journal.md` and add a Week 8 entry covering:

- What you cleaned up on your Hugging Face profile and Collection
- What your GitHub profile README v1 looks like (paste a link)
- What real outputs you swapped into `PAPER.md` and what you noticed when you ran the real test
- One thing you want to fix or extend before Session 9

Specifics matter more than completeness. "Fixed the title and added three opera-jazz-classical examples to Music-Starter-Opera-Jazz" is a stronger journal entry than "improved my Space."

---

## Optional: Stretch (only if Steps 1–6 are done)

Your cover note names one specific stretch move. Tier A students should aim for it. Tier B and C students should not — finish the public presentation and one solid Anchor + Voice pass rather than rushing to Stretch.

---

## What to bring to Session 9

- Your GitHub profile URL (`github.com/<your-username>`)
- Your Hugging Face profile URL with three working Spaces and a curated Collection
- Your paper repo URL with `PAPER.md` showing real outputs in section 4 and one rewritten paragraph
- A Week 8 journal entry
- Your `week-07-source-search.md` shortlist — Session 9 begins the careful-reading work on one source from that list

---

## What Session 9 picks up

Tonight's two halves were two versions of the same fitting problem.

- **Models talking to models.** When the first model is wrong, the second has no way to know. The pieces have to fit.
- **You talking to your audience.** When your profile says one thing and the substance underneath says another, the pieces don't fit. The system fails as a piece of public communication.

Session 9 picks up the same problem at a third scale: **the technical model talking to the humans it serves.** It's not enough for a model to produce a correct output; it has to do so in a way that fits the values, goals, and judgment of the people who will use it. This is exactly the problem RLHF named for generative AI — the move from "the model produces a fluent paragraph" to "the model produces a paragraph the person actually wanted."

So the question that runs across Sessions 8 and 9 is one question at three scales: *how does the technical connect to the human?* Tonight you experienced it twice. Next week is the third.

---

## A note on the original Session 8 between-session work

The "read one paper carefully with AI as a partner" exercise lives in [`WEEK-8-RESEARCH-WORK.md`](./WEEK-8-RESEARCH-WORK.md) and is now Session 9 work. If you finish the steps above and want to start the careful-reading work early, the file is here.

---

AI + Research Level 2 • Session 8: Make It Public

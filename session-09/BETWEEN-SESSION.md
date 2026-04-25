# Between Sessions 9 & 10

> **What this week is about:** finishing the audience-fit work on one of your Spaces, completing citation verification on every source you plan to use, and continuing the public-facing iteration you started in Session 8 (profile README, Collection, paper). By Session 10, the substance behind your profile is one round more honest and one round more useful.

Tonight extended Session 8's argument: the same fitting problem that runs between two chained models, and between your public profile and the substance behind it, runs again between your model and the real human who will use it. We named the move and rehearsed it once on the Restaurant Review Analyzer. This week you apply it to one of your own Spaces, verify every citation in your paper, and keep iterating the public-facing system you started building last week.

---

## Step 1: Space 3 — get it built and fit it to a human (60–90 min)

**Goal:** Space 3, your ambitious Space, deployed and working by Session 10 — and fit to a real human user from the start.

Some of you already have Space 3 built; others are still finishing. Either way, this week is when it lands. By Session 10 it needs to be live so we can polish, integrate, and start drafting the portfolio story.

**If Space 3 isn't deployed yet — this is the priority for the week.** Don't build it as a generic demo. Tonight's framing — fit the model to a real human — applies from the start:

1. **Name your user before you write any code.** One specific person, not "everyone." A specific kind of researcher, clinician, journalist, musician, gamer — whoever your project is actually for. Write that person as one sentence at the top of your notes: *"Sarah, an opera coach preparing students for NYSSMA."*
2. **Decide the four human-facing surfaces upfront:**
    - **Title** — what would *Sarah* call this tool?
    - **Description** — describe it to *Sarah*, not to a programmer.
    - **Examples** — three inputs *Sarah* would actually type.
    - **Output framing** — turn raw model output into something *Sarah* can read at a glance.
3. **Build the Space.** Use the plan from your Week 8 journal entry. Use the starter prompts in your student folder, or write your own and paste into Claude or ChatGPT. Create a new Space on Hugging Face. Upload the files. Debug as needed. Wire the four surfaces in as you build, not as polish-after.
4. **Test with one real person who didn't help build it.** Watch what they do. Their confusion is your redesign checklist.

**If Space 3 is already deployed:** apply the same audience-fit move to one of your weaker Spaces (often Space 1 or 2). Same loop — name the user, redesign the four surfaces without changing the model, test with someone real, watch what happens. Then come back and use whatever time is left to polish Space 3's user-facing surfaces too.

Either path:

- Update your **GitHub profile README** to point at the resulting Space with a one-line description that names the user it's for.
- Edit Spaces directly in the Hugging Face web editor. No terminal needed.

---

## Step 2: Citation verification (60–90 min)

**Goal:** Every citation in your paper passes the eyeball test.

This is the most important research-hygiene work of the course, and it applies anywhere you write with AI help — not just in here. AI language models hallucinate citations: plausible authors, plausible journals, plausible-looking DOIs, and some percentage of the time the paper does not exist.

Create `week-09-citations.md` in your paper repo. For each source on your Week 7 shortlist:

1. **DOI check.** Paste the DOI into [doi.org](https://doi.org). Does it resolve to a paper with matching title and authors?
2. **Title search.** Search the title in quotes on [Google Scholar](https://scholar.google.com). Confirm authors and year.
3. **Claim check.** Open the paper. Find the specific claim you plan to cite. Paste the supporting sentences from the paper into your `week-09-citations.md` next to your citation. If you can't find the claim in the paper, the citation does not go in your paper.

Format each entry like this:

```markdown
**Author, A., & Author, B. (YEAR).** *Title of paper.* Journal, vol(issue), pages. https://doi.org/...

- Claim I'm citing: <one sentence in your own words>
- Supporting passage from paper, with section/page: "<exact quote from the paper>"
```

At the top of `week-09-citations.md`, one paragraph naming which references are peer-reviewed and which (if any) are not. At the bottom, one paragraph reflecting: how many of your Week 7 sources survived verification? Did any fall out? Did any need to be replaced?

Full guide: [`WEEK-9-RESEARCH-WORK.md`](./WEEK-9-RESEARCH-WORK.md).

---

## Step 3: Revise one paragraph of `PAPER.md` for your audience (20 min)

**Goal:** Tonight's audience-design move applied once to your own paper.

Open your `PAPER.md`. Pick the paragraph that currently sounds the most like a *generic research paper introduction* and the least like *something a real person would want to read.* Often this is the introduction or the discussion.

Then:

1. Name the audience for your paper — not "the field," but one realistic reader. A peer in your school's AI club. A college admissions officer reading your portfolio. A specific teacher who knows your domain.
2. Rewrite the paragraph for that reader. Use language they'd use. Cut what they don't need. Keep what they'd find specific and surprising.
3. Commit the change to your paper repo.

This is the same fitting move you did on your Space, just applied to text instead of an interface.

---

## Step 4: Profile and journal iteration (15 min)

**Goal:** Your public-facing system stays current as the work evolves.

- Update your GitHub profile README to reflect the redesigned Space and the citation work in progress. The "What I'm Building Now" bullet should mention what you're doing this week.
- Add a Week 9 entry to your `research-journal.md` with: the user you redesigned for, what you swapped in the four surfaces, what surprised you when you tested it, how many citations survived verification, and which paragraph of `PAPER.md` you rewrote for your audience.

---

## Optional: Stretch

If Steps 1–4 are done and you have time:

- Apply the audience-redesign move to a *second* Space.
- Run the verification loop on one source you didn't have on your Week 7 shortlist — one you found by following a citation chain from a verified source.

Tier A students should aim for one stretch move; Tier B and C students should not — finishing audience-fit on one Space and verifying every citation is more valuable than rushing.

---

## What to bring to Session 10

- **Your Space 3 URL** (paste in chat at the start of class) — deployed and working, with the four human-facing surfaces (title, description, examples, output framing) fit to a named user
- The URL of any other Space you audience-redesigned this week
- Your `week-09-citations.md` with verified entries
- Your `PAPER.md` with one paragraph rewritten for your real audience
- Your Week 9 journal entry
- Your GitHub profile README updated to point at Space 3

---

## The through-line so far

We started Session 8 with two models in a pipeline (technical fit) and your profile pointing at substance (public-facing fit). Session 9 added the third scale: a model fit to a real human user. The pattern has held at every scale — pieces fit, or the system fails.

Sessions 10–12 stay in this pattern. Session 10 polishes your ambitious Space (Space 3), integrates the three Spaces and the paper into one coherent project, and starts drafting the portfolio narrative — every move tested against the same fitting question. Session 11 iterates through peer feedback — your work being read by real other humans. Session 12 is Demo Day, where the whole system gets shown to a real audience.

The fitting question is the AI research question. You're doing it now.

---

AI + Research Level 2 • Session 9: Make Your Model Fit the Human

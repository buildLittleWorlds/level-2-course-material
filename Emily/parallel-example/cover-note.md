# Cover Note — Emily

This packet is **a starter draft of your paper, rebuilt around the work you have already done in Google Drive**. It is not the version that was here before. The earlier draft assumed you were starting from scratch; you aren't, and that earlier framing didn't reflect your actual work. What follows treats the Drive material as the substance and treats the four remaining sessions as the time to translate that substance into the GitHub/Hugging Face surface — not to re-do the thinking.

Three moves over the next four sessions.

---

## Read this first

You have already done more than it looks like from the GitHub side. From your Drive document I can see:

- A real **project outline** for a four-pillar news newsletter — neutral summary, per-article bias detection, sentiment collection, user journal — inspired by Ground News.
- A **Week 1 and Week 6 journal entry** documenting a substantive pivot from a global conflict tracker to your current concept.
- A **34-paper Consensus literature review** that names four theoretical frames driving the field — the *machine heuristic* (Cloudy et al., Hong et al., Huh et al.), *algorithm aversion* and *trust degradation* (Altay & Gilardi, Wang et al.), *automation bias* (Tafur & Sarkar), and *emotional override of source cues* (Zhao et al.) — plus a research-gaps matrix and a set of open research questions.
- A refined research question: **"Does exposure to AI-detected bias change how users perceive news?"**

That's strong work. It is genuinely above the level of the parallel-example draft you'll see in `PAPER.md`. The reason it doesn't show up in your GitHub repo yet is that **you've been working in Drive, where you're comfortable as a writer**, instead of in GitHub, where the platform is unfamiliar. That's the actual gap, and that's what we work on across the next four sessions.

---

## Anchor

The anchor is **the translation**, not the research. The research is already there.

Three steps, doable across Sessions 8 and 9:

- **Move your Drive material into the repo.** The project outline (Tab 1), the Week 1 and Week 6 journal entries (Tab 2), and the literature review (Tab 3) all need GitHub homes. The `PAPER.md` in this packet shows what the academic write-up shape looks like; your job over Sessions 8 and 9 is to replace its placeholder content with **your** outline, **your** refined question, **your** lit review claims, and **your** Week 6 pivot story. We can do this together — most of it is paste-and-format, not rewrite.
- **Run one real test in Session 8.** Pick one news event you've followed (a UN vote, a climate story, an election outcome — your choice). Send the same article through Claude or ChatGPT three times asking each time for a summary written from a different stated perspective (humanitarian NGO, national-security adviser, youth climate delegate, or other Model UN positions you've actually played). Save the three outputs. Walk through them with me out loud applying the framing table in `PAPER.md` section 3 — shared facts, word choice, centered actor, main risk, implied solution. I'll transcribe what you say into a Week 7 journal entry while you talk. That gives you (a) a real test in your repo, and (b) outputs that can replace the placeholder example in `PAPER.md` section 4.
- **Build a stripped-down working version of one pillar in Sessions 9 and 10.** Not all four pillars — the bias-detection-per-article pillar, since it's the central research move and it's the one your refined question is about. A Hugging Face Space template that takes a pasted article, returns a neutral summary, and shows an AI-detected bias score with two cross-spectrum quotes. Roughly 30-40 lines of Python wrapped around a Gemini API call (you already have a key). The Space doesn't need to be polished. It needs to *exist* and produce one or two real bias-detection outputs that the paper can point at.

That sequence — translate, test, build one pillar — turns the Drive work into a defensible portfolio artifact without forcing you to redo any of the thinking.

## Voice

Three paragraphs to rewrite in our working sessions:

1. **Section 1 introduction.** Your real story is in your Drive Week 6 entry: you started with a global conflict tracker focused on what's happening in IR, realized it didn't actually help the general public make sense of news, and pivoted to a Ground-News-style personalized newsletter that makes bias visible on purpose. That pivot is the introduction. Say it plainly. You're a Model UN delegate who noticed AI tools flatten political stories into one neutral-sounding voice and decided to build something that does the opposite.
2. **Section 2 "Why this matters."** This is the section where your lit review most belongs. Your Consensus review names four theoretical frames — the machine heuristic, algorithm aversion, automation bias, and emotional override — that together explain *why* bias-aware design is a real research question, not a vague concern. Pull the strongest claim from each frame into a paragraph that explains what's at stake. You've already done this analysis; the move is fitting it into the paper's voice.
3. **Section 5 limitations.** Your honest limitations: small test set so far, the bias-detection pillar is a first build (the other three pillars are designed but not built), you're using a closed-source model (Gemini) which constrains reproducibility, and the per-article bias scoring depends on the model's own training biases — a limitation the lit review already names. Be plain about each.

Tell me each one out loud first, then we rewrite together. Don't paste into Claude — that's exactly the move that erases the Model UN voice we're trying to keep, and the Drive work already shows you can write in your own voice.

## Drive-to-GitHub workflow (alternate path)

This is your tier's third bullet. The technical environment of GitHub and Hugging Face is genuinely unfamiliar in a way the writing isn't, and the move here is to make the platform get out of your way so the work can be visible.

The honest workflow: **draft in Drive, paste into the GitHub web editor, commit.** Specifically:

- Keep writing in Drive when that's where you think clearly. The paper doesn't need to be composed in GitHub.
- When a section is ready, copy the text out of Drive, click the file in your repo, click the pencil icon, paste, scroll down, type a one-line commit message ("added introduction" / "moved Week 6 entry over"), and click "Commit changes."
- That's the entire deployment pipeline for the writing side. It's not different from saving a file in Drive — it just lives somewhere a portfolio reader can find it.
- Markdown formatting is forgiving. `# heading`, `## subheading`, `**bold**`, `*italic*`, blank lines between paragraphs. If you want a list, start the line with `- `. That's most of what you'll need.

For the Space build (Sessions 9 and 10), I'll bring a working code template — your job will be to read it, change the parts that need to be changed (the API key reference, the prompts, the labels), and paste it into a Hugging Face Space. Same model: paste, commit, see it run.

---

## Two housekeeping nudges

**Source verification.** Your Consensus lit review is the strongest single artifact in the cohort right now. Before any individual paper makes it into the final `sources.md` in the repo, verify the title, authors, venue, and the claim the paper actually makes. Consensus's abstract-level summaries are accurate but compressed; for the eight or ten papers you'll cite directly, read the abstract on Semantic Scholar or PubMed and confirm. We can do this together for the first three or four to calibrate what "verified" means.

**Repo population.** Your `AI-News-research` repo currently has 1-byte placeholder files for `paper.md` and `research-journal.md`. Before Session 9, those get replaced with content from this packet plus your Drive material. The Week 7 journal entry from our Session 8 in-class test goes in first, then your Week 1 and Week 6 entries get added (so the journal has continuity from before the course pivot through to the current concept), then this `PAPER.md` (with our adjustments and your real lit review).

---

AI + Research Level 2 • Paper Phase

# Week 9 Research Work

Prereq: your `week-08-paper-read.md`.

This is the most important piece of research work in the course, and it's relevant to anyone writing with AI help anywhere — not just in here.

## The problem

**AI language models hallucinate citations.** They generate things that look exactly like real paper citations — plausible authors, plausible journal names, plausible-looking DOIs — and some percentage of the time, the paper does not exist. In 2023 a real lawyer in New York got sanctioned for filing a brief where ChatGPT made up six court cases. All plausible. None real. He didn't verify.

The rule: **AI can tell you a citation exists. Only your eyeballs on the actual paper can confirm it does.** Every citation in your eventual brief has to pass the eyeball test.

## Legitimate AI uses for citations

- **Formatting** a citation after you've pasted in the real title, authors, year, venue, and DOI from the actual source.
- **Reformatting** from one style to another (e.g., to APA).

## The dangerous use

- Asking AI to *supply* a citation on a topic. This is where hallucinations happen.

## The three-step verification

For any citation:

1. **DOI check.** Paste the DOI into doi.org. Does it resolve to a paper with matching title and authors?
2. **Title search.** Google Scholar the title in quotes. Do the authors and year match?
3. **Claim check.** Open the paper and find the specific claim you plan to cite. The existence of a paper is not enough — the AI may have cited a real paper for a claim the paper doesn't actually make.

## What to do before Session 10

Create `week-09-citations.md`. This file becomes the References section of your Week 10 brief.

1. Start from your Week 7 shortlist. For each paper:
   - Full APA citation (authors, year, title, venue, DOI). You may use AI to format it — but only after you've pasted the real title/authors/year into the prompt.
   - **Verify the DOI.** Click it. Confirm it resolves to the right paper. If the AI garbled it, fix it from the real source.
   - **Verify the claim.** Next to each citation: one sentence stating the specific claim you plan to cite. Then go find that claim in the actual paper and paste the sentence(s) that support it, with section or page reference. If you can't find the claim, the citation doesn't go in the brief. Period.
2. At the top, one paragraph naming which references are peer-reviewed and which (if any) are not. The brief can include non-peer-reviewed references, but they should be labeled.
3. At the bottom, one paragraph reflecting: *How many of your Week 7 sources survived verification? Did any fall out? Did any need to be replaced?*

## Watch out for

- "Almost right is wrong." One author off, year off by one, wrong journal — all invalidate the citation.
- Hallucinated *quotes* attributed to real papers are the worst failure mode. If you had cited that quote, you would have fabricated evidence. Verify.
- Paywalls: if you can only read the abstract, you can only cite what's in the abstract.
- arXiv ID is fine for preprints; DOI preferred for published journal articles.

## For an example

Prea's [research brief References section](../example-student-prea/research-brief.md) shows what a fully verified citation list looks like — including one deliberately-labeled non-peer-reviewed source (the Mistral Voxtral blog post) that she cites for architectural context rather than empirical claims. Notice how each of her citations is tied to a specific claim in the main text, not just a general topic.

---

AI + Research Level 2 • Session 9 Research Work

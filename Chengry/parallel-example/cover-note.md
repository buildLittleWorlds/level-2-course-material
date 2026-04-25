# Cover Note — Chengry

This packet is a **starter draft** of your paper, built from your `paper-starter.md`. It is not a model answer and it is not the final version. Your job over the next four sessions is to make it yours. Three moves do that.

---

## Anchor

The packet imagines an "Uncertainty-First Symptom Explainer." That's a placeholder for **DxAI**, which is what you actually built. The first move is making that explicit throughout the paper.

The good news: the packet's central claim is already aligned with your real Space. DxAI gives ranked possible conditions with symptom analysis and recommended actions, plus prominent disclaimers. That *is* the ranked-and-cautious interface the paper argues for. So most of the work is making the paper sound like it's about DxAI specifically, not about an imagined system.

Two steps:

- **Replace the imagined Space name with DxAI throughout.** Title, abstract, introduction, method section, conclusion. Section 3 should describe DxAI's actual ranked-output design as Mode B, and either (a) describe a hypothetical single-answer baseline you're contrasting against, or (b) test the same prompt through Claude/GPT directly with no scaffolding as Mode A, and use that as the comparison.
- **Run two or three real symptom prompts through DxAI** and through a baseline (Claude or GPT directly, no ranked output, no red flags). Save both outputs side-by-side. Pick the one that shows the uncertainty-communication contrast most clearly. Replace the example in section 4 ("I have a headache and my vision is blurry") with your real one — though that example is fine if you want to use it for real, since the comparison is what matters.

This converts the paper from "an argument about how medical AI interfaces should work" into "an argument about how my interface, DxAI, communicates uncertainty better than the baseline." That's the version that goes in a portfolio.

The DxAI runtime error (missing audio dependencies) becomes part of the limitations paragraph, not a problem. Say plainly: "the current build has a runtime issue around audio input, but the ranked-text output design is implemented and testable." Honest and specific.

## Voice

Three paragraphs to rewrite in our working session:

1. **Section 1 introduction.** Your *real* design philosophy belongs here. You chose ranked outputs, you wrote the disclaimer language, you picked the dark theme with green accents, you decided to use Claude Opus 4.5 as the underlying model. Each of those was a design choice with a reason. The introduction should sound like a builder explaining design choices, not a generic study of medical AI safety.
2. **Section 2 "Why this matters."** This is where the paper currently feels least like you. Pull in your *actual* engagement with these questions — your Week 2 journal entry on the SHIFT framework and the Smol AI WorldCup space showed you already think carefully about how presentation shapes interpretation. That's the same instinct driving DxAI. Connect them.
3. **Section 5 limitations.** Your honest limitations: the runtime error, the fact that you haven't tested DxAI with real users, you're using a closed-source model (Claude) which makes the system harder to reproduce. Name each plainly.

Tell me each paragraph out loud first, then we rewrite together. Don't paste into Claude — that's exactly the move that makes a paper *about* responsible AI use sound generic.

## Stretch

You're one of the strongest stretch candidates. Two real options:

**Option A:** Build a stripped-down "Mode A" version of DxAI as a second tab or a second Space — same model, same disclaimer, but single-answer output instead of ranked. Run the same prompts through both. That gives you a real within-system comparison instead of comparing DxAI to an external baseline.

**Option B:** Run a small **user comprehension probe**. Show two friends or classmates the same symptom output in both formats (ranked vs. single-answer) and ask: "Did this feel like a diagnosis?" Even four or five people would give you something to report. That's a real user-testing finding, and your paper-starter already gestures at this question.

Either is a real extension. Skip if no time. Anchor + Voice is the priority.

---

## Two housekeeping nudges

**The DxAI runtime error.** Worth fixing before Session 12 if possible — not for the paper, but for the portfolio. An admissions reader following a link to a working Space is much better than one finding a runtime error. We can debug this together in a session.

**Source verification.** The candidate references in `PAPER.md` are abstract-checked only, via Consensus. The Singhal et al. *Nature* paper on clinical knowledge in LLMs and the Hager et al. *Nature Medicine* paper on clinical decision-making are real and very relevant — those are probably keepers. But still verify each one (title, authors, venue, what they actually claim) before you cite them in a finished paper.

---

AI + Research Level 2 • Paper Phase

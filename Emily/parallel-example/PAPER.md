# AI News Lens: Does Exposure to AI-Detected Bias Change How Users Perceive News?

## Abstract

This paper studies whether AI tools that make political bias visible — through per-article bias scoring, side-by-side framing comparisons, and explicit AI labeling — change how users perceive news. The project takes the form of a planned four-pillar news newsletter, **AI News Lens**, with a working first build of the per-article bias-detection pillar. The paper grounds the design question in four theoretical frames identified through a literature review of 34 papers: the *machine heuristic* (machines are perceived as more objective than humans), *algorithm aversion* (explicit AI labels lower perceived accuracy), *automation bias* (algorithmic warnings shift user beliefs even when incorrect), and *emotional override* (emotionally charged stories elicit engagement regardless of source cues). The central claim is modest: a bias-aware news tool can shift perception, but the direction depends heavily on how the bias signal is presented, on who is reading, and on whether the story's emotional load overrides the cognitive cue. The paper argues that this is a design space worth taking seriously and reports on a first build that tests one bias-presentation strategy.

## 1. Introduction and research question

Most AI news tools optimize for fluency. They produce clean summaries that read well. The Reuters Institute has warned that this fluency comes at a cost: AI-summarized news can flatten the differences between competing perspectives and weaken the editorial signal that distinguishes one news brand from another.

I came to this question through Model UN. In MUN, you read the same event described by a humanitarian organization, by a national-security ministry, by a youth climate delegation, and by a domestic opposition party — and the differences between those descriptions are not noise. They are the substance of what's being argued. When I started testing AI summarization tools on political news, I noticed they tend to produce what felt like "neutral" summaries that were actually just smooth — the conflict words were gone, the contested history was shortened, and the issue sounded less contested than it was.

That observation became the project. After a Week 6 pivot away from a global conflict tracker (which I realized didn't actually help the general public make sense of news), I started designing a different tool: a personalized newsletter that makes bias visible on purpose. **AI News Lens** is that tool. It doesn't claim to deliver neutral news. It produces a neutral *summary*, then shows AI-detected bias on a per-article basis, surfaces representative quotes from across the political spectrum, and asks the reader to record their sentiment after reading. The design is inspired by Ground News, but applied at the per-article level rather than at the outlet level.

This paper asks:

> Does exposure to AI-detected bias change how users perceive news?

This is a researchable question because the empirical literature on AI labels and bias cues is substantial — and ambivalent. The next section summarizes what's known.

## 2. Related work and theoretical frames

A literature review of 34 papers (Cloudy et al., 2021, 2022; Hong et al., 2024; Huh et al., 2025; Altay & Gilardi, 2024; Wang et al., 2025; Tafur & Sarkar, 2023; Zhao et al., 2025; Waddell, 2019; and others, full list in `sources.md`) identifies four theoretical frames that together describe why this design question matters.

**The machine heuristic.** Multiple experiments show that attributing news content or moderation to AI can *reduce* perceptions of hostile media bias. The proposed mechanism is the *machine heuristic*: audiences view machines as more objective and systematic than humans (Cloudy et al., 2022; Cloudy et al., 2021). Explicit attribution to an "AI journalist" and algorithmic fact-checking reduced perceived political bias, especially among readers with strong partisan attitudes (Chae & Tewksbury, 2024; Hong et al., 2024). For a tool that wants to make bias visible, this is a useful baseline finding — but it's also a warning, because it suggests users may be predisposed to *over-trust* an AI bias label.

**Algorithm aversion and trust degradation.** While some readers perceive AI-labeled content as less biased, others rate it as less trustworthy or accurate than human-authored content (Altay & Gilardi, 2024; Wang et al., 2025; Liu et al., 2023; Wischnewski & Krämer, 2024). Explicit "AI-generated" labeling consistently lowers perceived accuracy and willingness to share — even for true headlines — due to skepticism about full automation. However, *combining* human and algorithmic attribution can sometimes enhance credibility (Waddell, 2019). The implication for AI News Lens: how the bias label is framed (as algorithmic certainty? as algorithmic estimate? as one signal among several?) is itself a design choice with empirical consequences.

**Automation bias.** Tafur & Sarkar (2023) show that warnings from fake-news detection algorithms strongly influence user beliefs even when those warnings are *incorrect*. This is a real risk for any tool that assigns bias scores: users may treat a model's output as authoritative even when the model is wrong. The paper argues this implies AI News Lens needs to do more than show a score — it needs to surface the evidence (the quotes, the framing comparison) that lets users check the score themselves.

**Emotional override.** Zhao et al. (2025) show that emotionally charged stories elicit strong engagement and sharing regardless of AI labels. For a news tool focused on politically contentious topics — which are often the most emotionally charged — this is the theoretical frame that constrains all the others. A bias label may not save a reader from being persuaded by a story they're already emotionally invested in.

Together, these four frames make the research question more precise. Exposure to AI-detected bias *does* change how users perceive news, but the change is moderated by user attitudes toward AI, by the framing of the AI cue itself, by the emotional load of the content, and by the user's prior critical-thinking habits.

## 3. Method

The first build of AI News Lens implements the per-article bias-detection pillar. The build:

- Accepts a pasted article URL or text body.
- Returns a neutral summary generated via the Gemini API with a prompt that explicitly asks for a balanced description of the event.
- Returns an AI-detected bias score (left / center / right) with a short rationale.
- Surfaces two representative quotes from across the political spectrum that the model identifies as central to the article's framing.

For the paper-lite pilot reported here, the comparison is between two presentation modes for the same article:

- **Mode A — neutral summary only.** The reader sees the AI-generated neutral summary. No bias label, no quotes.
- **Mode B — neutral summary plus bias label and cross-spectrum quotes.** The reader sees the same neutral summary, then a per-article bias score with rationale, then two quotes from across the political spectrum.

A small framing table is used to compare what the reader notices in each mode:

| Category | Question |
|---|---|
| Shared facts | What appears in every version? |
| Word choice | Which labels or adjectives change? |
| Centered actor | Who becomes the main subject? |
| Main risk | What danger is emphasized? |
| Implied solution | What action seems most important? |

The pilot is small — three articles, two presentation modes, one reader (me) — and is meant as a design probe, not a controlled study.

## 4. Findings and discussion

The strongest pattern in the pilot is that **adding the bias label and cross-spectrum quotes pulled my attention toward what was missing from the neutral summary**. In Mode A, the neutral summary read as complete. In Mode B, the same summary read as a starting point, and the cross-spectrum quotes consistently surfaced framings — about who was responsible, about what the underlying cause was, about what action mattered most — that the neutral summary had smoothed over.

The finding is:

> In this small example, exposure to AI-detected bias and cross-spectrum quotes shifted *what felt missing* from the news summary. It did not shift the underlying facts.

This is consistent with the literature. The bias cue activated the kind of comparative reading that the machine-heuristic experiments describe — the reader treats the AI signal as a prompt to look more carefully. But it's also consistent with the algorithm-aversion literature: in two of the three test articles, the model's bias score felt over-confident relative to the underlying article, and I noticed myself wanting to second-guess it. That's the design tension the paper argues most matters.

The implication for the full four-pillar build: the bias label needs to be presented as one signal among several, the quotes need to do the work of letting the reader check the label, and the sentiment-collection pillar needs to ask readers what they noticed *after* reading the bias-aware version, not just whether they trusted it.

## 5. Limitations

This is an early-stage paper-lite. Three honest limitations.

First, the pilot is small. Three articles, two presentation modes, one reader. The patterns reported here are observations, not findings in the empirical sense. A real version would test 10-30 articles across different beats, with multiple readers, and would compare bias scores against an independent ground truth.

Second, only the bias-detection pillar of the four-pillar design is built. The neutral-summary, sentiment-collection, and journal pillars are designed but not implemented. Claims in this paper about how the full system works are claims about a planned build, not a finished one.

Third, the bias detection itself depends on Gemini's training biases. The lit review is explicit about this — algorithmic warnings can shift user beliefs even when the warnings are wrong (Tafur & Sarkar, 2023), and a model's bias detection inherits whatever biases were present in the model's training. A future version should test the bias detection against a corpus of articles with known framing characteristics, and should let users see *why* the model assigned the score it did, not just what the score was.

The paper does not claim that AI News Lens is unbiased, neutral, or a substitute for original-source reading. It claims that bias-aware presentation is a design space worth taking seriously, that the literature provides a real theoretical frame for it, and that a small first build suggests the comparative-reading move is the right design move to push on next.

## 6. Conclusion

Exposure to AI-detected bias changes how users perceive news — sometimes by reducing perceived hostility (the machine heuristic), sometimes by lowering trust in both true and false stories (algorithm aversion), sometimes by influencing belief regardless of accuracy (automation bias), and sometimes by being overridden entirely by emotional content (emotional override). The four-frame literature is what makes this a real research question rather than a vague design intuition.

AI News Lens is a small attempt to take the question seriously. The first build implements the per-article bias-detection pillar; the next sessions will build it out and test it more carefully. The most useful finding from the pilot is not that the tool changed how I read news. It's that the tool *prompted comparative reading* — pulling attention toward what was missing from the neutral summary — and that's the design move worth pushing on.

## Candidate references

The full Consensus-derived literature review is in `sources.md`. The papers below are the ones cited directly in this draft.

[1] [Hostile Media Perceptions in the Age of AI: Examining Machine Heuristic in News Algorithm Attribution](https://consensus.app/papers/details/) — Cloudy et al., 2022. *(Machine heuristic; AI attribution reduces hostile media bias perception.)*

[2] [Algorithmic Authority: Effects of AI Source Cues on News Perception](https://consensus.app/papers/details/) — Cloudy et al., 2021. *(Earlier machine-heuristic experiment with similar effect.)*

[3] [Mind perception of an AI agent and its effects on hostile media bias perceptions](https://consensus.app/papers/details/) — Hong et al., 2024. *(Extends machine heuristic to agentic AI.)*

[4] [How perceptions of AI moderate the relationship between bias and news perception](https://consensus.app/papers/details/) — Huh et al., 2025. *(Moderation by user attitudes toward AI.)*

[5] [Generative AI labelling reduces the perceived accuracy of online content](https://consensus.app/papers/details/) — Altay & Gilardi, 2024. *(Algorithm aversion; explicit AI labels reduce perceived accuracy.)*

[6] [The "AI-Generated" label and trust in news](https://consensus.app/papers/details/) — Wang et al., 2025. *(Algorithm aversion replication.)*

[7] [Algorithmic warnings shift user beliefs even when incorrect](https://consensus.app/papers/details/) — Tafur & Sarkar, 2023. *(Automation bias.)*

[8] [Emotional content and the override of source skepticism in AI-labeled news](https://consensus.app/papers/details/) — Zhao et al., 2025. *(Emotional override.)*

[9] [The Allure of Artificial Intelligence: How Source Bias and Authorship Cues Influence News Perceptions](https://consensus.app/papers/details/) — Waddell, 2019. *(Foundational source-cue study; human + AI attribution.)*

*Note: these references are abstract-checked via Consensus and need to be verified against title, authors, venue, and exact claim before final submission. The DOIs and full APA citations are in the Drive lit review and need to be migrated into `sources.md`.*

# Sources — AI News Lens

This sources file is built from the Consensus literature review you completed in Drive (34 papers, screened from an initial set of 50). Sources are organized by the four theoretical frames identified in that review. **All sources are abstract-checked via Consensus only.** Before any paper goes into the final submitted bibliography, verify the title, authors, venue, year, DOI, and the exact claim the paper supports.

The Drive lit review's full APA-style reference list (with DOIs) is the canonical version — these notes are the working subset for this paper.

## Frame 1 — Machine heuristic

The claim that audiences perceive AI-attributed content as more objective than human-attributed content, and the experimental evidence supporting that claim.

1. **Cloudy et al. (2022)** — *Hostile Media Perceptions in the Age of AI: Examining Machine Heuristic in News Algorithm Attribution*
   Foundational machine-heuristic experiment. AI attribution reduced perceived hostile media bias, especially among partisan readers. Cited as the central evidence for the machine-heuristic frame in `PAPER.md` section 2.

2. **Cloudy et al. (2021)** — Earlier machine-heuristic study with similar effect direction. Useful as a replication / robustness reference alongside the 2022 paper.

3. **Hong et al. (2024)** — *Mind perception of an AI agent and its effects on hostile media bias perceptions*
   Extends the machine heuristic to AI agents perceived as having agency. Relevant if AI News Lens's bias-label interface presents the model as agentic ("the AI thinks...") rather than as a tool.

4. **Huh et al. (2025)** — Moderation of the machine-heuristic effect by user attitudes toward AI. Skeptics benefit less from the debiasing effect. Important for the limitations discussion.

5. **Chae & Tewksbury (2024)** — *Algorithmic fact-checking and political bias perception*
   Algorithmic fact-checking reduces perceived political bias. Useful for grounding the bias-label-as-cue design choice.

## Frame 2 — Algorithm aversion and trust degradation

The countervailing finding that explicit AI labels can *lower* perceived accuracy and trustworthiness, especially for true headlines.

6. **Altay & Gilardi (2024)** — *Generative AI labelling reduces the perceived accuracy of online content*
   Explicit "AI-generated" labels lowered perceived accuracy across both true and false headlines. Robust effect across multiple experiments. The key counterweight to the machine-heuristic finding.

7. **Wang et al. (2025)** — Replication of the algorithm-aversion finding with a larger sample and different content domains. Useful for demonstrating the effect is not idiosyncratic.

8. **Liu et al. (2023)** — *AI-attributed news and credibility ratings*
   AI-authored content rated as less trustworthy than human-authored content. Relevant for the design choice about whether to label outputs as AI-produced.

9. **Wischnewski & Krämer (2024)** — Trust degradation under AI labels in a journalism context. Relevant for the journalistic-tool framing.

10. **Waddell (2019)** — *The Allure of Artificial Intelligence: How Source Bias and Authorship Cues Influence News Perceptions*
    Foundational source-cue paper. Combining human + algorithmic attribution can enhance credibility, more than either alone. Important for the design move of presenting the bias label alongside human-curated cross-spectrum quotes rather than as an autonomous algorithmic verdict.

## Frame 3 — Automation bias

The risk that algorithmic cues shift user beliefs even when the algorithm is wrong.

11. **Tafur & Sarkar (2023)** — *Algorithmic warnings and user belief shifts*
    Warnings from a fake-news detection algorithm strongly influenced user beliefs even when the warnings were incorrect. Most directly relevant cite for the automation-bias risk in AI News Lens's per-article bias scoring.

12. **Hanzhuo et al. (2024)** — Explicit labeling can backfire by reducing belief in accurate information without curbing belief in falsehoods. Important for the limitations discussion.

13. **Spearing et al. (2025)** — Pre-emptive inoculation interventions reduce general AI-info trust without diminishing specific misinformation influence unless combined with debunking. Useful background on intervention design.

## Frame 4 — Emotional override

The constraint that emotionally charged content elicits engagement regardless of source cues.

14. **Zhao et al. (2025)** — *Emotional content and the override of source skepticism*
    Engagement and sharing intentions remain high for emotionally charged stories even when they're labeled "AI-generated." The boundary condition that constrains all the other frames.

15. **Wang & Ophir (2024)** — Transparency about how algorithms work doesn't always enhance trust or reduce perceived bias unless users already endorse the machine heuristic. Useful for the section 5 discussion of why the bias label needs to be *paired* with verifiable evidence (the cross-spectrum quotes), not stand alone.

## Adjacent / supporting sources

These don't fit cleanly into the four frames but support specific claims in the paper.

16. **Horne et al. (2019)** — Frequent news readers benefit more from AI bias detection than heavy social-media users. Useful for the user-attitudes discussion.

17. **Shin et al. (2024)** — Recent work on AI-generated news bias measurement. Useful for the method section.

18. **Govers et al. (2025)** — Cross-cultural variation in AI-news perception. Cites a research gap the lit review identifies.

## Foundational research gaps (from the Drive lit review)

The Drive lit review identifies five gaps that this paper inherits and partially addresses:

| Gap | Status in this paper |
|---|---|
| Long-term behavioral impacts of repeated exposure | Acknowledged in limitations; not addressed |
| Cross-cultural differences | Acknowledged; not addressed |
| Optimal explanation strategies for non-experts | Partially addressed by the cross-spectrum-quotes design |
| Effects across factual vs. opinion content | Acknowledged; not addressed |
| Interaction between emotional resonance and source cues | Named in section 2; not empirically tested in this build |

The paper's claim is modest: the design probe is one small step toward the third gap. The other four are flagged for future work.

## Citation caution

These notes are abstract-checked only. For any paper that ends up cited in the final submission, verify:

- Title (Consensus sometimes truncates or auto-generates titles)
- Authors and order
- Venue and year
- DOI or stable URL
- The exact claim the paper supports — match against the abstract on Semantic Scholar or PubMed

The Drive lit review has the full APA-style references with DOIs. Migrating those into a final `references.md` (or into the paper's bibliography section directly) is part of the Week 8 work.

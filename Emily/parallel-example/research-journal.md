# Research Journal: Model UN News Lens

## Week 1 - Neutral summaries are not as neutral as they feel

I started with a simple idea: paste in a political news headline and ask an AI for a neutral summary. The output sounded balanced, but I noticed that "neutral" often meant "smooth." It removed conflict words, shortened the history, and made the issue sound less contested.

That is useful for a quick briefing, but Model UN work often depends on understanding why different countries or groups frame the same event differently.

Question raised: If a model claims to summarize neutrally, what perspective is hiding inside the summary?

## Week 2 - Perspective dropdown

This week I designed a perspective dropdown:

- Neutral briefing
- Humanitarian NGO
- National-security adviser
- Climate delegate
- Opposition party
- Youth delegate

I used the same news event and asked for a short summary from each perspective. The outputs did change. The humanitarian version emphasized civilian harm. The national-security version emphasized stability and risk. The youth delegate version emphasized future impact.

The surprise was that some perspectives changed tone more than facts. The model often kept the same basic content but changed adjectives and priorities.

## Week 3 - Source detour

Consensus searches on LLM news summarization and media bias helped me name the issue. The relevant concept is **framing**: what gets emphasized, softened, or omitted.

This shifted my question. I am not trying to build a perfectly unbiased summarizer. That may be impossible. I am trying to build a tool that makes perspective visible on purpose.

New research question:

> When an AI tool summarizes political news from different stated perspectives, how much does the framing actually change?

## Week 4 - What to measure

I created a simple comparison table:

- What facts appear in all versions?
- What words change?
- What actor is centered?
- What cause is emphasized?
- What solution is implied?

This worked better than asking "which summary is biased?" Bias is a difficult judgment. But inclusion, emphasis, and word choice are easier to compare.

One example: in a climate-disaster story, the climate delegate version used "adaptation" and "emissions," while the security version used "infrastructure" and "regional instability." The same event became part of different policy conversations.

## Week 5 - Ethical risk

The tool could help students prepare for debate or Model UN because it shows that perspective changes what people notice. But it could also teach students to manufacture slant.

That means the interface needs reflection questions:

- What changed between versions?
- Which summary feels most persuasive?
- Which facts disappeared?
- What would you need to verify from the original source?

The paper should argue that perspective-aware summarization is useful only if it trains skepticism, not just rhetorical control.

## Week 6 - Paper direction

The strongest claim is modest:

> In a small set of test summaries, perspective prompts changed emphasis and word choice more consistently than they changed core facts.

The limitation is that the test set is small and the scoring is subjective. A better project would use multiple news stories, human-coded framing categories, and comparison against real outlets or delegate statements.

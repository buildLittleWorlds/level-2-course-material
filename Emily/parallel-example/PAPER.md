# Model UN News Lens: Testing Perspective Prompts in AI Political News Summaries

## Abstract

This worked example studies how perspective prompts change AI-generated political news summaries. The imagined Hugging Face Space, Model UN News Lens, asks a model to summarize the same news event from different stated perspectives, such as a neutral briefing, humanitarian NGO, national-security adviser, climate delegate, opposition party, or youth delegate. The project asks whether these perspective settings change core facts or mostly change framing through emphasis, word choice, and implied priorities. A small paper-lite pilot suggests that perspective prompts often preserve the basic event while shifting which actors, risks, and solutions receive attention. The paper argues that this kind of tool could help students see framing in political communication, but only if it includes reflection and verification steps rather than pretending to produce perfectly neutral news.

## 1. Introduction and research question

Students studying international relations often need to understand how different actors describe the same event. A humanitarian organization, a government security office, and a youth climate delegate may all discuss the same crisis but emphasize different causes, harms, and responsibilities.

AI summarization tools can make news easier to process, but they may also hide framing choices behind fluent language. This project asks:

> When an AI tool summarizes political news from different stated perspectives, how much does the framing actually change?

The goal is not to create a perfectly unbiased news tool. The goal is to make framing visible enough that a student can compare perspectives critically.

## 2. Related work

Research on LLM news summarization suggests that political bias can appear in generated summaries, including through word choice [1]. Studies of AI-generated news content show broader concerns about bias in generated media [2]. Work on generated news corpora provides methods for quantifying differences between human-authored and machine-generated political news [3]. Research on framing bias detection also shows that models can struggle to distinguish framing from ordinary emotional or descriptive language [4]. Finally, work on bias in summarization emphasizes that measuring bias in summaries requires careful definitions and controlled comparisons [5].

These sources support the paper's basic caution: summarization is not just compression. It can also reshape emphasis.

## 3. Method

The imagined Space takes one news event and generates short summaries from several perspectives:

- Neutral briefing
- Humanitarian NGO
- National-security adviser
- Climate delegate
- Opposition party
- Youth delegate

The pilot compares outputs using a simple framing table:

| Category | Question |
|---|---|
| Shared facts | What appears in every version? |
| Word choice | Which labels or adjectives change? |
| Centered actor | Who becomes the main subject? |
| Main risk | What danger is emphasized? |
| Implied solution | What action seems most important? |

This method avoids asking only whether a summary is "biased." Instead, it asks what changed.

## 4. Findings and discussion

The strongest pattern is that perspective prompts changed emphasis more reliably than core facts. In a climate-disaster example, most summaries preserved the same basic event: flooding, displacement, and government response. But the framing shifted.

The humanitarian NGO version centered civilians and relief access. The national-security version centered infrastructure and regional instability. The climate delegate version centered emissions, adaptation, and long-term responsibility. The youth delegate version emphasized future impact and intergenerational fairness.

The finding is:

> In this small example, perspective prompting did not completely rewrite the facts, but it changed which facts seemed most important.

That is useful for Model UN preparation because delegates must understand how arguments are framed. It is also risky because the same tool could be used to make slanted summaries sound natural. For that reason, the Space should include reflection prompts and remind users to compare against the original article.

## 5. Limitations

This is an early-stage paper-lite example. It uses a small number of news events and hand-coded framing categories. The examples do not prove that one model is biased or unbiased. They only show that perspective prompts can shift outputs in ways worth analyzing.

The project also depends on the original article. If the article itself is biased, every generated summary inherits that starting point. A stronger version would test multiple news sources covering the same event and compare generated summaries against human-written source coverage.

Finally, political perspective is more complex than a dropdown menu. Real diplomatic positions depend on history, incentives, alliances, domestic politics, and law. The Space can teach framing awareness, but it cannot replace actual country research.

## 6. Conclusion

Model UN News Lens turns a news summarization tool into a research question about framing. The most useful result is not a single "best" summary. It is the comparison between summaries. When students see what changes across perspectives, they can ask better questions: What was emphasized? What was left out? Who benefited from this wording? That makes the tool valuable as a critical-reading aid, as long as it is paired with source verification and skepticism.

## Candidate references

[1] [Political Bias of Large Language Models in Few-Shot News Summarization](https://consensus.app/papers/details/4f82187cb0de5b5eb8c272c135e312bf/?utm_source=chatgpt). Takeshi Onishi and James Caverlee, 2024, venue not listed in Consensus output, citation count: 1.

[2] [Bias of AI-generated content: an examination of news produced by large language models](https://consensus.app/papers/details/0f7771ac19cf5827af0542a601a11172/?utm_source=chatgpt). Xiao Fang, Shangkun Che, Minjia Mao, Hongzhe Zhang, Ming Zhao, and Xiaohang Zhao, 2023, *Scientific Reports*, citation count: 121.

[3] [Quantifying Generative Media Bias with a Corpus of Real-world and Generated News Articles](https://consensus.app/papers/details/86da550116e6521fbf5f10a9304fa3a9/?utm_source=chatgpt). Filip Trhlik and Pontus Stenetorp, 2024, venue not listed in Consensus output, citation count: 10.

[4] [Decoding News Narratives: A Critical Analysis of Large Language Models in Framing Bias Detection](https://consensus.app/papers/details/15885d296c655d6cb30d50bbc2feefea/?utm_source=chatgpt). Valeria Pastorino, Jasivan Sivakumar, and N. Moosavi, 2024, *arXiv*, citation count: 3.

[5] [Bias in News Summarization: Measures, Pitfalls and Corpora](https://consensus.app/papers/details/f0555e874ac85a0da6d7cbd3578072bc/?utm_source=chatgpt). Julius Steen and Katja Markert, 2023, venue not listed in Consensus output, citation count: 11.

# External Validity / Generalization

Session 6 Research Method

## What It Is

External validity asks whether your results hold up outside the specific conditions you tested in. A model might ace every test you give it — but if those tests all come from the same kind of data it was trained on, you haven't learned much. Generalization means taking a tool that works in one context and seeing whether it works in another. The failures are the most informative part.

## When Researchers Use It

- A psychologist runs a study on college freshmen and finds that people make riskier decisions when they're hungry. But do the results generalize? Would the same thing happen with 60-year-olds, or with people in a different country, or outside a lab? If the finding only works with college freshmen in a university setting, it has low external validity.
- A novelist writes dialogue that sounds natural in a contemporary New York setting. She shares the manuscript with a friend in rural Mississippi, who says, "Nobody here talks like that." The dialogue was valid for one world but doesn't generalize to another.
- An engineer designs a bridge that handles traffic loads perfectly in computer simulations. Then winter hits — ice, wind, temperature swings. The simulation didn't include those conditions. The design had internal validity (it worked in the test) but low external validity (it failed in the real world).

## How to Apply It

1. **Identify the training domain.** Read the model card. What kind of data was this model trained on? Movie reviews? Tweets? Product listings? Medical records? That's the model's "home turf."
2. **Pick a different domain.** Choose text (or images, or audio — whatever your model processes) from a completely different context. If the model was trained on tweets, test it on poetry. If it was trained on English, test it on Spanish. If it was trained on product reviews, test it on legal documents.
3. **Compare home vs. away.** Run the same model on home-domain data and away-domain data. Where does performance drop? What specific kinds of inputs cause the biggest failures? The gap between home and away performance is the domain shift.

## Key Vocabulary

- **External validity** — Whether results hold up outside the original test conditions. A finding with high external validity generalizes broadly; one with low external validity only works in specific circumstances.
- **Generalization** — A model's ability to perform well on data it wasn't trained on. The opposite of memorization.
- **Domain shift** — What happens when the data a model encounters in the real world is different from its training data. The model didn't get dumber — the world changed around it.
- **Overfitting** — When a model gets so good at its training data that it can't handle anything else. Like studying only one teacher's tests — you ace theirs and bomb everyone else's.

## This Week's Shared Example

In class, we took the three sentiment models from Session 4 and ran them through a "Domain Safari" — testing them on news articles, poetry, legal text, medical notes, song lyrics, memes, and more. The models that worked perfectly on their home turf struggled in unfamiliar domains. The movie-review model had no "neutral" option for factual news. The Twitter model choked on formal legal language. The product-review model didn't know what to do with a Shakespeare sonnet. Same models, same weights — different worlds, different results.

## Apply It to Your Own Topic

- Pick a model from your Collection and identify its training domain (check the model card).
- Now find data from a domain the model has never seen. If your model does translation, try feeding it slang or poetry instead of textbook sentences. If your model classifies images, try drawings or memes instead of photos. If it summarizes text, try giving it dialogue or song lyrics.
- Run the model on its home domain first — confirm it works as expected. Then run it on the away domain. How much does performance drop?
- Can you predict which away domains will be hardest based on how different they are from the training data?
- Is the failure total (the model is useless outside its domain) or partial (it gets the gist but misses nuance)? That distinction matters for deciding whether the model is safe to use in a new context.

See `GUIDE-research-journal.md` for how to structure your domain-testing experiment as a journal entry.

## Explore the Training Data

The reason models fail on unfamiliar text is that they've only ever seen one "world." Browsing domain-specific datasets makes this concrete — you can see how differently the same word ("positive," "strong," "growth") is used in finance vs. poetry vs. product reviews. No code required — open the dataset page and click the viewer.

- **[takala/financial_phrasebank](https://hf.co/datasets/takala/financial_phrasebank)** — Nearly 5,000 financial news sentences labeled positive, negative, or neutral by finance experts. "Revenue increased 5%" is positive here — but a movie-review model has no idea what revenue means. Browse the rows and notice how different "positive" sounds when money is involved.
- **[google-research-datasets/poem_sentiment](https://hf.co/datasets/google-research-datasets/poem_sentiment)** — Sentiment labels on poem verses from Project Gutenberg. "Shall I compare thee to a summer's day?" gets a label here — but is a sentiment label really the right tool for understanding a poem? Browse the dataset and see if you agree with the labels.
- **[zeroshot/twitter-financial-news-sentiment](https://hf.co/datasets/zeroshot/twitter-financial-news-sentiment)** — Finance tweets labeled for sentiment. This dataset lives in two domains at once: social media language AND financial jargon. A model trained on movie reviews would struggle with both layers.

Same word, different world. That's domain shift in three datasets.

---

AI + Research Level 2 • Session 6: Same Space, Different Worlds

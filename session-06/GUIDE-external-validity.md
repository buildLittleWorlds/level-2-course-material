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

In class, we took the generative models from Session 5 — the text generator and the summarizer — and tested them outside their training domains. We built a domain-adapted text generator with prompt presets for game dialogue, medical notes, news articles, and poetry. The same model (distilgpt2, trained on web text) produced decent game-style text but struggled with clinical language and poetry. We also tested the summarizer (trained on CNN/DailyMail news) on poetry, legal text, and medical notes — it worked well on news but lost meaning on everything else. Same models, same weights — different worlds, different results.

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

## Apply It to Your Project — Personal Starter Prompts

The "Apply It to Your Own Topic" section above gives the general method. Here's a more specific starting point based on the work you've been doing so far. Find your name and use the prompt as a jumping-off point.

**Annabelle** — Your spaces produce playful, creative text (dino facts, silly phrases). That content is its own domain — informal, quirky, humorous. Test what happens when you feed that kind of text to a model trained on formal writing, or when you give a formal model a creative task. Where does the mismatch show up? Your collection annotations already track what works and what doesn't — this week, try to explain *why* something doesn't work by tracing it back to training data.

**Bobby** — Game writing is a domain most NLP models have never seen. Your Brackeys Game Jam project and "One Last Bird" concept give you authentic test material. Try the text generator with game dialogue prompts and see where it sounds natural vs. where it falls apart. Then check the model card — what was distilgpt2 actually trained on? Can you trace the failures back to missing training data?

**Chengry** — Medical text is the most consequential domain shift example in this class. "Patient tested negative for infection" is good news, but a model trained on web text reads "negative" as bad. Test the text generator and summarizer on clinical text and document exactly where and why they fail. You also now have `d4data/biomedical-ner-all` as a specialist model. Test its external validity: does it extract entities correctly from patient-facing health text (simpler language) as well as it does from clinical notes? Does it find false entities in non-medical text? That boundary — where the specialist stops being reliable — is external validity for a domain-specific model. Then connect it to DxAI: your Claude API approach (Path B, the generalist) handles domain shift differently than the NER model (Path A, the specialist). How do their failure modes differ?

**Emily** — Your curated tools are domain-specific: news recommendation works on news, summarization works on articles. Pick one and test it outside its domain. Give a news tool poetry, or give a summarizer a text message conversation. The gap between "works on news" and "works on everything" is the external validity question — and it's directly relevant to whether information management tools are useful in practice.

**George** — Medical language is full of words that mean different things in different domains. "Positive" in medicine means something was detected (often bad); "positive" in everyday language means something is good. "Critical" in medicine means life-threatening; "critical" in a review means disapproving. Test the text generator and summarizer on medical text with these double-meaning words and write about what you find. This is the core challenge facing any medical AI tool.

**Henry** — You have interests in two domains: computer vision and NLP. That's an advantage this week. Test the News Sentiment Analysis space on non-news text (poetry, lyrics, code comments). Then think about the visual equivalent: what happens when the camera angles LoRA gets an image from outside its training domain? Even if you can't test the image model directly, reasoning about where it would fail is valuable practice in thinking about external validity.

**Sevilla** — You've already found domain shift: BLIP models failing on cartoonish images, emotion detectors missing sarcasm. This week, name those findings using the vocabulary from class (overfitting, domain shift, external validity). Your Week 2 entry documented *what* happened; this week's entry can explain *why* using the conceptual framework from tonight. Try testing your emotion tools on text from very different emotional registers — a legal contract, a children's book, a medical report — and compare results.

**Shawn** — Your comparative methodology already tests across models. This week, test across *domains* within a single model. Pick one image generator from your collection, identify its training data from the model card, then give it prompts from increasingly distant domains. Realistic photo → illustration → abstract concept → something totally outside visual language (like "the feeling of forgetting something important"). Where does the model's world end? That boundary is what domain shift looks like in image generation.

---

AI + Research Level 2 • Session 6: Model Evaluation and Generalization

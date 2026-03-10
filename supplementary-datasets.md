# Supplementary Datasets for Sentiment Course

Curated datasets from Hugging Face that support the Level 2 course sessions. All are browseable in the HF dataset viewer without code.

---

## Tier 1: Foundational (Training data behind the models students use)

### stanfordnlp/sst2
- **URL:** https://hf.co/datasets/stanfordnlp/sst2
- **What:** Stanford Sentiment Treebank. Movie review sentences, POSITIVE/NEGATIVE. The dataset behind `distilbert-base-uncased-finetuned-sst-2-english` (the binary model in Sessions 1-4).
- **Size:** ~67K sentences
- **Downloads:** 1.4M
- **Session fit:** S02 (training data & representation), S04 (model evaluation). Show students the actual rows the model learned from. "If this is all the model ever read, what can't it understand?"

### SetFit/sst5
- **URL:** https://hf.co/datasets/SetFit/sst5
- **What:** 5-label version of SST (very negative, negative, neutral, positive, very positive). Same source text as SST-2 but finer-grained.
- **Size:** ~11K sentences
- **Downloads:** 392K
- **Session fit:** S02. Show SST-2 vs SST-5 side by side — same sentences, different label schemes. "Who decided there are only 2 feelings vs 5?"

### dair-ai/emotion
- **URL:** https://hf.co/datasets/dair-ai/emotion
- **What:** English Twitter messages labeled with 6 emotions: anger, fear, joy, love, sadness, surprise. Behind models like `j-hartmann/emotion-english-distilroberta-base` (the 7-emotion model students use).
- **Size:** ~20K tweets
- **Downloads:** 665K | **Likes:** 430
- **Session fit:** S02. "The emotion model knows 6 feelings because someone labeled 20K tweets into exactly these 6 buckets. What feelings are missing?"

### google-research-datasets/go_emotions
- **URL:** https://hf.co/datasets/google-research-datasets/go_emotions
- **What:** 58K Reddit comments labeled for 27 emotion categories or Neutral. Google Research. Multi-label (a comment can be both "amusement" and "approval").
- **Size:** 58K comments
- **Downloads:** 389K | **Likes:** 251
- **Session fit:** S02 or S06. Contrast with dair-ai/emotion: 6 labels from Twitter vs 27 labels from Reddit. Same task, completely different representation.

### cardiffnlp/tweet_eval
- **URL:** https://hf.co/datasets/cardiffnlp/tweet_eval
- **What:** 7 Twitter classification tasks in one dataset: sentiment, emotion, irony, hate, offensive, stance, emoji. Behind `cardiffnlp/twitter-roberta-base-sentiment-latest` (Session 4's Twitter model).
- **Size:** varies per subset (total 100K+)
- **Downloads:** 2.5M
- **Session fit:** S03 (irony subset), S04 (sentiment subset = training data for Twitter model), S07 (hate/offensive subsets show how bias detection datasets are built).

---

## Tier 2: Domain-Specific (Great for Session 6 — Domain Shift)

### takala/financial_phrasebank
- **URL:** https://hf.co/datasets/takala/financial_phrasebank
- **What:** ~4,800 financial news sentences labeled positive/negative/neutral from an investor's perspective. "Revenue increased 5%" is positive here but meaningless in a movie review context. Annotated by 16 finance experts with agreement levels tracked.
- **Size:** 4,840 sentences
- **Downloads:** 571K | **Likes:** 248
- **Session fit:** S06. Run a movie-review-trained model on financial sentences. Watch it fail. "If we retrained on this data, would the model understand Wall Street?"

### google-research-datasets/poem_sentiment
- **URL:** https://hf.co/datasets/google-research-datasets/poem_sentiment
- **What:** Sentiment labels on poem verses from Project Gutenberg. Literary language classified for sentiment.
- **Size:** ~1K verses
- **Downloads:** 678
- **Session fit:** S06. Run Showdown models on poetry. "Shall I compare thee to a summer's day?" gets POSITIVE — but is that really what the poem means? Connects to S06 Big Question.

### zeroshot/twitter-financial-news-sentiment
- **URL:** https://hf.co/datasets/zeroshot/twitter-financial-news-sentiment
- **What:** Finance-related tweets labeled for sentiment. Tweets about stocks, crypto, markets.
- **Size:** ~12K tweets
- **Downloads:** 5.1K | **Likes:** 164
- **Session fit:** S06. Crosses two domains — tweets (social media language) about finance (specialist domain).

---

## Tier 3: Contrast & Discussion

### cornell-movie-review-data/rotten_tomatoes
- **URL:** https://hf.co/datasets/cornell-movie-review-data/rotten_tomatoes
- **What:** 5,331 positive + 5,331 negative Rotten Tomatoes review sentences. Classic, clean, perfectly balanced.
- **Downloads:** 2.6M
- **Session fit:** S04. Show how clean training data produces a confident model that's confused by everything else.

### stanfordnlp/imdb
- **URL:** https://hf.co/datasets/stanfordnlp/imdb
- **What:** 25K positive + 25K negative movie reviews. Full paragraphs, not single sentences.
- **Downloads:** 8.4M (most downloaded sentiment dataset on HF)
- **Session fit:** S04 or S06. Contrast with SST-2: same domain but full reviews vs single sentences. Does length matter for sentiment?

### fancyzhx/amazon_polarity
- **URL:** https://hf.co/datasets/fancyzhx/amazon_polarity
- **What:** ~35 million Amazon reviews with binary polarity. Massive scale. Product reviews are the domain of `nlptown/bert-base-multilingual-uncased-sentiment` (Session 4's 5-star model).
- **Downloads:** 896K
- **Session fit:** S06 or S09. For S09, product reviews are the exact context of the restaurant review redesign.

### Yelp/yelp_review_full
- **URL:** https://hf.co/datasets/Yelp/yelp_review_full
- **What:** Yelp reviews with 1-5 star ratings.
- **Downloads:** 5.1M
- **Session fit:** S09 (restaurant review analyzer redesign). The actual kind of data the redesigned tool would process.

### Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data
- **URL:** https://hf.co/datasets/Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data
- **What:** 1,500 YouTube comments classified as nostalgic vs non-nostalgic.
- **Downloads:** 230
- **Session fit:** S02. "Nostalgia" isn't in any standard emotion model. Shows someone who cared about a feeling the big models ignore. Great for "who decided there are 6 emotions?" discussion.

---

## Quick Reference: Datasets by Session

| Session | Datasets | Teaching Moment |
|---------|----------|-----------------|
| 02 | sst2, sst5, dair-ai/emotion, go_emotions, nostalgic YouTube | "Here's what each model actually learned from. 2 labels vs 6 vs 27." |
| 03 | tweet_eval (irony subset) | "Someone built a whole dataset just for sarcasm detection." |
| 04 | sst2, rotten_tomatoes, imdb | "Three movie review datasets — different sizes, lengths, sources. Same task." |
| 05 | sst5 | "SST has a 5-point scale. What if sentiment were a number, not a label?" |
| 06 | financial_phrasebank, poem_sentiment, twitter-financial-news | "Same word, different world. 'Positive' means profit here and beauty there." |
| 07 | tweet_eval (hate/offensive subsets) | "How do you build a bias detection dataset? Someone had to label these." |
| 09 | yelp_review_full, amazon_polarity | "This is the real data your tool would process." |

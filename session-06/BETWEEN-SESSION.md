# Between Sessions 6 & 7

This week's homework has three parts: a challenge using your Collection, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total.

---

## Part 1: Hub Challenge — Test Across Domains

In class we did **cross-domain testing** — taking models trained on one type of data and testing them on completely different types. That's how you test **generalization** and **external validity** — does the model actually work outside its training world?

Now apply that same method to **your own interest**.

### Option A: Stay with Sentiment

1. Open your Sentiment Showdown Space (your duplicate from Session 4)
2. Find **2-3 new domains** we didn't test in class — try text from a world the models have definitely never seen (fan fiction, video game dialogue, a recipe, a religious text, sports commentary)
3. For each domain, note: which model handles it best? Which falls apart? Why?
4. **Bonus:** Search https://huggingface.co/models for a sentiment model trained on the domain where your models failed. Can you find one? Add it to your Collection with a tasting note explaining what domain it was trained on
5. **Update your Collection** with any new models you found

### Option B: Explore Your Own Topic

1. Pick a model or Space from your Collection
2. Find out what it was trained on — check the model card, the README, or the dataset description
3. Test it on **data from a different domain** than its training data. For example:
   - Image classifier trained on photos → test with drawings, paintings, or screenshots
   - Translation model trained on news → test with slang, poetry, or song lyrics
   - Text model trained on English → test with code-switched text or dialect
4. Document what happens: does it generalize, or does it break?
5. **Update your Collection** — add a tasting note describing the domain shift you found

The key idea is the same either way: **a model's training data defines its world, and the real world is bigger than any training set.** You saw it with sentiment tonight. Now test it with whatever topic you're exploring.

### What to Notice

- Does the model fail gracefully (lower confidence) or confidently get it wrong?
- Is there a pattern in what kinds of inputs break it?
- Could you predict the failure from the model card alone?

### Bring It Back

Next session, be ready to share: what domain did you test, and what did the model miss? Your domain-shift findings set up the next problem — what happens when the solution to domain shift (training on everything) brings its own costs.

### Looking Ahead

**Optional deeper reading:** The `bonus-bert-content-moderation` module explains how BERT was trained, why pretraining + fine-tuning was a breakthrough, and how Twitter used BERT-style models for content moderation. It bridges the domain-shift problem from this session into Session 7's topic: bias. If you're curious about the breakthrough we discussed at the end of class, start there.

---

## Part 2: Research Journal Entry

Add your Week 6 entry to `research-journal.md` in your GitHub repo. Same format as last week — 300-500 words.

### Week 6 Entry

```markdown
## Week 6 — Same Space, Different Worlds

### This Week's Method
(What research method did we learn? Hint: cross-domain testing — taking a model out of its training domain to see if it generalizes.)

### How I Applied It
(What model or Space did you test? What was its original training domain? What new domain did you test it on?)

### What I Expected
(Before testing — did you think the model would handle the new domain? Why or why not?)

### What I Found
(What actually happened? Did it generalize or fail? Were the failures obvious or subtle?)

### Why I Think This Happened
(Your explanation. Connect it to the training data — what did the model learn, and what was missing from its world?)

### Limitations
(What domains couldn't you test? Would a different model trained on different data handle it better?)

### What I Want to Try Next
(Is your topic coming into focus? What question keeps pulling you back?)
```

If you're not sure what to write, start with: what was the model trained on, what did I give it instead, and what broke? That's the core of domain shift.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **8 models and 5 Spaces** by Session 7. For new items, include tasting notes — especially note what domain each model was trained on and whether you've tested it outside that domain.

### Notebook

Finish the experiments in the Session 6 notebook:
- Test at least 2 more domains of your own choosing
- Fill in the observation table for Experiment 3
- Write your observations in the "My Observations" markdown cell (double-click to edit)

### SpaceCraft Resource

This week you learned **External Validity** — testing whether a model works outside the domain it was trained on. SpaceCraft has a dedicated page for this method with steps, examples on OCR and translation Spaces, and an exercise: [External Validity method card](https://buildlittleworlds.github.io/spaceCraft/methods/external-validity.html)

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 6 entry below the Week 5 entry, and commit

---

## Your Personal Challenge

The homework above applies to everyone. Below is a challenge tailored to **your** specific project and interests — a way to connect this week's method (cross-domain testing / external validity) to the work you're already building.

---

### Annabelle

Your spaces live in playful, quirky territory — dino facts, silly phrases, creative randomness. That's a domain. Most sentiment and classification models were trained on formal text: reviews, news, tweets. Your kind of content is outside their world.

**Your challenge:** Take a few of the silly phrases or dino facts from your own spaces and paste them into the Sentiment Showdown. Do the models read the tone correctly, or do they treat playful text like something else entirely? Then try it the other way: find a model from your collection and give it an input from a completely different domain than what it was designed for. Write about what you find — it would connect beautifully to the evaluative annotations you're already putting in your collections. You already know how to notice when a tool doesn't work the way you expected; this week, you're learning *why*.

---

### Bobby

Your game development work gives you a unique angle on domain shift. Game narrative text — with its own vocabulary, pacing, and tone — is a world most NLP models have never been trained on. You know what game writing actually sounds like, which means you can spot when a model is misreading it.

**Your challenge:** Write a few lines of game dialogue or narrative from your Chickens Nightmare project (or invent something in the style of "One Last Bird") and run them through the Sentiment Showdown. Compare: how does a model trained on movie reviews interpret game writing versus how a model trained on tweets handles it? Then check the model cards — can you trace the failure back to the training data? This is exactly the kind of cross-domain testing researchers do, and your game dev background gives you test material nobody else in the class has.

---

### Chengry

Medical text is literally one of the domains we tested tonight. Your entire project — DxAI — lives at the frontier of this problem: general-purpose models being asked to handle specialized medical language. You saw it in class; now test it with your own material.

**Your challenge:** Take sample medical text — symptom descriptions, clinical notes, patient-facing health advice — and run it through the Sentiment Showdown. Notice how "Patient tested negative" reads as bad news to a sentiment model but is actually good news. That's the domain shift problem your DxAI tool has to solve. Write about what breaks and why. Your journal entry on the SHIFT framework already shows you think carefully about how presentation and context shape meaning — this is the model-level version of that same insight. If you want to go deeper: search the Hub for a sentiment model specifically trained on medical or biomedical text and compare it to the general-purpose models.

---

### Emily

Your collection focuses on news and information management tools — Newsify AI, News Recommendation System, AI Deadlines. Each of those is built for a specific domain of text. Tonight's session is about what happens when tools meet text from outside their training world.

**Your challenge:** Pick one of the spaces in your collection (the News Recommendation System or Newsify AI) and try giving it text from a domain it probably wasn't designed for — a poem, a text message, a product review, song lyrics. Does it still work? Does it fail gracefully or confidently get it wrong? Write about what you find. This is a generalization test, and it would make a strong first journal entry. You've already shown good instincts for curating tools that do specific things well — this week is about discovering where those tools' worlds end.

---

### George

Like Chengry, your interest in medical AI puts you at the center of tonight's topic. Medical text is one of the hardest domains for general-purpose models. Words like "acute," "positive," "negative," and "critical" mean very different things in medicine versus everyday language.

**Your challenge:** Write a few sentences the way a doctor might — a patient note, an injury report, a prescription description — and paste them into the Sentiment Showdown. See what the models get wrong. Then write about it: what did the models miss, and why? Think about what kind of training data a medical AI tool actually needs to handle that language correctly. That's the core design question behind the Injury Prediction System and Medicine Prescription Gen tools in your collection. Even a short paragraph about this would be a great first journal entry — and it ties directly into the breakthrough we discussed at the end of class about why training on everything (not just one domain) was necessary.

---

### Henry

Your collection spans two different domains: computer vision (Qwen Image Edit, camera angles LoRA) and NLP (News Sentiment Analysis). That split is actually tonight's topic — what happens when a model is asked to work outside its training domain.

**Your challenge:** Take the News Sentiment Analysis space from your collection and give it text from a completely different domain — song lyrics, a recipe, a game review, a legal clause. Does it still work? Then think about your image models: the Qwen Camera Angles LoRA was trained on specific types of images. What would happen if you gave it a painting, a medical scan, or a hand-drawn sketch? That's the visual version of domain shift. Write about either experiment (or both) — this would be a great way to start populating your GitHub repo, and it connects your two interests through the shared concept of domain shift.

---

### Sevilla

You've already discovered domain shift in the wild. Your finding that BLIP-based models struggle with cartoonish and hand-drawn images — that's exactly what we named tonight. The models were trained on photographs, not drawings. Different domain, different results.

**Your challenge:** You also noted that emotion models struggle with sarcasm and hidden messages. That's another kind of domain shift — sarcastic language operates by different rules than literal language, and models trained on literal text get confused. Write a journal entry that connects your emotion detection findings to tonight's domain shift concept. You're further along on this idea than you might realize — your Week 2 entry is already halfway there. If you want to push further: find emotionally complex text (poetry, song lyrics, sarcastic tweets) and run it through both the Sentiment Showdown and your emotion detection tools. Where do they agree? Where do they diverge?

---

### Shawn

Your finding that "all models struggled with highly conceptual/complicated prompts" is a domain shift observation. Abstract concepts — things you can imagine but can't photograph — are outside the training domain of models trained primarily on captioned images of real objects. Tonight we explored that same pattern with text.

**Your challenge:** Try a cross-modal thought experiment. Take the prompts that broke your image generation models (the highly conceptual ones) and paste them into the Sentiment Showdown. Do the text models also struggle with abstract, conceptual language? Write about the parallel. You could also search the Hub for image models specifically trained on artistic or abstract content (look for models fine-tuned on illustration datasets or concept art) and compare their performance on your tricky prompts against the general-purpose models. Your comparative methodology — structured testing, connecting results to training data and architecture — is exactly the right approach for this kind of cross-domain analysis.

---

AI + Research Level 2 • Session 6: Same Space, Different Worlds

# Session 6: Model Evaluation and Generalization
*Student-Facing Title: "Same Space, Different Worlds"*

## Concept: OVERFITTING AND DOMAIN SHIFT

**Space:** Reuses Session 4 Sentiment Showdown (no new build this session)
**Key Idea:** Models trained on one type of text struggle with another type. The "world" the model learned from shapes what it can understand.
**Narrative Role:** The wall that classification couldn't get past — and the breakthrough that solved it. This is the pivot point of Act II.

---

## Design Note: The "Build Together" Restructure (Session 6)

Session 6 has no new Space to build, which makes it the ideal session to expand the Build Together time. The Domain Safari is compressed from 35 to 20 minutes (4 domains instead of 6+). The Pattern Recognition and Student Challenge sections are merged into one 12-minute block (they overlap heavily — both are "test domains and notice what breaks"). This frees up 30 minutes for portfolio work.

**Session 6 Build Together focus is different from Session 5.** Last session was about getting infrastructure in place (GitHub repo, first journal entry, Collection started). This session is about:
1. Getting every student to a working Space (debugging broken ones, duplicating the Text Playground for students who haven't built one yet)
2. A second journal entry (the habit starts forming with repetition)
3. Peer sharing — students see each other's work for the first time

**By the end of Session 6, every student should have:** a GitHub repo with 2 journal entries, a Hugging Face Collection with 6+ items, and at least one working Space — even if it's a customized duplicate. That's the foundation Sessions 7-12 build on.

---

## Time Breakdown (2 hours)

### 0:00–0:08 — Show-and-Tell + Story So Far

Ask: "What settings recipes did you find? What worked best for what task?"
Quick share of between-session experiments from the Text Playground.

**Portfolio check-in (new — 2 min):** "Quick show of hands — who committed their journal entry this week? Who added to their Collection? No judgment either way — we'll have more time to work on those tonight."

**Narrative bridge (2 min — don't skip this):**

"Last week we added controls to our generator — temperature, top-p, max length. You now know the same knobs that developers set on ChatGPT and Claude. But I ended last session with a question: what happens when you ask a model about something it's never seen? What if you feed medical text to a model trained on Reddit? What if you ask it about legal contracts when it's only read blog posts?"

"Every model we've seen so far — the classifiers from Sessions 1–3, the generator from Sessions 4–5 — they all share the same limitation. They only know what they were trained on. Tonight we hit that wall."

### 0:08–0:11 — SpaceCraft Check-In

Pull up SpaceCraft briefly. Show a CPU-only Space you tested outside its training domain — for example, one of the OCR Spaces on the leaderboard tested with handwritten text, or a translation Space tested with slang.

Say: "I found this on SpaceCraft this week. It works great on what it was trained on. But watch what happens when I give it something from a completely different world — that's domain shift, and that's what we're investigating tonight. Look at the leaderboard's CPU-trick tags: the Spaces that use small specialized models are the ones most vulnerable to this, because specialization means narrow training data."

> **SpaceCraft textbook link for this session:** [Chapter 3: GPU vs CPU](https://buildlittleworlds.github.io/spaceCraft/gpu-vs-cpu.html) — the "Choose Small, Specialized Models" section explains why these models are CPU-friendly but also why they're vulnerable to domain shift.

### 0:11–0:20 — Big Question: Is "Positive" the Same Thing Everywhere?

*(Compressed from 12 to 9 min. Keep the two live demos and the core push questions. The point lands fast with this group.)*

**Do this live:** Open the Session 4 Sentiment Showdown Space. Paste these two inputs one at a time:

> "This phone is great."

Run it. All three models will likely say POSITIVE with high confidence.

> "Shall I compare thee to a summer's day?"

Run it. The models will probably say POSITIVE again — maybe with slightly different confidence.

**Ask:** "Both got POSITIVE. Are they the same kind of positive?"

**Push further:**
- "The model gives both sentences the same label. But 'This phone is great' and 'Shall I compare thee to a summer's day?' are completely different kinds of positive. One is about a product. The other is about love."
- "A product review and a love poem exist in completely different domains. The word 'great' means something different in each. Is the model reading the same thing in both?"

**Don't resolve this.** The Domain Safari will bring the question to life with concrete examples.

### 0:20–0:23 — The Hook: "Same Models, Different Worlds"

- Open the Session 4 Sentiment Showdown Space (or have students open their own duplicates from Session 4).
- Say: "These three models haven't changed. Same weights, same training. But today we're going to give them text they've never seen before — from worlds they were never trained on."
- Quick reminder of what each model was trained on:
  - Movie reviews
  - Tweets
  - Product reviews
- Ask: "If the movie-review model has only ever read movie reviews, what happens when we give it a poem?"

### 0:23–0:43 — Domain Safari (20 minutes)

*(Compressed from 35 min. Four domains instead of 6+. Pick the four that generate the best discussion — the rest are available in the pre-prepared samples below if you want more.)*

Paste pre-prepared texts from different domains (see full list below). For each one:

1. **Before pasting:** Ask students to predict — "Which model will handle this best? Will any of them get it right?"
2. **Paste and observe:** Run the text through all three models.
3. **After results:** "Were you right? What surprised you?"

**Recommended four domains (5 min each):**

1. **Song lyrics** — the upbeat-with-dark-lyrics sample is the strongest. "Dancing on the ceiling, burning down the walls, laughing at the wreckage as the empire falls." Models read surface words, miss the meaning. Students get this immediately.

2. **Medical notes** — "Patient presents with acute onset of substernal chest pain." Clinical language with no sentiment. Models forced to output something. Connects to George and Chengry's interests.

3. **Text messages** — "lol ok sure whatever u say 🙄" Perfect for teenagers. Sarcasm, emoji, context-dependence. The Twitter model might get closer but still miss the tone.

4. **Legal text OR code comments** — pick one based on energy. Legal text shows neutral-domain failure. Code comments ("HACK: This is a terrible workaround") show that sentiment exists even in alien domains.

**If time and energy allow:** Add a 5th domain chosen by students. "What domain do you want to test? Throw something at it."

### 0:43–0:55 — Pattern Recognition + Student Challenge (12 minutes)

*(Merged from two separate sections. Same learning outcome: students connect failures to training data.)*

Step back and look for patterns:

- "Which model worked best across the most domains?"
- "Were there domains where ALL models struggled?"
- "What makes a domain 'hard' for these models?"

Pull up the model cards again:
- https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
- https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
- https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment

Connect model card → training data → domain performance: "The Twitter model handles slang because it was trained on tweets. The product model handles star ratings because that's what it learned from."

**Quick challenge (5 min):** "Can someone suggest a type of text that would confuse ALL three models?" Let students throw ideas out. Test 1-2 suggestions live. The point: every model has a training-data boundary.

### 0:55–1:10 — Name the Concept: OVERFITTING AND DOMAIN SHIFT (15 minutes)

**Overfitting:**
- "When a model gets SO good at its training data that it can't handle anything else."
- Analogy: "Imagine studying only one teacher's test style. You ace THEIR tests. Then you take a test from a different teacher and bomb it — not because you don't know the material, but because you only learned one format."
- The movie review model is overfit to movie review language. It "thinks" everything is a movie review.

**Domain Shift:**
- "When the data a model encounters in the real world is different from what it was trained on."
- The model didn't get dumber — the world shifted under it.
- Analogy: "You learned to drive in a small town. Then someone puts you on a six-lane highway in another country where they drive on the other side. Same skill (driving), completely different domain."

**Connect back to model evaluation (Session 4):**
- "Remember when we asked 'which model is best?' Now we know the answer: best FOR WHAT?"
- Evaluation must include testing on the DOMAIN you care about, not just any test set.

**The Breakthrough (scripted — this is the narrative pivot point, don't skip it):**

"So here's the thing. For years, every model had this problem. A movie review model couldn't understand tweets. A medical model couldn't read poetry. Every model was trapped in its training world. And the solution was always: build another specialized model. Need to analyze tweets? Train a tweet model. Need to read legal documents? Train a legal model. It was expensive, slow, and it never ended."

"Then someone asked a different question: what if the training domain was... everything? What if instead of training on movie reviews or tweets or medical notes, you trained on the whole internet — books, Wikipedia, news, forums, all of it? Not to do one task, but to learn language itself?"

"In 2018, a model called BERT showed that this could work. You pretrain on massive general text, and then fine-tune on your specific task. A single model that starts with general knowledge of language and then specializes. That's the idea behind every modern AI system — ChatGPT, Claude, Gemini, all of them. The domain wall we hit tonight? That's exactly what pretraining was designed to break through."

### 1:10–1:15 — Research Lens (5 minutes)

**Say:** "Let's name what we just did in research terms."

"We tested **generalization** — whether a model works on data it wasn't trained on. In research, this is called **external validity**: does your finding hold up outside the specific conditions you tested it in?"

"Think about it this way: BERT's breakthrough was essentially an answer to the external validity problem. Instead of building a model that only works in one domain, build one that starts with general knowledge of language. Pretraining on everything is how you build external validity into the model itself."

**Research question (shared, sentiment):** "How well do sentiment models generalize across domains — reviews, poetry, legal text, therapy transcripts?"

**The method (applies to any topic):** Cross-domain testing. Take a model trained on Domain A and test it on Domain B, C, D. Where it fails tells you about its training data. Where it succeeds tells you what it actually learned versus what it memorized.

**Bridge to Build Together:** "Alright — we've got the concept. Now let's put it to use. For the rest of tonight, we're going to work on your portfolios again. You'll write a journal entry about domain shift, and we're going to make sure everyone's Spaces are actually working."

### 1:15–1:54 — BUILD TOGETHER: Portfolio Work Session (39 minutes)

**This is the second Build Together block. Session 5 got the infrastructure in place. Session 6 is about making sure it's working and building the habit of writing.**

**Frame it (1 min):**

"Last week we set up repos and wrote our first journal entries together. Tonight we're going to do that again — because the second entry is what turns 'I tried this once' into 'I have a practice.' We're also going to make sure every single person has a Space that actually runs. By the end of tonight, your portfolio should have: a repo with two entries, a Collection with real items in it, and a Space you can point someone to."

#### Step 1: Space Status Check + Debugging (15 minutes) — 1:16–1:31

**This is the most important part of the Session 6 Build Together. Go around the room.**

"Everyone open your Hugging Face profile page. Let's go around — show me your Spaces."

**For each student, one of three things is true:**

**A) They have a working Space.** (Bobby, Chengry probably, Sevilla, Shawn)
- "Great. Open it, make sure it loads. While others are getting set up, try running one of tonight's domain-shift tests on your own Space. Does it handle text from a domain it wasn't built for?"
- This keeps strong students engaged while you help others.

**B) They have a Space with errors.** (Annabelle, George likely)
- Debug it live. This is teaching. Share the student's screen so everyone can see.
- Common fixes: missing dependency in requirements.txt, typo in app.py, model name wrong.
- Say: "Debugging is a real skill. Let's figure this out together."
- If it can't be fixed in 3 minutes, have them duplicate the Text Playground as a working backup and troubleshoot the broken one between sessions.

**C) They haven't built a Space yet.** (Emily, Henry likely)
- "Let's get you a Space right now. We're going to duplicate the Text Playground."
- Walk them through: go to the Text Playground Space → click the three dots → "Duplicate this Space" → name it something related to their interest → deploy.
- **The key move:** After duplicating, have them change the example prompts to match their topic. Emily changes the prompts to news/research topics. Henry changes them to something related to image generation or NLP. Now it's *theirs* even though the code is the same.
- This takes about 5 minutes per student. If both Emily and Henry need this, do them simultaneously while others work on their journal entries.

**Target:** Every student has at least one Space that loads without errors by 1:31.

#### Step 2: Journal Writing Sprint (15 minutes) — 1:31–1:46

**Same format as Session 5. Template on screen. Everyone writes.**

Put the Week 6 template in the Zoom chat:

```
## Week 6 — Model Evaluation and Generalization

### This Week's Method
(Cross-domain testing — testing a model outside its training domain.)

### How I Applied It
(What model did we test? What domains did we throw at it?)

### What I Expected
(Before we tested — did you think the models would handle poetry? Medical text? Why or why not?)

### What I Found
(What actually happened? Which domains broke the models? Which didn't?)

### Why I Think This Happened
(Connect it to training data. What did the model learn, and what was missing from its world?)

### What I Want to Try Next
(Is your topic coming into focus? What domain shift would you test on YOUR topic?)
```

**Say:** "You've got 15 minutes. Write about what we just saw. The Domain Safari gave you plenty of material. If you're stuck, start with: 'When we gave the movie review model a poem, it said...' and go from there."

**Circulate and check in.** Students who wrote their Session 5 entry will find this easier — the format is familiar. Students who are writing their first entry ever (despite Session 5's push) should just write *something*.

**At 1:46, say:** "Commit what you have. Two entries in two weeks — you're building a journal."

#### Step 3: Peer Share (8 minutes) — 1:46–1:54

**This is new and important. Students see each other's work for the first time.**

Pair students up. Suggested pairings based on interests and status:
- **Chengry + George** (both medical AI — Chengry can help George)
- **Bobby + Annabelle** (both prolific builders — Bobby's more polished, Annabelle can learn debugging approaches)
- **Sevilla + Shawn** (both strong analysts — different topics, can cross-pollinate)
- **Emily + Henry** (both earlier stage — solidarity and mutual encouragement)

**Instructions:** "Share your screen with your partner. Show them three things: your Collection, your journal, and your Space. Two minutes each. Tell them what you're interested in and what you're building toward."

**Why this matters:**
- Makes the portfolio feel real — someone else has seen it.
- Creates gentle accountability — next session, your partner might ask how it's going.
- Stronger students naturally help weaker ones when they see what's missing.
- Students often discover shared interests they didn't know about.

**After pairs:** Quick full-group debrief (2 min). "Did anyone see something interesting in their partner's work? Anything surprise you?"

### 1:54–2:00 — Bridge Forward + Wrap Up

**Bridge to Session 7 (scripted — say something like this):**

"So tonight we hit the wall. Models trapped in their training worlds. And we learned about the breakthrough that solved it: train on everything. Pretrain on the whole internet, then fine-tune."

"But training on everything solved one problem and created another. When you train on the entire internet, you train on every bias, stereotype, and inequality in human history. Every pattern in the data gets amplified — including the harmful ones. The bigger the model, the bigger the bias problem. That's next week."

**Homework framing (lighter, because the heavy lifting happened in session):**

"Your between-session work: finish polishing your journal entry — you already wrote the draft. Try testing one more domain on your own. And bring your Collection to at least 8 items. Next session, we're diving into bias — so start thinking about this: when a model learns from the entire internet, whose voices are loudest in that training data, and whose are missing?"

Share the between-session challenge (see BETWEEN-SESSION.md).

**Optional supplementary reading:** For students who want to go deeper on the BERT breakthrough, point them to the `bonus-bert-content-moderation` module.

**End-of-session status check (say this with energy):**

"Quick check — raise your hand if you now have: a GitHub repo? A journal entry from tonight? A working Space? A Collection with items in it? Look around. Two weeks ago some of you had none of that. You're building something real."

---

## Pre-Prepared Domain Text Samples

### Formal News Articles

**Sample 1:**
> The Federal Reserve announced a quarter-point interest rate cut on Wednesday, signaling confidence that inflation is moving sustainably toward its 2 percent target. Markets responded with modest gains across major indexes.

**Sample 2:**
> The city council voted unanimously to approve the new zoning regulations, which will allow mixed-use development in previously residential-only areas. Opponents plan to appeal the decision.

**Discussion:** "These are neutral/factual. The movie model has to pick POSITIVE or NEGATIVE — it has no neutral option. What does it do?"

---

### Tweets / Social Media

**Sample 1:**
> ngl this new update is mid at best 💀 they really thought they did something

**Sample 2:**
> bestie you did NOT just say that 😭😭😭 im screaming rn

**Discussion:** "Which model handles slang and emoji best? (Twitter model should win here.) What about the product review model — has it ever seen '💀'?"

---

### Product Reviews (Amazon-style)

**Sample 1:**
> Works exactly as advertised. Shipped on time. The build quality is decent for the price point. Would recommend for anyone on a budget who doesn't need premium features.

**Sample 2:**
> Bought this as a gift. Recipient seemed to like it. Packaging was nice. Took a star off because the color was slightly different from the photo.

**Discussion:** "The product review model should be at home here. But does 'decent for the price' read as positive or negative?"

---

### Song Lyrics

**Sample 1 (melancholy pop):**
> I've been losing sleep over the things that I can't keep. The photographs are fading and the memories are deep. But I'll keep walking through the rain because the sun is just a dream away.

**Sample 2 (upbeat with dark lyrics):**
> Dancing on the ceiling, burning down the walls, laughing at the wreckage as the empire falls. We'll celebrate the ending with confetti made of ash.

**Discussion:** "Song lyrics mix positive and negative imagery on purpose. Sample 2 sounds upbeat (dancing, laughing, celebrating) but is actually about destruction. Can the models tell?"

---

### Student Essay Excerpts

**Sample 1:**
> In conclusion, while both authors present compelling arguments, Smith's analysis is more thoroughly supported by evidence. However, Jones raises important counterpoints that cannot be ignored.

**Sample 2:**
> The experiment did not produce the expected results. The hypothesis was not supported by the data. However, the methodology was sound and the procedure could be replicated with adjusted variables.

**Discussion:** "Academic writing is carefully balanced — not really positive or negative. It lives in a middle ground that the movie model doesn't understand."

---

### Text Messages

**Sample 1:**
> lol ok sure whatever u say 🙄

**Sample 2:**
> omg YES that's literally the best thing ever im so happy rn ahhh

**Discussion:** "'lol ok sure whatever' — is that positive, negative, or sarcastic? Humans would need context. Models don't have that context."

---

### Legal Text

**Sample 1:**
> The party of the first part shall indemnify and hold harmless the party of the second part against any and all claims, damages, losses, costs, and expenses arising out of or relating to any breach of this agreement.

**Sample 2:**
> Nothing in this agreement shall be construed to limit the liability of either party for gross negligence, willful misconduct, or fraudulent misrepresentation.

**Discussion:** "Legal text has no sentiment — it's purely functional. But the models HAVE to output something. What do they say? Why?"

---

### Medical Notes

**Sample 1:**
> Patient presents with acute onset of substernal chest pain radiating to the left arm. ECG shows ST-elevation in leads II, III, and aVF. Troponin levels are pending. Started on aspirin and heparin drip.

**Sample 2:**
> Follow-up visit. Patient reports significant improvement in symptoms since starting the new medication. Range of motion has increased. Recommend continuing current regimen.

**Discussion:** "Sample 1 describes a heart attack in neutral clinical language. Sample 2 is genuinely positive news. Can the models tell the difference, or do clinical words confuse them?"

---

### Poetry

**Sample 1 (dark imagery, classic style):**
> I wandered lonely through the ash of things that used to gleam. The world had shed its golden mask and left a hollow dream.

**Sample 2 (joyful imagery):**
> The morning broke with strawberry light across the sleeping town. Each window caught a piece of sky and wore it like a crown.

**Discussion:** "Poetry uses figurative language. 'Ash of things that used to gleam' is negative to a human, but does the model understand metaphor?"

---

### Code Comments

**Sample 1:**
> // HACK: This is a terrible workaround for the race condition. TODO: fix this properly before it breaks production again.

**Sample 2:**
> // Beautiful implementation of the merge sort algorithm. Clean, efficient, and well-tested. Props to @sarah for this one.

**Discussion:** "Code comments are a completely alien domain for all three models. But they still contain sentiment. Can the models detect it through the technical noise?"

---

### Meme Transcriptions

**Sample 1:**
> Nobody: Absolutely nobody: My cat at 3am: *knocks everything off the counter*

**Sample 2:**
> Me: I should really go to bed early tonight. Also me at 2am: Let me just watch one more episode.

**Discussion:** "Meme format is its own language. 'Nobody:' format, self-deprecating humor, relatable content. These aren't really positive or negative — they're funny. How do sentiment models handle humor?"

---

## Discussion Questions by Domain

| Domain | Key Question |
|--------|-------------|
| News | "Can a model be useful if it has no 'neutral' option?" |
| Tweets | "Why does the Twitter model understand slang? What would happen if we trained a model only on Shakespeare?" |
| Product Reviews | "Is 'decent for the price' positive or negative? Is there a 'right' answer?" |
| Song Lyrics | "Should AI understand art? What would it need to learn that?" |
| Student Essays | "Academic writing is balanced on purpose. Is 'balanced' a sentiment?" |
| Text Messages | "How much of texting depends on who you're talking to?" |
| Legal Text | "If there's no sentiment, what should the model say? Is 'I don't know' an option?" |
| Medical Notes | "Where would domain shift be actually dangerous?" |
| Poetry | "Can AI understand metaphor? What would it need to?" |
| Code Comments | "These models never saw code. But humans wrote sentiment into comments. Weird, right?" |
| Memes | "Memes have their own grammar. Is that a 'domain'?" |

---

## Technical Notes

- No new Space to build or deploy this session.
- Students should use either the instructor's deployed Space or their own duplicate from Session 4.
- If students modified their duplicates (added models, etc.), that's fine — it adds to the discussion.
- Long text inputs should be kept under 512 characters (the model truncation limit).

---

## Concept Connections

- **Sessions 1–3 (Act I):** Classification — sorting into buckets. Students experienced the limits of narrow models.
- **Session 4:** The fork. Classification vs. generation. Introduced model comparison — "which model is best?"
- **Session 5:** The controls on generation. Temperature and top-p. **Build Together #1: GitHub repos, first journal entries, Collection check.**
- **Session 6 (this session):** The answer to "which model is best?" is "best FOR WHAT DOMAIN?" Models are products of their training data. The breakthrough: pretraining on everything. **Build Together #2: Space debugging, second journal entry, peer sharing.**
- **Session 7 (next):** The cost of scale. Training on everything means training on every bias in human history.
- **Bonus module:** `bonus-bert-content-moderation` — optional deeper dive on how BERT works and how Twitter used BERT-style models for content moderation. Fits naturally as supplementary reading between Sessions 6 and 7.

---

## Portfolio Status After Session 6

By the end of tonight, every student should have:

| Artifact | Minimum Status | Notes |
|----------|---------------|-------|
| GitHub repo (`my-ai-portfolio`) | Exists, has files | Created in Session 5 Build Together if not before |
| Research journal | 2 entries (Weeks 5 & 6) | Written in-session; can be polished between sessions |
| Hugging Face Collection | 6+ items with tasting notes | Checked in Session 5 round-robin; should grow naturally |
| Working Space | At least 1 that loads | Debugged or duplicated in Session 6 Build Together |
| Notebooks | Uploaded from Sessions 1-5 | Some students may be behind; not critical yet |

**If a student is missing any of the above after Session 6, flag it in their sp-26 profile and address it directly in the personalized Session 7 email.**

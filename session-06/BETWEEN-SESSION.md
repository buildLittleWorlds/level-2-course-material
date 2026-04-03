# Between Sessions 6 & 7

**Tonight you discovered domain shift.** You saw the same model produce good output on one kind of text and struggle on another — not because the model got worse, but because the world changed. This week's homework is about testing that idea with your own Space and getting ready for Session 7, where we ask: what happens when "train on everything" brings its own problems? Plan for about 1 hour total.

---

## Part 1: Test Your Space Across Domains (20 min)

In class we tested generative models on text from different worlds — news, medical, poetry, legal, game dialogue. We saw that quality depends on the match between the model's training data and the input domain.

Now do the same thing with **your Space.**

1. Open your deployed Space on Hugging Face
2. Test it with **3 inputs from different domains** — at least one should be far from what you designed it for
3. For each test, note: did the model handle it well, or did the quality drop? Was the failure obvious or subtle?

**Specific suggestions by Space type:**

- **Text generator:** Try prompts from different worlds — a medical case note, a poem's opening line, a legal clause, a recipe step, a game dialogue line. Where does it sound natural and where does it sound wrong?
- **Summarizer:** Paste in text from outside news — a poem, a legal paragraph, game lore, a medical report, song lyrics. Does the summary capture the right things, or does it flatten what matters?

Write down your best example — the one where the domain shift was most visible. Bring it to next session.

## Part 2: Iterate on Your Space (15 min)

Pick one failure from Part 1 and try to fix it:

- **For the text generator:** Can you change the prompt template to work better in the failing domain? What if you add context to the prompt? ("Write a clinical note:" vs. just "The patient presents with")
- **For the summarizer:** Try adjusting the max/min length sliders. Does a shorter summary work better for poetry? A longer one for legal text?
- **For any Space:** Could you add a domain-specific example to the examples section?

The point isn't to fix everything — it's to experience the iteration loop: test → find a problem → try a fix → test again.

## Part 3: Research Journal Entry (15 min)

Open `research-journal.md` in your GitHub repo and add your Week 6 entry.

### Week 6 Entry Template

```markdown
## Week 6 — Same Space, Different Worlds

### What I Tested
(Which Space did you test? What domains did you try?)

### What Worked
(Which domain produced good output? Why do you think this matched the model's training?)

### What Broke
(Which domain produced bad output? What specifically went wrong — did it lose meaning, miss key terms, change tone?)

### Why I Think This Happened
(Connect it to training data. What did the model learn? What was missing from its world?)

### What I Tried to Fix
(Did you change prompts, settings, or examples to handle the failing domain? Did it help?)

### What I Want to Build
(Now that you've seen what models can and can't do across domains — what kind of tool do you want to build for your project? What domain should it work in?)
```

## Part 4: Collection + GitHub (10 min)

- **Collection:** Target: 8 models and 5 Spaces by Session 7. For new items, note what domain each model was trained on.
- **GitHub:** Upload the Session 6 notebook and commit your journal entry.

---

## Your Personal Challenge

### Annabelle
Your playful, quirky content — dino facts, silly phrases — lives in a domain most models weren't trained on. Try running creative/whimsical prompts through your text generator and see where the model produces something that actually sounds playful vs. where it falls flat. Write about what domain the model seems to "understand" and what it doesn't. One polished observation is worth more than ten quick tests.

### Bobby
Game dialogue is a fascinating domain for this test. Take your text generator and prompt it with game-specific openings — "The quest giver leaned against the tavern wall and said:", "LOADING SCREEN TIP:", "Achievement Unlocked:". Does the model know what game writing sounds like? Write up which prompts worked and which didn't — that tells you exactly how much game text was in the training data.

### Chengry
Medical text is the hardest domain shift case. Take your summarizer (or text generator) and test it on a real clinical case description. Then test on patient-facing health advice (simpler language, same domain). Does the model handle one better than the other? That difference matters for your DxAI project — your tool needs to work with both clinical and patient language.

### Emily
Test your summarizer on news articles from different beats — politics, science, entertainment, sports. Is the summary quality consistent, or does it handle some topics better than others? That's domain shift within a single genre. Write about which news domains work best and which ones the model simplifies too much.

### George
Try your Space on health text written for different audiences — a Wikipedia health article, a medical journal abstract, and a patient instructions sheet. Same topic, different language levels. Does the model handle them all equally? That's a subtle form of domain shift — same domain, different register.

### Henry
You have interests in both vision and text. Think about domain shift in both: the camera angles LoRA was trained on specific image types, and any text model was trained on specific text types. Pick one and test it outside its comfort zone. Write about what you find — even a short paragraph connecting domain shift to your specific interest would be great journal material.

### Sevilla
You already found domain shift before we named it — BLIP models failing on cartoonish images, emotion detectors missing sarcasm. This week, try the reverse: take your text generator or summarizer and test it on emotionally complex text (a breakup text, a graduation speech, a eulogy). Does the model handle emotional register, or does it flatten everything?

### Shawn
Your systematic comparison methodology is perfect for domain testing. Pick one Space (text generator or summarizer) and run the same test across 4-5 domains. Build a comparison table like you did for image generation models. Document which domains produce the best output and hypothesize why based on what you know about the training data.

---

AI + Research Level 2 • Session 6: Same Space, Different Worlds

# Session 6: Domain Shift and Generalization
*Student-Facing Title: "Same Space, Different Worlds"*

## Concept: DOMAIN SHIFT AND GENERALIZATION

**Space:** Domain Generator (built live from Session 5's Text Playground)
**Model:** `distilgpt2` (same model as Sessions 4 and 5)
**Key Idea:** A model trained on one kind of text writes differently -- and worse -- when you move it to a different domain. You can't prompt your way out of domain shift. If the model never saw clinical language during training, no prompt will make it write like a doctor.
**Narrative Role:** The wall that generation couldn't get past, and the breakthrough that solved it. This is the pivot point of Act II.

---

## Materials Checklist

Before class, have the following open/ready:

- [ ] Session 5 Text Playground Space open in a tab (the deployed version with temperature/top-p sliders)
- [ ] Session 6 `domain-generator.py` open in a text editor (reference for the live build)
- [ ] Hugging Face account logged in, ready to create a new Space for the live build
- [ ] Pre-built backup of the Domain Generator Space deployed and tested (in case the live build stalls)
- [ ] Domain test text samples printed or in a doc you can paste from (see Appendix A)
- [ ] Session 5 summarizer Space URL ready (for Demo Build 2 -- if you built a summarizer in S5, use that; otherwise use any deployed BART/T5 summarizer)
- [ ] Colab notebook link ready to paste in Zoom chat
- [ ] Session 6 slides loaded
- [ ] A medical text sample ready to paste into the S5 text generator for the live hook

---

## Time Breakdown (2 hours)

### Block 1: Framing (0:00--0:15, 15 min)

#### 0:00--0:07 -- Check-In

Ask: "Who got their Space working this week? Anybody add a new slider or change their prompts?"

Quick share. Let students show what they built or modified. Celebrate working Spaces -- every deployed Space is a win.

**For students with broken Spaces (Annabelle, Chengry):** Don't troubleshoot now. Say: "We'll get to that during the build time. For now, you can use my deployed version."

#### 0:07--0:15 -- Narrative Bridge + Live Domain Shift Hook

**Narrative bridge (2 min -- don't skip this):**

"Last week we added controls to our generator -- temperature, top-p, max length. You now know the same knobs that developers set on ChatGPT and Claude. You can dial in the kind of writing you want. But there's something those knobs can't fix."

"Every model we've built so far -- the generator from Session 4, the Text Playground from Session 5 -- runs on distilgpt2. That model was trained on web text: Reddit, news articles, Wikipedia, blog posts. It learned what internet English looks like. And it can generate more internet English pretty well."

"But watch what happens when we ask it about something it never saw."

**Live hook (5 min -- do this live, don't just describe it):**

Open the Session 5 Text Playground Space. Set temperature to 0.7, max length to 80.

Type this prompt:

> "Patient presents with acute onset of substernal chest pain radiating to the left arm. Treatment plan:"

Generate. Read the output aloud. It will be gibberish -- the model will try to continue in web-text style, producing something that sounds nothing like a medical note.

Now type:

> "The warrior stepped into the dungeon and said:"

Generate. Read the output aloud. This will sound more natural -- fantasy/game dialogue is closer to the web text it trained on.

**Say:** "The model is the same. The settings are the same. The world changed. And the model can't keep up. That's what we're investigating tonight."

---

### Block 2: Demo Build 1 -- Domain-Adapted Text Generator (0:15--0:37, 22 min)

**The narrative frame:** We're taking the Session 5 text generator and adding a domain dropdown. The model stays the same -- distilgpt2. What changes is the prompt template. Each domain preset fills in a different kind of starting text. The question: does the model write equally well in every domain?

> **What we're building and why:** A text generator with a domain dropdown -- Game Dialogue, Medical Notes, News Article, Poetry, Recipe. Each preset fills a prompt template. Same model, different starting worlds. The completed code is in `session-06/domain-generator.py`.

#### The Build (15 min)

1. **Start from Session 5's code.** Pull up last week's `app.py` on screen. Say: "This is where we left off. A text generator with sliders. Now we're adding one more control: a domain selector."

2. **Create new Space on Hugging Face** -- "Domain Generator" (SDK: Gradio, Hardware: Free CPU)

3. **Write requirements.txt** -- `transformers`, `torch`, `gradio` (same as last two weeks -- point this out)

4. **Build app.py step by step:**
   - Start with the imports and model loading (same as S5)
   - Add the domain presets dictionary -- walk through each one: "Game Dialogue starts with a fantasy scene. Medical Notes starts with a clinical phrase. Same model is going to try to continue both."
   - Build the generate function with domain selection
   - Wire up Gradio with the dropdown, temperature slider, max length slider, and prompt box
   - Add the `domain.change` callback so selecting a domain fills the prompt

5. **Deploy and test**

**While the Space builds (1-2 min), explain the experiment:**

"Here's what I want you to watch for. We're about to test the same model on five different domains. Some will sound natural. Some will sound wrong. The model didn't get dumber between tests -- the domain shifted."

#### The Domain Shift Moment (7 min)

Once the Space is live, test each domain preset in order. For each one, generate and read the output aloud:

| Domain | What to expect | What to say |
|--------|---------------|-------------|
| Game Dialogue | Sounds okay -- fantasy/adventure is common in web text | "Not bad. The model has seen plenty of fantasy writing online." |
| Medical Notes | Sounds wrong -- clinical language is alien to this model | "Listen to that. It doesn't sound like a doctor wrote it. It sounds like someone who's never been to medical school trying to fake it." |
| News Article | Decent -- news is well-represented in web training data | "News is one of the biggest categories of web text. The model is on home turf." |
| Poetry | Weird -- might rhyme accidentally, probably sounds off | "Poetry is interesting. The model has seen some poems, but it doesn't understand meter or metaphor. It's pattern-matching." |
| Recipe | Mixed -- recipe format exists online but the model may drift | "Recipes have a specific structure. The model sort of gets it but keeps wandering off." |

**Land the observation:**

"Game dialogue sounds okay. Medical notes sound wrong. Poetry is weird. Same model, same temperature, same max length. The only thing that changed was the starting text -- the domain. You can't prompt your way out of this. If the model never saw clinical language during training, no prompt will make it write like a doctor."

---

### Block 3: Student Work 1 -- Cross-Domain Testing (0:37--0:57, 20 min)

**Setup:** Students test their own Spaces on text from OUTSIDE their intended domain. The goal is for every student to experience domain shift firsthand.

#### Student Work Priority Table -- Block 3

| Student | What they have | What to test | Expected discovery |
|---------|---------------|-------------|-------------------|
| Bobby | Game dev / creative AI Space | Feed it medical text or legal text | Game-trained prompts fall apart on clinical language |
| Annabelle | Music / creative Space (broken) | Use the instructor's Domain Generator; test music prompts vs. news prompts | Even creative domains shift -- song lyrics vs. poetry vs. dialogue |
| Shawn | Image generation comparison | Test image prompt generator with medical descriptions vs. fantasy descriptions | Prompt style matters -- clinical descriptions produce different image results |
| Emily | News/research tools | Feed summarizer or generator poetry, song lyrics, or recipe text | News-trained tools strip voice and imagery from creative text |
| Henry | News sentiment / computer vision | Test news tools on poetry or social media slang | Formal news tools struggle with informal or figurative language |
| Chengry | Medical AI / DxAI (runtime error) | Use the instructor's Domain Generator; compare medical vs. game output | Medical text quality is low -- the model wasn't trained on clinical data |
| George | Medical/health | Test health-related generation on legal text or poetry | Medical prompts don't transfer to other specialized domains |
| Sevilla | Emotion detection / news testing | Test emotion tools on recipes, legal text, or code comments | Emotion detection finds "emotions" in text that has none |

**Circulate and ask questions:**
- "What domain did you test? What happened?"
- "Does the output sound like it belongs in that domain?"
- "Could you tell, just from the output, that the model wasn't trained on this kind of text?"

**For Annabelle and Chengry (broken Spaces):** Have them use the instructor's deployed Domain Generator. They can still experience domain shift by testing different presets. During Block 5, help them debug their own Spaces.

---

### Block 4: Demo Build 2 -- Summarizer Across Domains (0:57--1:17, 20 min)

**The narrative frame:** We just saw domain shift in text generation. Now let's see it in summarization. The Session 5 summarizer (or any BART/T5 summarizer) was trained on news articles (CNN/DailyMail dataset). What happens when we feed it text from other domains?

**No new build this block -- live testing of an existing summarizer Space.**

Open the summarizer Space. For each test, paste the text, generate the summary, and read both aloud.

#### Test 1: News Article (home domain)

Paste:
> The Federal Reserve announced a quarter-point interest rate cut on Wednesday, signaling confidence that inflation is moving sustainably toward its 2 percent target. Markets responded with modest gains across major indexes. Economists broadly expected the decision, though some analysts warned that premature easing could reignite price pressures in the housing and energy sectors. The central bank's statement emphasized data-dependent decision-making going forward.

**Expected result:** Clean, accurate summary. The model is on home turf -- it was trained on exactly this kind of text.

**Say:** "Clean summary. The key facts are there. This is what the model was built for."

#### Test 2: Poem

Paste:
> I wandered through the silver rain and found a door of light. Behind it stood the years I'd lost, dressed up in borrowed white. They waved like strangers on a train who recognize your face but can't recall the place they knew or why they left no trace.

**Expected result:** The summary will strip the imagery and try to extract "facts." It might say something like "The speaker found a door and saw lost years" -- flattening the metaphor into literal events.

**Say:** "Listen to what it did. It tried to extract the 'facts' from a poem. But poems aren't about facts -- they're about images, rhythm, feeling. The model squeezed the poetry out."

#### Test 3: Legal Text

Paste:
> The party of the first part shall indemnify and hold harmless the party of the second part against any and all claims, damages, losses, costs, and expenses arising out of or relating to any breach of this agreement. Nothing in this agreement shall be construed to limit the liability of either party for gross negligence, willful misconduct, or fraudulent misrepresentation.

**Expected result:** The summary will miss key legal terms or oversimplify the indemnification clause. Legal precision gets lost.

**Say:** "A lawyer would read that summary and wince. The specific legal terms matter -- 'indemnify and hold harmless' is a precise legal concept, not just 'protect.' The model doesn't know that."

#### Test 4: Game Lore

Paste:
> In the age before the Sundering, the Archmage Velathos bound the nine spirit-wells to the roots of the World Tree. Each well held a fragment of the First Song -- the vibration that had called matter into being. When the Betrayer shattered the sixth well, the resulting cascade unwove three kingdoms and turned the Amber Coast to glass. The survivors built the Spire of Echoes to contain what remained.

**Expected result:** The summary will capture the basic plot (mage bound wells, one got shattered, bad things happened) but will lose the voice, the specific terminology, and the world-building flavor.

**Say:** "It got the plot. But the voice is gone. 'The Archmage Velathos' becomes something generic. 'The First Song' disappears. The lore -- the thing that makes this world feel real -- got summarized away."

#### Test 5: Medical Text

Paste:
> Patient presents with acute onset of substernal chest pain radiating to the left arm. ECG shows ST-elevation in leads II, III, and aVF. Troponin levels are pending. Started on aspirin and heparin drip. Cardiology consult requested. Patient is hemodynamically stable but reporting persistent 7/10 pain despite initial nitroglycerin administration.

**Expected result:** Mixed. It might capture "patient has chest pain" but will likely miss or garble the clinical specifics (ST-elevation, troponin, heparin drip).

**Say:** "A doctor needs to know about ST-elevation in specific leads, about troponin levels, about the heparin drip. Those details aren't decoration -- they're the whole point. The model treats them like filler because in news articles, specific technical terms usually ARE filler."

#### Land the Observation

"Same model. Same controls. Same summarization task. Five different kinds of text -- five different levels of quality. The news article got a clean summary because the model was trained on news. Everything else got flattened, garbled, or stripped of what made it matter."

"The domain shifted. The model didn't."

---

### Block 5: Student Work 2 -- Iterate and Adapt (1:17--1:42, 25 min)

**Two goals for this block:**
1. Students try adapting their Space for a different domain (change prompt templates, change examples, change the framing)
2. **Hard goal: every student has at least one deployed, running, customized Space by end of this block.**

#### Student Work Priority Table -- Block 5

| Student | Priority | Specific task |
|---------|----------|---------------|
| Bobby | Adapt | Add a "Medical Dialogue" or "News Report" preset to his game-focused generator. Compare output quality across domains. |
| Annabelle | Fix + Adapt | Debug her broken Space first (check `requirements.txt`, check `app.py` for syntax errors). Once running, add domain presets for different music styles. |
| Shawn | Adapt | Add domain-specific prompt templates to his image generation comparison tool. Test how prompt domain affects image output. |
| Emily | Adapt | Test her news summarizer on 2-3 non-news domains. Document where it breaks. Try rewriting the prompt template to help. |
| Henry | Adapt | Fork the Domain Generator and add a "Computer Vision Paper" domain preset. Compare with news output. |
| Chengry | Fix first | Debug the DxAI runtime error. Common issues: missing dependency in `requirements.txt`, model name typo, or import error. Get it running, then test on non-medical text. |
| George | Adapt | Add domain presets to his health Space -- test what happens when the same model gets medical vs. casual health text. |
| Sevilla | Adapt | Test her emotion detection on text with no emotion (recipes, legal text, math problems). Document what the model "finds." |

**Circulate aggressively during this block.** This is where students who are behind catch up and students who are ahead push further.

**For Annabelle:** Compare her `app.py` and `requirements.txt` against the working reference code. Most common issues are a missing library in `requirements.txt` or a copy-paste artifact. If the fix is fast, great. If not, have her duplicate the instructor's Domain Generator Space and customize it -- she gets a working Space AND learns the domain shift concept.

**For Chengry:** Check the runtime error log in the Space's "Logs" tab. Common causes: model name doesn't match what's on Hugging Face, a library version conflict, or a function signature mismatch. If the fix takes more than 5 minutes, have him duplicate a working Space and customize it. A working Space matters more than debugging tonight.

**The key question to ask every student:** "Did you try text from outside your domain? What happened?"

---

### Block 6: Wrap-Up (1:42--1:52, 10 min)

#### 1:42--1:45 -- Quick Findings (3 min)

Go around the room fast. Each student shares one sentence:

"What's the most surprising thing that happened when you tested outside your domain?"

Don't let this run long -- one sentence each, move on.

#### 1:45--1:48 -- Name the Concepts: OVERFITTING and DOMAIN SHIFT (3 min, compressed)

**Overfitting:**

"When a model gets so good at its training data that it can't handle anything else. Here's the analogy: imagine you study for a test by memorizing one teacher's exact questions. You ace THEIR test. Then you take a different teacher's test on the same material and bomb it -- not because you don't know the subject, but because you only learned one format. That's overfitting."

**Domain Shift:**

"When the data a model encounters in the real world is different from what it was trained on. The model didn't get dumber -- the world shifted under it. Analogy: you learned to drive in a small town. Then someone puts you on a six-lane highway in another country where they drive on the left side. Same skill -- driving. Completely different domain."

**Connect them:**

"distilgpt2 is overfit to web text. When we shifted the domain to medical notes, it fell apart. Not because it's a bad model -- because it only learned one world."

#### 1:48--1:50 -- The Breakthrough: BERT (2 min, compressed)

"So for years, every model had this problem. A web-text model couldn't write medical notes. A recipe model couldn't write news. Every model was trapped in its training world."

"Then someone asked: what if the training domain was... everything? What if you trained on the whole internet -- books, Wikipedia, news, forums, medical texts, legal documents, all of it? Not to do one task, but to learn language itself?"

"In 2018, a model called BERT showed this could work. Pretrain on massive general text, then fine-tune on your specific task. That idea -- pretrain on everything, then specialize -- is behind every modern AI system. ChatGPT, Claude, Gemini. The domain wall we hit tonight? That's exactly what pretraining was designed to break through."

#### 1:50--1:51 -- Research Lens: External Validity (1 min)

"Quick research connection. What we did tonight is called testing for **external validity** -- does your finding hold up outside the specific conditions you tested it in? We tested our model across domains. Where it failed tells us about its training data. Where it succeeded tells us what it actually learned versus what it memorized. That's cross-domain testing."

#### 1:51--1:52 -- Bridge to Session 7

"Training on everything solved the domain shift problem. But it created a new one. When you train on the entire internet, you train on every bias, stereotype, and inequality in human history. Every pattern in the data gets amplified -- including the harmful ones. The bigger the model, the bigger the bias problem. That's next week."

Share the between-session challenge (see BETWEEN-SESSION.md).

---

### Buffer (1:52--2:00, 8 min)

Use for:
- Students finishing their Space deployments
- Debugging Annabelle's or Chengry's Spaces if not yet resolved
- Additional domain testing if energy is high
- Sharing Colab notebook link for between-session work

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Domain Generator Space fails to build | Check `requirements.txt` for typos. Most common: missing `torch` or `gradio`. If stuck, paste the complete `domain-generator.py` as `app.py` and commit. "Same thing happens to professional developers." |
| Space takes too long to build in class | Switch to the pre-built backup. "I deployed this earlier -- same code, already running. Let's use it while the live one catches up." |
| distilgpt2 generates gibberish on all domains | Normal for temperature > 1.2. Lower temperature to 0.7. If still gibberish at 0.7, check that `do_sample=True` is set and `max_new_tokens` isn't too large. |
| Medical/legal domain output sounds "okay" | Sometimes the model gets lucky. Generate 3-4 times on the same prompt -- inconsistency across runs is itself evidence of domain shift. A model on home turf produces consistent quality. |
| Student says "but ChatGPT can write medical text fine" | "Exactly. ChatGPT was trained on medical text, legal text, poetry, news, everything. That's the BERT breakthrough -- pretrain on everything. Our little distilgpt2 only saw web text. That's why domain shift hits it so hard." |
| Summarizer produces decent summaries on all domains | Some texts are closer to news style than others. Try more extreme examples: dense legal text, highly figurative poetry, or technical medical notes. The failures become clearer with more specialized text. |
| Student's Space has a runtime error they can't fix | Have them duplicate the instructor's working Space and customize it. A working Space they can modify teaches more than a broken Space they're stuck on. |
| Student finishes early and is bored | Challenge them: "Can you find a domain where distilgpt2 actually sounds good? What does that tell you about its training data?" Or: "Try writing a prompt template that makes the medical output sound more clinical. Does it help?" (It won't much -- that's the lesson.) |
| Annabelle's Space still broken | Priority: get her a working Space by any means. Duplicate the Domain Generator, rename it, customize the presets for music. Debug the original Space between sessions. |
| Chengry's DxAI runtime error | Check the Logs tab on Hugging Face. Most runtime errors are: (1) model name doesn't exist on HF, (2) missing library in requirements.txt, (3) function parameter mismatch. If the fix isn't obvious in 3 minutes, duplicate a working Space and move on. |

---

## Concept Connections

- **Sessions 1--3 (Act I):** Classification -- sorting into buckets. Students experienced the limits of narrow models. Every classifier was trained on one kind of text.
- **Session 4:** The fork. Classification vs. generation. Built a raw text generator with no controls. Introduced the idea that generation models train on "just text" -- no labels needed.
- **Session 5:** Added controls to the generator. Temperature, top-p, max length. Students learned that hyperparameters change behavior but don't change what the model knows. Closed with the domain shift teaser: "What happens when you feed medical text to a model trained on Reddit?"
- **Session 6 (this session):** The answer: it falls apart. Models are products of their training data. "Best for what domain?" The breakthrough -- pretraining on everything (BERT, 2018). The domain wall is what pretraining was designed to break.
- **Session 7 (next):** The cost of pretraining on everything. Training on the entire internet means training on every bias in human history. Scale solves domain shift but amplifies harm.

---

## Key Vocabulary

- **Domain** -- The type or category of text a model was trained on or is being asked to process. Examples: medical notes, news articles, poetry, legal contracts, game dialogue. Each domain has its own vocabulary, structure, and conventions.
- **Domain Shift** -- When the data a model encounters in the real world is different from what it was trained on. The model's quality degrades not because it broke, but because the world changed.
- **Overfitting** -- When a model becomes so specialized to its training data that it can't handle anything else. Like studying only one teacher's test format and failing a different teacher's test on the same subject.
- **Generalization** -- A model's ability to perform well on data it wasn't specifically trained on. The opposite of overfitting. A model that generalizes can handle new domains; an overfit model can't.
- **Pretraining** -- Training a model on massive, general-purpose data (like the whole internet) before fine-tuning it on a specific task. BERT (2018) showed this approach could break through the domain wall.
- **Fine-tuning** -- Taking a pretrained model and training it further on a specific, smaller dataset for a particular task. Pretraining gives general knowledge; fine-tuning gives specialized skill.
- **External Validity** -- A research concept: does a finding hold up outside the specific conditions it was tested in? Cross-domain testing is how you check external validity for AI models.
- **Cross-Domain Testing** -- Testing a model on data from domains it wasn't trained on. Where it fails reveals what it memorized. Where it succeeds reveals what it actually learned.

---

## Teaching Moments to Watch For

**"But I changed the prompt and it got better"**
This will come up. Students will try to write better prompt templates to "fix" the medical output. It might improve slightly -- but it won't sound like a real medical note. This is the key insight: **you can't prompt your way out of domain shift.** The model's vocabulary, its sense of what words follow other words, its entire understanding of language comes from training data. If clinical language wasn't in the training data, no prompt will conjure it. Name this moment when it happens.

**"My Space works fine on everything"**
Push back gently. Generate multiple times. The inconsistency across runs on out-of-domain text is itself evidence. A model on home turf produces reliably similar quality. A model in a foreign domain produces wildly variable quality -- sometimes accidentally good, usually not.

**"So small models are useless?"**
No -- small models are excellent within their domain. distilgpt2 is fast, free, and fine for casual web-style text generation. The lesson isn't "small models are bad" -- it's "every model has a world it knows and a world it doesn't." Even GPT-4 has domain shift problems on highly specialized text.

**The medical text moment**
When students see the medical output for the first time, some will laugh. Redirect: "Imagine this model was generating text in a medical app. A patient reads this output and thinks it's real medical advice. That's why domain shift isn't just an academic concept -- it's a safety problem." This connects forward to Session 7 (bias and harm).

---

## Appendix A: Domain Test Text Samples

These are ready-to-paste text samples for cross-domain testing. Use them in Blocks 2, 3, and 4. Each is short enough to fit in a text input box.

### News Article

> The Federal Reserve announced a quarter-point interest rate cut on Wednesday, signaling confidence that inflation is moving sustainably toward its 2 percent target. Markets responded with modest gains across major indexes. Economists broadly expected the decision, though some analysts warned that premature easing could reignite price pressures in the housing and energy sectors.

### Poetry

> I wandered through the silver rain and found a door of light. Behind it stood the years I'd lost, dressed up in borrowed white. They waved like strangers on a train who recognize your face but can't recall the place they knew or why they left no trace.

### Legal Text

> The party of the first part shall indemnify and hold harmless the party of the second part against any and all claims, damages, losses, costs, and expenses arising out of or relating to any breach of this agreement. Nothing in this agreement shall be construed to limit the liability of either party for gross negligence, willful misconduct, or fraudulent misrepresentation.

### Medical Notes

> Patient presents with acute onset of substernal chest pain radiating to the left arm. ECG shows ST-elevation in leads II, III, and aVF. Troponin levels are pending. Started on aspirin and heparin drip. Cardiology consult requested. Patient is hemodynamically stable but reporting persistent 7/10 pain despite initial nitroglycerin administration.

### Game Lore

> In the age before the Sundering, the Archmage Velathos bound the nine spirit-wells to the roots of the World Tree. Each well held a fragment of the First Song -- the vibration that had called matter into being. When the Betrayer shattered the sixth well, the resulting cascade unwove three kingdoms and turned the Amber Coast to glass.

### Recipe

> To make a proper French omelette, crack three eggs into a bowl and beat vigorously with a fork for thirty seconds. Heat a tablespoon of butter in a nonstick pan over medium-high heat until it foams but doesn't brown. Pour in the eggs and immediately begin stirring with a spatula, pulling the cooked edges toward the center while tilting the pan to let raw egg flow underneath.

### Song Lyrics (Melancholy)

> I've been losing sleep over the things that I can't keep. The photographs are fading and the memories are deep. But I'll keep walking through the rain because the sun is just a dream away, and every step I take reminds me of the price I'll never pay.

### Social Media / Text Message

> ngl this new update is mid at best. they really thought they did something. bestie you did NOT just say that im screaming rn

### Code Comments

> // HACK: This is a terrible workaround for the race condition. TODO: fix this properly before it breaks production again. The mutex lock should be acquired before the async callback fires, not after.

### Student Essay

> In conclusion, while both authors present compelling arguments, Smith's analysis is more thoroughly supported by evidence. However, Jones raises important counterpoints that cannot be ignored. Further research is needed to reconcile these conflicting perspectives.

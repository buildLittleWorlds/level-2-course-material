# Between Sessions 6 & 7

**Tonight you hit the wall.** You tested your Space on text from outside its world and watched it struggle — not because the model broke, but because it was never trained on that kind of text. That's domain shift, and it's the reason your project matters. A tool that works "in general" isn't a tool yet. A tool that works for *your* domain is.

This week: test deeper, start planning what you actually want to build, and look at the prompts in your student folder. Plan for about 1 hour.

---

## Build Step: Test Your Space and Pick a Direction (30 min)

**Test your Space 1 on at least 3 inputs from different domains.** At least one should be far from what you designed it for. For each test, write down: did the quality drop? Was the failure obvious or subtle?

- **Text generator:** Try a medical case note, a poem's opening line, a legal clause, a recipe step, game dialogue. Where does it sound natural? Where does it sound wrong?
- **Summarizer:** Paste in a poem, a legal paragraph, game lore, a medical report, song lyrics. Does the summary capture what matters, or does it flatten everything?

Save your best example of domain shift — the one where the failure is most visible. Bring it to Session 7.

**Then open your student folder on the course repo and read through the README.** The prompts there are designed for your interests — better models, more ambitious Spaces, comparison tools. Pick one direction that interests you. You don't have to build it yet, but by next session you should be able to say: *"Here's what I want my next Space to do."*

---

## Journal Entry (15 min)

Open `research-journal.md` in your GitHub repo and add your Week 6 entry:

```markdown
## Week 6 — The Domain Wall

### What I Tested
(Which Space did you test? What domains did you try?)

### What Broke
(Which domain produced bad output? What specifically went wrong?)

### Why I Think This Happened
(Connect it to training data. What did the model learn? What was missing?)

### What I Want to Build Next
(Now that you've seen what your baseline can't do — what kind of tool do you want to build? What domain should it work in? Which prompt from your student folder interests you?)
```

---

## Portfolio Check

By Session 7, you should have:
- A GitHub repo (`my-ai-portfolio`) with `research-journal.md`
- At least 2 journal entries (Week 5 + Week 6)
- A running Space 1 on Hugging Face
- A Hugging Face Collection with 6+ items
- A direction for your next Space (even if it's just an idea)

---

## Your Folder

Your student folder has prompts that go beyond Space 1. **Read through the README this week.** The prompts are designed so you can paste them into a coding AI (ChatGPT, Claude, Gemini) and get back working code for a more ambitious Space. You don't need to build it all this week — but reading the prompts will help you figure out what you want to aim for.

---

## Your Personal Challenge

### Annabelle
Your playful, quirky content lives in a domain most models weren't trained on. Try creative and whimsical prompts through your text generator — where does the model sound playful vs. where does it fall flat? Then look at your folder prompts and pick one direction for your next Space. One polished observation in your journal is worth more than ten quick tests.

### Bobby
Game dialogue is a fascinating domain for this test. Prompt your Space with game-specific openings — "The quest giver leaned against the tavern wall and said:", "LOADING SCREEN TIP:", "Achievement Unlocked:". Does the model know what game writing sounds like? Your folder has a prompt for a better model version — try building it this week if you have time. That becomes your Space 2.

### Chengry
You have two paths: the specialist (biomedical NER) and the generalist (API). This week, push the specialist. Test the NER model on different medical text types — clinical notes, patient-facing advice, drug labels, research abstracts. Where does it extract entities well? Where does it miss? Document the edge cases. Then think about your project architecture: could you combine both paths? That's a real design used in production medical AI.

### Emily
Test your summarizer on news from different beats — politics, science, entertainment, sports. Is the quality consistent, or does it handle some topics better than others? That's domain shift within a single genre. Your folder has prompts for a news model comparison lab and a better summarizer — read through them and decide which direction you want to go.

### George
Try your Space on health text written for different audiences — a Wikipedia article, a journal abstract, and a patient instruction sheet. Same topic, different register. Does the model handle them equally? That's a subtle form of domain shift. Write about what you find, then look at your folder for next steps.

### Henry
Think about domain shift in both vision and text — the camera angles LoRA was trained on specific image types, and any text model was trained on specific text types. Pick one and test it outside its comfort zone. Your folder has prompts for a scene description Space that connects to your visual interests. Read through them this week.

### Sevilla
You already found domain shift before we named it — BLIP models failing on cartoonish images, emotion detectors missing sarcasm. This week, test your Space on emotionally complex text (a breakup text, a graduation speech, a eulogy). Does the model handle emotional register, or does it flatten everything? That connects directly to what you could build next.

### Shawn
Your systematic comparison methodology is perfect here. Pick one Space and run the same test across 4-5 domains. Build a comparison table. Your folder has prompts for a model comparison lab — that's a natural Space 2 for you. Read through the prompts and start thinking about what models you'd compare.

---

AI + Research Level 2 • Session 6: The Domain Wall

# Between Sessions 5 & 6

**You built something tonight.** Whether it's the text generator, the summarizer, or a duplicate you customized — you have a working Space on Hugging Face. This week's homework is about making it yours and getting ready for next session, where we'll test what happens when models leave their comfort zone. Plan for about 1 hour total.

---

## Part 1: Get Your Space Working (20 min)

**Priority one: you need a running Space.** If you deployed one in class and it's working, great — skip to customizing it. If it's erroring out or you didn't finish, do this now:

1. Go to huggingface.co and sign in
2. Open the Space you started in class (or duplicate `profplate/text-playground` or `profplate/quick-summarizer`)
3. Check `app.py` and `requirements.txt` — compare with the working code in the session materials
4. Fix any errors and commit
5. Wait for it to build. If it says RUNNING, you're good.

**Then customize it:**
- Change the title and description to match your interest
- Change the example prompts to topics you care about
- If it's the text generator, try different default temperature/top-p settings
- If it's the summarizer, try different max/min length defaults
- Commit your changes

## Part 2: Test It on Something Unexpected (15 min)

This is a preview of next session's concept. Try feeding your Space text from a domain it wasn't designed for:

- If you have the **text generator**: try prompts from different worlds — medical text, legal language, poetry, game dialogue, recipe instructions. Does the quality change depending on the domain?
- If you have the **summarizer**: paste in a poem, a legal paragraph, song lyrics, or a recipe. Does the summary make sense, or does it fall apart?

**Write down one example that surprised you.** Bring it to next session — we'll use it.

## Part 3: Research Journal Entry (15 min)

Open `research-journal.md` in your GitHub repo and add your Week 5 entry. If you don't have a GitHub repo yet, create one now — go to github.com, click New Repository, name it `my-ai-portfolio`, and create a file called `research-journal.md`.

### Week 5 Entry Template

```markdown
## Week 5 — Add Controls

### What I Built
(Which Space did you build or customize? What does it do?)

### The Controls
(What hyperparameters does your Space have? What do they change about the output?)

### What I Tried
(What settings did you experiment with? What happened at the extremes?)

### What Surprised Me
(Was there a moment where the output changed in a way you didn't expect?)

### What I Want to Try Next
(What would make your Space more useful? What question is forming in your mind?)
```

## Part 4: Collection + GitHub (10 min)

- **Collection:** Add your new Space to your Hugging Face Collection. Include a tasting note describing what it does and what controls it has. Target: 7 models and 5 Spaces by Session 6.
- **GitHub:** Upload the Session 5 notebook to your `my-ai-portfolio` repo and commit your journal entry.

---

## Your Personal Challenge

### Annabelle
You build fast — that's a real strength. This week, pick ONE of your Spaces (Dino Fact Explorers, Silly Phrase Finder, or the text generator from tonight) and make it fully yours. Change the title, the description, the examples. Write a journal entry about what you changed and why. One polished Space is worth more than four half-finished ones.

### Bobby
Your game development background is perfect for the text generator. Change the example prompts to game narrative — character dialogue, item descriptions, quest introductions. Experiment with temperature: what setting produces the best game writing? Write up your "settings recipe" in your journal.

### Chengry
Your DxAI project is ambitious and important. This week, focus on getting it running — the runtime error is likely a missing dependency in `requirements.txt`. If you get stuck, bring the error message to next session. Also try the summarizer with medical text — paste in a clinical case description and see what the summary captures vs. what it misses. That's directly relevant to your project.

### Emily
Tonight was your launchpad. If you duplicated the summarizer, customize it: change the title to something related to news or research, swap the examples for news articles that interest you. Getting this Space running and personalized is your main goal this week. Then create your GitHub repo and write your first journal entry about what you built.

### George
Same as Emily — your main goal is a running, customized Space. If you went with the summarizer, try it on health articles. Write your first GitHub journal entry about what the summarizer did well and where it struggled with medical text. That observation connects directly to next session.

### Henry
You've been a thoughtful curator — your collection shows good taste. This week, become a builder. Make sure you have a running Space (duplicate one from class if needed). Try the text generator with news-style prompts at different temperature settings. Start your journal entry about what controls you discovered.

### Sevilla
Your emotion detection work and the text generator are natural partners. Try feeding emotionally charged prompts into the generator at different temperatures. Does high temperature produce more emotionally varied text? Does low temperature flatten the emotional range? That's a parameter sweep applied to your specific interest — perfect journal material.

### Shawn
Your systematic comparison methodology is ideal for parameter sweeps. Pick one of tonight's Spaces and run a proper comparison: same prompt, one slider changed at a time, results documented in a table. This is what you already do with image generation models — same method, different medium. Write it up in your journal.

---

AI + Research Level 2 • Session 5: Add Controls

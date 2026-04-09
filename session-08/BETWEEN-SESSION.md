# Between Sessions 8 & 9

> **Heads-up:** This is also the week the course turns toward research work. Your main research work between sessions 8 and 9 is in [`WEEK-8-RESEARCH-WORK.md`](./WEEK-8-RESEARCH-WORK.md). Read that first. The build and journal steps below support that research work.

**Tonight you chained models together** and saw how errors cascade — when the first model gets something wrong, the second model just works with the wrong answer. That's a real concept for any student building a pipeline this term, and the Week 8 research work asks you to read one paper carefully enough that you could actually cite it.

Prea's [Week 8 journal entry ("Space 2 Polished, and the First Real Numbers")](../example-student-prea/research-journal.md) is a good example of improvement and planning working together. She adds a confidence check that warns when a clip has too few words to compute reliable prosodic features, writes her four feature functions properly, and tests the Space on five real practice speeches from her own team. She notices a pattern between one of her features (speaking-rate variance across thirds of the speech) and her own ratings of the clips — then immediately writes, *"n = 5 is not a result."* She also connects tonight's class topic to her own pipeline: a Whisper mistranscription won't break her prosodic features, but it will feed a garbled transcript into any content-scoring stage she adds later. That's the move: *improve what works, plan what's next, and be honest about what the numbers can and can't tell you.*

This week: improve Space 2, start thinking about Space 3, and do the Week 8 research work.

---

## Build Step: Improve Space 2, Plan Space 3 (30 min)

Your Space 2 should be deployed by now. This week, make it better:

- **Fix what's broken.** If there are errors, bugs, or ugly outputs, paste the issue into a coding AI and get a fix.
- **Customize it.** Change the title, description, and example inputs so it looks like *your* tool, not a template.
- **Test it seriously.** Try 5-10 inputs that a real user in your domain would actually type. Note where it works and where it doesn't.

**Then think about Space 3.** This is your ambitious Space — the one that shows what you can do. It might be a bigger model, a multi-step pipeline, a more polished interface, or a completely different approach to your domain. You don't have to build it yet, but you should be able to describe it by Session 9.

Ideas for Space 3:
- Chain two models together (if that fits your project — tonight's session showed you how)
- Use a larger or more specialized model
- Add features your domain audience would actually need
- Build a comparison tool that lets users see the difference between models
- Create something that solves a real problem for a specific person

---

## Journal Entry (15 min)

Open `research-journal.md` and add your Week 8 entry:

```markdown
## Week 8 — Improving and Planning

### What I Improved in Space 2
(What did you fix, change, or add? How does it work now compared to the first version?)

### What I Learned from Class
(Quick note on pipelines and error cascades — anything useful for your project? If not, what else stuck with you this week?)

### My Plan for Space 3
(What's your ambitious Space going to be? What will it do? Who is it for? What makes it different from Space 2?)
```

**Not sure what to write?** Read [Prea's Week 8 journal entry](../example-student-prea/research-journal.md). Notice how specific her improvements are (not "I made it better" but "added a confidence check that warns below 20 words"), how honestly she handles her first small-n numbers, and how directly she maps tonight's error-propagation topic onto her own pipeline. Your entry should follow the same arc: what you improved, what you learned, and where you're headed — with specifics, not generalities.

---

## Portfolio Check

By Session 9, you should have:
- Space 1 running (your baseline)
- Space 2 polished and working well
- 4 journal entries in `research-journal.md`
- A plan for Space 3
- A Hugging Face Collection with 8+ items

**Reference:** Prea's three-Space arc is mapped in her [portfolio README](../example-student-prea/README.md). By Week 8, Prea had a working sentiment-comparison Space (Space 1), a polished Delivery Analyzer built on the Whisper API (Space 2), and the beginnings of a plan for a two-factor WSDC judge assistant (Space 3). Your arc will look different, but the shape — baseline, domain-specific, ambitious — should be similar.

---

## Your Personal Challenge

### Annabelle
Your Space 2 should be deployed. This week, make it yours — customize the examples, fix any rough edges, and test it with content that matches your style. For Space 3, think about what would make someone say "this is really cool." What's the most ambitious thing you could build with what you know?

### Bobby
Polish your model comparison lab. Make the game writing prompts specific and interesting — the kind of thing you'd actually want to test. For Space 3, think bigger: could you build a game dialogue generator that lets you pick a genre, a character type, and a tone?

### Chengry
Your medical NER or upgraded text generator should be working. Refine it — test with real medical text and note where it succeeds and fails. For Space 3, think about your DxAI vision. What's the most impressive version of a medical AI tool you could build on free CPU?

### Emily
Polish whichever Space 2 you built — the comparison lab or the better summarizer. Test it on real news articles. For Space 3, think about what a journalism tool should actually do. What would a reporter or editor want from an AI assistant?

### George
Refine your health-focused Space. Test it with real health content and note what works. For Space 3, think about audience: who would use a health AI tool? A patient? A student? A caregiver? Design for that person.

### Henry
Polish your scene description Space or whichever direction you went. For Space 3, think about combining your visual and text interests — that could be a really distinctive project.

### Sevilla
Refine your emotion or image Space. For Space 3, lean into what makes your project different from everyone else's. You have strong instincts about what AI gets wrong emotionally — build something that shows that.

### Shawn
Your comparison lab should be working well. Polish the interface and test systematically. For Space 3, think about scale: could you compare more models, or add a new dimension to the comparison? Your methodical approach is your strength — push it further.

---

AI + Research Level 2 • Session 8: Improving and Planning

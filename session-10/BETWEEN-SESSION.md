# Between Sessions 10 & 11

This week's homework has three parts: getting your Space working, a research journal entry, and GitHub uploads. Plan for about 1-2 hours total. This is the most important between-session work of the whole course.

---

## Part 1: Hub Challenge — Get Your Space Working

In class you did **end-to-end system design** — choosing a question, a model, and building a complete tool. Your Space is YOUR project — the thing you'll present on Demo Day (Session 12).

Now make sure it actually works, and think about **your own design choices**.

### Option A: Stay with Sentiment

1. Visit your Space URL. Does it load without errors?
2. Test with **5 different inputs** — vary length, tone, and topic:
   - A clearly positive input (baseline)
   - A clearly negative input
   - Something neutral or ambiguous
   - Something very short (one word)
   - Something very long (a full paragraph)
3. For each input, ask yourself:
   - Does the output make sense?
   - Would your target audience understand it?
   - Is the suggested action helpful?
4. **Fix the worst result.** Can you change the code, examples, or output formatting to handle it better?
5. **Bonus:** Have someone outside the class try it. Don't explain anything — just share the URL.
6. **Update your Collection** with any models or Spaces that inspired your build

### Option B: Explore Your Own Topic

1. Visit your Space URL. Does it load without errors?
2. If it's broken, check the "Logs" tab on Hugging Face for error messages. Common fixes:
   - Missing import → add it to `app.py`
   - Missing package → add it to `requirements.txt`
   - Model too large → switch to a `distil-` variant
3. Test with **5 different inputs** that your target audience would actually use
4. For each input:
   - Does the model give a reasonable result?
   - Is the output framed for your audience (not for programmers)?
   - What would you change?
5. **Fix one thing.** Improve the title, add a better example, or reformat the output.
6. **Update your Collection** — add a tasting note about why you chose this model and what you learned building with it

The key idea is the same either way: **you chose a question, a model, and a design. Now test whether your choices work.** That's the research cycle — build, test, iterate.

### Checklist

- [ ] Space loads without errors
- [ ] All example inputs produce reasonable output
- [ ] Title is clear to someone who doesn't know AI
- [ ] Description explains who this is for and what it does
- [ ] Tried 5 weird inputs (emoji, gibberish, empty, very long, very short)

### Bring It Back

Next session, bring your working Space URL, one thing you're proud of, and one thing you want to improve.

### SpaceCraft Resources

Now that you're building your own Space, three parts of SpaceCraft are especially useful:

- **[Build Guides](https://buildlittleworlds.github.io/spaceCraft/guides.html)** — Annotated walkthroughs of three leaderboard Spaces showing how they're built. If you're stuck on architecture decisions, study the one closest to your pattern (API wrapper, specialized model, or data dashboard).
- **[Student Showcase](https://buildlittleworlds.github.io/spaceCraft/showcase.html)** — Where the best student Spaces from each cohort are featured. Your Space could end up here after Demo Day.
- **[Chapter 8: Designing for Your Audience](https://buildlittleworlds.github.io/spaceCraft/design.html)** — The craft checklist at the bottom is a pre-flight check for your Space before you share it.

### Looking Ahead

You just did the synthesis — every concept from the course embedded in one build. But a first draft is just a first draft.

Next session is about the experimentation loop. You'll swap Spaces with classmates. They'll try inputs you never thought of — the way we broke models back in Session 3 with sarcasm and ambiguity. You'll get feedback, and then you'll iterate. Build, test, improve.

Before next session, ask yourself: what's the one input that breaks my Space? If you can find it before your classmates do, you're already iterating.

---

## Part 2: Research Journal Entry

Add your Week 10 entry to `research-journal.md` in your GitHub repo. This is your most important entry — you're documenting the choices behind your own project. 300-500 words.

### Week 10 Entry

```markdown
## Week 10 — End-to-End System Design (My Own Build)

### This Week's Method
(What research method did we learn? Hint: end-to-end system design — choosing a question, selecting a model, and building a research prototype.)

### How I Applied It
(What did you build? What model did you choose and why? What task does it perform? Who is it designed for?)

### What I Expected
(Before building — did you think this model would work well for your task? Did you expect the build to be easy or hard?)

### What I Found
(What actually happened? Does the model do what you expected? What inputs work well? What inputs break it?)

### Why I Think This Happened
(Your explanation. Connect it to the model's training data, the task it was designed for, and the choices its creators made.)

### Limitations
(What can't your Space do? What would you need to make it better? Is the model good enough for your intended audience?)

### What I Want to Try Next
(What will you improve for Demo Day? What's the one thing that would make the biggest difference?)
```

If you're not sure what to write, start with: why did you choose this model, and does it actually do what you need? That's the core of research methodology — justifying your methods.

---

## Part 3: Grow Your Collection + GitHub

### Collection

Your Collection should have at least **12 models and 7 Spaces** by Session 11. For your newest items, include tasting notes that connect to your project — what did you learn from exploring this model that informed what you built?

### Notebook

Keep experimenting with your model in the Session 10 notebook. Push it to your GitHub repo when you're ready.

### GitHub

Upload this week's notebook to your `my-ai-portfolio` repo:

1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**
4. Open `research-journal.md`, click the pencil icon to edit, add your Week 10 entry below the Week 9 entry, and commit

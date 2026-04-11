# Emily — Research Path

This file is your guide from "I'm interested in politics, international relations, and news" to a real research question, a proper journal, and a written brief. It is modeled on what Prea did for debate speeches — read [her journal](../example-student-prea/research-journal.md) and [her research brief](../example-student-prea/research-brief.md) to see the end product.

---

## Step 1: Start Your Journal (Do This First)

You have no journal entries yet. You're starting fresh, which means you don't have to catch up—you get to start thinking deliberately about what you've noticed and what you want to explore.

Write your first entry this week. Here's what to include:

**What have you noticed about AI and news/politics so far?** This could be from class, from testing tools on your own, from conversations, from anything. Examples:
- "When I ask AI tools to summarize political news, they sometimes flatten competing viewpoints into a single narrative."
- "I tested three different AI tools on the same news article and got three very different summaries."
- "Some AI models seem to favor certain political framings or word choices over others."
- "News-writing models get facts right but sometimes miss nuance about why something matters politically."

Be specific. Use real examples from things you've actually tested or read.

**What about this interests you?** Why does this gap or pattern matter? Connect it to your interests in politics, IR, and ethics. Examples:
- "This matters because news summarization affects how people understand complex political issues."
- "If AI tools systematically favor certain political framings, that's an ethics problem."
- "I want to understand whether small, free AI models can be trusted to handle politically sensitive information accurately."

**What do you want to explore?** Don't commit to a research question yet—just say what draws you. Examples:
- "I want to test whether different AI models treat opposing political viewpoints differently."
- "I want to see whether news-generation models introduce political bias or just factual errors."
- "I want to understand how AI summarization affects the 'balance' of a political news story."

Your entry doesn't have to be long. A few paragraphs is fine. The point is to name what you've noticed and what you want to dig into. Write this after this week's class.

---

## Step 2: Sharpen a Research Question

You are interested in politics, international relations, news, and ethics. That is a topic, not a research question. A research question has to be something you can *investigate* — something with an answer you don't yet know.

Here is how your topic connects to the kind of question that could drive a research brief:

**Your observation so far:** You've been looking at news-related Spaces (your collection shows that). You've probably noticed that different AI tools handle political news differently. You care about whether those differences are accurate, fair, and ethically sound.

**The move from observation to question:** Prea noticed that sentiment models could read *what* she said but not *how* she said it. That gap became her research question. You need to find your equivalent gap. Here are three candidate questions at different levels of specificity, written for your topic:

**Broad:** "Do small, free AI models handle political news fairly, or do they introduce biases, simplifications, or framings that distort the original reporting?"

**Medium:** "When a small text-generation model is given a news article about a politically contentious topic, does the model's summary preserve the original article's political balance and nuance, or does it flatten competing perspectives?"

**Narrow:** "On a set of 10 news articles about politically divisive topics (chosen from different outlets and perspectives), how do three small AI models (distilgpt2, SmolLM2-360M-Instruct, and Falconsai/text_summarization) differ in their summarization? Specifically, do instruction-tuned models preserve political perspective better than non-instruct models? And do any of the models systematically introduce political framings that weren't in the original text?"

Notice the structure: the broad question is a conversation starter. The medium question identifies a specific gap you could test. The narrow question describes an experiment you could actually run with your existing tools.

**Your exercise for this week:** Run a question-sharpening conversation with one of your AI tools. Paste this into Claude, ChatGPT, Gemini, or whichever you prefer:

```text
I'm a high school student taking an applied AI course. I'm interested in politics, international relations, and ethics. My special interest right now is how AI tools handle political news and information—whether they're fair, accurate, and preserve competing viewpoints or whether they introduce bias, simplification, or political framing.

I've tested some AI summarizers and noticed they handle political topics differently than neutral topics. I want to write a short research brief about this but I don't have a research question yet—I just have observations and concerns. Can you help me sharpen this into a researchable question?

Also, I have Model UN experience, so I understand political terminology, competing interests, and how language is used to frame arguments. That's probably relevant to my angle on this project.

Don't give me the answer. Give me three candidate questions at different levels of specificity, and explain what would count as evidence for each one.
```

Save the conversation and the question you pick in your journal as part of your Week 1 entry.

---

## Step 3: Connect to Published Research

After you have a question, the next step is finding out if anyone else has studied something related. This is where Consensus comes in (we'll cover this in Session 7). But here are some search directions that connect to your politics-and-news interest:

- *"AI bias in news summarization"* — Do language models introduce political bias when summarizing news?
- *"political text generation NLP"* — How do researchers study whether language models can handle political language fairly?
- *"automated news summarization accuracy"* — What does the literature say about how good automated summarization actually is?
- *"perspective and framing in NLP"* — Are there papers about whether AI tools preserve or flatten different political perspectives?
- *"bias in language models news"* — Specifically, do pre-trained language models inherit political biases from their training data?

You don't need to read full papers yet. Just find 3–5 that seem relevant and note their titles and what they seem to be about. Prea found her first sources in Week 3 and didn't read them carefully until Week 8. The point right now is to know the territory exists and to ground your question in what researchers have actually studied.

---

## Step 4: What Your Three Spaces Should Look Like

You currently have no Spaces. That's your starting point. For the research brief, you want three Spaces that tell a story together—not just three separate experiments, but a sequence that builds:

**Space 1 (baseline):** A simple news generator or summarizer using one model and basic controls. This is the "before" picture. Prea's Space 1 was intentionally limited—it existed to show what *didn't* work or what was missing. Your Space 1 might be a news-drafting tool using `distilgpt2` (the simpler, older model) or a straightforward summarizer using the class baseline. The point is simplicity so you can measure what a basic version does.

**Space 2 (the experiment):** This is where your research question lives. If your question is about whether instruction-tuning preserves political balance better, this is the Space where you compare models side-by-side on the same political articles. If your question is about whether summarization flattens competing perspectives, this is the Space where you test that systematically. SPACE-PROMPTS.md already has a model-comparison prompt (Prompt 2) that you can use.

**Space 3 (the full version):** The Space that combines what you learned from Space 1 and Space 2 into something more useful. If Space 2 showed you that one model does better on political balance, Space 3 might be that model with better controls. If Space 2 showed you that perspective-preservation matters, Space 3 might flag when a summary is missing viewpoints.

You don't have to start from scratch. SPACE-PROMPTS.md already has five ready-to-use prompts for building these. Just paste them into ChatGPT or Claude and use the code they generate.

---

## Step 5: Your Unique Angle—Domain Expertise in Politics

Here's something no other student in this cohort has as clearly as you do: serious experience thinking about competing political perspectives, IR dynamics, and the nuances of political language. Model UN taught you to read political arguments carefully and to understand why different groups frame issues differently.

Most of this cohort will test AI models on generic tasks. You can evaluate AI outputs on political text with real domain knowledge. If an AI tool misses a crucial IR concept or flattens a political distinction that matters, you'll *know* it because you've studied politics. That's a research superpower. Your unique contribution is not just testing models—it's testing them with the kind of critical reading that a political analyst or journalist would bring.

Think about whether your research question could leverage this. *"When small AI models summarize news articles about politically contentious topics, do they preserve the political nuance a real journalist or policy expert would care about, or do they flatten competing viewpoints?"* — that question plays directly to your expertise.

---

## What Prea Did That You Should Notice

Read [Prea's journal](../example-student-prea/research-journal.md), especially:

- **Week 1** — Notice how she tested the class tools on *her own material* (debate transcripts), not generic inputs. Do the same: test models on political articles that matter to you, or on news about topics you care about. Don't test on random examples.

- **Week 3** — Notice the Consensus detour. She went from "I think prosody matters" to "here are three papers that say it does" in one search session. Your version of this is finding out what the literature says about AI bias in news and political text. Don't skip this step.

- **Week 4** — Notice how she committed to a specific hypothesis. You don't need one yet, but you need to be working toward one. By the end of Week 2, you should have a research question that you've sharpened with an AI tool *and* grounded in published research.

- **Weeks 5–7** — Notice the architectural pivot. She tried something, it failed, and the failure became the most interesting part of her story. If a Space you build doesn't work perfectly, that's not a problem for your journal—it's material. The question is: why did it fail? What does that tell you about how the model works?

- **Week 8** — Notice how she set up a careful test. She recorded clips, collected data, and designed a comparison. Your equivalent might be: pick 10 news articles from different outlets about different political topics, run them through your three models, and note what each model does. Then think about what counts as "good" summarization on political text.

- **Week 11** — Notice the voice. Prea cites sources, hedges her claims ("Spearman ρ = 0.63 on n=20 is a pilot, single-rater, small-scale. None of this would survive a real evaluation."), and is explicit about what counts as evidence versus what counts as a hunch. That's the voice to aim for. You're not writing a polished research paper. You're writing an honest notebook about what you tested and what you learned.

The voice matters as much as the content. Match Prea's tone: curious, specific, willing to say when something surprised you, clear about your limitations.

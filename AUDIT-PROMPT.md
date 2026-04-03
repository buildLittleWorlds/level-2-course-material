# Prompt: Audit Level 2 Course for Sentiment Analysis Overemphasis

Run this prompt in plan mode in a new conversation from the `youth-horizons` directory.

---

## The Task

I need a complete audit of the Level 2 course materials to remove sentiment analysis as a through-line after Session 3. The course lives in `level-2-active/course/` (which is a symlink to `level-2-course/`, which has its own git repo linked to `buildLittleWorlds/level-2-course-material` on GitHub).

## Background

This is a 12-session AI course for G7-11 students who don't code. The course arc:

- **Sessions 1-3:** Students explore AI through sentiment analysis and classification. This is intentional — sentiment is a concrete, relatable entry point for understanding supervised learning. Students feed text to models, compare outputs, and test edge cases.
- **Session 4:** The fork. Students cross from classification to generation. One line of code changes from `pipeline("sentiment-analysis")` to `pipeline("text-generation")`. This is the biggest conceptual shift in the course.
- **Sessions 5-6:** Students build generative Spaces (text generator with sliders, summarizer with controls) and test them across domains. These sessions were just revised into workshop format — they should be clean.
- **Sessions 7-8:** Bias testing and multi-model pipelines.
- **Sessions 9-12:** Student projects — redesign for an audience, independent build, iterate, present.

## The Problem

The course was originally designed with a broader ML focus. I then restructured it heavily around sentiment analysis as the unifying example, thinking it would be more concrete for students. I went too far — sentiment analysis became the assumed activity in nearly every session, including sessions where students should be working on their own topics with generative models. I've done partial revisions, but sentiment analysis residue remains throughout.

## The Principle

**Sessions 1-3:** Sentiment analysis is the primary example. This is correct. Keep it.

**Session 4 onward:** Sentiment analysis should appear ONLY as brief backward references ("remember when we classified text as positive or negative? That was supervised learning"). It should NOT be:
- The assumed model type students are using
- The Space students are building or testing
- The example in homework assignments
- The through-line in instructor guides or slides
- Referenced by specific Space names like "Sentiment Showdown" (which doesn't exist)

**What should replace it:** After Session 4, the course should be driven by two things:
1. The ML concepts being taught (hyperparameters, domain shift, bias, pipelines, etc.)
2. Student interest — each student has their own topic (medical AI, game development, creative tools, emotion detection, news analysis, image generation, etc.)

## What to Audit

Check every file in sessions 4 through 12 for sentiment analysis overemphasis. The relevant folders are:

```
level-2-course/session-04/
level-2-course/session-05/
level-2-course/session-06/
level-2-course/session-07/
level-2-course/session-08/
level-2-course/session-09/
level-2-course/session-10/
level-2-course/session-11/
level-2-course/session-12/
```

Also check these course-level files:
```
level-2-course/CURRICULUM.md
level-2-course/COURSE-STRUCTURE.md
level-2-course/README.md
level-2-course/supplementary-datasets.md
```

And the SpaceCraft reference site:
```
hugging-face-spaceCraft/
```

For each file, look for:

1. **"Sentiment Showdown" references** — This Space does not exist. Any reference to it is leftover from an abandoned design. Remove completely.

2. **Sentiment models as the assumed activity** — References to `distilbert-base-uncased-finetuned-sst-2-english`, `cardiffnlp/twitter-roberta-base-sentiment-latest`, `nlptown/bert-base-multilingual-uncased-sentiment` as THE models students are using (not just as examples mentioned in passing).

3. **Homework framed around sentiment analysis** — Between-session challenges that assume students are working with sentiment models rather than their own chosen topics.

4. **Instructor guide segments built around sentiment demos** — Live-build segments, demo sequences, or discussion questions that assume sentiment analysis is what's happening in class.

5. **Slides that frame sentiment as the course activity** — Slide content that positions sentiment analysis as the ongoing focus rather than a Session 1-3 example.

6. **Notebook exercises using sentiment pipelines** — Colab notebooks that load sentiment models for exercises in sessions 4+.

7. **Guide cards (GUIDE-*.md) with sentiment-specific framing** — Research method cards that frame the method specifically through sentiment rather than through the student's own topic.

## What to Preserve

- Sessions 1-3 sentiment content — leave as-is
- Brief backward references like "remember from Sessions 1-3 when we classified text..." — these are fine
- Session 7's use of a sentiment model for bias testing — this may be legitimate (sentiment models are good examples of bias because labels like positive/negative are subjective). Flag it for review but don't automatically remove it.
- Session 8's use of sentiment in the image-to-sentiment pipeline — the pipeline concept requires chaining two models, and sentiment is a reasonable second model. Flag for review but don't automatically remove it.

## What to Replace With

When you find sentiment-specific content that needs to change, the replacement should be:
- **Generic model references** that work for any student's chosen task (classification, generation, summarization, zero-shot, etc.)
- **Student-interest-driven framing** ("test YOUR model on YOUR topic" rather than "run this through the sentiment model")
- **Generative model examples** where the session concept works better with generation (as was done in Sessions 5-6)

## Deliverable

Produce a plan with:

1. **An inventory** — every file with sentiment analysis content, what kind of content it is (Sentiment Showdown reference, assumed activity, homework framing, etc.), and severity (must fix / should fix / fine as-is)

2. **A session-by-session action list** — for each session 4-12, what specifically needs to change in each file, with enough detail to execute

3. **A list of files that are clean** — so I know what doesn't need touching

4. **Recommendations for Sessions 7 and 8** — whether the sentiment usage there is legitimate or should be replaced, with reasoning

The plan should be executable — specific enough that a new conversation can implement the changes file by file.

## 8 Students (for context on "student interest")

- **Bobby:** Game development, creative/generative AI
- **Annabelle:** Creative/playful AI, music generation
- **Shawn:** Image generation comparison
- **Chengry:** Medical AI (built a disease identification tool)
- **George:** Medical/health AI
- **Emily:** News, research, information management tools
- **Henry:** News sentiment, computer vision
- **Sevilla:** Emotion detection, news testing

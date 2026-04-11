# Annabelle — Research Path

This is your step-by-step guide to moving from building Spaces to writing research. You have already done the hardest part — actually building things that work and iterating on them. This is about learning to write about what you know.

---

## Step 1: Upgrade Your Journal Entries

You have journal entries. You have tested things. Now you need to extract the research questions hiding inside those entries.

**How:** Re-read your existing journal entries on Spaces, Models, and Creating Spaces. For each entry, ask yourself these four questions and write down the answers:

1. **What did I expect?** What did you think would happen before you tested it?
2. **What actually happened?** What did you observe?
3. **Why did that happen?** What explains the gap between expectation and reality?
4. **What question does this raise?** If you ran the experiment again but changed one thing, what would you want to know?

**The Difference:**

Here is what your journal sounds like now (example from descriptive observations):

> "I tested the Opera-Generator Space with the prompt 'write an opera libretto' and it produced a lot of text. The output had some musical vocabulary but also a lot of generic description."

Here is what it should sound like (analytical version):

> "I tested the Opera-Generator Space expecting it to recognize 'opera' as a specific genre with conventions — formal recitatives, structured arias, repetition for dramatic effect. Instead it produced generic lyrics that could describe any musical scene. This raises a question: when I give a small instruction-tuned model a genre label, does it actually understand what makes that genre distinct, or does it just output high-probability music words? To test this rigorously I would need to collect outputs in multiple genres and score them on genre-specificity, not just on whether they sound musical."

Notice the second version has a clear expectation, a comparison to what actually happened, and a follow-up question that *could be tested*.

**Model to follow:** Read Prea's Week 3 entry in the example student folder (`example-student-prea/research-journal.md`, starting at "Week 3 — Adversarial Testing and the Consensus Detour"). Notice how she structures it:

- What method did I use?
- What did I expect?
- What did I find?
- Why did this happen?
- Limitations of this approach.
- What do I want to try next?

You have been doing this in your head. Now write it on paper.

---

## Step 2: Sharpen a Research Question

You have been exploring "music and AI" for weeks. It is time to crystallize that into a question you could actually test.

### The Progression

**Broad (too broad for a portfolio):** "Can small text-generation models produce genre-specific musical writing?"

This is real, but it is a research program, not a research question. It does not tell you what you are measuring, what counts as success, or what models you are testing.

**Medium (testable, but still diffuse):** "When a small instruct model is asked to write in opera style vs. jazz style, does the output actually use genre-specific vocabulary and structure, or does it produce generic 'music words'?"

This is better. You have a clear comparison (opera vs. jazz), a clear input (genre labels in prompts), and two things you are measuring (vocabulary specificity and structural patterns). But "does it or doesn't it" is still a yes/no question. Research usually asks *how much* or *in what way*.

**Narrow (specific enough to be your portfolio question):** "Testing three small instruction-tuned models on 12 prompts across three genres (opera, jazz, classical), measuring genre accuracy, musical vocabulary specificity, and prompt-following, to determine whether instruction-tuning improves genre distinction more than it improves general writing quality."

This is your actual research question. It is specific about:
- Which models you are testing (three of them — you pick which three)
- How many prompts (12)
- Which genres (opera, jazz, classical — your expertise plus a baseline)
- What you are measuring (three scoring rubrics)
- The comparison you care about (does instruction-tuning help genre-specific writing more than general quality?)

### Your Customized Prompt

Once you settle on a question, you need a prompt template. Here is a skeleton:

```
You are a music writing assistant. Your task is to write a short piece 
of [GENRE] music in the style of [STYLE-DETAIL]. 

Key requirements:
- Use vocabulary specific to [GENRE]
- Follow the structural conventions of [GENRE]
- Keep it to 2-3 stanzas or 8-12 bars

Now write:
```

Test this on:
- **Opera:** "write a formal recitative for a soprano character expressing doubt"
- **Jazz:** "write a jazz standard song lyric with harmonic language and swing idioms"
- **Classical:** "write a classical song with formal structure and romantic sensibility"

Then vary the style details and see if the model can distinguish them, or if it produces the same output regardless.

---

## Step 3: Connect to Published Research

You need to know what already exists. This is not about reinventing the wheel — it is about standing on existing shoulders.

**Run these Consensus searches** and keep rough notes on what you find:

- `"music generation language models genre"`
- `"AI text generation musical style classification"`
- `"computational creativity music composition"`
- `"music education AI tools evaluation"`

**What you are looking for:** Papers that ask questions adjacent to yours. You probably won't find a paper on "small models generating genre-specific opera and jazz lyrics" — that is too specific. But you might find papers on:
- How music models distinguish between genres
- How human listeners evaluate AI-generated music
- Whether computational models capture genre conventions
- How to evaluate creative AI outputs

**Write down:**
- Paper title and authors
- What question they asked
- How their approach differs from yours (different models? different evaluation method? different genres? different measurement?)
- One key finding

This is the backbone of your "related work" section later. You do not need a lot of papers. Three to five solid sources is enough for a portfolio research brief.

---

## Step 4: What Your Three Spaces Should Look Like

You have seven Spaces. Not all of them are portfolio centerpieces.

**Here is the story you should tell with your three:**

**Space 1 — Baseline:** Opera-Generator (RUNNING)

What it shows: A small model generating text when given a genre label. Demonstrates the baseline — what does the model produce with minimal guidance?

What it is good for: Showing the raw behavior of the model before you add anything sophisticated.

**Space 2 — The Experiment:** Music-Starter-Opera-Jazz (RUNNING)

What it shows: The same model, but with more structured prompts that compare opera vs. jazz side-by-side. This is where you actually test the hypothesis — does the model produce different outputs for different genres, or the same generic music words?

What it is good for: Demonstrating that you can *test* a hypothesis, not just observe model behavior.

**Space 3 — The Full Version:** Either nyssma-trainer (RUNNING — your debugged victory) OR a new Music Genre Model Lab

What it is good for: Scaling the comparison up. If Space 2 is "can I distinguish opera and jazz," Space 3 is "can I do this across three models and systematically score the results?"

The nyssma-trainer is already impressive as a standalone project (you took a YAML file and debugged broken code to make it useful in minutes, without prompting). The question is whether it tells the research story or whether a dedicated "Genre Model Lab" would better show the arc from baseline → experiment → full evaluation.

**What this means:** The other four Spaces (silly-phrase-finder, dictionary, dino-fact-explorers, Creative-Story-Starter) are supporting work. They are important for what you learned building them. But they do not belong in the portfolio centerpiece because they do not tell the story about music and genre. You can mention them in your journal as *process*, but the three you choose should form a narrative.

---

## Step 5: Your Unique Angle

You have something that Prea does not and that most students do not: **NYSSMA context**.

NYSSMA (New York State School Music Association) is a real music education standard. You have trained within it. You understand opera and jazz not as genres in the abstract, but as living traditions with real pedagogy. That experience matters.

**Your unique contribution is not "I built AI tools." Your unique contribution is "I built AI tools to investigate a specific problem in music education — can computational models distinguish between the genres I actually study?"**

The nyssma-trainer Space is a portfolio piece an admissions reader would notice. It is not just a random model interface. It connects AI to music education practice. That is the angle.

When you write up your research brief, lead with that. Not "I like music and AI." But "As a classically trained musician, I care about whether AI tools can capture genre-specific writing conventions, which matters for music education and composition pedagogy."

---

## Step 6: What Prea Did That You Should Notice

Prea's journal is not longer than yours. But it has a different *shape*.

Read her Week 5 entry ("Space 1 and a Blog Post That Changed My Plan"). Notice:

- She explains *why* she built Space 1 badly on purpose
- She found an external source (Mistral blog post) and explained how it shaped her thinking
- She explicitly states the problem it created ("Mistral's API is not free")
- She writes the "insight sentence" in all caps because it matters
- She ends with "What I Want to Try Next" — a specific, testable next step

**The writing quality difference is not about length. It is about:**
- **Framing:** "Why am I doing this?" not just "I did this."
- **Evidence:** "Here is what the output looked like" not just "the output was interesting."
- **Reasoning:** "This happened because..." not just "This happened."
- **Questions:** "What does this observation raise?" not just "I observed this."

You have already built like Prea. You need to write like Prea.

---

## What Comes Next

Once you have upgraded your journal entries and solidified your research question:

1. **Research brief** — A 3-4 page document in the format of a mini research paper. Abstract, Introduction (with your research question), Related Work (from Consensus searches), Methods (what you tested and how you measured it), Results (what you found), Limitations (what you could not test or what biases might affect your findings).

2. **Space selection** — Pick your three Spaces and make sure each one has clear, short documentation of what it does and what it shows about your research question.

3. **Journal finalization** — Make sure your journal tells the story from "I wonder if..." through "Here is what I tested" through "Here is what I learned."

The Spaces you have already built are the hard part. The writing is the final step, and it is where you earn the "research" part of "AI + Research Level 2."

You have got this.

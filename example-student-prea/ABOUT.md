# About This Example Student

This folder contains the complete work of **Prea Callahan**, a fictional student in AI + Research Level 2. Prea is the example student for this course — a portrait of what the full arc of the course can look like when a student works on a research question with real rigor, sharpens it over the first few weeks, and ends with a short written research brief she could hand to an admissions officer.

Prea is not a real person. Everything in this folder — the journal, the Spaces, the portfolio page, the research brief — was written as an example for students to see what the course's research work looks like when it's done fully and carefully.

## Who Prea is

Prea Callahan is a Grade 11 student at a public high school in the Greater Toronto Area. She has been debating since ninth grade in the World Schools (WSDC) format and is a member of her school team. She plans to apply to universities in fall 2026 and is interested in programs that mix cognitive science, linguistics, and computer science. She came into AI + Research Level 2 already knowing what she wanted to investigate: *why do some debate speeches feel more persuasive than others, and could an AI tool help measure the difference?*

She is not a coding prodigy. She took one Python class in tenth grade and has used Google Colab a few times for a biology project. She is, however, a practiced reader — she reads essays and nonfiction for fun, annotates her books, and is already comfortable tracking down sources. That background shapes everything about how her journal reads: she cites things, she hedges her claims, and she is careful about the difference between "I found" and "the literature says."

## Her research question

Prea enters the course with a vague version of the question and sharpens it across the first four weeks. By Week 4 she has committed to a formal hypothesis:

> **Acoustic-prosodic features of a short persuasive speech (speaking rate, pause frequency, pause duration, and speaking-rate variance) correlate with listener ratings of persuasiveness, and a pipeline that combines prosodic features with LLM-based content analysis produces more useful feedback than either modality alone.**

She spends the rest of the course trying to test a miniature version of this hypothesis on 20 clips (10 TED talks and 10 student WSDC practice speeches, including her own and her teammates') using only free tools.

## Her arc

Prea's project moves through three Spaces that mirror the course structure, but the architectural story is unusual. In Week 5 she builds the standard distilgpt2 baseline and around the same time her instructor hands her a Mistral blog post about the Voxtral speech-to-speech pipeline. She is excited by the architecture — transcription with word-level timestamps, LLM reasoning over the transcript, all cleanly separated — but she notices the Mistral API is not free and decides she wants a version of the same pipeline that her classmates could reproduce without a credit card on file. In Week 6 she tries the opposite approach, loading a local wav2vec2 audio-emotion model directly into a Hugging Face Space, and watches it time out on free-tier CPU. That failure becomes the pivot: she realizes the Mistral architectural pattern is correct but she needs free components. From Week 7 onward she builds everything as a thin Gradio frontend that calls the Hugging Face Inference API for Whisper-small transcription, computes prosodic features in pure Python from Whisper's word-level timestamps, and sends the transcript to a small instruction-tuned model (also via HF Inference API) for content scoring.

Her three Spaces:

1. **Space 1 (Week 5): Debate Content Scorer (baseline).** A distilgpt2 text playground wired up to "continue" debate speeches on WSDC motions. Intentionally bad — it fabricates rebuttals rather than scoring them. Her journal uses it as the proof that text-only, generator-based approaches can't do what she wants.
2. **Space 2 (Weeks 7–8): Delivery Analyzer.** A thin Gradio frontend that uploads audio to the HF Inference API for Whisper-small transcription with word-level timestamps, then extracts four prosodic features in pure Python: words per minute, pause count above 400 ms, pause-duration variance, and speaking-rate variance across thirds of the speech. No local model loading; the Space boots in seconds.
3. **Space 3 (Weeks 9–10): WSDC Speech Judge Assistant.** The full two-factor pipeline. Audio in → Whisper transcription (via API) → Python prosodic features → transcript also sent to SmolLM2-1.7B-Instruct (via API) with a rubric prompt for content scoring → Gradio interface with three tabs: *Score*, *Breakdown*, and *Coach*. Tested on 20 clips with Spearman correlation analysis.

## Her written artifact

The final document is what most clearly makes Prea's portfolio read as research apprentice work. In addition to a GitHub portfolio README, Prea writes a short research brief — roughly four pages in the format of a miniature research paper, with an abstract, introduction, related work, methods, results, limitations, and references. The related-work section cites six real papers she found by searching Consensus, including Kišiček (2018) on the persuasive power of prosody in argumentation, Pejčić et al. (2015) on pauses and speech rate in political discourse, Koenecke et al. (2020) on racial disparities in ASR systems, and the Mistral Voxtral blog post as an architectural (non-peer-reviewed) reference. The brief is the artifact that reads most obviously like undergraduate research apprentice work — it's the thing parents and admissions readers will actually screenshot.

## How to use this example

- **Don't copy Prea's project.** Her research question is specific to her debate background. Yours should come from wherever your curiosity actually lives.
- **Notice how Prea writes.** She cites sources from Week 3 onward, hedges her claims, and is explicit about what counts as evidence versus what counts as a hunch. That is the voice this course is aiming at. You are not Prea, but the habits in her journal — citing, hedging, distinguishing evidence from hunch — are the habits to imitate.
- **Notice the architectural pivot in Weeks 5–7.** The interesting part of Prea's story is not that she built a working tool — it's that she discovered an architectural pattern (thin client over API) from a blog post, tried the wrong approach first, hit a compute wall, and then pivoted to a free version of the right approach. That kind of informed failure is what research actually looks like.
- **Notice the research brief.** The brief is the artifact that turns a portfolio into something that reads like research, and it's the kind of thing that's worth showing to an admissions reader or keeping in your own file as a proof of what you can do.

---

AI + Research Level 2 • Example Student Portfolio

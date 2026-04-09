# Prea's Research Journal

AI + Research Level 2 — Spring 2026

---

## Week 1 — First Impressions

I went into class today already knowing a little bit about sentiment analysis because my English teacher last year showed us an online demo that scored Amazon reviews. What I didn't know was that you could do this kind of thing on your own laptop for free through Hugging Face. Dr. Plate walked us through six pre-built Spaces and had us test inputs. I tried to be a good sport and type in normal sentences, but I mostly ended up typing in lines from my own WSDC speeches, because those were the only things I had memorized that I wanted to know an opinion about.

What I tested in the Mood Meter Space:

- "Climate inaction is killing us." — predicted Negative (94%). Okay, fair. I did mean it to sound urgent.
- "We must act now, before it is too late." — predicted Positive (71%). This one surprised me. When I delivered this line at regionals last November I paused for almost a full second before "now" and the judges wrote "strong finish" on two of my ballots. The model thinks it sounds positive just because of "must act" and "we."
- "The government's policy is indefensible." — predicted Negative (88%). In context this was me on the opposition bench in a round about private schools. It was not a sad line. It was supposed to sound like an accusation.
- "Honorable judges, I put it to you that the burden of proof has not been met." — predicted Neutral (63%). This is the most debate-specific line I typed and the model had the least to say about it. I think that is because the rest of the words are procedural — "burden of proof" doesn't show up in movie reviews.

What I notice, looking back at these four results: the model is reading the *words* but it has nothing to say about *how I said them*. The first line and the third line are about the same topic (climate), but the third is an accusation and the first is a warning, and those feel very different when you are actually delivering them. The model sees both as Negative and does not distinguish between accusation and warning. For a debater, that distinction is most of the point.

I wrote in the margin of my notebook: *the model sees what I said but not how I said it.* I am going to keep that sentence around because I think it might turn out to be the seed of my project.

**Collection so far:** 2 models (distilbert-sst-2, cardiffnlp twitter-roberta), 3 Spaces (Mood Meter, Text Playground, a text summarizer Dr. Plate recommended). Tasting notes on each. For the two sentiment models I wrote tasting notes that compare how they handled my four debate lines, which is maybe more detail than anyone asked for but it is the thing I actually care about.

---

## Week 2 — Comparative Analysis on Transcripts

**This Week's Method:** Comparative Analysis.

**How I Applied It:** I had transcripts of three of my own WSDC speeches from this year because our coach makes us transcribe one speech a month as a self-reflection exercise. (She does not do it to make us miserable. She does it because it is easier to see the filler words when they are on paper.) I ran both `distilbert-base-uncased-finetuned-sst-2-english` (binary sentiment) and `j-hartmann/emotion-english-distilroberta-base` (7-emotion) on the same sentences from each transcript and logged the results in a Google Sheet.

**What I Expected:** I thought the two models would more or less agree, with the emotion model being a slightly more detailed version of the sentiment model. I also thought they might actually track something real about how persuasive each line was, since I already had a gut sense of which lines had worked in the round and which hadn't.

**What I Found:** The two models disagreed constantly. On "The evidence from the 2022 UNICEF report is unambiguous," the sentiment model said Positive (79%) and the emotion model said Neutral (51%) with Surprise as the second label (22%). On "And that, judges, is why the opposition's case collapses under its own weight," the sentiment model said Negative (66%) and the emotion model said Anger (43%) with Sadness second (19%). Neither of those labels feels right to me. The second line is a concluding flourish. It's supposed to sound like a closing statement in a courtroom, not like someone is actually angry.

But the thing that really got me is what happened when I looked at two sentences from the same speech that I *knew* had landed differently. Both sentences were about the same topic (a ban on single-use plastics). I had delivered one of them with a long, deliberate pause before the key phrase and the other in a rushed way because I was running low on time. The judges' ballots explicitly called out the first line and ignored the second. But to the models, the two sentences looked essentially identical — same sentiment labels, within a few percentage points.

**Why I Think This Happened:** The models are reading the text of what I said, not a recording of how I said it. There is nothing in the text to tell them that I paused before "single-use" in one sentence and not in the other. The distinction that mattered to the judges — delivery — is literally absent from the input.

**Limitations:** I ran this on three of my own speeches. That is a sample of one speaker, from one tournament season, in one debate format. I cannot generalize from this to anything. But the observation that the two models disagreed on every line is already interesting even at n=3, because if the models can't even agree with each other, it's hard to imagine either of them agreeing with a human judge.

**What I Want to Try Next:** I sketched a diagram in my journal: `text-features ∪ audio-features → rating`. I think the thing I actually want to build is a tool that takes both the words *and* some measurement of how they were delivered, and produces something closer to what a judge would say. I don't know yet if this is possible with free tools. Dr. Plate said we will get to audio models later in the course and to hold the thought.

---

## Week 3 — Adversarial Testing and the Consensus Detour

**This Week's Method:** Adversarial Testing.

**How I Applied It:** Instead of just feeding the emotion classifier more of my own debate speeches, I decided this week to try to break it on purpose using debate-specific rhetoric. I wanted to find sentences where the model would confidently label something with an emotion that the debater did not mean.

**The Three Best Breaks:**

1. "The government's policy is indefensible and the evidence speaks for itself." — model: Anger (81%). In a debate, this is a completely standard opposition opening move. It is not angry. It is the argumentative equivalent of a handshake.
2. "We stand on the right side of history on this motion." — model: Joy (52%), Surprise (23%). This is one of the most overused lines in high school WSDC debate. It is a rhetorical flourish, not an expression of joy. If I said this sentence to a friend, they would roll their eyes.
3. "Honorable judges, I put it to you that the affirmative has not met its burden of proof." — model: Neutral (68%). This is the most *performative* sentence I could think of — it is the moment in a rebuttal where you turn directly to the judges and point at the flaw in the other side's case. The model saw it as unremarkable because every word in it is a procedural debate word.

**The Pattern:** The model reads debate rhetoric as if it were ordinary emotional speech. It either mis-labels the performative layer as literal emotion (Anger, Joy) or it ignores it entirely (Neutral). In neither case does it detect that the speaker is doing something *with* the words beyond their dictionary meaning.

**The Consensus Detour:** I told Dr. Plate after class that I had a hunch about prosody but no idea if anyone had written about it for public speaking or debate specifically. She showed me Consensus — a search engine that only returns peer-reviewed papers and summarizes them. I ran three searches this week and kept rough notes:

- *"prosodic features persuasive speech"* returned a systematic review by Gomes et al. (2023) in a Brazilian journal called DELTA. The review found that across the literature, faster speech rate and higher intensity are the two features most consistently linked to persuasive impressions. That matches my intuition from my own debates — my best speeches have felt fast.
- *"pauses speech rate persuasiveness political discourse"* returned a paper by Pejčić, Trajković, and Janković (2015) that compared Serbian and English political speech and found a correlation between persuasiveness ratings and pause duration, and also that more persuasive speakers modulated their speech rate within syntactic units rather than keeping it constant. This is almost exactly the experiment I have been imagining, but on political speeches instead of student debate.
- *"persuasion prosody argumentation"* returned a paper by Kišiček (2018) in *Argumentation and Advocacy*, which argues that rhetorical research has somewhat marginalized prosody and that prosodic features play a real role in ethos, pathos, and logos. The journal title alone is a good sign — this is a paper in an argumentation journal, written by someone who takes debate and rhetoric seriously as a subject.

I have not read any of these carefully yet. I read the abstracts and skimmed the conclusions. But the fact that there is already a literature on this exact question is either really good news (people care about it, I can stand on their shoulders) or really bad news (it has already been done, what am I adding). I think it is mostly the first one, because none of these papers used AI tools on student debate speeches, they used human raters on professional political speakers. There may be room for a student project that tries a small version on a different population.

**Limitations:** I am still working with text models, but debate speeches are fundamentally audio events. Everything interesting about this project is going to be in the audio. I also need to be careful about the Pejčić paper specifically — I am going to re-read it closely next week because it sounds so close to what I want to do that I should either be clearly extending it or clearly doing something different.

**What I Want to Try Next:** The session on classification vs. generation is next week. I want to see if that framing helps me pin down what kind of model I actually need. My instinct is that I need a classifier that takes audio features as input and produces some kind of persuasiveness score. But I am not sure whether I can train one of those or whether I should be using a general-purpose audio model to extract features and then doing the scoring separately.

---

## Week 4 — Classification vs. Generation, and the Two-Factor Hypothesis

**This Week's Big Idea:** Classification puts inputs into buckets. Generation produces new things that did not exist before. The two tasks require fundamentally different training data and do fundamentally different work.

**The Demo:** Dr. Plate changed one line in a Colab notebook — `pipeline("sentiment-analysis")` to `pipeline("text-generation")` — and showed us that the same input ("The cat sat on the mat") went from producing a sentiment label to producing a continuation about a cat who got bored and moved to the rug. Same input, totally different output, totally different purpose.

**How I Applied It:** I tested distilgpt2 on a line from one of my own speeches: "The affirmative's case rests on an assumption the data does not support." Three generations later I had:

- "The affirmative's case rests on an assumption the data does not support the argument that the defendant was not aware of the risk of the product." (Legal filler.)
- "The affirmative's case rests on an assumption the data does not support. The data is not a good proxy for a good data set." (Tautological nonsense.)
- "The affirmative's case rests on an assumption the data does not support, and the affirmative's case rests on an assumption the data does not support." (It just looped.)

Then I ran the same sentence through the emotion classifier: Anger (62%), Disgust (14%). Also unhelpful, but at least it returned a label.

**The Fork for My Project:** I spent a long time thinking about this. I do not need a model that *generates* better debate speeches. That would not help me. What I need is a model that *scores* them — a classifier, or at least a regressor. But I have already established over the last two weeks that scoring from text alone misses everything about delivery. So either I need a better classifier that somehow encodes delivery, or I need a different input modality entirely. Audio is the different modality.

**The Hypothesis:** Near the end of the week I wrote down a formal version of what I actually want to test:

> Acoustic-prosodic features of a short persuasive speech — specifically speaking rate, pause frequency, pause duration, and speaking-rate variance across sections of the speech — correlate with listener ratings of persuasiveness at least as strongly as content features do, and a pipeline that combines the two kinds of features produces more useful feedback than either modality alone.

That is a mouthful. But writing it as a single sentence helped me see the shape of the project. It is a *two-factor* design: one factor is prosody (measured from the audio), one factor is content (scored somehow from the transcript), and the interesting question is whether either of them correlates with how I rate the speech and whether combining them does better than either alone.

I re-read the Pejčić et al. (2015) abstract more carefully this week and I think my project is clearly distinct from theirs in two ways: they used a listener perception experiment with 124 participants on professional political speeches, and I am doing something much smaller on student debate speeches with a single rater (myself). The overlap in feature choice is real — they also looked at pause duration and speech rate — but the *population*, the *scoring mechanism*, and the *scale* are all different. I think the honest framing is: "This project attempts a miniature, single-rater version of the Pejčić design on a student debate corpus, using free AI tools to extract the prosodic features automatically."

**What I Want to Try Next:** Next week we start building Spaces. I want to build Space 1 the way everyone else does, as a distilgpt2 text playground, but I want to frame it explicitly as a "Debate Content Scorer" that is intentionally bad at its job. Its failure is going to motivate the pivot to audio.

---

## Week 5 — Space 1 and a Blog Post That Changed My Plan

**What I Built:** My Space 1. Following the class instructions, it is a distilgpt2 text playground. I customized the framing so that instead of being a generic text generator, it is labeled "Debate Content Scorer" and pre-loads three example prompts that are real WSDC motions from this season ("This house would ban private schools"; "This house believes that social media does more harm than good to democracy"; "This house would require wealthy nations to accept climate refugees"). The temperature slider goes from 0.1 to 1.5 and there is a top-p control and a max length control.

**What It Does (Badly):** The "scoring" part is a lie. Distilgpt2 is a generator, not a classifier. What the Space actually does is take a prompt like "The affirmative's strongest argument is" and continue it with whatever the model thinks comes next. At temperature 0.7 on the private schools motion it generated: "The affirmative's strongest argument is that the private schools are not a good place to learn. The private schools are not a good place to learn because they are not." That is not a debate argument. That is a loop pretending to be an argument.

I ran the same prompt at five temperatures (0.3, 0.5, 0.7, 1.0, 1.3) and wrote the outputs in a table in my journal. Lower temperatures loop. Higher temperatures produce more interesting words but say things that are factually wrong (at 1.3 it generated something about "the private schools lobby in Ottawa which controls 43% of the federal budget," which is both fabricated and funny). Nowhere in the range does it produce something you could mistake for a debate argument.

**Why I Built a Broken Space On Purpose:** This is the baseline. Its whole job in my portfolio is to be the thing whose limitations motivated the rest of the project. A generator can produce text that looks like a debate sentence, but it has no concept of whether the sentence is any good and no way to assign a score. To get to scoring I need a different kind of model.

**The Blog Post:** On Wednesday I went to Dr. Plate's office hours and told her I wanted to do something with audio eventually. She pulled up a blog post from Mistral AI titled "Designing a speech-to-speech assistant — From Audio Input to Spoken Response: Building a Triggerable Assistant with Voxtral and Mistral Small." It was from April 2026, so essentially brand new. She said: "This is the architectural pattern you want. Don't worry about the specific Mistral pieces; look at the *shape* of it."

I spent most of the evening reading it. The pipeline Mistral describes has three stages:

1. **Speech-to-text** — a model called Voxtral Transcribe turns audio into text, with optional *diarization* (who is speaking when) and segment-level timestamps.
2. **Assistant LLM** — a text model (Mistral Small, in their example) reads the transcript and does whatever reasoning the use case requires — in their example, answering a question with a web search.
3. **Text-to-speech** — a model called Voxtral TTS reads the answer out loud.

The thing that hit me hardest is the sentence where they explain why the pipeline is designed in stages: *"There are three main components... Speech-to-Text (Transcription)... Assistant LLM (Agent)... Text-to-Speech (Voice Generation)."* The models do not have to live in the same place. Each stage is its own thing. The *client* — the actual program the user interacts with — just calls each stage in order. That means the client does not need to be heavy. It can be a small program that makes HTTP requests.

For my project, I only need the first two stages. I want audio → transcript (with timestamps, so I can compute pause durations) → some kind of scoring. I do not need to synthesize speech back out.

**The Problem:** Mistral's API is not free. Voxtral is a paid service. I have no credit card of my own and I am not going to ask my parents to put one on file at an AI company in France so I can finish a school project. More importantly, even if I paid for it myself, the other students in my class would not be able to run my Space without also paying, which kind of defeats the point of a portfolio that is supposed to demonstrate reproducibility.

**The Insight I Am Writing Down Carefully Because I Think It Matters:** The Mistral architecture is right. The models do not have to live in my Space. The Space can be a thin frontend that makes API calls to models that live somewhere else. I just need to find a *free* version of the same architectural pattern — some way to do transcription-with-timestamps, and some way to do text scoring, without paying anyone.

Dr. Plate suggested Hugging Face's free Inference API as the free-components version of the Mistral architecture. I did not know until this week that Hugging Face has a free Inference API at all. It is rate-limited and slow, but it exists. So the plan is: instead of Voxtral, use Whisper (OpenAI's open-source transcription model) via the HF Inference API. Instead of Mistral Small, use a small instruction-tuned model like SmolLM2 via the HF Inference API. Everything free, all the heavy compute running on Hugging Face's servers, my Space is a thin Gradio frontend.

**What I Want to Try Next:** Before I commit to the API approach, I want to try the *opposite* approach first as a sanity check. I want to try loading an audio model *directly* inside a Hugging Face Space and see what happens. If it works, great, I have a simpler pipeline. If it doesn't work, I will have a real reason to go to the API approach, and I will have evidence for my journal.

---

## Week 6 — The Compute Wall

**What I Tried:** I tried to load `superb/wav2vec2-base-superb-er` (a wav2vec2 model fine-tuned for speech emotion recognition on the SUPERB benchmark) directly inside a Hugging Face Space, with a Gradio audio uploader and a button that runs the model on the uploaded audio and returns the predicted emotion class. The model has about 95 million parameters and the model card says inference should be fast.

**What Happened, in the Order It Happened:**

1. The first build took eleven minutes. Most of that was downloading the model weights and installing torch.
2. The Space crashed on its first boot because I had not pinned the transformers version and the latest version had a breaking change. I fixed that.
3. The second build took nine minutes. The Space booted successfully.
4. I uploaded a 30-second clip of my own voice reading a line from a WSDC speech. The Space showed a spinner for about 25 seconds and then returned a result. ("neutral", 61%.) This is a perfectly reasonable output for a model that was trained on the IEMOCAP dataset, which is American actors reading scripted emotional lines, not a Canadian teenager reading a debate argument.
5. I uploaded a 2-minute clip of a full speech. The Space showed the spinner for about 40 seconds and then returned a 500 error. The logs said the process had run out of memory.
6. I tried to upgrade the model to Whisper-medium for better transcription (I know this is a transcription model, not an emotion model, but I wanted to see if Whisper would even load on the free tier). The Space failed to build. The logs showed `OOM` during the weight loading step.

I wrote all of this down in my journal with timestamps because it felt important to have the evidence. My free-tier Space can load a small audio model and run it on clips under about 45 seconds of audio. Beyond that, it either times out or runs out of memory. My actual project needs to handle full WSDC speeches, which are up to 8 minutes for a main speaker. The free CPU tier cannot do this.

**What This Means:** The local-model approach is not going to work for my project. Not because wav2vec2 is the wrong model, but because the compute the free tier gives me is not enough to run a 95M-parameter audio model on multi-minute clips. I could try harder — I could downsample the audio, chunk the clips, try a smaller model — but every workaround adds complexity to the Space, and the more complexity I add, the less reproducible the project becomes.

**The Pivot Sentence:** I wrote this at the top of the next page of my journal in capital letters because I wanted it to be visible: **THE MISTRAL ARCHITECTURE IS RIGHT. I JUST NEED FREE COMPONENTS.**

The Mistral blog post says: transcription model lives elsewhere, LLM lives elsewhere, client is a thin frontend that calls them. If I do that with Hugging Face's free Inference API instead of Mistral's paid API, I should be able to handle arbitrary-length audio because the transcription does not happen in my Space. It happens on HF's GPU servers. My Space just uploads the audio file, waits for the response, and parses the JSON.

**The New Plan for Space 2:** A Gradio frontend. An audio uploader. A function that POSTs the audio to the HF Inference API endpoint for `openai/whisper-small` with `return_timestamps="word"`. Then a pure-Python function that takes the returned word timings and computes four prosodic features:

1. Speaking rate in words per minute (total words / total duration excluding silence)
2. Number of pauses longer than 400 ms
3. Variance of pause durations
4. Variance of speaking rate across thirds of the speech (to measure whether the speaker modulates their pace, which Pejčić et al. found mattered)

No audio model in the Space. No wav2vec2. No OOM. Just the frontend and a couple of API calls. If this works, the Space will boot in a few seconds and use negligible memory.

**What I Want to Try Next:** I am going to spend all of Week 7 on this. I want Space 2 working by the end of that week. I also want to read the Pejčić paper more carefully, because my four prosodic features should be grounded in something the literature actually says matters.

---

## Week 7 — Bias, and Starting Space 2

**What We Talked About In Class:** Bias in AI models. Dr. Plate walked through examples of sentiment models that score statements about different demographic groups differently even when the only thing that changed was the group name, and then we talked about how ASR systems — speech recognition — have been shown to have racial and accent biases.

**Why This Is Not Just a Side Reflection For Me:** My project is built on Whisper. Whisper is an ASR system. My data is WSDC practice speeches from me and my teammates, and my team includes native English speakers and students for whom English is a second or third language. If Whisper transcribes non-native speakers less accurately, then every downstream feature I compute from those transcripts — speaking rate, pause counts, everything — is going to be less reliable for some speakers than for others. And that means any correlation I find between prosody and my own ratings could be partly an artifact of transcription quality rather than of actual delivery.

I ran two Consensus searches this week:

- *"automatic speech recognition racial bias"* returned Koenecke et al. (2020) in PNAS, with 647 citations. This is the foundational paper. They tested five commercial ASR systems and found that Word Error Rate was almost twice as high for Black speakers as for white speakers (0.35 vs 0.19). The key thing is that this was not about vocabulary or content — the same phrases spoken by Black and white speakers produced different error rates, which traces the bias to the acoustic model itself, not to anything the speakers were saying.
- *"whisper ASR bias dialect"* returned Li et al. (2024) on arXiv, which is *specifically about Whisper*. They ran Whisper on the Corpus of Regional African American Language (CORAAL) and confirmed the bias persists, and also identified a "confounding by provenance" effect where recording quality varied by study location. The second finding matters to me because my team's practice recordings are made in different rooms with different phones, and some teammates have noisier recordings than others.

I am going to cite both of these in my eventual write-up. The honest version of the limitations section on my project has to say: "Whisper has documented performance disparities across speaker groups, and the clips from non-native speakers on my team may be transcribed less accurately, which would propagate into the prosodic feature values. I did not correct for this."

**Starting Space 2:** I also spent the weekend building the first version of Space 2. The Gradio interface is very simple — an audio uploader, a "Analyze" button, and a table output. The hard part was figuring out the HF Inference API call. The documentation was clearer than I expected. The endpoint is `https://api-inference.huggingface.co/models/openai/whisper-small` and you POST the audio file with your HF token in the Authorization header. The response comes back as JSON with a `text` field and, if you set the right parameter, a `chunks` field with word-level timestamps.

The first time I ran it, I uploaded a 30-second clip of myself reading one of my opening statements and got back this (abbreviated):

```json
{
  "text": "The affirmative's strongest argument...",
  "chunks": [
    {"text": "The", "timestamp": [0.0, 0.18]},
    {"text": "affirmative's", "timestamp": [0.18, 0.82]},
    ...
  ]
}
```

That is exactly what I need. From that JSON I can compute all four of my features in pure Python. No local model loading. The Space uses about 50 MB of memory and boots in about 4 seconds.

**What I Still Need To Do:** Clean up the feature extraction code, test on longer clips, and add some display logic to the Gradio output so it shows each feature with a short explanation of what it measures. That is next week's work.

---

## Week 8 — Space 2 Polished, and the First Real Numbers

**What I Improved In Space 2:**

- Added a confidence check: if Whisper returns fewer than 20 words, the Space shows a warning that the clip is too short to compute reliable prosodic features. Below that threshold, a single long pause skews every variance measure.
- Wrote the four feature functions properly. Words per minute is just `total_word_count / (last_word_end - first_word_start) * 60`, excluding the silence before the first word and after the last. Pause count above 400 ms is the number of gaps between consecutive words where `chunks[i+1].start - chunks[i].end > 0.4`. Pause duration variance is the variance of those gap values. Speaking-rate variance across thirds is computed by splitting the chunks into three roughly equal groups by number of words, computing words-per-minute for each third, and taking the variance of those three numbers.
- Made the Gradio output show a small table with each feature, its value for this clip, and a one-sentence explanation of what the feature measures and what a "typical" value looks like based on the five clips I have tested so far.

**The First Real Numbers:** I tested Space 2 on five clips of my own and my teammates' practice speeches, and I wrote the results in a table in my journal. I am going to reproduce the table here because the pattern is worth looking at:

| Clip | Speaker | Duration (s) | Words/min | Pauses >400ms | Pause var | Rate var (thirds) | My rating (1–5) |
|------|---------|--------------|-----------|----------------|-----------|-------------------|----------------|
| P-01 | Me, regionals opener | 87 | 168 | 9 | 0.31 | 21.4 | 4 |
| P-02 | Me, novice tournament | 92 | 184 | 5 | 0.08 | 6.2 | 2 |
| P-03 | Teammate A, semifinals | 104 | 162 | 12 | 0.42 | 19.8 | 5 |
| P-04 | Me, practice against wall | 79 | 192 | 3 | 0.05 | 3.1 | 2 |
| P-05 | Teammate B, practice round | 95 | 171 | 7 | 0.22 | 14.6 | 3 |

Looking at this table, the thing that jumps out is the relationship between the **rate variance across thirds** column and the ratings I gave the speeches. The two clips I rated highest (P-01 and P-03) both have rate variance above 19, meaning the speaker dramatically changed their pace between the beginning, middle, and end of the speech. The two clips I rated lowest (P-02 and P-04) both have rate variance below 7, meaning the speaker held basically the same pace throughout. This matches what Pejčić et al. (2015) found about "regular and significant speech rate modulation within higher syntactic units" being a feature of persuasive speeches.

I need to be very careful here. **n = 5 is not a result.** Five clips is enough to suggest that the feature is worth looking at more carefully. It is not enough to conclude anything. I also rated the clips myself before running the pipeline, but I already had the feature definitions in my head, which means my ratings may have been subtly influenced by what I knew the features would measure. A cleaner experiment would have had a second rater who did not know what the features were.

**Class Reflection On Pipelines:** Dr. Plate talked about multi-model pipelines and error propagation. Errors in the first stage of a pipeline become inputs to the next stage, and bad inputs make the next stage fail in ways you can't always see. For my project the relevant cascading error is: if Whisper mistranscribes a word, that does not break my prosodic features (the timestamps are still valid), but if I later send the transcript to an LLM for content scoring, the LLM is going to score a garbled version of what was actually said. I need to remember this for Space 3.

**What I Want To Do For Space 3:** I want to build the full two-factor pipeline. Audio in, Whisper transcription (via API), prosodic features computed in Python, *same* transcript sent to a small instruction-tuned LLM (SmolLM2 or similar) via the same HF Inference API with a rubric prompt for content scoring, and then a Gradio interface that shows both scores side by side. I also want to think about who this tool is actually for, because I think the answer is me and my teammates, and "what would my teammates want from this" should shape the interface.

---

## Week 9 — Space 3 Design, and Asking Two Teammates What They Want

**The Audience:** This week's class was about UX and designing for a specific audience. The audience for my tool is me and my WSDC teammates. I decided to actually ask two of them what kind of feedback they would want from a tool like this, rather than guess.

I showed them a mockup of Space 2 running on a clip of my own practice speech and asked: "Imagine this tool also scored the content of your speech. What would you want to see?"

- **Teammate A** said: "I don't care about the number. I care about *which ten seconds* I should listen to again. Just tell me where the moments are."
- **Teammate B** said: "I want to know what I did wrong. The number is fine, but I want a sentence that says why."

Both responses were much more concrete than I expected. Teammate A's request gave me a feature idea I had not thought of: use the pause-variance peaks to automatically generate timestamp pointers to "moments that mattered" in the speech. Teammate B's request is the use case for the LLM content scoring stage — the LLM can generate the one-sentence explanation.

**The Three-Tab Design:** Based on what my teammates said, I designed Space 3 as a three-tab Gradio interface:

1. **Score tab.** Upload audio. After processing, shows two numbers side by side: a *Delivery Score* (derived from the four prosodic features, normalized to a 0–100 scale) and a *Content Score* (from SmolLM2's rubric evaluation of the transcript). Also shows a combined score that is the simple average of the two.
2. **Breakdown tab.** Shows the four prosodic feature values individually with their one-sentence explanations, and shows the LLM's rubric evaluation in full (the LLM is prompted to return a score out of 5 on each of three rubric dimensions: *claim clarity*, *evidence quality*, and *rebuttal strength*, plus a one-sentence comment on each). This is the detail view.
3. **Coach tab.** This is the tab that addresses Teammate A's request. It identifies the three longest pauses in the clip and shows their timestamps with a "listen back to 0:45–0:52" style pointer. It also shows the LLM's one-paragraph "what to work on" comment, which addresses Teammate B's request.

**The Rubric Prompt:** The prompt for SmolLM2 is about 300 words long and I iterated on it this week. The final version gives the model a role ("You are a debate coach familiar with the World Schools format"), a task ("Score the following speech transcript on three dimensions"), the three dimensions with brief definitions, an instruction to return the scores in a specific JSON format so I can parse them, and an instruction to write one sentence of constructive feedback. SmolLM2-1.7B is small enough that I cannot expect the reasoning to be deep — it is going to miss subtle things and it is going to over-confidently score things it should not — but for a 5-rubric-point scoring task on short transcripts it is good enough to produce something I can compare against my own ratings.

**What I Am Aware Of But Cannot Fix This Week:** SmolLM2 has no idea what the WSDC format actually is. I am giving it a brief description in the prompt but that is not the same as having it trained on debate feedback. This is the same domain-shift problem we have talked about all term — the model I am using was not trained on the domain I care about. A more sophisticated version of this project would fine-tune a model on actual debate ballots, which I cannot do with free tools.

**What I Want To Do In Week 10:** Build Space 3 end-to-end, test it on a larger set of clips (I want at least 20), and do a real correlation analysis between the tool's scores and my own ratings.

---

## Week 10 — End-to-End Testing and the Correlation Analysis

**This Week's Method:** End-to-End System Testing with Quantitative Analysis.

**What I Built:** Space 3 is deployed. All three tabs work. The Whisper call averages about 8 seconds for a 90-second clip, the SmolLM2 call averages about 6 seconds, and the Python feature extraction is basically instant. Total round trip from upload to results is about 15 seconds, which is slow but acceptable.

**The Test Set:** 20 clips, chosen to have variety:

- **10 TED talks**, clipped to 60–120 seconds each from the introduction of well-known talks. Speakers vary in gender, accent, and topic. I chose these because TED talks are professionally delivered and I expected content and delivery to both be generally high.
- **10 WSDC practice speeches** from me and four teammates, 60–120 seconds each, from a mix of tournaments and practice rounds. I chose these to span the range of quality I knew existed within my team, from novice-level to strong.

**The Rating Procedure:** I rated each clip on a 1–5 scale for "how persuasive I found this as a piece of spoken argument" *before* running it through Space 3, while listening without taking notes. I did this in a single sitting on Saturday to keep my rating scale as consistent as I could. I recognize this is not inter-rater reliability — there is only one rater, me — but it is at least a rating procedure that is not contaminated by the tool's output.

**The Results:** I then ran all 20 clips through Space 3 and computed Spearman rank correlations between my ratings and the tool's three scores (delivery, content, combined). Here is what I found:

| Condition | Prosody score vs my rating | Content score vs my rating | Combined score vs my rating |
|-----------|-----------------------------|------------------------------|-------------------------------|
| TED talks (n=10) | ρ = 0.52 | ρ = 0.48 | ρ = 0.61 |
| Student debate (n=10) | ρ = 0.63 | ρ = 0.24 | ρ = 0.58 |
| All clips (n=20) | ρ = 0.57 | ρ = 0.38 | ρ = 0.63 |

**What This Looks Like To Me:** Three things stand out.

First, the prosody score correlates with my ratings about as well on TED talks as on student debates (0.52 vs 0.63), which is somewhat reassuring — it suggests the prosodic features are picking up something that generalizes across speaker populations, not just something about my teammates' voices.

Second, the content score correlates much more weakly on student debates (0.24) than on TED talks (0.48). My best guess about why: TED talk content varies a lot in quality across the ten clips (some are polished and substantive, some are anecdotal), so the LLM has a real signal to grade on. Student debate content, for my teammates in practice rounds, is much more uniform in quality — everyone is running broadly similar arguments because we all prep from the same sources, so the *variance* in content quality is small, and a score that tracks small variance is hard to correlate with anything. This is actually a methodological observation I think is worth putting in the brief: when variance on one factor is small, that factor cannot carry much of the explanatory signal, so the other factor will look more important by comparison.

Third, on student debates specifically, the combined score (0.58) is *worse* than the prosody score alone (0.63). This is the opposite of what I expected. I expected combining the two factors to always help. Looking at it carefully, I think what is happening is that the content score on student debate is noisy enough that adding it to the prosody score is introducing noise rather than signal. On the TED set, where the content score actually carries information, the combined score does beat either factor alone (0.61 vs 0.52 and 0.48). So the combined-score advantage depends on whether the content score has enough signal to contribute.

**Limitations (I Am Going To Put All Of These In The Brief):**

- **n = 20**, split 10/10. This is a pilot. Nothing here is significant in any statistical sense; I am reporting rank correlations on a tiny sample.
- **Single rater.** All ratings are mine. There is no inter-rater reliability check. A proper version of this study would have at least three raters and report Krippendorff's alpha.
- **Rater contamination risk.** I designed the features, so when I rated the clips I already had opinions about what should count as good delivery. My ratings may correlate with the features because I built the features to match my own criteria, not because the features predict something independent.
- **ASR bias on non-native speakers.** Two of my five teammate sources are non-native English speakers. Per Koenecke et al. (2020) and Li et al. (2024), Whisper has documented performance disparities across speaker groups. I did not correct for this and did not stratify my analysis by speaker origin.
- **Small-model content scoring.** SmolLM2-1.7B is not a debate expert. The content scores are rough. A better study would use a larger model or, better, fine-tune on actual debate ballots.
- **TED clips were chosen by me from talks I already knew.** That is a selection bias.

**What I Want To Say In Week 11:** I want to pull all of this together into the research brief. I also want to write a final journal entry that traces the thread from Week 1 through here and names what I actually learned.

---

## Week 11 — The Thread, and Drafting the Brief

**Looking Back:** I started this course with a hunch — that the sentiment analysis demo my English teacher showed us last year was missing something important about how debate works. The hunch turned into a question by Week 2 ("text-only scoring misses delivery"), into a literature-aware question by Week 3 (when Dr. Plate showed me Consensus and I found Pejčić et al., Gomes et al., and Kišiček), into a formal hypothesis by Week 4 (the two-factor design), into a compute problem by Week 6 (local wav2vec2 won't fit on free tier), into an architectural insight by Week 7 (thin client over API, adapted from the Mistral Voxtral blog post), and finally into a pilot result by Week 10 (prosody correlates with my ratings at ρ ≈ 0.57 across 20 clips; combined scoring helps when content variance is high).

**The Thread, Named:**

- Weeks 1–4 established that **text alone is the wrong modality** for scoring debate delivery, and that a two-factor (prosody + content) design is the right shape of the question.
- Week 5 gave me the **architectural pattern** through the Mistral Voxtral blog post — models on a server, thin client on the frontend — and also the constraint that I needed a *free* version of that pattern.
- Week 6 confirmed through **direct failure** that the alternative (local audio model on a free Space) does not fit the compute envelope. This failure is not wasted; it is the empirical justification for the pivot.
- Weeks 7–8 implemented the free version of the Mistral pattern: Whisper-small via HF Inference API for transcription-with-timestamps, pure-Python feature extraction, no local model loading.
- Weeks 9–10 added the LLM content scoring stage (SmolLM2-1.7B via the same API) to get the full two-factor pipeline, designed the interface around what two teammates actually asked for, and tested on 20 clips with a correlation analysis.

**Methods I Used and What I Would Call Them:**

1. **Comparative Analysis** (Week 2) — two models, same inputs, observe disagreement.
2. **Adversarial Testing** (Week 3) — trying to break models on purpose with domain-specific inputs to find their blind spots.
3. **Literature Search via Consensus** (Weeks 3, 7) — targeted search for peer-reviewed work to ground methodology.
4. **Hypothesis Formulation** (Week 4) — writing a single-sentence testable version of the research question.
5. **Controlled Failure Testing** (Week 6) — deliberately trying the alternative architecture to justify the chosen one.
6. **Pipeline Design with Free Components** (Weeks 7–9) — adapting a paid architectural pattern from industry writing to free tools.
7. **End-to-End Testing with Correlation Analysis** (Week 10) — quantitative validation on a small, stratified test set.
8. **Honest Limitations Accounting** (throughout, but especially Week 10) — naming what the study cannot claim.

**What My Collection Shows:** 14 models and 9 Spaces. The early items are sentiment and emotion classifiers I tested in Weeks 1–3. The middle items are the Whisper variants I considered for transcription and the small instruction-tuned models I considered for content scoring. The later items are my own three Spaces and four comparable Spaces I found that other people built for speech analysis, each with a tasting note explaining what I learned from looking at them.

**What My Three Spaces Represent:**

- **Space 1** is the baseline I built to have something to point at when I claim text generation alone can't do scoring. It's intentionally bad at its job.
- **Space 2** is the minimal working version of the architectural pattern: free thin client over free API, producing real prosodic feature values from real audio clips.
- **Space 3** is the full two-factor pipeline with an interface designed for an actual audience (me and my teammates) and a test set that produced real, honest, modest results.

**The Brief:** I started drafting the research brief this week. It is four pages in a research-paper structure (abstract, introduction, related work, methods, results, limitations, conclusion, references). I am citing six papers plus the Mistral Voxtral blog post. The abstract says: *"This pilot study tests whether acoustic-prosodic features automatically extracted via a thin-client pipeline over free inference APIs correlate with listener ratings of persuasiveness on a small set of TED talks and student WSDC debate speeches, and whether combining prosodic features with LLM-based content scoring improves rating prediction over either modality alone."*

**If I Kept Going (and I Might):**

- **Multi-rater study.** Get at least three raters independent of me and report inter-rater reliability on the same 20 clips.
- **Larger test set.** 100 clips with pre-registered hypotheses.
- **Speaker stratification.** Report correlations separately for native and non-native English speakers on my team, explicitly to diagnose whether ASR bias is affecting the results.
- **Diarization.** If I ever get access to Voxtral or a free diarization model, add speaker-turn analysis so the tool can handle full debate rounds instead of just single-speaker clips. The Mistral blog post specifically mentions diarization as a feature of Voxtral Transcribe, and my current pipeline cannot do it.
- **Fine-tuning on debate ballots.** A proper content-scoring model would be fine-tuned on real judge feedback, not a general-purpose small LLM given a rubric prompt.

None of those are things I can do in Level 2. Some of them would be a Level 3 project. That is okay. The purpose of this pilot was to see whether the architectural pattern works with free components and whether the two-factor design is worth pursuing, and on both questions the honest answer is: it works well enough to justify a larger study.

---

*End of journal — 11 entries, Weeks 1–11*

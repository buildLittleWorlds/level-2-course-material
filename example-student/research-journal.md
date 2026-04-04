# Riley's Research Journal

AI + Research Level 2 — Spring 2026

---

## Week 1 — First Impressions

I tested the Mood Meter Space with a bunch of different inputs. Most of them were just things I was thinking about or song lyrics I like. I tried:

- "I can't wait for Saturday" — predicted Positive (97%). Makes sense.
- "The test was harder than I expected" — predicted Negative (89%). I mean, it wasn't great, but I wasn't upset about it? I'd say neutral.
- "The red-tailed hawk circled above the parking lot after school" — predicted Positive (62%). This is interesting to me because it's not really positive or negative. It's just something I saw. I've been birding with my grandmother since last summer and I notice birds a lot now. The model seems to think any sentence about nature is positive.
- "I heard something in the woods but I couldn't see it" — predicted Negative (71%). Again, not negative. It was actually exciting. I was trying to find a bird by its call.
- "My grandmother can identify a bird just from its song" — predicted Positive (85%). Okay, fair.

The model seems to think it knows how I feel, but it really just knows which words usually go with positive or negative reviews. Birds and nature seem to confuse it because those words show up in positive movie reviews but they're not actually emotional — they're just descriptions of what's there.

**Collection so far:** 2 models (distilbert-sst-2, cardiffnlp twitter-roberta), 3 Spaces (Mood Meter, Text Playground, a summarizer I found). I wrote tasting notes for each. The summarizer is interesting — it takes a paragraph and makes it shorter. Not sure how that relates to anything yet but I liked testing it.

---

## Week 2 — Training Data and Representation

**This Week's Method:** Comparative Analysis

**How I Applied It:** I found an emotion classifier (j-hartmann/emotion-english-distilroberta-base) that detects 7 emotions instead of just positive/negative. I tested it side by side with the binary sentiment model from last week using the same bird-related inputs.

**What I Expected:** I thought the emotion model would be better at understanding my bird sentences since it has more categories. "Surprise" or "neutral" seemed like they'd fit better than forcing everything into positive/negative.

**What I Found:** The emotion model was more interesting but still missed the point. "The red-tailed hawk circled above the parking lot" got labeled "neutral" (42%) and "surprise" (23%). "I heard something in the woods but I couldn't see it" got "fear" (51%). That's closer than "negative" but still wrong — I wasn't scared, I was curious and excited. The model doesn't have a "curiosity" category.

The biggest thing I noticed: neither model has any idea what birding is. They're reading the words but they don't understand the activity. "I couldn't see it" sounds scary in a movie review. In birding, it just means the bird was hidden in the canopy.

**Why I Think This Happened:** Both models were trained on movie reviews or tweets. Nobody writes movie reviews about identifying birds. The training data doesn't include the kind of language birders use.

**Limitations:** I only tested text inputs. Birds make sounds, not sentences. I wonder if there are models that work with audio.

**What I Want to Try Next:** I want to find out if there are AI models that can classify sounds — not just text. If a model can tell the difference between a dog bark and a car horn, maybe one can tell the difference between a cardinal and a robin.

---

## Week 3 — Adversarial Testing and the Limits of Classification

**This Week's Method:** Adversarial Testing

**How I Applied It:** I tried to break the emotion classifier by feeding it sentences that use "bird language" — words that mean one thing in birding and another thing in normal conversation. I was looking for inputs where the model confidently gets it wrong.

**What I Expected:** I thought the model would struggle with domain-specific language. Birding has a lot of words that sound dramatic but aren't: "kill" (a large group of birds), "mob" (when small birds chase a predator), "irruption" (when species show up outside their normal range).

**What I Found:** Three good breaks:

1. "The mob attacked from all sides" — model said "anger" (78%). In birding, this is just chickadees chasing a hawk. It's actually amazing to watch. Not angry at all.
2. "I got a life bird today" — model said "joy" (44%) and "surprise" (31%). It got this right by accident. A "life bird" means you saw a species for the first time, which IS exciting. But the model doesn't know what a life bird is — it just keyed on "got" and "today."
3. "The warbler was skulking in the underbrush" — model said "fear" (39%) and "sadness" (28%). "Skulking" sounds negative but in birding it just describes how certain warblers move through low vegetation. It's normal warbler behavior.

The pattern: the model treats specialized vocabulary as if the words mean what they mean in everyday English. It has no concept of domain-specific meaning.

**Why I Think This Happened:** Same reason as last week — the training data is general-purpose text. Birding vocabulary is a niche domain the model was never exposed to.

**Limitations:** I'm still working with text models, but birds don't communicate in text. I found a Space called "Audio Classification" this week that classifies sounds into categories. It's not bird-specific, but it can tell the difference between natural sounds and urban sounds. That feels like a step in the right direction.

**What I Want to Try Next:** The fork between classification and generation that we're learning about next week is interesting to me. A classifier that sorts audio into categories sounds like exactly what birding needs. I want to see if I can find an audio classifier that knows about bird species.

---

## Week 4 — Classification vs. Generation

**This Week's Big Idea:** Classification puts things in buckets. Generation creates new things. These are fundamentally different tasks and the models that do them need fundamentally different training data.

**The Demo:** In class, we compared a classifier and a generator on the same inputs. The classifier always gives the same answer; the generator gives something different every time.

**How I Explored It:** I tested the distilgpt2 text generator with bird prompts and compared it to the emotion classifier.

- Prompt: "The northern cardinal sings" — Generator continued with "...a beautiful tune to the people of the world. In the first of its kind, the new album from the band..." It just turned my bird sentence into something about a music album. It has no idea what a northern cardinal is.
- Same input to classifier: "joy" (52%). At least it picked up on "sings" being positive-ish.

I also ran the generator 4 times on the same prompt and got completely different outputs each time. One was about music, one was about a church, one was about a sports team (the Cardinals!), and one actually mentioned a bird but then wandered into nonsense.

**The Training Data Connection:** distilgpt2 was trained on web text. It knows "cardinal" as a baseball team, a Catholic title, and a bird — and it picks whichever association the surrounding words nudge it toward. A bird-specific generator would need to be trained on bird text. But a bird-specific *classifier* might be more useful to me — I don't need to generate text about birds, I need to identify them.

**What I Want to Try Next:** I've been thinking about this all week. I want to find a classifier that works on audio and knows bird species. That would be a tool I'd actually use when I'm birding. I searched Hugging Face this week and found `dima806/bird_sounds_classification` — a model that classifies 50 bird species from audio. I haven't tested it yet but I added it to my Collection. Next week we start building Spaces, and I think I know what I want to build eventually.

---

## Week 5 — Add Controls

**What I Built:** My Space 1. It's the text playground with distilgpt2, same as everyone. I changed the title to "Bird Text Generator" and added bird-themed example prompts: "The robin sings at dawn because", "In the forest canopy, the warbler", "Migration patterns suggest that."

**What I Tried:** I swept the temperature from 0.1 to 1.5 on the prompt "The cardinal appeared in the backyard."

- At 0.1: "The cardinal appeared in the backyard. The cardinal appeared in the backyard. The cardinal appeared in the backyard." Just repeated itself. Boring but predictable.
- At 0.5: "The cardinal appeared in the backyard, where it was seen by the family. The family was very excited." Readable but generic.
- At 1.0: "The cardinal appeared in the backyard — flash of vermillion between the maple branches, then gone." Actually nice. Sounds like nature writing.
- At 1.5: "The cardinal appeared in the backyard trumpeting sampled fisheries along doorbell contraption whimsy." Nonsense.

I also tested it on a medical prompt ("The patient presents with") and a legal prompt ("The defendant argued that"). The medical one was surprisingly coherent. The legal one was word salad. Domain matters even for a general model.

**What Surprised Me:** Temperature 1.0 produced the most bird-like writing. The model accidentally sounded like a field guide at that setting. But it still doesn't know anything about actual birds — it's just stringing together words that sound like nature writing. That's generation, not knowledge.

**What I Want to Try Next:** This Space is fine but it's not useful for birding. It generates text about birds but can't identify them. Next week I want to test Space 1 across different domains to feel where it breaks, and then I want to start thinking about Space 2 — which I think should be the audio classifier.

---

## Week 6 — The Domain Wall

**What I Tested:** I tested Space 1 (Bird Text Generator) on three types of input:

1. **Bird-related:** "The wood thrush sings a flute-like song at dusk" — generated a nice paragraph about forest soundscapes. It sounded right but was probably making things up.
2. **Cooking:** "To prepare the chicken, first" — generated a plausible recipe step. Totally different domain, worked fine.
3. **Medical:** "The patient's blood work showed" — generated something that sounded medical but included a made-up condition. Confident and wrong.

**What Broke:** Nothing "broke" exactly — distilgpt2 will generate text about anything. But the quality was inconsistent. The bird text was poetic but not factual. The cooking text was practical. The medical text was dangerous — it sounded authoritative but was fabricated. This is domain shift for a generator: it doesn't fail by refusing, it fails by confidently making things up in domains where accuracy matters.

**Why I Think This Happened:** The model was trained on all kinds of web text, so it can imitate the style of different domains. But imitating style isn't the same as knowing facts. For birding, I don't want a model that writes poetically about birds — I want one that can tell me which bird I'm hearing.

**What I Want to Build Next:** Space 2 is going to be an audio classifier. I've been looking at `dima806/bird_sounds_classification` all week. It classifies 50 bird species from audio recordings. That's a completely different kind of tool than Space 1 — it takes audio in and gives a species label out. Classification, not generation. The domain wall for my project is the wall between "text about birds" and "actual bird identification."

---

## Week 7 — Building Space 2

**What We Talked About in Class:** Bias in AI models. How training data reflects the biases of whoever created it and whatever sources they drew from. Interesting to think about but not directly relevant to what I'm building this week.

**What I'm Building for Space 2:** A bird song identifier. I used the prompt from my student folder as a starting point, but I modified it heavily because I wanted an audio classification Space, not a text generation one. I pasted a prompt into Claude asking it to write a Gradio Space that:

- Takes an audio file upload
- Runs it through an audio classification model
- Shows the top 3 predicted species with confidence scores

I used `dima806/bird_sounds_classification` as the model. It's based on the Audio Spectrogram Transformer architecture and was trained on recordings of 50 bird species.

**How It's Going:** The Space is deployed and working — but I hit a surprise. The model knows 50 species, but they're all Tinamous, Guans, and Chachalacas. These are tropical and neotropical birds. Not a single backyard bird I'd actually see from my window. I uploaded a recording of a Plain Chachalaca from Xeno-Canto and it correctly identified it with 87% confidence. Then I tried a Great Tinamou — also correct (79%). But when I uploaded a Northern Cardinal recording, it guessed "Chestnut-winged Chachalaca" at 31% confidence. It doesn't know what a cardinal sounds like because cardinals aren't in its training data.

This is exactly the domain shift concept from our earlier sessions, except now I'm seeing it with audio instead of text. The model is really good at what it was trained on — but what it was trained on doesn't match what I need.

I also tried a recording of my dog barking and it said "Spotted Nothura" with 19% confidence. So it doesn't handle non-bird audio gracefully either.

The Space is basic — just a file upload, a "Classify" button, and a text output. It's not pretty. But it works for the species it knows, and building it taught me a lot about how audio classification pipelines work. The limitation isn't the architecture — it's the training data.

---

## Week 8 — Improving and Planning

**What I Improved in Space 2:**
- Added a confidence threshold: if the top prediction is below 40%, it now says "Not confident — this may not be a recognizable bird song" instead of guessing
- Added all 50 species to the description so users know what the model can identify
- Tested with 10 different recordings from Xeno-Canto. Results: 7 correct in top-1, 9 correct in top-3 (all tested with species the model actually knows). The model struggles most with similar-sounding Tinamous — it confuses Cinereous Tinamou and Grey Tinamou pretty consistently
- Made the output show a formatted table instead of raw text

**What I Learned from Class:** We talked about multi-model pipelines and error propagation. When you chain two models together, errors from the first model feed into the second. This is relevant to what I'm planning for Space 3.

**My Plan for Space 3:** I want to build a birding assistant that does more than just identify a species. My plan:

1. Audio input → bird species classification (same model from Space 2)
2. Species name → look up information about that bird (habitat, range, behavior)
3. Let the user add a date and location to log the sighting
4. Display everything together: species ID, confidence, bird info, sighting log

The pipeline part is steps 1-2: audio classification feeds into information retrieval. If the classifier gets the species wrong, the info will be about the wrong bird — that's the error propagation we talked about in class. I want to handle this by showing the top 3 predictions so users can pick the right one if the model's top guess is wrong.

---

## Week 9 — Space 3 and the Home Stretch

**What I Built:** The Backyard Birder — a multi-feature birding assistant. It has three tabs:

1. **Identify:** Upload a bird recording, get top-3 species predictions with confidence bars. Uses the same audio classification model from Space 2.
2. **Learn:** Select a species from a dropdown, see a description of the bird (habitat, song description, range, fun fact). I wrote these descriptions myself for 15 of the 50 species in the model — mostly Tinamous and Chachalacas, since those are what the model knows. I used the Cornell Lab's Birds of the World site to get accurate information.
3. **Log:** Enter a species, date, time, and location. The Space keeps a running log of sightings during the session. (It doesn't save between sessions because of Hugging Face's free tier limitations, but you could copy the log.)

**What Was Hard:** Getting the tabs to work in Gradio took a while. The layout kept breaking when I tried to put the confidence bars next to the species names. I also spent a lot of time writing the bird descriptions — I wanted them to be accurate, so I cross-referenced with my Sibley field guide and the Cornell Lab website.

The pipeline connection between Identify and Learn was tricky. When you identify a bird, I wanted the Learn tab to automatically update to show that species. I got it working with Gradio's event system but it's a little slow.

**What I Learned from Class:** We talked about user-centered design — thinking about who would use your tool and what they need. I thought about my grandmother: she's the one who got me into birding, and she'd want a simple interface with big text and clear results, not a technical readout. I made the confidence display use color-coded bars (green for high confidence, yellow for medium, red for low) instead of just numbers. Even though the model only knows tropical species she'd never see in her yard, she thought the interface was well-designed and said "if this knew our birds, I'd use it every day."

**The Story So Far:** I started this course testing sentiment models on bird sentences, which was kind of a dead end — those models don't know anything about birds. Then I found audio classification models and realized that's what birding actually needs. Space 1 was a text generator that wrote about birds. Space 2 was an audio classifier that identifies birds from their songs. Space 3 combines identification with information and logging. Each Space got closer to being a real tool — even though the current model doesn't cover the species in my backyard, the architecture would work perfectly with a better-matched model like BirdNET.

---

## Week 10 — End-to-End System Design (My Own Build)

**This Week's Method:** End-to-End System Testing

**How I Applied It:** I tested the Backyard Birder with 5 types of input, trying to break it the way we learned in adversarial testing back in Week 3.

**What I Expected:** I thought it would handle common bird songs well but struggle with edge cases — background noise, multiple birds at once, non-bird sounds.

**What I Found:**

1. **Clean Great Tinamou recording:** Correct ID, 91% confidence. Works great.
2. **Plain Chachalaca with wind noise:** Correct ID but only 47% confidence. The wind confused it. Still above my threshold.
3. **Two birds at once (Chachalaca + Tinamou):** It picked Chachalaca (63%) and missed the Tinamou entirely. Makes sense — the model classifies the whole audio clip, not individual voices within it.
4. **One-second clip (very short):** "Not confident" message. The model needs a few seconds of audio to work with.
5. **Full 30-second recording with background noise:** Identified correctly (Crested Guan, 72%) but took a long time to process. On the free CPU tier, longer audio clips are slow.

I also showed it to my grandmother. She played a Plain Chachalaca recording from Xeno-Canto and the model got it right. She said "the interface is easy to understand — if this knew our birds, I'd use it every day." That comment stuck with me. The tool works, but the training data doesn't match what a backyard birder in North America actually needs. That's a problem I can't solve just by improving the interface.

**Why I Think This Happened:** The model was trained on clean, isolated recordings from a dataset, not on field recordings with noise. This is exactly the domain shift concept from Week 6 — the model's training world is quiet; the real world is noisy.

**Limitations:** Single-species identification only. Can't handle multiple birds. Sensitive to background noise. Only knows 50 species. Sighting log doesn't persist between sessions.

**What I Want to Try Next:** I want to add a note in the interface that tells users to try to record when the bird is singing clearly, without too much background noise. Managing user expectations is part of good design.

---

## Week 11 — The Thread

**Looking Back:** I started this course trying to make a sentiment model understand bird sentences. That was the wrong question. Sentiment models classify emotions in text — they don't know anything about birds, and they never will, because that's not what they were trained for. The real question was: what kind of AI task does birding actually need?

The answer turned out to be audio classification. Birding is fundamentally about identifying species from what you hear and see. That's a classification problem — but over audio, not text. Once I made that connection in Week 4, the rest of the course became about building toward a tool that actually works.

**The Thread:** Weeks 1-3 were about learning what AI models can and can't do, using birding as a test case. Weeks 4-6 were about finding the right kind of model for my domain. Weeks 7-10 were about building, testing, and improving. Each week built on the last.

**Methods I Used:**
- Comparative analysis (Week 2): comparing emotion vs. sentiment models on bird text
- Adversarial testing (Week 3): finding birding vocabulary that breaks text models
- Parameter sweeps (Week 5): temperature experiments on my text generator
- Domain shift testing (Week 6): pushing my Space across unfamiliar domains
- Pipeline design (Weeks 8-9): chaining audio classification with information lookup
- End-to-end testing (Week 10): systematic testing of the finished tool
- User-centered design (Weeks 9-10): designing for my grandmother

**What My Collection Shows:** 14 models and 8 Spaces. The early items are text classifiers and sentiment models — I was still figuring out the landscape. The middle items are audio models and bird-specific tools — that's when I found my direction. The later items are things that inspired specific features in my Spaces.

**What My Space Represents:** The Backyard Birder isn't perfect. It only knows 50 tropical species — not the cardinals and chickadees in my grandmother's yard. It struggles with noisy recordings, and the sighting log doesn't save. But the architecture works. The pipeline works. And I learned that the gap between "this tool works" and "this tool works *for me*" often comes down to training data, not code.

**If I Kept Going:** The biggest thing: I'd switch to a model trained on North American birds. BirdNET from the Cornell Lab covers thousands of species including all the common backyard birds. That one change would make the tool actually useful for the birding I do. Beyond that, I'd add image classification so you could photograph a bird and identify it visually. I'd make the sighting log save to a file so you could build a life list over time. And I'd want to test it in the field, outside, with real birds — not just with recordings from a website.

---

*End of journal — 11 entries, Weeks 1-11*

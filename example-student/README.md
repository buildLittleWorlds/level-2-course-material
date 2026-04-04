# Riley — AI + Research Level 2 Portfolio

I'm a high school student interested in birding and machine learning. Over 12 weeks in AI + Research Level 2, I explored whether AI tools could help identify birds from their songs — and built a working tool that does exactly that.

## The Question

Can AI identify bird species from audio recordings, and can a high school student build a usable tool around that capability using free, open-source models? (Spoiler: yes — but the available models might not know the birds in your backyard.)

## The Journey

I started this course knowing nothing about AI except that it could classify text as "positive" or "negative." I spent the first few weeks testing sentiment and emotion models on bird-related sentences — which turned out to be the wrong approach entirely. Text models don't know anything about birds. But that failure was useful: it taught me the difference between classification and generation, and helped me understand that the right tool for birding isn't a text model — it's an audio classifier.

In Week 4, I discovered that audio classification models exist on Hugging Face. By Week 7, I had a working bird song identifier — though I quickly learned the best available model only knows 50 tropical species (Tinamous, Guans, and Chachalacas), not the cardinals and chickadees in my backyard. By Week 10, I had a multi-feature birding assistant that demonstrates how audio classification pipelines work, even if the training data doesn't match my local birds yet.

## Three Spaces

| Space | What It Does | What I Learned |
|-------|-------------|----------------|
| [**Bird Text Generator**](https://huggingface.co/spaces/profplate/bird-text-generator) | Generates text continuations from bird-themed prompts using distilgpt2 | Text generation models can imitate nature writing but don't actually know anything about birds. Temperature control matters. |
| [**Bird Song Classifier**](https://huggingface.co/spaces/profplate/bird-song-classifier) | Identifies bird species from audio recordings using a wav2vec2 classifier trained on 50 species | Domain-specific models exist and they're powerful — but training data determines what they know. The best free bird audio model covers tropical species, not backyard birds. |
| [**The Backyard Birder**](https://huggingface.co/spaces/profplate/backyard-birder) | Multi-tab birding assistant: identify species from audio, learn about the bird, log your sightings | Chaining models creates useful tools but also propagates errors. The gap between "working tool" and "useful tool" is often about training data, not architecture. |

## Research Journal

My [research journal](research-journal.md) tracks 11 weeks of exploration, from testing sentiment models on bird sentences (Week 1) to systematic end-to-end testing of a finished birding tool (Week 10). Key entries:

- **Week 3:** Discovered that birding vocabulary ("mob," "kill," "skulking") consistently breaks emotion classifiers. Domain-specific language is invisible to general-purpose models.
- **Week 6:** Hit the domain wall. My text generator writes beautifully about birds but fabricates everything. I needed classification, not generation.
- **Week 7:** Built the bird song classifier and discovered the model only knows tropical species — not the birds in my backyard. Training data mismatch became the central tension of my project.
- **Week 9:** Built The Backyard Birder with three tabs. Designed the interface for my grandmother — big text, color-coded confidence bars, plain-language species descriptions.
- **Week 11:** Connected the whole thread. The "wrong" approach in Weeks 1-3 taught me what birding actually needs from AI.

## Hugging Face Collection

14 models and 8 Spaces, curated over 11 weeks. Early items are text classifiers I was experimenting with. Later items are audio models, bird-specific tools, and things that inspired features in my Spaces. Each item has a tasting note explaining what I tested and what I found.

## ML Concepts I Used

- **Classification vs. Generation:** Learned that birding needs classification (labeling audio) not generation (writing text). This insight shaped my entire project.
- **Domain Shift:** A model trained on movie reviews can't understand birding vocabulary. A model trained on tropical bird recordings can't identify North American backyard birds. A model trained on clean recordings struggles with noisy field audio. Same concept, different modalities.
- **Adversarial Testing:** Used birding jargon to systematically break text models. "Mob," "kill," and "skulking" all triggered false predictions.
- **Parameter Sweeps:** Tested temperature on distilgpt2. Found that 1.0 produces the best nature writing. Too low = repetition. Too high = nonsense.
- **Multi-Model Pipelines:** Chained audio classification with text generation for the Learn tab in Space 3. Errors in species ID propagate to wrong information — that's error cascading.
- **User-Centered Design:** Designed The Backyard Birder for a specific user (my grandmother). Changed the interface based on what she would need: clear confidence indicators, plain language, simple layout.

## What I'd Do Next

- Switch to a model trained on North American species (BirdNET from Cornell Lab covers thousands, including all common backyard birds)
- Add image classification for visual bird ID from photographs
- Make the sighting log persist between sessions
- Test in the field with real birds, not just website recordings
- Explore whether the model performs differently on birds from different regions

---

*Built during AI + Research Level 2, Spring 2026*

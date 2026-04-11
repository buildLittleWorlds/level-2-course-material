# External Validity / Generalization

Session 6 Research Method

## What It Is

External validity asks whether your results hold up outside the specific conditions you tested in. A model might ace every test you give it — but if those tests all come from the same kind of data it was trained on, you haven't learned much. Generalization means taking a tool that works in one context and seeing whether it works in another. The failures are the most informative part.

For your research project, external validity is one of the most important questions you'll address: does the thing you found apply beyond the specific examples you tested? If your tool works on five inputs, will it work on fifty? If it works on text you wrote, will it work on text someone else wrote? These questions are what your limitations section will need to answer honestly.

## When Researchers Use It

- A psychologist runs a study on college freshmen and finds that people make riskier decisions when they're hungry. But do the results generalize? Would the same thing happen with 60-year-olds, or with people in a different country, or outside a lab? If the finding only works with college freshmen in a university setting, it has low external validity.
- A novelist writes dialogue that sounds natural in a contemporary New York setting. She shares the manuscript with a friend in rural Mississippi, who says, "Nobody here talks like that." The dialogue was valid for one world but doesn't generalize to another.
- An engineer designs a bridge that handles traffic loads perfectly in computer simulations. Then winter hits — ice, wind, temperature swings. The simulation didn't include those conditions. The design had internal validity (it worked in the test) but low external validity (it failed in the real world).

## How It Connects to Your Research Question

Your research question lives in a domain — music, medicine, politics, images, animation, game dev. The AI models you're testing were trained on different domains. When you test whether a model works for your topic, you're testing external validity: does a model trained on web text generalize to opera lyrics, or medical notes, or political arguments?

But external validity also applies to your own findings. If you test your Space on 5 inputs and it works well, that doesn't mean it works well in general. It means it works well on those 5 inputs. Your research brief should name the limits of your testing — what you tested, what you didn't, and why that matters.

Prea does this explicitly in her research brief (Section 5, Limitations): "n = 20, split 10/10. This is a pilot. Nothing here is significant in any statistical sense." That kind of honesty about external validity is what makes a student project read like research.

## How to Apply It

1. **Identify the training domain.** Read the model card. What kind of data was this model trained on? Movie reviews? Tweets? Product listings? Medical records? That's the model's "home turf."
2. **Pick a different domain.** Choose text (or images, or audio — whatever your model processes) from a completely different context. If the model was trained on tweets, test it on poetry. If it was trained on product reviews, test it on legal documents.
3. **Compare home vs. away.** Run the same model on home-domain data and away-domain data. Where does performance drop? What specific kinds of inputs cause the biggest failures? The gap between home and away performance is the domain shift.
4. **Name the limits of your own testing.** How many examples did you test? How diverse were they? Would someone from a different background get the same results? These questions go in your research brief's limitations section.

## Key Vocabulary

- **External validity** — Whether results hold up outside the original test conditions. A finding with high external validity generalizes broadly; one with low external validity only works in specific circumstances.
- **Generalization** — A model's ability to perform well on data it wasn't trained on. The opposite of memorization.
- **Domain shift** — What happens when the data a model encounters in the real world is different from its training data. The model didn't get dumber — the world changed around it.
- **Overfitting** — When a model gets so good at its training data that it can't handle anything else.

## Apply It to Your Project

The general method: test your model on its home domain (where it was trained), then test it on your domain (your research topic). Document where it succeeds and where it fails. The gap tells you something about the model — and it may sharpen your research question.

**Annabelle** — Your models were trained on general web text. Your domain is music — opera and jazz specifically. Test a text generator on music prompts vs. general prompts. Does it handle music vocabulary, or does it flatten opera and jazz into generic text? That flattening, if you find it, is domain shift — and it could be part of your research question.

**Bobby** — Game writing is a domain most NLP models haven't seen much of. Your test: give a model game-specific prompts (quest dialogue, loading screen tips, achievement descriptions) and compare the quality to its output on news or general text. Where does the model's world end and game writing begin?

**Chengry** — Medical text is the highest-stakes domain shift example. "Patient tested negative for infection" is good news, but a general model reads "negative" as bad. Test the gap between what a general model produces and what a medical specialist model produces on the same input. That gap is the core tension in medical AI — and your research question may live there.

**Emily** — Political text has a specific challenge: it's emotionally loaded but factually dense. Test whether a summarizer or sentiment model handles political content differently from neutral content. Does it strip the political framing? Does it add bias? The way AI handles political text is an external validity question with real-world stakes.

**George** — Medical language is full of words that mean different things in different domains. "Positive" in medicine means something was detected (often bad); "positive" in everyday language means good. Test a model on health text aimed at different audiences — a clinical note vs. a patient brochure vs. a Wikipedia article. Does it handle all three equally?

**Henry** — External validity for your project means: does the model produce genuinely different perspectives, or just surface variation? If you ask for a bird's-eye view and a close-up of the same scene, how different are the outputs really? Testing whether the model generalizes across viewpoint instructions IS your external validity check.

**Sevilla** — You've already found domain shift: BLIP failing on cartoonish images, emotion detectors missing sarcasm. This week, name those findings using the vocabulary from class. Your prior observations are external validity evidence — you just didn't have the term yet.

**Shawn** — Your comparative methodology is already external validity testing. When you test the same model on different art styles, you're asking: does this model generalize across styles, or is it really only good at one? Now apply the same method to your research question.

---

AI + Research Level 2 • Session 6: Research Methods

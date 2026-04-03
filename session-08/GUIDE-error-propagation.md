# Error Propagation / Systems Testing

Session 8 Research Method

## What It Is

Error propagation means tracing how a mistake in one part of a system causes mistakes in every part that comes after it. In a multi-model pipeline, the output of Model 1 becomes the input of Model 2. If Model 1 is wrong, Model 2 has no way to know — it just processes what it was given. Systems testing is the practice of deliberately injecting errors at each stage and measuring how they travel through the chain.

## When Researchers Use It

- A public health official traces a food poisoning outbreak backward through the supply chain: restaurant, distributor, processing plant, farm. The contamination started at one link, but every link after it passed the problem along without knowing. Finding the source requires testing each step independently.
- A newspaper editor checks a story that went wrong. The reporter misquoted a source, the fact-checker didn't catch it, the editor approved it, and it ran on the front page. Four steps, one original error — but the damage compounded at each stage because every person trusted the step before them.
- A music producer notices a final mix sounds muddy. Instead of tweaking the master, she solos each track — drums, bass, vocals, guitar — to find which one has the problem. Adjusting the master would hide the error; tracing it to the source fixes it.

## How to Apply It

1. **Map the chain.** Draw every step in your pipeline: what goes in, what comes out, what model or process sits in between. Label each arrow. If you can't draw it, you don't fully understand it yet.
2. **Break step 1 on purpose.** Give the first model an input you know will cause trouble — an image it can't caption well, text in a language it wasn't trained on, an edge case from your adversarial testing (Session 3). Record what it outputs.
3. **Trace the error forward.** Feed that flawed output into step 2. Does the error get worse, stay the same, or (rarely) accidentally get corrected? Repeat for every step in the chain. The pattern tells you where the system is fragile and where it's resilient.

## Key Vocabulary

- **Error propagation** — How a mistake in one component of a system travels to and affects every component that follows it. Also called error cascading.
- **Pipeline / multi-model system** — A chain where the output of one model becomes the input of the next. Each model does one job, and none of them know about the others.
- **Garbage in, garbage out** — If the input to any step is wrong, the output of that step will be wrong too — no matter how good the model is. This applies at every link in the chain, not just the first one.
- **Debugging a pipeline** — Checking each step independently to find where the error started, rather than only looking at the final output. The last step in the chain is usually the symptom, not the cause.
- **Systems testing** — Deliberately stressing each component of a system to understand how failures interact and compound.

## This Week's Shared Example

In class, we chained two models: BLIP (which generates a text caption from an image) and DistilBERT (which reads the caption and classifies its sentiment). When we uploaded a clear photo of a dog in a park, the caption was accurate and the sentiment made sense. But when we uploaded abstract art, BLIP described something that wasn't there — and the sentiment model analyzed that wrong description with full confidence. The sentiment model did its job perfectly. The problem was that its input was already broken. The error started at step 1 and cascaded to step 2.

## Apply It to Your Own Topic

- Can you connect two models or Spaces from your Collection into a chain? The output of one becomes the input of the other — translation followed by summarization, image generation followed by captioning, text generation followed by classification.
- If you can build a chain: map it out, test it with easy inputs first, then find inputs that break step 1. What happens downstream?
- If your tools don't chain naturally, you can still study error propagation. Take any model's output, copy it, and paste it into a second model as input. That's a manual pipeline — and it shows the same cascading behavior.
- When you find an error in the final output, resist the urge to fix the last step. Trace backward: where did the error actually start? Is it a problem with step 1's output, step 2's interpretation, or both?
- Think about real-world stakes: if this pipeline were used for something important (medical image analysis, automated news reporting, accessibility tools), where would an error cascade cause the most harm?

See `GUIDE-research-journal.md` for how to structure your pipeline experiment as a journal entry.

---

AI + Research Level 2 • Session 8: From Single Models to Systems

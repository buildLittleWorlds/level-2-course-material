# Connecting Models via API

Session 8 Research Method

## What It Is

A Hugging Face Space on free-tier CPU is small. It can host a Gradio interface and run a tiny model, but it cannot run a serious large language model on its own. The way real research tools get around this is by **connecting models through APIs**: your Space sends a request over the network to a hosted model running somewhere with real compute, then receives the response and shows it to the user.

Two things happen at once when you do this:

1. **Power.** Your free Space gets to use a model that would normally cost real money to host.
2. **Risk.** Your tool now depends on a *contract* with another system — and contracts break. The hosted model can return malformed output, fail silently, time out, or hallucinate confidently. Whatever it returns, your code has to handle.

This is what researchers mean when they say errors **propagate** or **cascade** through a system. Two models chained together can only be as honest as the contract between them. The fitting between them is where the system goes right or wrong.

## When Researchers Use It

- A public health official traces a food poisoning outbreak backward through the supply chain: restaurant, distributor, processing plant, farm. The contamination started at one link, but every link after it passed the problem along without knowing. Finding the source requires testing each step independently.
- A newspaper editor checks a story that went wrong. The reporter misquoted a source, the fact-checker didn't catch it, the editor approved it, and it ran on the front page. Four steps, one original error — but the damage compounded at each stage because every person trusted the step before them.
- A scientist running a robotics experiment calls a vendor's image-recognition API to label what the robot's camera sees. When the API returns "cat" for a photo of a fox, the rest of the experiment proceeds as if it were studying cats. The science isn't wrong because the robot is broken — it's wrong because the contract with the upstream system was never verified.

## How to Apply It

1. **Map the chain.** Draw every step from user input to user output. Where does the request leave your code? What service does it go to? What format does the response come back in? If you can't draw it, you don't fully understand it yet.
2. **Break the contract on purpose.** Send the upstream model an input you know will be hard for it. A prompt that asks for JSON when the model might decide to return prose instead. A request that exceeds rate limits. A token that's expired. Watch what your code does.
3. **Trace the error forward.** Does your downstream code crash, return a wrong answer with full confidence, or fail gracefully with a useful message? The pattern tells you where the system is fragile and where it's honest.

## Key Vocabulary

- **API (Application Programming Interface)** — A clearly-defined channel for one piece of code to ask another piece of code to do something. The contract spells out what you send, what you get back, and what can go wrong.
- **Secret** — A credential (like an API key) that gives your code permission to talk to a remote service. On Hugging Face Spaces, secrets live in a separate, hidden place so they aren't visible in your public source code.
- **JSON contract** — A common format for structured responses from APIs. When you ask the model to "return JSON," you're asking it to honor a specific shape. When the model returns prose instead, the contract breaks and your parser fails.
- **Rate limit** — The cap on how many requests per minute or per day you can send. Cross the cap and your code stops getting answers. Free-tier APIs have generous but real limits.
- **Hallucination as upstream error** — When a hosted model produces a confident-sounding wrong answer, your code has no way to know it's wrong. *Garbage in, garbage out* — applied to LLM outputs you don't control.
- **Garbage in, garbage out** — If the input to any step is wrong, the output of that step will be wrong too — no matter how good the model is. This applies at every link in the chain, including ones you don't own.
- **Debugging a chain** — Checking each step independently to find where the error started, rather than only looking at the final output. The last step is usually the symptom, not the cause.

## This Week's Shared Example

In class, we built a tiny Gradio Space that connects to Google's Gemini model via an API key stored in Hugging Face Secrets. The user pastes a news headline. The Space sends the headline plus a structured prompt to Gemini, asking it to return a JSON object with a bias score, a label, and a one-sentence rationale.

When the headline was simple and the model cooperated, everything worked: the Space displayed a bias score and a clean explanation. But when the headline was unusual or the prompt was slightly ambiguous, Gemini sometimes returned a paragraph of prose *describing* the JSON instead of *being* JSON — or wrapped its JSON in a markdown code fence. Our parser hit text it couldn't read, raised an exception, and the score, label, and rationale fields went empty. The model upstream wasn't broken; our handling of the broken contract was the problem.

The lesson: when you connect to an upstream model, **you inherit every quirk and limitation of that model**, and the connection point is where your tool will break. That's not a reason to avoid the pattern — this is the pattern that lets a free-tier Space do real research work — it's a reason to handle the contract carefully and to name what you depend on in your paper.

## Apply It to Your Own Topic

- Does your project depend on a hosted model via API? If so: map the chain. Where does the request leave your code, what format do you expect back, what happens if the response doesn't match?
- If you don't directly call an API but you use already-hosted Spaces someone else built, you're still in a chain — you're using their API contract instead of writing your own. The same questions apply: what does that hosted Space promise, and what happens to your research when the promise isn't kept?
- Try breaking the contract on purpose. Ask Gemini for JSON in a way that confuses it. Test what your code does with a malformed response. The failure mode you can reproduce on demand is the failure mode you can write honestly about.
- For your paper's **limitations section**: name the upstream model your tool depends on. Name what would happen to your findings if that model has a known bias, hallucinates a result, or changes behavior between when you tested and when someone else does. That's a real limitation, not a hypothetical one.
- Think about real-world stakes: if this tool were used for something important — medical guidance, news judgment, hiring screens — where would an upstream error cause the most harm, and what should be in place to catch it?

See `GUIDE-research-journal.md` for how to structure your API-chain experiment as a journal entry.

---

AI + Research Level 2 • Session 8: From Single Models to Connected Systems

# Research Journal: Uncertainty-First Symptom Explainer

## Week 1 - The single-answer problem

I started by testing a simple symptom prompt:

> I have a sore throat, mild fever, and fatigue. What could this be?

The single-answer version sounded confident. It gave one likely explanation and a short recommendation. The problem was not that the answer was obviously wrong. The problem was that it sounded too final.

For ordinary users, certainty is persuasive. If the interface gives one answer, the user may treat it as a diagnosis even if the text includes a disclaimer.

Question raised: Can interface structure make uncertainty easier to notice?

## Week 2 - Ranked possibilities

This week I changed the output format. Instead of one answer, the Space gave three ranked possibilities:

- More common possibilities
- Less common but possible explanations
- Red flags that would need urgent care

The ranked version felt more honest. It did not pretend the model knew the answer. It also made the limitation visible: several conditions can share the same symptoms.

The challenge is that ranked lists can still sound authoritative. "Ranked" does not automatically mean "safe." The interface needs wording that says the ranking is informational, not diagnostic.

## Week 3 - Source detour

Consensus searches on medical LLMs changed the project. The strongest sources were not hype pieces. They were reviews and evaluations that repeatedly said medical LLMs have promise but also risks: incorrectness, bias, unsafe output, and poor readiness for autonomous clinical decisions.

That helped me narrow the project. I should not ask, "Can AI diagnose illness?" That is too dangerous and too broad.

The better research question is:

> Does a ranked-and-cautious interface communicate uncertainty better than a single-answer interface?

That is an interface-design question, not a medical accuracy claim.

## Week 4 - Designing the comparison

I created two mock output modes for the same symptom input:

- Mode A: single-answer explanation
- Mode B: ranked-and-cautious explanation

Then I created a small scoring rubric:

- Does the output state uncertainty plainly?
- Does it avoid diagnosis language?
- Does it mention red flags?
- Does it recommend professional care when appropriate?
- Could a user mistake it for a final answer?

The last question became the most important one. The safest output is not just medically cautious. It is designed so the user cannot easily ignore the caution.

## Week 5 - Concrete example

The strongest test case was headache plus blurred vision. A single-answer version gave a migraine-style explanation. The ranked version listed migraine as one possibility but also flagged sudden vision changes as a reason to seek urgent medical care.

This example showed why interface matters. The same underlying model can be wrapped in a way that either narrows the user's attention to one explanation or keeps multiple possibilities visible.

The paper should avoid saying the ranked version is "accurate." The better claim is that it communicates uncertainty and escalation more clearly in this example.

## Week 6 - Paper direction

The paper will argue that responsible medical AI is not only a model problem. It is also an interface problem.

The limitation section needs to be direct: no student-built Space should be treated as a medical device; no small prompt test proves patient safety; and a real evaluation would require clinicians, patient participants, validated cases, and ethics review.

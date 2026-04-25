# Research Journal: Health Reading-Level Lab

## Week 1 - Shorter is not always clearer

I started by asking a model to explain high blood pressure to a middle school student. The output was shorter than the adult version and used simpler words. At first I thought that meant it worked.

Then I compared the two versions. The simpler version removed "arteries," "long-term risk," and "blood vessel damage." It was easier to read, but it also removed some of the mechanism.

Question raised: When an AI health explainer simplifies text, does it preserve the important idea or just make the words easier?

## Week 2 - Audience levels

This week I created four audience levels:

- Elementary student
- Middle school student
- Adult patient
- Pre-med student

For the topic "asthma attack," the model changed sentence length and vocabulary well. The elementary version used "breathing tubes." The adult version used "airways." The pre-med version used "bronchoconstriction."

The surprising part was that the simpler versions sometimes lost actionability. They explained what asthma is but were less clear about what someone should do during serious symptoms.

## Week 3 - Source detour

Consensus searches on LLMs and patient education showed that readability is a real research topic. Many patient materials are written above recommended reading levels, and LLMs may help simplify them. But the sources also made the evaluation problem clearer: readability is not the same as accuracy.

My question sharpened:

> When a health explainer changes reading level, is it actually adapting the explanation, or mostly swapping vocabulary and sentence length?

I need to track meaning, not just grade level.

## Week 4 - A comparison rubric

I made a rubric with four checks:

- Readability: Are the words and sentences easier?
- Concept preservation: Are the key ideas still there?
- Actionability: Does the user know what to do next?
- Caution: Does the output avoid overconfident medical advice?

The concept-preservation check was the most useful. A simplified explanation of fever kept "body fighting infection" but lost the idea that fever can have many causes. That made it simpler but less careful.

## Week 5 - Concrete example

The best test topic was "high blood pressure." The middle school version said:

> Your heart has to push blood too hard through your body.

That was clear, but it missed the long-term risk. A better version added:

> Over time, this can hurt your heart and blood vessels, even if you feel fine.

That sentence was still readable and preserved the important idea. This showed that simplification can work, but only if the prompt asks the model to preserve key concepts.

## Week 6 - Paper direction

The paper should not say "AI makes medical explanations understandable." It should say something narrower:

> In this small comparison, the model improved readability more easily than it preserved completeness and actionability.

The limitation is that I am not a clinician and the test set is tiny. A real project would need medical review and user testing with actual readers.

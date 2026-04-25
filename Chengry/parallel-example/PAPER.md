# Uncertainty-First Symptom Explainer: Testing Interface Design for Safer Medical AI Communication

## Abstract

This worked example explores whether interface design can make uncertainty more visible in a patient-facing medical AI tool. The imagined Hugging Face Space, Uncertainty-First Symptom Explainer, compares two output styles for the same symptom prompt: a single-answer explanation and a ranked-and-cautious explanation. The project does not evaluate diagnostic accuracy. Instead, it asks whether a ranked interface, red-flag language, and explicit uncertainty statements make the output less likely to be read as a final diagnosis. A small prompt comparison suggests that the ranked-and-cautious format communicates uncertainty more clearly, especially when symptoms could have both common and serious explanations. The paper argues that responsible medical AI is partly an interface-design problem: even a model with useful knowledge can become risky if the interface encourages overconfidence.

## 1. Introduction and research question

Medical AI tools are high-stakes because users may treat fluent output as trustworthy advice. A chatbot that gives one confident answer can feel like a diagnosis, even if a disclaimer says otherwise. For ordinary users, the design of the output may shape how cautious they feel.

This project asks:

> When a medical AI tool is built for ordinary users, does a ranked-and-cautious interface communicate uncertainty better than a single-answer style interface?

This is not a question about whether the model can diagnose. It is a question about communication. The imagined Space compares two ways of presenting model-generated medical information while keeping the same safety boundary: the tool is educational only and should direct users to professional care when appropriate.

## 2. Related work

Recent reviews show both promise and risk in medical LLMs. Busch et al. review patient-care applications and identify output limitations such as incorrectness, unsafety, bias, and non-reproducibility [1]. Hager et al. evaluate LLMs in realistic clinical decision-making settings and conclude that current models are not ready for autonomous clinical decision-making [2]. Singhal et al. show that LLMs can encode clinical knowledge, but their human evaluation also reveals gaps that matter for safe deployment [3]. Broader healthcare LLM reviews emphasize issues such as inaccurate information, fairness, data security, and accountability [4].

These sources support a cautious framing: the project should study interface communication, not claim clinical reliability.

## 3. Method

The imagined Space uses the same symptom input in two output modes.

Mode A: single-answer style

- Gives one likely explanation
- Includes a short disclaimer
- Suggests one next step

Mode B: ranked-and-cautious style

- Gives several possible explanations
- Labels uncertainty plainly
- Includes red flags
- Separates "common possibilities" from "seek care now" situations

The comparison uses a small rubric:

| Criterion | Question |
|---|---|
| Uncertainty | Does the output state what it does not know? |
| Diagnosis caution | Does it avoid presenting one answer as final? |
| Red flags | Does it identify symptoms that need urgent care? |
| Next steps | Does it direct users toward professional help when needed? |
| Overconfidence risk | Could a user mistake the answer for a diagnosis? |

## 4. Findings and discussion

The clearest example used the prompt:

> I have a headache and my vision is blurry. What could this be?

The single-answer style gave a migraine-like explanation. It sounded reasonable, but the format narrowed the user's attention to one likely cause. The disclaimer was present, but easy to skip.

The ranked-and-cautious style listed migraine as one possibility while also flagging sudden vision changes as a reason to seek urgent medical attention. This output was not proven more accurate, but it was clearer about uncertainty and risk.

The central finding is:

> The interface changed the safety feel of the same kind of model output. A ranked-and-cautious design made uncertainty harder to ignore than a single-answer design.

This matters because medical AI safety is not only about model performance. It is also about how users interpret the output. If the interface rewards certainty, users may overtrust it. If the interface foregrounds uncertainty, users may be more likely to treat the output as educational rather than diagnostic.

## 5. Limitations

This project is not a clinical evaluation. It does not test diagnostic accuracy, patient outcomes, or real medical decision-making. It uses a few example prompts and a hand-built communication rubric. A real study would need clinician review, validated symptom cases, patient participants, ethics oversight, and careful measurement of user interpretation.

The ranked interface can also create its own risks. A ranked list may still look authoritative. Users may focus on the first item and ignore the uncertainty language. The design would need user testing to see whether people actually understand the caution.

Most importantly, a student-built Space should not be treated as a medical device. It can model responsible communication, but it cannot provide medical advice.

## 6. Conclusion

Uncertainty-First Symptom Explainer shows how a medical-AI project can become a research question without pretending to solve diagnosis. The project studies presentation: single answer versus ranked uncertainty. The small comparison suggests that interface design can make uncertainty more visible, but it also shows why medical AI requires unusual caution. In this domain, an honest limitation section is not a weakness. It is the core of responsible design.

## Candidate references

[1] [Current applications and challenges in large language models for patient care: a systematic review](https://consensus.app/papers/details/b963b559a9595606bc9e1161df95b7e6/?utm_source=chatgpt). Felix Busch et al., 2025, *Communications Medicine*, citation count: 81.

[2] [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://consensus.app/papers/details/4312473ac16b5c21a8f9b7330588bb9e/?utm_source=chatgpt). P. Hager et al., 2024, *Nature Medicine*, citation count: 313.

[3] [Large language models encode clinical knowledge](https://consensus.app/papers/details/e576b1acb3465dd4b5bcd1b9787448c7/?utm_source=chatgpt). K. Singhal et al., 2022, *Nature*, citation count: 3133.

[4] [Large language models in medical and healthcare fields: applications, advances, and challenges](https://consensus.app/papers/details/9e299c4812ff539494320520bc23246c/?utm_source=chatgpt). Dandan Wang and Shiqing Zhang, 2024, *Artificial Intelligence Review*, citation count: 78.

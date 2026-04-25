# Health Reading-Level Lab: Testing Whether AI Simplification Preserves Meaning in Patient Explanations

## Abstract

This worked example explores how a health explainer changes when asked to rewrite medical information for different reading levels. The imagined Hugging Face Space, Health Reading-Level Lab, rewrites a short health explanation for several audiences and shows what concepts were kept, removed, or simplified. The research question asks whether reading-level adaptation changes the explanation meaningfully or mostly changes vocabulary and sentence length. A small prompt comparison suggests that AI simplification can make text easier to read, but it may also remove mechanism, actionability, or caution. The paper argues that readability is only one part of health communication. A useful AI health explainer must also preserve key concepts and avoid overconfident advice.

## 1. Introduction and research question

Health information is often hard to understand. AI tools can rewrite text quickly, which makes them tempting for patient education. But a simpler explanation is not automatically a better explanation. If simplification removes the important idea, the user may understand the words while missing the meaning.

This project asks:

> When a health explainer changes its reading level, is it actually changing the explanation, or mostly swapping vocabulary and sentence length?

The focus is communication, not medical diagnosis. The project studies whether AI-generated explanations preserve meaning across audience levels.

## 2. Related work

Recent studies examine whether LLMs can improve readability of patient education materials. Will et al. report that LLMs can significantly improve readability while maintaining understandability, though model performance varies [1]. Srinivasan et al. compare LLM-generated bariatric surgery patient education materials with institutional resources and find that simplified LLM responses can improve reading level [2]. Romoff et al. study orthopedic spine patient materials and emphasize readability, accuracy, and the need to preserve medical relevance [3]. Aydin et al. provide a broader scoping review of LLMs in patient education and note both potential and challenges [4]. Daram et al. offer a useful caution: LLM outputs can be concise but still fail to meet recommended reading levels or create an illusion of accessibility [5].

These sources support the paper's central distinction: readability improvement must be evaluated alongside accuracy, completeness, and usefulness.

## 3. Method

The imagined Space takes one medical topic and generates explanations for four audience levels:

- Elementary student
- Middle school student
- Adult patient
- Pre-med student

The pilot tests topics such as high blood pressure, asthma attack, fever, and sprained ankle. Each output is checked with a four-part rubric:

| Criterion | Question |
|---|---|
| Readability | Are words and sentences easier for the chosen audience? |
| Concept preservation | Are the key ideas still present? |
| Actionability | Does the reader know what to do next or what to watch for? |
| Caution | Does the output avoid sounding like final medical advice? |

The project compares whether simplification improves only readability or also preserves explanation quality.

## 4. Findings and discussion

The strongest example used high blood pressure. The adult version explained arteries, pressure, and long-term risk. The middle school version was easier to read, but the first draft removed the long-term risk almost entirely. It said:

> Your heart has to push blood too hard through your body.

That sentence is clear, but incomplete. A stronger simplified version said:

> Your heart has to push blood too hard through your body. Over time, this can hurt your heart and blood vessels, even if you feel fine.

The second version is still readable, but it preserves the reason high blood pressure matters.

The finding is:

> In this small comparison, the model improved readability more easily than it preserved completeness and actionability.

This does not mean AI simplification is bad. It means the prompt and evaluation need to ask for more than "make it simpler." A good health explainer should say: make it understandable, keep the core concepts, include next steps, and do not overstate certainty.

## 5. Limitations

This is not a clinical study. The example uses a small number of topics and a hand-built rubric. The outputs were not reviewed by clinicians or tested with real readers. A real version would need medical expert review, validated readability measures, patient-education assessment tools, and user testing.

The project also focuses on English-language text. Health literacy varies by language, culture, background knowledge, disability, and trust in medical systems. A reading-level score cannot capture all of that.

## 6. Conclusion

Health Reading-Level Lab shows how a simple AI explainer can become a research project. The key move is separating readability from meaning. If a model only shortens sentences, it may make the text easier while making the explanation weaker. The best use of AI in this example is not automatic medical teaching. It is a draft-and-check workflow where simplification is paired with concept preservation, caution, and human review.

## Candidate references

[1] [Enhancing the Readability of Online Patient Education Materials Using Large Language Models: Cross-Sectional Study](https://consensus.app/papers/details/ce1e1b29d03a59cd8c2633c29222f8eb/?utm_source=chatgpt). John Will, Mahin Gupta, J. Zaretsky, Aliesha Dowlath, Paul Testa, and Jonah Feldman, 2024, *Journal of Medical Internet Research*, citation count: 13.

[2] [Large language models and bariatric surgery patient education: a comparative readability analysis of GPT-3.5, GPT-4, Bard, and online institutional resources](https://consensus.app/papers/details/aa7a6d7dafd75ef78c14567c6fae5634/?utm_source=chatgpt). N. Srinivasan et al., 2024, *Surgical Endoscopy*, citation count: 35.

[3] [The role of large language models in improving the readability of orthopaedic spine patient educational material](https://consensus.app/papers/details/f0fe908932c85d238f9acb85cd102298/?utm_source=chatgpt). Melissa Romoff, Madison Brunette, Melanie K. Peterson, Sohaib Hashmi, and Michael S. Kim, 2025, *Journal of Orthopaedic Surgery and Research*, citation count: 4.

[4] [Large language models in patient education: a scoping review of applications in medicine](https://consensus.app/papers/details/6e0269f9db5b5ba5a242bcf5516ef4f2/?utm_source=chatgpt). Serhat Aydin, Mert Karabacak, Victoria Vlachos, and Konstantinos Margetis, 2024, *Frontiers in Medicine*, citation count: 70.

[5] [Can AI Improve the Readability of Patient Education Information in Gynecology?](https://consensus.app/papers/details/e85bd38be52e5658aec06e12a061845a/?utm_source=chatgpt). N. Daram, Rose A. Maxwell, Josette D'Amato, and Jason C. Massengill, 2025, *American Journal of Obstetrics and Gynecology*, citation count: 1.

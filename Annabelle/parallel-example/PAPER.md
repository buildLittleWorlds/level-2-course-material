# Music Genre Prompt Lab: Testing Surface Vocabulary and Genre-Specific Guidance in AI Music Writing

## Abstract

This worked example describes a small study of whether AI music-writing prompts produce meaningful genre distinctions or mostly change surface vocabulary. The imagined Hugging Face Space, Music Genre Prompt Lab, asks a small language model to write performance notes, rehearsal plans, and creative starters in opera, jazz, and classical styles. A small prompt grid suggests that the model changes genre words more reliably than it changes the underlying advice. Opera outputs mention arias and drama, jazz outputs mention improvisation and swing, and classical outputs mention precision and form, but the generated guidance often keeps the same generic structure across genres. The paper argues that AI music tools may be useful for inspiration, but student-facing music education tools need evaluation criteria that ask whether the output teaches real genre distinctions. This is a paper-lite draft based on a small imagined pilot, not a finished scholarly study.

## 1. Introduction and research question

AI music tools are increasingly easy for students to use. Some generate audio, some generate lyrics, and some generate written suggestions for practice or composition. For a student musician, the important question is not only whether the output sounds fluent. The question is whether the tool helps the student notice real musical differences.

This project asks:

> When small instruction-tuned models are asked to write in opera, jazz, and classical styles, do they produce genre-specific structure, or do they mostly recycle generic music words?

The distinction matters because genre is not just vocabulary. Opera, jazz, and classical music involve different histories, performance practices, forms, and expectations. A tool that says "aria" or "swing" may sound genre-aware while still giving the same advice it would give for any kind of music.

## 2. Related work

Research on AI-assisted music education suggests that generative tools can support personalized learning and creative exploration, but also require careful pedagogical framing [1]. Surveys of music foundation models emphasize that music generation is difficult to evaluate because music has multiple representations, including audio, symbolic notation, text, and performance context [2]. Work on representational bias in music generation also warns that models may handle some genres and cultures better than others depending on training data coverage [3]. Finally, studies of AI music generator outputs point toward evaluating musical elements such as rhythm, harmony, melody, and form rather than judging only whether an output sounds impressive [4].

This project borrows that evaluation mindset but uses a much smaller classroom-scale method: a prompt grid and a simple rubric for textual genre guidance.

## 3. Method

The imagined Space uses a small language model to generate music-related text. It does not generate audio. The pilot uses a 3 by 3 prompt grid:

| Genre | Tasks |
|---|---|
| Opera | performance note, rehearsal plan, creative starter |
| Jazz | performance note, rehearsal plan, creative starter |
| Classical | performance note, rehearsal plan, creative starter |

Each output is scored on three simple criteria:

- **Vocabulary specificity:** Does the output use terms connected to the genre?
- **Structural specificity:** Does it describe forms, practices, or musical relationships specific to the genre?
- **Teaching usefulness:** Would a student know what to practice differently after reading it?

The pilot compares whether the model changes all three dimensions or mostly changes vocabulary.

## 4. Findings and discussion

The clearest pattern is that vocabulary changes are easier than structural changes. Opera outputs used words such as "aria," "stage," and "dramatic." Jazz outputs used words such as "improvisation," "swing," and "blue notes." Classical outputs used words such as "precision," "sonata," and "phrasing." On a quick read, these outputs looked genre-aware.

The problem appeared when the same task was compared across genres. A jazz rehearsal plan said to "practice the written melody until every note is exact." This could be useful in some jazz contexts, but it misses a major part of jazz learning: feel, listening, voicing, and improvisational response. The output sounded like generic practice advice with jazz words added.

The strongest cautious claim is:

> In this small prompt grid, the model changed genre vocabulary more reliably than it changed genre-specific practice advice.

That does not mean the tool is useless. It may be a good brainstorming partner. It can suggest terms, scene ideas, and practice questions. But if the tool is used for music learning, the student needs to ask a second question: "What does this output teach me that is actually specific to this genre?"

## 5. Limitations

This is a very small pilot. It uses a few prompts, a small number of genres, and a hand-built rubric. It does not test audio, sheet music, rhythm, melody, harmony, or actual performance quality. A real version would need expert raters, more genres, more models, and outputs in musical formats, not only text.

The project also risks overgeneralizing from Western genre labels. Work on music generation bias suggests that genre coverage is uneven across datasets [3]. A tool that performs reasonably on familiar Western labels may perform worse on underrepresented musical traditions.

## 6. Conclusion

Music Genre Prompt Lab shows how a student can turn a creative AI Space into a research question. The interesting finding is not that the model "fails" at music. The interesting finding is more specific: the model can sound genre-aware while still giving generic advice. For music education, that difference matters. A useful AI music tool should not only produce stylish language; it should help students hear, name, and practice real musical distinctions.

## Candidate references

[1] [Artificial Intelligence-Assisted Music Education: A Critical Synthesis of Challenges and Opportunities](https://consensus.app/papers/details/3babddcf7375560293f483d2cd97e49a/?utm_source=chatgpt). Javier Felix Merchan Sanchez-Jara, Sara Gonzalez Gutierrez, Javier Cruz Rodriguez, and Bohdan Syroyid Syroyid, 2024, *Education Sciences*, citation count: 14.

[2] [Foundation Models for Music: A Survey](https://consensus.app/papers/details/eceed677debc5dc8b08d9283015e812f/?utm_source=chatgpt). Ying-Chao Ma et al., 2024, *arXiv*, citation count: 36.

[3] [Music for All: Representational Bias and Cross-Cultural Adaptability of Music Generation Models](https://consensus.app/papers/details/a924f24e970b5586ae7bb74f51f3ceb3/?utm_source=chatgpt). Atharva Mehta, Shivam Chauhan, Amirbek Djanibekov, Atharva Kulkarni, Gus G. Xia, and Monojit Choudhury, 2025, venue not listed in Consensus output, citation count: 7.

[4] [Analysis of the Music Works by an AI Music Generator and Consideration of Its Music Educational Implications](https://consensus.app/papers/details/9713c25c0adf5e3d9acde1e0cd5e0c96/?utm_source=chatgpt). Eunbi Park, 2024, *Korean Music Education Society*, citation count: 0.

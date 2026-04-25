# Research Journal: Music Genre Prompt Lab

## Week 1 - The first genre test

I started with a simple question: if I ask a small model for opera, jazz, or classical writing, does it know what those words mean musically? My first test used the same task across all three genres:

> Write a short performance description for a student musician preparing for a competition.

The opera output used words like "dramatic," "aria," and "stage." The jazz output used "improvisation," "swing," and "blue notes." The classical output used "precision," "sonata," and "phrasing." At first this looked successful because the vocabulary changed.

But when I read more carefully, the sentence structure barely changed. Every output had the same pattern: a performer prepares, expresses emotion, and impresses the audience. The model changed the costume of the writing, not the skeleton.

Question raised: Is genre control in this kind of tool mostly vocabulary control?

## Week 2 - A stricter prompt

This week I made the prompt more demanding:

> Write four lines of guidance for a student. Include one genre-specific structural feature, not just vocabulary.

This helped a little. The opera output mentioned recitative and aria, but it did not explain how they function differently. The jazz output mentioned improvisation, but it treated improvisation like "add creativity," which is too vague. The classical output mentioned form, but it did not name a specific form until I asked directly.

I started a scoring table with three columns:

- Vocabulary specificity: Does it use terms connected to the genre?
- Structural specificity: Does it describe how the genre is organized?
- Teaching usefulness: Would a student know what to practice differently?

The surprising part was that vocabulary specificity was easy to get. Teaching usefulness was much harder.

## Week 3 - Source detour

I searched Consensus for work on AI music education and music generation. The useful shift was realizing that my project should not claim to evaluate actual music quality from text alone. It is narrower than that.

The better research question is about **textual genre guidance**. If a Space writes practice suggestions or creative starters, does it teach meaningful genre distinctions or only produce genre-flavored language?

One source direction that mattered was AI music education. Those papers do not prove my Space works, but they show why the question matters: if students use AI as a music-learning assistant, the tool's explanations need to be musically specific.

## Week 4 - Mini prompt grid

I made a small prompt grid:

- Genres: opera, jazz, classical
- Tasks: performance note, rehearsal plan, creative starter
- Models: one base generator and one instruction-tuned model

The instruction-tuned model followed the task better. It gave cleaner bullets and sounded more helpful. But it still tended to explain genres through surface markers. Opera was "dramatic," jazz was "improvised," classical was "precise."

One concrete output bothered me: the jazz rehearsal plan said, "Practice the written melody until every note is exact." That is not wrong in all contexts, but it misses the point of style. Jazz practice often includes listening, feel, voicing, and improvisational response. The model sounded like a generic classical practice coach wearing jazz vocabulary.

## Week 5 - What counts as evidence

I decided the paper should not say, "The model does not understand music." That is too broad and impossible to prove from my tests.

A better claim is:

> In this small prompt grid, the model changed genre vocabulary more reliably than it changed genre-specific practice advice.

That claim is modest, but it is testable. I can point to the output table and show examples where words changed while the advice pattern stayed the same.

The limitation is also clear: text outputs are not music. A real study of genre generation would need audio or symbolic music output, expert raters, and a better scoring rubric.

## Week 6 - Paper direction

The paper should be about using music knowledge to evaluate AI output. The strongest section will be the method: same prompts, different genres, simple rubric.

The most honest ending is that the Space is still useful as an inspiration tool. It can produce starting language, rehearsal questions, and genre vocabulary. But if the goal is music learning, a student still needs human musical judgment to tell whether the genre guidance is real.

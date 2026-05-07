# Integration Checklist

How to make your Space, paper, journal, and profile tell one research story

## Where You Are Right Now

You have spent the course building toward a public research portfolio.

- Session 6 sharpened your research question.
- Session 7 gave you a rough `PAPER.md`.
- Session 8 made the work public through GitHub and Hugging Face.
- Session 9 made the Space and the paper fit a real human audience and verified the citations.

Session 10 asks a different question:

> If someone opens your profile right now, can they understand what you are investigating and find the evidence?

Use this checklist during class. Mark each section Green, Yellow, or Red.

- **Green:** present, public, specific, and aligned
- **Yellow:** present but generic, stale, broken, or disconnected
- **Red:** missing or unusable

## 1. Research Question

Your research question should appear in your profile, paper, and journal in roughly the same form.

**Check:**

- [ ] I can state my research question in one sentence.
- [ ] It appears near the top of my GitHub profile README.
- [ ] It appears in the introduction or first section of `PAPER.md`.
- [ ] My Space actually tests or demonstrates part of the question.

**One-sentence version:**

```markdown
I am investigating whether/how <model or AI system> handles <specific task/domain/problem> for <specific user or context>.
```

## 2. Space Status

Your Space does not need to be perfect. It needs to be honest and testable.

**Check:**

- [ ] Space URL opens.
- [ ] Title describes the tool in plain language.
- [ ] Description names who it is for.
- [ ] Examples are inputs a real user would try.
- [ ] Output is readable by the audience, not just raw model labels.
- [ ] I know one input where it works well.
- [ ] I know one input where it struggles.

**If broken:**

```markdown
Space error:

First debugging step:

What I can still say honestly in PAPER.md:
```

## 3. Paper Evidence

Your `PAPER.md` should include evidence from your own build, not only claims about AI in general.

**Check:**

- [ ] `PAPER.md` names the Space or tool I built.
- [ ] It includes at least one real input/output result.
- [ ] It explains what that result shows.
- [ ] It includes at least one verified source from `week-09-citations.md`.
- [ ] The source supports the claim I attach it to.
- [ ] The limitations section names what my test cannot prove.

**Claim-Evidence-Source Chain:**

```markdown
Claim:

Space evidence:

Verified source:

Limitation:
```

## 4. Research Journal

The journal is the trail of thinking that makes the paper believable.

**Check:**

- [ ] Week 10 entry exists or is started.
- [ ] It names the exact inputs I tested.
- [ ] It records one result that surprised me.
- [ ] It says what I changed in `PAPER.md`.
- [ ] It names what I want peer testers to try next.

## 5. GitHub Profile README

The profile is the front door. It should not oversell; it should connect.

**Check:**

- [ ] Research question is current.
- [ ] Main Space link works.
- [ ] Paper repo link works.
- [ ] Journal link works.
- [ ] Hugging Face profile/Collection link works.
- [ ] "What I'm Building Now" names the current next step.

**Minimal profile update:**

```markdown
## What I'm Building Now

- Testing <Space name> with <kind of input>
- Revising `PAPER.md` to connect <Space result> with <verified source>
- Looking for feedback on <specific thing peer testers should try>
```

## 6. Peer Testing Request

Before Session 11, write one concrete request for classmates:

```markdown
When you test my Space, please try:

1. <input type>
2. <input type>
3. <input type>

Tell me whether:

- the output is useful for <audience>
- the result supports my paper's claim
- anything in the profile/paper/Space feels disconnected
```

## What Good Looks Like

A strong Session 10 integration sounds like this:

> "My profile says I'm investigating whether image models can keep a music-performance explanation useful for a student musician. My Space takes a music prompt and returns practice advice. In `PAPER.md`, I added one result from the Space and connected it to a verified source about automated music transcription. The limitation is that my test set is tiny and only uses examples I wrote myself. In Session 11, I want someone to try a prompt from their own instrument and tell me whether the advice is actually useful."

Notice: the profile, Space, paper, journal, and next testing request are all the same project.

## Rescue Paths

**If your Space is broken:** paste the error into the journal, fix one obvious issue, and revise the paper around what the failure shows.

**If your paper is empty:** write one honest paragraph using the Claim-Evidence-Source Chain.

**If your profile is empty:** add only four links: paper, Space, journal, Hugging Face. Then add the current research question.

**If your citations are weak:** use one verified source only. One real citation beats five fake or unsupported ones.

---

AI + Research Level 2 • Session 10: Polish, Integrate, and Tell the Portfolio Story

# Research Journal

## Week 2 Thoughts about Spaces

I've got lots of thoughts. This week I've been browsing Hugging Face Spaces to see what people are building, and one space in particular caught my eye.

### Smol AI WorldCup

**Link:** [ginigen-ai/smol-worldcup](https://huggingface.co/spaces/ginigen-ai/smol-worldcup)

The first thing you notice about this space is the *visual design*. Most Hugging Face Spaces use the default Gradio theme — clean but plain. This one goes in a completely different direction: a **dark green and gold color scheme** that feels like you're watching a football broadcast. The typography is bold and stylized, with all-caps headers and a monospaced font that gives it an official, tournament-style feel.

#### What makes it interesting

1. **The theme itself** — turning a model benchmark into a World Cup competition is a creative way to make leaderboards fun
2. **The SHIFT framework** — they invented their own 5-axis scoring system (Size, Honesty, Intelligence, Fast, Thrift)
3. **League tiers** — models are grouped into leagues (League One, La Liga, Premier, Champions) just like real football
4. **The ranking formula** — `WCS = √(SHIFT × PIR_norm)` balances quality *and* efficiency, so a model can't just be smart or just be small

#### Space features at a glance

| Feature | Details |
|---------|---------|
| Models evaluated | 18 |
| Benchmark questions | 125 |
| Languages covered | 7 |
| Scoring axes | 5 (SHIFT) |
| League tiers | 4 |
| Season | Season 1 — March 2026 |
| Creator | ginigen-ai |

#### Why this matters for us

This is a great example of how **design choices change the way people interact with information**. A plain table of benchmark scores is boring. Wrapping it in a World Cup metaphor — with leagues, rankings, and a custom formula — makes you actually *want* to explore the data. It's the same information, presented in a way that tells a story.

> "Both quality AND efficiency must be high. A model that's smart but huge, or tiny but dumb, ranks low."
> — from the space's description of the SHIFT framework

---

*Added March 14, 2026*

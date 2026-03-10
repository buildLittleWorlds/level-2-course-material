# User-Centered Design / Usability

Session 9 Research Method

## What It Is

User-centered design means shifting your question from "does the model work?" to "can a real person use it?" A model that classifies text perfectly is useless if the output says "POSITIVE 0.9714" and your user is a restaurant owner who wants to know if a customer is happy. Usability testing puts your tool in front of someone who didn't build it and watches what happens — where they get confused, where they give up, and where they light up.

## When Researchers Use It

- A children's book author reads her draft to a group of five-year-olds and watches their faces. She doesn't ask "do you like it?" — she watches where they lean in, where they fidget, and where they ask "what does that mean?" The audience's behavior is the data, not their opinions.
- A hospital redesigns its patient intake forms by sitting next to patients and watching them fill out the old version. Every question that makes someone pause, squint, or ask the receptionist for help gets rewritten. The form didn't change because of a design theory — it changed because of real people struggling with it.
- A game designer runs a playtest where new players try a tutorial level with no instructions. She records where they die, where they get stuck, and where they accidentally skip the thing they were supposed to learn. The failures reveal what the tutorial needs to teach.

## How to Apply It

1. **Name your user.** Not "everyone" — one specific person. A restaurant owner reading reviews. A student checking email tone. A journal keeper tracking mood. The more specific, the better your design decisions.
2. **Redesign the interface.** Change the title, description, examples, and output labels so they make sense to YOUR user. "POSITIVE 0.97" becomes "Happy Customer — consider thanking them." Same model, completely different experience.
3. **Test with someone who didn't build it.** Hand your tool to another person (a classmate, a family member, anyone) with zero explanation. Watch what they do. Where do they hesitate? What do they misunderstand? What do they wish it said? Their confusion is your redesign checklist.

## Key Vocabulary

- **User-centered design** — Designing a tool around the needs, knowledge, and context of a specific person, not around the capabilities of the model.
- **Usability testing** — Putting your tool in front of a real user and observing what happens. The goal is to find confusion, not to confirm that it works.
- **Prompt engineering** — Designing the inputs, examples, and framing around a model to shape what it produces. Not just "talking to ChatGPT" — it's the entire experience you build around an AI system.
- **Output framing** — How you present a model's raw prediction to a human. The same result can be helpful or meaningless depending on how you label and explain it.

## This Week's Shared Example

In class, we took the same sentiment model from Session 4 and redesigned it as a Restaurant Review Analyzer. We changed the title, wrote a description for restaurant owners (not programmers), added realistic review examples, and replaced "POSITIVE / NEGATIVE" with "Happy Customer / Unhappy Customer" plus a suggested action. The model didn't change at all — but the tool went from a technical demo to something a real person could actually use.

## Apply It to Your Own Topic

- Pick a model or Space from your Collection. Imagine one specific person who would use it — not a programmer, not a classmate, but someone in the real world with a real problem.
- Redesign everything around that person. What would you call it? What examples would you show? What should the output say in plain language?
- Now test it. Show your redesigned tool to someone (a friend, a family member, a classmate who wasn't involved) with no explanation. Just hand it to them and watch. Where do they get confused?
- Write down three things you'd change based on watching someone use it. That list is your usability report — and it's more valuable than any feature you could add.
- Ask yourself the harder question: should this tool exist for this person? Is it helpful, or is it invasive? Would the user feel empowered or surveilled?

See `GUIDE-research-journal.md` for how to structure your redesign experiment as a journal entry.

## Explore the Training Data

When you redesign a sentiment tool for a specific audience, the training data question flips: instead of "what did the model learn from?" you ask "does the training data look like what my user will actually type?" Browsing real-world review datasets shows you the gap between training data and real use. No code required — open the dataset page and click the viewer.

- **[Yelp/yelp_review_full](https://hf.co/datasets/Yelp/yelp_review_full)** — Yelp reviews with 1-5 star ratings. This is the kind of data a restaurant review analyzer would actually process in the real world. Browse the 1-star and 5-star reviews — notice how different they sound from the movie review sentences in SST-2. A tool designed for restaurant owners needs to handle this kind of language, not film criticism.
- **[fancyzhx/amazon_polarity](https://hf.co/datasets/fancyzhx/amazon_polarity)** — 35 million Amazon reviews with binary polarity. Product reviews have their own style — short, practical, full of specific complaints and praise. If your redesign targets product reviewers, this is the world your user lives in. Scroll through and notice what "positive" and "negative" mean when money and expectations are involved.

This is the real data your tool would process. If the training data looks nothing like it, your redesign has a domain shift problem on top of a design problem.

---

AI + Research Level 2 • Session 9: Make It Actually Useful

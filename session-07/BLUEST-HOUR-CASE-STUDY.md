# The Bluest Hour Case Study

*A three-stage worked example for Session 7. Read this first; it's the arc your own project will trace.*

---

## The three stages

| Stage | What it is | Link |
|---|---|---|
| **1. Original Space** | A Gradio app. Twilight-gradient background, glassmorphic cards, a "when should I walk tonight" predictor for Godfrey, Illinois. Deployed on Hugging Face. | [github.com/buildLittleWorlds/bluest-hour](https://github.com/buildLittleWorlds/bluest-hour) · [hf.co/spaces/profplate/bluest-hour](https://huggingface.co/spaces/profplate/bluest-hour) |
| **2. Redesigned Space** | The same question asked a different way. Almanac / ephemeris aesthetic. IBM Plex Mono + Source Serif 4. Ephemeris table, solar-altitude chart, seasonal blue-hour curve, 28-emotion walk journal using RoBERTa-GoEmotions in the browser. | [github.com/buildLittleWorlds/bluest-hour-almanac](https://github.com/buildLittleWorlds/bluest-hour-almanac) · [hf.co/spaces/profplate/bluest-hour-almanac](https://huggingface.co/spaces/profplate/bluest-hour-almanac) |
| **3. Paper** | A short working paper, in markdown, living inside the redesigned repo. Reads the Space as a small intellectual object. Masthead → abstract → §§ I–XI → colophon → footnotes. | [PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) |

## What changed between Stage 1 and Stage 2

Same question, different form. A blue-hour walk is the same phenomenon in both apps — the interval between civil and nautical twilight, when the sky deepens to what Joan Didion called "the blue of the glass on a clear day at Chartres." What changed is the **genre** the app claims.

| axis | Stage 1 (original) | Stage 2 (almanac) |
|---|---|---|
| visual genre | consumer weather widget | nineteenth-century almanac |
| typography | Inter, sans-serif | IBM Plex Mono + Source Serif 4 |
| what it returns | a time to go outside | a time, a chart, a year, a journal field-note, a seasonal curve, a walk |
| what the model does | nothing — just math and an API | runs a 28-label emotion classifier on the user's walk note, in the browser, via WASM |
| argument the form makes | "glance at this and go" | "sit down, read the sky, write a field note" |

The redesign was not a visual upgrade. It was an argument about what kind of object the app wants to be.

## What changed between Stage 2 and Stage 3

The app was the first argument. The paper is the second. Where the app makes its argument **in form** (the almanac shape), the paper makes it **in prose**: it names the form, defends it against the alternatives, proposes a small category ("ephemeral interfaces"), and ends with a task list of things the app does not yet do.

The paper does not replace the app. It does not advertise the app. It **comments on** the app — as if the paper's author had stumbled on the app in the wild and wanted to say what made it interesting.

## Why this matters for your project

You are at different points in this arc. Some of you have Stage 1 and are going to work on Stage 3 (the paper) while planning Stage 2 (the redesign) later. Some of you have Stage 2 — a second Space, a clear research question — and are ready to write the paper now. Some of you will use Stage 3 (the paper draft) to *discover* what Stage 2 should be.

All three orderings are fine. The arc is not a deadline; it's a map.

## What the Bluest Hour paper does that yours will also do

Open [PAPER.md](https://github.com/buildLittleWorlds/bluest-hour-almanac/blob/main/PAPER.md) and read it once end to end. Three moves to notice; you'll make versions of them in your own paper.

### 1. The masthead smuggles the author's one opinion in as if it were a fact

Look at the top of the paper:

```
LAT 38.9556°N · LNG 90.1868°W    JD 2461149.292    MOON waxing crescent, 4% · Δ +35m
```

Lat, longitude, Julian date, moon phase — and then **Δ +35m**. Everything else on that line is an astronomical constant. Δ is the author's opinion: *"at Godfrey, the bluest moment arrives 35 minutes before the textbook midpoint, because the bluffs above the Mississippi block the sun earlier than a sea-level horizon would."* It is the one piece of personal judgment in the paper, and the paper hides it among facts.

**Your version:** every paper has one tunable that encodes its author. Your paper-starter names it as "your Δ." Find it. Put it in the masthead if you can.

### 2. §VI treats the model as "just another ephemeris"

The Bluest Hour paper's §VI is titled "The field note, and why GoEmotions." The obvious framing of a transformer-in-the-browser section would be *"here is how a language model works."* The paper refuses that framing. It says instead: the almanac quantizes the continuous sky into civil / nautical / astronomical. The classifier quantizes the continuous feeling of a walk into 28 GoEmotions labels. Both are doing the same job.

**Your version:** don't describe what your model *does*. Describe what it *quantizes* — what continuous phenomenon it collapses into a vocabulary. This reframing is the single move most likely to turn your paper from a how-to into a reading.

### 3. §IX proposes a small category

Not a grand theory. Not a paradigm shift. A small, specific, defensible category. The Bluest Hour paper proposes **ephemeral interfaces**: *software whose primary function is to tell you when to stop using it.* Short definition. Three examples. That's it. It's a category you could argue with, and a reader who agreed with it would see tools like Bluest Hour differently forever.

**Your version:** your paper-starter has two candidate §IX categories suggested already. You will pick one during Session 7's drafting block. The AI will not write this section for you. **You will.**

## How this case study maps onto Session 7's work

During the 40-minute drafting block, you will do two things at once:

1. **Follow the template.** The Bluest Hour paper is the proof that the template works. You are not inventing a form; you are filling one.
2. **Steal the three moves.** Your masthead will smuggle your Δ. Your model section will quantize something. Your §IX will name a small category.

That's it. The rest is prose — and an AI can help with the prose. The form, the Δ, and the category: that's where the work becomes yours.

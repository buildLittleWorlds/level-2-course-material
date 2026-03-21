# Adversarial Test Stories for Story Emotion Arc Spaces

Three stories designed to break the Story Arc Spaces in three different ways. Paste each one into all four Story Arc Spaces (3-Sentiment, 6-Emotion, 7-Ekman, 28-GoEmotions) and compare the arc charts.

Each story is formatted with double line breaks between paragraphs so the Spaces split them correctly.

---

## Test 1: The Sarcastic Narrator

**What it tests:** Can the models detect tone that contradicts the words?

**Prediction:** The 3-sentiment model will read most paragraphs as positive because the surface vocabulary is positive. The 6 and 7-emotion models will likely show joy or surprise. The 28-emotion model might scatter across amusement, approval, and admiration — none of which capture sarcasm. All four arcs will look cheerful. The story is not cheerful.

**Paste this:**

```
Monday morning. My alarm went off at 5:45 and I thought, wow, what a blessing, another chance to be alive and productive. I absolutely love the sound of that alarm. It fills me with purpose. I sprang out of bed like someone who has their life completely figured out and definitely gets enough sleep.

First period was a delight. My teacher handed back our essays and I got a C-minus, which was awesome because it means I have so much room for growth. She wrote "see me after class" at the top, which I think is her way of saying she sees real potential in me. I can hardly wait for that conversation.

Lunch was the highlight of my day. The cafeteria served mystery meat again, and honestly, I admire the creativity. It takes real talent to make food that is simultaneously brown and gray. My friend dared me to eat it and I did, because I make excellent life choices and nothing bad ever happens to me.

After school I had the great privilege of missing my bus. What a fantastic opportunity to walk two miles in the rain. The rain was refreshing and cleansing and I felt so connected to nature as the water soaked through my backpack and into my homework. My essay on "perseverance" got especially wet, which I thought was poetic.

I got home and my mom asked how my day was. "Amazing," I said. "Truly one of the best days I've ever had." She looked at me for a long time and then said dinner would be ready in an hour. Even she could tell I was radiating joy.

I went to my room and lay on my bed and stared at the ceiling, smiling, because everything is wonderful and I am so grateful for every single moment of this incredible life.
```

---

## Test 2: The Mixed-Emotion Story

**What it tests:** Can the models handle two or more genuine emotions happening at the same time in the same paragraph?

**Prediction:** The 3-sentiment model will collapse each paragraph to a single label, losing the mixture. The 6 and 7-emotion models will pick one dominant emotion and flatten the rest. The 28-emotion model is the most interesting — it might distribute scores across several emotions, but the question is whether that distribution looks like "detecting complexity" or "being confused." Look at the confidence scores: if the top emotion is only at 18% and the next five are all around 12%, the model is probably confused, not insightful.

**Paste this:**

```
The acceptance letter came on a Tuesday. I read it three times to make sure it was real. Full scholarship, my first choice, the school I'd been dreaming about since seventh grade. I screamed and then I cried and then I went very quiet, because I suddenly realized that getting in meant leaving. My best friend lives next door. We've walked to school together every day for six years. That walk ends in August.

I told my dad at dinner. He put his fork down and his eyes got red and he said he was proud of me, and then he said he wasn't ready. He said both things in the same sentence. My little sister asked if she could have my room and everyone laughed, but it was the kind of laughing where nobody actually thinks it's funny, it's just that someone needed to break the silence before it broke us.

The graduation party was beautiful and terrible. My mom made my favorite cake and decorated the yard with photos of me from every year of school. Baby photos, gap-toothed photos, awkward middle school photos. Everyone I loved was in one place and I kept thinking: this is the last time all of these people will be in the same room. I wanted to memorize every face. I also wanted it to be over so I could stop feeling so much.

I spent the last week of summer packing. Every object was a choice. The stuffed bear from when I was five — do I bring it and seem childish, or leave it and lose the only thing that smells like home? My books went into boxes. My posters came off the walls and left those pale rectangles behind, like ghosts of the room I used to live in. The room was still mine but it didn't feel like mine anymore.

Moving day was worse than I expected and better than I expected. My mom held it together until the very last hug, and then she didn't, and then I didn't. But when they drove away and I turned around and looked at the campus, I felt something I hadn't felt in months: curiosity. Not happiness, not yet. But a door opening. The grief and the excitement were the same size, and they were both mine, and I held them in each hand and walked forward.
```

---

## Test 3: The Earth Doesn't Feel Anything

**What it tests:** Do the models detect actual emotions, or do they just react to words that sound emotional?

**Prediction:** All four models will draw dramatic emotional arcs — probably fear and negativity for the eruption and fire paragraphs, positivity and joy for the regrowth paragraph. But there are no people in this story. Nobody is feeling anything. The mountain doesn't feel anger. The fire doesn't feel hunger. The wildflowers don't feel joy. The models are projecting human emotions onto rocks and weather because the words "erupt," "destroy," "consume," and "bloom" co-occur with emotional language in the training data. The arc charts will look like a story about feelings, but it's a story about geology.

**Paste this:**

```
The mountain had been building pressure for nine hundred years. Magma pushed upward through cracks in the basalt, heating the groundwater to a boil, swelling the north face outward by three feet. On the morning of the eruption, the summit collapsed. A column of ash and rock exploded sixteen miles into the atmosphere. The blast flattened three hundred square miles of forest in under four minutes.

Pyroclastic flows — superheated gas and pulverized stone moving at four hundred miles per hour — poured down the valleys. They vaporized rivers. They stripped the bark from trees and then stripped the trees from the earth. Where the flows met the lake, the water boiled instantly, sending a wall of steam a thousand feet into the air. The temperature at ground level was six hundred degrees.

For three months, nothing grew. The landscape was gray and silent. Ash buried everything under twenty feet of powder. The rivers ran thick with sediment, clogged and lifeless. No birds returned. No insects moved through the stillness. Rain fell on the ash and turned it to cement. The mountain continued to smoke quietly, occasionally trembling, the way a machine idles after running hard.

The first green appeared seven months later: a single fireweed pushing through a crack in the ash crust. Then another, and another, until the gray slopes were spotted with pink. Gophers that had been underground during the blast tunneled upward, churning buried soil into the ash layer, mixing nutrients back into the dead ground. Elk wandered in from the edges, and where they walked, seeds fell from their fur.

Within five years, the valleys were thick with wildflowers. Alder trees colonized the riverbanks and pulled nitrogen from the air into the soil. Frogs returned to the ponds. Hawks circled overhead. The forest was not recovering — it was being replaced by something entirely new, built from scratch on the bones of the old one. The mountain watched over all of it, steam still curling from its crater, saying nothing.
```

---

## Teaching Notes

### Running the Test

Open all four Story Arc Spaces in separate tabs. Paste the same story into each. Wait for the arc charts to render. Compare.

### What to Look For

**Test 1 (Sarcasm):** Are the arcs positive? They should be — the words are positive. The tone is miserable. Ask students: "According to these four models, did this person have a good day?"

**Test 2 (Mixed Emotions):** Does any model show two strong emotions in the same paragraph? Or does every paragraph collapse to one winner? Ask students: "Is there a single paragraph in this story where the narrator is feeling only one thing?"

**Test 3 (Nature):** Do the arcs show emotions? They almost certainly will. Ask students: "Who is feeling these emotions? Point to the character in the story who is afraid, or angry, or happy." There is no such character. The models are reading emotion where there is none.

### The Three Failure Modes

| Test | What the Model Does | What It Should Do | Name for the Failure |
|------|--------------------|--------------------|---------------------|
| 1 — Sarcasm | Reads the words, misses the tone | Detect that the surface meaning and the intended meaning are opposite | **Tone deafness** — the model hears the notes but misses the music |
| 2 — Mixed Emotions | Picks one emotion per paragraph | Represent that two or more emotions coexist at the same time | **Emotional flattening** — the model forces complex feelings into a single label |
| 3 — Nature | Projects emotions onto rocks and weather | Recognize that emotional vocabulary in a non-human context does not indicate actual emotion | **Anthropomorphic projection** — the model assumes everything that sounds emotional is emotional |

### Connection to Session 3's Framework

All three map onto the noise vs. meaning distinction from Session 3, but in different directions:

- **Test 1:** The meaning is there but reversed. The model gets the words right and the meaning wrong.
- **Test 2:** The meaning is there but multiple. The model can only hold one meaning at a time.
- **Test 3:** The meaning isn't there at all. The model invents meaning that doesn't exist.

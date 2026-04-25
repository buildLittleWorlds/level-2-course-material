# Research Journal: Motion Continuity Lab

## Week 1 - Pretty frames are not animation

I started with a simple animation prompt:

> A paper lantern floats away from a child during a rainy festival, then returns glowing brighter.

The AI output made three beautiful moments: the child holding the lantern, the lantern in the rain, and the lantern glowing. But the connection between moments was weak. It did not explain how the lantern moved, how the child reacted, or what changed between beats.

Question raised: Is the tool helping with animation, or only with still-image ideas?

## Week 2 - Start, change, end

This week I forced the prompt into three beats:

- Start: the child holds the lantern under an umbrella
- Change: wind pulls the lantern away
- End: the lantern returns, glowing brighter

This improved the output. The model gave clearer beats. But the continuity still broke. In one version, the umbrella disappeared in the middle beat and returned at the end. In another, the lantern changed from red to gold without explanation.

I realized continuity means tracking what stays the same while motion happens.

## Week 3 - Source detour

Consensus searches on text-to-video generation showed that temporal consistency is a major research problem. I am not building a video model, but the same idea applies to animation writing: the output needs to preserve characters, objects, motion, and cause-and-effect across time.

My question sharpened:

> Which AI tools are best at helping with animation scene generation when the real challenge is motion continuity instead of a single pretty frame?

## Week 4 - The continuity checklist

I made a checklist:

- Character consistency: Does the character stay recognizable?
- Object consistency: Do key props stay present and stable?
- Motion cause: Does one beat cause the next?
- Mood transition: Does emotion shift gradually?
- Camera/scene continuity: Does the setting stay coherent?

The checklist made weak outputs easier to see. Some tools were great at mood words but bad at action logic. Others gave practical beat lists but weak visual atmosphere.

## Week 5 - Tool-switching as evidence

I tested the same three-beat scene through different tool styles: one for cinematic description, one for storyboard panels, and one for animator notes.

The animator-notes style was the least beautiful but the most useful. It included actions like "lantern string stretches," "child steps forward," and "umbrella tilts in wind." Those details make motion possible.

This surprised me. The best animation helper might not be the tool that writes the prettiest scene. It might be the tool that tracks small physical changes.

## Week 6 - Paper direction

The paper should argue:

> For animation planning, outputs should be judged by continuity across beats, not by the beauty of individual frames.

The limitation is that this example evaluates written scene plans, not actual rendered animation. A real next step would compare generated storyboards or video clips and ask animators to rate continuity.

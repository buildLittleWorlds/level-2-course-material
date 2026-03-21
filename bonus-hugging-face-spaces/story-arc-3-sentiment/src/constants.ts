export const MODEL_ID = "cardiffnlp/twitter-roberta-base-sentiment-latest";
export const APP_TITLE = "Story Emotion Arc";
export const APP_SUBTITLE = "3-Class Sentiment";
export const APP_DESCRIPTION =
  "Paste a multi-paragraph story to see how positive, negative, and neutral sentiment shifts across the narrative. The simplest emotional lens.";

export const EMOTIONS = [
  { label: "negative", color: "#e74c3c", emoji: "\u{1F44E}" },
  { label: "neutral", color: "#95a5a6", emoji: "\u{1F610}" },
  { label: "positive", color: "#27ae60", emoji: "\u{1F44D}" },
] as const;

export const MAX_VISIBLE_LINES = 3;
export const MAX_PARAGRAPHS = 15;

// This model returns LABEL_0/1/2 instead of named labels
export const LABEL_MAP: Record<string, string> = {
  LABEL_0: "negative",
  LABEL_1: "neutral",
  LABEL_2: "positive",
  label_0: "negative",
  label_1: "neutral",
  label_2: "positive",
  Negative: "negative",
  Neutral: "neutral",
  Positive: "positive",
};

export const THEME = {
  bgLight: "#F8FAFC",
  bgGrid: "#E2E8F0",
  bgDark: "#CBD5E1",
  accent: "#6366F1",
  accentDark: "#4F46E5",
  accentLight: "#818CF8",
  textBlack: "#1E1E1E",
  black: "#000000",
  white: "#FFFFFF",
  errorRed: "#EF4444",
} as const;

export const EXAMPLE_TEXTS = [
  `The morning sun cast long shadows across the quiet village. Birds sang in the ancient oaks, and the air smelled of fresh bread. Everything felt peaceful.

Then the sirens started. At first just one thin wail from the harbor, then another and another, until the whole sky vibrated with warning.

Maria grabbed her daughter's hand and ran. Behind her she heard shouting, the crash of something heavy, glass breaking.

They reached the shelter just as rain began. Inside, families huddled together. A baby cried. An old man prayed quietly. Maria held her daughter close.

By evening the sirens had stopped. They emerged into a changed world \u2014 trees down, windows shattered, but buildings standing. Neighbors helped each other, passing water, sharing food.

Maria watched her daughter playing with other children in the rubble, already turning disaster into adventure. She felt something unexpected: hope.`,
  `Once upon a time, in a kingdom nestled between two mountains, there lived a young girl who could hear the whispers of stones. The villagers thought her strange but harmless.

One autumn morning, the stones began to scream. The girl ran to the village square, shouting warnings that no one believed. They laughed and returned to their market stalls.

By noon the ground shook. Cracks split the cobblestones. The mountain to the north groaned like a wounded beast, and boulders tumbled into the river.

The villagers fled to the girl's cottage on the hill \u2014 the only place the stones had told her was safe. They huddled in silence, ashamed of their laughter.

When dawn came, the valley was transformed. Where the river once flowed, a lake glittered in the sunlight. New paths wound through fields of wildflowers that had not been there before.

The girl smiled. The stones were singing again.`,
];

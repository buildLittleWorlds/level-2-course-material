export const MODEL_ID = "SamLowe/roberta-base-go_emotions";
export const APP_TITLE = "Story Emotion Arc";
export const APP_SUBTITLE = "28 GoEmotions";
export const APP_DESCRIPTION =
  "Paste a multi-paragraph story to see how 28 fine-grained emotions rise and fall. GoEmotions detects subtle states like admiration, curiosity, and grief.";

export const EMOTIONS = [
  { label: "admiration", color: "#FFD700", emoji: "\u{1F929}" },
  { label: "amusement", color: "#FF69B4", emoji: "\u{1F604}" },
  { label: "anger", color: "#DC143C", emoji: "\u{1F620}" },
  { label: "annoyance", color: "#CD5C5C", emoji: "\u{1F612}" },
  { label: "approval", color: "#32CD32", emoji: "\u{1F44D}" },
  { label: "caring", color: "#FF8C69", emoji: "\u{1F917}" },
  { label: "confusion", color: "#DDA0DD", emoji: "\u{1F615}" },
  { label: "curiosity", color: "#00CED1", emoji: "\u{1F9D0}" },
  { label: "desire", color: "#FF1493", emoji: "\u{1F60D}" },
  { label: "disappointment", color: "#708090", emoji: "\u{1F61E}" },
  { label: "disapproval", color: "#B22222", emoji: "\u{1F44E}" },
  { label: "disgust", color: "#556B2F", emoji: "\u{1F922}" },
  { label: "embarrassment", color: "#F08080", emoji: "\u{1F633}" },
  { label: "excitement", color: "#FF4500", emoji: "\u{1F389}" },
  { label: "fear", color: "#8B008B", emoji: "\u{1F628}" },
  { label: "gratitude", color: "#3CB371", emoji: "\u{1F64F}" },
  { label: "grief", color: "#4682B4", emoji: "\u{1F62D}" },
  { label: "joy", color: "#FFA500", emoji: "\u{1F60A}" },
  { label: "love", color: "#E91E63", emoji: "\u{2764}\u{FE0F}" },
  { label: "nervousness", color: "#BA55D3", emoji: "\u{1F630}" },
  { label: "optimism", color: "#98FB98", emoji: "\u{1F31F}" },
  { label: "pride", color: "#DAA520", emoji: "\u{1F60E}" },
  { label: "realization", color: "#20B2AA", emoji: "\u{1F4A1}" },
  { label: "relief", color: "#66CDAA", emoji: "\u{1F60C}" },
  { label: "remorse", color: "#778899", emoji: "\u{1F614}" },
  { label: "sadness", color: "#4169E1", emoji: "\u{1F622}" },
  { label: "surprise", color: "#FF8C00", emoji: "\u{1F632}" },
  { label: "neutral", color: "#A9A9A9", emoji: "\u{1F610}" },
] as const;

export const MAX_VISIBLE_LINES = 5;
export const MAX_PARAGRAPHS = 15;

export const LABEL_MAP: Record<string, string> | null = null;

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

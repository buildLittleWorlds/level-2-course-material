export type AppStatus = "idle" | "loading" | "done" | "error";

export interface EmotionConfig {
  readonly label: string;
  readonly color: string;
  readonly emoji: string;
}

export interface ParagraphResult {
  index: number;
  text: string;
  preview: string;
  topEmotion: string;
  topColor: string;
  scores: Record<string, number>;
}

export interface AnalysisResult {
  paragraphs: ParagraphResult[];
}

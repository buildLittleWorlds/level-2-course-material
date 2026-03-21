import { EMOTIONS, MAX_VISIBLE_LINES } from "../constants";
import { useState } from "react";
import type { ParagraphResult } from "../types";

interface Props {
  paragraphs: ParagraphResult[];
  visibleEmotions: Set<string>;
  highlightedEmotion: string | null;
  onToggleEmotion: (label: string) => void;
  onHoverEmotion: (label: string | null) => void;
}

export const EmotionLegend = ({
  paragraphs,
  visibleEmotions,
  highlightedEmotion,
  onToggleEmotion,
  onHoverEmotion,
}: Props) => {
  const [expanded, setExpanded] = useState(false);

  // Rank emotions by total intensity across all paragraphs
  const ranked = [...EMOTIONS].sort((a, b) => {
    const totalA = paragraphs.reduce(
      (sum, p) => sum + (p.scores[a.label] ?? 0),
      0,
    );
    const totalB = paragraphs.reduce(
      (sum, p) => sum + (p.scores[b.label] ?? 0),
      0,
    );
    return totalB - totalA;
  });

  const showExpander = EMOTIONS.length > MAX_VISIBLE_LINES;
  const primaryEmotions = showExpander
    ? ranked.slice(0, MAX_VISIBLE_LINES)
    : ranked;
  const secondaryEmotions = showExpander
    ? ranked.slice(MAX_VISIBLE_LINES)
    : [];

  const renderItem = (emotion: (typeof EMOTIONS)[number]) => {
    const isVisible = visibleEmotions.has(emotion.label);
    const isHighlighted = highlightedEmotion === emotion.label;

    return (
      <button
        key={emotion.label}
        onClick={() => onToggleEmotion(emotion.label)}
        onMouseEnter={() => onHoverEmotion(emotion.label)}
        onMouseLeave={() => onHoverEmotion(null)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-lg border cursor-pointer transition-all duration-200 hover:-translate-y-0.5 bg-transparent"
        style={{
          borderColor: isHighlighted
            ? emotion.color
            : isVisible
              ? `${emotion.color}40`
              : "#E2E8F0",
          opacity: isVisible ? 1 : 0.35,
          backgroundColor: isHighlighted ? `${emotion.color}0D` : "transparent",
        }}
      >
        <span
          className="w-3 h-3 rounded-sm inline-block flex-shrink-0 transition-transform"
          style={{
            backgroundColor: emotion.color,
            transform: isHighlighted ? "scale(1.3)" : "scale(1)",
          }}
        />
        <span
          className="text-xs font-medium capitalize"
          style={{
            color: isVisible ? "#1E1E1E" : "#94A3B8",
            fontWeight: isHighlighted ? 700 : 500,
          }}
        >
          {emotion.label}
        </span>
        <span className="text-xs">{emotion.emoji}</span>
      </button>
    );
  };

  return (
    <div className="space-y-2">
      <div className="flex flex-wrap gap-2">
        {primaryEmotions.map(renderItem)}

        {showExpander && !expanded && (
          <button
            onClick={() => setExpanded(true)}
            className="px-3 py-1.5 rounded-lg border text-xs text-gray-500 cursor-pointer hover:bg-gray-50 transition-colors bg-transparent"
            style={{ borderColor: "#E2E8F0" }}
          >
            +{secondaryEmotions.length} more
          </button>
        )}
      </div>

      {expanded && secondaryEmotions.length > 0 && (
        <div className="flex flex-wrap gap-2 animate-enter">
          {secondaryEmotions.map(renderItem)}
          <button
            onClick={() => setExpanded(false)}
            className="px-3 py-1.5 rounded-lg border text-xs text-gray-500 cursor-pointer hover:bg-gray-50 transition-colors bg-transparent"
            style={{ borderColor: "#E2E8F0" }}
          >
            Show less
          </button>
        </div>
      )}

      <p className="text-[10px] font-mono text-gray-400 uppercase tracking-widest">
        Click to toggle &middot; Hover to highlight
      </p>
    </div>
  );
};

import { useState } from "react";
import { EMOTIONS, THEME } from "../constants";
import type { ParagraphResult } from "../types";

interface Props {
  paragraphs: ParagraphResult[];
  highlightedParagraph: number | null;
  onHoverParagraph: (index: number | null) => void;
}

export const ParagraphCards = ({
  paragraphs,
  highlightedParagraph,
  onHoverParagraph,
}: Props) => {
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);

  return (
    <div className="space-y-2">
      {paragraphs.map((p, i) => {
        const isHighlighted = highlightedParagraph === p.index;
        const isExpanded = expandedIndex === p.index;

        // Top 3 emotions for mini bar
        const top3 = Object.entries(p.scores)
          .sort(([, a], [, b]) => b - a)
          .slice(0, 3);

        return (
          <div
            key={p.index}
            className="animate-enter rounded-xl border transition-all duration-200 cursor-pointer overflow-hidden"
            style={{
              animationDelay: `${i * 60}ms`,
              borderColor: isHighlighted ? `${p.topColor}80` : THEME.bgGrid,
              borderLeftWidth: 4,
              borderLeftColor: p.topColor,
              backgroundColor: isHighlighted
                ? `${p.topColor}08`
                : `${THEME.white}CC`,
              transform: isHighlighted ? "translateX(4px)" : "none",
            }}
            onMouseEnter={() => onHoverParagraph(p.index)}
            onMouseLeave={() => onHoverParagraph(null)}
            onClick={() =>
              setExpandedIndex(isExpanded ? null : p.index)
            }
          >
            {/* Card header */}
            <div className="flex items-center gap-3 px-4 py-3">
              {/* Paragraph number */}
              <span
                className="text-xs font-bold font-mono w-7 text-center flex-shrink-0"
                style={{ color: "#94A3B8" }}
              >
                P{p.index}
              </span>

              {/* Top emotion badge */}
              <span
                className="px-2.5 py-0.5 rounded-full text-xs font-semibold text-white flex-shrink-0 capitalize"
                style={{ backgroundColor: p.topColor }}
              >
                {p.topEmotion}
              </span>

              {/* Preview text */}
              <span className="text-sm text-gray-600 flex-1 truncate">
                {p.preview}
              </span>

              {/* Mini score bar */}
              <div className="flex h-2 w-24 rounded-full overflow-hidden flex-shrink-0 border border-gray-200">
                {top3.map(([label, score]) => {
                  const color =
                    EMOTIONS.find((e) => e.label === label)?.color ?? "#999";
                  return (
                    <div
                      key={label}
                      style={{
                        width: `${score}%`,
                        backgroundColor: color,
                        minWidth: score > 0 ? 2 : 0,
                      }}
                    />
                  );
                })}
              </div>

              {/* Expand indicator */}
              <svg
                className="w-4 h-4 text-gray-400 flex-shrink-0 transition-transform duration-200"
                style={{
                  transform: isExpanded ? "rotate(180deg)" : "rotate(0deg)",
                }}
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="m19.5 8.25-7.5 7.5-7.5-7.5"
                />
              </svg>
            </div>

            {/* Expanded content */}
            {isExpanded && (
              <div
                className="px-4 pb-4 pt-1 border-t space-y-3 animate-enter"
                style={{ borderColor: THEME.bgGrid }}
              >
                {/* Full text */}
                <p className="text-sm text-gray-700 leading-relaxed">
                  {p.text}
                </p>

                {/* All scores as bars */}
                <div className="space-y-1.5">
                  {Object.entries(p.scores)
                    .sort(([, a], [, b]) => b - a)
                    .map(([label, score]) => {
                      const emotion = EMOTIONS.find(
                        (e) => e.label === label,
                      );
                      if (!emotion) return null;
                      return (
                        <div
                          key={label}
                          className="flex items-center gap-2"
                        >
                          <span className="text-xs w-20 text-right capitalize text-gray-500 font-mono">
                            {label}
                          </span>
                          <div className="flex-1 h-2.5 rounded-full bg-gray-100 overflow-hidden">
                            <div
                              className="h-full rounded-full transition-all duration-500"
                              style={{
                                width: `${score}%`,
                                backgroundColor: emotion.color,
                                minWidth: score > 0 ? 4 : 0,
                              }}
                            />
                          </div>
                          <span className="text-xs font-mono text-gray-400 w-8">
                            {score}%
                          </span>
                        </div>
                      );
                    })}
                </div>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

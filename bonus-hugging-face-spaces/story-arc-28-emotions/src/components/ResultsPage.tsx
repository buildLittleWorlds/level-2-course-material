import { useState, useCallback } from "react";
import { useAnalysisContext } from "../App";
import { THEME, EMOTIONS, APP_TITLE, APP_SUBTITLE, MODEL_ID } from "../constants";
import { AppGridBackground, useMountedTransition } from "./SharedUI";
import { EmotionChart } from "./EmotionChart";
import { EmotionLegend } from "./EmotionLegend";
import { ParagraphCards } from "./ParagraphCards";

export const ResultsPage = () => {
  const { result, reset } = useAnalysisContext();
  const mounted = useMountedTransition();

  const [highlightedEmotion, setHighlightedEmotion] = useState<string | null>(
    null,
  );
  const [highlightedParagraph, setHighlightedParagraph] = useState<
    number | null
  >(null);
  const [visibleEmotions, setVisibleEmotions] = useState<Set<string>>(
    () => new Set(EMOTIONS.map((e) => e.label)),
  );

  const handleToggleEmotion = useCallback((label: string) => {
    setVisibleEmotions((prev) => {
      const next = new Set(prev);
      if (next.has(label)) {
        if (next.size > 1) next.delete(label);
      } else {
        next.add(label);
      }
      return next;
    });
  }, []);

  if (!result) return null;

  return (
    <AppGridBackground
      className="min-h-screen px-4 py-6 md:px-6"
      style={{ color: THEME.textBlack }}
    >
      <div
        className={`max-w-5xl mx-auto transition-all duration-700 ${
          mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
        }`}
      >
        {/* Top bar */}
        <div className="flex items-center justify-between mb-6 animate-enter">
          <div>
            <h1 className="text-2xl md:text-3xl font-semibold tracking-tight">
              {APP_TITLE}
            </h1>
            <p
              className="text-xs font-mono uppercase tracking-widest mt-1"
              style={{ color: THEME.accent }}
            >
              {APP_SUBTITLE} &middot; {result.paragraphs.length} paragraphs
            </p>
          </div>
          <button
            onClick={reset}
            className="px-4 py-2 rounded-xl border text-sm font-semibold transition-all duration-300 hover:-translate-y-0.5 cursor-pointer bg-transparent"
            style={{
              borderColor: THEME.bgDark,
              color: THEME.textBlack,
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = `${THEME.accent}0D`;
              e.currentTarget.style.borderColor = THEME.accent;
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = "transparent";
              e.currentTarget.style.borderColor = THEME.bgDark;
            }}
          >
            New Analysis
          </button>
        </div>

        {/* Chart card */}
        <div
          className="rounded-2xl border shadow-lg p-5 md:p-6 mb-6 animate-enter delay-100"
          style={{
            backgroundColor: `${THEME.white}E6`,
            borderColor: THEME.bgGrid,
          }}
        >
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <svg
                className="w-4 h-4 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
                />
              </svg>
              <span className="text-xs font-bold text-gray-500 uppercase tracking-widest">
                Emotion Arc
              </span>
            </div>
            <span
              className="text-[10px] font-mono uppercase tracking-widest px-2 py-1 rounded-full"
              style={{
                backgroundColor: THEME.bgLight,
                color: "#94A3B8",
              }}
            >
              Hover dots for detail
            </span>
          </div>

          <EmotionChart
            paragraphs={result.paragraphs}
            highlightedEmotion={highlightedEmotion}
            highlightedParagraph={highlightedParagraph}
            visibleEmotions={visibleEmotions}
            onHoverEmotion={setHighlightedEmotion}
            onHoverParagraph={setHighlightedParagraph}
          />

          <div className="mt-5 pt-4 border-t" style={{ borderColor: THEME.bgGrid }}>
            <EmotionLegend
              paragraphs={result.paragraphs}
              visibleEmotions={visibleEmotions}
              highlightedEmotion={highlightedEmotion}
              onToggleEmotion={handleToggleEmotion}
              onHoverEmotion={setHighlightedEmotion}
            />
          </div>
        </div>

        {/* Paragraph cards */}
        <div className="animate-enter delay-200">
          <div className="flex items-center gap-2 mb-3">
            <svg
              className="w-4 h-4 text-gray-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={2}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
            <span className="text-xs font-bold text-gray-500 uppercase tracking-widest">
              Paragraphs
            </span>
            <span className="text-[10px] font-mono text-gray-400 ml-auto">
              Click to expand
            </span>
          </div>

          <ParagraphCards
            paragraphs={result.paragraphs}
            highlightedParagraph={highlightedParagraph}
            onHoverParagraph={setHighlightedParagraph}
          />
        </div>

        {/* Footer */}
        <div
          className="mt-8 pt-4 border-t flex items-center justify-between text-[10px] font-mono text-gray-400 animate-enter delay-300"
          style={{ borderColor: THEME.bgGrid }}
        >
          <span>model: {MODEL_ID}</span>
          <span>paragraphs: {result.paragraphs.length}</span>
        </div>
      </div>
    </AppGridBackground>
  );
};

import { useState } from "react";
import { useAnalysisContext } from "../App";
import {
  THEME,
  APP_TITLE,
  APP_SUBTITLE,
  APP_DESCRIPTION,
  EXAMPLE_TEXTS,
} from "../constants";
import {
  AppGridBackground,
  DocumentIcon,
  ChartIcon,
  StatusDot,
  useMountedTransition,
} from "./SharedUI";

const FEATURES = [
  {
    step: "1",
    title: "Paste Your Text",
    description:
      "Multi-paragraph stories, essays, or scenes. At least 2 paragraphs separated by blank lines. Works best up to ~1,500 words (15 paragraphs).",
  },
  {
    step: "2",
    title: "AI Analysis",
    description:
      "Each paragraph is scored by an emotion classification model running on Hugging Face servers.",
  },
  {
    step: "3",
    title: "See the Arc",
    description:
      "An interactive chart shows how emotions rise and fall across the narrative.",
  },
] as const;

export const LandingPage = () => {
  const { analyze, hfToken, updateToken } = useAnalysisContext();
  const mounted = useMountedTransition();
  const [text, setText] = useState("");
  const [showToken, setShowToken] = useState(false);

  const handleAnalyze = () => {
    if (text.trim()) analyze(text);
  };

  return (
    <AppGridBackground
      className="min-h-screen flex items-center justify-center p-6 overflow-y-auto"
      style={{ color: THEME.textBlack }}
    >
      <div
        className={`relative max-w-4xl w-full backdrop-blur-sm p-10 md:p-12 rounded-2xl border shadow-2xl transition-all duration-700 ${
          mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
        }`}
        style={{
          backgroundColor: `${THEME.white}F2`,
          borderColor: THEME.bgGrid,
        }}
      >
        {/* Status dot */}
        <div className="absolute top-6 right-6">
          <StatusDot />
        </div>

        <div className="space-y-10">
          {/* Header */}
          <div className="text-center space-y-4 animate-enter">
            <div className="flex flex-col items-center justify-center space-y-5">
              <div
                className="w-20 h-20 rounded-full flex items-center justify-center shadow-lg"
                style={{ backgroundColor: `${THEME.accent}1A` }}
              >
                <DocumentIcon
                  className="w-10 h-10"
                  style={{ color: THEME.accent }}
                />
              </div>
              <h1
                className="text-5xl md:text-6xl font-semibold tracking-tighter"
                style={{ color: THEME.textBlack }}
              >
                {APP_TITLE}
              </h1>
              <p
                className="text-lg font-mono uppercase tracking-widest"
                style={{ color: THEME.accent }}
              >
                {APP_SUBTITLE}
              </p>
            </div>
            <p className="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto font-light leading-relaxed">
              {APP_DESCRIPTION}
            </p>
          </div>

          {/* Feature cards */}
          <div
            className="grid grid-cols-1 md:grid-cols-3 gap-6 border-t border-b py-8 animate-enter delay-100"
            style={{ borderColor: THEME.bgGrid }}
          >
            {FEATURES.map((feature) => (
              <div key={feature.step} className="space-y-3 group">
                <div
                  className="w-10 h-10 rounded-lg flex items-center justify-center text-white font-bold text-lg shadow-sm transition-transform duration-300 group-hover:-translate-y-1"
                  style={{ backgroundColor: THEME.accent }}
                >
                  {feature.step}
                </div>
                <h4 className="font-semibold text-lg">{feature.title}</h4>
                <p className="text-gray-600 leading-relaxed text-sm">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>

          {/* Text input */}
          <div className="space-y-4 animate-enter delay-200">
            <textarea
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Paste a multi-paragraph story here...&#10;&#10;Separate paragraphs with blank lines.&#10;&#10;Like this."
              rows={8}
              className="w-full rounded-xl border px-5 py-4 text-base leading-relaxed resize-y focus:outline-none focus:ring-2 transition-shadow"
              style={{
                borderColor: THEME.bgDark,
                backgroundColor: THEME.white,
              }}
              onFocus={(e) =>
                (e.target.style.boxShadow = `0 0 0 2px ${THEME.accent}40`)
              }
              onBlur={(e) => (e.target.style.boxShadow = "none")}
            />

            {/* Example buttons */}
            <div className="flex flex-wrap gap-2">
              <span className="text-xs text-gray-400 font-mono uppercase tracking-wider self-center mr-1">
                Examples:
              </span>
              {EXAMPLE_TEXTS.map((example, i) => (
                <button
                  key={i}
                  onClick={() => setText(example)}
                  className="px-3 py-1.5 text-xs rounded-lg border cursor-pointer transition-all hover:-translate-y-0.5"
                  style={{
                    borderColor: THEME.bgDark,
                    backgroundColor: `${THEME.bgLight}`,
                    color: THEME.accent,
                  }}
                >
                  Story {i + 1}
                </button>
              ))}
            </div>
          </div>

          {/* Analyze button */}
          <div className="flex flex-col items-center animate-enter delay-300">
            <button
              onClick={handleAnalyze}
              disabled={!text.trim()}
              className="group relative px-8 py-4 text-white overflow-hidden transition-all hover:shadow-2xl hover:-translate-y-0.5 rounded-xl border-none cursor-pointer outline-none disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:translate-y-0 disabled:hover:shadow-none"
              style={{
                background: `linear-gradient(135deg, ${THEME.accentDark}, ${THEME.accent})`,
              }}
            >
              <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out" />
              <span className="relative font-bold text-lg tracking-wide flex items-center gap-3">
                <ChartIcon className="w-5 h-5" style={{ color: "white" }} />
                ANALYZE STORY
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  strokeWidth={2.5}
                  stroke="currentColor"
                  className="w-5 h-5 transition-transform duration-300 group-hover:translate-x-1"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"
                  />
                </svg>
              </span>
            </button>

            {/* HF Token toggle */}
            <div className="mt-6 w-full max-w-md">
              <button
                onClick={() => setShowToken(!showToken)}
                className="text-xs text-gray-400 hover:text-gray-600 font-mono uppercase tracking-wider cursor-pointer bg-transparent border-none"
              >
                {showToken ? "Hide" : "Advanced:"} HF Token (optional)
              </button>
              {showToken && (
                <div className="mt-2 flex gap-2">
                  <input
                    type="password"
                    value={hfToken}
                    onChange={(e) => updateToken(e.target.value)}
                    placeholder="hf_..."
                    className="flex-1 px-3 py-2 text-xs font-mono rounded-lg border focus:outline-none focus:ring-1"
                    style={{
                      borderColor: THEME.bgDark,
                      backgroundColor: THEME.white,
                    }}
                  />
                  <span className="text-xs text-gray-400 self-center">
                    For higher rate limits
                  </span>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </AppGridBackground>
  );
};

import { useAnalysisContext } from "../App";
import { THEME } from "../constants";
import {
  AppGridBackground,
  ErrorMessageBox,
  useMountedTransition,
} from "./SharedUI";

export const LoadingPage = () => {
  const { progress, progressMessage, error, reset, status } =
    useAnalysisContext();
  const mounted = useMountedTransition();

  const progressClamped = Math.min(100, Math.max(0, progress));
  const isError = status === "error";

  return (
    <AppGridBackground className="min-h-screen flex items-center justify-center p-8">
      <div
        className={`max-w-md w-full backdrop-blur-sm rounded-2xl border shadow-xl transition-all duration-700 transform ${
          mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
        }`}
        style={{
          backgroundColor: `${THEME.white}F2`,
          borderColor: THEME.bgGrid,
        }}
      >
        {/* Top accent bar */}
        <div
          className="h-1 w-full rounded-t-2xl transition-colors duration-300"
          style={{
            backgroundColor: isError ? THEME.errorRed : THEME.accent,
          }}
        />

        <div className="p-8 space-y-8">
          {/* Icon */}
          <div className="flex justify-center">
            {isError ? (
              <div
                className="w-20 h-20 rounded-full flex items-center justify-center border"
                style={{
                  backgroundColor: `${THEME.errorRed}1A`,
                  borderColor: `${THEME.errorRed}33`,
                }}
              >
                <svg
                  className="w-10 h-10"
                  style={{ color: THEME.errorRed }}
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  strokeWidth={2}
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z"
                  />
                </svg>
              </div>
            ) : (
              <div className="relative">
                <div
                  className="w-20 h-20 border-4 rounded-full animate-spin"
                  style={{
                    borderColor: THEME.bgDark,
                    borderTopColor: THEME.accent,
                  }}
                />
                <div className="absolute inset-0 flex items-center justify-center">
                  <div
                    className="w-2 h-2 rounded-full animate-pulse"
                    style={{ backgroundColor: THEME.accent }}
                  />
                </div>
              </div>
            )}
          </div>

          {/* Heading */}
          <div className="text-center space-y-2">
            <h2
              className="text-2xl font-bold tracking-tight"
              style={{ color: THEME.textBlack }}
            >
              {isError ? "Analysis Failed" : "Analyzing Story"}
            </h2>
            <p className="text-sm text-gray-500 font-mono uppercase tracking-widest">
              {isError ? "Something went wrong" : progressMessage}
            </p>
          </div>

          {/* Progress bar */}
          {!isError && (
            <div className="space-y-4">
              <div className="flex justify-between text-xs font-mono font-bold text-gray-500">
                <span>PROGRESS</span>
                <span>{Math.round(progressClamped)}%</span>
              </div>
              <div
                className="w-full rounded-full h-4 overflow-hidden border"
                style={{
                  backgroundColor: `${THEME.bgDark}80`,
                  borderColor: THEME.bgDark,
                }}
              >
                <div
                  className="h-full progress-stripe transition-all duration-500 ease-out rounded-full"
                  style={{
                    width: `${progressClamped}%`,
                    backgroundColor: THEME.accent,
                  }}
                />
              </div>
              <div
                className="border p-3 rounded-lg"
                style={{
                  backgroundColor: THEME.white,
                  borderColor: THEME.bgGrid,
                }}
              >
                <div className="flex items-center space-x-2">
                  <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                  <p className="font-mono text-xs text-gray-600 truncate">
                    {`> ${progressMessage}`}
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Error state */}
          {isError && error && (
            <div className="space-y-4">
              <ErrorMessageBox
                className="border p-4 rounded-lg"
                message={error}
              />
              <button
                onClick={reset}
                className="w-full py-3 text-white font-bold transition-colors shadow-lg cursor-pointer rounded-xl border-none"
                style={{ backgroundColor: THEME.textBlack }}
                onMouseEnter={(e) =>
                  (e.currentTarget.style.backgroundColor = THEME.black)
                }
                onMouseLeave={(e) =>
                  (e.currentTarget.style.backgroundColor = THEME.textBlack)
                }
              >
                TRY AGAIN
              </button>
            </div>
          )}
        </div>
      </div>
    </AppGridBackground>
  );
};

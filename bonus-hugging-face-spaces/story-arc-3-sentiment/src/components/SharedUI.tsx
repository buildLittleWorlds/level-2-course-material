import {
  useEffect,
  useState,
  type CSSProperties,
  type ReactNode,
} from "react";
import { THEME } from "../constants";

/* ── Grid background ──────────────────────────────────────── */

const GRID_STYLE: CSSProperties = {
  backgroundColor: THEME.bgLight,
  backgroundImage: `
    linear-gradient(${THEME.bgGrid} 1px, transparent 1px),
    linear-gradient(90deg, ${THEME.bgGrid} 1px, transparent 1px)
  `,
  backgroundSize: "40px 40px",
};

export const AppGridBackground = ({
  children,
  className,
  style,
}: {
  children: ReactNode;
  className: string;
  style?: CSSProperties;
}) => (
  <div className={className} style={{ ...GRID_STYLE, ...style }}>
    {children}
  </div>
);

/* ── Mount transition hook ────────────────────────────────── */

export const useMountedTransition = () => {
  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
  }, []);
  return mounted;
};

/* ── Status dot (pinging) ─────────────────────────────────── */

export const StatusDot = ({
  color = THEME.accent,
  label = "System Ready",
}: {
  color?: string;
  label?: string;
}) => (
  <div className="group cursor-help z-10">
    <span className="absolute right-full mr-4 top-1/2 -translate-y-1/2 whitespace-nowrap text-xs font-mono uppercase tracking-widest text-gray-500 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-x-2 group-hover:translate-x-0 pointer-events-none">
      {label}
    </span>
    <div className="relative flex h-3 w-3">
      <span
        className="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75"
        style={{ backgroundColor: color }}
      />
      <span
        className="relative inline-flex rounded-full h-3 w-3"
        style={{ backgroundColor: color }}
      />
    </div>
  </div>
);

/* ── Document icon ────────────────────────────────────────── */

export const DocumentIcon = ({
  className,
  strokeWidth = 1.5,
  style,
}: {
  className: string;
  strokeWidth?: number;
  style?: CSSProperties;
}) => (
  <svg
    className={className}
    style={style}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={strokeWidth}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"
    />
  </svg>
);

/* ── Chart icon ───────────────────────────────────────────── */

export const ChartIcon = ({
  className,
  style,
}: {
  className: string;
  style?: CSSProperties;
}) => (
  <svg
    className={className}
    style={style}
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={1.5}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
    />
  </svg>
);

/* ── Error box ────────────────────────────────────────────── */

export const ErrorMessageBox = ({
  message,
  className,
}: {
  message: string;
  className?: string;
}) => (
  <div
    className={className}
    style={{
      backgroundColor: `${THEME.errorRed}0D`,
      borderColor: `${THEME.errorRed}33`,
    }}
  >
    <p
      className="font-mono text-xs break-words"
      style={{ color: THEME.errorRed }}
    >
      {`> Error: ${message}`}
    </p>
  </div>
);

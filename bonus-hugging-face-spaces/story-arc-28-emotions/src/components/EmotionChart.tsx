import { useMemo, useState, useRef } from "react";
import { EMOTIONS } from "../constants";
import type { ParagraphResult } from "../types";

const SVG_WIDTH = 700;
const SVG_HEIGHT = 280;
const PAD_LEFT = 50;
const PAD_RIGHT = 30;
const PAD_TOP = 30;
const PAD_BOTTOM = 40;
const PLOT_W = SVG_WIDTH - PAD_LEFT - PAD_RIGHT;
const PLOT_H = SVG_HEIGHT - PAD_TOP - PAD_BOTTOM;

interface Props {
  paragraphs: ParagraphResult[];
  highlightedEmotion: string | null;
  highlightedParagraph: number | null;
  visibleEmotions: Set<string>;
  onHoverEmotion: (emotion: string | null) => void;
  onHoverParagraph: (index: number | null) => void;
}

/**
 * Catmull-Rom to cubic bezier conversion for smooth curves.
 * Given 4 points, returns 2 cubic bezier control points for the middle segment.
 */
function catmullRomToBezier(
  p0: [number, number],
  p1: [number, number],
  p2: [number, number],
  p3: [number, number],
  tension = 0.3,
): [[number, number], [number, number]] {
  const cp1x = p1[0] + ((p2[0] - p0[0]) * tension) / 3;
  const cp1y = p1[1] + ((p2[1] - p0[1]) * tension) / 3;
  const cp2x = p2[0] - ((p3[0] - p1[0]) * tension) / 3;
  const cp2y = p2[1] - ((p3[1] - p1[1]) * tension) / 3;
  return [
    [cp1x, cp1y],
    [cp2x, cp2y],
  ];
}

function buildSmoothPath(points: [number, number][]): string {
  if (points.length < 2) return "";
  if (points.length === 2) {
    return `M ${points[0][0]},${points[0][1]} L ${points[1][0]},${points[1][1]}`;
  }

  let d = `M ${points[0][0]},${points[0][1]}`;

  for (let i = 0; i < points.length - 1; i++) {
    const p0 = points[Math.max(0, i - 1)];
    const p1 = points[i];
    const p2 = points[i + 1];
    const p3 = points[Math.min(points.length - 1, i + 2)];

    const [cp1, cp2] = catmullRomToBezier(p0, p1, p2, p3);
    d += ` C ${cp1[0].toFixed(1)},${cp1[1].toFixed(1)} ${cp2[0].toFixed(1)},${cp2[1].toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)}`;
  }

  return d;
}

function xPos(index: number, total: number): number {
  return PAD_LEFT + (index / Math.max(total - 1, 1)) * PLOT_W;
}

function yPos(score: number): number {
  return PAD_TOP + (1 - score / 100) * PLOT_H;
}

export const EmotionChart = ({
  paragraphs,
  highlightedEmotion,
  highlightedParagraph,
  visibleEmotions,
  onHoverEmotion,
  onHoverParagraph,
}: Props) => {
  const svgRef = useRef<SVGSVGElement>(null);
  const [tooltip, setTooltip] = useState<{
    x: number;
    y: number;
    text: string;
  } | null>(null);

  const n = paragraphs.length;

  // Compute paths and dots
  const emotionPaths = useMemo(() => {
    return EMOTIONS.map((emotion) => {
      const points: [number, number][] = paragraphs.map((p, i) => [
        xPos(i, n),
        yPos(p.scores[emotion.label] ?? 0),
      ]);
      return {
        label: emotion.label,
        color: emotion.color,
        path: buildSmoothPath(points),
        points,
      };
    });
  }, [paragraphs, n]);

  // Grid lines
  const gridLines = useMemo(() => {
    const lines: { y: number; label: string }[] = [];
    for (const pct of [0, 25, 50, 75, 100]) {
      lines.push({ y: yPos(pct), label: `${pct}%` });
    }
    return lines;
  }, []);

  const handleDotEnter = (
    emotion: string,
    paraIndex: number,
    score: number,
    cx: number,
    cy: number,
  ) => {
    onHoverEmotion(emotion);
    onHoverParagraph(paraIndex);
    // Convert SVG coordinates to container coordinates
    if (svgRef.current) {
      const rect = svgRef.current.getBoundingClientRect();
      const scaleX = rect.width / SVG_WIDTH;
      const scaleY = rect.height / SVG_HEIGHT;
      setTooltip({
        x: cx * scaleX,
        y: cy * scaleY,
        text: `P${paraIndex} · ${emotion}: ${score}%`,
      });
    }
  };

  const handleDotLeave = () => {
    onHoverEmotion(null);
    onHoverParagraph(null);
    setTooltip(null);
  };

  return (
    <div className="relative">
      <svg
        ref={svgRef}
        viewBox={`0 0 ${SVG_WIDTH} ${SVG_HEIGHT}`}
        className="w-full"
        style={{ maxHeight: 340 }}
      >
        {/* Background */}
        <rect
          x={PAD_LEFT}
          y={PAD_TOP}
          width={PLOT_W}
          height={PLOT_H}
          fill="white"
          fillOpacity={0.5}
          rx={4}
        />

        {/* Horizontal grid */}
        {gridLines.map((g) => (
          <g key={g.label}>
            <line
              x1={PAD_LEFT}
              y1={g.y}
              x2={PAD_LEFT + PLOT_W}
              y2={g.y}
              stroke="#E2E8F0"
              strokeWidth={1}
              strokeDasharray="4 4"
            />
            <text
              x={PAD_LEFT - 8}
              y={g.y + 4}
              textAnchor="end"
              fontSize={10}
              fill="#94A3B8"
              fontFamily="monospace"
            >
              {g.label}
            </text>
          </g>
        ))}

        {/* Vertical paragraph markers */}
        {paragraphs.map((_, i) => {
          const x = xPos(i, n);
          return (
            <g key={i}>
              <line
                x1={x}
                y1={PAD_TOP}
                x2={x}
                y2={PAD_TOP + PLOT_H}
                stroke="#E2E8F0"
                strokeWidth={1}
                strokeDasharray="2 4"
              />
              <text
                x={x}
                y={SVG_HEIGHT - 10}
                textAnchor="middle"
                fontSize={11}
                fill="#94A3B8"
                fontFamily="monospace"
              >
                P{i + 1}
              </text>
            </g>
          );
        })}

        {/* Emotion paths */}
        {emotionPaths.map((ep) => {
          if (!visibleEmotions.has(ep.label)) return null;
          const isHighlighted =
            !highlightedEmotion || highlightedEmotion === ep.label;
          const className = highlightedEmotion
            ? isHighlighted
              ? "arc-line highlight"
              : "arc-line dimmed"
            : "arc-line";

          return (
            <path
              key={ep.label}
              d={ep.path}
              fill="none"
              stroke={ep.color}
              strokeWidth={2.5}
              opacity={0.8}
              className={className}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          );
        })}

        {/* Dots */}
        {emotionPaths.map((ep) => {
          if (!visibleEmotions.has(ep.label)) return null;
          return ep.points.map(([cx, cy], i) => {
            const score = paragraphs[i].scores[ep.label] ?? 0;
            const isEmotionMatch =
              !highlightedEmotion || highlightedEmotion === ep.label;
            const isParaMatch =
              !highlightedParagraph || highlightedParagraph === i + 1;
            const isDimmed = highlightedEmotion && !isEmotionMatch;
            const isActive =
              highlightedParagraph === i + 1 && isEmotionMatch;

            return (
              <circle
                key={`${ep.label}-${i}`}
                cx={cx}
                cy={cy}
                r={isActive ? 6 : highlightedParagraph && isParaMatch && isEmotionMatch ? 5 : 3.5}
                fill={ep.color}
                opacity={isDimmed ? 0.08 : 0.9}
                className={
                  isDimmed ? "arc-dot dimmed" : "arc-dot"
                }
                style={{ cursor: "pointer" }}
                onMouseEnter={() =>
                  handleDotEnter(ep.label, i + 1, score, cx, cy)
                }
                onMouseLeave={handleDotLeave}
              />
            );
          });
        })}
      </svg>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="chart-tooltip"
          style={{ left: tooltip.x, top: tooltip.y }}
        >
          {tooltip.text}
        </div>
      )}
    </div>
  );
};

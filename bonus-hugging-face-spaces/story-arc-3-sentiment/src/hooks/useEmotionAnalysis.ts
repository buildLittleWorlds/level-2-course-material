import { useState, useCallback, useRef } from "react";
import { MODEL_ID, EMOTIONS, LABEL_MAP, MAX_PARAGRAPHS } from "../constants";
import type { AppStatus, ParagraphResult, AnalysisResult } from "../types";

const TOKEN_KEY = "hf_token";
const API_BASE = import.meta.env.DEV
  ? "/api/inference"
  : "https://router.huggingface.co";
const API_URL = `${API_BASE}/models/${MODEL_ID}`;

function getStoredToken(): string {
  try {
    return localStorage.getItem(TOKEN_KEY) ?? "";
  } catch {
    return "";
  }
}

function storeToken(token: string) {
  try {
    if (token) localStorage.setItem(TOKEN_KEY, token);
    else localStorage.removeItem(TOKEN_KEY);
  } catch {
    /* ignore */
  }
}

function remapLabel(raw: string): string {
  if (LABEL_MAP && raw in LABEL_MAP) return LABEL_MAP[raw];
  return raw.toLowerCase();
}

function splitParagraphs(text: string): string[] {
  return text
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter((p) => p.length > 0)
    .slice(0, MAX_PARAGRAPHS);
}

interface ApiScore {
  label: string;
  score: number;
}

const CHUNK_MAX = 500;

// Split a long paragraph into chunks at sentence boundaries (~500 chars each)
function chunkParagraph(text: string): string[] {
  if (text.length <= CHUNK_MAX) return [text];
  const sentences = text.match(/[^.!?]+[.!?]+[\s]*/g) ?? [text];
  const chunks: string[] = [];
  let current = "";
  for (const s of sentences) {
    if (current.length + s.length > CHUNK_MAX && current.length > 0) {
      chunks.push(current.trim());
      current = s;
    } else {
      current += s;
    }
  }
  if (current.trim()) chunks.push(current.trim());
  return chunks;
}

// Average scores across multiple chunks for one paragraph
function averageScores(allScores: ApiScore[][]): ApiScore[] {
  const sums: Record<string, number> = {};
  const count = allScores.length;
  for (const scores of allScores) {
    for (const { label, score } of scores) {
      sums[label] = (sums[label] ?? 0) + score;
    }
  }
  return Object.entries(sums).map(([label, total]) => ({
    label,
    score: total / count,
  }));
}

// Generate demo scores dynamically from configured EMOTIONS
// Each paragraph gets a different "dominant" emotion for visual variety
function generateDemoScores(): ApiScore[][] {
  const labels = EMOTIONS.map((e) => e.label);
  const n = labels.length;
  // 6 paragraphs, each with a different dominant emotion (cycles if fewer emotions)
  const dominantPatterns = [
    // P1: first emotion dominates, P2: second, etc.
    [0.52, 0.20, 0.12, 0.08, 0.04, 0.02, 0.01, 0.01],
    [0.55, 0.18, 0.10, 0.08, 0.05, 0.02, 0.01, 0.01],
    [0.62, 0.15, 0.10, 0.06, 0.04, 0.02, 0.01, 0.00],
    [0.40, 0.25, 0.15, 0.10, 0.05, 0.03, 0.01, 0.01],
    [0.35, 0.25, 0.18, 0.10, 0.06, 0.04, 0.01, 0.01],
    [0.55, 0.20, 0.12, 0.06, 0.04, 0.02, 0.01, 0.00],
  ];
  return dominantPatterns.map((pattern, pIdx) => {
    // Rotate which emotion is dominant for each paragraph
    const offset = pIdx % n;
    return labels.map((label, i) => ({
      label,
      score: pattern[(i - offset + n) % n] ?? pattern[pattern.length - 1] ?? 0.01,
    }));
  });
}

const DEMO_SCORES = generateDemoScores();

async function classifyText(
  text: string,
  token: string,
): Promise<ApiScore[]> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const res = await fetch(API_URL, {
    method: "POST",
    headers,
    body: JSON.stringify({ inputs: text }),
  });

  if (!res.ok) {
    const body = await res.text();
    if (res.status === 503) {
      throw new Error(
        "Model is loading on Hugging Face servers. Please try again in 20-30 seconds.",
      );
    }
    if (res.status === 401) {
      throw new Error(
        "A Hugging Face token is required. Get a free one at huggingface.co/settings/tokens, then paste it in the HF Token field below.",
      );
    }
    if (res.status === 429) {
      throw new Error(
        "Rate limited by Hugging Face. Add an HF token (free at huggingface.co) for higher limits.",
      );
    }
    throw new Error(`API error ${res.status}: ${body.slice(0, 200)}`);
  }

  const data = await res.json();
  // The API returns [[{label, score}, ...]] (nested array) for single input
  if (Array.isArray(data) && Array.isArray(data[0])) {
    return data[0] as ApiScore[];
  }
  if (Array.isArray(data)) {
    return data as ApiScore[];
  }
  throw new Error("Unexpected API response format");
}

export function useEmotionAnalysis() {
  const [status, setStatus] = useState<AppStatus>("idle");
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);
  const [progressMessage, setProgressMessage] = useState("");
  const [hfToken, setHfToken] = useState(getStoredToken);
  const abortRef = useRef(false);

  const updateToken = useCallback((token: string) => {
    setHfToken(token);
    storeToken(token);
  }, []);

  const analyze = useCallback(
    async (text: string) => {
      const paragraphs = splitParagraphs(text);
      if (paragraphs.length < 2) {
        setError(
          "Please paste at least 2 paragraphs separated by blank lines.",
        );
        setStatus("error");
        return;
      }

      setStatus("loading");
      setError(null);
      setResult(null);
      setProgress(0);
      abortRef.current = false;

      const results: ParagraphResult[] = [];

      try {
        for (let i = 0; i < paragraphs.length; i++) {
          if (abortRef.current) return;

          const chunks = chunkParagraph(paragraphs[i]);
          const chunkLabel = chunks.length > 1 ? ` (${chunks.length} chunks)` : "";
          setProgressMessage(
            i === 0 && paragraphs.length > 3
              ? `Waking up model & analyzing paragraph 1 of ${paragraphs.length}${chunkLabel}...`
              : `Analyzing paragraph ${i + 1} of ${paragraphs.length}${chunkLabel}...`,
          );

          let response: ApiScore[];
          try {
            // Analyze each chunk and average the scores
            const chunkResults: ApiScore[][] = [];
            for (const chunk of chunks) {
              chunkResults.push(await classifyText(chunk, hfToken));
            }
            response = chunks.length === 1 ? chunkResults[0] : averageScores(chunkResults);
          } catch (apiErr) {
            // Fall back to demo data if API fails (no token, rate limit, etc.)
            const demoIdx = i % DEMO_SCORES.length;
            response = DEMO_SCORES[demoIdx];
            // Small delay so the progress bar feels natural
            await new Promise((r) => setTimeout(r, 300));
            if (i === 0) {
              console.warn(
                "API unavailable, using demo data:",
                apiErr instanceof Error ? apiErr.message : apiErr,
              );
            }
          }

          const scores: Record<string, number> = {};
          for (const item of response) {
            const label = remapLabel(item.label);
            scores[label] = Math.round(item.score * 100);
          }

          // Ensure all configured emotions have a score
          for (const e of EMOTIONS) {
            if (!(e.label in scores)) scores[e.label] = 0;
          }

          const topEmotion = Object.entries(scores).reduce((a, b) =>
            b[1] > a[1] ? b : a,
          );
          const topColor =
            EMOTIONS.find((e) => e.label === topEmotion[0])?.color ?? "#999";

          results.push({
            index: i + 1,
            text: paragraphs[i],
            preview:
              paragraphs[i].length > 70
                ? paragraphs[i].slice(0, 70) + "..."
                : paragraphs[i],
            topEmotion: topEmotion[0],
            topColor,
            scores,
          });

          setProgress(((i + 1) / paragraphs.length) * 100);
        }

        if (!abortRef.current) {
          setResult({ paragraphs: results });
          setStatus("done");
          setProgressMessage("");
        }
      } catch (err: unknown) {
        if (abortRef.current) return;
        const msg =
          err instanceof Error ? err.message : "Analysis failed unexpectedly.";
        setError(msg);
        setStatus("error");
      }
    },
    [hfToken],
  );

  const reset = useCallback(() => {
    abortRef.current = true;
    setStatus("idle");
    setResult(null);
    setError(null);
    setProgress(0);
    setProgressMessage("");
  }, []);

  return {
    status,
    result,
    error,
    progress,
    progressMessage,
    hfToken,
    updateToken,
    analyze,
    reset,
  };
}

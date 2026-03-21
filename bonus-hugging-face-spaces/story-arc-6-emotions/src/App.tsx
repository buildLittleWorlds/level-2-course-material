import { createContext, useContext } from "react";
import { useEmotionAnalysis } from "./hooks/useEmotionAnalysis";
import { LandingPage } from "./components/LandingPage";
import { LoadingPage } from "./components/LoadingPage";
import { ResultsPage } from "./components/ResultsPage";

type AnalysisContextType = ReturnType<typeof useEmotionAnalysis>;

const AnalysisContext = createContext<AnalysisContextType | null>(null);

export function useAnalysisContext(): AnalysisContextType {
  const ctx = useContext(AnalysisContext);
  if (!ctx) throw new Error("useAnalysisContext must be used within App");
  return ctx;
}

const PAGE_BY_STATUS = {
  idle: LandingPage,
  loading: LoadingPage,
  done: ResultsPage,
  error: LoadingPage,
} as const;

const AppContent = () => {
  const analysis = useAnalysisContext();
  const Page = PAGE_BY_STATUS[analysis.status];
  return <Page />;
};

const App = () => {
  const analysis = useEmotionAnalysis();

  return (
    <AnalysisContext.Provider value={analysis}>
      <AppContent />
    </AnalysisContext.Provider>
  );
};

export default App;

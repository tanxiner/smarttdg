import * as React from "react";
import { useState } from "react";
import { Navigation } from "./components/Navigation";
import { HomePage } from "./components/HomePage";
import { AboutPage } from "./components/AboutPage";
import { FAQPage } from "./components/FAQPage";
import { HowToPage } from "./components/HowToPage";
import { DownloadPage } from "./components/DownloadPage";

export default function App() {
  const [currentPage, setCurrentPage] = useState("home");
  const [showDownloadPage, setShowDownloadPage] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<any>(null);

  const handleDocumentationReady = (result?: any) => {
    setAnalysisResult(result ?? null);
    setShowDownloadPage(true);
  };

  const handleStartOver = () => {
    setShowDownloadPage(false);
    setCurrentPage("home");
    setAnalysisResult(null);
  };

  const handlePageChange = (page: string) => {
    setShowDownloadPage(false);
    setCurrentPage(page);
  };

  const handleShowDownloadDemo = () => {
    setShowDownloadPage(true);
    setCurrentPage("download");
  };

  const renderPage = () => {
    if (showDownloadPage) {
      return <DownloadPage onStartOver={handleStartOver} analysis={analysisResult} />;
    }

    switch (currentPage) {
      case "about":
        return <AboutPage />;
      case "faq":
        return <FAQPage />;
      case "howto":
        return <HowToPage />;
      default:
        return <HomePage onDocumentationReady={handleDocumentationReady} />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Navigation 
        currentPage={currentPage} 
        onPageChange={handlePageChange}
        onShowDownload={handleShowDownloadDemo}
      />
      <main className="py-8 px-4 sm:px-6 lg:px-8">
        {renderPage()}
      </main>
    </div>
  );
}
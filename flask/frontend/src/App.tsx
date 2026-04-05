import * as React from "react";
import { useEffect, useState } from "react";
import { Navigation } from "./components/Navigation";
import { HomePage } from "./components/HomePage";
import { AboutPage } from "./components/AboutPage";
import { FAQPage } from "./components/FAQPage";
import { HowToPage } from "./components/HowToPage";
import { DownloadPage } from "./components/DownloadPage";

const STORAGE_KEYS = {
    currentPage: "smarttdg_current_page",
    showDownloadPage: "smarttdg_show_download_page",
    analysisResult: "smarttdg_analysis_result",
};

export default function App() {
    const [currentPage, setCurrentPage] = useState("home");
    const [showDownloadPage, setShowDownloadPage] = useState(false);
    const [analysisResult, setAnalysisResult] = useState<any>(null);
    const [isHydrated, setIsHydrated] = useState(false);

    useEffect(() => {
        try {
            const savedCurrentPage = sessionStorage.getItem(STORAGE_KEYS.currentPage);
            const savedShowDownloadPage = sessionStorage.getItem(STORAGE_KEYS.showDownloadPage);
            const savedAnalysisResult = sessionStorage.getItem(STORAGE_KEYS.analysisResult);

            if (savedCurrentPage) {
                setCurrentPage(savedCurrentPage);
            }

            if (savedShowDownloadPage === "true") {
                setShowDownloadPage(true);
            }

            if (savedAnalysisResult) {
                setAnalysisResult(JSON.parse(savedAnalysisResult));
            }
        } catch (e) {
            console.warn("Failed to restore app state:", e);
            sessionStorage.removeItem(STORAGE_KEYS.currentPage);
            sessionStorage.removeItem(STORAGE_KEYS.showDownloadPage);
            sessionStorage.removeItem(STORAGE_KEYS.analysisResult);
        } finally {
            setIsHydrated(true);
        }
    }, []);

    useEffect(() => {
        if (!isHydrated) return;
        sessionStorage.setItem(STORAGE_KEYS.currentPage, currentPage);
    }, [currentPage, isHydrated]);

    useEffect(() => {
        if (!isHydrated) return;
        sessionStorage.setItem(
            STORAGE_KEYS.showDownloadPage,
            String(showDownloadPage)
        );
    }, [showDownloadPage, isHydrated]);

    useEffect(() => {
        if (!isHydrated) return;

        if (analysisResult != null) {
            sessionStorage.setItem(
                STORAGE_KEYS.analysisResult,
                JSON.stringify(analysisResult)
            );
        } else {
            sessionStorage.removeItem(STORAGE_KEYS.analysisResult);
        }
    }, [analysisResult, isHydrated]);

    const handleDocumentationReady = (result?: any) => {
        const safeResult = result ?? null;
        setAnalysisResult(safeResult);
        setShowDownloadPage(true);
        setCurrentPage("download");
    };

    const handleStartOver = () => {
        setShowDownloadPage(false);
        setCurrentPage("home");
        setAnalysisResult(null);

        sessionStorage.removeItem(STORAGE_KEYS.showDownloadPage);
        sessionStorage.removeItem(STORAGE_KEYS.analysisResult);
        sessionStorage.setItem(STORAGE_KEYS.currentPage, "home");
    };

    const handlePageChange = (page: string) => {
        setShowDownloadPage(false);
        setCurrentPage(page);

        if (page !== "download") {
            sessionStorage.setItem(STORAGE_KEYS.showDownloadPage, "false");
        }
    };

    const handleShowDownloadDemo = () => {
        setShowDownloadPage(true);
        setCurrentPage("download");
    };

    const renderPage = () => {
        if (showDownloadPage) {
            return (
                <DownloadPage
                    onStartOver={handleStartOver}
                    analysis={analysisResult}
                />
            );
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

    if (!isHydrated) {
        return null;
    }

    return (
        <div className="min-h-screen bg-gray-50">
            <Navigation
                currentPage={currentPage}
                onPageChange={handlePageChange}
                onShowDownload={handleShowDownloadDemo}
            />
            <main className="py-8 px-4 sm:px-6 lg:px-8">{renderPage()}</main>
        </div>
    );
}
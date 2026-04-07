import { FileUploadZone } from "./FileUploadZone";
import { Zap, BarChart3 } from "lucide-react";
import * as React from "react";
import DiagramViewer from "./DiagramViewer";

interface HomePageProps {
    onDocumentationReady?: (result?: any) => void;
}

export function HomePage({ onDocumentationReady }: HomePageProps) {
    const [selectedModel, setSelectedModel] = React.useState<string>("gemma3:latest");
    const [activeTab, setActiveTab] = React.useState<"upload" | "diagrams">("upload");

    // Treat both processing and canceling as "busy" from the parent's perspective
    const [isBusy, setIsBusy] = React.useState<boolean>(false);

    const MODELS = [
        "gemma3:latest",
        "gemma3n:latest",
        "gemma4:e2b",
        "gemma4:latest",
        "qwen3:latest",
        "gpt-oss:latest",
    ].sort();

    return (
        <div className="space-y-8">
            <div className="text-center py-6 mb-4">
                <h1 className="text-4xl font-medium text-gray-900 mb-0">
                    SmartTDG: AI-Powered Technical Document Generator
                </h1>
            </div>

            <div className="flex justify-center mb-8">
                <div className="flex bg-gray-100 rounded-lg p-1">
                    <button
                        onClick={() => setActiveTab("upload")}
                        className={`px-6 py-2 rounded-md flex items-center gap-2 transition-colors ${activeTab === "upload"
                                ? "bg-white text-blue-600 shadow-sm"
                                : "text-gray-600 hover:text-gray-900"
                            }`}
                    >
                        <Zap size={16} />
                        Generate Documentation
                    </button>

                    <button
                        onClick={() => setActiveTab("diagrams")}
                        className={`px-6 py-2 rounded-md flex items-center gap-2 transition-colors ${activeTab === "diagrams"
                                ? "bg-white text-blue-600 shadow-sm"
                                : "text-gray-600 hover:text-gray-900"
                            }`}
                    >
                        <BarChart3 size={16} />
                        View Diagrams
                    </button>
                </div>
            </div>

            {activeTab === "upload" ? (
                <section>
                    <div className="text-center mb-6">
                        <h2 className="text-2xl font-medium text-gray-900 mb-2">Get Started</h2>
                        <p className="text-gray-600">
                            Upload your project ZIP file to begin generating technical documentation
                        </p>
                    </div>

                    <div className="flex items-center justify-center mb-2">
                        <label className="mr-3 text-sm font-medium text-gray-700">Model: </label>
                        <select
                            value={selectedModel}
                            onChange={(e) => setSelectedModel(e.target.value)}
                            className="border rounded px-3 py-1"
                            aria-label="Select analysis model"
                            disabled={isBusy}
                        >
                            {MODELS.map((m) => (
                                <option key={m} value={m}>
                                    {m}
                                </option>
                            ))}
                        </select>
                    </div>

                    <FileUploadZone
                        onDocumentationReady={onDocumentationReady}
                        selectedModel={selectedModel}
                        onProcessingChanged={(busy) => setIsBusy(busy)}
                    />
                </section>
            ) : (
                <section>
                    <div className="text-center mb-6">
                        <h2 className="text-2xl font-medium text-gray-900 mb-2">Diagrams Generation</h2>
                            <p className="text-gray-600">Upload your project ZIP file to view and generate diagrams from source code</p>
                    </div>
                    <DiagramViewer />
                </section>
            )}
        </div>
    );
}
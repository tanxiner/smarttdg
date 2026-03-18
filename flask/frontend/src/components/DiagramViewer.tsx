import React, { useState, useEffect, useRef, useCallback } from "react";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Upload, FileArchive, BarChart3, X, Loader2, CheckCircle, Code, Eye, Download, ChevronRight, ZoomIn, ZoomOut, RotateCcw,} from "lucide-react";
import { Progress } from "./ui/progress";
import mermaid from "mermaid"; // Import directly for offline use

interface DiagramInfo {
    type: string;
    filename: string;
    path: string;
    size?: number;
}

interface DiagramsResponse {
    diagrams: DiagramInfo[];
}

// --- Mermaid Rendering Component (Offline Capable) ---
interface MermaidRendererProps {
    chart: string;
    onSvgRendered?: (svg: string) => void;
}

const MermaidRenderer: React.FC<MermaidRendererProps> = ({
    chart,
    onSvgRendered,
}) => {
    const containerRef = useRef<HTMLDivElement>(null);
    const [svg, setSvg] = useState<string>("");
    const [renderError, setRenderError] = useState<string>("");
    const [scale, setScale] = useState<number>(1);
    // Initialize to true if chart exists to prevent flash of empty state before effect runs
    const [isRendering, setIsRendering] = useState<boolean>(!!chart);

    useEffect(() => {
        mermaid.initialize({
            startOnLoad: false,
            theme: "default",
            securityLevel: "loose",
        });
    }, []);

    useEffect(() => {
        let mounted = true;

        const renderChart = async () => {
            // 1. Prepare clean content first
            const cleanChart = extractMermaid(chart);

            // Option C: hard guardrail to avoid Mermaid "max text size exceeded" + tab lockups
            const MAX_RENDER_CHARS = 250_000;
            if (cleanChart.length > MAX_RENDER_CHARS) {
                if (mounted) {
                    setSvg("");
                    setRenderError(
                        `Diagram too large to render (${cleanChart.length.toLocaleString()} chars). ` +
                        `Try regenerating diagrams; output may be truncated for safety.`
                    );
                    setIsRendering(false);
                }
                return;
            }

            // 2. Check for empty string
            if (!cleanChart) {
                if (mounted) {
                    setSvg("");
                    setRenderError("");
                    setIsRendering(false);
                }
                return;
            }

            // 3. Heuristic: Check if chart contains only definitions/styles but no data
            const isSkeletonOnly = () => {
                const lines = cleanChart
                    .split("\n")
                    .map((l) => l.trim())
                    .filter((l) => l);
                const meaningfulLines = lines.filter((l) => {
                    // Ignore comments
                    if (l.startsWith("%%")) return false;
                    // Ignore style definitions
                    if (l.startsWith("classDef")) return false;
                    // Ignore diagram type declarations
                    if (/^(graph|flowchart)\s+[A-Za-z0-9]+$/.test(l)) return false;
                    if (l === "classDiagram") return false;
                    if (l === "erDiagram") return false;
                    return true;
                });
                return meaningfulLines.length === 0;
            };

            if (isSkeletonOnly()) {
                if (mounted) {
                    setSvg("");
                    setRenderError("");
                    setIsRendering(false);
                }
                return;
            }

            // 4. Content exists, start rendering state
            if (mounted) setIsRendering(true);

            try {
                const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
                const { svg } = await mermaid.render(id, cleanChart);

                if (mounted) {
                    // Check if SVG is effectively empty (mermaid sometimes returns empty SVG for empty graph)
                    if (!svg || svg.length < 50) {
                        setSvg("");
                    } else {
                        setSvg(svg);
                        setScale(1); // Reset zoom on new chart
                        if (onSvgRendered) onSvgRendered(svg);
                    }
                    setRenderError("");
                }
            } catch (err) {
                console.error("Mermaid rendering error:", err);

                const msg =
                    err instanceof Error ? err.message || String(err) : String(err);

                if (mounted) {
                    if (/maximum text size/i.test(msg)) {
                        setRenderError(
                            "Diagram too large to render (Mermaid maximum text size exceeded)."
                        );
                    } else {
                        // ✅ show the real parser error
                        setRenderError(msg);
                    }
                    setSvg("");
                }
            } finally {
                if (mounted) setIsRendering(false);
            }
        };

        renderChart();

        return () => {
            mounted = false;
        };
    }, [chart, onSvgRendered]);

    if (renderError) {
        return (
            <div
                className="flex items-center justify-center p-8 text-red-500 bg-red-50 rounded-lg border border-red-100 h-full"
                style={{ minHeight: "500px" }}
            >
                <p className="font-semibold text-sm">Render Error: {renderError}</p>
            </div>
        );
    }

    return (
        <div className="flex flex-col h-full w-full border rounded-lg bg-white relative min-h-[400px] min-h-0">            {/* Zoom Controls Toolbar */}
            <div className="flex items-center justify-end p-2 gap-2 bg-gray-50 border-b z-20">
                <span className="text-xs text-gray-500 font-medium uppercase tracking-wide mr-2">
                    Zoom
                </span>

                <Button
                    variant="outline"
                    size="sm"
                    className="h-8 w-8 p-0"
                    onClick={() => setScale((s) => Math.max(0.25, s - 0.25))}
                    title="Zoom Out"
                    disabled={!svg}
                >
                    <ZoomOut className="h-4 w-4" />
                </Button>

                <span className="text-sm font-medium w-12 text-center text-gray-700">
                    {Math.round(scale * 100)}%
                </span>

                <Button
                    variant="outline"
                    size="sm"
                    className="h-8 w-8 p-0"
                    onClick={() => setScale((s) => Math.min(5, s + 0.25))}
                    title="Zoom In"
                    disabled={!svg}
                >
                    <ZoomIn className="h-4 w-4" />
                </Button>

                <div className="w-px h-4 bg-gray-300 mx-1" />

                <Button
                    variant="outline"
                    size="sm"
                    className="h-8 px-2 text-xs"
                    onClick={() => setScale(1)}
                    title="Reset Zoom"
                    disabled={!svg}
                >
                    <RotateCcw className="h-3 w-3 mr-1" />
                    Reset
                </Button>
            </div>

            {/* Scrollable Container */}
            <div className="flex-1 overflow-auto p-4 bg-gray-50/30 relative min-h-[450px]">
                {/* Loading Indicator */}
                {isRendering && (
                    <div className="absolute inset-0 flex flex-col items-center justify-center bg-white/80 z-10 backdrop-blur-sm">
                        <Loader2 className="h-10 w-10 animate-spin text-primary mb-3" />
                        <p className="text-gray-600 font-medium animate-pulse">
                            Rendering diagram...
                        </p>
                    </div>
                )}

                {/* Empty Indicator */}
                {!isRendering && !svg && (
                    <div className="absolute inset-0 flex flex-col items-center justify-center text-gray-400">
                        <BarChart3 className="h-16 w-16 mb-4 opacity-20" />
                        <p className="text-gray-500 font-medium">
                            No diagram content generated.
                        </p>
                        <p className="text-xs text-gray-400 mt-1">
                            Try analyzing a different set of files.
                        </p>
                    </div>
                )}

                <div
                    ref={containerRef}
                    className="mermaid-output flex items-start justify-center origin-top-left transition-all duration-200 ease-in-out"
                    style={{
                        width: scale === 1 ? "100%" : `${scale * 100}%`,
                        minWidth: "100%",
                        opacity: isRendering ? 0 : 1,
                    }}
                    dangerouslySetInnerHTML={{ __html: svg }}
                />
            </div>
        </div>
    );
};

function extractMermaid(chart: string): string {
    if (!chart) return "";

    // Prefer fenced mermaid blocks
    const fenced = chart.match(/```mermaid\s*([\s\S]*?)```/i);
    if (fenced?.[1]) return fenced[1].trim();

    // Fallback: old behavior (in case backend returns raw mermaid)
    return chart.replace(/```mermaid/gi, "").replace(/```/g, "").trim();
}

const DiagramViewer: React.FC = () => {
    const [diagrams, setDiagrams] = useState<DiagramInfo[]>([]);
    const [selectedDiagram, setSelectedDiagram] = useState<string | null>(null);
    const [diagramContent, setDiagramContent] = useState<string>("");
    const [currentSvg, setCurrentSvg] = useState<string>("");
    const [loading, setLoading] = useState(false);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState<string>("");
    const [uploadProgress, setUploadProgress] = useState<number>(0);
    const [analysisStatus, setAnalysisStatus] = useState<string>("");
    const [showCode, setShowCode] = useState(false);

    // File upload states
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [dragOver, setDragOver] = useState(false);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const [currentJobId, setCurrentJobId] = useState<string | null>(null);

    const pollHandleRef = useRef<number | null>(null);
    const runTokenRef = useRef(0);
    const activeJobIdRef = useRef<string | null>(null);

    const clearPollTimer = useCallback(() => {
        if (pollHandleRef.current != null) {
            window.clearInterval(pollHandleRef.current);
            pollHandleRef.current = null;
        }
    }, []);

    // Clear diagrams function
    const clearDiagrams = useCallback(async () => {
        try {
            await fetch("/diagrams", { method: "DELETE" });
            setDiagrams([]);
            setSelectedDiagram(null);
            setDiagramContent("");
            setCurrentSvg("");
        } catch (error) {
            console.error("Error clearing diagrams:", error);
        }
    }, []);

    const loadDiagramContent = async (diagramPath: string) => {
        setLoading(true);
        setError("");
        setShowCode(false);
        setCurrentSvg(""); // Clear previous SVG while loading
        try {
            const response = await fetch(`/${diagramPath}`);
            if (response.ok) {
                const content = await response.text();
                setDiagramContent(content);
            } else {
                const errorText = `Failed to load diagram content (${response.status})`;
                setDiagramContent(errorText);
                setError(errorText);
            }
        } catch (error) {
            const errorText = "Error loading diagram content";
            setDiagramContent(errorText);
            setError(errorText);
        } finally {
            setLoading(false);
        }
    };

    const handleDiagramSelect = useCallback(
        (diagram: DiagramInfo) => {
            setSelectedDiagram(diagram.type);
            loadDiagramContent(diagram.path);
        },
        [] // loadDiagramContent is stable enough for our usage
    );

    const loadDiagrams = useCallback(async () => {
        try {
            setError("");
            const response = await fetch("/diagrams");
            if (response.ok) {
                const data: DiagramsResponse = await response.json();
                setDiagrams(data.diagrams);
                if (data.diagrams.length > 0 && !selectedDiagram) {
                    handleDiagramSelect(data.diagrams[0]);
                }
            } else {
                const errorData = await response
                    .json()
                    .catch(() => ({ error: "Unknown error" }));
                setError(`Failed to load diagrams: ${errorData.error}`);
            }
        } catch (error) {
            console.error("Error loading diagrams:", error);
            setError("Error loading diagrams. Make sure the backend is running.");
        }
    }, [handleDiagramSelect, selectedDiagram]);

    const uploadAndGenerateDiagrams = useCallback(
        async (file: File) => {
            await clearDiagrams();

            runTokenRef.current += 1;
            const myRunToken = runTokenRef.current;
            clearPollTimer();

            setUploading(true);
            setError("");
            setUploadProgress(0);
            setAnalysisStatus("Uploading file...");

            try {
                const formData = new FormData();
                formData.append("file", file);

                const response = await fetch("/upload_for_diagrams", {
                    method: "POST",
                    body: formData,
                });

                if (!response.ok) throw new Error(`Upload failed: ${response.statusText}`);

                const { jobId } = await response.json();
                setCurrentJobId(jobId);
                activeJobIdRef.current = jobId;

                setAnalysisStatus("Starting...");
                setUploadProgress(0);

                pollHandleRef.current = window.setInterval(async () => {
                    if (runTokenRef.current !== myRunToken) return;
                    if (activeJobIdRef.current !== jobId) return;

                    try {
                        const sres = await fetch(`/diagram_status/${jobId}`);
                        if (sres.status === 404) {
                            clearPollTimer();
                            setAnalysisStatus("Job not found or expired.");
                            setUploadProgress(0);
                            setUploading(false);
                            setCurrentJobId(null);
                            activeJobIdRef.current = null;
                            return;
                        }
                        if (!sres.ok) throw new Error(`Status ${sres.status}`);

                        const st = await sres.json();

                        // terminal states
                        if (st.step === "error") {
                            clearPollTimer();
                            setError(st.error || "Diagram generation failed");
                            setUploading(false);
                            setCurrentJobId(null);
                            activeJobIdRef.current = null;
                            return;
                        }

                        if (
                            st.step === "cancel_requested" ||
                            st.step === "canceled" ||
                            st.canceled
                        ) {
                            clearPollTimer();
                            setAnalysisStatus("Canceled");
                            setUploadProgress(0);
                            setUploading(false);
                            setCurrentJobId(null);
                            activeJobIdRef.current = null;
                            return;
                        }

                        // done
                        if (st.step === "done") {
                            clearPollTimer();
                            setAnalysisStatus("Diagram generation complete!");
                            setUploadProgress(100);
                            await loadDiagrams();
                            setUploading(false);
                            setSelectedFile(null);
                            setCurrentJobId(null);
                            activeJobIdRef.current = null;
                            return;
                        }

                        // progress updates
                        setUploadProgress(typeof st.progress === "number" ? st.progress : 0);
                        setAnalysisStatus(st.step || "Processing...");
                    } catch (e) {
                        console.warn("Polling error", e);
                    }
                }, 1000);
            } catch (error) {
                console.error("Upload error:", error);
                setError(`Upload failed: ${error}`);
                setUploading(false);
                setCurrentJobId(null);
                activeJobIdRef.current = null;
            }
        },
        [clearDiagrams, clearPollTimer, loadDiagrams]
    );

    const handleFileSelect = (file: File) => {
        if (!file.name.toLowerCase().endsWith(".zip")) {
            setError("Please select a ZIP file");
            return;
        }
        setSelectedFile(file);
        setError("");
    };

    const handleDragOver = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(true);
    };

    const handleDragLeave = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(false);
    };

    const handleDrop = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(false);

        const files = Array.from(e.dataTransfer.files);
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    };

    const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;
        if (files && files.length > 0) {
            handleFileSelect(files[0]);
        }
    };

    const startDiagramGeneration = async () => {
        if (!selectedFile) return;
        await uploadAndGenerateDiagrams(selectedFile);
    };

    const formatDiagramType = (type: string) => {
        return type
            .split("_")
            .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
            .join(" ");
    };

    const openFileDialog = () => {
        fileInputRef.current?.click();
    };

    const downloadSvg = async () => {
        if (!selectedDiagram) return;

        try {
            const response = await fetch(`/diagrams/${selectedDiagram}/svg`);
            if (!response.ok) {
                const msg = await response.text().catch(() => "");
                throw new Error(msg || "Server-side SVG generation failed");
            }

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            const link = document.createElement("a");
            link.href = url;
            link.download = `${selectedDiagram}.svg`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

            URL.revokeObjectURL(url);
        } catch (e) {
            // optional fallback: if server export fails but you have currentSvg, download it
            if (currentSvg) {
                const blob = new Blob([currentSvg], { type: "image/svg+xml;charset=utf-8" });
                const url = URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.href = url;
                link.download = `${selectedDiagram}.svg`;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                URL.revokeObjectURL(url);
                return;
            }

            setError(`Failed to download SVG: ${String(e)}`);
        }
    };

    const cancelJob = useCallback(
        async (jobId: string | null) => {
            if (!jobId) return;
            try {
                await fetch(`/diagram_cancel/${jobId}`, { method: "POST" });
            } catch (e) {
                console.warn("Cancel request failed", e);
            } finally {
                clearPollTimer();
                setAnalysisStatus("Canceled");
                setUploadProgress(0);
                setUploading(false);
                setCurrentJobId(null);
                activeJobIdRef.current = null;
            }
        },
        [clearPollTimer]
    );

    useEffect(() => {
        // clear on mount (matches your current behavior)
        clearDiagrams();
        return () => {
            runTokenRef.current += 1;
            clearPollTimer();
        };
    }, [clearDiagrams, clearPollTimer]);

    return (
        <div className="space-y-8 animate-in fade-in duration-500">
            {/* Upload Zone */}
            <div className="max-w-2xl mx-auto">
                {uploading ? (
                    <Card className="p-8 text-center">
                        <div className="mb-6">
                            {uploadProgress < 100 ? (
                                <Loader2 className="mx-auto h-12 w-12 text-primary animate-spin mb-4" />
                            ) : (
                                <CheckCircle className="mx-auto h-12 w-12 text-green-500 mb-4" />
                            )}
                            <h3 className="text-lg font-medium text-gray-900 mb-2">
                                {uploadProgress < 100 ? "Processing" : "Diagrams Ready!"}
                            </h3>
                            <p className="text-gray-600 mb-2">{analysisStatus}</p>
                        </div>

                        <div className="mb-6">
                            <div className="flex items-center justify-between text-sm text-gray-600 mb-2">
                                <span>Progress</span>
                                <span>{uploadProgress}%</span>
                            </div>
                            <Progress value={uploadProgress} className="h-3" />
                        </div>

                        {currentJobId && (
                            <div className="flex items-center justify-center space-x-1 mt-1">
                                <Button
                                    variant="destructive"
                                    onClick={async () => {
                                        setAnalysisStatus("Canceling...");
                                        await cancelJob(currentJobId);
                                    }}
                                >
                                    Cancel
                                </Button>
                            </div>
                        )}
                    </Card>
                ) : !selectedFile ? (
                    <Card
                        className={`border-2 border-dashed p-8 text-center transition-colors ${dragOver ? "border-primary bg-primary/5" : "border-gray-300"
                            }`}
                        onDragOver={handleDragOver}
                        onDragLeave={handleDragLeave}
                        onDrop={handleDrop}
                    >
                        <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
                        <h3 className="text-lg font-medium text-gray-900 mb-2">
                            Upload your project files
                        </h3>
                        <p className="text-gray-600 mb-4">
                            Drag and drop a ZIP file containing your project, or click to browse
                        </p>

                        <input
                            ref={fileInputRef}
                            type="file"
                            accept=".zip"
                            onChange={handleFileInputChange}
                            className="hidden"
                        />

                        <Button
                            variant="outline"
                            className="cursor-pointer"
                            onClick={openFileDialog}
                        >
                            Choose ZIP File
                        </Button>

                        <p className="text-sm text-gray-500 mt-2">
                            Only ZIP files are supported
                        </p>
                    </Card>
                ) : (
                    <Card className="p-6">
                        <div className="flex items-center justify-between mb-4">
                            <div className="flex items-center space-x-3">
                                <FileArchive className="h-8 w-8 text-primary" />
                                <div>
                                    <h4 className="font-medium">{selectedFile.name}</h4>
                                    <p className="text-sm text-gray-500">
                                        {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                                    </p>
                                </div>
                            </div>
                            <Button
                                variant="ghost"
                                size="sm"
                                onClick={() => setSelectedFile(null)}
                            >
                                <X className="h-4 w-4" />
                            </Button>
                        </div>

                        <Button onClick={startDiagramGeneration} className="w-full">
                            Generate Diagrams
                        </Button>
                    </Card>
                )}

                {/* Error Message */}
                {error && (
                    <div className="mt-4 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
                        <p className="font-medium">Error:</p>
                        <p>{error}</p>
                    </div>
                )}

                {/* Success indicator */}
                {!uploading && uploadProgress === 100 && (
                    <div className="mt-4 p-3 rounded-md bg-green-50 border border-green-100 text-green-700 text-sm flex items-center gap-2">
                        <CheckCircle className="h-4 w-4" />
                        Diagrams generated successfully.
                    </div>
                )}
            </div>

            {/* Viewer Layout */}
            {diagrams.length > 0 && (
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 bg-gray-50/50 p-6 rounded-xl border">
                    {/* Sidebar */}
                    <div className="lg:col-span-3">
                        <Card className="h-full shadow-sm border-gray-200 overflow-hidden">
                            <div className="p-4 border-b bg-gray-50/50">
                                <h3 className="font-semibold text-gray-900 flex items-center gap-2">
                                    <BarChart3 className="h-4 w-4" />
                                    Diagrams
                                </h3>
                            </div>
                            <div className="p-2 space-y-1">
                                {diagrams.map((diagram) => (
                                    <button
                                        key={diagram.type}
                                        onClick={() => handleDiagramSelect(diagram)}
                                        className={`w-full text-left px-3 py-2.5 rounded-md text-sm transition-all flex items-center justify-between group ${selectedDiagram === diagram.type
                                                ? "bg-primary/10 text-primary font-medium"
                                                : "text-gray-600 hover:bg-gray-100"
                                            }`}
                                    >
                                        <span>{formatDiagramType(diagram.type)}</span>
                                        {selectedDiagram === diagram.type && (
                                            <ChevronRight className="h-4 w-4 opacity-50" />
                                        )}
                                    </button>
                                ))}
                            </div>
                        </Card>
                    </div>

                    {/* Main Viewer */}
                    <div className="lg:col-span-9">
                        <Card className="h-full shadow-sm border-gray-200 flex flex-col min-h-[400px]">
                            {selectedDiagram ? (
                                <>
                                    {/* Header Toolbar */}
                                    <div className="p-4 border-b flex flex-row justify-between items-center gap-4 bg-white rounded-t-xl sticky top-0 z-10">
                                        <h3 className="text-lg font-semibold text-gray-900 whitespace-nowrap overflow-hidden text-ellipsis">
                                            {formatDiagramType(selectedDiagram)}
                                        </h3>

                                        <div className="flex items-center gap-2 shrink-0">
                                            <Button
                                                variant="outline"
                                                size="sm"
                                                className="gap-2 h-9"
                                                onClick={downloadSvg}
                                                disabled={!selectedDiagram || showCode}
                                            >
                                                <Download className="h-4 w-4" />
                                                <span className="hidden sm:inline">SVG</span>
                                            </Button>

                                            <div className="h-4 w-px bg-gray-200 mx-1 hidden sm:block"></div>

                                            <Button
                                                variant="outline"
                                                size="sm"
                                                className="gap-2 h-9"
                                                onClick={() => setShowCode(!showCode)}
                                            >
                                                {showCode ? (
                                                    <Eye className="h-4 w-4" />
                                                ) : (
                                                    <Code className="h-4 w-4" />
                                                )}
                                                <span className="hidden sm:inline">
                                                    {showCode ? "View" : "Code"}
                                                </span>
                                            </Button>
                                        </div>
                                    </div>

                                    {/* Canvas */}
                                    <div className="flex-1 bg-white overflow-hidden flex flex-col min-h-0">
                                        {loading ? (
                                            <div className="h-full flex flex-col items-center justify-center text-gray-400 p-8">
                                                <Loader2 className="h-8 w-8 animate-spin mb-3 text-primary" />
                                                <p>Rendering diagram...</p>
                                            </div>
                                        ) : showCode ? (
                                            <pre className="text-sm text-gray-700 font-mono bg-gray-50 p-4 m-4 rounded-lg border border-gray-100 overflow-auto flex-1">
                                                {diagramContent}
                                            </pre>
                                        ) : (
                                            <MermaidRenderer
                                                chart={diagramContent}
                                                onSvgRendered={setCurrentSvg}
                                            />
                                        )}
                                    </div>
                                </>
                            ) : (
                                <div className="h-full flex flex-col items-center justify-center text-gray-400 p-8 min-h-[400px]">
                                    <div className="bg-gray-100 p-4 rounded-full mb-4">
                                        <BarChart3 className="h-8 w-8 text-gray-400" />
                                    </div>

                                    <p className="font-medium text-gray-600">No Diagram Selected</p>
                                    <p className="text-sm mt-1">
                                        Choose a diagram from the sidebar to visualize it.
                                    </p>
                                </div>
                            )}
                        </Card>
                    </div>
                </div>
            )}
        </div>
    );
};

export default DiagramViewer;
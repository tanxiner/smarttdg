import React, { useState, useEffect, useRef } from 'react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Upload, FileArchive, BarChart3, PlayCircle, X, Loader2, CheckCircle, Code, Eye, Download, ChevronRight } from 'lucide-react';
import { Progress } from './ui/progress';
import mermaid from 'mermaid'; // Import directly for offline use

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

const MermaidRenderer: React.FC<MermaidRendererProps> = ({ chart, onSvgRendered }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [svg, setSvg] = useState<string>('');
  const [renderError, setRenderError] = useState<string>('');

  useEffect(() => {
    mermaid.initialize({ 
      startOnLoad: false, 
      theme: 'default',
      securityLevel: 'loose', 
    });
  }, []);

  useEffect(() => {
    const renderChart = async () => {
      if (!chart) return;
      
      try {
        const cleanChart = chart.replace(/```mermaid/g, '').replace(/```/g, '').trim();
        const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
        const { svg } = await mermaid.render(id, cleanChart);
        setSvg(svg);
        setRenderError('');
        if (onSvgRendered) onSvgRendered(svg);
      } catch (err) {
        console.error("Mermaid rendering error:", err);
        setRenderError('Failed to render diagram. Code syntax might be invalid.');
        setSvg('');
      }
    };

    renderChart();
  }, [chart, onSvgRendered]);

  if (renderError) {
    return (
      <div className="flex items-center justify-center p-8 text-red-500 bg-red-50 rounded-lg border border-red-100">
        <p className="font-semibold text-sm">Render Error: {renderError}</p>
      </div>
    );
  }

  // Improved container: centering and auto-scaling
  return (
    <div 
      ref={containerRef} 
      className="mermaid-output flex items-start justify-center min-h-[500px] w-full p-4 overflow-auto bg-white"
      dangerouslySetInnerHTML={{ __html: svg }} 
    />
  );
};

const DiagramViewer: React.FC = () => {
  const [diagrams, setDiagrams] = useState<DiagramInfo[]>([]);
  const [selectedDiagram, setSelectedDiagram] = useState<string | null>(null);
  const [diagramContent, setDiagramContent] = useState<string>('');
  const [currentSvg, setCurrentSvg] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string>('');
  const [uploadProgress, setUploadProgress] = useState<number>(0);
  const [analysisStatus, setAnalysisStatus] = useState<string>('');
  const [showCode, setShowCode] = useState(false);

  // File upload states
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [dragOver, setDragOver] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Clear diagrams function
  const clearDiagrams = async () => {
    try {
      await fetch('/diagrams', { method: 'DELETE' });
      setDiagrams([]);
      setSelectedDiagram(null);
      setDiagramContent('');
      setCurrentSvg('');
    } catch (error) {
      console.error('Error clearing diagrams:', error);
    }
  };

  const loadDiagrams = async () => {
    try {
      setError('');
      const response = await fetch('/diagrams');
      if (response.ok) {
        const data: DiagramsResponse = await response.json();
        setDiagrams(data.diagrams);
        if (data.diagrams.length > 0 && !selectedDiagram) {
           handleDiagramSelect(data.diagrams[0]);
        }
      } else {
        const errorData = await response.json().catch(() => ({ error: 'Unknown error' }));
        setError(`Failed to load diagrams: ${errorData.error}`);
      }
    } catch (error) {
      console.error('Error loading diagrams:', error);
      setError('Error loading diagrams. Make sure the backend is running.');
    }
  };

  const uploadAndGenerateDiagrams = async (file: File) => {
    setUploading(true);
    setError('');
    setUploadProgress(0);
    setAnalysisStatus('Uploading file...');

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('/upload_for_diagrams', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Upload failed: ${response.statusText}`);
      }

      const { jobId } = await response.json();
      await pollDiagramJobStatus(jobId);
      
    } catch (error) {
      console.error('Upload error:', error);
      setError(`Upload failed: ${error}`);
      setUploading(false);
    }
  };

  const pollDiagramJobStatus = async (jobId: string) => {
    const pollInterval = 1000;
    const maxAttempts = 180;
    let attempts = 0;

    const poll = async () => {
      try {
        const response = await fetch(`/diagram_status/${jobId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch job status');
        }

        const status = await response.json();
        setUploadProgress(status.progress || 0);
        setAnalysisStatus(status.step || 'Processing...');

        if (status.step === 'done') {
          setAnalysisStatus('Diagram generation complete!');
          setUploadProgress(100);
          await loadDiagrams();
          setUploading(false);
          setSelectedFile(null);
          return;
        } else if (status.step === 'error') {
          throw new Error(status.error || 'Diagram generation failed');
        }

        attempts++;
        if (attempts >= maxAttempts) {
          throw new Error('Diagram generation timed out');
        }

        setTimeout(poll, pollInterval);

      } catch (error) {
        setError(`Diagram generation failed: ${error}`);
        setUploading(false);
      }
    };

    poll();
  };

  const handleFileSelect = (file: File) => {
    if (!file.name.toLowerCase().endsWith('.zip')) {
      setError('Please select a ZIP file');
      return;
    }
    setSelectedFile(file);
    setError('');
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

  const loadDiagramContent = async (diagramPath: string) => {
    setLoading(true);
    setError('');
    setShowCode(false);
    setCurrentSvg(''); // Clear previous SVG while loading
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
      const errorText = 'Error loading diagram content';
      setDiagramContent(errorText);
      setError(errorText);
    } finally {
      setLoading(false);
    }
  };

  const handleDiagramSelect = (diagram: DiagramInfo) => {
    setSelectedDiagram(diagram.type);
    loadDiagramContent(diagram.path);
  };

  const formatDiagramType = (type: string) => {
    return type.split('_').map(word => 
      word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
  };

  const openFileDialog = () => {
    fileInputRef.current?.click();
  };

  const downloadSvg = () => {
    if (!currentSvg || !selectedDiagram) return;
    const blob = new Blob([currentSvg], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${selectedDiagram}.svg`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  useEffect(() => {
    clearDiagrams();
  }, []);

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
          </Card>
        ) : !selectedFile ? (
          <Card
            className={`border-2 border-dashed p-8 text-center transition-colors ${
              dragOver ? "border-primary bg-primary/5" : "border-gray-300"
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
              Drag and drop a ZIP file to generate diagrams
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

            <p className="text-sm text-gray-500 mt-2">Only ZIP files are supported</p>
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
              <Button variant="ghost" size="sm" onClick={() => setSelectedFile(null)}>
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
                {diagrams.map(diagram => (
                  <button
                    key={diagram.type}
                    onClick={() => handleDiagramSelect(diagram)}
                    className={`w-full text-left px-3 py-2.5 rounded-md text-sm transition-all flex items-center justify-between group ${
                      selectedDiagram === diagram.type
                        ? 'bg-primary/10 text-primary font-medium'
                        : 'text-gray-600 hover:bg-gray-100'
                    }`}
                  >
                    <span>{formatDiagramType(diagram.type)}</span>
                    {selectedDiagram === diagram.type && <ChevronRight className="h-4 w-4 opacity-50" />}
                  </button>
                ))}
              </div>
            </Card>
          </div>

          {/* Main Viewer */}
          <div className="lg:col-span-9">
            <Card className="h-full shadow-sm border-gray-200 flex flex-col min-h-[600px]">
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
                        disabled={!currentSvg || showCode}
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
                        {showCode ? <Eye className="h-4 w-4" /> : <Code className="h-4 w-4" />}
                        <span className="hidden sm:inline">{showCode ? "View" : "Code"}</span>
                      </Button>
                    </div>
                  </div>

                  {/* Canvas */}
                  <div className="flex-1 bg-white p-6 overflow-auto">
                    {loading ? (
                      <div className="h-full flex flex-col items-center justify-center text-gray-400">
                        <Loader2 className="h-8 w-8 animate-spin mb-3 text-primary" />
                        <p>Rendering diagram...</p>
                      </div>
                    ) : showCode ? (
                      <pre className="text-sm text-gray-700 font-mono bg-gray-50 p-4 rounded-lg border border-gray-100 overflow-auto h-full">
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
                <div className="h-full flex flex-col items-center justify-center text-gray-400 p-8">
                  <div className="bg-gray-100 p-4 rounded-full mb-4">
                    <BarChart3 className="h-8 w-8 text-gray-400" />
                  </div>
                  <p className="font-medium text-gray-600">No Diagram Selected</p>
                  <p className="text-sm mt-1">Choose a diagram from the sidebar to visualize it.</p>
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
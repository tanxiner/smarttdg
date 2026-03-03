import { useState, useCallback, useRef, useEffect } from "react";
import { Button } from "./ui/button";
import { Card } from "./ui/card";
import { Progress } from "./ui/progress";
import * as React from "react";
import { Upload, FileArchive, X, Loader2, CheckCircle } from "lucide-react";

interface FileUploadZoneProps {
  onDocumentationReady?: (result?: any) => void;
  selectedModel?: string;
  onProcessingChanged?: (isProcessing: boolean) => void;
}

export function FileUploadZone({ onDocumentationReady, selectedModel, onProcessingChanged }: FileUploadZoneProps) {
  const [isDragOver, setIsDragOver] = useState(false);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingProgress, setProcessingProgress] = useState(0);
  const [processingStep, setProcessingStep] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [expectedChapters, setExpectedChapters] = useState<number>(0);
  const [chaptersGenerated, setChaptersGenerated] = useState<number>(0);
  const [currentJobId, setCurrentJobId] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const modelToUse = selectedModel ?? "gemma3:latest";

  useEffect(() => {
    // Clear any stale job id on mount (prevent polling a non-existent job)
    setCurrentJobId(null);
  }, []);

  // Notify parent when processing state changes
  useEffect(() => {
    onProcessingChanged?.(isProcessing);
  }, [isProcessing, onProcessingChanged]);

  const isZip = (name: string) => name.toLowerCase().endsWith(".zip");

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(true);
  }, []);

  const handleDragLeave = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
  }, []);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);

    const files = Array.from(e.dataTransfer.files);
    const zipFile = files.find((file) => isZip(file.name));

    if (zipFile) {
      setUploadedFile(zipFile);
      setError(null);
    } else {
      setError("Only .zip files are supported.");
    }
  }, []);

  const handleFileSelect = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && isZip(file.name)) {
      setUploadedFile(file);
      setError(null);
    } else if (file) {
      setError("Only .zip files are supported.");
    }
  }, []);

  const openFileDialog = () => {
    fileInputRef.current?.click();
  };

  const removeFile = () => {
    setUploadedFile(null);
    setIsProcessing(false);
    setProcessingProgress(0);
    setProcessingStep("");
    setError(null);
    setExpectedChapters(0);
    setChaptersGenerated(0);
    setCurrentJobId(null);
  };

  // Cancel helper used by Cancel button and navigation handlers
  const cancelJob = async (jobId: string | null) => {
    if (!jobId) return;
    try {
      await fetch(`/cancel/${jobId}`, { method: "POST" });
    } catch (e) {
      console.warn("Cancel request failed", e);
    } finally {
      setProcessingStep("Canceled");
      setProcessingProgress(0);
      setIsProcessing(false);
      setCurrentJobId(null);
    }
  };

  const generateDocs = async () => {
    if (!uploadedFile) return;

    setIsProcessing(true);
    setProcessingProgress(0);
    setProcessingStep("Uploading...");
    setError(null);
    setExpectedChapters(0);
    setChaptersGenerated(0);

    const formData = new FormData();
    formData.append("file", uploadedFile);
    formData.append("model", modelToUse);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/analyze_async");

    let jobId: string | null = null;
    let pollHandle: number | null = null;

    xhr.upload.onprogress = (e: ProgressEvent) => {
      if (e.lengthComputable) {
        const percent = Math.min(60, Math.round((e.loaded / e.total) * 60));
        setProcessingProgress(percent);
        setProcessingStep(`Uploading... ${percent}%`);
      }
    };

    xhr.onerror = () => {
      setError("Network error during upload.");
      setIsProcessing(false);
    };

    xhr.onreadystatechange = () => {
      if (xhr.readyState === 4) {
        if (xhr.status >= 200 && xhr.status < 300) {
          try {
            const resp = JSON.parse(xhr.responseText);
            jobId = resp?.jobId;
            if (jobId) setCurrentJobId(jobId);
          } catch {
            jobId = null;
          }

          if (!jobId) {
            try {
              const r = JSON.parse(xhr.responseText);
              setProcessingStep("Finalizing...");
              setProcessingProgress(100);
              setTimeout(() => onDocumentationReady?.(r), 600);
            } catch {
              setError("Unexpected response from server.");
              setIsProcessing(false);
            }
            return;
          }

          // start polling status
          setProcessingStep("Queued on server...");
          setProcessingProgress(65);

          pollHandle = window.setInterval(async () => {
            try {
              const sres = await fetch(`/status/${jobId}`);
              if (sres.status === 404) {
                // job not found -> stop polling and inform user
                if (pollHandle) clearInterval(pollHandle);
                setProcessingStep("Job not found or expired.");
                setProcessingProgress(0);
                setIsProcessing(false);
                setCurrentJobId(null);
                return;
              }
              if (!sres.ok) {
                throw new Error(`Status ${sres.status}`);
              }
              const st = await sres.json();

              // numeric chapter counters (explicit)
              const expected = typeof st.expected_chapters === "number" ? st.expected_chapters : 0;
              const generated = typeof st.chapters_generated === "number" ? st.chapters_generated : 0;
              setExpectedChapters(expected);
              setChaptersGenerated(generated);

              // Respect cancellation reported by server
              if (st.step === "cancel_requested" || st.step === "canceled" || st.canceled) {
                if (pollHandle) clearInterval(pollHandle);
                setProcessingStep("Canceled");
                setProcessingProgress(0);
                setIsProcessing(false);
                setCurrentJobId(null);
                return;
              }

              if (expected > 0) {
                // If all chapters generated, show "finalizing" and move progress to 99%
                if (generated >= expected) {
                  setProcessingStep(`All chapters generated (${generated}/${expected}) — Finalizing...`);
                  setProcessingProgress(99);
                } else {
                  const remaining = Math.max(0, expected - generated);
                  setProcessingStep(`Generating chapters: ${generated}/${expected} — ${remaining} chapter(s) remaining`);
                  const pct = Math.round((generated / expected) * 100);
                  setProcessingProgress(Math.min(98, Math.max(0, pct)));
                }
              } else {
                // fallback to step text or progress
                if (st.step) setProcessingStep(String(st.step));
                if (typeof st.progress === "number") setProcessingProgress(st.progress);
              }

              // When backend reports final result, finish
              if (st.result && (typeof st.progress === "number" ? st.progress >= 100 : true)) {
                if (pollHandle) {
                  clearInterval(pollHandle);
                }
                setProcessingProgress(100);
                setProcessingStep("Done — preparing results...");
                setTimeout(() => onDocumentationReady?.(st.result), 400);
                setCurrentJobId(null);
                setIsProcessing(false);
              }

              if (st.step === "error") {
                if (pollHandle) clearInterval(pollHandle);
                setError(st.error || "Analysis error");
                setIsProcessing(false);
                setCurrentJobId(null);
              }
            } catch (e) {
              console.warn("Polling error", e);
              // keep polling for transient errors; if you prefer, implement retry/backoff here
            }
          }, 1000);
        } else {
          let msg = "Upload failed.";
          try {
            const j = JSON.parse(xhr.responseText);
            if (j?.error) msg = j.error;
          } catch {
            /* ignore */
          }
          setError(msg);
          setIsProcessing(false);
        }
      }
    };

    xhr.send(formData);
  };

  if (isProcessing) {
    return (
      <div className="max-w-2xl mx-auto">
        <Card className="p-8 text-center">
          <div className="mb-6">
            {processingProgress < 100 ? (
              <Loader2 className="mx-auto h-12 w-12 text-primary animate-spin mb-4" />
            ) : (
              <CheckCircle className="mx-auto h-12 w-12 text-green-500 mb-4" />
            )}
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              {processingProgress < 100 ? "Processing" : "Documentation Ready!"}
            </h3>
            <p className="text-gray-600 mb-2">{processingStep}</p>
          {/*  <p className="text-sm text-gray-500">Model used: <strong>{modelToUse}</strong></p>*/}
          </div>

          <div className="flex items-center justify-center space-x-1 mt-1">
            {currentJobId && (
              <Button
                variant="destructive"
                onClick={async () => {
                  try {
                    setProcessingStep("Canceling...");
                    await cancelJob(currentJobId);
                  } catch (e) {
                    console.warn("Cancel request failed", e);
                  }
                }}
              >
                Cancel
              </Button>
            )}
          </div>

          <div className="mb-6">
            <div className="flex items-center justify-between text-sm text-gray-600 mb-2">
              <span>Progress</span>
              <span>{processingProgress}%</span>
            </div>
            <Progress value={processingProgress} className="h-3" />
          </div>

          <div className="flex items-center justify-center space-x-3 text-sm text-gray-500">
            <FileArchive className="h-4 w-4" />
            <span>{uploadedFile?.name}</span>
            <span>•</span>
            <span>
              {uploadedFile ? (uploadedFile.size / 1024 / 1024).toFixed(2) : 0} MB
            </span>
          </div>

          {error && <p className="text-sm text-red-600 mt-2">{error}</p>}

          {/*{processingProgress < 100 && (*/}
          {/*  <p className="text-xs text-gray-500 mt-2">*/}
          {/*    This usually takes 2-5 minutes depending on project size*/}
          {/*  </p>*/}
          {/*)}*/}
        </Card>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto">
      {!uploadedFile ? (
        <Card
          className={`border-2 border-dashed p-8 text-center transition-colors ${
            isDragOver ? "border-primary bg-primary/5" : "border-gray-300"
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
            onChange={handleFileSelect}
            className="hidden"
          />

          <Button
            variant="outline"
            className="cursor-pointer"
            onClick={() => {
              openFileDialog();
            }}
          >
            Choose ZIP File
          </Button>

          <p className="text-sm text-gray-500 mt-2">Supports ZIP files up to 1GB</p>
          <p className="text-sm text-gray-500 mt-2">Selected model: <strong>{modelToUse}</strong></p>
        </Card>
      ) : (
        <Card className="p-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-3">
              <FileArchive className="h-8 w-8 text-primary" />
              <div>
                <h4 className="font-medium">{uploadedFile.name}</h4>
                <p className="text-sm text-gray-500">
                  {(uploadedFile.size / 1024 / 1024).toFixed(2)} MB
                </p>
              </div>
            </div>
            <Button variant="ghost" size="sm" onClick={removeFile}>
              <X className="h-4 w-4" />
            </Button>
          </div>

          <p className="text-sm text-gray-500 mb-4">
            Model selected: <strong>{modelToUse}</strong>
          </p>

          <Button onClick={generateDocs} className="w-full">
            Generate Documentation
          </Button>
        </Card>
      )}
    </div>
  );
}
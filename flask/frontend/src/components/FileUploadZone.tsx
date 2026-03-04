import { Button } from "./ui/button";
import { Card } from "./ui/card";
import { Progress } from "./ui/progress";
import * as React from "react";
import { Upload, FileArchive, X, Loader2, CheckCircle } from "lucide-react";
import { useCallback, useEffect, useRef, useState } from "react";

interface FileUploadZoneProps {
  onDocumentationReady?: (result?: any) => void;
  selectedModel?: string;
  onProcessingChanged?: (isProcessing: boolean) => void;
}

export function FileUploadZone({
  onDocumentationReady,
  selectedModel,
  onProcessingChanged,
}: FileUploadZoneProps) {
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

  const pollHandleRef = useRef<number | null>(null);
  const runTokenRef = useRef(0);
  const activeJobIdRef = useRef<string | null>(null);

  const clearPollTimer = useCallback(() => {
    if (pollHandleRef.current != null) {
      window.clearInterval(pollHandleRef.current);
      pollHandleRef.current = null;
    }
  }, []);

  useEffect(() => {
    setCurrentJobId(null);
    activeJobIdRef.current = null;

    return () => {
      runTokenRef.current += 1;
      clearPollTimer();
    };
  }, [clearPollTimer]);

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

  const resetUi = useCallback(() => {
    setIsProcessing(false);
    setProcessingProgress(0);
    setProcessingStep("");
    setError(null);
    setExpectedChapters(0);
    setChaptersGenerated(0);
    setCurrentJobId(null);
    activeJobIdRef.current = null;
  }, []);

  const cancelJob = useCallback(
    async (jobId: string | null) => {
      if (!jobId) return;
      try {
        await fetch(`/cancel/${jobId}`, { method: "POST" });
      } catch (e) {
        console.warn("Cancel request failed", e);
      } finally {
        clearPollTimer();
        setProcessingStep("Canceled");
        setProcessingProgress(0);
        setIsProcessing(false);
        setCurrentJobId(null);
        activeJobIdRef.current = null;
      }
    },
    [clearPollTimer]
  );

  const removeFile = useCallback(async () => {
    if (activeJobIdRef.current) {
      await cancelJob(activeJobIdRef.current);
    } else {
      clearPollTimer();
    }

    setUploadedFile(null);
    resetUi();
  }, [cancelJob, clearPollTimer, resetUi]);

  const generateDocs = async () => {
    if (!uploadedFile) return;

    runTokenRef.current += 1;
    const myRunToken = runTokenRef.current;
    clearPollTimer();

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

    xhr.upload.onprogress = (e: ProgressEvent) => {
      if (runTokenRef.current !== myRunToken) return;
      if (e.lengthComputable) {
        const percent = Math.min(60, Math.round((e.loaded / e.total) * 60));
        setProcessingProgress(percent);
        setProcessingStep(`Uploading... ${percent}%`);
      }
    };

    xhr.onerror = () => {
      if (runTokenRef.current !== myRunToken) return;
      setError("Network error during upload.");
      setIsProcessing(false);
    };

    xhr.onreadystatechange = () => {
      if (xhr.readyState !== 4) return;
      if (runTokenRef.current !== myRunToken) return;

      if (xhr.status >= 200 && xhr.status < 300) {
        try {
          const resp = JSON.parse(xhr.responseText);
          jobId = resp?.jobId ?? null;
          if (jobId) {
            setCurrentJobId(jobId);
            activeJobIdRef.current = jobId;
          }
        } catch {
          jobId = null;
        }

        if (!jobId) {
          try {
            const r = JSON.parse(xhr.responseText);
            setProcessingStep("Finalizing...");
            setProcessingProgress(100);
            setTimeout(() => {
              if (runTokenRef.current !== myRunToken) return;
              onDocumentationReady?.(r);
            }, 600);
          } catch {
            setError("Unexpected response from server.");
            setIsProcessing(false);
          }
          return;
        }

        setProcessingStep("Starting...");
        setProcessingProgress(0);

        pollHandleRef.current = window.setInterval(async () => {
          if (runTokenRef.current !== myRunToken) {
            clearPollTimer();
            return;
          }
          if (activeJobIdRef.current !== jobId) {
            clearPollTimer();
            return;
          }

          try {
            const sres = await fetch(`/status/${jobId}`);
            if (sres.status === 404) {
              clearPollTimer();
              setProcessingStep("Job not found or expired.");
              setProcessingProgress(0);
              setIsProcessing(false);
              setCurrentJobId(null);
              activeJobIdRef.current = null;
              return;
            }
            if (!sres.ok) throw new Error(`Status ${sres.status}`);

            const st = await sres.json();

            if (runTokenRef.current !== myRunToken) return;
            if (activeJobIdRef.current !== jobId) return;

            // terminal states first
            if (st.step === "error") {
              clearPollTimer();
              setError(st.error || "Analysis error");
              setIsProcessing(false);
              setCurrentJobId(null);
              activeJobIdRef.current = null;
              return;
            }

            if (st.step === "cancel_requested" || st.step === "canceled" || st.canceled) {
              clearPollTimer();
              setProcessingStep("Canceled");
              setProcessingProgress(0);
              setIsProcessing(false);
              setCurrentJobId(null);
              activeJobIdRef.current = null;
              return;
            }

            if (st.step === "done" && !st.result) {
              clearPollTimer();
              setError("Job finished but no result payload was returned by the server.");
              setIsProcessing(false);
              setCurrentJobId(null);
              activeJobIdRef.current = null;
              return;
            }

            // ✅ COMPLETE: result is the authoritative signal (step/progress may race)
            if (st.result) {
              console.log("[SmartTDG] Job completed; navigating to download page", {
                jobId,
                step: st.step,
                progress: st.progress,
              });

              clearPollTimer();
              setProcessingProgress(100);
              setProcessingStep("Done — preparing results...");

              // ✅ Navigate immediately (don’t gate on activeJobIdRef after you clear it)
              onDocumentationReady?.(st.result);

              // now cleanup
              setCurrentJobId(null);
              activeJobIdRef.current = null;
              setIsProcessing(false);
              return;
            }

            // non-terminal progress updates
            const expected = typeof st.expected_chapters === "number" ? st.expected_chapters : 0;
            const generated = typeof st.chapters_generated === "number" ? st.chapters_generated : 0;
            setExpectedChapters(expected);
            setChaptersGenerated(generated);

            if (expected > 0) {
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
              if (st.step) setProcessingStep(String(st.step));
              if (typeof st.progress === "number") setProcessingProgress(st.progress);
            }
          } catch (e) {
            console.warn("Polling error", e);
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
            <span>{uploadedFile ? (uploadedFile.size / 1024 / 1024).toFixed(2) : 0} MB</span>
          </div>

          {error && <p className="text-sm text-red-600 mt-2">{error}</p>}
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
          <h3 className="text-lg font-medium text-gray-900 mb-2">Upload your project files</h3>
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

          <Button variant="outline" className="cursor-pointer" onClick={openFileDialog}>
            Choose ZIP File
          </Button>

          <p className="text-sm text-gray-500 mt-2">Only ZIP files are supported</p>
          <p className="text-sm text-gray-500 mt-2">
            Selected model: <strong>{modelToUse}</strong>
          </p>
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
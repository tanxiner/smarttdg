import { useState, useCallback, useRef } from "react";
import { Button } from "./ui/button";
import { Card } from "./ui/card";
import { Progress } from "./ui/progress";
import * as React from "react";
import { Upload, FileArchive, X, Loader2, CheckCircle } from "lucide-react";

interface FileUploadZoneProps {
  onDocumentationReady?: (result?: any) => void;
}

export function FileUploadZone({ onDocumentationReady }: FileUploadZoneProps) {
  const [isDragOver, setIsDragOver] = useState(false);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingProgress, setProcessingProgress] = useState(0);
  const [processingStep, setProcessingStep] = useState("");
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

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
  };

  const generateDocs = async () => {
    if (!uploadedFile) return;

    setIsProcessing(true);
    setProcessingProgress(0);
    setProcessingStep("Uploading...");
    setError(null);

    const formData = new FormData();
    formData.append("file", uploadedFile);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/analyze");

    let lastResult: any = null;

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
          setProcessingStep("Analyzing on server...");
          setProcessingProgress(80);

          try {
            lastResult = JSON.parse(xhr.responseText);
            console.log("Analyze result:", lastResult);
          } catch {
            /* ignore */
          }

          setTimeout(() => {
            setProcessingStep("Finalizing...");
            setProcessingProgress(100);
            setTimeout(() => onDocumentationReady?.(lastResult), 800);
          }, 600);
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
            <p className="text-gray-600 mb-6">{processingStep}</p>
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

          {error && <p className="text-sm text-red-600 mt-4">{error}</p>}

          {processingProgress < 100 && (
            <p className="text-xs text-gray-500 mt-4">
              This usually takes 2-5 minutes depending on project size
            </p>
          )}
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
            className="hidden" // use hidden instead of sr-only
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
          <Button onClick={generateDocs} className="w-full">
            Generate Documentation
          </Button>
        </Card>
      )}
    </div>
  );
}
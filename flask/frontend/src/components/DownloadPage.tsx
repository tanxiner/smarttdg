import React from "react";
import { useState, useMemo } from "react";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { Separator } from "./ui/separator";
import { Progress } from "./ui/progress";
import {
  FileText,
  Globe,
  Share2,
  Eye,
  CheckCircle,
  Clock,
  FileArchive,
  Copy,
  ExternalLink,
} from "lucide-react";

interface DownloadPageProps {
  onStartOver: () => void;
  analysis?: any;
}

type Totals = {
  filesProcessed: number;
  classes: number;
  methods: number;
};

function accumulateTotals(analysis?: any): Totals {
  const results = Array.isArray(analysis?.results) ? analysis.results : [];

  let classes = 0;
  let methods = 0;

  for (const r of results) {
    const res = r?.result;
    if (!res) continue;

    // New analyzer shape: { totals: { classes, methods }, ... }
    if (res?.totals && typeof res.totals.classes === "number") {
      classes += res.totals.classes || 0;
      methods += res.totals.methods || 0;
      continue;
    }

    // Legacy analyzer shape: array of classes with Methods array
    if (Array.isArray(res)) {
      classes += res.length;
      methods += res.reduce(
        (sum: number, c: any) => sum + (Array.isArray(c?.Methods) ? c.Methods.length : 0),
        0
      );
      continue;
    }
  }

  const filesProcessed =
    typeof analysis?.filesAnalyzed === "number" ? analysis.filesAnalyzed : results.length;

  return { filesProcessed, classes, methods };
}

function formatDuration(ms: number): string {
  if (!Number.isFinite(ms) || ms < 0) return "—";
  const sec = Math.floor(ms / 1000);
  const msR = ms % 1000;
  if (sec === 0) return `${ms} ms`;
  const minutes = Math.floor(sec / 60);
  const seconds = sec % 60;
  if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  }
  return `${seconds}s`;
}

function formatFileSizeFromMB(sizeMB?: number): string {
  if (typeof sizeMB !== "number" || !Number.isFinite(sizeMB) || sizeMB < 0) return "—";
  if (sizeMB < 1) {
    const kb = sizeMB * 1024;
    return `${kb.toFixed(2)} KB`;
  }
  return `${sizeMB.toFixed(2)} MB`;
}

export function DownloadPage({ onStartOver, analysis }: DownloadPageProps) {
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [isDownloading, setIsDownloading] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);

  const totals = useMemo(() => accumulateTotals(analysis), [analysis]);

  const projectName = analysis?.zipFilename || analysis?.filename || "Uploaded Project";
  const processedAt = new Date().toLocaleString();
  const sizeMB: number | undefined =
    typeof analysis?.sizeMB === "number" ? analysis.sizeMB : undefined;
  const processingMs: number | undefined =
    typeof analysis?.processingMs === "number" ? analysis.processingMs : undefined;

  const handleDownload = async (format: string) => {
    setIsDownloading(true);
    setDownloadProgress(0);

    const interval = setInterval(() => {
      setDownloadProgress((prev) => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsDownloading(false);
          return 100;
        }
        return prev + 10;
      });
    }, 200);

    setTimeout(() => {
      alert(`Downloading ${format} documentation...`);
    }, 2000);
  };

  const shareableLink = "https://docgen.app/shared/abc123def456";

  const copyShareLink = () => {
    navigator.clipboard.writeText(shareableLink);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 2000);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Status Header */}
      <Card className="p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-3">
            <CheckCircle className="h-8 w-8 text-green-500" />
            <div>
              <h1 className="text-2xl font-medium text-gray-900">Documentation Ready!</h1>
              <p className="text-gray-600">
                {analysis?.message ?? "Your documentation has been successfully generated"}
              </p>
            </div>
          </div>
          <Badge variant="secondary" className="bg-green-100 text-green-800">
            <CheckCircle className="h-3 w-3 mr-1" />
            Complete
          </Badge>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          <div className="space-y-1">
            <div className="text-2xl font-medium text-gray-900">{totals.filesProcessed}</div>
            <div className="text-sm text-gray-600">Files Processed</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-medium text-gray-900">{totals.classes}</div>
            <div className="text-sm text-gray-600">Components (Classes)</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-medium text-gray-900">{totals.methods}</div>
            <div className="text-sm text-gray-600">Functions (Methods)</div>
          </div>
          <div className="space-y-1">
            <div className="text-2xl font-medium text-gray-900">
              {Math.max(totals.filesProcessed, 1)}
            </div>
            <div className="text-sm text-gray-600">Doc Pages</div>
          </div>
        </div>
      </Card>

      <div className="max-w-4xl mx-auto space-y-6">
        {/* Download Options */}
        <Card className="p-6">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Download Documentation</h2>

          {isDownloading && (
            <div className="mb-4">
              <div className="flex items-center justify-between text-sm text-gray-600 mb-2">
                <span>Preparing download...</span>
                <span>{downloadProgress}%</span>
              </div>
              <Progress value={downloadProgress} className="h-2" />
            </div>
          )}

          <div className="space-y-3">
            <Button
              onClick={() => handleDownload("HTML")}
              className="w-full justify-start"
              disabled={isDownloading}
            >
              <Globe className="h-4 w-4 mr-2" />
              Word Document
              <span className="ml-auto text-xs text-gray-500">Recommended</span>
            </Button>

            <Button
              onClick={() => handleDownload("PDF")}
              variant="outline"
              className="w-full justify-start"
              disabled={isDownloading}
            >
              <FileText className="h-4 w-4 mr-2" />
              PDF Document
              <span className="ml-auto text-xs text-gray-500">—</span>
            </Button>

            <Button
              onClick={() => handleDownload("Markdown")}
              variant="outline"
              className="w-full justify-start"
              disabled={isDownloading}
            >
              <FileArchive className="h-4 w-4 mr-2" />
              Markdown Document
              <span className="ml-auto text-xs text-gray-500">—</span>
            </Button>
          </div>

          <Separator className="my-4" />
        </Card>
      </div>

      {/* Project Info */}
      <Card className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-medium text-gray-900">Project Details</h2>
          <Badge variant="outline">{projectName}</Badge>
        </div>

        <div className="grid md:grid-cols-3 gap-4 text-sm">
          <div>
            <div className="font-medium text-gray-900 mb-1">Processing Time</div>
            <div className="text-gray-600">
              {typeof processingMs === "number" ? formatDuration(processingMs) : "—"}
            </div>
          </div>
          <div>
            <div className="font-medium text-gray-900 mb-1">File Size</div>
            <div className="text-gray-600">
              {typeof sizeMB === "number" ? formatFileSizeFromMB(sizeMB) : "—"}
            </div>
          </div>
          <div>
            <div className="font-medium text-gray-900 mb-1">Documentation Size</div>
            <div className="text-gray-600">—</div>
          </div>
        </div>

        {analysis && (
          <div className="mt-6">
            <div className="font-medium text-gray-900 mb-2">Analysis Result</div>
            <pre className="bg-gray-50 p-3 rounded text-xs overflow-auto max-h-72">
              {JSON.stringify(analysis, null, 2)}
            </pre>
          </div>
        )}
      </Card>

      {/* Actions */}
      <div className="flex flex-col sm:flex-row gap-3 pt-4">
        <Button onClick={onStartOver} variant="outline" className="flex-1">
          Generate New Documentation
        </Button>
      </div>
    </div>
  );
}
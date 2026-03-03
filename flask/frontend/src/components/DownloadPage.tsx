import React, { useMemo, useState } from "react";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { Separator } from "./ui/separator";
import { Progress } from "./ui/progress";
import {
  FileText,
  Globe,
  CheckCircle,
  FileArchive,
} from "lucide-react";

interface DownloadPageProps {
  onStartOver: () => void;
  analysis?: any;
}

type Totals = {
  filesProcessed: number;
  webChapters: number;     // Final Documentation Chapters (.md)
  sqlChapters: number;     // SQL Documentation Chapters (.md)
  utilityChapters: number; // Utility Documentation Chapters (.md)
};

/**
 * Uses backend-computed .md counts from analysis_output folders.
 * Priority:
 *  1) analysis.computedTotals.{webChapters, sqlChapters, utilityChapters}
 *  2) analysis.totals.{webChapters, sqlChapters, utilityChapters}
 *  3) legacy: analysis.analysis.totals.{classes, methods, others}
 *  4) fallback heuristic (your old logic)
 */
function accumulateTotals(analysis?: any): Totals {
  const results = Array.isArray(analysis?.results) ? analysis.results : [];

  const filesProcessed =
    typeof analysis?.filesAnalyzed === "number"
      ? analysis.filesAnalyzed
      : results.length;

  // 1) BEST: backend already counted .md files in analysis_output folders
  if (analysis?.computedTotals) {
    return {
      filesProcessed,
      webChapters: Number(analysis.computedTotals.webChapters ?? 0),
      sqlChapters: Number(analysis.computedTotals.sqlChapters ?? 0),
      utilityChapters: Number(analysis.computedTotals.utilityChapters ?? 0),
    };
  }

  // 2) NEXT: backend also exposes a clearer totals object
  if (analysis?.totals) {
    return {
      filesProcessed,
      webChapters: Number(analysis.totals.webChapters ?? 0),
      sqlChapters: Number(analysis.totals.sqlChapters ?? 0),
      utilityChapters: Number(analysis.totals.utilityChapters ?? 0),
    };
  }

  // 3) LEGACY SHIM: your app.py also maps computed totals into analysis.totals
  //    but if you ever pass nested objects, this catches older structures.
  const legacyTotals = analysis?.analysis?.totals;
  if (legacyTotals) {
    return {
      filesProcessed,
      webChapters: Number(legacyTotals.classes ?? 0),
      sqlChapters: Number(legacyTotals.methods ?? 0),
      utilityChapters: Number(legacyTotals.others ?? 0),
    };
  }

  // 4) LAST RESORT: derive counts from results array (heuristics)
  let webChapters = 0;
  let sqlChapters = 0;
  let utilityChapters = 0;

  for (const r of results) {
    const filePath = (r?.file || r?.path || "").toString().toLowerCase();
    const res = r?.result ?? r;

    const looksLikePage =
      filePath.endsWith(".aspx") ||
      filePath.endsWith(".html") ||
      filePath.endsWith(".htm") ||
      res?.isAspx ||
      res?.isHtml ||
      res?.kind === "Page" ||
      (res?.types && res.types.some((t: any) => /page/i.test(t.name)));

    if (looksLikePage) {
      webChapters++;
      continue;
    }

    const looksLikeSql =
      filePath.endsWith(".sql") ||
      (Array.isArray(res?.sql) && res.sql.length > 0) ||
      (res?.ir &&
        Array.isArray(res.ir.file_level_sql) &&
        res.ir.file_level_sql.length > 0) ||
      res?.kind === "StoredProcedure";

    if (looksLikeSql) {
      sqlChapters++;
      continue;
    }

    utilityChapters++;
  }

  return { filesProcessed, webChapters, sqlChapters, utilityChapters };
}

function formatDuration(ms: number): string {
  if (!Number.isFinite(ms) || ms < 0) return "—";
  const sec = Math.floor(ms / 1000);
  const msR = ms % 1000;
  if (sec === 0) return `${ msR } ms`;
  const minutes = Math.floor(sec / 60);
  const seconds = sec % 60;
  if (minutes > 0) return `${ minutes }m ${ seconds } s`;
  return `${ seconds } s`;
}

function formatFileSizeFromMB(sizeMB?: number): string {
  if (typeof sizeMB !== "number" || !Number.isFinite(sizeMB) || sizeMB < 0)
    return "—";
  if (sizeMB < 1) {
    const kb = sizeMB * 1024;
    return `${ kb.toFixed(2) } KB`;
  }
  return `${ sizeMB.toFixed(2) } MB`;
}

export function DownloadPage({ onStartOver, analysis }: DownloadPageProps) {
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [isDownloading, setIsDownloading] = useState(false);

  const totals = useMemo(() => accumulateTotals(analysis), [analysis]);

  const projectName = analysis?.zipFilename || analysis?.filename || "Uploaded Project";
  const sizeMB: number | undefined =
    typeof analysis?.sizeMB === "number" ? analysis.sizeMB : undefined;
  const processingMs: number | undefined =
    typeof analysis?.processingMs === "number" ? analysis.processingMs : undefined;

  // Use backend-provided documentation size when available.
  const documentationSizeMB: number | undefined =
    typeof analysis?.documentationSizeMB === "number"
      ? analysis.documentationSizeMB
      : typeof analysis?.documentationSizeBytes === "number"
      ? analysis.documentationSizeBytes / 1024 / 1024
      : undefined;

  const modelUsed =
    analysis?.analysisModel ??
    analysis?.model ??
    analysis?.analysis?.model ??
    "—";

  const handleDownload = async (format: string) => {
    console.log("handleDownload()", format);
    setIsDownloading(true);
    setDownloadProgress(0);

    // Only special-case Markdown (server serves text/markdown attachment)
    if (format === "Markdown") {
      const url = "/download/complete_documentation";

      try {
        const res = await fetch(url, { method: "GET" });

        if (!res.ok) {
          const t = await res.text().catch(() => "");
          console.error("Download failed", res.status, t);
          alert(`Download failed: ${ res.status } `);
          setIsDownloading(false);
          return;
        }

        // Try streaming with progress if Content-Length is present
        const contentLengthHeader = res.headers.get("content-length");
        if (res.body && contentLengthHeader) {
          const total = parseInt(contentLengthHeader, 10);
          const reader = res.body.getReader();
          const chunks: Uint8Array[] = [];
          let received = 0;

          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            if (value) {
              chunks.push(value);
              received += value.length;
              if (total > 0) {
                setDownloadProgress(
                  Math.min(100, Math.floor((received / total) * 100))
                );
              }
            }
          }

          const blob = new Blob(chunks, { type: "text/markdown" });
          const href = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = href;
          a.download = "Complete_Documentation.md";
          document.body.appendChild(a);
          a.click();
          a.remove();
          URL.revokeObjectURL(href);

          setDownloadProgress(100);
          setTimeout(() => setIsDownloading(false), 400);
          return;
        }

        // Fallback: server didn't provide a streamable body or content-length
        const blob = await res.blob();
        const href = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = href;
        a.download = "Complete_Documentation.md";
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(href);

        setDownloadProgress(100);
        setTimeout(() => setIsDownloading(false), 400);
        return;
      } catch (err) {
        console.error("Download error:", err);
        // final fallback: navigate to endpoint
        try {
          window.location.href = url;
        } catch (_) {
          alert("Unable to download file.");
        } finally {
          setIsDownloading(false);
        }
        return;
      }
    }

    // Placeholder behavior for other formats (existing behavior)
    setTimeout(() => {
      alert(`Downloading ${ format } documentation...`);
      setIsDownloading(false);
    }, 2000);
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Status Header */}
      <Card className="p-6">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center space-x-2">
            <CheckCircle className="h-7 w-7 text-green-500" />
            <div>
              <h1 className="text-xl font-medium text-gray-900">
                Documentation Ready!
              </h1>
              <p className="text-sm text-gray-600">
                {analysis?.message ??
                  "Your documentation has been successfully generated"}
              </p>
            </div>
          </div>
          <Badge variant="secondary" className="bg-green-100 text-green-800 text-sm">
            <CheckCircle className="h-3 w-3 mr-1" />
            Complete
          </Badge>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.filesProcessed}
            </div>
            <div className="text-sm text-gray-600">Files Processed</div>
          </div>
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.webChapters}
            </div>
            <div className="text-sm text-gray-600">
              Final Documentation Chapters
            </div>
          </div>
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.sqlChapters}
            </div>
            <div className="text-sm text-gray-600">SQL Documentation Chapters</div>
          </div>
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.utilityChapters}
            </div>
            <div className="text-sm text-gray-600">
              Other Documentation Chapters
            </div>
          </div>
        </div>
      </Card>

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

      </Card>

      {/* Project Info */}
      <Card className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-medium text-gray-900">Project Details</h2>
          <Badge variant="outline" className="text-sm">{projectName}</Badge>
        </div>

        <div className="grid md:grid-cols-4 gap-4 text-sm">
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
            <div className="text-gray-600">
              {typeof documentationSizeMB === "number"
                ? formatFileSizeFromMB(documentationSizeMB)
                : "—"}
            </div>
          </div>
          <div>
            <div className="font-medium text-gray-900 mb-1">Model Used</div>
            <div className="text-gray-600">{modelUsed}</div>
          </div>
        </div>
      </Card>

          {/* Actions */}
          <div className="flex flex-col sm:flex-row gap-3 pt-2">
              <Button
                  onClick={onStartOver}
                  variant="outline"
                  className="flex-1 py-4 h-10 font-medium"
              >
                  Generate New Documentation
              </Button>
          </div>
    </div>
  );
}

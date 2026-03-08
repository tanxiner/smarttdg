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
  apiChapters: number;     // API Documentation Chapters (.md)
};

/**
 * Use only backend-computed .md counts from analysis_output folders.
 * Priority:
 *  1) analysis.computedTotals.{webChapters, sqlChapters, utilityChapters, apiChapters}
 *  2) analysis.totals.{webChapters, sqlChapters, utilityChapters, apiChapters}
 *  3) legacy: analysis.analysis.totals.{classes, methods, others, api}
 *  4) fallback: zero (do not guess by inspecting results)
 */
function accumulateTotals(analysis?: any): Totals {
  const results = Array.isArray(analysis?.results) ? analysis.results : [];

  const filesProcessed =
    typeof analysis?.filesAnalyzed === "number"
      ? analysis.filesAnalyzed
      : results.length;

  const toNumber = (v: any) => {
    const n = Number(v ?? 0);
    return Number.isFinite(n) ? n : 0;
  };

  // 1) BEST: backend already counted .md files in analysis_output folders
  if (analysis?.computedTotals) {
    return {
      filesProcessed,
      webChapters: toNumber(analysis.computedTotals.webChapters),
      sqlChapters: toNumber(analysis.computedTotals.sqlChapters),
      utilityChapters: toNumber(analysis.computedTotals.utilityChapters),
      apiChapters: toNumber(analysis.computedTotals.apiChapters),
    };
  }

  // 2) NEXT: backend also exposes a clearer totals object
  if (analysis?.totals) {
    return {
      filesProcessed,
      webChapters: toNumber(analysis.totals.webChapters),
      sqlChapters: toNumber(analysis.totals.sqlChapters),
      utilityChapters: toNumber(analysis.totals.utilityChapters),
      apiChapters: toNumber(analysis.totals.api ?? analysis.totals.apiChapters),
    };
  }

  // 3) LEGACY SHIM: preserve compatibility with older analyzer shapes
  const legacyTotals = analysis?.analysis?.totals;
  if (legacyTotals) {
    return {
      filesProcessed,
      webChapters: toNumber(legacyTotals.classes),
      sqlChapters: toNumber(legacyTotals.methods),
      utilityChapters: toNumber(legacyTotals.others),
      apiChapters: toNumber(legacyTotals.api),
    };
  }

  // 4) Do not attempt to derive counts client-side anymore.
  return { filesProcessed, webChapters: 0, sqlChapters: 0, utilityChapters: 0, apiChapters: 0 };
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

// Helpers for Content-Disposition parsing and safe filenames
function safeDecodeFilenameStar(raw: string): string {
  try {
    // RFC5987 format: charset'lang'%XX...
    // keep everything after the last single-quote sections (encoded part)
    const firstQuote = raw.indexOf("'");
    if (firstQuote === -1) {
      return decodeURIComponent(raw);
    }
    // parts: charset'lang'encoded
    const parts = raw.split("'");
    const encoded = parts.slice(2).join("'");
    return decodeURIComponent(encoded);
  } catch {
    return raw;
  }
}

function sanitizeFilename(name: string): string {
  const base = name.replace(/.*[\\/]/, "");
  // remove control and reserved characters
  return base.replace(/[\u0000-\u001f<>:"\/\\|?*\x7f]/g, "_").trim();
}

function getFilenameFromResponse(res: Response, defaultName: string) {
  const cd = res.headers.get("content-disposition");
  if (!cd) return defaultName;
  // Try filename* first (RFC5987)
  const mStar = cd.match(/filename\*\s*=\s*([^;]+)/i);
  if (mStar && mStar[1]) {
    let val = mStar[1].trim().replace(/^['"]|['"]$/g, "");
    val = safeDecodeFilenameStar(val);
    return sanitizeFilename(val) || defaultName;
  }
  // Fallback to filename=
  const m = cd.match(/filename\s*=\s*["']?([^;"']+)["']?/i);
  if (m && m[1]) {
    return sanitizeFilename(m[1].trim()) || defaultName;
  }
  return defaultName;
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

  // Consider docs present only when at least one chapter count > 0
  const docsAvailable =
    (totals.webChapters ?? 0) +
    (totals.sqlChapters ?? 0) +
    (totals.utilityChapters ?? 0) +
    (totals.apiChapters ?? 0) > 0;

  // Unified fetch-based downloader used for Markdown, Word and PDF.
  const doFetchDownload = async (url: string, defaultFileName: string) => {
    setIsDownloading(true);
    setDownloadProgress(0);
    try {
      const res = await fetch(url, { method: "GET" });
      if (!res.ok) {
        const t = await res.text().catch(() => "");
        console.error("Download failed", res.status, t);
        alert(`Download failed: ${ res.status }`);
        setIsDownloading(false);
        return;
      }

      const filename = getFilenameFromResponse(res, defaultFileName);

      // Try streaming if content-length is present
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
              setDownloadProgress(Math.min(100, Math.floor((received / total) * 100)));
            }
          }
        }

        const contentType = res.headers.get("content-type") || "application/octet-stream";
        const blob = new Blob(chunks, { type: contentType });
        const href = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = href;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(href);

        setDownloadProgress(100);
        setTimeout(() => setIsDownloading(false), 400);
        return;
      }

      // Fallback: blob()
      const blob = await res.blob();
      const href = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = href;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(href);

      setDownloadProgress(100);
      setTimeout(() => setIsDownloading(false), 400);
      return;
    } catch (err) {
      console.error("Download error:", err);
      // final fallback: navigate to endpoint which will trigger browser download
      try {
        window.location.href = url;
      } catch (_) {
        alert("Unable to download file.");
      } finally {
        setIsDownloading(false);
      }
    }
  };

  const handleDownload = async (format: string) => {
    console.log("handleDownload()", format);

    const safeProject = sanitizeFilename(projectName);
    const zipQuery = encodeURIComponent(analysis?.zipFilename || analysis?.zip || "");
    let url = "";
    let defaultFileName = "";

    if (format === "Word") {
      // use the backend's expected query name "zipFilename"
      url = "/download/word_documentation" + (zipQuery ? `?zipFilename=${zipQuery}` : "");
      defaultFileName = `${safeProject}_Technical_Documentation.docx`;
    } else if (format === "PDF") {
      url = "/download/pdf_documentation" + (zipQuery ? `?zipFilename=${zipQuery}` : "");
      defaultFileName = `${safeProject}_Technical_Documentation.pdf`;
    } else if (format === "Markdown") {
      url = "/download/md_documentation" + (zipQuery ? `?zipFilename=${zipQuery}` : "");
      defaultFileName = `${safeProject}_Technical_Documentation.md`;
    } else {
      return;
    }

    await doFetchDownload(url, defaultFileName);
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
        <div
            className="grid gap-3 text-center"
            style={{ gridTemplateColumns: "repeat(auto-fit, minmax(130px, 1fr))" }}
              >
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
              Web Docs
            </div>
          </div>
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.sqlChapters}
            </div>
            <div className="text-sm text-gray-600">SQL Docs</div>
          </div>
           <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.apiChapters}
            </div>
            <div className="text-sm text-gray-600">API Docs</div>
          </div>
          <div className="space-y-1">
            <div className="text-xl font-medium text-gray-900">
              {totals.utilityChapters}
            </div>
            <div className="text-sm text-gray-600">
              Other Docs
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

          {/* If no documentation chapters were generated, show message and disable downloads */}
          {!docsAvailable && !isDownloading && (
            <div className="mb-4 p-4 rounded bg-yellow-50 border border-yellow-100 text-sm text-yellow-800">
              No documentation chapters were generated. Downloads are disabled.
            </div>
          )}

          <div className="space-y-3">
          <Button
              onClick={() => handleDownload("Markdown")}
              className="w-full justify-start"
              disabled={isDownloading || !docsAvailable}
           >
        <Globe className="h-4 w-4 mr-2" />
            Markdown Document
            <span className="ml-auto text-xs text-gray-500">Recommended</span>
              </Button>

         
          <Button
            onClick={() => handleDownload("Word")}
            variant="outline"
              className="w-full justify-start"
            disabled={isDownloading || !docsAvailable}
          >
            <FileArchive className="h-4 w-4 mr-2" />
            Word Document
            <span className="ml-auto text-xs text-gray-500">—</span>
          </Button>

          <Button
            onClick={() => handleDownload("PDF")}
            variant="outline"
              className="w-full justify-start"
            disabled={isDownloading || !docsAvailable}
          >
            <FileText className="h-4 w-4 mr-2" />
            PDF Document
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

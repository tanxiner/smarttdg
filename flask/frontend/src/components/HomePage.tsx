import { FileUploadZone } from "./FileUploadZone";
import { Card } from "./ui/card";
import { Zap, Shield, Palette } from "lucide-react";
import * as React from "react";

interface HomePageProps {
  onDocumentationReady?: (result?: any) => void;
}

export function HomePage({ onDocumentationReady }: HomePageProps) {
  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <div className="text-center py-12">
        <h1 className="text-4xl font-medium text-gray-900 mb-4">
          SmartTDG: AI-Powered Technical Document Generator
        </h1>
      </div>

      {/* Upload Section */}
      <section>
        <div className="text-center mb-8">
          <h2 className="text-2xl font-medium text-gray-900 mb-2">
            Get Started
          </h2>
          <p className="text-gray-600">
            Upload your project ZIP file to begin generating technical documentation
          </p>
        </div>
        <FileUploadZone onDocumentationReady={onDocumentationReady} />
      </section>
    </div>
  );
}
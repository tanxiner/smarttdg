import { Card } from "./ui/card";
import { FileArchive, Upload, Settings, Download } from "lucide-react";
import * as React from "react";

export function HowToPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-medium text-gray-900 mb-4">How to Use SmartTDG</h1>
        <p className="text-lg text-gray-600">
          Follow these simple steps to generate technical documentation for your project.
        </p>
      </div>

      <div className="space-y-8">
        <Card className="p-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <div className="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center text-sm font-medium">
                1
              </div>
            </div>
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                <FileArchive className="h-5 w-5 text-primary" />
                <h3 className="text-lg font-medium">Prepare Your Project</h3>
              </div>
              <p className="text-gray-600 mb-3">
                Create a ZIP file containing your project source code. Include all relevant 
                files such as source code and stored procedures.
              </p>
              {/* <div className="bg-gray-50 p-3 rounded text-sm">
                <strong>Tips:</strong>
                <ul className="list-disc list-inside mt-1 space-y-1">
                  <li>Include README files and inline code comments</li>
                  <li>Add package.json, requirements.txt, or similar dependency files</li>
                  <li>Exclude node_modules, build folders, and large binary files</li>
                </ul>
              </div> */}
            </div>
          </div>
        </Card>

        <Card className="p-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <div className="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center text-sm font-medium">
                2
              </div>
            </div>
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                <Upload className="h-5 w-5 text-primary" />
                <h3 className="text-lg font-medium">Upload Your ZIP File</h3>
              </div>
              <p className="text-gray-600 mb-3">
                Drag and drop your ZIP file onto the upload zone or click to browse and 
                select your file. Maximum file size is 1GB.
              </p>
              <div className="bg-blue-50 p-3 rounded text-sm">
                <strong>Supported formats:</strong> .zip files containing aspx, .ascx, 
                .vb, .cs, .js, .sql, .html, .master, and .sln files.
              </div>
            </div>
          </div>
        </Card>

        {/* <Card className="p-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <div className="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center text-sm font-medium">
                3
              </div>
            </div>
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                <Settings className="h-5 w-5 text-primary" />
                <h3 className="text-lg font-medium">Configure Options (Optional)</h3>
              </div>
              <p className="text-gray-600 mb-3">
                Customize your documentation by selecting a template, choosing which files 
                to include, and adding any custom sections or branding.
              </p>
              <div className="bg-green-50 p-3 rounded text-sm">
                <strong>Quick start:</strong> Use the default settings for instant results, 
                or customize later when you're familiar with the platform.
              </div>
            </div>
          </div>
        </Card> */}

        <Card className="p-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0">
              <div className="w-8 h-8 bg-primary text-white rounded-full flex items-center justify-center text-sm font-medium">
                3
              </div>
            </div>
            <div className="flex-1">
              <div className="flex items-center space-x-2 mb-2">
                <Download className="h-5 w-5 text-primary" />
                <h3 className="text-lg font-medium">Download Your Documentation/Diagrams</h3>
              </div>
              <p className="text-gray-600 mb-3">
                Once processing is complete, download your documentation/diagrams.
              </p>
              {/* <div className="bg-purple-50 p-3 rounded text-sm">
                <strong>Sharing:</strong> HTML documentation can be hosted anywhere, and 
                you'll get a shareable preview link that expires in 30 days.
              </div> */}
            </div>
          </div>
        </Card>
      </div>

      {/* <Card className="p-6 mt-8 bg-gray-50">
        <h3 className="text-lg font-medium mb-3">Need Help?</h3>
        <p className="text-gray-600">
          Check out our <span className="font-medium">FAQ section</span> for other common questions.
        </p>
      </Card> */}
    </div>
  );
}
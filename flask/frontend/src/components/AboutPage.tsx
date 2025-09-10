import * as React from "react";
import { Card } from "./ui/card";

export function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-medium text-gray-900 mb-4">About SmartTDG</h1>
        <p className="text-lg text-gray-600">
          Automatically generate technical documentation from your codebase.
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <Card className="p-6">
          <h3 className="text-lg font-medium mb-3">Static Analysis</h3>
          <p className="text-gray-600">
            Static analysis is conducted through Roslyn analyser, to extract namespaces, classes, 
            interfaces, methods, parameters, and XML comments.
          </p>
        </Card>

        <Card className="p-6">
          <h3 className="text-lg font-medium mb-3">AI-Powered</h3>
          <p className="text-gray-600">
            Using AI/ML, summaries and useful key insights are generated.
          </p>
        </Card>

        <Card className="p-6">
          <h3 className="text-lg font-medium mb-3">Diagram Generation</h3>
          <p className="text-gray-600">
            Output from static analysis and AI/ML analysis are combined to create meaningful 
            diagrams such as class diagrams, flowchart, etc.
          </p>
        </Card>
      </div>

      {/* <Card className="p-6">
        <h3 className="text-lg font-medium mb-3">Our Mission</h3>
        <p className="text-gray-600">
          We believe that good documentation shouldn't be a burden. DocGen helps 
          developers focus on building great software while ensuring their projects 
          are well-documented and accessible to their teams and users.
        </p>
      </Card> */}
    </div>
  );
}
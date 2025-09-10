import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./ui/accordion";
import * as React from "react";
export function FAQPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-medium text-gray-900 mb-4">
          Frequently Asked Questions
        </h1>
        <p className="text-lg text-gray-600">
          Get answers to common questions about SmartTDG.
        </p>
      </div>

      <Accordion type="single" collapsible className="space-y-4">
        <AccordionItem value="item-1" className="border rounded-lg px-6">
          <AccordionTrigger>What file formats are supported?</AccordionTrigger>
          <AccordionContent>
            SmartTDG supports ZIP files containing aspx, .ascx, .vb, .cs, .js, .sql, .html, .master, and .sln files. 
            The maximum file size is 1GB.
          </AccordionContent>
        </AccordionItem>

        <AccordionItem value="item-2" className="border rounded-lg px-6">
          <AccordionTrigger>How long does it take to generate documentation?</AccordionTrigger>
          <AccordionContent>
            Processing time depends on the size and complexity of your project. Most projects 
            are processed within X minutes.
          </AccordionContent>
        </AccordionItem>

        <AccordionItem value="item-3" className="border rounded-lg px-6">
          <AccordionTrigger>Is my code kept private and secure?</AccordionTrigger>
          <AccordionContent>
            Yes, we take security seriously. Your code is processed in isolated environments, 
            encrypted in transit and at rest, and automatically deleted after processing. 
            We never store or share your source code.
          </AccordionContent>
        </AccordionItem>

        <AccordionItem value="item-4" className="border rounded-lg px-6">
          <AccordionTrigger>Can I customize the documentation output?</AccordionTrigger>
          <AccordionContent>
            Absolutely! You can choose from multiple templates, customize colors and branding, 
            exclude certain files or directories, and add custom sections to your documentation.
          </AccordionContent>
        </AccordionItem>

        <AccordionItem value="item-5" className="border rounded-lg px-6">
          <AccordionTrigger>What if my project has dependencies?</AccordionTrigger>
          <AccordionContent>
            DocGen automatically detects and documents your project's dependencies. Make sure to 
            include your package.json, requirements.txt, or equivalent dependency files in your ZIP.
          </AccordionContent>
        </AccordionItem>

        <AccordionItem value="item-6" className="border rounded-lg px-6">
          <AccordionTrigger>Do you offer API access?</AccordionTrigger>
          <AccordionContent>
            Yes! We provide a REST API for enterprise customers who want to integrate DocGen 
            into their CI/CD pipelines. Contact us for API documentation and pricing.
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </div>
  );
}
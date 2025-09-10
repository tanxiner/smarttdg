import { useState } from "react";
import { Button } from "./ui/button";
import * as React from "react";

interface NavigationProps {
  currentPage: string;
  onPageChange: (page: string) => void;
  onShowDownload?: () => void;
}

export function Navigation({ currentPage, onPageChange, onShowDownload }: NavigationProps) {
  return (
    <header className="border-b border-gray-200 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-xl font-medium text-gray-900">SmartTDG</h1>
          </div>
          <nav className="flex space-x-8">
            <Button
              variant={currentPage === "home" ? "default" : "ghost"}
              onClick={() => onPageChange("home")}
            >
              Home
            </Button>
            {/* <Button
              variant={currentPage === "about" ? "default" : "ghost"}
              onClick={() => onPageChange("about")}
            >
              About
            </Button>
            <Button
              variant={currentPage === "faq" ? "default" : "ghost"}
              onClick={() => onPageChange("faq")}
            >
              FAQ
            </Button> */}
            <Button
              variant={currentPage === "howto" ? "default" : "ghost"}
              onClick={() => onPageChange("howto")}
            >
              How To
            </Button>
            <Button
              variant="outline"
              onClick={onShowDownload}
              className="bg-blue-50 border-blue-200 text-blue-700 hover:bg-blue-100"
            >
              Download (Demo)
            </Button>
          </nav>
        </div>
      </div>
    </header>
  );
}
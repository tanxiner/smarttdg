import json
import time
import os
import json
import graphviz
from langchain_ollama import OllamaLLM
import subprocess

INPUT_FILE = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results1.json")
OUTPUT_MAP = 'project_map.txt'
input_path = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results1.json")


def get_file_name(item):
    """Find the filename by checking multiple possible keys."""
    if "file" in item and item["file"]: return item["file"]
    if "fileName" in item and item["fileName"]: return item["fileName"]
    if "ir" in item:
        if "path" in item["ir"] and item["ir"]["path"]: return item["ir"]["path"]
        if "file" in item["ir"] and item["ir"]["file"]: return item["ir"]["file"]
    return "Unknown File"

def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    summary_lines = ["PROJECT STRUCTURE MAP (Use for Context references)\n"]
    
    # Counter to see how much noise we remove
    skipped_count = 0

    for item in data:
        # --- NAMESPACE ---
        ns = "Unknown"
        if "namespaces" in item and item["namespaces"] and len(item["namespaces"]) > 0:
            ns = item["namespaces"][0]
        elif "ir" in item and "namespaces" in item["ir"] and item["ir"]["namespaces"] and len(item["ir"]["namespaces"]) > 0:
            ns = item["ir"]["namespaces"][0]

        # --- FILENAME ---
        file_name = get_file_name(item)
        
        # --- CLASSES ---
        classes = []
        if "classes" in item:
            classes = item["classes"]
        elif "ir" in item and "types" in item["ir"]:
            classes = item["ir"]["types"]

        # FILTER: If no classes are found, SKIP this file.
        # This removes the empty .aspx entries, config files, etc.
        if not classes:
            skipped_count += 1
            continue

        for cls in classes:
            class_name = cls.get("name", "Unnamed")
            summary_lines.append(f"Namespace: {ns} | File: {file_name} | Class: {class_name}")
            
            # --- METHODS ---
            methods = cls.get("methods", [])
            if not methods and "methods" in item: methods = item["methods"]

            method_names = [m.get("name") for m in methods if isinstance(m, dict) and m.get("name")]
            
            if method_names:
                display_methods = method_names[:10]
                method_str = ", ".join(display_methods)
                if len(method_names) > 10:
                    method_str += ", ..."
                summary_lines.append(f"   Methods: {method_str}")
            
            summary_lines.append("") 

    with open(OUTPUT_MAP, 'w', encoding='utf-8') as f:
        f.write("\n".join(summary_lines))
    
    print(f"Success! Map generated: {OUTPUT_MAP}")
    print(f"Cleaned up {skipped_count} empty files (views/configs) to save context.")

if __name__ == "__main__":
    main()
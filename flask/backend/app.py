from flask import Flask, request, jsonify, send_from_directory
import os
from time import sleep
import tempfile
import zipfile
import shutil
import time
from pathlib import Path

# Import the analyzer runner
from services.analyzer.analyzer_runner import analyze_code as run_analyzer

BASE_DIR = os.path.dirname(__file__)
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, '..', 'frontend', 'build'),
    static_url_path='/'
)

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def analyze_zip(zip_path: str) -> dict:
    temp_dir = tempfile.mkdtemp(prefix="smarttdg_")
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            print("Files in ZIP:", [f.filename for f in z.infolist()])
            z.extractall(temp_dir)
            print("Extracted files:", list(Path(temp_dir).rglob("*")))

        # Recursively collect .cs and .vb files
        all_paths = list(Path(temp_dir).rglob("*"))
        dirs = [p for p in all_paths if p.is_dir()]
        cs_files = [
            p for p in all_paths
            if p.is_file() and p.suffix.lower() in (".cs", ".vb")
        ]
        cs_files.sort(key=lambda p: str(p.relative_to(temp_dir)).lower())
        
        if not cs_files:
            return {
                "status": "ok",
                "message": "No .cs or .vb files found in archive.",
                "filesDiscovered": 0,
                "filesAnalyzed": 0,
                "foldersVisited": len(dirs),
                "results": []
            }
        
        # Collect all file paths as strings
        file_paths = [str(p) for p in cs_files]
        
        # Call analyzer ONCE with ALL files
        try:
            analysis_result = run_analyzer(*file_paths)  # Pass all files as separate arguments
            
            # Build results array with relative paths
            results = []
            for p in cs_files:
                rel = str(p.relative_to(temp_dir))
                results.append({
                    "file": rel,
                    "result": "analyzed"  # or extract individual result if available
                })
            
        except Exception as ex:
            return {
                "status": "error",
                "message": f"Analysis failed: {str(ex)}",
                "filesDiscovered": len(cs_files),
                "filesAnalyzed": 0,
                "foldersVisited": len(dirs),
                "results": []
            }
        
        # Diagnostics
        discovered_sample = [str(p.relative_to(temp_dir)) for p in cs_files[:10]]
        folders_with_cs = sorted({str(p.parent.relative_to(temp_dir)) for p in cs_files})[:10]
        
        return {
            "status": "ok",
            "message": "Analysis complete",
            "filesDiscovered": len(cs_files),
            "filesAnalyzed": len(results),
            "foldersVisited": len(dirs),
            "foldersWithCsSample": folders_with_cs,
            "discoveredSample": discovered_sample,
            "results": results,
            "analysisOutput": analysis_result  # Include the actual analysis result
        }
    finally:
        try:
            os.remove(zip_path)
        except OSError:
            pass
        shutil.rmtree(temp_dir, ignore_errors=True)


@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if not file.filename.lower().endswith(".zip"):
        return jsonify({"error": "Only .zip files are supported"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        size_mb = round(os.path.getsize(filepath) / 1024 / 1024, 2)
    except OSError:
        size_mb = None

    start = time.perf_counter()
    try:
        result = analyze_zip(filepath)
        duration_ms = int((time.perf_counter() - start) * 1000)
        result.update({
            "zipFilename": file.filename,
            "sizeMB": size_mb,
            "processingMs": duration_ms
        })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve static assets and SPA fallback
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_spa(path):
    file_path = os.path.join(app.static_folder, path)
    if path and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

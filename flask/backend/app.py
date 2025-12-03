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
    # create a short temp base on the same drive as the system temp to avoid very long paths
    sys_tmp = Path(tempfile.gettempdir())
    short_base = os.path.join(sys_tmp.drive + os.sep, "sdtg_tmp")
    os.makedirs(short_base, exist_ok=True)

    temp_dir = tempfile.mkdtemp(prefix="smarttdg_", dir=short_base)
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            print("Files in ZIP:", [f.filename for f in z.infolist()])
            z.extractall(temp_dir)
            print("Extracted files:", list(Path(temp_dir).rglob("*")))

        # Recursively collect files we want to analyze (code-behind and markup)
        all_paths = list(Path(temp_dir).rglob("*"))
        dirs = [p for p in all_paths if p.is_dir()]

        # include code and markup extensions commonly used by the analyzer
        desired_suffixes = {
            ".cs", ".vb",          # code-behind / source files
            ".cshtml", ".vbhtml",  # Razor views
            ".aspx", ".ascx", ".master"  # WebForms markup
        }

        files_to_analyze = [
            p for p in all_paths
            if p.is_file() and p.suffix.lower() in desired_suffixes
        ]
        files_to_analyze.sort(key=lambda p: str(p.relative_to(temp_dir)).lower())

        if not files_to_analyze:
            return {
                "status": "ok",
                "message": "No supported source or markup files found in archive.",
                "filesDiscovered": 0,
                "filesAnalyzed": 0,
                "foldersVisited": len(dirs),
                "results": []
            }

        # Prepare to call analyzer with short, relative paths to avoid long command-line / path issues
        rel_paths = [str(p.relative_to(temp_dir)) for p in files_to_analyze]

        # Debug: print command length estimates
        total_length = sum(len(p) + 1 for p in rel_paths)
        print(f"[Debug] Calling analyzer from cwd='{temp_dir}' with {len(rel_paths)} files (approx cmd length={total_length})")

        analysis_result = None
        cwd_before = os.getcwd()
        try:
            # run analyzer from inside temp_dir so arguments are short relative paths
            os.chdir(temp_dir)
            # call analyzer with relative paths
            analysis_result = run_analyzer(*rel_paths)
        finally:
            # always restore cwd
            try:
                os.chdir(cwd_before)
            except Exception:
                pass

        # Build results array with relative paths
        results = []
        for p in files_to_analyze:
            rel = str(p.relative_to(temp_dir))
            results.append({
                "file": rel,
                "result": "analyzed"
            })

        # Diagnostics
        discovered_sample = [str(p.relative_to(temp_dir)) for p in files_to_analyze[:10]]
        folders_with_cs = sorted({str(p.parent.relative_to(temp_dir)) for p in files_to_analyze})[:10]

        return {
            "status": "ok",
            "message": "Analysis complete",
            "filesDiscovered": len(rel_paths),
            "filesAnalyzed": len(results),
            "foldersVisited": len(dirs),
            "foldersWithCsSample": folders_with_cs,
            "discoveredSample": discovered_sample,
            "results": results,
            "analysisOutput": analysis_result  # Include the actual analysis result
        }
    except Exception as ex:
        return {
            "status": "error",
            "message": f"Analysis failed: {str(ex)}",
            "filesDiscovered": len(files_to_analyze) if 'files_to_analyze' in locals() else 0,
            "filesAnalyzed": 0,
            "foldersVisited": len(dirs) if 'dirs' in locals() else 0,
            "results": []
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

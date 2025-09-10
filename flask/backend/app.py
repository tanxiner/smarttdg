from flask import Flask, request, jsonify, send_from_directory
import os
from time import sleep
import tempfile
import zipfile
import shutil

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
            z.extractall(temp_dir)

        # Collect C# files
        cs_files = []
        for root, _, files in os.walk(temp_dir):
            for f in files:
                if f.lower().endswith(".cs"):
                    cs_files.append(os.path.join(root, f))

        if not cs_files:
            return {
                "status": "ok",
                "message": "No .cs files found in archive.",
                "filesAnalyzed": 0,
                "results": []
            }

        results = []
        # Limit to a reasonable number to keep response quick; remove slice to analyze all
        for f in cs_files[:100]:
            rel = os.path.relpath(f, start=temp_dir)
            try:
                analysis = run_analyzer(f)
                results.append({"file": rel, "result": analysis})
            except Exception as ex:
                results.append({"file": rel, "error": str(ex)})

        return {
            "status": "ok",
            "message": "Analysis complete",
            "filesAnalyzed": len(results),
            "results": results
        }
    finally:
        # Clean up the uploaded zip and extracted content
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
        result = analyze_zip(filepath)
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
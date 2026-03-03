using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Roslyn.Analyzers;

class Program
{
    static int Main(string[] args)
    {
        try
        {
            // Prefer explicit FLASK_ROOT env var set by caller; otherwise try to locate the repository's "flask" folder
            string? flaskRoot = null;
            var flaskRootEnv = Environment.GetEnvironmentVariable("FLASK_ROOT");
            if (!string.IsNullOrWhiteSpace(flaskRootEnv) && Directory.Exists(flaskRootEnv))
            {
                flaskRoot = flaskRootEnv;
            }
            else
            {
                var exeDir = AppContext.BaseDirectory;
                flaskRoot = FindFolderUp(exeDir, "flask");
            }

            if (args.Length == 0)
            {
                Console.WriteLine(JsonConvert.SerializeObject(new { error = "No file path provided" }));
                return 0;
            }

            // --- CHANGED: Support for @filelist argument to bypass CLI limits ---
            List<string> filesToAnalyze = new List<string>();
            
            // Check if the first argument is a file list (starts with @ or just a .txt convention we establish)
            // Ideally, we just check if args[0] is a text file that contains a list of paths.
            // For robustness, we'll assume if args.Length == 1 and it's a valid text file, treat it as a list.
            if (args.Length == 1 && File.Exists(args[0]) && Path.GetExtension(args[0]).Equals(".txt", StringComparison.OrdinalIgnoreCase))
            {
                try 
                {
                    // Read lines, trimming and ignoring empty ones
                    var lines = File.ReadAllLines(args[0]);
                    foreach (var line in lines)
                    {
                        var trimmed = line.Trim();
                        if (!string.IsNullOrWhiteSpace(trimmed)) 
                        {
                            filesToAnalyze.Add(trimmed);
                        }
                    }
                    Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Read file list from input file", listFile = args[0], count = filesToAnalyze.Count }));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new { error = "Failed to read file list", message = ex.Message }));
                    return 1;
                }
            }
            else
            {
                // Normal behavior: args are the files
                filesToAnalyze.AddRange(args);
            }

            if (filesToAnalyze.Count == 0)
            {
                Console.WriteLine(JsonConvert.SerializeObject(new { error = "No files found to analyze" }));
                return 0;
            }

            // Accumulate ALL results in memory first
            List<object> allResults = new List<object>();

            // Process each file
            foreach (var filePath in filesToAnalyze)
            {
                if (!File.Exists(filePath))
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new
                    {
                        error = "File not found",
                        filePath,
                        cwd = Environment.CurrentDirectory
                    }));
                    continue; // Skip this file but continue with others
                }

                var code = File.ReadAllText(filePath);
                var ext = Path.GetExtension(filePath).ToLowerInvariant();
                object result = null;

                try
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Analyzing file", filePath, ext }));

                    if (ext == ".cs")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeCSharp", filePath }));
                        result = CSharpAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".vb")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeVisualBasic", filePath }));
                        result = VisualBasicAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".aspx" || ext == ".ascx" || ext == ".master")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeAspx", filePath }));
                        result = AspxAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".js")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeJs", filePath }));
                        result = JsAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".html")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeHtml", filePath }));
                        result = HtmlAnalyzer.Analyze(code, filePath);
                    }
                    else
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Skipping unsupported file", filePath, ext }));
                    }
                }
                catch (Exception innerEx)
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new
                    {
                        error = "Exception in analysis dispatch",
                        filePath,
                        ext,
                        exceptionType = innerEx.GetType().FullName,
                        message = innerEx.Message,
                        stackTrace = innerEx.StackTrace
                    }));
                    continue; // Skip this file but continue with others
                }

                if (result != null)
                {
                    allResults.Add(result);
                }
            }

            // Write ALL results ONCE at the end
            if (allResults.Count > 0)
            {
                // Determine output directory:
                // 1) If caller sets ANALYZER_OUTPUT_DIR env var, use it.
                // 2) Otherwise try current working directory.
                // 3) Fallback to user's Documents.
                string? outputDir = Environment.GetEnvironmentVariable("ANALYZER_OUTPUT_DIR");
                if (string.IsNullOrWhiteSpace(outputDir))
                {
                    try
                    {
                        outputDir = Environment.CurrentDirectory;
                    }
                    catch
                    {
                        outputDir = null;
                    }
                }
                if (string.IsNullOrWhiteSpace(outputDir))
                {
                    outputDir = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
                }

                var outputPath = Path.Combine(outputDir, "all_analysis_results.json");

                File.WriteAllText(outputPath, JsonConvert.SerializeObject(allResults, Formatting.Indented));
                Console.WriteLine(JsonConvert.SerializeObject(new
                {
                    savedTo = outputPath,
                    totalFiles = filesToAnalyze.Count,
                    successfulAnalyses = allResults.Count
                }));

                // --- AUTOMATION: invoke downstream Python processors (non-interactive) ---
                // Skip when called from Flask (ROSLYN_SKIP_DOWNSTREAM=1) because app.py owns
                // the downstream pipeline in that context.  When invoked directly from the CLI
                // (no such flag), Program.cs runs the full pipeline itself.
                var skipDownstream = string.Equals(
                    Environment.GetEnvironmentVariable("ROSLYN_SKIP_DOWNSTREAM") ?? "",
                    "1", StringComparison.Ordinal);

                if (skipDownstream)
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new { debug = "ROSLYN_SKIP_DOWNSTREAM=1; downstream scripts will be run by the calling process (Flask)" }));
                }
                else
                try
                {
                    if (flaskRoot == null)
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "flask folder not found; skipping downstream scripts" }));
                    }
                    else
                    {
                        // Load the canonical pipeline from the shared pipeline.json file.
                        // This is the single source of truth for script ordering; edit that file to
                        // add, remove, or reorder steps.
                        var backendRoot = Path.Combine(flaskRoot, "backend");
                        var pipelineJsonPath = Path.Combine(backendRoot, "pipeline.json");

                        string[] scripts;
                        if (File.Exists(pipelineJsonPath))
                        {
                            try
                            {
                                var pipelineObj = JObject.Parse(File.ReadAllText(pipelineJsonPath));
                                var steps = (JArray?)pipelineObj["steps"] ?? new JArray();
                                var scriptList = new List<string>();
                                foreach (var step in steps)
                                {
                                    var rel = ((string?)step["script"] ?? "").Replace('/', Path.DirectorySeparatorChar);
                                    if (!string.IsNullOrWhiteSpace(rel))
                                        scriptList.Add(Path.Combine(backendRoot, rel));
                                }
                                scripts = scriptList.ToArray();
                                Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Loaded pipeline from pipeline.json", stepCount = scripts.Length, path = pipelineJsonPath }));
                            }
                            catch (Exception exJson)
                            {
                                Console.WriteLine(JsonConvert.SerializeObject(new { error = "Failed to parse pipeline.json; skipping downstream scripts. Please verify the JSON syntax in pipeline.json.", path = pipelineJsonPath, message = exJson.Message }));
                                scripts = Array.Empty<string>();
                            }
                        }
                        else
                        {
                            Console.WriteLine(JsonConvert.SerializeObject(new { error = $"pipeline.json not found; skipping downstream scripts. Expected path: {pipelineJsonPath}" }));
                            scripts = Array.Empty<string>();
                        }

                        var pythonExe = FindPythonExecutable() ?? "python";

                        foreach (var script in scripts)
                        {
                            if (!File.Exists(script))
                            {
                                Console.WriteLine(JsonConvert.SerializeObject(new { debug = "script_not_found", script }));
                                continue;
                            }

                            Console.WriteLine(JsonConvert.SerializeObject(new { debug = "running_script", script }));

                            var workDir = Path.GetDirectoryName(script) ?? flaskRoot;
                            var success = RunExternalScript(pythonExe, script, workDir, TimeSpan.FromMinutes(30), out var stdout, out var stderr);

                            Console.WriteLine(JsonConvert.SerializeObject(new
                            {
                                script,
                                success,
                                stdout_summary = Shorten(stdout, 2000),
                                stderr_summary = Shorten(stderr, 2000)
                            }));
                        }
                    }
                }
                catch (Exception exScripts)
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new
                    {
                        error = "Exception while running downstream scripts",
                        exceptionType = exScripts.GetType().FullName,
                        message = exScripts.Message,
                        stackTrace = exScripts.StackTrace
                    }));
                }
            }

            return 0;
        }
        catch (Exception ex)
        {
            Console.WriteLine(JsonConvert.SerializeObject(new
            {
                error = "Exception in Main",
                exceptionType = ex.GetType().FullName,
                message = ex.Message,
                stackTrace = ex.StackTrace
            }));
            return 1;
        }
    }

    // --- Helper: run external python script with timeout and capture output ---
    static bool RunExternalScript(string pythonExe, string scriptPath, string workingDirectory, TimeSpan timeout, out string stdout, out string stderr)
    {
        stdout = "";
        stderr = "";

        try
        {
            var psi = new ProcessStartInfo
            {
                FileName = pythonExe,
                Arguments = $"\"{scriptPath}\"",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
                WorkingDirectory = workingDirectory
            };

            using var proc = new Process { StartInfo = psi, EnableRaisingEvents = true };
            var sbOut = new StringBuilder();
            var sbErr = new StringBuilder();

            proc.OutputDataReceived += (_, e) => { if (e.Data != null) sbOut.AppendLine(e.Data); };
            proc.ErrorDataReceived += (_, e) => { if (e.Data != null) sbErr.AppendLine(e.Data); };

            if (!proc.Start())
            {
                stderr = "Failed to start process.";
                return false;
            }

            proc.BeginOutputReadLine();
            proc.BeginErrorReadLine();

            if (!proc.WaitForExit((int)timeout.TotalMilliseconds))
            {
                try
                {
                    proc.Kill(true);
                }
                catch { /* best-effort */ }

                stderr = $"Process timed out after {timeout.TotalMinutes} minutes.";
                stdout = sbOut.ToString();
                return false;
            }

            stdout = sbOut.ToString();
            stderr = sbErr.ToString();

            return proc.ExitCode == 0;
        }
        catch (Exception ex)
        {
            stderr = ex.ToString();
            return false;
        }
    }

    // --- Helper: shorten long outputs for logs ---
    static string Shorten(string s, int max)
    {
        if (string.IsNullOrEmpty(s)) return "";
        if (s.Length <= max) return s;
        return s.Substring(0, max) + "...(truncated)";
    }

    // --- Helper: find folder by walking parent directories ---
    static string? FindFolderUp(string startDirectory, string folderName)
    {
        try
        {
            var dir = new DirectoryInfo(startDirectory);
            while (dir != null)
            {
                var candidate = Path.Combine(dir.FullName, folderName);
                if (Directory.Exists(candidate)) return candidate;
                dir = dir.Parent;
            }
        }
        catch { }
        return null;
    }

    // --- Helper: try to resolve a usable python exe name by probing common names ---
    static string? FindPythonExecutable()
    {
        var candidates = new[] { Environment.GetEnvironmentVariable("PYTHON_BIN") ?? "", "python", "python3" }
                         .Where(s => !string.IsNullOrWhiteSpace(s));

        foreach (var c in candidates)
        {
            try
            {
                var psi = new ProcessStartInfo
                {
                    FileName = c,
                    Arguments = "--version",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };
                using var p = Process.Start(psi);
                if (p == null) continue;
                if (!p.WaitForExit(3000)) { try { p.Kill(true); } catch { } continue; }
                // If exit code is 0, treat as valid python
                if (p.ExitCode == 0) return c;
            }
            catch { /* ignore and try next */ }
        }
        return null;
    }
}

using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using Roslyn.Analyzers;

class Program
{
    static int Main(string[] args)
    {
        try
        {
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
                var pathLower = (filePath ?? "").ToLowerInvariant();
                object result = null;

                try
                {
                    Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Analyzing file", filePath, ext }));

                    // Prefer compound checks (code-behind for Razor pages) before single-extension checks
                    if (pathLower.EndsWith(".cshtml.cs") || pathLower.EndsWith(".razor.cs") || ext == ".cs")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeCSharp", filePath }));
                        result = CSharpAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".vb")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeVisualBasic", filePath }));
                        result = VisualBasicAnalyzer.Analyze(code, filePath);
                    }
                    else if (pathLower.EndsWith(".aspx") || pathLower.EndsWith(".ascx") || pathLower.EndsWith(".master"))
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeAspx", filePath }));
                        result = AspxAnalyzer.Analyze(code, filePath);
                    }
                    else if (ext == ".js" || ext == ".jsx")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeJs", filePath }));
                        result = JsAnalyzer.Analyze(code, filePath);
                    }
                    else if (pathLower.EndsWith(".html"))
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeHtml", filePath }));
                        result = HtmlAnalyzer.Analyze(code, filePath);
                    }
                    // Razor markup (.cshtml) and Blazor components (.razor) -> use CshtmlExtractor
                    else if (pathLower.EndsWith(".cshtml") || pathLower.EndsWith(".razor"))
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling CshtmlExtractor.Analyze (Razor/Blazor)", filePath }));
                        result = CshtmlExtractor.Analyze(code, filePath);
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

}

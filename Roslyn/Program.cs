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

            // Accumulate ALL results in memory first
            List<object> allResults = new List<object>();

            // Process each file
            foreach (var filePath in args)
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
                    else if (ext == ".cshtml")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeCshtml", filePath }));
                        result = CshtmlExtractor.Analyze(code, filePath);
                    }
                    else if (ext == ".aspx" || ext == ".ascx" || ext == ".master")
                    {
                        Console.WriteLine(JsonConvert.SerializeObject(new { debug = "Calling AnalyzeAspx", filePath }));
                        result = AspxExtractor.Analyze(code, filePath);

                        // Debug: confirm AspxExtractor ran and returned something
                        try
                        {
                            Console.WriteLine(JsonConvert.SerializeObject(new
                            {
                                debug = "AspxAnalyzerReturned",
                                file = Path.GetFileName(filePath),
                                ext,
                                hasResult = result != null
                            }, Formatting.None));
                        }
                        catch
                        {
                            Console.WriteLine(JsonConvert.SerializeObject(new
                            {
                                debug = "AspxAnalyzerReturned (serialization failed)",
                                file = Path.GetFileName(filePath),
                                ext
                            }));
                        }
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
                var outputPath = Path.Combine(
                    Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
                    "all_analysis_results1.json"
                );

                File.WriteAllText(outputPath, JsonConvert.SerializeObject(allResults, Formatting.Indented));
                Console.WriteLine(JsonConvert.SerializeObject(new
                {
                    savedTo = outputPath,
                    totalFiles = args.Length,
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

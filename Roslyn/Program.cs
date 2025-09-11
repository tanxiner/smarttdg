// Import necessary namespaces for code analysis, C# & VB syntax parsing, JSON serialization, and file operations
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.VisualBasic;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Linq;

// Alias syntax namespaces to avoid type name collisions (e.g., CompilationUnitSyntax)
using CSS = Microsoft.CodeAnalysis.CSharp.Syntax;
using VBS = Microsoft.CodeAnalysis.VisualBasic.Syntax;

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

            var filePath = args[0];
            if (!File.Exists(filePath))
            {
                Console.WriteLine(JsonConvert.SerializeObject(new
                {
                    error = "File not found",
                    filePath,
                    cwd = Environment.CurrentDirectory
                }));
                return 0;
            }

            var code = File.ReadAllText(filePath);
            var ext = Path.GetExtension(filePath).ToLowerInvariant();

            object result = ext switch
            {
                ".vb" => AnalyzeVisualBasic(code, filePath),
                _ => AnalyzeCSharp(code, filePath)
            };

            Console.WriteLine(JsonConvert.SerializeObject(result, Formatting.None));
            return 0;
        }
        catch (Exception ex)
        {
            Console.WriteLine(JsonConvert.SerializeObject(new { error = ex.Message }));
            return 1;
        }
    }

    private static object AnalyzeCSharp(string code, string filePath)
    {
        var tree = CSharpSyntaxTree.ParseText(code);
        var root = tree.GetCompilationUnitRoot(); // Remove explicit cast

        var classes = root.DescendantNodes().OfType<CSS.ClassDeclarationSyntax>()
            .Select(cls => new
            {
                Name = cls.Identifier.Text,
                Methods = cls.Members
                    .OfType<CSS.MethodDeclarationSyntax>()
                    .Select(m => new
                    {
                        Name = m.Identifier.Text,
                        ReturnType = m.ReturnType.ToString(),
                        Parameters = m.ParameterList.Parameters
                            .Select(p => new
                            {
                                Name = p.Identifier.Text,
                                Type = p.Type?.ToString()
                            })
                            .ToArray()
                    })
                    .ToArray()
            });

        var usingNames = root.Imports
            .SelectMany(i => i.ImportsClauses)
            .Select(ic => (ic as VBS.SimpleImportsClauseSyntax)?.Name?.ToString())
            .Where(s => !string.IsNullOrWhiteSpace(s))
            .Distinct()
            .Cast<string>()
            .ToArray();

        var namespaceNames = root.DescendantNodes()
            .OfType<CSS.BaseNamespaceDeclarationSyntax>() // NamespaceDeclarationSyntax, FileScopedNamespaceDeclarationSyntax
            .Select(n => n.Name?.ToString())
            .Where(s => !string.IsNullOrEmpty(s))
            .Distinct()
            .Cast<string>()
            .ToArray();

        var classList = classes.ToArray();
        return new
        {
            file = Path.GetFileName(filePath),
            usings = usingNames,
            namespaces = namespaceNames,
            totals = new
            {
                classes = classList.Length,
                methods = classList.Sum(c => c.Methods.Length)
            },
            classes = classList
        };
    }

    private static object AnalyzeVisualBasic(string code, string filePath)
    {
        var tree = VisualBasicSyntaxTree.ParseText(code);
        var root = (VBS.CompilationUnitSyntax)tree.GetCompilationUnitRoot();

        var usingNames = root.Imports
            .SelectMany(i => i.ImportsClauses)
            .Select(ic => (ic as VBS.SimpleImportsClauseSyntax)?.Name?.ToString())
            .Where(s => !string.IsNullOrWhiteSpace(s))
            .Distinct()
            .Cast<string>()
            .ToArray();

        var namespaceNames = root.Members
            .OfType<VBS.NamespaceBlockSyntax>()
            .Select(n => n.NamespaceStatement.Name?.ToString())
            .Where(s => !string.IsNullOrWhiteSpace(s))
            .Distinct()
            .Cast<string>()
            .ToArray();

        var classBlocks = root.DescendantNodes().OfType<VBS.ClassBlockSyntax>().ToArray();

        var classes = classBlocks.Select(cb =>
        {
            var methodBlocks = cb.Members.OfType<VBS.MethodBlockSyntax>()
                .Select(mb =>
                {
                    var header = mb.SubOrFunctionStatement;
                    var name = header.Identifier.Text;
                    var returnType = header.AsClause?.Type?.ToString() ?? "Void";
                    var parameters = (header.ParameterList?.Parameters
                        .Select(p => new
                        {
                            Name = p.Identifier?.ToString(),
                            Type = p.AsClause?.Type?.ToString()
                        })
                        .ToArray()) ?? Array.Empty<object>();

                    return new
                    {
                        Name = name,
                        ReturnType = returnType,
                        Parameters = parameters
                    };
                });

            var methodDecls = cb.Members.OfType<VBS.MethodStatementSyntax>()
                .Select(header => new
                {
                    Name = header.Identifier.Text,
                    ReturnType = header.AsClause?.Type?.ToString() ?? "Void",
                    Parameters = (header.ParameterList?.Parameters
                        .Select(p => new
                        {
                            Name = p.Identifier?.ToString(),
                            Type = p.AsClause?.Type?.ToString()
                        })
                        .ToArray()) ?? Array.Empty<object>()
                });

            var methods = methodBlocks.Concat(methodDecls).ToArray();

            return new
            {
                Name = cb.ClassStatement.Identifier.Text,
                Methods = methods
            };
        }).ToArray();

        return new
        {
            file = Path.GetFileName(filePath),
            usings = usingNames,
            namespaces = namespaceNames,
            totals = new
            {
                classes = classes.Length,
                methods = classes.Sum(c => c.Methods.Length)
            },
            classes
        };
    }
}

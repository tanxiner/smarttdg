using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.VisualBasic;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Roslyn.Analyzers
{
    using CSS = Microsoft.CodeAnalysis.CSharp.Syntax;
    using VBS = Microsoft.CodeAnalysis.VisualBasic.Syntax;

    public static class DependencyExtractor
    {
        public static object Extract(string path, string language = "C#")
        {
            try
            {
                string sourceDirectory = File.Exists(path)
                    ? Path.GetDirectoryName(path) ?? Environment.CurrentDirectory
                    : path;

                var csFiles = language == "C#"
                    ? Directory.GetFiles(sourceDirectory, "*.cs", SearchOption.AllDirectories)
                    : Array.Empty<string>();

                var vbFiles = language == "VB"
                    ? Directory.GetFiles(sourceDirectory, "*.vb", SearchOption.AllDirectories)
                    : Array.Empty<string>();

                var csSyntaxTrees = csFiles.Select(f => CSharpSyntaxTree.ParseText(File.ReadAllText(f), path: f)).ToList();
                var vbSyntaxTrees = vbFiles.Select(f => VisualBasicSyntaxTree.ParseText(File.ReadAllText(f), path: f)).ToList();

                var references = new List<MetadataReference>
                {
                    MetadataReference.CreateFromFile(typeof(object).Assembly.Location),
                    MetadataReference.CreateFromFile(typeof(Console).Assembly.Location),
                    MetadataReference.CreateFromFile(typeof(Enumerable).Assembly.Location),
                    MetadataReference.CreateFromFile(typeof(Uri).Assembly.Location)
                };

                var usings = new HashSet<string>();
                var imports = new HashSet<string>();
                var assemblies = new HashSet<string>();

                if (language == "C#")
                {
                    var csCompilation = CSharpCompilation.Create("CSharpAnalysis")
                        .AddSyntaxTrees(csSyntaxTrees)
                        .AddReferences(references);

                    foreach (var tree in csSyntaxTrees)
                    {
                        var root = tree.GetRoot();
                        foreach (var u in root.DescendantNodes().OfType<CSS.UsingDirectiveSyntax>())
                            usings.Add(u.Name.ToString());
                    }

                    foreach (var r in csCompilation.References)
                        if (!string.IsNullOrEmpty(r.Display))
                            assemblies.Add(Path.GetFileNameWithoutExtension(r.Display));
                }
                else if (language == "VB")
                {
                    var vbCompilation = VisualBasicCompilation.Create("VBAnalysis")
                        .AddSyntaxTrees(vbSyntaxTrees)
                        .AddReferences(references);

                    foreach (var tree in vbSyntaxTrees)
                    {
                        var root = tree.GetRoot();
                        foreach (var i in root.DescendantNodes().OfType<VBS.ImportsStatementSyntax>())
                        {
                            foreach (var ic in i.ImportsClauses.OfType<VBS.SimpleImportsClauseSyntax>())
                                if (!string.IsNullOrWhiteSpace(ic.Name?.ToString()))
                                    imports.Add(ic.Name.ToString());
                        }
                    }

                    foreach (var r in vbCompilation.References)
                        if (!string.IsNullOrEmpty(r.Display))
                            assemblies.Add(Path.GetFileNameWithoutExtension(r.Display));
                }

                return new
                {
                    dependencies = new
                    {
                        Language = language,
                        Usings = usings.ToArray(),
                        Imports = imports.ToArray(),
                        Assemblies = assemblies.ToArray()
                    }
                };
            }
            catch (Exception ex)
            {
                return new { error = "Dependency analysis failed", details = ex.Message };
            }
        }
    }
}

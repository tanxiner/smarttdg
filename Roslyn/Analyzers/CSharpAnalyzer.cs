using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace Roslyn.Analyzers
{
    using CSS = Microsoft.CodeAnalysis.CSharp.Syntax;

    public static class CSharpAnalyzer
    {
        public static object Analyze(string code, string filePath)
        {
            var tree = CSharpSyntaxTree.ParseText(code, path: filePath);
            var root = (CSS.CompilationUnitSyntax)tree.GetCompilationUnitRoot();

            // Create compilation with basic references; when run via MSBuildWorkspace Program.cs will provide richer references.
            var refs = new List<MetadataReference>
            {
                MetadataReference.CreateFromFile(typeof(object).Assembly.Location)
            };

            // attempt to add System.Data or Microsoft.Data.SqlClient if available in AppDomain
            try
            {
                var sd = AppDomain.CurrentDomain.GetAssemblies()
                    .FirstOrDefault(a => a.GetName().Name.Equals("System.Data", StringComparison.OrdinalIgnoreCase));
                if (sd != null) refs.Add(MetadataReference.CreateFromFile(sd.Location));
            }
            catch { /* ignore */ }

            var compilation = CSharpCompilation.Create("CSharpAnalysis")
                .AddSyntaxTrees(tree)
                .AddReferences(refs);

            var model = compilation.GetSemanticModel(tree);

            string GetTypeName(TypeSyntax? type) => type?.ToString() ?? "void";

            string FormatParameters(CSS.ParameterListSyntax? paramList)
            {
                if (paramList == null) return "";
                return string.Join(", ", paramList.Parameters.Select(p =>
                {
                    var type = p.Type?.ToString() ?? "object";
                    return $"{p.Identifier.Text}: {type}";
                }));
            }

            string GetModifiers(SyntaxTokenList mods)
                => string.Join(" ", mods.Select(m => m.Text));

            var classDetails = root.DescendantNodes().OfType<CSS.ClassDeclarationSyntax>()
                .Select(c => new
                {
                    name = c.Identifier.Text,
                    modifiers = GetModifiers(c.Modifiers),
                    baseType = c.BaseList?.Types.FirstOrDefault()?.Type.ToString(),
                    interfaces = c.BaseList?.Types.Skip(1).Select(t => t.Type.ToString()).ToArray() ?? Array.Empty<string>()
                })
                .ToArray();

            var interfaces = root.DescendantNodes().OfType<CSS.InterfaceDeclarationSyntax>()
                .Select(i => new
                {
                    name = i.Identifier.Text,
                    modifiers = GetModifiers(i.Modifiers)
                })
                .ToArray();

            var structs = root.DescendantNodes().OfType<CSS.StructDeclarationSyntax>()
                .Select(s => new
                {
                    name = s.Identifier.Text,
                    modifiers = GetModifiers(s.Modifiers)
                })
                .ToArray();

            var enums = root.DescendantNodes().OfType<CSS.EnumDeclarationSyntax>()
                .Select(e => new
                {
                    name = e.Identifier.Text,
                    modifiers = GetModifiers(e.Modifiers)
                })
                .ToArray();

            var methods = root.DescendantNodes().OfType<CSS.MethodDeclarationSyntax>()
                .Select(m =>
                {
                    var name = m.Identifier.Text;
                    var returnType = GetTypeName(m.ReturnType);
                    var parameters = FormatParameters(m.ParameterList);
                    var mods = GetModifiers(m.Modifiers);
                    return $"{mods} {name}({parameters}): {returnType}".Trim();
                })
                .Distinct()
                .ToArray();

            var properties = root.DescendantNodes().OfType<CSS.PropertyDeclarationSyntax>()
                .Select(p =>
                {
                    var mods = GetModifiers(p.Modifiers);
                    var name = p.Identifier.Text;
                    var type = GetTypeName(p.Type);
                    return $"{mods} {name}: {type}".Trim();
                })
                .Distinct()
                .ToArray();

            var fields = root.DescendantNodes().OfType<CSS.FieldDeclarationSyntax>()
                .SelectMany(f =>
                {
                    var mods = GetModifiers(f.Modifiers);
                    var type = f.Declaration.Type?.ToString() ?? "object";
                    return f.Declaration.Variables.Select(v => $"{mods} {v.Identifier.Text}: {type}".Trim());
                })
                .Distinct()
                .ToArray();

            var namespaces = root.DescendantNodes()
                .OfType<CSS.BaseNamespaceDeclarationSyntax>()
                .Select(n => n.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            var usings = root.Usings
                .Select(u => u.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            var dependencies = DependencyExtractor.Extract(filePath, "C#");

            // === Collect SQL usages from both the general extractor and the DB-wrapper helper ===
            List<SqlCommandExtractor.SqlUsage> extractUsages = new List<SqlCommandExtractor.SqlUsage>();
            List<SqlCommandExtractor.SqlUsage> wrapperUsages = new List<SqlCommandExtractor.SqlUsage>();
            try
            {
                extractUsages = SqlCommandExtractor.AnalyzeDocument(tree, model, filePath) ?? new List<SqlCommandExtractor.SqlUsage>();
            }
            catch
            {
                // non-fatal - continue without these usages
            }
            try
            {
                wrapperUsages = SqlCommandExtractor.AnalyzeDbWrapperCalls(root, model, filePath).ToList();
            }
            catch
            {
                // non-fatal - continue
            }

            // Merge and deduplicate usages (prefer entries with SqlText)
            var merged = new List<SqlCommandExtractor.SqlUsage>();
            var seen = new HashSet<string>();
            IEnumerable<SqlCommandExtractor.SqlUsage> all = extractUsages.Concat(wrapperUsages);
            foreach (var u in all.OrderByDescending(u => !string.IsNullOrEmpty(u.SqlText)).ThenBy(u => u.Line))
            {
                var key = $"{u.Kind}|{u.Line}|{(u.SqlText ?? "").Trim()}|{(u.RawSnippet ?? "").Trim()}";
                if (seen.Add(key))
                {
                    merged.Add(u);
                }
            }

            return new
            {
                file = Path.GetFileName(filePath),
                language = "C#",
                namespaces,
                usings,
                classes = classDetails,
                //interfaces,
                //structs,
                //enums,
                methods,
                //properties,
                //fields,
                dependencies,
                sql_usages = merged.Select(s => new {
                    file = Path.GetFileName(s.FilePath),
                    s.Namespace,
                    s.ClassName,
                    s.MethodName,
                    s.MethodSignature,
                    s.Line,
                    s.Kind,
                    s.SqlText,
                    s.CommandTypeIsStoredProcedure,
                    s.InferredStoredProcedures,
                    s.RawSnippet
                }).ToArray()
            };
        }
    }
}
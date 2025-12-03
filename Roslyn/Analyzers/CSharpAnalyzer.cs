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

            // Build IR for this file
            var ir = BuildIR(root, model, compilation, merged.ToList(), filePath);

            return new
            {
                file = Path.GetFileName(filePath),
                language = "C#",
                namespaces,
                //usings,
                classes = classDetails,
                //interfaces,
                //structs,
                //enums,
                methods,
                //properties,
                //fields,
                //dependencies,
                ir, // include IR here
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

        // Add this helper near the bottom of the file (inside the CSharpAnalyzer class)
        // It builds a simple, compact IR for the file's types/members and SQL usages.

        private static object BuildIR(CSS.CompilationUnitSyntax root, SemanticModel model, Compilation compilation, List<SqlCommandExtractor.SqlUsage> sqlUsages, string filePath)
        {
            string Modifiers(SyntaxTokenList mods) => string.Join(" ", mods.Select(m => m.Text)).Trim();

            Func<CSS.ParameterListSyntax?, object[]> FormatParams = (pList) =>
            {
                if (pList == null) return Array.Empty<object>();
                return pList.Parameters.Select(p => new
                {
                    name = p.Identifier.Text,
                    type = p.Type?.ToString() ?? "object",
                    defaultValue = p.Default?.Value?.ToString()
                }).ToArray();
            };

            var types = root.DescendantNodes().OfType<CSS.TypeDeclarationSyntax>()
                .Select(t =>
                {
                    var methods = t.Members.OfType<CSS.MethodDeclarationSyntax>()
                        .Select(m => new
                        {
                            name = m.Identifier.Text,
                            modifiers = Modifiers(m.Modifiers),
                            returnType = (m.ReturnType != null) ? m.ReturnType.ToString() : "void",
                            parameters = FormatParams(m.ParameterList)
                        })
                        .ToArray();

                    var properties = t.Members.OfType<CSS.PropertyDeclarationSyntax>()
                        .Select(p => new
                        {
                            name = p.Identifier.Text,
                            modifiers = Modifiers(p.Modifiers),
                            type = p.Type?.ToString() ?? "object"
                        })
                        .ToArray();

                    var fields = t.Members.OfType<CSS.FieldDeclarationSyntax>()
                        .SelectMany(f => f.Declaration.Variables.Select(v => new
                        {
                            name = v.Identifier.Text,
                            modifiers = Modifiers(f.Modifiers),
                            type = f.Declaration.Type?.ToString() ?? "object"
                        }))
                        .ToArray();

                    var baseTypes = (t is CSS.ClassDeclarationSyntax cd && cd.BaseList != null)
                        ? cd.BaseList.Types.Select(bt => bt.Type.ToString()).ToArray()
                        : (t is CSS.StructDeclarationSyntax sd && sd.BaseList != null)
                            ? sd.BaseList.Types.Select(bt => bt.Type.ToString()).ToArray()
                            : Array.Empty<string>();

                    // attach SQL usages for this type (by class name)
                    var typeName = t.Identifier.Text;
                    var sqlForType = sqlUsages
                        .Where(s => string.Equals(s.ClassName, typeName, StringComparison.OrdinalIgnoreCase))
                        .Select(s => new
                        {
                            s.Line,
                            s.Kind,
                            sql = s.SqlText,
                            s.CommandTypeIsStoredProcedure,
                            inferred = s.InferredStoredProcedures,
                            raw = s.RawSnippet
                        })
                        .ToArray();

                    return new
                    {
                        kind = t.Kind().ToString().Replace("DeclarationSyntax", ""), // "ClassDeclaration" -> "Class"
                        name = typeName,
                        namespaceName = t.Ancestors().OfType<CSS.BaseNamespaceDeclarationSyntax>().FirstOrDefault()?.Name?.ToString() ?? "",
                        modifiers = Modifiers(t.Modifiers),
                        baseTypes,
                        methods,
                        properties,
                        fields,
                        sql = sqlForType
                    };
                })
                .ToArray();

            var fileLevelSql = sqlUsages
                .Where(s => string.IsNullOrEmpty(s.ClassName))
                .Select(s => new
                {
                    s.FilePath,
                    s.Line,
                    s.Kind,
                    sql = s.SqlText,
                    s.CommandTypeIsStoredProcedure,
                    inferred = s.InferredStoredProcedures,
                    raw = s.RawSnippet
                })
                .ToArray();

            var ir = new
            {
                file = Path.GetFileName(filePath),
                path = filePath,
                namespaces = root.DescendantNodes().OfType<CSS.BaseNamespaceDeclarationSyntax>()
                                 .Select(n => n.Name?.ToString()).Where(s => !string.IsNullOrWhiteSpace(s)).Distinct().ToArray(),
                usings = root.Usings.Select(u => u.Name?.ToString()).Where(s => !string.IsNullOrWhiteSpace(s)).Distinct().ToArray(),
                types,
                file_level_sql = fileLevelSql
            };

            return ir;
        }
    }
}
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.VisualBasic;
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace Roslyn.Analyzers
{
    using VBS = Microsoft.CodeAnalysis.VisualBasic.Syntax;

    public static class VisualBasicAnalyzer
    {
        public static object Analyze(string code, string filePath)
        {
            // include filePath so tree.FilePath is populated (helps other extractors)
            var tree = VisualBasicSyntaxTree.ParseText(code, path: filePath);
            var root = (VBS.CompilationUnitSyntax)tree.GetCompilationUnitRoot();

            // build a small references list (match C# approach and try to include System.Data if present)
            var refs = new List<MetadataReference>
            {
                MetadataReference.CreateFromFile(typeof(object).Assembly.Location)
            };

            try
            {
                var sd = AppDomain.CurrentDomain.GetAssemblies()
                    .FirstOrDefault(a => a.GetName().Name.Equals("System.Data", StringComparison.OrdinalIgnoreCase)
                                      || a.GetName().Name.Equals("Microsoft.Data.SqlClient", StringComparison.OrdinalIgnoreCase));
                if (sd != null && !string.IsNullOrEmpty(sd.Location))
                    refs.Add(MetadataReference.CreateFromFile(sd.Location));
            }
            catch
            {
                // non-fatal
            }

            var compilation = VisualBasicCompilation.Create("VBAnalysis")
                .AddSyntaxTrees(tree)
                .AddReferences(refs);

            var model = compilation.GetSemanticModel(tree);

            // Helpers
            string GetModifiers(SyntaxTokenList mods) =>
                mods == default ? string.Empty : string.Join(" ", mods.Select(m => m.Text).Where(t => !string.IsNullOrWhiteSpace(t)));

            string FormatParameters(VBS.ParameterListSyntax? paramList)
            {
                if (paramList == null) return "";
                return string.Join(", ", paramList.Parameters.Select(p =>
                {
                    var name = p.Identifier.Identifier.Text;
                    var type = (p.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object";
                    return $"{name}: {type}";
                }));
            }

            // CLASSES
            var classes = root.DescendantNodes().OfType<VBS.ClassBlockSyntax>()
                .Select(cb =>
                {
                    var stmt = cb.ClassStatement;
                    var name = stmt.Identifier.Text;
                    var modifiers = GetModifiers(stmt.Modifiers);

                    string? baseType = null;
                    var inheritsClause = cb.Inherits.FirstOrDefault();
                    if (inheritsClause != null)
                    {
                        baseType = inheritsClause.Types.FirstOrDefault()?.ToString();
                    }

                    var interfaces = cb.Implements
                        .SelectMany(im => im.Types.Select(t => t.ToString()))
                        .Where(s => !string.IsNullOrWhiteSpace(s))
                        .ToArray();

                    var methods = cb.Members.OfType<VBS.MethodBlockSyntax>()
                        .Select(mb => mb.SubOrFunctionStatement.Identifier.Text)
                        .Concat(cb.Members.OfType<VBS.MethodStatementSyntax>().Select(ms => ms.Identifier.Text))
                        .Distinct()
                        .ToArray();

                    var props = cb.Members.OfType<VBS.PropertyStatementSyntax>()
                        .Select(p => p.Identifier.Text)
                        .ToArray();

                    return new
                    {
                        name,
                        modifiers,
                        baseType,
                        interfaces,
                        Methods = methods,
                        Properties = props
                    };
                })
                .ToArray();

            // Not currently used in output; keep commented unless needed later.
            /*
            var interfacesList = root.DescendantNodes().OfType<VBS.InterfaceBlockSyntax>()
                .Select(ib =>
                {
                    var stmt = ib.InterfaceStatement;
                    return new
                    {
                        name = stmt.Identifier.Text,
                        modifiers = GetModifiers(stmt.Modifiers)
                    };
                })
                .ToArray();

            var structs = root.DescendantNodes().OfType<VBS.StructureBlockSyntax>()
                .Select(sb =>
                {
                    var stmt = sb.StructureStatement;
                    return new
                    {
                        name = stmt.Identifier.Text,
                        modifiers = GetModifiers(stmt.Modifiers)
                    };
                })
                .ToArray();

            var enums = root.DescendantNodes().OfType<VBS.EnumBlockSyntax>()
                .Select(eb =>
                {
                    var stmt = eb.EnumStatement;
                    return new
                    {
                        name = stmt.Identifier.Text,
                        modifiers = GetModifiers(stmt.Modifiers)
                    };
                })
                .ToArray();
            */

            // METHODS - handle both MethodStatementSyntax (declarations) and MethodBlockSyntax bodies
            var methods = root.DescendantNodes()
                .Where(n => n is VBS.MethodStatementSyntax)
                .Cast<VBS.MethodStatementSyntax>()
                .Select(m =>
                {
                    var name = m.Identifier.Text;
                    var returnType = (m.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Void";
                    var parameters = FormatParameters(m.ParameterList);
                    var mods = GetModifiers(m.Modifiers);
                    return $"{mods} {name}({parameters}): {returnType}".Trim();
                })
                .Distinct()
                .ToArray();

            // Not currently used in output; duplicates IR/type-level details.
            /*
            var properties = root.DescendantNodes().OfType<VBS.PropertyStatementSyntax>()
                .Select(p =>
                {
                    var mods = GetModifiers(p.Modifiers);
                    var name = p.Identifier.Text;
                    var type = (p.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object";
                    return $"{mods} {name}: {type}".Trim();
                })
                .Distinct()
                .ToArray();

            var fields = root.DescendantNodes().OfType<VBS.FieldDeclarationSyntax>()
                .SelectMany(f => f.Declarators.SelectMany(d =>
                    d.Names.Select(n =>
                    {
                        var type = (d.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object";
                        var mods = GetModifiers(f.Modifiers);
                        var fieldStr = $"{mods} {n.Identifier.Text}: {type}".Trim();

                        bool isUIField = fieldStr.Contains("System.Windows.Forms")
                                      || fieldStr.Contains("System.ComponentModel")
                                      || fieldStr.StartsWith("WM_")
                                      || fieldStr.StartsWith("WS_")
                                      || fieldStr.StartsWith("SWP_");

                        return isUIField ? null : fieldStr;
                    })))
                .Where(f => f != null)
                .Distinct()
                .ToArray();
            */

            var namespaces = root.DescendantNodes()
                .OfType<VBS.NamespaceBlockSyntax>()
                .Select(n => n.NamespaceStatement.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            var imports = root.Imports
                .SelectMany(i => i.ImportsClauses)
                .OfType<VBS.SimpleImportsClauseSyntax>()
                .Select(c => c.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            // Not currently returned; keep disabled unless dependency output is needed.
            // var dependencies = DependencyExtractor.Extract(filePath, "VB");

            // === Collect SQL usages using SqlCommandExtractor (best-effort) ===
            List<SqlCommandExtractor.SqlUsage> extractUsages = new List<SqlCommandExtractor.SqlUsage>();
            List<SqlCommandExtractor.SqlUsage> wrapperUsages = new List<SqlCommandExtractor.SqlUsage>();

            try
            {
                extractUsages = SqlCommandExtractor.AnalyzeDocument(tree, model, filePath) ?? new List<SqlCommandExtractor.SqlUsage>();
            }
            catch
            {
                // non-fatal
            }

            try
            {
                wrapperUsages = SqlCommandExtractor.AnalyzeDbWrapperCalls(root, model, filePath).ToList();
            }
            catch
            {
                // non-fatal
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

            // Build VB IR
            var ir = BuildIR(root, model, compilation, merged.ToList(), filePath);

            // Discover API endpoints (best-effort, non-fatal)
            List<ApiEndpoint> apiEndpoints = new List<ApiEndpoint>();
            try
            {
                apiEndpoints = ApiEndpointAnalyzer.Analyze(root, filePath);
            }
            catch
            {
                // non-fatal: proceed without API endpoint data
            }

            return new
            {
                file = Path.GetFileName(filePath),
                language = "VB",
                namespaces,
                imports,
                classes,
                methods,
                ir,
                api_endpoints = apiEndpoints.Count > 0
                    ? apiEndpoints.Select(e => new
                    {
                        e.Kind,
                        e.ControllerOrServiceName,
                        e.OperationName,
                        e.FilePath,
                        e.Route,
                        e.HttpMethods,
                        parameters = e.Parameters.Select(p => new { p.Name, p.Type }).ToArray(),
                        e.ReturnType,
                        e.Evidence
                    }).ToArray()
                    : null,
                sql_usages = merged.Select(s => new
                {
                    file = Path.GetFileName(s.FilePath),
                    s.Namespace,
                    s.ClassName,
                    s.MethodName,
                    s.MethodSignature,
                    // s.Line, // keep commented out unless you want trace/debug detail
                    s.Kind,
                    s.SqlText,
                    s.CommandTypeIsStoredProcedure,
                    s.InferredStoredProcedures,
                    s.RawSnippet
                }).ToArray()

                // Optional outputs kept disabled to reduce noise:
                // interfaces = interfacesList,
                // structs,
                // enums,
                // properties,
                // fields,
                // dependencies
            };
        }

        // Build a compact IR for VB files.
        private static object BuildIR(
            VBS.CompilationUnitSyntax root,
            SemanticModel model,
            Compilation compilation,
            List<SqlCommandExtractor.SqlUsage> sqlUsages,
            string filePath)
        {
            string Modifiers(SyntaxTokenList mods) => string.Join(" ", mods.Select(m => m.Text)).Trim();

            Func<VBS.ParameterListSyntax?, object[]> FormatParams = (pList) =>
            {
                if (pList == null) return Array.Empty<object>();
                return pList.Parameters.Select(p => new
                {
                    name = p.Identifier.Identifier.Text,
                    type = (p.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object",
                    defaultValue = p.Default?.Value?.ToString()
                }).ToArray();
            };

            var types = new List<object>();

            // Classes
            foreach (var cb in root.DescendantNodes().OfType<VBS.ClassBlockSyntax>())
            {
                var stmt = cb.ClassStatement;
                var typeName = stmt.Identifier.Text;
                var ns = cb.Ancestors().OfType<VBS.NamespaceBlockSyntax>().FirstOrDefault()?.NamespaceStatement.Name?.ToString() ?? "";

                var methods = cb.Members.OfType<VBS.MethodBlockSyntax>()
                    .Select(mb => new
                    {
                        name = mb.SubOrFunctionStatement.Identifier.Text,
                        modifiers = Modifiers(mb.SubOrFunctionStatement.Modifiers),
                        returnType = (mb.SubOrFunctionStatement.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Void",
                        parameters = FormatParams(mb.SubOrFunctionStatement.ParameterList)
                    })
                    .Concat(cb.Members.OfType<VBS.MethodStatementSyntax>().Select(ms => new
                    {
                        name = ms.Identifier.Text,
                        modifiers = Modifiers(ms.Modifiers),
                        returnType = (ms.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Void",
                        parameters = FormatParams(ms.ParameterList)
                    }))
                    .ToArray();

                var properties = cb.Members.OfType<VBS.PropertyStatementSyntax>()
                    .Select(p => new
                    {
                        name = p.Identifier.Text,
                        modifiers = Modifiers(p.Modifiers),
                        type = (p.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object"
                    })
                    .ToArray();

                var fields = cb.Members.OfType<VBS.FieldDeclarationSyntax>()
                    .SelectMany(f => f.Declarators.SelectMany(d => d.Names.Select(n => new
                    {
                        name = n.Identifier.Text,
                        modifiers = Modifiers(f.Modifiers),
                        type = (d.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object"
                    })))
                    .ToArray();

                var baseTypes = cb.Inherits
                    .SelectMany(i => i.Types)
                    .Select(t => t.ToString())
                    .ToArray();

                // Optional SQL grouping by type; currently not returned to keep payload small.
                /*
                var sqlForType = sqlUsages
                    .Where(s => string.Equals(s.ClassName, typeName, StringComparison.OrdinalIgnoreCase))
                    .Select(s => new
                    {
                        // s.Line,
                        s.Kind,
                        sql = s.SqlText,
                        s.CommandTypeIsStoredProcedure,
                        inferred = s.InferredStoredProcedures,
                        raw = s.RawSnippet
                    })
                    .ToArray();
                */

                types.Add(new
                {
                    kind = "Class",
                    name = typeName,
                    namespaceName = ns,
                    modifiers = Modifiers(stmt.Modifiers),
                    baseTypes,
                    methods,
                    properties,
                    fields

                    // sql = sqlForType
                });
            }

            // Structures
            foreach (var sb in root.DescendantNodes().OfType<VBS.StructureBlockSyntax>())
            {
                var stmt = sb.StructureStatement;
                var name = stmt.Identifier.Text;

                var methods = sb.Members.OfType<VBS.MethodStatementSyntax>()
                    .Select(m => new
                    {
                        name = m.Identifier.Text
                    })
                    .ToArray();

                types.Add(new
                {
                    kind = "Struct",
                    name,
                    methods
                });
            }

            // Interfaces
            foreach (var ib in root.DescendantNodes().OfType<VBS.InterfaceBlockSyntax>())
            {
                var stmt = ib.InterfaceStatement;
                var name = stmt.Identifier.Text;

                var methodsIface = ib.Members.OfType<VBS.MethodStatementSyntax>()
                    .Select(m => new
                    {
                        name = m.Identifier.Text
                    })
                    .ToArray();

                types.Add(new
                {
                    kind = "Interface",
                    name,
                    methods = methodsIface
                });
            }

            // Enums
            foreach (var eb in root.DescendantNodes().OfType<VBS.EnumBlockSyntax>())
            {
                var stmt = eb.EnumStatement;
                var name = stmt.Identifier.Text;

                var members = eb.Members.OfType<VBS.EnumMemberDeclarationSyntax>()
                    .Select(m => m.Identifier.Text)
                    .ToArray();

                types.Add(new
                {
                    kind = "Enum",
                    name,
                    members
                });
            }

            // Optional file-level SQL; currently not returned to keep payload small.
            /*
            var fileLevelSql = sqlUsages
                .Where(s => string.IsNullOrEmpty(s.ClassName))
                .Select(s => new
                {
                    s.FilePath,
                    // s.Line,
                    s.Kind,
                    sql = s.SqlText,
                    s.CommandTypeIsStoredProcedure,
                    inferred = s.InferredStoredProcedures,
                    raw = s.RawSnippet
                })
                .ToArray();
            */

            var ir = new
            {
                file = Path.GetFileName(filePath),
                path = filePath,
                namespaces = root.DescendantNodes()
                    .OfType<VBS.NamespaceBlockSyntax>()
                    .Select(n => n.NamespaceStatement.Name?.ToString())
                    .Where(s => !string.IsNullOrWhiteSpace(s))
                    .Distinct()
                    .ToArray(),
                types = types.ToArray()

                // imports = ...
                // file_level_sql = fileLevelSql
            };

            return ir;
        }
    }
}
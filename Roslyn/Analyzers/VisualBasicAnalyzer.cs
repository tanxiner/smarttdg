using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.VisualBasic;
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
            var tree = VisualBasicSyntaxTree.ParseText(code);
            var root = (VBS.CompilationUnitSyntax)tree.GetCompilationUnitRoot();

            var compilation = VisualBasicCompilation.Create("VBAnalysis")
                .AddSyntaxTrees(tree)
                .AddReferences(MetadataReference.CreateFromFile(typeof(object).Assembly.Location));

            var model = compilation.GetSemanticModel(tree);

            // Helpers
            string GetTypeName(VBS.TypeSyntax? type) => type?.ToString() ?? "Object";

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

            // CLASSES (use ClassBlockSyntax to access Inherits/Implements properly)
            var classes = root.DescendantNodes().OfType<VBS.ClassBlockSyntax>()
                .Select(cb =>
                {
                    var stmt = cb.ClassStatement;
                    var name = stmt.Identifier.Text;
                    var modifiers = GetModifiers(stmt.Modifiers);

                    // base type: check Inherits clause(s)
                    string? baseType = null;
                    var inheritsClause = cb.Inherits.FirstOrDefault();
                    if (inheritsClause != null)
                    {
                        baseType = inheritsClause.Types.FirstOrDefault()?.ToString();
                    }

                    // implements: collect all implemented interface type names
                    var interfaces = cb.Implements
                        .SelectMany(im => im.Types.Select(t => t.ToString()))
                        .Where(s => !string.IsNullOrWhiteSpace(s))
                        .ToArray();

                    return new
                    {
                        name,
                        modifiers,
                        baseType,
                        interfaces
                    };
                })
                .ToArray();

            // INTERFACES (InterfaceBlockSyntax)
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

            // STRUCTS (StructureBlockSyntax)
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

            // ENUMS (EnumBlockSyntax)
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

            // PROPERTIES - PropertyStatementSyntax has AsClause; use SimpleAsClauseSyntax to access Type
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

            // FIELDS - FieldDeclarationSyntax -> Declarators -> Names & AsClause
            var fields = root.DescendantNodes().OfType<VBS.FieldDeclarationSyntax>()
             .SelectMany(f => f.Declarators.SelectMany(d =>
                 d.Names.Select(n =>
                 {
                     var type = (d.AsClause as VBS.SimpleAsClauseSyntax)?.Type?.ToString() ?? "Object";
                     var mods = GetModifiers(f.Modifiers);
                     var fieldStr = $"{mods} {n.Identifier.Text}: {type}".Trim();
                     // Skip fields whose type contains "System.Windows.Forms" OR "System.ComponentModel"
                     bool isUIField = fieldStr.Contains("System.Windows.Forms") || fieldStr.Contains("System.ComponentModel") ||
                     fieldStr.StartsWith("WM_") || fieldStr.StartsWith("WS_") || fieldStr.StartsWith("SWP_") || fieldStr.Contains("System.Globalization.CultureInfo")
                     || fieldStr.Contains("HWND_") || fieldStr.Contains("hHwnd")|| fieldStr.Contains("System.Resources.ResourceManager")
                     || fieldStr.Contains("System.Windows.Forms.Panel") || fieldStr.Contains("System") || fieldStr.Contains("Windows") ||
                     fieldStr.Contains("System.Windows.Forms.RadioButton") || fieldStr.Contains("System.Windows.Forms.Label") || fieldStr.Contains("System.Windows.Forms.TextBox")
                     || fieldStr.Contains("System.Windows.Forms.Button") || fieldStr.Contains("System.ComponentModel.IContainer") || fieldStr.Contains("System.Windows.Forms.Label");

                     return isUIField ? null : fieldStr;
                 })))
             .Where(f => f != null)
             .Distinct()
             .ToArray();


            // NAMESPACES
            var namespaces = root.Members
                .OfType<VBS.NamespaceBlockSyntax>()
                .Select(n => n.NamespaceStatement.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            // IMPORTS
            var imports = root.Imports
                .SelectMany(i => i.ImportsClauses)
                .OfType<VBS.SimpleImportsClauseSyntax>()
                .Select(c => c.Name?.ToString())
                .Where(s => !string.IsNullOrWhiteSpace(s))
                .Distinct()
                .ToArray();

            var dependencies = DependencyExtractor.Extract(filePath, "VB");

            return new
            {
                file = Path.GetFileName(filePath),
                language = "VB",
                namespaces,
                imports,
                classes,
                //interfaces = interfacesList,
                //structs,
                //enums,
                methods,
                //properties,
                //fields,
                dependencies
            };
        }
    }
}

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.CSharp;

namespace Roslyn.Analyzers
{
    // Partial helper to detect DB wrapper patterns like:
    //   string spname = "sp_TAMS_GetTarByTarId";
    //   object[] parms = { ... };
    //   return db.Read(spname, MakeTar, parms).FirstOrDefault();
    //
    // Best-effort:
    // - tracks local/field/property string variables initialized with literal/const values
    // - tracks simple string assignments
    // - looks for likely DB wrapper invocations that pass those values
    public static partial class SqlCommandExtractor
    {
        public static IEnumerable<SqlUsage> AnalyzeDbWrapperCalls(SyntaxNode root, SemanticModel semanticModel, string filePath)
        {
            var results = new List<SqlUsage>();
            if (root == null || semanticModel == null) return results;

            // Map tracked variable symbol -> resolved string value
            var literalVarValues = new Dictionary<ISymbol, string>(SymbolEqualityComparer.Default);

            // 1) Find variable declarations with string initializer
            var varDecls = root.DescendantNodes().OfType<VariableDeclaratorSyntax>();
            foreach (var decl in varDecls)
            {
                try
                {
                    var declared = semanticModel.GetDeclaredSymbol(decl);
                    if (declared == null) continue;

                    ITypeSymbol? varType = null;
                    if (declared is ILocalSymbol ls) varType = ls.Type;
                    else if (declared is IFieldSymbol fs) varType = fs.Type;
                    else if (declared is IPropertySymbol ps) varType = ps.Type;

                    if (varType == null || varType.SpecialType != SpecialType.System_String) continue;

                    var init = decl.Initializer?.Value;
                    if (init == null) continue;

                    var resolved = TryResolveStringExpression(init, semanticModel);
                    if (!string.IsNullOrEmpty(resolved))
                        literalVarValues[declared] = resolved;
                }
                catch
                {
                    // best-effort
                }
            }

            // 2) Pick up simple assignments: spname = "sp_xxx";
            var assignments = root.DescendantNodes().OfType<AssignmentExpressionSyntax>();
            foreach (var a in assignments)
            {
                try
                {
                    var leftSym = semanticModel.GetSymbolInfo(a.Left).Symbol;
                    if (leftSym == null) continue;

                    ITypeSymbol? leftType = null;
                    if (leftSym is ILocalSymbol lls) leftType = lls.Type;
                    else if (leftSym is IFieldSymbol lfs) leftType = lfs.Type;
                    else if (leftSym is IPropertySymbol lps) leftType = lps.Type;

                    if (leftType == null || leftType.SpecialType != SpecialType.System_String) continue;

                    var resolved = TryResolveStringExpression(a.Right, semanticModel);
                    if (!string.IsNullOrEmpty(resolved))
                        literalVarValues[leftSym] = resolved;
                }
                catch
                {
                    // ignore
                }
            }

            // 3) Find wrapper invocations using tracked string variables
            var invocations = root.DescendantNodes().OfType<InvocationExpressionSyntax>();
            foreach (var inv in invocations)
            {
                try
                {
                    string? invokedName = null;

                    if (inv.Expression is MemberAccessExpressionSyntax mae)
                        invokedName = mae.Name.Identifier.Text;
                    else
                    {
                        var sym = semanticModel.GetSymbolInfo(inv).Symbol as IMethodSymbol;
                        invokedName = sym?.Name;
                    }

                    if (string.IsNullOrWhiteSpace(invokedName)) continue;

                    var low = invokedName.ToLowerInvariant();
                    if (!(low.Contains("read") || low.Contains("update") || low.Contains("query") || low.Contains("execute")))
                        continue;

                    foreach (var arg in inv.ArgumentList.Arguments)
                    {
                        var argSym = semanticModel.GetSymbolInfo(arg.Expression).Symbol;
                        if (argSym == null) continue;

                        if (!literalVarValues.TryGetValue(argSym, out var sqlText)) continue;

                        var methodSym = GetEnclosingMethodSymbol(inv, semanticModel);

                        var usage = new SqlUsage
                        {
                            FilePath = filePath,
                            Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
                            ClassName = methodSym?.ContainingType?.Name ?? Path.GetFileNameWithoutExtension(filePath),
                            MethodName = methodSym?.Name ?? "(top-level)",
                            MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
                            // Line = inv.GetLocation().GetLineSpan().StartLinePosition.Line + 1,
                            Kind = "DbWrapperCall",
                            SqlText = sqlText,
                            CommandTypeIsStoredProcedure = false,
                            RawSnippet = TrimSnippet(inv.ToString())
                        };

                        PopulateInferredProcs(usage);
                        results.Add(usage);
                        break; // one match per invocation is enough
                    }
                }
                catch
                {
                    // ignore and continue
                }
            }

            return results;
        }
    }
}
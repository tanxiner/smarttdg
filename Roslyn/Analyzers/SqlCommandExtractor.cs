using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace Roslyn.Analyzers
{
    /// <summary>
    /// Analyze a SyntaxTree + SemanticModel to extract SQL usages mapped to method symbols.
    /// Supports:
    ///  - new SqlCommand("...") constructor string argument
    ///  - cmd.CommandText = "..."
    ///  - assignments of CommandType = StoredProcedure
    ///  - some Dapper/EF invocation patterns (best-effort)
    /// Uses semanticModel.GetConstantValue(...) to extract compile-time constants.
    /// </summary>
    public static partial class SqlCommandExtractor
    {
        private static readonly Regex ProcNameHeuristic =
            new Regex(@"^\[?[A-Za-z0-9_\.]+\]?$", RegexOptions.Compiled);

        private const int MaxRawSnippetLength = 500;

        public class SqlUsage
        {
            public string FilePath { get; set; } = "";
            public string Namespace { get; set; } = "";
            public string ClassName { get; set; } = "";
            public string MethodName { get; set; } = "";
            public string MethodSignature { get; set; } = "";
            public int Line { get; set; }
            public string Kind { get; set; } = "";
            public string? SqlText { get; set; } = null;
            public bool CommandTypeIsStoredProcedure { get; set; } = false;
            public List<string> InferredStoredProcedures { get; set; } = new List<string>();
            public string RawSnippet { get; set; } = "";
        }

        /// <summary>
        /// Analyze a single document and return found SQL usages.
        /// </summary>
        public static List<SqlUsage> AnalyzeDocument(SyntaxTree tree, SemanticModel semanticModel, string filePath)
        {
            var results = new List<SqlUsage>();
            var root = tree.GetRoot();

            // 1) Find object creations of SqlCommand e.g. new SqlCommand("text", ...)
            var objectCreations = root.DescendantNodes().OfType<ObjectCreationExpressionSyntax>();
            foreach (var oc in objectCreations)
            {
                try
                {
                    var typeInfo = semanticModel.GetTypeInfo(oc);
                    var typeSymbol = typeInfo.Type;
                    if (typeSymbol == null) continue;

                    var fullName = typeSymbol.ToDisplayString();

                    bool isSqlCommand =
                        string.Equals(fullName, "System.Data.SqlClient.SqlCommand", StringComparison.OrdinalIgnoreCase) ||
                        string.Equals(fullName, "Microsoft.Data.SqlClient.SqlCommand", StringComparison.OrdinalIgnoreCase) ||
                        string.Equals(typeSymbol.Name, "SqlCommand", StringComparison.OrdinalIgnoreCase);

                    if (!isSqlCommand) continue;

                    string? resolved = TryResolveStringExpression(
                        oc.ArgumentList?.Arguments.FirstOrDefault()?.Expression,
                        semanticModel);

                    var location = oc.GetLocation().GetLineSpan();
                    var methodSym = GetEnclosingMethodSymbol(oc, semanticModel);

                    var usage = new SqlUsage
                    {
                        FilePath = filePath,
                        Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
                        ClassName = methodSym?.ContainingType?.Name ?? "",
                        MethodName = methodSym?.Name ?? "(top-level)",
                        MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
                        Line = location.StartLinePosition.Line + 1,
                        Kind = "SqlCommandCtor",
                        SqlText = resolved,
                        RawSnippet = TrimSnippet(oc.ToString())
                    };

                    PopulateInferredProcs(usage);
                    results.Add(usage);
                }
                catch
                {
                    // best-effort
                }
            }

            // 2) Find assignments to .CommandText and .CommandType
            var assignments = root.DescendantNodes().OfType<AssignmentExpressionSyntax>();
            foreach (var a in assignments)
            {
                try
                {
                    if (a.Left is MemberAccessExpressionSyntax mae)
                    {
                        var memberName = mae.Name.Identifier.Text;

                        if (string.Equals(memberName, "CommandText", StringComparison.OrdinalIgnoreCase))
                        {
                            var resolved = TryResolveStringExpression(a.Right, semanticModel);
                            var loc = a.GetLocation().GetLineSpan();
                            var methodSym = GetEnclosingMethodSymbol(a, semanticModel);

                            var usage = new SqlUsage
                            {
                                FilePath = filePath,
                                Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
                                ClassName = methodSym?.ContainingType?.Name ?? "",
                                MethodName = methodSym?.Name ?? "(top-level)",
                                MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
                                Line = loc.StartLinePosition.Line + 1,
                                Kind = "CommandTextAssignment",
                                SqlText = resolved,
                                RawSnippet = TrimSnippet(a.ToString())
                            };

                            PopulateInferredProcs(usage);
                            results.Add(usage);
                        }
                        else if (string.Equals(memberName, "CommandType", StringComparison.OrdinalIgnoreCase))
                        {
                            var rightText = a.Right.ToString();
                            bool isStoredProc = rightText.IndexOf("StoredProcedure", StringComparison.OrdinalIgnoreCase) >= 0;

                            if (isStoredProc)
                            {
                                var loc = a.GetLocation().GetLineSpan();
                                var methodSym = GetEnclosingMethodSymbol(a, semanticModel);

                                var usage = new SqlUsage
                                {
                                    FilePath = filePath,
                                    Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
                                    ClassName = methodSym?.ContainingType?.Name ?? "",
                                    MethodName = methodSym?.Name ?? "(top-level)",
                                    MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
                                    Line = loc.StartLinePosition.Line + 1,
                                    Kind = "CommandTypeAssignment",
                                    SqlText = null,
                                    CommandTypeIsStoredProcedure = true,
                                    RawSnippet = TrimSnippet(a.ToString())
                                };

                                results.Add(usage);
                            }
                        }
                    }
                }
                catch
                {
                    // ignore
                }
            }

            // 3) Invocation patterns for Dapper/EF (best-effort)
            var invocations = root.DescendantNodes().OfType<InvocationExpressionSyntax>();
            foreach (var inv in invocations)
            {
                try
                {
                    var sym = semanticModel.GetSymbolInfo(inv).Symbol as IMethodSymbol;
                    bool isDapper = false;
                    bool isEF = false;
                    bool looksDatabaseLike = false;

                    if (sym != null)
                    {
                        var methodName = sym.Name;
                        var owner = sym.ContainingType?.ToDisplayString();

                        isDapper = owner != null && owner.IndexOf("Dapper", StringComparison.OrdinalIgnoreCase) >= 0;
                        isEF = owner != null &&
                               (owner.IndexOf("EntityFramework", StringComparison.OrdinalIgnoreCase) >= 0 ||
                                owner.IndexOf("Microsoft.EntityFrameworkCore", StringComparison.OrdinalIgnoreCase) >= 0);

                        looksDatabaseLike =
                            isDapper ||
                            isEF ||
                            methodName.IndexOf("Query", StringComparison.OrdinalIgnoreCase) >= 0 ||
                            methodName.IndexOf("Execute", StringComparison.OrdinalIgnoreCase) >= 0 ||
                            methodName.IndexOf("FromSql", StringComparison.OrdinalIgnoreCase) >= 0;
                    }
                    else
                    {
                        var exprText = inv.Expression.ToString();
                        looksDatabaseLike =
                            exprText.IndexOf("Query", StringComparison.OrdinalIgnoreCase) >= 0 ||
                            exprText.IndexOf("Execute", StringComparison.OrdinalIgnoreCase) >= 0 ||
                            exprText.IndexOf("FromSql", StringComparison.OrdinalIgnoreCase) >= 0;
                    }

                    if (!looksDatabaseLike) continue;

                    string? resolved = null;
                    bool commandTypeSP = false;

                    foreach (var arg in inv.ArgumentList.Arguments)
                    {
                        if (arg.NameColon != null &&
                            arg.NameColon.Name.Identifier.Text.IndexOf("commandType", StringComparison.OrdinalIgnoreCase) >= 0)
                        {
                            if (arg.Expression.ToString().IndexOf("StoredProcedure", StringComparison.OrdinalIgnoreCase) >= 0)
                                commandTypeSP = true;
                        }

                        if (resolved == null)
                        {
                            resolved = TryResolveStringExpression(arg.Expression, semanticModel);
                            if (!string.IsNullOrEmpty(resolved))
                                break;
                        }
                    }

                    var loc = inv.GetLocation().GetLineSpan();
                    var methodSym = GetEnclosingMethodSymbol(inv, semanticModel);

                    if (!string.IsNullOrEmpty(resolved) || commandTypeSP)
                    {
                        var usage = new SqlUsage
                        {
                            FilePath = filePath,
                            Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
                            ClassName = methodSym?.ContainingType?.Name ?? "",
                            MethodName = methodSym?.Name ?? "(top-level)",
                            MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
                            Line = loc.StartLinePosition.Line + 1,
                            Kind = isDapper ? "DapperInvocation" : isEF ? "EFInvocation" : "DbInvocation",
                            SqlText = resolved,
                            CommandTypeIsStoredProcedure = commandTypeSP,
                            RawSnippet = TrimSnippet(inv.ToString())
                        };

                        PopulateInferredProcs(usage);
                        results.Add(usage);
                    }
                }
                catch
                {
                    // ignore
                }
            }

            return results;
        }

        /// <summary>
        /// Try to resolve string expressions:
        /// - literal string
        /// - constant field or const variable
        /// - simple binary concatenation with constant operands
        /// - interpolated string with constant parts only
        /// Otherwise returns null.
        /// </summary>
        private static string? TryResolveStringExpression(ExpressionSyntax? expr, SemanticModel semanticModel)
        {
            if (expr == null) return null;

            var constVal = semanticModel.GetConstantValue(expr);
            if (constVal.HasValue && constVal.Value is string s)
                return s;

            if (expr is LiteralExpressionSyntax les && les.IsKind(SyntaxKind.StringLiteralExpression))
            {
                return les.Token.ValueText;
            }

            if (expr is InterpolatedStringExpressionSyntax interpolated)
            {
                var parts = new List<string>();
                bool allConstant = true;

                foreach (var content in interpolated.Contents)
                {
                    if (content is InterpolatedStringTextSyntax text)
                    {
                        parts.Add(text.TextToken.ValueText);
                    }
                    else if (content is InterpolationSyntax interp)
                    {
                        var innerConst = semanticModel.GetConstantValue(interp.Expression);
                        if (innerConst.HasValue && innerConst.Value is string ivs)
                        {
                            parts.Add(ivs);
                        }
                        else if (innerConst.HasValue && innerConst.Value != null)
                        {
                            parts.Add(innerConst.Value.ToString() ?? "");
                        }
                        else
                        {
                            allConstant = false;
                            break;
                        }
                    }
                }

                if (allConstant)
                    return string.Concat(parts);
            }

            if (expr is BinaryExpressionSyntax bin && bin.IsKind(SyntaxKind.AddExpression))
            {
                var left = TryResolveStringExpression(bin.Left, semanticModel);
                var right = TryResolveStringExpression(bin.Right, semanticModel);
                if (left != null && right != null)
                    return string.Concat(left, right);
            }

            var symbol = semanticModel.GetSymbolInfo(expr).Symbol;
            if (symbol is IFieldSymbol fsym && fsym.IsConst && fsym.HasConstantValue && fsym.ConstantValue is string fsv)
                return fsv;

            if (symbol is ILocalSymbol lsym && lsym.HasConstantValue && lsym.ConstantValue is string lsv)
                return lsv;

            return null;
        }

        private static void PopulateInferredProcs(SqlUsage usage)
        {
            if (string.IsNullOrEmpty(usage.SqlText)) return;

            var s = usage.SqlText.Trim();

            var execMatch = Regex.Match(
                s,
                @"\bEXEC(?:UTE)?\b\s+([\[\]A-Za-z0-9_\.\$]+)",
                RegexOptions.IgnoreCase);

            if (execMatch.Success)
            {
                var proc = execMatch.Groups[1].Value.Trim().Trim('\'', '"');
                AddProc(usage, proc);
                return;
            }

            var compact = Regex.Replace(s, @"\s+", " ").Trim();
            if (compact.Length < 200 &&
                ProcNameHeuristic.IsMatch(compact) &&
                !Regex.IsMatch(compact, @"\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|FROM|WHERE|JOIN|VALUES|SET)\b", RegexOptions.IgnoreCase))
            {
                AddProc(usage, compact);
            }
        }

        private static void AddProc(SqlUsage usage, string proc)
        {
            var cleaned = proc.Replace("[", "").Replace("]", "");
            if (!string.IsNullOrWhiteSpace(cleaned) &&
                !usage.InferredStoredProcedures.Contains(cleaned, StringComparer.OrdinalIgnoreCase))
            {
                usage.InferredStoredProcedures.Add(cleaned);
            }
        }

        private static IMethodSymbol? GetEnclosingMethodSymbol(SyntaxNode node, SemanticModel semanticModel)
        {
            var methodDecl = node.AncestorsAndSelf().OfType<MethodDeclarationSyntax>().FirstOrDefault();
            if (methodDecl != null)
            {
                var sym = semanticModel.GetDeclaredSymbol(methodDecl) as IMethodSymbol;
                if (sym != null) return sym;
            }

            var localFunc = node.AncestorsAndSelf().OfType<LocalFunctionStatementSyntax>().FirstOrDefault();
            if (localFunc != null)
            {
                var sym = semanticModel.GetDeclaredSymbol(localFunc) as IMethodSymbol;
                if (sym != null) return sym;
            }

            var ctor = node.AncestorsAndSelf().OfType<ConstructorDeclarationSyntax>().FirstOrDefault();
            if (ctor != null)
            {
                var sym = semanticModel.GetDeclaredSymbol(ctor) as IMethodSymbol;
                if (sym != null) return sym;
            }

            var sym2 = semanticModel.GetEnclosingSymbol(node.SpanStart);
            return sym2 as IMethodSymbol;
        }

        private static string TrimSnippet(string? text)
        {
            if (string.IsNullOrWhiteSpace(text)) return "";
            var normalized = Regex.Replace(text, @"\s+", " ").Trim();
            return normalized.Length <= MaxRawSnippetLength
                ? normalized
                : normalized.Substring(0, MaxRawSnippetLength) + "...";
        }
    }
}
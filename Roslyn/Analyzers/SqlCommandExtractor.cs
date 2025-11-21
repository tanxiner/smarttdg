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
	/// Uses semanticModel.GetConstantValue(...) to extract compile-time constants (consts / literal folding).
	/// </summary>
	public static partial class SqlCommandExtractor
	{
		// Simple stored-proc heuristic
		private static readonly Regex ProcNameHeuristic = new Regex(@"^\[?[A-Za-z0-9_\.]+\]?$", RegexOptions.Compiled);

		public class SqlUsage
		{
			public string FilePath { get; set; }
			public string Namespace { get; set; }
			public string ClassName { get; set; }
			public string MethodName { get; set; }
			public string MethodSignature { get; set; }
			public int Line { get; set; }
			public string Kind { get; set; }           // "SqlCommandCtor", "CommandTextAssignment", "DapperInvocation", "EFInvocation"
			public string SqlText { get; set; }        // resolved text if available (literal/const), else null
			public bool CommandTypeIsStoredProcedure { get; set; } = false;
			public List<string> InferredStoredProcedures { get; set; } = new List<string>();
			public string RawSnippet { get; set; }
		}

		/// <summary>
		/// Analyze a single document (text and semantic model) and return found SQL usages.
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

					var fullName = typeSymbol.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat);
					// accept System.Data.SqlClient.SqlCommand or Microsoft.Data.SqlClient.SqlCommand
					if (!fullName.EndsWith("SqlCommand", StringComparison.OrdinalIgnoreCase)) continue;

					// look for first argument that is a string expression
					string resolved = TryResolveStringExpression(oc.ArgumentList?.Arguments.FirstOrDefault()?.Expression, semanticModel);

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
						RawSnippet = oc.ToString()
					};

					PopulateInferredProcs(usage);
					results.Add(usage);
				}
				catch
				{
					// continue on errors - best-effort
				}
			}

			// 2) Find assignments to .CommandText and .CommandType
			var assignments = root.DescendantNodes().OfType<AssignmentExpressionSyntax>();
			foreach (var a in assignments)
			{
				try
				{
					// left side could be member access like cmd.CommandText
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
								RawSnippet = a.ToString()
							};
							PopulateInferredProcs(usage);
							results.Add(usage);
						}
						else if (string.Equals(memberName, "CommandType", StringComparison.OrdinalIgnoreCase))
						{
							// check if right side is CommandType.StoredProcedure
							var rightText = a.Right.ToString();
							bool isStoredProc = false;
							// check enum constant textually if symbol not resolvable
							if (rightText.IndexOf("StoredProcedure", StringComparison.OrdinalIgnoreCase) >= 0)
								isStoredProc = true;
							// also inspect constant value
							var constVal = semanticModel.GetConstantValue(a.Right);
							if (constVal.HasValue)
							{
								// not much to do here but mark stored proc if rightText matches
							}

							if (isStoredProc)
							{
								var loc = a.GetLocation().GetLineSpan();
								var methodSym = GetEnclosingMethodSymbol(a, semanticModel);
								// mark an entry indicating commandtype assignment (without sql text)
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
									RawSnippet = a.ToString()
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

			// 3) Invocation patterns for Dapper/EF (best-effort): find invocation expressions with string literal first arg or named arg "sql"
			var invocations = root.DescendantNodes().OfType<InvocationExpressionSyntax>();
			foreach (var inv in invocations)
			{
				try
				{
					var sym = semanticModel.GetSymbolInfo(inv).Symbol as IMethodSymbol;
					if (sym == null)
					{
						// try to use expression text to match common names
						var exprText = inv.Expression.ToString();
						if (exprText.IndexOf("Query", StringComparison.OrdinalIgnoreCase) >= 0 ||
							exprText.IndexOf("Execute", StringComparison.OrdinalIgnoreCase) >= 0 ||
							exprText.IndexOf("FromSql", StringComparison.OrdinalIgnoreCase) >= 0)
						{
							// attempt to extract string literal arg
						}
					}
					else
					{
						var methodName = sym.Name;
						var owner = sym.ContainingType?.ToDisplayString();
						bool isDapper = owner != null && owner.IndexOf("Dapper", StringComparison.OrdinalIgnoreCase) >= 0;
						bool isEF = owner != null && (owner.IndexOf("EntityFramework", StringComparison.OrdinalIgnoreCase) >= 0 ||
													   owner.IndexOf("Microsoft.EntityFrameworkCore", StringComparison.OrdinalIgnoreCase) >= 0);
						if (isDapper || isEF || methodName.IndexOf("Query", StringComparison.OrdinalIgnoreCase) >= 0 || methodName.IndexOf("Execute", StringComparison.OrdinalIgnoreCase) >= 0 || methodName.IndexOf("FromSql", StringComparison.OrdinalIgnoreCase) >= 0)
						{
							// search arguments for a string expression or for named argument commandType: CommandType.StoredProcedure
							string resolved = null;
							bool commandTypeSP = false;
							foreach (var arg in inv.ArgumentList.Arguments)
							{
								// named argument like commandType: CommandType.StoredProcedure
								if (arg.NameColon != null && arg.NameColon.Name.Identifier.Text.IndexOf("commandType", StringComparison.OrdinalIgnoreCase) >= 0)
								{
									if (arg.Expression.ToString().IndexOf("StoredProcedure", StringComparison.OrdinalIgnoreCase) >= 0)
										commandTypeSP = true;
								}
								// first string arg or named "sql"
								if (resolved == null)
								{
									// check literal or const
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
									RawSnippet = inv.ToString()
								};
								PopulateInferredProcs(usage);
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

			// 4) Consolidate: if there are CommandTypeAssignment entries in same method but without SqlText, try to attach storedproc inferences via nearby CommandText or SqlCommand
			// (Later consolidation can be done by the caller)

			return results;
		}

		/// <summary>
		/// Try to resolve string expressions:
		/// - literal string -> returns value
		/// - constant field or const variable -> semanticModel.GetConstantValue
		/// - simple binary concatenation with constant operands -> reconstruct
		/// Otherwise returns null.
		/// </summary>
		private static string TryResolveStringExpression(ExpressionSyntax expr, SemanticModel semanticModel)
		{
			if (expr == null) return null;

			// Constant folding
			var constVal = semanticModel.GetConstantValue(expr);
			if (constVal.HasValue && constVal.Value is string s)
				return s;

			// If it's a literal expression
			if (expr is LiteralExpressionSyntax les && les.IsKind(SyntaxKind.StringLiteralExpression))
			{
				return les.Token.ValueText;
			}

			// Interpolated string - try to evaluate constant parts only (best-effort)
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
							parts.Add(innerConst.Value.ToString());
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

			// Binary concatenation
			if (expr is BinaryExpressionSyntax bin && (bin.IsKind(SyntaxKind.AddExpression) || bin.IsKind(SyntaxKind.AddAssignmentExpression)))
			{
				var left = TryResolveStringExpression(bin.Left, semanticModel);
				var right = TryResolveStringExpression(bin.Right, semanticModel);
				if (left != null && right != null)
					return string.Concat(left, right);
			}

			// Member access or identifier (const field)
			var symbol = semanticModel.GetSymbolInfo(expr).Symbol;
			if (symbol is IFieldSymbol fsym && fsym.IsConst && fsym.HasConstantValue && fsym.ConstantValue is string fsv)
				return fsv;
			if (symbol is ILocalSymbol lsym && lsym.HasConstantValue && lsym.ConstantValue is string lsv)
				return lsv;
			if (symbol is IPropertySymbol psym && psym.IsReadOnly)
			{
				// if property has constant getter, GetConstantValue may have worked earlier; otherwise skip
			}
			// Could add more heuristics here (resolve static readonly fields initialized with literal concatenation) — omitted for brevity

			return null;
		}

		private static void PopulateInferredProcs(SqlUsage usage)
		{
			if (string.IsNullOrEmpty(usage.SqlText)) return;
			// look for EXEC or single token
			var s = usage.SqlText.Trim();
			// look for EXEC procname or EXEC schema.proc
			var execMatch = Regex.Match(s, @"\bEXEC(?:UTE)?\b\s+([\[\]A-Za-z0-9_\.\$]+)", RegexOptions.IgnoreCase);
			if (execMatch.Success)
			{
				var proc = execMatch.Groups[1].Value.Trim().Trim('\'', '"');
				usage.InferredStoredProcedures.Add(proc.Replace("[", "").Replace("]", ""));
				return;
			}
			// If the whole SQL looks like a single identifier (no spaces and no SQL keywords), treat as proc name
			var compact = Regex.Replace(s, @"\s+", " ").Trim();
			if (compact.Length < 200 && ProcNameHeuristic.IsMatch(compact) && !Regex.IsMatch(compact, @"\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|FROM|WHERE|JOIN|VALUES|SET)\b", RegexOptions.IgnoreCase))
			{
				usage.InferredStoredProcedures.Add(compact.Replace("[", "").Replace("]", ""));
			}

			// If CommandType was flagged elsewhere, consumer can join by location/method
		}

		private static IMethodSymbol GetEnclosingMethodSymbol(SyntaxNode node, SemanticModel semanticModel)
		{
			var methodDecl = node.AncestorsAndSelf().OfType<MethodDeclarationSyntax>().FirstOrDefault();
			if (methodDecl != null)
			{
				var sym = semanticModel.GetDeclaredSymbol(methodDecl) as IMethodSymbol;
				if (sym != null) return sym;
			}

			// try local functions
			var localFunc = node.AncestorsAndSelf().OfType<LocalFunctionStatementSyntax>().FirstOrDefault();
			if (localFunc != null)
			{
				var sym = semanticModel.GetDeclaredSymbol(localFunc) as IMethodSymbol;
				if (sym != null) return sym;
			}

			// fallback to nearest enclosing type constructor or property accessors
			var ctor = node.AncestorsAndSelf().OfType<ConstructorDeclarationSyntax>().FirstOrDefault();
			if (ctor != null)
			{
				var sym = semanticModel.GetDeclaredSymbol(ctor) as IMethodSymbol;
				if (sym != null) return sym;
			}

			// fallback: try to find any symbol containing the position
			var sym2 = semanticModel.GetEnclosingSymbol(node.SpanStart);
			return sym2 as IMethodSymbol;
		}
	}
}
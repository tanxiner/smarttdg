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
	// This method is best-effort: it tracks local string variables initialized with literal/const
	// values and looks for invocations that pass those variables into likely DB wrapper methods
	// (Read/Update/Query/Execute/etc). When found it emits SqlUsage objects containing resolved SQL text
	// (when possible) and inferred stored-proc names.
	public static partial class SqlCommandExtractor
	{
		public static IEnumerable<SqlUsage> AnalyzeDbWrapperCalls(SyntaxNode root, SemanticModel semanticModel, string filePath)
		{
			var results = new List<SqlUsage>();
			if (root == null || semanticModel == null) return results;

			// Map tracked variable symbol -> resolved string value
			var literalVarValues = new Dictionary<ISymbol, string>();

			// 1) Find local variable declarations with string initializer
			var varDecls = root.DescendantNodes().OfType<VariableDeclaratorSyntax>();
			foreach (var decl in varDecls)
			{
				try
				{
					var declared = semanticModel.GetDeclaredSymbol(decl);
					if (declared == null) continue;

					// only string locals/fields/properties
					ITypeSymbol varType = null;
					if (declared is ILocalSymbol ls) varType = ls.Type;
					else if (declared is IFieldSymbol fs) varType = fs.Type;
					else if (declared is IPropertySymbol ps) varType = ps.Type;

					if (varType == null) continue;
					if (varType.SpecialType != SpecialType.System_String) continue;

					var init = decl.Initializer?.Value;
					if (init == null) continue;
					var resolved = TryResolveStringExpression(init, semanticModel);
					if (!string.IsNullOrEmpty(resolved))
						literalVarValues[declared] = resolved;
				}
				catch
				{
					// ignore - best-effort
				}
			}

			// 2) Also pick up simple assignments: spname = "sp_xxx";
			var assignments = root.DescendantNodes().OfType<AssignmentExpressionSyntax>();
			foreach (var a in assignments)
			{
				try
				{
					var leftSym = semanticModel.GetSymbolInfo(a.Left).Symbol;
					if (leftSym == null) continue;
					// ensure left is string-typed
					ITypeSymbol leftType = null;
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

			// 3) Find invocations where an argument is one of the tracked variables and method name looks like DB wrapper
			var invocations = root.DescendantNodes().OfType<InvocationExpressionSyntax>();
			foreach (var inv in invocations)
			{
				try
				{
					// try to get invoked name
					string invokedName = null;
					if (inv.Expression is MemberAccessExpressionSyntax mae)
						invokedName = mae.Name.Identifier.Text;
					else
					{
						var sym = semanticModel.GetSymbolInfo(inv).Symbol as IMethodSymbol;
						invokedName = sym?.Name;
					}
					if (string.IsNullOrEmpty(invokedName)) continue;
					var low = invokedName.ToLowerInvariant();
					if (!(low.Contains("read") || low.Contains("update") || low.Contains("query") || low.Contains("execute") || low.Contains("run"))) continue;

					// examine arguments for a tracked symbol
					foreach (var arg in inv.ArgumentList.Arguments)
					{
						var argSym = semanticModel.GetSymbolInfo(arg.Expression).Symbol;
						if (argSym == null) continue;
						if (!literalVarValues.TryGetValue(argSym, out var sqlText)) continue;

						// build usage entry
						var methodDecl = inv.AncestorsAndSelf().OfType<MethodDeclarationSyntax>().FirstOrDefault();
						var methodSym = methodDecl != null ? semanticModel.GetDeclaredSymbol(methodDecl) as IMethodSymbol : null;
						var loc = inv.GetLocation().GetLineSpan();

						var usage = new SqlUsage
						{
							FilePath = filePath,
							Namespace = methodSym?.ContainingNamespace?.ToDisplayString() ?? "",
							ClassName = methodSym?.ContainingType?.Name ?? Path.GetFileNameWithoutExtension(filePath),
							MethodName = methodSym?.Name ?? "(top-level)",
							MethodSignature = methodSym?.ToDisplayString() ?? "(unknown)",
							Line = loc.StartLinePosition.Line + 1,
							Kind = "DbWrapperCall",
							SqlText = sqlText,
							CommandTypeIsStoredProcedure = false,
							RawSnippet = inv.ToString()
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
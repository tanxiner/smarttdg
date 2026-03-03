using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using Esprima;
using Esprima.Ast;

namespace Roslyn.Analyzers
{
    /// <summary>
    /// Lightweight JS/TS/JSX/TSX analyzer.
    /// Best-effort/tolerant parsing using Esprima.
    /// Emits a compact client_js_summary and only essential arrays to keep payload small.
    /// 
    /// Updated: dynamic, generic URL detection using both name-heuristics and value-heuristics
    /// (no hard-coded serverUrl/apiUrl variable names).
    /// </summary>
    public static class JsAnalyzer
    {
        public static bool IsJsPath(string filePath)
            => !string.IsNullOrEmpty(filePath)
               && (filePath.EndsWith(".js", StringComparison.OrdinalIgnoreCase));

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            try
            {
                // Compact containers (use tuples for predictable extraction)
                var exports = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
                var funcs = new List<(string kind, string name, string[] parameters)>();
                var apiCalls = new List<(string kind, string method, string url)>();
                var eventBindings = new List<(string kind, string eventName, string handler)>();
                var selectors = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

                // Small text-based summary (safe, regex-driven) - updated dynamic URL detection
                var clientSummary = SummarizeJsText(code);

                // Instantiate Esprima parser in a version-tolerant way.
                Script? esprimaScript = null;
                try
                {
                    ParserOptions options = new ParserOptions { Tolerant = true };
                    try
                    {
                        var parserWithOptions = Activator.CreateInstance(typeof(JavaScriptParser), new object[] { code, options }) as JavaScriptParser;
                        if (parserWithOptions != null)
                        {
                            esprimaScript = parserWithOptions.ParseScript();
                        }
                    }
                    catch
                    {
                        var parserSingle = Activator.CreateInstance(typeof(JavaScriptParser), new object[] { code }) as JavaScriptParser;
                        if (parserSingle != null)
                        {
                            esprimaScript = parserSingle.ParseScript();
                        }
                        else
                        {
                            try
                            {
                                var direct = new JavaScriptParser(code);
                                esprimaScript = direct.ParseScript();
                            }
                            catch
                            {
                                // leave esprimaScript null and continue — we still return clientSummary
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    return new
                    {
                        file = Path.GetFileName(filePath),
                        path = filePath,
                        isJs = IsJsPath(filePath),
                        exports = Array.Empty<string>(),
                        funcs_summary = new { count = 0, sample = Array.Empty<object>() },
                        apiCalls_summary = new { count = 0, sample = Array.Empty<object>() },
                        eventBindings_summary = new { count = 0, sample = Array.Empty<object>() },
                        selectors = Array.Empty<string>(),
                        client_js_summary = clientSummary,
                        error = $"Esprima parser error: {ex.Message}"
                    };
                }

                if (esprimaScript != null)
                {
                    // Helper for NodeList indexing
                    T? GetAtOrDefault<T>(NodeList<T> list, int index) where T : Node
                    {
                        return index >= 0 && index < list.Count ? list[index] : null;
                    }

                    // Visitor to collect compact info
                    void Visit(Node node)
                    {
                        if (node == null) return;

                        if (node is Script prog)
                        {
                            foreach (var n in prog.Body) Visit(n);
                            return;
                        }

                        if (node is FunctionDeclaration fd)
                        {
                            var name = fd.Id?.Name ?? "<anonymous>";
                            var paramNames = fd.Params.Select(p => ParamName(p)).ToArray();
                            funcs.Add(("func", name, paramNames));
                            if (fd.Body is BlockStatement blk)
                                foreach (var s in blk.Body) Visit(s);
                            return;
                        }

                        if (node is VariableDeclaration vd)
                        {
                            foreach (var decl in vd.Declarations)
                            {
                                if (decl?.Init is ArrowFunctionExpression afe)
                                {
                                    var name = GetNodeName(decl.Id) ?? "<anonymous>";
                                    var paramNames = afe.Params.Select(p => ParamName(p)).ToArray();
                                    funcs.Add(("var-func", name, paramNames));
                                    if (afe.Body is BlockStatement abody)
                                        foreach (var s in abody.Body) Visit(s);
                                    else
                                        Visit(afe.Body);
                                }
                                else if (decl?.Init is FunctionExpression fe)
                                {
                                    var name = GetNodeName(decl.Id) ?? "<anonymous>";
                                    var paramNames = fe.Params.Select(p => ParamName(p)).ToArray();
                                    funcs.Add(("var-func", name, paramNames));
                                    if (fe.Body is BlockStatement fb)
                                        foreach (var s in fb.Body) Visit(s);
                                    else
                                        Visit(fe.Body);
                                }
                                else
                                {
                                    if (decl?.Init is Node initNode) Visit(initNode);
                                }
                            }
                            return;
                        }

                        if (node is ClassDeclaration cd)
                        {
                            var className = cd.Id?.Name ?? "<class>";
                            foreach (var element in cd.Body.Body.Cast<Node>())
                            {
                                if (element is MethodDefinition md)
                                {
                                    string methodName;
                                    if (md.Key is Identifier keyId) methodName = keyId.Name ?? "<method>";
                                    else methodName = md.Key?.ToString()?.Trim('\'', '"') ?? "<method>";

                                    if (md.Value is FunctionExpression fe2)
                                    {
                                        var paramNames = fe2.Params.Select(p => ParamName(p)).ToArray();
                                        funcs.Add(("class-method", className + "." + methodName, paramNames));
                                    }
                                    else
                                    {
                                        funcs.Add(("class-method", className + "." + methodName, Array.Empty<string>()));
                                    }
                                    Visit(md.Value);
                                }
                            }
                            return;
                        }

                        if (node is ExportNamedDeclaration en)
                        {
                            if (en.Declaration is VariableDeclaration ved)
                            {
                                foreach (var d in ved.Declarations) exports.Add(d?.Id?.ToString() ?? "");
                            }
                            else if (en.Declaration is FunctionDeclaration fed)
                            {
                                exports.Add(fed.Id?.Name ?? "anonymous");
                            }
                            if (en.Declaration is Node declNode) Visit(declNode);
                            return;
                        }

                        if (node is ExportDefaultDeclaration exd)
                        {
                            exports.Add("default");
                            if (exd.Declaration is Node defNode) Visit(defNode);
                            return;
                        }

                        if (node is CallExpression ce)
                        {
                            // fetch(...)
                            if (ce.Callee is Identifier id && string.Equals(id.Name, "fetch", StringComparison.Ordinal))
                            {
                                apiCalls.Add(("fetch", "fetch", ResolveExpressionForUrl(GetAtOrDefault(ce.Arguments, 0)) ?? ""));
                            }
                            else if (ce.Callee is MemberExpression me)
                            {
                                var objName = (me.Object as Identifier)?.Name;
                                var propName = (me.Property as Identifier)?.Name ?? (me.Property as Literal)?.Value?.ToString();

                                if (!string.IsNullOrEmpty(objName) && string.Equals(objName, "axios", StringComparison.OrdinalIgnoreCase))
                                {
                                    if (!string.IsNullOrEmpty(propName) && new[] { "get", "post", "put", "delete", "patch" }.Contains(propName))
                                    {
                                        apiCalls.Add(("axios", propName, ResolveExpressionForUrl(GetAtOrDefault(ce.Arguments, 0)) ?? ""));
                                    }
                                    else if (GetAtOrDefault(ce.Arguments, 0) is ObjectExpression cfg)
                                    {
                                        apiCalls.Add(("axios", ObjectPropertyLiteral(cfg, "method") ?? "", ObjectPropertyLiteral(cfg, "url") ?? ""));
                                    }
                                }

                                if ((objName == "$" || objName == "jQuery") && string.Equals(propName, "ajax", StringComparison.OrdinalIgnoreCase))
                                {
                                    if (GetAtOrDefault(ce.Arguments, 0) is ObjectExpression cfg)
                                    {
                                        apiCalls.Add(("jquery.ajax", ObjectPropertyLiteral(cfg, "method") ?? ObjectPropertyLiteral(cfg, "type") ?? "", ObjectPropertyLiteral(cfg, "url") ?? ""));
                                    }
                                }

                                if (string.Equals(propName, "addEventListener", StringComparison.OrdinalIgnoreCase))
                                {
                                    var ev = LiteralValue(GetAtOrDefault(ce.Arguments, 0)) ?? "";
                                    var handlerNode = GetAtOrDefault(ce.Arguments, 1);
                                    var handler = handlerNode?.ToString() ?? "";
                                    eventBindings.Add(("addEventListener", ev, handler));
                                }

                                if (me.Object is Identifier objId && objId.Name == "document" &&
                                    (string.Equals(propName, "getElementById", StringComparison.OrdinalIgnoreCase) ||
                                     string.Equals(propName, "querySelector", StringComparison.OrdinalIgnoreCase)))
                                {
                                    var sel = LiteralValue(GetAtOrDefault(ce.Arguments, 0));
                                    if (!string.IsNullOrEmpty(sel)) selectors.Add(sel);
                                }
                            }

                            Visit(ce.Callee);
                            foreach (var a in ce.Arguments) Visit(a);
                            return;
                        }

                        if (node is MemberExpression mem)
                        {
                            Visit(mem.Object);
                            Visit(mem.Property);
                            return;
                        }

                        if (node is ObjectExpression oe)
                        {
                            foreach (var p in oe.Properties)
                                if (p is Property prop)
                                    Visit(prop.Value);
                            return;
                        }

                        if (node is ExpressionStatement es)
                        {
                            Visit(es.Expression);
                            return;
                        }

                        if (node is VariableDeclarator vdec)
                        {
                            if (vdec.Init is Node initNode) Visit(initNode);
                            return;
                        }

                        if (node is ArrowFunctionExpression arrow)
                        {
                            if (arrow.Body is BlockStatement bs)
                                foreach (var s in bs.Body) Visit(s);
                            else
                                Visit(arrow.Body);
                            return;
                        }

                        if (node is BlockStatement block)
                        {
                            foreach (var s in block.Body) Visit(s);
                            return;
                        }

                        // Fallback: reflectively traverse child Node properties/collections
                        var props = node.GetType().GetProperties()
                            .Where(pr => typeof(Node).IsAssignableFrom(pr.PropertyType) || typeof(System.Collections.IEnumerable).IsAssignableFrom(pr.PropertyType));
                        foreach (var pr in props)
                        {
                            var val = pr.GetValue(node);
                            if (val is Node n) Visit(n);
                            else if (val is System.Collections.IEnumerable col)
                            {
                                foreach (var item in col)
                                {
                                    if (item is Node nn) Visit(nn);
                                }
                            }
                        }
                    }

                    Visit(esprimaScript);
                }

                // Build compact summaries (limit samples)
                var exportsArr = exports.Take(50).ToArray();
                var distinctFuncs = funcs
                    .Select(f => (kind: f.kind ?? "", name: (f.name ?? "<anonymous>").Trim(), parameters: f.parameters))
                    .Where(f => !string.IsNullOrEmpty(f.name))
                    .Distinct()
                    .ToList();
                var funcsSummary = new
                {
                    count = distinctFuncs.Count,
                    sample = distinctFuncs.Take(20).Select(f => new { f.kind, f.name, f.parameters }).ToArray()
                };
                var apiCallsSummary = new
                {
                    count = apiCalls.Count,
                    sample = apiCalls.Take(20).Select(a => new { a.kind, a.method, a.url }).ToArray()
                };
                var eventBindingsSummary = new
                {
                    count = eventBindings.Count,
                    sample = eventBindings.Take(20).Select(e => new { e.kind, e.eventName }).ToArray()
                };
                var selectorsArr = selectors.Take(50).ToArray();

                // -----------------------
                // Merge text-level summary with AST-detected API calls and URLs (deduplicated)
                // -----------------------
                object mergedClientSummary = clientSummary;
                try
                {
                    // Extract facts dictionary from clientSummary (anonymous object's 'facts' is a Dictionary<string,object>)
                    var factsProp = clientSummary?.GetType().GetProperty("facts");
                    var origFacts = factsProp?.GetValue(clientSummary) as Dictionary<string, object> ?? new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);

                    // Collect existing api_calls from text summary (if any)
                    var existingApi = new List<(string kind, string method, string url)>();
                    if (origFacts.TryGetValue("api_calls", out var existingApiObj) && existingApiObj is System.Collections.IEnumerable existingApiEnum)
                    {
                        foreach (var o in existingApiEnum)
                        {
                            try
                            {
                                var t = o.GetType();
                                var kindV = t.GetProperty("kind")?.GetValue(o)?.ToString() ?? "";
                                var methodV = t.GetProperty("method")?.GetValue(o)?.ToString() ?? "";
                                var urlV = t.GetProperty("url")?.GetValue(o)?.ToString() ?? "";
                                existingApi.Add((kindV, methodV, urlV));
                            }
                            catch { /* ignore reflection issues */ }
                        }
                    }

                    // Add AST-discovered apiCalls
                    existingApi.AddRange(apiCalls);

                    // Deduplicate API calls by url (prefer first seen)
                    var apiByUrl = new Dictionary<string, (string kind, string method, string url)>(StringComparer.OrdinalIgnoreCase);
                    foreach (var a in existingApi)
                    {
                        var u = a.url ?? "";
                        if (string.IsNullOrWhiteSpace(u)) continue;
                        if (!apiByUrl.ContainsKey(u))
                            apiByUrl[u] = a;
                    }

                    var mergedApiList = apiByUrl.Values
                        .Select(a => (object)new { kind = a.kind, method = a.method, url = a.url })
                        .Take(20)
                        .ToList();

                    origFacts["api_calls"] = mergedApiList;

                    // Build URL candidate set from existing url_candidates, url_by_value, and api URLs
                    var urlSet = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

                    if (origFacts.TryGetValue("url_candidates", out var existingUrlsObj) && existingUrlsObj is IEnumerable<object> existingUrlEnum)
                    {
                        foreach (var uo in existingUrlEnum)
                        {
                            var s = uo?.ToString();
                            if (!string.IsNullOrWhiteSpace(s)) urlSet.Add(s);
                        }
                    }

                    if (origFacts.TryGetValue("url_by_value", out var urlByValueObj) && urlByValueObj is IEnumerable<object> urlByValueEnum)
                    {
                        foreach (var uo in urlByValueEnum)
                        {
                            var s = uo?.ToString();
                            if (!string.IsNullOrWhiteSpace(s)) urlSet.Add(s);
                        }
                    }

                    // Add urls from merged API calls
                    foreach (var a in apiByUrl.Values)
                    {
                        if (!string.IsNullOrWhiteSpace(a.url)) urlSet.Add(a.url);
                    }

                    origFacts["url_candidates"] = urlSet.Take(20).ToList();

                    // Rebuild a concise summary string based on merged facts
                    var parts = new List<string>();
                    if (origFacts.ContainsKey("url_candidates")) parts.Add($"{((List<string>)origFacts["url_candidates"]).Count} url_candidates");
                    if (origFacts.ContainsKey("functions")) parts.Add($"{((List<string>)origFacts["functions"]).Count} functions");
                    if (origFacts.ContainsKey("api_calls")) parts.Add($"{((List<object>)origFacts["api_calls"]).Count} API patterns");
                    if (origFacts.ContainsKey("selectors")) parts.Add($"{((List<string>)origFacts["selectors"]).Count} selectors");
                    var mergedSummaryStr = string.Join("; ", parts);

                    mergedClientSummary = new { summary = mergedSummaryStr, facts = origFacts };
                }
                catch
                {
                    // best-effort; keep original clientSummary if merge fails
                    mergedClientSummary = clientSummary;
                }

                // Final compact result
                return new
                {
                    file = Path.GetFileName(filePath),
                    path = filePath,
                    isJs = IsJsPath(filePath),
                    exports = exportsArr,
                    funcs = funcsSummary,
                    apiCalls = apiCallsSummary,
                    eventBindings = eventBindingsSummary,
                    selectors = selectorsArr,
                    client_js_summary = mergedClientSummary
                };
            }
            catch (Exception ex)
            {
                return new
                {
                    file = Path.GetFileName(filePath),
                    path = filePath,
                    isJs = IsJsPath(filePath),
                    exports = Array.Empty<string>(),
                    funcs = new { count = 0, sample = Array.Empty<object>() },
                    apiCalls = new { count = 0, sample = Array.Empty<object>() },
                    eventBindings = new { count = 0, sample = Array.Empty<object>() },
                    selectors = Array.Empty<string>(),
                    client_js_summary = SummarizeJsText(code),
                    error = ex.Message
                };
            }
        }

        // ---------------------------
        // Updated dynamic SummarizeJsText
        // ---------------------------
        private static object SummarizeJsText(string text)
        {
            if (string.IsNullOrWhiteSpace(text)) return new { summary = "", facts = new { } };

            // Work on a bounded snippet so runtime and output are predictable
            var snippet = text.Length > 20000 ? text.Substring(0, 20000) : text;
            var facts = new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);

            const int SAMPLE_LIMIT = 20;

            // ---------- DYNAMIC URL DETECTION (NO HARDCODED NAMES) ----------
            // 1) Name heuristic - detect variable names that imply URL endpoints (Url, URL, Endpoint, BaseUrl, BaseURL etc.)
            //    capture variable name and assigned value (if any)
            var urlByName = new List<object>();
            // match patterns like: const apiBaseUrl = "https://api.example.com"
            // groups: 1 = identifier (name), 2 = value (if quoted)
            var namePattern = @"^\s*(?:const|let|var)?\s*([A-Za-z0-9_\$]*?(?:Url|URL|Endpoint|BaseUrl|BaseURL|ApiUrl|apiBase|baseURL|endpoint))\s*[:=]\s*['""]?([^'""]+)['""]?";
            foreach (Match m in Regex.Matches(snippet, namePattern, RegexOptions.Multiline | RegexOptions.IgnoreCase))
            {
                var name = m.Groups.Count > 1 ? m.Groups[1].Value.Trim() : "";
                var val = m.Groups.Count > 2 ? m.Groups[2].Value.Trim() : "";
                if (!string.IsNullOrEmpty(name))
                {
                    // only keep if reasonable (either value looks like URL or name strongly implies URL)
                    if (!string.IsNullOrEmpty(val) || Regex.IsMatch(name, "(Url|URL|Endpoint|BaseUrl|BaseURL|ApiUrl|apiBase|endpoint)$", RegexOptions.IgnoreCase))
                    {
                        urlByName.Add(new { name, value = val });
                        if (urlByName.Count >= SAMPLE_LIMIT) break;
                    }
                }
            }
            if (urlByName.Count > 0) facts["url_by_name"] = urlByName;

            // 2) Value heuristic - detect any string assignment whose value looks like an http or https URL
            var urlByValue = new List<string>();
            var valuePattern = @"([A-Za-z0-9_\$]+)?\s*[:=]\s*['""]\s*(https?:\/\/[^'""\s]+)\s*['""]";
            foreach (Match m in Regex.Matches(snippet, valuePattern, RegexOptions.IgnoreCase))
            {
                var name = m.Groups.Count > 1 ? m.Groups[1].Value.Trim() : "";
                var val = m.Groups.Count > 2 ? m.Groups[2].Value.Trim() : "";
                if (!string.IsNullOrEmpty(val))
                {
                    // include either "value only" or "name:value" string
                    if (!string.IsNullOrEmpty(name))
                        urlByValue.Add($"{name}={val}");
                    else
                        urlByValue.Add(val);

                    if (urlByValue.Count >= SAMPLE_LIMIT) break;
                }
            }
            if (urlByValue.Count > 0) facts["url_by_value"] = urlByValue.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();

            // 3) Combined candidates (merged view) - merge unique values from both heuristics
            var combinedUrls = new List<string>();
            try
            {
                // extract value strings from urlByName (if any)
                foreach (var o in urlByName)
                {
                    try
                    {
                        var dict = (o as object);
                        // using reflection-light approach via anonymous -> ToString fallback: try to get "value"
                        var valueProp = o.GetType().GetProperty("value");
                        var nameProp = o.GetType().GetProperty("name");
                        var val = valueProp?.GetValue(o) as string;
                        var nm = nameProp?.GetValue(o) as string;
                        if (!string.IsNullOrEmpty(val))
                        {
                            combinedUrls.Add(!string.IsNullOrEmpty(nm) ? $"{nm}={val}" : val);
                        }
                        else if (!string.IsNullOrEmpty(nm))
                        {
                            combinedUrls.Add(nm);
                        }
                    }
                    catch
                    {
                        // ignore reflection issues
                    }
                }

                // add urlByValue entries
                combinedUrls.AddRange(urlByValue);
            }
            catch
            {
                // ignore
            }

            if (combinedUrls.Count > 0)
                facts["url_candidates"] = combinedUrls.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();

            // ---------- END DYNAMIC URL DETECTION ----------

            // ---------- CONSTANTS (simple assignments) ----------
            var consts = new List<object>();
            foreach (Match cm in Regex.Matches(snippet, @"^\s*(?:const|let|var)\s+([A-Za-z0-9_\$]+)\s*=\s*([^\r\n;]+)", RegexOptions.Multiline))
            {
                var name = cm.Groups[1].Value?.Trim();
                var val = cm.Groups[2].Value?.Trim() ?? "";
                if (!string.IsNullOrEmpty(name))
                {
                    consts.Add(new { name, value_preview = val.Length <= 200 ? val : val.Substring(0, 200) });
                    if (consts.Count >= 10) break;
                }
            }
            //if (consts.Count > 0) facts["constants"] = consts;

            // ---------- FUNCTIONS (named + var/const arrow) ----------
            var functions = new List<string>();
            functions.AddRange(CollectSamplesHelper(snippet, @"function\s+([A-Za-z0-9_\$]+)\s*\(", 1, SAMPLE_LIMIT));
            functions.AddRange(CollectSamplesHelper(snippet, @"^\s*(?:const|let|var)\s+([A-Za-z0-9_\$]+)\s*=\s*(?:async\s*)?(?:\(|[A-Za-z0-9_\$]+)\s*=>", 1, SAMPLE_LIMIT, RegexOptions.Multiline));
            functions = functions.Distinct(StringComparer.OrdinalIgnoreCase).Take(30).ToList();
            if (functions.Count > 0) facts["functions"] = functions;

            // ---------- API CALLS (simple text-level heuristics) ----------
            var apiCalls = new List<object>();
            foreach (Match m in Regex.Matches(snippet, @"\bfetch\s*\(\s*['""]([^'""]+)['""]", RegexOptions.IgnoreCase))
                apiCalls.Add(new { kind = "fetch", url = m.Groups[1].Value });
            foreach (Match m in Regex.Matches(snippet, @"\baxios\.(get|post|put|delete|patch)\s*\(\s*['""]([^'""]+)['""]", RegexOptions.IgnoreCase))
                apiCalls.Add(new { kind = "axios", method = m.Groups[1].Value, url = m.Groups[2].Value });
            if (apiCalls.Count > 0) facts["api_calls"] = apiCalls.Take(SAMPLE_LIMIT).ToList();

            // ---------- SELECTORS (jQuery and querySelector) ----------
            var selectors = new List<string>();
            selectors.AddRange(CollectSamplesHelper(snippet, @"\$\s*\(\s*['""]([^'""]+)['""]\s*\)", 1, SAMPLE_LIMIT));
            selectors.AddRange(CollectSamplesHelper(snippet, @"querySelector(?:All)?\s*\(\s*['""]([^'""]+)['""]\s*\)", 1, SAMPLE_LIMIT));
            selectors = selectors.Distinct(StringComparer.OrdinalIgnoreCase).Take(50).ToList();
            if (selectors.Count > 0) facts["selectors"] = selectors;

            // ---------- SERVER EXPRESSIONS (templates, server-side tags) ----------
            var serverExprs = CollectSamplesHelper(snippet, @"<%=?\s*(.*?)\s*%>", 1, SAMPLE_LIMIT, RegexOptions.Singleline);
            if (serverExprs.Count > 0) facts["server_expressions"] = serverExprs;

            // Build short human-readable summary (dynamic)
            var parts = new List<string>();
            if (facts.ContainsKey("url_candidates")) parts.Add($"{((List<string>)facts["url_candidates"]).Count} url_candidates");
            if (facts.ContainsKey("functions")) parts.Add($"{((List<string>)facts["functions"]).Count} functions");
            if (facts.ContainsKey("api_calls")) parts.Add($"{((List<object>)facts["api_calls"]).Count} API patterns");
            if (facts.ContainsKey("selectors")) parts.Add($"{((List<string>)facts["selectors"]).Count} selectors");
            var summary = string.Join("; ", parts);

            return new { summary = summary, facts = facts };

            // Local helper used in several places
            static List<string> CollectSamplesHelper(string snippetLocal, string patternLocal, int groupIndexLocal = 1, int limitLocal = 20, RegexOptions optsLocal = RegexOptions.IgnoreCase | RegexOptions.Singleline)
            {
                try
                {
                    return Regex.Matches(snippetLocal, patternLocal, optsLocal)
                                .Cast<Match>()
                                .Select(m => (groupIndexLocal < m.Groups.Count ? m.Groups[groupIndexLocal].Value : m.Value)?.Trim())
                                .Where(s => !string.IsNullOrEmpty(s))
                                .Select(s => s!)
                                .Distinct(StringComparer.OrdinalIgnoreCase)
                                .Take(limitLocal)
                                .ToList();
                }
                catch
                {
                    return new List<string>();
                }
            }
        }

        private static string ParamName(Node? p)
        {
            if (p == null) return "<param>";
            return p switch
            {
                Identifier id => id.Name ?? "<param>",
                AssignmentPattern ap => ap.Left?.ToString() ?? "<param>",
                RestElement re => re.Argument?.ToString() ?? "<param>",
                _ => p.ToString() ?? "<param>"
            };
        }

        private static string? LiteralValue(Node? node)
        {
            if (node == null) return null;
            if (node is Literal lit) return lit.Value?.ToString();
            if (node is TemplateLiteral tpl)
            {
                try
                {
                    var quasis = tpl.Quasis;
                    return string.Concat(quasis.Select(q => q.Value?.Raw ?? q.Value?.Cooked));
                }
                catch { return null; }
            }
            return null;
        }

        private static string? ObjectPropertyLiteral(ObjectExpression? obj, string propName)
        {
            if (obj == null) return null;
            foreach (var p in obj.Properties)
            {
                if (p is Property property)
                {
                    var key = property.Key?.ToString()?.Trim('\'', '"');
                    if (string.Equals(key, propName, StringComparison.OrdinalIgnoreCase))
                        return LiteralValue(property.Value);
                }
            }
            return null;
        }

        // --- new helper: robust node -> name resolver (place near ParamName/LiteralValue methods) ---
        private static string? GetNodeName(Node? node)
        {
            if (node == null) return null;
            switch (node)
            {
                case Identifier id:
                    return id.Name;
                case MemberExpression me:
                    // prefer simple textual form for complex patterns
                    return me.ToString();
                case Property prop:
                    return prop.Key?.ToString()?.Trim('\'', '"');
                default:
                    // common pattern: VariableDeclarator.Id may be Identifier or Binding pattern; fallback to ToString()
                    var s = node.ToString();
                    if (string.IsNullOrWhiteSpace(s)) return null;
                    // avoid Esprima type names leaking ("Esprima.Ast.Identifier")
                    if (s.Contains("Esprima.Ast", StringComparison.OrdinalIgnoreCase)) return null;
                    return s;
            }
        }

        // Add this helper near the other helpers (e.g. next to LiteralValue / ObjectPropertyLiteral)
        private static string ResolveExpressionForUrl(Node? node)
        {
            if (node == null) return "";

            // plain literal
            if (node is Literal lit) return lit.Value?.ToString() ?? "";

            // template literal -> combine quasis and placeholders for expressions
            if (node is TemplateLiteral tpl)
            {
                try
                {
                    var parts = tpl.Quasis.Select(q => q.Value?.Raw ?? q.Value?.Cooked).ToArray();
                    // If there are expressions, show placeholders {exprN}
                    var exprs = tpl.Expressions.Select((e, i) => "{" + (e is Identifier id ? id.Name : i.ToString()) + "}").ToArray();
                    var outParts = new List<string>();
                    for (int i = 0; i < parts.Length; i++)
                    {
                        outParts.Add(parts[i] ?? "");
                        if (i < exprs.Length) outParts.Add(exprs[i]);
                    }
                    return string.Concat(outParts);
                }
                catch { /* best-effort */ }
            }

            // identifier -> placeholder
            if (node is Identifier idn) return "{" + (idn.Name ?? "id") + "}";

            // binary concatenation: combine left/right for '+' operator
            if (node is BinaryExpression be && be.Operator == BinaryOperator.Plus)
            {
                return ResolveExpressionForUrl(be.Left) + ResolveExpressionForUrl(be.Right);
            }

            // new URLSearchParams({ ... }) -> produce ?k1={v1}&k2={v2}
            if (node is NewExpression ne)
            {
                // Determine callee name robustly (Identifier, MemberExpression, or ToString fallback)
                string calleeText = "";
                try
                {
                    if (ne.Callee is Identifier ci) calleeText = ci.Name ?? "";
                    else if (ne.Callee is MemberExpression cm) calleeText = cm.ToString() ?? "";
                    else calleeText = ne.Callee?.ToString() ?? "";
                }
                catch
                {
                    calleeText = ne.Callee?.ToString() ?? "";
                }

                if (!string.IsNullOrEmpty(calleeText) && calleeText.IndexOf("URLSearchParams", StringComparison.OrdinalIgnoreCase) >= 0
                    && ne.Arguments.Count > 0 && ne.Arguments[0] is ObjectExpression obj)
                {
                    var parts = new List<string>();
                    foreach (var prop in obj.Properties.OfType<Property>())
                    {
                        var key = prop.Key?.ToString()?.Trim('\'', '"') ?? "";
                        string valRep;
                        if (prop.Value is Identifier vi) valRep = "{" + (vi.Name ?? "v") + "}";
                        else if (prop.Value is Literal vl) valRep = vl.Value?.ToString() ?? "";
                        else valRep = "{" + (prop.Value?.ToString() ?? "expr") + "}";
                        parts.Add($"{key}={valRep}");
                    }
                    return parts.Count > 0 ? "?" + string.Join("&", parts) : "";
                }

                // safe fallback: return empty string rather than exposing Esprima internals
                return "";
            }

            // call expressions like encodeURIComponent(...) -> keep callee name
            if (node is CallExpression ce)
            {
                var callee = ce.Callee?.ToString() ?? "call";
                // if first arg is literal or expression, show a short pattern
                var arg0 = ce.Arguments.Count > 0 ? ResolveExpressionForUrl(ce.Arguments[0]) : "";
                return $"{callee}({arg0})";
            }

            // fallback: try node.ToString(), but avoid Esprima type names leaking
            try
            {
                var s = node.ToString() ?? "";
                if (s.Contains("Esprima.Ast", StringComparison.OrdinalIgnoreCase)) return "";
                return s;
            }
            catch { return ""; }
        }
    }
}

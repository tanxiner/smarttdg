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
    /// Lightweight JS/JSX analyzer.
    /// Best-effort/tolerant parsing using Esprima.
    /// Emits compact summaries to keep payload small.
    /// 
    /// Notes:
    /// - Strongest support is for .js/.jsx style syntax.
    /// - TypeScript/TSX syntax is not guaranteed to parse with Esprima.
    /// - Falls back to text-summary heuristics when parsing is incomplete or fails.
    /// </summary>
    public static class JsAnalyzer
    {
        public static bool IsJsPath(string filePath)
            => !string.IsNullOrEmpty(filePath)
               && (filePath.EndsWith(".js", StringComparison.OrdinalIgnoreCase)
                   || filePath.EndsWith(".jsx", StringComparison.OrdinalIgnoreCase)
                   //|| filePath.EndsWith(".mjs", StringComparison.OrdinalIgnoreCase)
                   //|| filePath.EndsWith(".cjs", StringComparison.OrdinalIgnoreCase)
                   );

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            try
            {
                var exports = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
                var funcs = new List<(string kind, string name, string[] parameters)>();
                var apiCalls = new List<(string kind, string method, string url)>();
                var eventBindings = new List<(string kind, string eventName, string handler)>();
                var selectors = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

                var clientSummary = SummarizeJsText(code);

                Script? esprimaScript = null;
                string? parseError = null;

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
                            var direct = new JavaScriptParser(code);
                            esprimaScript = direct.ParseScript();
                        }
                    }
                }
                catch (Exception ex)
                {
                    parseError = ex.Message;
                }

                if (esprimaScript != null)
                {
                    T? GetAtOrDefault<T>(NodeList<T> list, int index) where T : Node
                    {
                        return index >= 0 && index < list.Count ? list[index] : null;
                    }

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
                                foreach (var d in ved.Declarations)
                                    exports.Add(GetNodeName(d?.Id) ?? "");
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
                                    if (!string.IsNullOrEmpty(propName) &&
                                        new[] { "get", "post", "put", "delete", "patch" }.Contains(propName))
                                    {
                                        apiCalls.Add(("axios", propName, ResolveExpressionForUrl(GetAtOrDefault(ce.Arguments, 0)) ?? ""));
                                    }
                                    else if (GetAtOrDefault(ce.Arguments, 0) is ObjectExpression cfg)
                                    {
                                        apiCalls.Add(("axios",
                                            ObjectPropertyLiteral(cfg, "method") ?? "",
                                            ObjectPropertyLiteral(cfg, "url") ?? ""));
                                    }
                                }

                                if ((objName == "$" || objName == "jQuery") &&
                                    string.Equals(propName, "ajax", StringComparison.OrdinalIgnoreCase))
                                {
                                    if (GetAtOrDefault(ce.Arguments, 0) is ObjectExpression cfg)
                                    {
                                        apiCalls.Add(("jquery.ajax",
                                            ObjectPropertyLiteral(cfg, "method") ?? ObjectPropertyLiteral(cfg, "type") ?? "",
                                            ObjectPropertyLiteral(cfg, "url") ?? ""));
                                    }
                                }

                                if (string.Equals(propName, "addEventListener", StringComparison.OrdinalIgnoreCase))
                                {
                                    var ev = LiteralValue(GetAtOrDefault(ce.Arguments, 0)) ?? "";
                                    var handlerNode = GetAtOrDefault(ce.Arguments, 1);
                                    var handler = handlerNode?.ToString() ?? "";
                                    eventBindings.Add(("addEventListener", ev, handler));
                                }

                                if ((objName == "$" || objName == "jQuery") &&
                                    !string.IsNullOrEmpty(propName) &&
                                    new[] { "on", "click", "change", "submit", "keyup", "keydown" }.Contains(propName))
                                {
                                    if (string.Equals(propName, "on", StringComparison.OrdinalIgnoreCase))
                                    {
                                        var ev = LiteralValue(GetAtOrDefault(ce.Arguments, 0)) ?? "";
                                        var handlerNode = GetAtOrDefault(ce.Arguments, 1);
                                        var handler = handlerNode?.ToString() ?? "";
                                        eventBindings.Add(("jquery.on", ev, handler));
                                    }
                                    else
                                    {
                                        var handlerNode = GetAtOrDefault(ce.Arguments, 0);
                                        var handler = handlerNode?.ToString() ?? "";
                                        eventBindings.Add(("jquery.shortcut", propName, handler));
                                    }
                                }

                                if (me.Object is Identifier objId && objId.Name == "document" &&
                                    (string.Equals(propName, "getElementById", StringComparison.OrdinalIgnoreCase) ||
                                     string.Equals(propName, "querySelector", StringComparison.OrdinalIgnoreCase) ||
                                     string.Equals(propName, "querySelectorAll", StringComparison.OrdinalIgnoreCase)))
                                {
                                    var sel = LiteralValue(GetAtOrDefault(ce.Arguments, 0));
                                    if (!string.IsNullOrEmpty(sel)) selectors.Add(sel);
                                }
                            }

                            Visit(ce.Callee);
                            foreach (var a in ce.Arguments) Visit(a);
                            return;
                        }

                        if (node is AssignmentExpression ae)
                        {
                            if (ae.Left is MemberExpression leftMe)
                            {
                                var propName = (leftMe.Property as Identifier)?.Name ?? (leftMe.Property as Literal)?.Value?.ToString();
                                if (!string.IsNullOrWhiteSpace(propName) &&
                                    new[] { "onclick", "onchange", "onsubmit", "oninput", "onblur", "onfocus" }.Contains(propName))
                                {
                                    eventBindings.Add(("dom-property", propName, ae.Right?.ToString() ?? ""));
                                }
                            }

                            Visit(ae.Left);
                            Visit(ae.Right);
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

                        var props = node.GetType().GetProperties()
                            .Where(pr => typeof(Node).IsAssignableFrom(pr.PropertyType) ||
                                         typeof(System.Collections.IEnumerable).IsAssignableFrom(pr.PropertyType));

                        foreach (var pr in props)
                        {
                            var val = pr.GetValue(node);
                            if (val is Node n) Visit(n);
                            else if (val is System.Collections.IEnumerable col)
                            {
                                foreach (var item in col)
                                    if (item is Node nn) Visit(nn);
                            }
                        }
                    }

                    Visit(esprimaScript);
                }

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

                var mergedClientSummary = MergeClientSummary(clientSummary, apiCalls);

                var result = new Dictionary<string, object>
                {
                    ["file"] = Path.GetFileName(filePath),
                    ["path"] = filePath,
                    ["isJs"] = IsJsPath(filePath),
                    ["exports"] = exportsArr,
                    ["funcs"] = funcsSummary,
                    ["apiCalls"] = apiCallsSummary,
                    ["eventBindings"] = eventBindingsSummary,
                    ["selectors"] = selectorsArr,
                    ["client_js_summary"] = mergedClientSummary
                };

                if (!string.IsNullOrWhiteSpace(parseError))
                {
                    result["parseWarning"] = parseError;
                }

                return result;
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

        private static object MergeClientSummary(object clientSummary, List<(string kind, string method, string url)> apiCalls)
        {
            try
            {
                var factsProp = clientSummary?.GetType().GetProperty("facts");
                var origFacts = factsProp?.GetValue(clientSummary) as Dictionary<string, object>
                               ?? new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);

                var existingApi = new List<(string kind, string method, string url)>();

                if (origFacts.TryGetValue("api_calls", out var existingApiObj) &&
                    existingApiObj is System.Collections.IEnumerable existingApiEnum)
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
                        catch { }
                    }
                }

                existingApi.AddRange(apiCalls);

                var apiByUrl = new Dictionary<string, (string kind, string method, string url)>(StringComparer.OrdinalIgnoreCase);
                foreach (var a in existingApi)
                {
                    var u = a.url ?? "";
                    if (string.IsNullOrWhiteSpace(u)) continue;
                    if (!apiByUrl.ContainsKey(u))
                        apiByUrl[u] = a;
                }

                origFacts["api_calls"] = apiByUrl.Values
                    .Select(a => (object)new { kind = a.kind, method = a.method, url = a.url })
                    .Take(20)
                    .ToList();

                var urlSet = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

                AddEnumerableStrings(origFacts.TryGetValue("url_candidates", out var existingUrlsObj) ? existingUrlsObj : null, urlSet);
                AddEnumerableStrings(origFacts.TryGetValue("url_by_value", out var urlByValueObj) ? urlByValueObj : null, urlSet);

                foreach (var a in apiByUrl.Values)
                {
                    if (!string.IsNullOrWhiteSpace(a.url)) urlSet.Add(a.url);
                }

                origFacts["url_candidates"] = urlSet.Take(20).ToList();

                var parts = new List<string>();
                if (origFacts.ContainsKey("url_candidates")) parts.Add($"{CountEnumerable(origFacts["url_candidates"])} url_candidates");
                if (origFacts.ContainsKey("functions")) parts.Add($"{CountEnumerable(origFacts["functions"])} functions");
                if (origFacts.ContainsKey("api_calls")) parts.Add($"{CountEnumerable(origFacts["api_calls"])} API patterns");
                if (origFacts.ContainsKey("selectors")) parts.Add($"{CountEnumerable(origFacts["selectors"])} selectors");
                if (origFacts.ContainsKey("jquery_events")) parts.Add($"{CountEnumerable(origFacts["jquery_events"])} jquery_events");
                if (origFacts.ContainsKey("dom_updates")) parts.Add($"{CountEnumerable(origFacts["dom_updates"])} dom_updates");
                if (origFacts.ContainsKey("storage_usage")) parts.Add($"{CountEnumerable(origFacts["storage_usage"])} storage_patterns");
                if (origFacts.ContainsKey("timers")) parts.Add($"{CountEnumerable(origFacts["timers"])} timer_patterns");
                if (origFacts.ContainsKey("startup_hooks")) parts.Add($"{CountEnumerable(origFacts["startup_hooks"])} startup_hooks");

                var mergedSummaryStr = string.Join("; ", parts);

                return new { summary = mergedSummaryStr, facts = origFacts };
            }
            catch
            {
                return clientSummary;
            }
        }

        private static object SummarizeJsText(string text)
        {
            if (string.IsNullOrWhiteSpace(text))
                return new { summary = "", facts = new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase) };

            var snippet = text.Length > 20000 ? text.Substring(0, 20000) : text;
            var facts = new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);

            const int SAMPLE_LIMIT = 20;

            var urlByName = new List<object>();
            var namePattern = @"^\s*(?:const|let|var)?\s*([A-Za-z0-9_\$]*?(?:Url|URL|Endpoint|BaseUrl|BaseURL|ApiUrl|apiBase|baseURL|endpoint))\s*[:=]\s*['""]?([^'""]+)['""]?";
            foreach (Match m in Regex.Matches(snippet, namePattern, RegexOptions.Multiline | RegexOptions.IgnoreCase))
            {
                var name = m.Groups.Count > 1 ? m.Groups[1].Value.Trim() : "";
                var val = m.Groups.Count > 2 ? m.Groups[2].Value.Trim() : "";
                if (!string.IsNullOrEmpty(name))
                {
                    if (!string.IsNullOrEmpty(val) || Regex.IsMatch(name, "(Url|URL|Endpoint|BaseUrl|BaseURL|ApiUrl|apiBase|endpoint)$", RegexOptions.IgnoreCase))
                    {
                        urlByName.Add(new { name, value = val });
                        if (urlByName.Count >= SAMPLE_LIMIT) break;
                    }
                }
            }
            if (urlByName.Count > 0) facts["url_by_name"] = urlByName;

            var urlByValue = new List<string>();
            var valuePattern = @"([A-Za-z0-9_\$]+)?\s*[:=]\s*['""]\s*(https?:\/\/[^'""\s]+)\s*['""]";
            foreach (Match m in Regex.Matches(snippet, valuePattern, RegexOptions.IgnoreCase))
            {
                var name = m.Groups.Count > 1 ? m.Groups[1].Value.Trim() : "";
                var val = m.Groups.Count > 2 ? m.Groups[2].Value.Trim() : "";
                if (!string.IsNullOrEmpty(val))
                {
                    urlByValue.Add(!string.IsNullOrEmpty(name) ? $"{name}={val}" : val);
                    if (urlByValue.Count >= SAMPLE_LIMIT) break;
                }
            }
            if (urlByValue.Count > 0) facts["url_by_value"] = urlByValue.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();

            var combinedUrls = new List<string>();
            foreach (var o in urlByName)
            {
                try
                {
                    var valueProp = o.GetType().GetProperty("value");
                    var nameProp = o.GetType().GetProperty("name");
                    var val = valueProp?.GetValue(o) as string;
                    var nm = nameProp?.GetValue(o) as string;

                    if (!string.IsNullOrEmpty(val))
                        combinedUrls.Add(!string.IsNullOrEmpty(nm) ? $"{nm}={val}" : val);
                    else if (!string.IsNullOrEmpty(nm))
                        combinedUrls.Add(nm);
                }
                catch { }
            }
            combinedUrls.AddRange(urlByValue);

            if (combinedUrls.Count > 0)
                facts["url_candidates"] = combinedUrls.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();

            var functions = new List<string>();
            functions.AddRange(CollectSamplesHelper(snippet, @"function\s+([A-Za-z0-9_\$]+)\s*\(", 1, SAMPLE_LIMIT));
            functions.AddRange(CollectSamplesHelper(snippet, @"^\s*(?:const|let|var)\s+([A-Za-z0-9_\$]+)\s*=\s*(?:async\s*)?(?:\(|[A-Za-z0-9_\$]+)\s*=>", 1, SAMPLE_LIMIT, RegexOptions.Multiline));
            functions = functions.Distinct(StringComparer.OrdinalIgnoreCase).Take(30).ToList();
            if (functions.Count > 0) facts["functions"] = functions;

            var apiCalls = new List<object>();
            foreach (Match m in Regex.Matches(snippet, @"\bfetch\s*\(\s*['""]([^'""]+)['""]", RegexOptions.IgnoreCase))
                apiCalls.Add(new { kind = "fetch", url = m.Groups[1].Value });
            foreach (Match m in Regex.Matches(snippet, @"\baxios\.(get|post|put|delete|patch)\s*\(\s*['""]([^'""]+)['""]", RegexOptions.IgnoreCase))
                apiCalls.Add(new { kind = "axios", method = m.Groups[1].Value, url = m.Groups[2].Value });
            if (apiCalls.Count > 0) facts["api_calls"] = apiCalls.Take(SAMPLE_LIMIT).ToList();

            var selectors = new List<string>();
            selectors.AddRange(CollectSamplesHelper(snippet, @"\$\s*\(\s*['""]([^'""]+)['""]\s*\)", 1, SAMPLE_LIMIT));
            selectors.AddRange(CollectSamplesHelper(snippet, @"querySelector(?:All)?\s*\(\s*['""]([^'""]+)['""]\s*\)", 1, SAMPLE_LIMIT));
            selectors = selectors.Distinct(StringComparer.OrdinalIgnoreCase).Take(50).ToList();
            if (selectors.Count > 0) facts["selectors"] = selectors;

            var serverExprs = CollectSamplesHelper(snippet, @"<%=?\s*(.*?)\s*%>", 1, SAMPLE_LIMIT, RegexOptions.Singleline);
            if (serverExprs.Count > 0) facts["server_expressions"] = serverExprs;

            var jqueryEvents = new List<object>();
            foreach (Match m in Regex.Matches(snippet, @"\$\s*\(\s*['""]([^'""]+)['""]\s*\)\s*\.on\s*\(\s*['""]([^'""]+)['""]", RegexOptions.IgnoreCase))
                jqueryEvents.Add(new { selector = m.Groups[1].Value, eventName = m.Groups[2].Value, kind = "jquery.on" });
            foreach (Match m in Regex.Matches(snippet, @"\$\s*\(\s*['""]([^'""]+)['""]\s*\)\s*\.(click|change|submit|keyup|keydown)\s*\(", RegexOptions.IgnoreCase))
                jqueryEvents.Add(new { selector = m.Groups[1].Value, eventName = m.Groups[2].Value, kind = "jquery.shortcut" });
            if (jqueryEvents.Count > 0) facts["jquery_events"] = jqueryEvents.Take(SAMPLE_LIMIT).ToList();

            var domUpdates = new List<string>();
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.innerHTML\s*=", 0, SAMPLE_LIMIT));
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.textContent\s*=", 0, SAMPLE_LIMIT));
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.appendChild\s*\(", 0, SAMPLE_LIMIT));
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.insertAdjacentHTML\s*\(", 0, SAMPLE_LIMIT));
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.html\s*\(", 0, SAMPLE_LIMIT));
            domUpdates.AddRange(CollectSamplesHelper(snippet, @"\.append\s*\(", 0, SAMPLE_LIMIT));
            domUpdates = domUpdates.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();
            if (domUpdates.Count > 0) facts["dom_updates"] = domUpdates;

            var storageUsage = new List<string>();
            storageUsage.AddRange(CollectSamplesHelper(snippet, @"localStorage\.(getItem|setItem|removeItem|clear)\s*\(", 1, SAMPLE_LIMIT));
            storageUsage.AddRange(CollectSamplesHelper(snippet, @"sessionStorage\.(getItem|setItem|removeItem|clear)\s*\(", 1, SAMPLE_LIMIT));
            storageUsage.AddRange(CollectSamplesHelper(snippet, @"document\.cookie", 0, SAMPLE_LIMIT));
            storageUsage = storageUsage.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();
            if (storageUsage.Count > 0) facts["storage_usage"] = storageUsage;

            var timers = new List<string>();
            timers.AddRange(CollectSamplesHelper(snippet, @"\b(setTimeout|setInterval)\s*\(", 1, SAMPLE_LIMIT));
            timers = timers.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();
            if (timers.Count > 0) facts["timers"] = timers;

            var startupHooks = new List<string>();
            startupHooks.AddRange(CollectSamplesHelper(snippet, @"addEventListener\s*\(\s*['""](DOMContentLoaded|load)['""]", 1, SAMPLE_LIMIT));
            startupHooks.AddRange(CollectSamplesHelper(snippet, @"\$\s*\(\s*document\s*\)\s*\.ready\s*\(", 0, SAMPLE_LIMIT));
            startupHooks.AddRange(CollectSamplesHelper(snippet, @"window\.onload\s*=", 0, SAMPLE_LIMIT));
            startupHooks = startupHooks.Distinct(StringComparer.OrdinalIgnoreCase).Take(SAMPLE_LIMIT).ToList();
            if (startupHooks.Count > 0) facts["startup_hooks"] = startupHooks;

            var parts = new List<string>();
            if (facts.ContainsKey("url_candidates")) parts.Add($"{CountEnumerable(facts["url_candidates"])} url_candidates");
            if (facts.ContainsKey("functions")) parts.Add($"{CountEnumerable(facts["functions"])} functions");
            if (facts.ContainsKey("api_calls")) parts.Add($"{CountEnumerable(facts["api_calls"])} API patterns");
            if (facts.ContainsKey("selectors")) parts.Add($"{CountEnumerable(facts["selectors"])} selectors");
            if (facts.ContainsKey("jquery_events")) parts.Add($"{CountEnumerable(facts["jquery_events"])} jquery_events");
            if (facts.ContainsKey("dom_updates")) parts.Add($"{CountEnumerable(facts["dom_updates"])} dom_updates");
            if (facts.ContainsKey("storage_usage")) parts.Add($"{CountEnumerable(facts["storage_usage"])} storage_patterns");
            if (facts.ContainsKey("timers")) parts.Add($"{CountEnumerable(facts["timers"])} timer_patterns");
            if (facts.ContainsKey("startup_hooks")) parts.Add($"{CountEnumerable(facts["startup_hooks"])} startup_hooks");

            var summary = string.Join("; ", parts);

            return new { summary, facts };

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
                catch
                {
                    return null;
                }
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

        private static string? GetNodeName(Node? node)
        {
            if (node == null) return null;

            switch (node)
            {
                case Identifier id:
                    return id.Name;
                case MemberExpression me:
                    return me.ToString();
                case Property prop:
                    return prop.Key?.ToString()?.Trim('\'', '"');
                default:
                    var s = node.ToString();
                    if (string.IsNullOrWhiteSpace(s)) return null;
                    if (s.Contains("Esprima.Ast", StringComparison.OrdinalIgnoreCase)) return null;
                    return s;
            }
        }

        private static string ResolveExpressionForUrl(Node? node)
        {
            if (node == null) return "";

            if (node is Literal lit) return lit.Value?.ToString() ?? "";

            if (node is TemplateLiteral tpl)
            {
                try
                {
                    var parts = tpl.Quasis.Select(q => q.Value?.Raw ?? q.Value?.Cooked).ToArray();
                    var exprs = tpl.Expressions.Select((e, i) => "{" + (e is Identifier id ? id.Name : i.ToString()) + "}").ToArray();

                    var outParts = new List<string>();
                    for (int i = 0; i < parts.Length; i++)
                    {
                        outParts.Add(parts[i] ?? "");
                        if (i < exprs.Length) outParts.Add(exprs[i]);
                    }
                    return string.Concat(outParts);
                }
                catch
                {
                }
            }

            if (node is Identifier idn) return "{" + (idn.Name ?? "id") + "}";

            if (node is BinaryExpression be && be.Operator == BinaryOperator.Plus)
            {
                return ResolveExpressionForUrl(be.Left) + ResolveExpressionForUrl(be.Right);
            }

            if (node is NewExpression ne)
            {
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

                if (!string.IsNullOrEmpty(calleeText) &&
                    calleeText.IndexOf("URLSearchParams", StringComparison.OrdinalIgnoreCase) >= 0 &&
                    ne.Arguments.Count > 0 &&
                    ne.Arguments[0] is ObjectExpression obj)
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

                return "";
            }

            if (node is CallExpression ce)
            {
                var callee = ce.Callee?.ToString() ?? "call";
                var arg0 = ce.Arguments.Count > 0 ? ResolveExpressionForUrl(ce.Arguments[0]) : "";
                return $"{callee}({arg0})";
            }

            try
            {
                var s = node.ToString() ?? "";
                if (s.Contains("Esprima.Ast", StringComparison.OrdinalIgnoreCase)) return "";
                return s;
            }
            catch
            {
                return "";
            }
        }

        private static int CountEnumerable(object? value)
        {
            if (value == null) return 0;
            if (value is System.Collections.ICollection c) return c.Count;
            if (value is System.Collections.IEnumerable e) return e.Cast<object>().Count();
            return 0;
        }

        private static void AddEnumerableStrings(object? value, HashSet<string> target)
        {
            if (value is System.Collections.IEnumerable e)
            {
                foreach (var item in e)
                {
                    var s = item?.ToString();
                    if (!string.IsNullOrWhiteSpace(s))
                        target.Add(s);
                }
            }
        }
    }
}
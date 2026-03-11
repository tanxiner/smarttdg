using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class RazorComponentExtractor
    {
        public static bool IsRazorComponentPath(string filePath)
            => !string.IsNullOrEmpty(filePath) &&
               filePath.EndsWith(".razor", StringComparison.OrdinalIgnoreCase);

        public static object Analyze(string code, string filePath)
        {
            code ??= string.Empty;

            var directives = ExtractDirectives(code);
            var codeBlocks = ExtractCodeBlocks(code);
            var injections = ExtractInjections(code);
            var parameters = ExtractParameters(codeBlocks);
            var lifecycleMethods = ExtractLifecycleMethods(codeBlocks);
            var eventBindings = ExtractEventBindings(code);
            var bindAttributes = ExtractBindAttributes(code);

            var markupOnly = BuildMarkupOnlyView(code);

            var headings = ExtractHeadings(markupOnly);
            var forms = ExtractForms(markupOnly);
            var inputs = ExtractInputs(markupOnly);
            var buttons = ExtractButtons(markupOnly);
            var links = ExtractLinks(markupOnly);
            var tables = ExtractTables(markupOnly);
            var modals = ExtractModals(markupOnly);
            var displayRegions = ExtractDisplayRegions(markupOnly);
            var componentUsages = ExtractComponentUsages(markupOnly);

            var summaryHints = BuildSummaryHints(
                directives,
                injections,
                parameters,
                lifecycleMethods,
                eventBindings,
                bindAttributes,
                forms,
                inputs,
                buttons,
                links,
                tables,
                modals,
                displayRegions,
                componentUsages
            );

            return new
            {
                file = System.IO.Path.GetFileName(filePath ?? ""),
                path = filePath,
                isRazorComponent = IsRazorComponentPath(filePath ?? ""),
                directives,
                injections,
                codeBlocks,
                parameters,
                lifecycleMethods,
                eventBindings,
                bindAttributes,
                headings,
                forms,
                inputs,
                buttons,
                links,
                tables,
                modals,
                displayRegions,
                componentUsages,
                summaryHints
            };
        }

        private static object[] ExtractDirectives(string code)
        {
            var list = new List<object>();
            var lines = NormalizeNewlines(code).Split('\n');

            var patterns = new[]
            {
                new { Name = "@page",       Regex = new Regex(@"^\s*@page(?:\s+(.+))?\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@layout",     Regex = new Regex(@"^\s*@layout\s+(.+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@using",      Regex = new Regex(@"^\s*@using\s+(.+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@inject",     Regex = new Regex(@"^\s*@inject\s+(.+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@typeparam",  Regex = new Regex(@"^\s*@typeparam\s+(.+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@implements", Regex = new Regex(@"^\s*@implements\s+(.+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@attribute",  Regex = new Regex(@"^\s*@attribute\s+(.+?)\s*$", RegexOptions.IgnoreCase) }
            };

            for (int i = 0; i < lines.Length; i++)
            {
                var line = lines[i];

                foreach (var pattern in patterns)
                {
                    var m = pattern.Regex.Match(line);
                    if (!m.Success) continue;

                    list.Add(new
                    {
                        directive = pattern.Name,
                        value = m.Groups.Count > 1 ? m.Groups[1].Value.Trim() : "",
                        line = i + 1
                    });
                    break;
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractInjections(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"^\s*@inject\s+([A-Za-z0-9_<>\.\[\],\?\s]+?)\s+([A-Za-z_][A-Za-z0-9_]*)\s*$",
                RegexOptions.Multiline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                list.Add(new
                {
                    serviceType = m.Groups[1].Value.Trim(),
                    name = m.Groups[2].Value.Trim(),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractCodeBlocks(string code)
        {
            var results = new List<object>();

            for (int i = 0; i < code.Length - 1; i++)
            {
                if (code[i] != '@') continue;

                int look = i + 1;
                while (look < code.Length && char.IsWhiteSpace(code[look])) look++;

                int j = look;
                while (j < code.Length && (char.IsLetter(code[j]) || code[j] == '_')) j++;
                var ident = code.Substring(look, Math.Max(0, j - look));

                if (string.Equals(ident, "code", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(ident, "functions", StringComparison.OrdinalIgnoreCase))
                {
                    int k = j;
                    while (k < code.Length && char.IsWhiteSpace(code[k])) k++;

                    if (k < code.Length && code[k] == '{')
                    {
                        int end = FindBalancedBraceBlock(code, k);
                        if (end > k)
                        {
                            string snippet = code.Substring(i, end - i);
                            results.Add(new
                            {
                                kind = "@" + ident,
                                text = snippet,
                                content = snippet.Substring(snippet.IndexOf('{') + 1).TrimEnd('}', ' ', '\r', '\n', '\t'),
                                //startLine = GetLineNumber(code, i),
                                //endLine = GetLineNumber(code, end - 1)
                            });
                            i = end - 1;
                        }
                    }
                }
            }

            return results.ToArray();
        }

        private static object[] ExtractParameters(object[] codeBlocks)
        {
            var list = new List<object>();

            foreach (var block in codeBlocks)
            {
                var content = GetProp(block, "content");
                if (string.IsNullOrWhiteSpace(content)) continue;

                var rx = new Regex(
                    @"\[(Parameter|CascadingParameter)\]\s*(?:\r?\n|\s)*public\s+([A-Za-z0-9_<>\.\[\],\?\s]+?)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\{",
                    RegexOptions.IgnoreCase | RegexOptions.Singleline);

                foreach (Match m in rx.Matches(content))
                {
                    list.Add(new
                    {
                        attribute = m.Groups[1].Value.Trim(),
                        type = NormalizeWhitespace(m.Groups[2].Value),
                        name = m.Groups[3].Value.Trim()
                    });
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractLifecycleMethods(object[] codeBlocks)
        {
            var list = new List<object>();
            var known = new[]
            {
                "OnInitialized",
                "OnInitializedAsync",
                "OnParametersSet",
                "OnParametersSetAsync",
                "OnAfterRender",
                "OnAfterRenderAsync",
                "SetParametersAsync",
                "ShouldRender"
            };

            foreach (var block in codeBlocks)
            {
                var content = GetProp(block, "content");
                if (string.IsNullOrWhiteSpace(content)) continue;

                foreach (var method in known)
                {
                    foreach (Match m in Regex.Matches(content, $@"\b{Regex.Escape(method)}\s*\(", RegexOptions.IgnoreCase))
                    {
                        list.Add(new
                        {
                            name = method
                        });
                    }
                }
            }

            return DeduplicateObjects(list);
        }

        private static object[] ExtractEventBindings(string code)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<([A-Za-z][A-Za-z0-9\.\-]*)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                var attrs = m.Groups[2].Value;

                foreach (Match em in Regex.Matches(attrs, @"(@on[a-z]+)\s*=\s*(""[^""]*""|'[^']*')", RegexOptions.IgnoreCase))
                {
                    list.Add(new
                    {
                        tag,
                        eventName = em.Groups[1].Value.Trim(),
                        handler = em.Groups[2].Value.Trim().Trim('"', '\''),
                        //line = GetLineNumber(code, m.Index)
                    });
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractBindAttributes(string code)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<([A-Za-z][A-Za-z0-9\.\-]*)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                var attrs = m.Groups[2].Value;

                foreach (Match bm in Regex.Matches(attrs, @"(@bind(?::[A-Za-z0-9_-]+)?)\s*=\s*(""[^""]*""|'[^']*')", RegexOptions.IgnoreCase))
                {
                    list.Add(new
                    {
                        tag,
                        bindName = bm.Groups[1].Value.Trim(),
                        expression = bm.Groups[2].Value.Trim().Trim('"', '\''),
                        //line = GetLineNumber(code, m.Index)
                    });
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractHeadings(string markup)
        {
            var list = new List<object>();
            var rx = new Regex(@"<h([1-6])\b([^>]*)>(.*?)</h\1>", RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[2].Value);
                var text = CleanInnerText(m.Groups[3].Value);
                if (string.IsNullOrWhiteSpace(text)) continue;

                list.Add(new
                {
                    level = "h" + m.Groups[1].Value,
                    text,
                    id = GetAttr(attrs, "id"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractForms(string markup)
        {
            var list = new List<object>();

            var htmlFormRx = new Regex(@"<form\b([^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in htmlFormRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "form",
                    id = GetAttr(attrs, "id"),
                    method = GetAttr(attrs, "method"),
                    action = GetAttr(attrs, "action"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            var editFormRx = new Regex(@"<EditForm\b([^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in editFormRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "EditForm",
                    model = GetAttr(attrs, "Model"),
                    editContext = GetAttr(attrs, "EditContext"),
                    onValidSubmit = GetAttr(attrs, "OnValidSubmit"),
                    onInvalidSubmit = GetAttr(attrs, "OnInvalidSubmit"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractInputs(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(@"<(input|select|textarea|InputText|InputTextArea|InputSelect|InputNumber|InputDate|InputCheckbox)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value;
                var attrs = ParseAttributes(m.Groups[2].Value);

                list.Add(new
                {
                    tag,
                    type = GetAttr(attrs, "type"),
                    id = GetAttr(attrs, "id"),
                    name = GetAttr(attrs, "name"),
                    value = GetAttr(attrs, "value"),
                    placeholder = GetAttr(attrs, "placeholder"),
                    bind = GetAttr(attrs, "@bind") ?? GetAttr(attrs, "@bind-Value") ?? GetAttr(attrs, "Value"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractButtons(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(@"<button\b([^>]*)>(.*?)</button>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    type = GetAttr(attrs, "type"),
                    id = GetAttr(attrs, "id"),
                    text = CleanInnerText(m.Groups[2].Value),
                    cssClass = GetAttr(attrs, "class"),
                    onclick = GetAttr(attrs, "@onclick"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractLinks(string markup)
        {
            var list = new List<object>();

            var anchorRx = new Regex(@"<a\b([^>]*)>(.*?)</a>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in anchorRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "a",
                    href = GetAttr(attrs, "href"),
                    text = CleanInnerText(m.Groups[2].Value),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            var navRx = new Regex(@"<NavLink\b([^>]*)>(.*?)</NavLink>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in navRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "NavLink",
                    href = GetAttr(attrs, "href"),
                    match = GetAttr(attrs, "Match"),
                    text = CleanInnerText(m.Groups[2].Value),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractTables(string markup)
        {
            var list = new List<object>();
            var rx = new Regex(@"<table\b([^>]*)>(.*?)</table>", RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                var inner = m.Groups[2].Value;

                var headers = Regex.Matches(inner, @"<th\b[^>]*>(.*?)</th>", RegexOptions.IgnoreCase | RegexOptions.Singleline)
                    .Cast<Match>()
                    .Select(x => CleanInnerText(x.Groups[1].Value))
                    .Where(x => !string.IsNullOrWhiteSpace(x))
                    .Distinct()
                    .ToArray();

                list.Add(new
                {
                    id = GetAttr(attrs, "id"),
                    cssClass = GetAttr(attrs, "class"),
                    headers,
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractModals(string markup)
        {
            var list = new List<object>();
            var rx = new Regex(@"<([A-Za-z][A-Za-z0-9\.\-]*)\b([^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value;
                var attrs = ParseAttributes(m.Groups[2].Value);

                var id = GetAttr(attrs, "id");
                var cssClass = GetAttr(attrs, "class");
                var combined = $"{id} {cssClass}".ToLowerInvariant();

                if (combined.Contains("modal") || combined.Contains("dialog"))
                {
                    list.Add(new
                    {
                        tag,
                        id,
                        cssClass,
                        //line = GetLineNumber(markup, m.Index)
                    });
                }
            }

            return DeduplicateObjects(list);
        }

        private static object[] ExtractDisplayRegions(string markup)
        {
            var list = new List<object>();
            var rx = new Regex(@"<([A-Za-z][A-Za-z0-9\.\-]*)\b([^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value;
                var attrs = ParseAttributes(m.Groups[2].Value);
                var id = GetAttr(attrs, "id");
                var cssClass = GetAttr(attrs, "class");
                var combined = $"{tag} {id} {cssClass}".ToLowerInvariant();

                string regionType = null;

                if (tag.Equals("table", StringComparison.OrdinalIgnoreCase))
                    regionType = "table-region";
                else if (tag.Equals("canvas", StringComparison.OrdinalIgnoreCase))
                    regionType = "canvas-region";
                else if (combined.Contains("chart") || combined.Contains("graph"))
                    regionType = "chart-region";
                else if (combined.Contains("list"))
                    regionType = "list-region";
                else if (combined.Contains("grid"))
                    regionType = "grid-region";
                else if (combined.Contains("detail"))
                    regionType = "detail-region";
                else if (combined.Contains("summary"))
                    regionType = "summary-region";

                if (regionType == null) continue;

                list.Add(new
                {
                    regionType,
                    tag,
                    id,
                    cssClass,
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return DeduplicateObjects(list);
        }

        private static object[] ExtractComponentUsages(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(@"<([A-Z][A-Za-z0-9_\.]*)(\s[^>]*)?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(markup))
            {
                var component = m.Groups[1].Value;
                var attrs = (m.Groups[2].Value ?? "").Trim();

                if (string.Equals(component, "InputText", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "InputSelect", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "InputTextArea", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "InputNumber", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "InputDate", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "InputCheckbox", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "EditForm", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "NavLink", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "AuthorizeView", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "ValidationSummary", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(component, "ValidationMessage", StringComparison.OrdinalIgnoreCase) ||
                    component.Contains(".") ||
                    char.IsUpper(component[0]))
                {
                    list.Add(new
                    {
                        component,
                        attributes = attrs,
                        //line = GetLineNumber(markup, m.Index)
                    });
                }
            }

            return DeduplicateObjects(list);
        }

        private static object BuildSummaryHints(
            object[] directives,
            object[] injections,
            object[] parameters,
            object[] lifecycleMethods,
            object[] eventBindings,
            object[] bindAttributes,
            object[] forms,
            object[] inputs,
            object[] buttons,
            object[] links,
            object[] tables,
            object[] modals,
            object[] displayRegions,
            object[] componentUsages)
        {
            var clues = new List<string>();

            if (directives.Any(d => string.Equals(GetProp(d, "directive"), "@page", StringComparison.OrdinalIgnoreCase)))
                clues.Add("declares a routable component");
            if (injections.Length > 0)
                clues.Add("injects framework or application services");
            if (parameters.Length > 0)
                clues.Add("accepts component parameters");
            if (lifecycleMethods.Length > 0)
                clues.Add("uses Blazor lifecycle methods");
            if (eventBindings.Length > 0)
                clues.Add("contains component event bindings");
            if (bindAttributes.Length > 0)
                clues.Add("uses bound input or field values");
            if (forms.Length > 0)
                clues.Add("contains form or edit-form handling");
            if (tables.Length > 0)
                clues.Add("contains tabular data display");
            if (modals.Length > 0)
                clues.Add("contains modal or dialog UI");
            if (displayRegions.Any(x => string.Equals(GetProp(x, "regionType"), "chart-region", StringComparison.OrdinalIgnoreCase) ||
                                        string.Equals(GetProp(x, "regionType"), "canvas-region", StringComparison.OrdinalIgnoreCase)))
                clues.Add("contains chart or canvas display areas");
            if (componentUsages.Length > 0)
                clues.Add("uses nested UI components");

            return new
            {
                hasRouteDirective = directives.Any(d => string.Equals(GetProp(d, "directive"), "@page", StringComparison.OrdinalIgnoreCase)),
                hasInjection = injections.Length > 0,
                hasParameters = parameters.Length > 0,
                hasLifecycleMethods = lifecycleMethods.Length > 0,
                hasEventBindings = eventBindings.Length > 0,
                hasBoundInputs = bindAttributes.Length > 0,
                hasForms = forms.Length > 0,
                hasTabularDisplay = tables.Length > 0,
                hasModalDialog = modals.Length > 0,
                hasNestedComponents = componentUsages.Length > 0,
                clues
            };
        }

        private static string BuildMarkupOnlyView(string code)
        {
            var text = code ?? "";

            text = RemoveNamedBalancedRazorBlocks(text, "@code");
            text = RemoveNamedBalancedRazorBlocks(text, "@functions");

            return text;
        }

        private static string RemoveNamedBalancedRazorBlocks(string text, string marker)
        {
            int index = 0;
            while (index < text.Length)
            {
                int start = text.IndexOf(marker, index, StringComparison.OrdinalIgnoreCase);
                if (start < 0) break;

                int braceIndex = start + marker.Length;
                while (braceIndex < text.Length && char.IsWhiteSpace(text[braceIndex])) braceIndex++;

                if (braceIndex >= text.Length || text[braceIndex] != '{')
                {
                    index = start + marker.Length;
                    continue;
                }

                int end = FindBalancedBraceBlock(text, braceIndex);
                if (end <= braceIndex)
                {
                    index = start + marker.Length;
                    continue;
                }

                text = text.Substring(0, start) + new string(' ', end - start) + text.Substring(end);
                index = end;
            }

            return text;
        }

        private static int FindBalancedBraceBlock(string text, int openBraceIndex)
        {
            if (openBraceIndex < 0 || openBraceIndex >= text.Length || text[openBraceIndex] != '{')
                return -1;

            int depth = 1;
            int pos = openBraceIndex + 1;

            while (pos < text.Length && depth > 0)
            {
                char c = text[pos];

                if (c == '"' || c == '\'')
                {
                    char quote = c;
                    pos++;
                    while (pos < text.Length)
                    {
                        if (text[pos] == '\\')
                        {
                            pos += 2;
                            continue;
                        }
                        if (text[pos] == quote)
                        {
                            pos++;
                            break;
                        }
                        pos++;
                    }
                    continue;
                }

                if (c == '{') depth++;
                else if (c == '}') depth--;

                pos++;
            }

            return depth == 0 ? pos : -1;
        }

        private static Dictionary<string, string> ParseAttributes(string raw)
        {
            var dict = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            if (string.IsNullOrWhiteSpace(raw)) return dict;

            var rx = new Regex(
                @"([a-zA-Z_:@][a-zA-Z0-9_:\-\.@]*)\s*=\s*(""([^""]*)""|'([^']*)'|([^\s""'=<>`]+))",
                RegexOptions.Singleline);

            foreach (Match m in rx.Matches(raw))
            {
                var key = m.Groups[1].Value.Trim();
                var value =
                    m.Groups[3].Success ? m.Groups[3].Value :
                    m.Groups[4].Success ? m.Groups[4].Value :
                    m.Groups[5].Success ? m.Groups[5].Value :
                    "";

                dict[key] = value.Trim();
            }

            return dict;
        }

        private static string GetAttr(Dictionary<string, string> attrs, string name)
            => attrs.TryGetValue(name, out var value) ? value : null;

        private static string CleanInnerText(string html)
        {
            if (string.IsNullOrWhiteSpace(html)) return string.Empty;

            var text = Regex.Replace(html, @"<[^>]+>", " ");
            text = System.Net.WebUtility.HtmlDecode(text);
            text = Regex.Replace(text, @"\s+", " ").Trim();
            return text;
        }

        private static string NormalizeNewlines(string text)
            => (text ?? "").Replace("\r\n", "\n").Replace("\r", "\n");

        private static int GetLineNumber(string text, int index)
        {
            if (index <= 0) return 1;
            index = Math.Min(index, text.Length);

            int line = 1;
            for (int i = 0; i < index; i++)
            {
                if (text[i] == '\n') line++;
            }
            return line;
        }

        private static string GetProp(object obj, string propName)
        {
            var prop = obj.GetType().GetProperty(propName);
            return prop?.GetValue(obj)?.ToString();
        }

        private static object[] DeduplicateObjects(IEnumerable<object> items)
        {
            return items
                .GroupBy(x => Newtonsoft.Json.JsonConvert.SerializeObject(x))
                .Select(g => g.First())
                .ToArray();
        }

        private static string NormalizeWhitespace(string value)
        {
            if (string.IsNullOrWhiteSpace(value)) return value;
            return Regex.Replace(value, @"\s+", " ").Trim();
        }
    }
}
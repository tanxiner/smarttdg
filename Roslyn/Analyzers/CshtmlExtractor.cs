using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class CshtmlExtractor
    {
        public static bool IsCshtmlPath(string filePath)
            => !string.IsNullOrEmpty(filePath) &&
               filePath.EndsWith(".cshtml", StringComparison.OrdinalIgnoreCase);

        public static bool IsRazorComponentPath(string filePath)
            => !string.IsNullOrEmpty(filePath) &&
               filePath.EndsWith(".razor", StringComparison.OrdinalIgnoreCase);

        public static object Analyze(string code, string filePath)
        {
            code ??= string.Empty;

            var modelDeclarations = ExtractModelDeclarations(code);
            var directives = ExtractDirectives(code);
            var razorCodeBlocks = ExtractRazorAndNamedCodeBlocks(code);
            var beginForms = ExtractBeginForms(code);
            var scriptBlocks = ExtractScriptBlocks(code);
            var scriptHints = ExtractScriptHints(code);
            var razorDataHints = ExtractRazorDataHints(code);
            var pageMetadata = ExtractPageMetadata(code);

            // Strip Razor code/script bodies before HTML-like extraction
            var markupOnly = BuildMarkupOnlyView(code);

            var headings = ExtractHeadings(markupOnly);
            var forms = ExtractHtmlForms(markupOnly).Concat(beginForms).ToArray();
            var inputs = ExtractInputs(markupOnly);
            var buttons = ExtractButtons(markupOnly);
            var links = ExtractUsefulLinks(markupOnly);
            var tables = ExtractTables(markupOnly);
            var displayRegions = ExtractDisplayRegions(markupOnly);
            var modals = ExtractModals(markupOnly);
            var interactiveElements = ExtractInteractiveElements(markupOnly);

            var pageSummaryHints = BuildPageSummaryHints(
                modelDeclarations,
                forms,
                inputs,
                buttons,
                links,
                tables,
                displayRegions,
                modals,
                interactiveElements,
                scriptHints,
                razorDataHints
            );

            return new
            {
                file = System.IO.Path.GetFileName(filePath ?? ""),
                path = filePath,
                isCshtml = IsCshtmlPath(filePath ?? ""),
                isRazorComponent = false,

                pageMetadata,
                modelDeclarations,
                directives,
                razorCodeBlocks,
                forms,
                inputs,
                buttons,
                links,
                headings,
                tables,
                displayRegions,
                modals,
                interactiveElements,
                scriptBlocks,
                scriptHints,
                razorDataHints,
                pageSummaryHints
            };
        }

        // =========================
        // Metadata / directives
        // =========================

        private static object ExtractPageMetadata(string code)
        {
            string title = null;

            var titleMatch = Regex.Match(
                code,
                @"ViewBag\.Title\s*=\s*""([^""]+)""",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            if (titleMatch.Success)
            {
                title = titleMatch.Groups[1].Value.Trim();
            }

            return new
            {
                title
            };
        }

        private static object[] ExtractModelDeclarations(string code)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"^\s*@model\s+([^\r\n]+)$",
                RegexOptions.Multiline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                list.Add(new
                {
                    text = m.Value.Trim(),
                    modelType = m.Groups[1].Value.Trim(),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractDirectives(string code)
        {
            var list = new List<object>();
            var lines = NormalizeNewlines(code).Split('\n');

            var patterns = new[]
            {
                new { Name = "@using",      Regex = new Regex(@"^\s*@using\s+([A-Za-z_][A-Za-z0-9_\.]*(?:\s*;\s*)?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@inherits",   Regex = new Regex(@"^\s*@inherits\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@inject",     Regex = new Regex(@"^\s*@inject\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@layout",     Regex = new Regex(@"^\s*@layout\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@page",       Regex = new Regex(@"^\s*@page(?:\s+([^\r\n]+?))?\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@typeparam",  Regex = new Regex(@"^\s*@typeparam\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@implements", Regex = new Regex(@"^\s*@implements\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) },
                new { Name = "@attribute",  Regex = new Regex(@"^\s*@attribute\s+([^\r\n]+?)\s*$", RegexOptions.IgnoreCase) }
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

        // =========================
        // Razor block extraction
        // =========================

        private static object[] ExtractRazorAndNamedCodeBlocks(string code)
        {
            var results = new List<object>();

            for (int i = 0; i < code.Length - 1; i++)
            {
                if (code[i] != '@') continue;

                int look = i + 1;
                while (look < code.Length && char.IsWhiteSpace(code[look])) look++;

                if (look < code.Length && code[look] == '{')
                {
                    int end = FindBalancedBraceBlock(code, look);
                    if (end > look)
                    {
                        string snippet = code.Substring(i, end - i);
                        results.Add(new
                        {
                            kind = "@{ }",
                            text = snippet,
                            content = snippet.Length > 2
                                ? snippet.Substring(2, Math.Max(0, snippet.Length - 3)).Trim()
                                : string.Empty,
                            //startLine = GetLineNumber(code, i),
                            //endLine = GetLineNumber(code, end - 1)
                        });
                        i = end - 1;
                        continue;
                    }
                }

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

        private static object[] ExtractBeginForms(string code)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"@using\s*\(\s*Html\.BeginForm\s*\((.*?)\)\s*\)",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(code))
            {
                var args = m.Groups[1].Value;

                string action = ExtractQuotedArgument(args, 1);
                string controller = ExtractQuotedArgument(args, 2);
                string method = ExtractFormMethod(args);
                string formId = ExtractAnonymousHtmlAttribute(args, "id");
                string role = ExtractAnonymousHtmlAttribute(args, "role");

                list.Add(new
                {
                    source = "Html.BeginForm",
                    action,
                    controller,
                    method,
                    id = formId,
                    role,
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        // =========================
        // HTML / markup extraction
        // =========================

        private static object[] ExtractHeadings(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<h([1-6])\b([^>]*)>(.*?)</h\1>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

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

        private static object[] ExtractHtmlForms(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<form\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);

                list.Add(new
                {
                    source = "form",
                    action = GetAttr(attrs, "action"),
                    method = GetAttr(attrs, "method"),
                    id = GetAttr(attrs, "id"),
                    role = GetAttr(attrs, "role"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractInputs(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<(input|select|textarea)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value.ToLowerInvariant();
                var attrs = ParseAttributes(m.Groups[2].Value);

                list.Add(new
                {
                    tag,
                    type = GetAttr(attrs, "type"),
                    name = GetAttr(attrs, "name"),
                    id = GetAttr(attrs, "id"),
                    value = GetAttr(attrs, "value"),
                    placeholder = GetAttr(attrs, "placeholder"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractButtons(string markup)
        {
            var list = new List<object>();

            var buttonRx = new Regex(
                @"<button\b([^>]*)>(.*?)</button>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in buttonRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);

                list.Add(new
                {
                    tag = "button",
                    type = GetAttr(attrs, "type"),
                    id = GetAttr(attrs, "id"),
                    text = CleanInnerText(m.Groups[2].Value),
                    cssClass = GetAttr(attrs, "class"),
                    dataDismiss = GetAttr(attrs, "data-dismiss"),
                    dataToggle = GetAttr(attrs, "data-toggle"),
                    title = GetAttr(attrs, "title"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            var inputButtonRx = new Regex(
                @"<input\b([^>]*\btype\s*=\s*[""']?(button|submit|reset)[""']?[^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in inputButtonRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "input",
                    type = GetAttr(attrs, "type"),
                    id = GetAttr(attrs, "id"),
                    text = GetAttr(attrs, "value"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractUsefulLinks(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<a\b([^>]*)>(.*?)</a>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                var href = GetAttr(attrs, "href");
                var onclick = GetAttr(attrs, "onclick");
                var title = GetAttr(attrs, "title");
                var cssClass = GetAttr(attrs, "class");
                var text = CleanInnerText(m.Groups[2].Value);

                bool useful =
                    !string.IsNullOrWhiteSpace(href) ||
                    !string.IsNullOrWhiteSpace(onclick) ||
                    !string.IsNullOrWhiteSpace(text) ||
                    !string.IsNullOrWhiteSpace(title);

                if (!useful) continue;

                list.Add(new
                {
                    href,
                    onclick,
                    title,
                    text,
                    cssClass,
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractTables(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<table\b([^>]*)>(.*?)</table>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                var inner = m.Groups[2].Value;

                var headers = Regex.Matches(
                        inner,
                        @"<th\b[^>]*>(.*?)</th>",
                        RegexOptions.IgnoreCase | RegexOptions.Singleline)
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

        private static object[] ExtractDisplayRegions(string markup)
        {
            var list = new List<object>();

            var canvasRx = new Regex(
                @"<canvas\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in canvasRx.Matches(markup))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    regionType = "canvas",
                    tag = "canvas",
                    id = GetAttr(attrs, "id"),
                    cssClass = GetAttr(attrs, "class"),
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            var rx = new Regex(
                @"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value.ToLowerInvariant();
                var attrs = ParseAttributes(m.Groups[2].Value);

                var id = GetAttr(attrs, "id");
                var cssClass = GetAttr(attrs, "class");
                var combined = $"{id} {cssClass}".ToLowerInvariant();

                string regionType = null;

                if (combined.Contains("chart") || combined.Contains("graph"))
                    regionType = "chart-region";
                else if (combined.Contains("timetable"))
                    regionType = "timetable-region";
                else if (combined.Contains("popup"))
                    regionType = "popup-region";
                else if (combined.Contains("modal"))
                    regionType = "modal-region";
                else if (combined.Contains("breadcrumb"))
                    regionType = "breadcrumb-region";
                else if (combined.Contains("sidebar"))
                    regionType = "sidebar-region";
                else if (combined.Contains("main-content"))
                    regionType = "main-content-region";
                else if (combined.Contains("document"))
                    regionType = "document-region";
                else if (combined.Contains("table"))
                    regionType = "table-region";
                else if (combined.Contains("box"))
                    regionType = "panel-region";

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

        private static object[] ExtractModals(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value.ToLowerInvariant();
                var attrs = ParseAttributes(m.Groups[2].Value);

                var id = GetAttr(attrs, "id");
                var cssClass = GetAttr(attrs, "class");
                var role = GetAttr(attrs, "role");
                var combined = $"{id} {cssClass} {role}".ToLowerInvariant();

                if (!combined.Contains("modal")) continue;

                list.Add(new
                {
                    tag,
                    id,
                    cssClass,
                    role,
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return DeduplicateObjects(list);
        }

        private static object[] ExtractInteractiveElements(string markup)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*)>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(markup))
            {
                var tag = m.Groups[1].Value.ToLowerInvariant();
                var attrs = ParseAttributes(m.Groups[2].Value);

                var id = GetAttr(attrs, "id");
                var cssClass = GetAttr(attrs, "class");
                var href = GetAttr(attrs, "href");
                var onclick = GetAttr(attrs, "onclick");
                var dataToggle = GetAttr(attrs, "data-toggle");
                var dataDismiss = GetAttr(attrs, "data-dismiss");
                var dataStop = GetAttr(attrs, "data-stop");
                var dataDir = GetAttr(attrs, "data-dir");
                var title = GetAttr(attrs, "title");

                bool isInteractive =
                    tag == "form" ||
                    tag == "input" ||
                    tag == "select" ||
                    tag == "textarea" ||
                    tag == "button" ||
                    tag == "a" ||
                    !string.IsNullOrWhiteSpace(onclick) ||
                    !string.IsNullOrWhiteSpace(dataToggle) ||
                    !string.IsNullOrWhiteSpace(dataDismiss) ||
                    !string.IsNullOrWhiteSpace(dataStop) ||
                    !string.IsNullOrWhiteSpace(dataDir);

                if (!isInteractive) continue;

                list.Add(new
                {
                    tag,
                    id,
                    cssClass,
                    href,
                    onclick,
                    dataToggle,
                    dataDismiss,
                    dataStop,
                    dataDir,
                    title,
                    //line = GetLineNumber(markup, m.Index)
                });
            }

            return list.ToArray();
        }

        // =========================
        // Scripts / Razor data hints
        // =========================

        private static object[] ExtractScriptBlocks(string code)
        {
            var list = new List<object>();

            var rx = new Regex(
                @"<script\b([^>]*)>(.*?)</script\s*>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            foreach (Match m in rx.Matches(code))
            {
                list.Add(new
                {
                    tag = "script",
                    attributes = (m.Groups[1].Value ?? "").Trim(),
                    content = (m.Groups[2].Value ?? "").Trim(),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractScriptHints(string code)
        {
            var list = new List<object>();

            foreach (Match m in Regex.Matches(code, @"window\.[A-Za-z_][A-Za-z0-9_]*\s*=", RegexOptions.IgnoreCase))
            {
                list.Add(new
                {
                    hintType = "window-assignment",
                    value = m.Value.Trim(),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            foreach (Match m in Regex.Matches(code, @"@Url\.Action\s*\(\s*""([^""]+)""\s*,\s*""([^""]+)""\s*\)", RegexOptions.IgnoreCase))
            {
                list.Add(new
                {
                    hintType = "url-action",
                    value = $"{m.Groups[1].Value}|{m.Groups[2].Value}",
                    //line = GetLineNumber(code, m.Index)
                });
            }

            foreach (Match m in Regex.Matches(code, @"\$\((window|document)\)\.on\s*\(\s*['""]([A-Za-z]+)['""]", RegexOptions.IgnoreCase))
            {
                list.Add(new
                {
                    hintType = "event-binding",
                    value = $"{m.Groups[1].Value}:{m.Groups[2].Value}",
                    //line = GetLineNumber(code, m.Index)
                });
            }

            foreach (Match m in Regex.Matches(code, @"\binit\s*\(", RegexOptions.IgnoreCase))
            {
                list.Add(new
                {
                    hintType = "init-call",
                    value = "init(",
                    //line = GetLineNumber(code, m.Index)
                });
            }

            foreach (Match m in Regex.Matches(code, @"\bdraw[A-Za-z0-9_]*\s*\(", RegexOptions.IgnoreCase))
            {
                list.Add(new
                {
                    hintType = "draw-call",
                    value = m.Value.Trim(),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return DeduplicateObjects(list);
        }

        private static object ExtractRazorDataHints(string code)
        {
            var modelProps = Regex.Matches(code, @"\bModel\.([A-Za-z_][A-Za-z0-9_]*)", RegexOptions.IgnoreCase)
                .Cast<Match>()
                .Select(m => m.Groups[1].Value)
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .OrderBy(x => x)
                .ToArray();

            var viewBagKeys = Regex.Matches(code, @"\bViewBag\.([A-Za-z_][A-Za-z0-9_]*)", RegexOptions.IgnoreCase)
                .Cast<Match>()
                .Select(m => m.Groups[1].Value)
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .OrderBy(x => x)
                .ToArray();

            var controllerCalls = Regex.Matches(code, @"\bcontroller\.([A-Za-z_][A-Za-z0-9_]*)\s*\(", RegexOptions.IgnoreCase)
                .Cast<Match>()
                .Select(m => m.Groups[1].Value)
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .OrderBy(x => x)
                .ToArray();

            var helperCalls = Regex.Matches(code, @"\b([A-Za-z_][A-Za-z0-9_]*)\.([A-Za-z_][A-Za-z0-9_]*)\s*\(", RegexOptions.IgnoreCase)
                .Cast<Match>()
                .Select(m => $"{m.Groups[1].Value}.{m.Groups[2].Value}")
                .Where(x =>
                    !x.StartsWith("Model.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("ViewBag.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("Html.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("Url.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("string.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("Convert.", StringComparison.OrdinalIgnoreCase) &&
                    !x.StartsWith("Regex.", StringComparison.OrdinalIgnoreCase))
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .OrderBy(x => x)
                .ToArray();

            return new
            {
                modelPropertiesUsed = modelProps,
                viewBagKeysUsed = viewBagKeys,
                controllerCalls,
                helperCalls
            };
        }

        // =========================
        // Summary hints
        // =========================

        private static object BuildPageSummaryHints(
            object[] modelDeclarations,
            object[] forms,
            object[] inputs,
            object[] buttons,
            object[] links,
            object[] tables,
            object[] displayRegions,
            object[] modals,
            object[] interactiveElements,
            object[] scriptHints,
            object razorDataHints)
        {
            var inputTypes = inputs
                .Select(x => GetProp(x, "type"))
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .ToArray();

            var regionTypes = displayRegions
                .Select(x => GetProp(x, "regionType"))
                .Where(x => !string.IsNullOrWhiteSpace(x))
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .ToArray();

            var clues = new List<string>();

            if (modelDeclarations.Length > 0) clues.Add("uses model binding");
            if (forms.Length > 0) clues.Add("contains form submission flow");
            if (inputs.Length > 0) clues.Add("contains user input controls");
            if (inputTypes.Any(x => string.Equals(x, "radio", StringComparison.OrdinalIgnoreCase)))
                clues.Add("contains option selection via radio inputs");
            if (tables.Length > 0) clues.Add("contains tabular data display");
            if (regionTypes.Any(x => x.Contains("chart", StringComparison.OrdinalIgnoreCase) || x.Contains("canvas", StringComparison.OrdinalIgnoreCase)))
                clues.Add("contains chart or canvas display regions");
            if (regionTypes.Any(x => x.Contains("timetable", StringComparison.OrdinalIgnoreCase)))
                clues.Add("contains timetable-style display regions");
            if (modals.Length > 0) clues.Add("contains modal or popup display");
            if (links.Any(x => !string.IsNullOrWhiteSpace(GetProp(x, "onclick"))))
                clues.Add("contains click-driven navigation");
            if (interactiveElements.Any(x => !string.IsNullOrWhiteSpace(GetProp(x, "dataStop"))))
                clues.Add("contains item-specific interactive detail triggers");
            if (scriptHints.Length > 0) clues.Add("contains client-side initialization or scripting hooks");

            return new
            {
                hasModelBinding = modelDeclarations.Length > 0,
                hasFormSubmission = forms.Length > 0,
                hasFilteringControls = inputTypes.Any(x =>
                    string.Equals(x, "radio", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(x, "checkbox", StringComparison.OrdinalIgnoreCase)),
                hasSelectionControls = inputs.Any(x =>
                    string.Equals(GetProp(x, "tag"), "select", StringComparison.OrdinalIgnoreCase) ||
                    !string.IsNullOrWhiteSpace(GetProp(x, "name"))),
                hasTabularDisplay = tables.Length > 0,
                hasChartOrCanvasRegion = regionTypes.Any(x =>
                    x.Contains("chart", StringComparison.OrdinalIgnoreCase) ||
                    x.Contains("canvas", StringComparison.OrdinalIgnoreCase)),
                hasModalDialog = modals.Length > 0,
                hasPopupTrigger = interactiveElements.Any(x =>
                    !string.IsNullOrWhiteSpace(GetProp(x, "dataToggle")) ||
                    !string.IsNullOrWhiteSpace(GetProp(x, "dataStop"))),
                hasClientSideInitialization = scriptHints.Any(x =>
                    string.Equals(GetProp(x, "hintType"), "init-call", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(GetProp(x, "hintType"), "event-binding", StringComparison.OrdinalIgnoreCase)),
                hasAjaxEndpoints = scriptHints.Any(x =>
                    string.Equals(GetProp(x, "hintType"), "url-action", StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(GetProp(x, "hintType"), "window-assignment", StringComparison.OrdinalIgnoreCase)),
                clues
            };
        }

        // =========================
        // Helpers
        // =========================

        private static string BuildMarkupOnlyView(string code)
        {
            var text = code;

            // Remove script bodies entirely but keep outer tags shape from being parsed as content
            text = Regex.Replace(
                text,
                @"<script\b[^>]*>.*?</script\s*>",
                " ",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            // Remove Razor code blocks @{ ... }, @code { ... }, @functions { ... }
            text = RemoveBalancedRazorBlocks(text, "@{");
            text = RemoveNamedBalancedRazorBlocks(text, "@code");
            text = RemoveNamedBalancedRazorBlocks(text, "@functions");

            // Remove inline control expressions that often inject code noise
            text = Regex.Replace(text, @"@\b(if|for|foreach|while|switch)\b[^{\r\n]*\{", " ", RegexOptions.IgnoreCase);
            text = Regex.Replace(text, @"@Html\.[A-Za-z0-9_]+\s*\([^)]*\)", " ", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            text = Regex.Replace(text, @"@Url\.[A-Za-z0-9_]+\s*\([^)]*\)", " ", RegexOptions.IgnoreCase | RegexOptions.Singleline);

            return text;
        }

        private static string RemoveBalancedRazorBlocks(string text, string marker)
        {
            int index = 0;
            while (index < text.Length)
            {
                int start = text.IndexOf(marker, index, StringComparison.Ordinal);
                if (start < 0) break;

                int braceIndex = start + marker.Length - 1; // points at {
                if (braceIndex < 0 || braceIndex >= text.Length || text[braceIndex] != '{')
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

            if (string.IsNullOrWhiteSpace(raw))
                return dict;

            var rx = new Regex(
                @"([a-zA-Z_:][a-zA-Z0-9_:\-\.]*)\s*=\s*(""([^""]*)""|'([^']*)'|([^\s""'=<>`]+))",
                RegexOptions.Singleline);

            foreach (Match m in rx.Matches(raw))
            {
                string key = m.Groups[1].Value.Trim();
                string value =
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

        private static string ExtractQuotedArgument(string args, int argumentPosition)
        {
            var matches = Regex.Matches(args, @"""([^""]*)""");
            if (matches.Count >= argumentPosition)
                return matches[argumentPosition - 1].Groups[1].Value.Trim();

            return null;
        }

        private static string ExtractFormMethod(string args)
        {
            var m = Regex.Match(args, @"\bFormMethod\.(Get|Post)\b", RegexOptions.IgnoreCase);
            return m.Success ? m.Groups[1].Value : null;
        }

        private static string ExtractAnonymousHtmlAttribute(string args, string attributeName)
        {
            var rx = new Regex(
                $@"@\s*{Regex.Escape(attributeName)}\s*=\s*""([^""]*)""",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            var m = rx.Match(args);
            return m.Success ? m.Groups[1].Value.Trim() : null;
        }
    }
}
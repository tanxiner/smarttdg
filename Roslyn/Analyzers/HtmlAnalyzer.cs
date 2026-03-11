using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class HtmlAnalyzer
    {
        public static bool IsHtmlPath(string filePath)
            => !string.IsNullOrEmpty(filePath) &&
               (filePath.EndsWith(".html", StringComparison.OrdinalIgnoreCase) ||
                filePath.EndsWith(".htm", StringComparison.OrdinalIgnoreCase));

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            try
            {
                var scripts = ExtractScriptBlocks(code);
                var forms = ExtractForms(code);
                var links = ExtractLinks(code);
                var buttons = ExtractButtons(code);
                var headings = ExtractHeadings(code);
                var tables = ExtractTables(code);
                var displayRegions = ExtractDisplayRegions(code);
                var inlineEvents = ExtractInlineEvents(code);
                var ids = ExtractAttributeValues(code, "id");
                var classes = ExtractClassList(code);
                var assets = ExtractAssets(code);
                var summaryHints = BuildSummaryHints(
                    scripts, forms, links, buttons, headings, tables, displayRegions, inlineEvents, assets
                );

                return new
                {
                    file = Path.GetFileName(filePath ?? ""),
                    path = filePath,
                    isHtml = IsHtmlPath(filePath ?? ""),
                    scripts,
                    forms,
                    links,
                    buttons,
                    headings,
                    tables,
                    displayRegions,
                    inlineEventAttrs = inlineEvents,
                    assets,
                    ids,
                    classes,
                    summaryHints
                };
            }
            catch (Exception ex)
            {
                return new
                {
                    file = Path.GetFileName(filePath ?? ""),
                    path = filePath,
                    isHtml = IsHtmlPath(filePath ?? ""),
                    error = ex.Message
                };
            }
        }

        private static object[] ExtractScriptBlocks(string code)
        {
            var rx = new Regex(
                @"<script\b(?<attrs>(?:[^'""<>]|'[^']*'|""[^""]*"")*)>(?<inner>.*?)</script\s*>",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups["attrs"].Value ?? "").Trim();
                string rawSrc = ExtractAttribute(attrs, "src");

                string normalizedSrc = null;
                string srcFileName = null;
                bool hasQuery = false;

                if (!string.IsNullOrEmpty(rawSrc))
                {
                    var qIdx = rawSrc.IndexOf('?');
                    hasQuery = qIdx >= 0;
                    normalizedSrc = qIdx >= 0 ? rawSrc.Substring(0, qIdx) : rawSrc;
                    normalizedSrc = normalizedSrc.Trim().Trim('\'', '"');
                    if (!string.IsNullOrEmpty(normalizedSrc))
                        srcFileName = Path.GetFileName(normalizedSrc);
                }

                list.Add(new
                {
                    rawSrc,
                    normalizedSrc,
                    srcFileName,
                    hasQuery
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractForms(string code)
        {
            var rxForm = new Regex(@"<form\b([^>]*)>(.*?)</form\s*>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            var fieldRx = new Regex(@"<(input|select|textarea)\b([^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            var list = new List<object>();

            foreach (Match m in rxForm.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var inner = (m.Groups[2].Value ?? "");
                var action = ExtractAttribute(attrs, "action");
                var method = (ExtractAttribute(attrs, "method") ?? "GET").ToUpperInvariant();

                var fields = new List<object>();
                foreach (Match f in fieldRx.Matches(inner))
                {
                    var fAttrs = (f.Groups[2].Value ?? "").Trim();
                    var name = ExtractAttribute(fAttrs, "name") ?? ExtractAttribute(fAttrs, "id");
                    var type = ExtractAttribute(fAttrs, "type") ?? f.Groups[1].Value;

                    if (!string.IsNullOrEmpty(name))
                        fields.Add(new { name, type });
                }

                list.Add(new
                {
                    action,
                    method,
                    fields = fields.ToArray()
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractLinks(string code)
        {
            var rx = new Regex(@"<a\b([^>]*?)href\s*=\s*(['""]?)([^'"">\s]+)\2([^>]*)>(.*?)</a\s*>",
                RegexOptions.Singleline | RegexOptions.IgnoreCase);

            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var href = m.Groups[3].Value;
                var text = Regex.Replace(m.Groups[5].Value ?? "", @"\s+", " ").Trim();
                list.Add(new { href, text });
            }

            return list.ToArray();
        }

        private static object[] ExtractButtons(string code)
        {
            var list = new List<object>();

            var buttonRx = new Regex(@"<button\b([^>]*)>(.*?)</button\s*>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            foreach (Match m in buttonRx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                list.Add(new
                {
                    tag = "button",
                    type = ExtractAttribute(attrs, "type"),
                    id = ExtractAttribute(attrs, "id"),
                    text = Regex.Replace(m.Groups[2].Value ?? "", @"\s+", " ").Trim(),
                    cssClass = ExtractAttribute(attrs, "class")
                });
            }

            var inputRx = new Regex(@"<input\b([^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            foreach (Match m in inputRx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var type = ExtractAttribute(attrs, "type");
                if (!string.Equals(type, "submit", StringComparison.OrdinalIgnoreCase) &&
                    !string.Equals(type, "button", StringComparison.OrdinalIgnoreCase) &&
                    !string.Equals(type, "reset", StringComparison.OrdinalIgnoreCase))
                    continue;

                list.Add(new
                {
                    tag = "input",
                    type,
                    id = ExtractAttribute(attrs, "id"),
                    text = ExtractAttribute(attrs, "value"),
                    cssClass = ExtractAttribute(attrs, "class")
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractHeadings(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<h([1-6])\b([^>]*)>(.*?)</h\1>", RegexOptions.Singleline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups[2].Value ?? "").Trim();
                var text = Regex.Replace(m.Groups[3].Value ?? "", "<[^>]+>", " ");
                text = Regex.Replace(text, @"\s+", " ").Trim();

                if (string.IsNullOrWhiteSpace(text)) continue;

                list.Add(new
                {
                    level = "h" + m.Groups[1].Value,
                    text,
                    id = ExtractAttribute(attrs, "id"),
                    cssClass = ExtractAttribute(attrs, "class")
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractTables(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<table\b([^>]*)>(.*?)</table\s*>", RegexOptions.Singleline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var inner = m.Groups[2].Value ?? "";

                var headers = Regex.Matches(inner, @"<th\b[^>]*>(.*?)</th>", RegexOptions.Singleline | RegexOptions.IgnoreCase)
                    .Cast<Match>()
                    .Select(x => Regex.Replace(x.Groups[1].Value ?? "", "<[^>]+>", " "))
                    .Select(x => Regex.Replace(x, @"\s+", " ").Trim())
                    .Where(x => !string.IsNullOrWhiteSpace(x))
                    .Distinct()
                    .ToArray();

                list.Add(new
                {
                    id = ExtractAttribute(attrs, "id"),
                    cssClass = ExtractAttribute(attrs, "class"),
                    headers
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractDisplayRegions(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value.ToLowerInvariant();
                var attrs = (m.Groups[2].Value ?? "").Trim();
                var id = ExtractAttribute(attrs, "id");
                var cssClass = ExtractAttribute(attrs, "class");
                var combined = $"{tag} {id} {cssClass}".ToLowerInvariant();

                string regionType = null;

                if (tag == "canvas") regionType = "canvas-region";
                else if (combined.Contains("chart") || combined.Contains("graph")) regionType = "chart-region";
                else if (combined.Contains("modal") || combined.Contains("dialog")) regionType = "modal-region";
                else if (combined.Contains("list")) regionType = "list-region";
                else if (combined.Contains("grid")) regionType = "grid-region";
                else if (combined.Contains("detail")) regionType = "detail-region";
                else if (combined.Contains("summary")) regionType = "summary-region";

                if (regionType == null) continue;

                list.Add(new
                {
                    regionType,
                    tag,
                    id,
                    cssClass
                });
            }

            return list
                .GroupBy(x => Newtonsoft.Json.JsonConvert.SerializeObject(x))
                .Select(g => g.First())
                .ToArray();
        }

        private static object[] ExtractAssets(string code)
        {
            var list = new List<object>();

            foreach (Match m in Regex.Matches(code, @"<img\b([^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var src = ExtractAttribute(attrs, "src");
                if (!string.IsNullOrWhiteSpace(src))
                {
                    list.Add(new { tag = "img", src });
                }
            }

            foreach (Match m in Regex.Matches(code, @"<link\b([^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var href = ExtractAttribute(attrs, "href");
                var rel = ExtractAttribute(attrs, "rel");
                if (!string.IsNullOrWhiteSpace(href))
                {
                    list.Add(new { tag = "link", rel, href });
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractInlineEvents(string code)
        {
            var attrs = new[] { "onclick", "onsubmit", "onchange", "oninput", "onblur", "onfocus" };
            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*?(?:\b" + string.Join("|\\b", attrs) + @")[^>]*)>",
                RegexOptions.Singleline | RegexOptions.IgnoreCase);

            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                var allAttrs = m.Groups[2].Value;
                var selector = InlineElementSelector(allAttrs, tag);
                var ev = new Dictionary<string, string>();

                foreach (var a in attrs)
                {
                    var val = ExtractAttribute(allAttrs, a);
                    if (val != null) ev[a] = val;
                }

                list.Add(new { selector, events = ev });
            }

            return list.ToArray();
        }

        private static string[] ExtractAttributeValues(string code, string attrName)
        {
            var rx = new Regex($@"\b{Regex.Escape(attrName)}\s*=\s*(['""])(.*?)\1", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            var vals = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var v = m.Groups[2].Value.Trim();
                if (!string.IsNullOrEmpty(v)) vals.Add(v);
            }

            return vals.ToArray();
        }

        private static string[] ExtractClassList(string code)
        {
            var rx = new Regex(@"\bclass\s*=\s*(['""])(.*?)\1", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            var set = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var v = m.Groups[2].Value;
                foreach (var c in v.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries))
                    set.Add(c.Trim());
            }

            return set.ToArray();
        }

        private static string ExtractAttribute(string attrText, string name)
        {
            if (string.IsNullOrEmpty(attrText)) return null;

            var rx = new Regex(
                @"\b" + Regex.Escape(name) + @"\s*=\s*(?:(['""])(.*?)\1|([^\s>]+))",
                RegexOptions.IgnoreCase | RegexOptions.Singleline);

            var m = rx.Match(attrText);
            return m.Success
                ? (m.Groups[2].Success ? m.Groups[2].Value : m.Groups[3].Value)
                : null;
        }

        private static string InlineElementSelector(string attrText, string tag)
        {
            var id = ExtractAttribute(attrText, "id");
            if (!string.IsNullOrEmpty(id)) return $"#{id}";

            var cls = ExtractAttribute(attrText, "class");
            if (!string.IsNullOrEmpty(cls))
                return "." + cls.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault();

            return tag;
        }

        private static object BuildSummaryHints(
            object[] scripts,
            object[] forms,
            object[] links,
            object[] buttons,
            object[] headings,
            object[] tables,
            object[] displayRegions,
            object[] inlineEvents,
            object[] assets)
        {
            var clues = new List<string>();

            if (scripts.Length > 0) clues.Add("contains client-side script references");
            if (forms.Length > 0) clues.Add("contains form submission structure");
            if (links.Length > 0) clues.Add("contains navigation or hyperlink elements");
            if (buttons.Length > 0) clues.Add("contains clickable button controls");
            if (headings.Length > 0) clues.Add("contains visible heading structure");
            if (tables.Length > 0) clues.Add("contains tabular data display");
            if (displayRegions.Length > 0) clues.Add("contains structured display regions such as chart, modal, list, grid, detail, or summary areas");
            if (inlineEvents.Length > 0) clues.Add("contains inline DOM event handlers");
            if (assets.Length > 0) clues.Add("references static assets such as images or stylesheets");

            return new
            {
                hasScripts = scripts.Length > 0,
                hasForms = forms.Length > 0,
                hasLinks = links.Length > 0,
                hasButtons = buttons.Length > 0,
                hasHeadings = headings.Length > 0,
                hasTables = tables.Length > 0,
                hasDisplayRegions = displayRegions.Length > 0,
                hasInlineEvents = inlineEvents.Length > 0,
                hasAssets = assets.Length > 0,
                clues
            };
        }
    }
}
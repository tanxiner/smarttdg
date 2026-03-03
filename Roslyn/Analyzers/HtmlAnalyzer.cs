using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    /// <summary>
    /// Lightweight HTML-only analyzer for .html/.htm files.
    /// Extracts scripts, forms, links, inline events, ids, and classes.
    /// Script info includes rawSrc, normalizedSrc, srcFileName, and hasQuery.
    /// </summary>
    public static class HtmlAnalyzer
    {
        public static bool IsHtmlPath(string filePath)
            => !string.IsNullOrEmpty(filePath) &&
               (filePath.EndsWith(".html", StringComparison.OrdinalIgnoreCase));

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            try
            {
                var scripts = ExtractScriptBlocks(code);
                var forms = ExtractForms(code);
                var links = ExtractLinks(code);
                var inlineEvents = ExtractInlineEvents(code);
                var ids = ExtractAttributeValues(code, "id");
                var classes = ExtractClassList(code);

                return new
                {
                    file = Path.GetFileName(filePath ?? ""),
                    path = filePath,
                    isHtml = IsHtmlPath(filePath ?? ""),
                    scripts,               // { rawSrc, normalizedSrc, srcFileName, hasQuery }[]
                    forms,                 // { action, method, fields: [{name,type}] }[]
                    links,                 // { href, text }[]
                    inlineEventAttrs = inlineEvents, // { selector, events }[]
                    ids,
                    classes
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

        // --- SCRIPT EXTRACTION ---
        private static object[] ExtractScriptBlocks(string code)
        {
            var rx = new Regex(@"<script\b(?<attrs>(?:[^'""<>]|'[^']*'|""[^""]*"")*)>(?<inner>.*?)<\/script\s*>",
                               RegexOptions.IgnoreCase | RegexOptions.Singleline);
            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups["attrs"].Value ?? "").Trim();
                string rawSrc = null;
                var srcMatch = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])(.*?)\1", RegexOptions.IgnoreCase | RegexOptions.Singleline);
                if (srcMatch.Success) rawSrc = srcMatch.Groups[2].Value;
                else
                {
                    var srcMatch2 = Regex.Match(attrs, @"\bsrc\s*=\s*([^\s>]+)", RegexOptions.IgnoreCase | RegexOptions.Singleline);
                    if (srcMatch2.Success) rawSrc = srcMatch2.Groups[1].Value;
                }

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

        // --- FORM EXTRACTION ---
        private static object[] ExtractForms(string code)
        {
            var rxForm = new Regex(@"<form\b([^>]*)>(.*?)<\/form\s*>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
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

        // --- LINK EXTRACTION ---
        private static object[] ExtractLinks(string code)
        {
            var rx = new Regex(@"<a\b([^>]*?)href\s*=\s*(['""]?)([^'"">\s]+)\2([^>]*)>(.*?)<\/a\s*>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var href = m.Groups[3].Value;
                var text = Regex.Replace(m.Groups[5].Value ?? "", @"\s+", " ").Trim();
                list.Add(new { href, text });
            }
            return list.ToArray();
        }

        // --- INLINE EVENTS ---
        private static object[] ExtractInlineEvents(string code)
        {
            var attrs = new[] { "onclick", "onsubmit", "onchange", "oninput", "onblur", "onfocus" };
            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*?(?:\b" + string.Join("|\\b", attrs) + @")[^>]*)>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
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
            var rx = new Regex(@"\b" + Regex.Escape(name) + @"\s*=\s*(['""]?)([^'""\s>]+)\1", RegexOptions.IgnoreCase);
            var m = rx.Match(attrText);
            return m.Success ? m.Groups[2].Value : null;
        }

        private static string InlineElementSelector(string attrText, string tag)
        {
            var id = ExtractAttribute(attrText, "id");
            if (!string.IsNullOrEmpty(id)) return $"#{id}";
            var cls = ExtractAttribute(attrText, "class");
            if (!string.IsNullOrEmpty(cls)) return "." + cls.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault();
            return tag;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class AspxExtractor
    {
        public static bool IsAspxPath(string filePath)
            => !string.IsNullOrEmpty(filePath)
               && (filePath.EndsWith(".aspx", StringComparison.OrdinalIgnoreCase)
                   || filePath.EndsWith(".ascx", StringComparison.OrdinalIgnoreCase)
                   || filePath.EndsWith(".master", StringComparison.OrdinalIgnoreCase));

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            // Debug: start of analysis for this file
            try
            {
                Console.WriteLine($"[Debug] AspxExtractor.Analyze start: {filePath}");
            }
            catch { /* best-effort logging */ }

            var directives = ExtractDirectives(code);
            var codeBlocks = ExtractCodeBlocks(code);
            var scriptBlocks = ExtractScriptBlocks(code);
            var htmlTags = ExtractHtmlTags(code);

            // Debug: report counts of extracted items
            try
            {
                Console.WriteLine($"[Debug] AspxExtractor: directives={directives?.Length ?? 0}, codeBlocks={codeBlocks?.Length ?? 0}, scripts={scriptBlocks?.Length ?? 0}, htmlTags={htmlTags?.Length ?? 0}");
            }
            catch { /* best-effort logging */ }

            return new
            {
                file = System.IO.Path.GetFileName(filePath ?? ""),
                path = filePath,
                isAspx = IsAspxPath(filePath ?? ""),
                directives,
                codeBlocks,
                scriptBlocks,
                htmlTags
            };
        }

        // <%@ ... %>
        private static object[] ExtractDirectives(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<%@\s*(.*?)%>", RegexOptions.Singleline | RegexOptions.IgnoreCase);
            foreach (Match m in rx.Matches(code))
            {
                list.Add(new
                {
                    text = m.Value,
                    content = m.Groups[1].Value.Trim(),
                    line = GetLineNumber(code, m.Index),
                    startIndex = m.Index,
                    endIndex = m.Index + m.Length
                });
            }
            return list.ToArray();
        }

        // <% ... %> and <%= ... %> and <%# ... %>
        private static object[] ExtractCodeBlocks(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<%(?!@)(.*?)%>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var full = m.Value;
                var inner = m.Groups[1].Value;
                list.Add(new
                {
                    text = full,
                    content = inner.Trim(),
                    type = GetBlockType(full),
                    line = GetLineNumber(code, m.Index),
                    startIndex = m.Index,
                    endIndex = m.Index + m.Length
                });
            }
            return list.ToArray();

            static string GetBlockType(string full)
            {
                if (full.StartsWith("<%=", StringComparison.Ordinal)) return "expression";
                if (full.StartsWith("<%#", StringComparison.Ordinal)) return "databind";
                if (full.StartsWith("<%--", StringComparison.Ordinal)) return "comment";
                return "code";
            }
        }

        // Reuse simple script extractor
        private static object[] ExtractScriptBlocks(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<script\b([^>]*)>(.*?)<\/script\s*>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var inner = (m.Groups[2].Value ?? "");
                var start = m.Index;
                list.Add(new
                {
                    tag = "script",
                    attributes = attrs,
                    content = inner,
                    line = GetLineNumber(code, start),
                    startIndex = start,
                    endIndex = start + m.Length
                });
            }
            return list.ToArray();
        }

        // Simple HTML opening-tag extractor (captures server controls like <asp:...>)
        private static object[] ExtractHtmlTags(string code)
        {
            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            var list = new List<object>();
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                var attrs = (m.Groups[2].Value ?? "").Trim();
                int idx = m.Index;
                list.Add(new
                {
                    tag,
                    attributes = attrs,
                    text = m.Value,
                    line = GetLineNumber(code, idx),
                    startIndex = idx,
                    endIndex = idx + m.Length
                });
            }
            return list.ToArray();
        }

        // Utility: 1-based line numbers
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
    }
}
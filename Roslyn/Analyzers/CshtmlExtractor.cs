using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class CshtmlExtractor
    {
        public static bool IsCshtmlPath(string filePath)
            => !string.IsNullOrEmpty(filePath) && filePath.EndsWith(".cshtml", StringComparison.OrdinalIgnoreCase);

        public static object Analyze(string code, string filePath)
        {
            if (code == null) code = string.Empty;

            var modelDeclarations = ExtractModelDeclarations(code);
            var razorCodeBlocks = ExtractRazorCodeBlocks(code);
            var scriptBlocks = ExtractScriptBlocks(code);
            var htmlTags = ExtractHtmlTags(code);

            return new
            {
                file = System.IO.Path.GetFileName(filePath ?? ""),
                path = filePath,
                isCshtml = IsCshtmlPath(filePath ?? ""),
                modelDeclarations,
                razorCodeBlocks,
                scriptBlocks,
                htmlTags
            };
        }

        // Extract lines with "@model ..." (multiline; can appear more than once but usually once)
        private static object[] ExtractModelDeclarations(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"^\s*@model\s+(.+)$", RegexOptions.Multiline | RegexOptions.IgnoreCase);
            foreach (Match m in rx.Matches(code))
            {
                var value = m.Groups[1].Value.Trim();
                list.Add(new
                {
                    text = m.Value.Trim(),
                    modelType = value,
                    line = GetLineNumber(code, m.Index)
                });
            }
            return list.ToArray();
        }

        // Extract Razor @{ ... } blocks with simple brace-balancing and line numbers
        private static object[] ExtractRazorCodeBlocks(string code)
        {
            var results = new List<object>();
            for (int i = 0; i < code.Length - 1; i++)
            {
                if (code[i] == '@' && i + 1 < code.Length && code[i + 1] == '{')
                {
                    int start = i;
                    int pos = i + 2;
                    int depth = 1;
                    while (pos < code.Length && depth > 0)
                    {
                        char c = code[pos];

                        // skip strings to avoid braces inside them interfering
                        if (c == '"' || c == '\'')
                        {
                            char quote = c;
                            pos++;
                            while (pos < code.Length)
                            {
                                if (code[pos] == '\\') { pos += 2; continue; }
                                if (code[pos] == quote) { pos++; break; }
                                pos++;
                            }
                            continue;
                        }

                        if (c == '{') depth++;
                        else if (c == '}') depth--;
                        pos++;
                    }

                    int end = Math.Min(pos, code.Length);
                    var snippet = code.Substring(start, end - start);
                    results.Add(new
                    {
                        text = snippet,
                        content = snippet.Length > 2 ? snippet.Substring(2, Math.Max(0, snippet.Length - 3)) : string.Empty, // remove leading "@{" and trailing "}"
                        startLine = GetLineNumber(code, start),
                        endLine = GetLineNumber(code, Math.Max(0, end - 1)),
                        startIndex = start,
                        endIndex = end
                    });

                    i = end - 1;
                }
            }
            return results.ToArray();
        }

        // Extract <script ...>...</script> blocks (singleline to capture innerHTML) and attributes
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

        // Extract simple HTML tags (opening tags only) with attributes. Does not parse nested HTML.
        private static object[] ExtractHtmlTags(string code)
        {
            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
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
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Roslyn.Analyzers
{
    public static class AspxAnalyzer
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

            // collect linked files referenced via script src attributes AND Register directives (user controls)
            var linkedFiles = new List<string>();

            // existing script src collection
            foreach (var sb in scriptBlocks)
            {
                var prop = sb.GetType().GetProperty("src_file");
                if (prop != null)
                {
                    var v = prop.GetValue(sb) as string;
                    if (!string.IsNullOrEmpty(v)) linkedFiles.Add(v);
                }
            }

            // new: extract Src from <%@ Register ... %> directives (e.g. Src="~/UserControls/OCCAuth_NEL.ascx")
            foreach (var d in directives)
            {
                try
                {
                    var prop = d?.GetType().GetProperty("content");
                    if (prop == null) continue;
                    var content = prop.GetValue(d) as string ?? "";
                    var m = Regex.Match(content, @"\bSrc\s*=\s*(['""])?(?<val>[^'"">\s]+)", RegexOptions.IgnoreCase);
                    if (m.Success)
                    {
                        var raw = m.Groups["val"].Value.Trim();
                        // drop leading "~/" or "~"
                        if (raw.StartsWith("~/")) raw = raw.Substring(2);
                        else if (raw.StartsWith("~")) raw = raw.Substring(1);
                        var norm = NormalizeSrcValue(raw);
                        if (!string.IsNullOrWhiteSpace(norm)) linkedFiles.Add(norm);
                    }
                }
                catch { /* best-effort: ignore directive parse errors */ }
            }

            var linkedFilesArr = linkedFiles.Distinct(StringComparer.OrdinalIgnoreCase).ToArray();

            // Debug: report counts of extracted items
            try
            {
                Console.WriteLine($"[Debug] AspxExtractor: directives={directives?.Length ?? 0}, codeBlocks={codeBlocks?.Length ?? 0}, scripts={scriptBlocks?.Length ?? 0}, htmlTags={htmlTags?.Length ?? 0}, linkedFiles={linkedFilesArr.Length}");
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
                linkedFiles = linkedFilesArr
                //htmlTags
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

        // Reuse simple script extractor, but also parse src attribute and normalize referenced file
        private static object[] ExtractScriptBlocks(string code)
        {
            var list = new List<object>();

            // 1) Match full <script ...>...</script> blocks (existing)
            var rx = new Regex(@"<script\b([^>]*)>(.*?)<\/script\s*>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var inner = (m.Groups[2].Value ?? "");
                var attrsDict = ParseAttributes(attrs);

                // tolerant src extraction (fallbacks)
                attrsDict.TryGetValue("src", out var rawSrc);
                if (string.IsNullOrWhiteSpace(rawSrc))
                {
                    var mSrc = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>[^'""\s>]+)", RegexOptions.IgnoreCase);
                    if (mSrc.Success) rawSrc = mSrc.Groups["val"].Value;
                    else
                    {
                        var mSrc2 = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>.+)$", RegexOptions.IgnoreCase | RegexOptions.Singleline);
                        if (mSrc2.Success) rawSrc = mSrc2.Groups["val"].Value.TrimEnd('>', '"', '\'', ' ', '\t');
                    }
                }

                var srcFile = NormalizeSrcValue(rawSrc);

                list.Add(new
                {
                    tag = "script",
                    attributes = attrs,
                    attributes_parsed = attrsDict,
                    src = rawSrc,
                    src_file = srcFile,
                    content = inner,
                });
            }

            // 2) Also capture opening <script ...> tags that may not have a closing tag or are malformed
            var rxOpen = new Regex(@"<script\b([^>]*\bsrc\b[^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rxOpen.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();

                // skip if already added (by identical attrs)
                if (list.Any(x => string.Equals((string)x.GetType().GetProperty("attributes")?.GetValue(x) ?? "", attrs, StringComparison.Ordinal))) 
                    continue;

                var attrsDict = ParseAttributes(attrs);
                attrsDict.TryGetValue("src", out var rawSrc);
                if (string.IsNullOrWhiteSpace(rawSrc))
                {
                    var mSrc = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>[^'""\s>]+)", RegexOptions.IgnoreCase);
                    if (mSrc.Success) rawSrc = mSrc.Groups["val"].Value;
                    else
                    {
                        var mSrc2 = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>.+)$", RegexOptions.IgnoreCase | RegexOptions.Singleline);
                        if (mSrc2.Success) rawSrc = mSrc2.Groups["val"].Value.TrimEnd('>', '"', '\'', ' ', '\t');
                    }
                }

                var srcFile = NormalizeSrcValue(rawSrc);

                list.Add(new
                {
                    tag = "script",
                    attributes = attrs,
                    attributes_parsed = attrsDict,
                    src = rawSrc,
                    src_file = srcFile,
                    content = ""
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
                });
            }
            return list.ToArray();
        }

        // Parse attributes string into a dictionary (best-effort)
        private static Dictionary<string, string> ParseAttributes(string attrs)
        {
            var dict = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            if (string.IsNullOrWhiteSpace(attrs)) return dict;

            // name = "value"  or name='value'  or name=value
            var rxAttr = new Regex(@"(?<name>[^\s=]+)\s*=\s*(?:(['""])(?<val>.*?)\2|(?<val>[^\s>]+))", RegexOptions.Singleline);
            foreach (Match am in rxAttr.Matches(attrs))
            {
                var name = am.Groups["name"].Value?.Trim();
                var val = am.Groups["val"].Value?.Trim();
                if (!string.IsNullOrEmpty(name))
                {
                    dict[name] = val;
                }
            }

            return dict;
        }

        // Normalize the src attribute value to a file path if possible.
        // Handles querystrings and ignores embedded server-side expressions.
        private static string NormalizeSrcValue(string raw)
        {
            if (string.IsNullOrWhiteSpace(raw)) return null;

            // drop any server-side tag that starts with '<%'
            var serverTagIdx = raw.IndexOf("<%", StringComparison.Ordinal);
            if (serverTagIdx >= 0)
            {
                raw = raw.Substring(0, serverTagIdx);
            }

            // drop query string part
            var qIdx = raw.IndexOf('?');
            if (qIdx >= 0) raw = raw.Substring(0, qIdx);

            raw = raw.Trim().Trim('\'', '"');

            if (string.IsNullOrWhiteSpace(raw)) return null;

            // return as-is (relative/absolute) — caller can resolve if needed
            return raw;
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
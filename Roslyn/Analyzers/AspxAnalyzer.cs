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
            code ??= string.Empty;

            var pageDirectiveInfo = ExtractPageDirectiveInfo(code);
            var directives = ExtractDirectives(code);
            var codeBlocks = ExtractCodeBlocks(code);
            var scriptBlocks = ExtractScriptBlocks(code);
            var serverControls = ExtractServerControls(code);
            var forms = ExtractForms(code);
            var inputControls = ExtractInputControls(code);
            var buttonControls = ExtractButtonControls(code);
            var eventBindings = ExtractEventBindings(code);
            var dataControls = ExtractDataControls(code);
            var linkedFiles = ExtractLinkedFiles(directives, scriptBlocks, serverControls, pageDirectiveInfo);
            var summaryHints = BuildSummaryHints(
                pageDirectiveInfo,
                directives,
                forms,
                inputControls,
                buttonControls,
                eventBindings,
                dataControls,
                serverControls,
                scriptBlocks,
                linkedFiles
            );

            return new
            {
                file = System.IO.Path.GetFileName(filePath ?? ""),
                path = filePath,
                isAspx = IsAspxPath(filePath ?? ""),
                pageDirectiveInfo,
                directives,
                codeBlocks,
                scriptBlocks,
                linkedFiles,
                serverControls,
                forms,
                inputControls,
                buttonControls,
                eventBindings,
                dataControls,
                summaryHints
            };
        }

        private static object ExtractPageDirectiveInfo(string code)
        {
            var m = Regex.Match(code, @"<%@\s*Page\s+(.*?)%>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            if (!m.Success)
            {
                return new
                {
                    exists = false
                };
            }

            var attrs = ParseAttributes(m.Groups[1].Value);

            return new
            {
                exists = true,
                language = GetAttr(attrs, "Language"),
                inherits = GetAttr(attrs, "Inherits"),
                codeFile = GetAttr(attrs, "CodeFile") ?? GetAttr(attrs, "CodeBehind"),
                masterPageFile = GetAttr(attrs, "MasterPageFile"),
                autoEventWireup = GetAttr(attrs, "AutoEventWireup"),
                //line = GetLineNumber(code, m.Index)
            };
        }

        private static object[] ExtractDirectives(string code)
        {
            var list = new List<object>();
            var rx = new Regex(@"<%@\s*(.*?)%>", RegexOptions.Singleline | RegexOptions.IgnoreCase);

            foreach (Match m in rx.Matches(code))
            {
                var content = m.Groups[1].Value.Trim();
                var firstToken = content.Split(new[] { ' ', '\t', '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries)
                                        .FirstOrDefault();

                list.Add(new
                {
                    text = m.Value,
                    content,
                    directiveType = firstToken,
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

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
                    //line = GetLineNumber(code, m.Index)
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

        private static object[] ExtractScriptBlocks(string code)
        {
            var list = new List<object>();

            var rx = new Regex(@"<script\b([^>]*)>(.*?)<\/script\s*>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();
                var inner = (m.Groups[2].Value ?? "");
                var attrsDict = ParseAttributes(attrs);

                attrsDict.TryGetValue("src", out var rawSrc);
                if (string.IsNullOrWhiteSpace(rawSrc))
                {
                    var mSrc = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>[^'""\s>]+)", RegexOptions.IgnoreCase);
                    if (mSrc.Success) rawSrc = mSrc.Groups["val"].Value;
                }

                rawSrc = rawSrc?.Trim().Trim('\'', '"');
                var srcFile = NormalizeSrcValue(rawSrc);

                list.Add(new
                {
                    tag = "script",
                    attributes = attrs,
                    attributesParsed = attrsDict,
                    src = rawSrc,
                    srcFile,
                    content = inner,
                    //line = GetLineNumber(code, m.Index)
                });
            }

            var rxOpen = new Regex(@"<script\b([^>]*\bsrc\b[^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in rxOpen.Matches(code))
            {
                var attrs = (m.Groups[1].Value ?? "").Trim();

                if (list.Any(x => string.Equals(GetProp(x, "attributes"), attrs, StringComparison.Ordinal)))
                    continue;

                var attrsDict = ParseAttributes(attrs);
                attrsDict.TryGetValue("src", out var rawSrc);
                if (string.IsNullOrWhiteSpace(rawSrc))
                {
                    var mSrc = Regex.Match(attrs, @"\bsrc\s*=\s*(['""])?(?<val>[^'""\s>]+)", RegexOptions.IgnoreCase);
                    if (mSrc.Success) rawSrc = mSrc.Groups["val"].Value;
                }

                rawSrc = rawSrc?.Trim().Trim('\'', '"');
                var srcFile = NormalizeSrcValue(rawSrc);

                list.Add(new
                {
                    tag = "script",
                    attributes = attrs,
                    attributesParsed = attrsDict,
                    src = rawSrc,
                    srcFile,
                    content = "",
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractServerControls(string code)
        {
            var list = new List<object>();

            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                if (!tag.Contains(":")) continue;

                var attrs = ParseAttributes(m.Groups[2].Value);
                var prefix = tag.Split(':')[0];

                if (!string.Equals(prefix, "asp", StringComparison.OrdinalIgnoreCase) &&
                    !string.Equals(prefix, "uc", StringComparison.OrdinalIgnoreCase))
                    continue;

                list.Add(new
                {
                    tag,
                    id = GetAttr(attrs, "ID"),
                    runat = GetAttr(attrs, "runat"),
                    cssClass = GetAttr(attrs, "CssClass") ?? GetAttr(attrs, "class"),
                    text = GetAttr(attrs, "Text"),
                    commandName = GetAttr(attrs, "CommandName"),
                    commandArgument = GetAttr(attrs, "CommandArgument"),
                    dataSourceId = GetAttr(attrs, "DataSourceID"),
                    navigateUrl = GetAttr(attrs, "NavigateUrl"),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractForms(string code)
        {
            var list = new List<object>();

            var htmlFormRx = new Regex(@"<form\b([^>]*)>", RegexOptions.IgnoreCase | RegexOptions.Singleline);
            foreach (Match m in htmlFormRx.Matches(code))
            {
                var attrs = ParseAttributes(m.Groups[1].Value);
                list.Add(new
                {
                    tag = "form",
                    id = GetAttr(attrs, "id") ?? GetAttr(attrs, "ID"),
                    runat = GetAttr(attrs, "runat"),
                    action = GetAttr(attrs, "action"),
                    method = GetAttr(attrs, "method"),
                    cssClass = GetAttr(attrs, "class") ?? GetAttr(attrs, "CssClass"),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractInputControls(string code)
        {
            var list = new List<object>();

            var controlNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
            {
                "asp:TextBox",
                "asp:DropDownList",
                "asp:CheckBox",
                "asp:RadioButton",
                "asp:RadioButtonList",
                "asp:CheckBoxList",
                "asp:ListBox",
                "asp:HiddenField",
                "asp:FileUpload"
            };

            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                if (!controlNames.Contains(tag)) continue;

                var attrs = ParseAttributes(m.Groups[2].Value);

                list.Add(new
                {
                    tag,
                    id = GetAttr(attrs, "ID"),
                    runat = GetAttr(attrs, "runat"),
                    text = GetAttr(attrs, "Text"),
                    value = GetAttr(attrs, "Value"),
                    selectedValue = GetAttr(attrs, "SelectedValue"),
                    autoPostBack = GetAttr(attrs, "AutoPostBack"),
                    cssClass = GetAttr(attrs, "CssClass"),
                   // line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractButtonControls(string code)
        {
            var list = new List<object>();

            var controlNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
            {
                "asp:Button",
                "asp:LinkButton",
                "asp:ImageButton"
            };

            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                if (!controlNames.Contains(tag)) continue;

                var attrs = ParseAttributes(m.Groups[2].Value);

                list.Add(new
                {
                    tag,
                    id = GetAttr(attrs, "ID"),
                    text = GetAttr(attrs, "Text"),
                    commandName = GetAttr(attrs, "CommandName"),
                    commandArgument = GetAttr(attrs, "CommandArgument"),
                    onClick = GetAttr(attrs, "OnClick"),
                    onCommand = GetAttr(attrs, "OnCommand"),
                    cssClass = GetAttr(attrs, "CssClass"),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static object[] ExtractEventBindings(string code)
        {
            var list = new List<object>();

            var eventNames = new[]
            {
                "OnClick",
                "OnCommand",
                "OnRowDataBound",
                "OnRowCommand",
                "OnSelectedIndexChanged",
                "OnTextChanged",
                "OnItemDataBound",
                "OnItemCommand",
                "OnInit",
                "OnLoad",
                "OnPreRender",
                "OnCheckedChanged"
            };

            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                var attrs = ParseAttributes(m.Groups[2].Value);

                foreach (var eventName in eventNames)
                {
                    var handler = GetAttr(attrs, eventName);
                    if (string.IsNullOrWhiteSpace(handler)) continue;

                    list.Add(new
                    {
                        tag,
                        id = GetAttr(attrs, "ID"),
                        eventName,
                        handler,
                        //line = GetLineNumber(code, m.Index)
                    });
                }
            }

            return list.ToArray();
        }

        private static object[] ExtractDataControls(string code)
        {
            var list = new List<object>();

            var controlNames = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
            {
                "asp:GridView",
                "asp:Repeater",
                "asp:DataList",
                "asp:ListView",
                "asp:DetailsView",
                "asp:FormView",
                "asp:DataGrid"
            };

            var rx = new Regex(@"<([a-zA-Z][a-zA-Z0-9:\-]*)\b([^>]*)\/?>", RegexOptions.Singleline);
            foreach (Match m in rx.Matches(code))
            {
                var tag = m.Groups[1].Value;
                if (!controlNames.Contains(tag)) continue;

                var attrs = ParseAttributes(m.Groups[2].Value);

                list.Add(new
                {
                    tag,
                    id = GetAttr(attrs, "ID"),
                    runat = GetAttr(attrs, "runat"),
                    dataSourceId = GetAttr(attrs, "DataSourceID"),
                    autoGenerateColumns = GetAttr(attrs, "AutoGenerateColumns"),
                    allowPaging = GetAttr(attrs, "AllowPaging"),
                    allowSorting = GetAttr(attrs, "AllowSorting"),
                    cssClass = GetAttr(attrs, "CssClass"),
                    //line = GetLineNumber(code, m.Index)
                });
            }

            return list.ToArray();
        }

        private static string[] ExtractLinkedFiles(
            object[] directives,
            object[] scriptBlocks,
            object[] serverControls,
            object pageDirectiveInfo)
        {
            var linkedFiles = new List<string>();

            foreach (var sb in scriptBlocks)
            {
                var v = GetProp(sb, "srcFile");
                if (!string.IsNullOrWhiteSpace(v)) linkedFiles.Add(v);
            }

            foreach (var d in directives)
            {
                var content = GetProp(d, "content") ?? "";
                var m = Regex.Match(content, @"\bSrc\s*=\s*(['""])?(?<val>[^'"">\s]+)", RegexOptions.IgnoreCase);
                if (m.Success)
                {
                    var raw = m.Groups["val"].Value.Trim();
                    if (raw.StartsWith("~/")) raw = raw.Substring(2);
                    else if (raw.StartsWith("~")) raw = raw.Substring(1);

                    var norm = NormalizeSrcValue(raw);
                    if (!string.IsNullOrWhiteSpace(norm)) linkedFiles.Add(norm);
                }
            }

            var masterPageFile = GetProp(pageDirectiveInfo, "masterPageFile");
            if (!string.IsNullOrWhiteSpace(masterPageFile))
            {
                var norm = NormalizeSrcValue(masterPageFile);
                if (!string.IsNullOrWhiteSpace(norm)) linkedFiles.Add(norm);
            }

            var codeFile = GetProp(pageDirectiveInfo, "codeFile");
            if (!string.IsNullOrWhiteSpace(codeFile))
            {
                var norm = NormalizeSrcValue(codeFile);
                if (!string.IsNullOrWhiteSpace(norm)) linkedFiles.Add(norm);
            }

            foreach (var sc in serverControls)
            {
                var navigateUrl = GetProp(sc, "navigateUrl");
                if (!string.IsNullOrWhiteSpace(navigateUrl))
                {
                    var norm = NormalizeSrcValue(navigateUrl);
                    if (!string.IsNullOrWhiteSpace(norm) && LooksLikeFileReference(norm))
                        linkedFiles.Add(norm);
                }
            }

            return linkedFiles
                .Distinct(StringComparer.OrdinalIgnoreCase)
                .ToArray();
        }

        private static object BuildSummaryHints(
            object pageDirectiveInfo,
            object[] directives,
            object[] forms,
            object[] inputControls,
            object[] buttonControls,
            object[] eventBindings,
            object[] dataControls,
            object[] serverControls,
            object[] scriptBlocks,
            string[] linkedFiles)
        {
            var clues = new List<string>();

            if (forms.Length > 0) clues.Add("contains server or HTML form structure");
            if (inputControls.Length > 0) clues.Add("contains input or selection controls");
            if (buttonControls.Length > 0) clues.Add("contains button-style action controls");
            if (eventBindings.Length > 0) clues.Add("declares server-side event handlers in markup");
            if (dataControls.Length > 0) clues.Add("contains data-bound list or grid controls");
            if (scriptBlocks.Length > 0) clues.Add("contains client-side script references or inline scripts");
            if (linkedFiles.Length > 0) clues.Add("references linked files such as scripts, user controls, master pages, or code-behind");

            return new
            {
                hasPageDirective = string.Equals(GetProp(pageDirectiveInfo, "exists"), "True", StringComparison.OrdinalIgnoreCase),
                hasForms = forms.Length > 0,
                hasInputControls = inputControls.Length > 0,
                hasButtonControls = buttonControls.Length > 0,
                hasEventBindings = eventBindings.Length > 0,
                hasDataControls = dataControls.Length > 0,
                hasScripts = scriptBlocks.Length > 0,
                hasLinkedFiles = linkedFiles.Length > 0,
                serverControlCount = serverControls.Length,
                clues
            };
        }

        private static Dictionary<string, string> ParseAttributes(string attrs)
        {
            var dict = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            if (string.IsNullOrWhiteSpace(attrs)) return dict;

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

        private static string GetAttr(Dictionary<string, string> attrs, string name)
            => attrs.TryGetValue(name, out var value) ? value : null;

        private static string NormalizeSrcValue(string raw)
        {
            if (string.IsNullOrWhiteSpace(raw)) return null;

            var serverTagIdx = raw.IndexOf("<%", StringComparison.Ordinal);
            if (serverTagIdx >= 0)
            {
                raw = raw.Substring(0, serverTagIdx);
            }

            if (raw.StartsWith("~/")) raw = raw.Substring(2);
            else if (raw.StartsWith("~")) raw = raw.Substring(1);

            var qIdx = raw.IndexOf('?');
            if (qIdx >= 0) raw = raw.Substring(0, qIdx);

            raw = raw.Trim().Trim('\'', '"');

            return string.IsNullOrWhiteSpace(raw) ? null : raw;
        }

        private static bool LooksLikeFileReference(string value)
        {
            if (string.IsNullOrWhiteSpace(value)) return false;

            var lowered = value.ToLowerInvariant();
            return lowered.EndsWith(".aspx") ||
                   lowered.EndsWith(".ascx") ||
                   lowered.EndsWith(".master") ||
                   lowered.EndsWith(".js") ||
                   lowered.EndsWith(".css") ||
                   lowered.EndsWith(".png") ||
                   lowered.EndsWith(".jpg") ||
                   lowered.EndsWith(".jpeg") ||
                   lowered.EndsWith(".gif") ||
                   lowered.EndsWith(".svg");
        }

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
    }
}
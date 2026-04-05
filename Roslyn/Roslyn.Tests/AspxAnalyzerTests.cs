using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class AspxAnalyzerTests
    {
        [Fact]
        public void IsAspxPath_Recognizes_Aspx_Ascx_And_Master()
        {
            Assert.True(AspxAnalyzer.IsAspxPath("page.aspx"));
            Assert.True(AspxAnalyzer.IsAspxPath("control.ascx"));
            Assert.True(AspxAnalyzer.IsAspxPath("site.master"));
            Assert.False(AspxAnalyzer.IsAspxPath("view.cshtml"));
        }

        [Fact]
        public void Analyze_Extracts_Directives()
        {
            var code = @"<%@ Page Language=""C#"" AutoEventWireup=""true"" %>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var directives = obj["directives"] as JArray;
            Assert.NotNull(directives);
            Assert.Single(directives!);
            Assert.Contains("Page", (string?)directives![0]!["content"]);
        }

        [Fact]
        public void Analyze_Extracts_Register_Directive_LinkedFile()
        {
            var code = @"<%@ Register TagPrefix=""uc"" TagName=""Auth"" Src=""~/UserControls/OCCAuth_NEL.ascx"" %>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var linkedFiles = obj["linkedFiles"]!.ToObject<string[]>();
            Assert.NotNull(linkedFiles);
            Assert.Contains("UserControls/OCCAuth_NEL.ascx", linkedFiles!);
        }

        [Fact]
        public void Analyze_Extracts_Script_Block_With_Src()
        {
            var code = @"<script src=""scripts/app.js?v=123""></script>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var scriptBlocks = obj["scriptBlocks"] as JArray;
            Assert.NotNull(scriptBlocks);
            Assert.Single(scriptBlocks!);
            Assert.Equal("scripts/app.js?v=123", (string?)scriptBlocks![0]!["src"]);
        }

        [Fact]
        public void Analyze_Extracts_Open_Script_Tag_With_Src()
        {
            var code = @"<script src=""js/site.js"">";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var linkedFiles = obj["linkedFiles"]!.ToObject<string[]>();
            Assert.NotNull(linkedFiles);
            Assert.Contains("js/site.js", linkedFiles!);
        }

        [Fact]
        public void Analyze_Extracts_CodeBlocks()
        {
            var code = @"<div><%= User.Identity.Name %></div><% if (true) { %>Hi<% } %>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var codeBlocks = obj["codeBlocks"] as JArray;
            Assert.NotNull(codeBlocks);
            Assert.True(codeBlocks!.Count >= 2);

            var firstType = (string?)codeBlocks[0]!["type"];
            Assert.Equal("expression", firstType);
        }

        [Fact]
        public void Analyze_Extracts_HtmlTags()
        {
            var code = @"<asp:Label ID=""lblName"" runat=""server"" /><div class=""x""></div>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var scriptBlocks = obj["scriptBlocks"] as JArray;
            Assert.NotNull(scriptBlocks);

            var directives = obj["directives"] as JArray;
            Assert.NotNull(directives);
        }

        [Fact]
        public void Analyze_IsAspx_Flag_Is_True_For_Aspx_File()
        {
            var code = "<div>Hello</div>";

            var result = AspxAnalyzer.Analyze(code, @"C:\temp\page.aspx");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            Assert.True((bool)obj["isAspx"]!);
            Assert.Equal("page.aspx", (string?)obj["file"]);
        }
    }
}
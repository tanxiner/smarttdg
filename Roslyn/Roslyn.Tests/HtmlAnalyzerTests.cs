using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class HtmlAnalyzerTests
    {
        [Fact]
        public void IsHtmlPath_Works()
        {
            Assert.True(HtmlAnalyzer.IsHtmlPath("index.html"));
            Assert.False(HtmlAnalyzer.IsHtmlPath("page.aspx"));
            Assert.False(HtmlAnalyzer.IsHtmlPath("view.cshtml"));
        }

        [Fact]
        public void Analyze_Extracts_Script_Info()
        {
            var code = @"<script src=""js/app.js?v=1""></script>";

            var result = HtmlAnalyzer.Analyze(code, @"C:\temp\index.html");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var scripts = obj["scripts"] as JArray;
            Assert.NotNull(scripts);
            Assert.Single(scripts!);

            var script = scripts![0]!;
            Assert.Equal("js/app.js?v=1", (string?)script["rawSrc"]);
            Assert.Equal("js/app.js", (string?)script["normalizedSrc"]);
            Assert.Equal("app.js", (string?)script["srcFileName"]);
            Assert.True((bool)script["hasQuery"]!);
        }

        [Fact]
        public void Analyze_Extracts_Forms()
        {
            var code = @"
<form action=""/submit"" method=""post"">
    <input name=""username"" type=""text"" />
    <input name=""password"" type=""password"" />
</form>";

            var result = HtmlAnalyzer.Analyze(code, @"C:\temp\index.html");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var forms = obj["forms"] as JArray;
            Assert.NotNull(forms);
            Assert.Single(forms!);

            var form = forms![0]!;
            Assert.Equal("/submit", (string?)form["action"]);
            Assert.Equal("POST", (string?)form["method"]);

            var fields = form["fields"] as JArray;
            Assert.NotNull(fields);
            Assert.Equal(2, fields!.Count);
            Assert.Equal("username", (string?)fields[0]!["name"]);
            Assert.Equal("text", (string?)fields[0]!["type"]);
        }

        [Fact]
        public void Analyze_Extracts_Links_Ids_And_Classes()
        {
            var code = @"
<a href=""/home"">Home</a>
<div id=""main"" class=""container hero""></div>";

            var result = HtmlAnalyzer.Analyze(code, @"C:\temp\index.html");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var links = obj["links"] as JArray;
            Assert.NotNull(links);
            Assert.Single(links!);
            Assert.Equal("/home", (string?)links![0]!["href"]);
            Assert.Equal("Home", (string?)links![0]!["text"]);

            var ids = obj["ids"]!.ToObject<string[]>();
            Assert.NotNull(ids);
            Assert.Contains("main", ids!);

            var classes = obj["classes"]!.ToObject<string[]>();
            Assert.NotNull(classes);
            Assert.Contains("container", classes!);
            Assert.Contains("hero", classes!);
        }

        [Fact]
        public void Analyze_Extracts_Inline_Events()
        {
            var code = @"<button id=""saveBtn"" onclick=""saveData()"">Save</button>";

            var result = HtmlAnalyzer.Analyze(code, @"C:\temp\index.html");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var events = obj["inlineEventAttrs"] as JArray;
            Assert.NotNull(events);
            Assert.Single(events!);

            var ev = events![0]!;
            Assert.Equal("#saveBtn", (string?)ev["selector"]);
        }

        [Fact]
        public void Analyze_Sets_IsHtml_Flag()
        {
            var code = "<div>Hello</div>";

            var result = HtmlAnalyzer.Analyze(code, @"C:\temp\index.html");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.True((bool)obj["isHtml"]!);
            Assert.Equal("index.html", (string?)obj["file"]);
        }
    }
}
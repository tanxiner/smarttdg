using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class CshtmlExtractorTests
    {
        [Fact]
        public void Path_Detection_Works()
        {
            Assert.True(CshtmlExtractor.IsCshtmlPath("Index.cshtml"));
            Assert.True(CshtmlExtractor.IsRazorComponentPath("Counter.razor"));
            Assert.False(CshtmlExtractor.IsCshtmlPath("Default.aspx"));
            Assert.False(CshtmlExtractor.IsRazorComponentPath("site.master"));
        }

        [Fact]
        public void Analyze_Extracts_Model_Declaration()
        {
            var code = @"
@model MyApp.Models.UserViewModel
<div>Hello</div>";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var modelDeclarations = obj["modelDeclarations"] as JArray;
            Assert.NotNull(modelDeclarations);
            Assert.Single(modelDeclarations!);
            Assert.Equal("MyApp.Models.UserViewModel", (string?)modelDeclarations![0]!["modelType"]);
        }

        [Fact]
        public void Analyze_Extracts_Directives()
        {
            var code = @"
@page
@using MyApp.Helpers
@inject IService Service
@layout MainLayout";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var directives = obj["directives"] as JArray;
            Assert.NotNull(directives);

            var names = directives!
                .Select(d => (string?)d!["directive"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("@page", names);
            Assert.Contains("@using", names);
            Assert.Contains("@inject", names);
            Assert.Contains("@layout", names);
        }

        [Fact]
        public void Analyze_Extracts_Code_And_Functions_Blocks()
        {
            var code = @"
@code {
    int count = 0;
}

@functions {
    void DoWork() { }
}";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Component.razor");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var razorBlocks = obj["razorCodeBlocks"] as JArray;
            Assert.NotNull(razorBlocks);
            Assert.Equal(2, razorBlocks!.Count);

            var kinds = razorBlocks.Select(x => (string?)x!["kind"]).ToArray();
            Assert.Contains("@code", kinds);
            Assert.Contains("@functions", kinds);
        }

        [Fact]
        public void Analyze_Extracts_Script_Block()
        {
            var code = @"
<script>
    console.log('hello');
</script>";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var scriptBlocks = obj["scriptBlocks"] as JArray;
            Assert.NotNull(scriptBlocks);
            Assert.Single(scriptBlocks!);
            Assert.Contains("console.log", (string?)scriptBlocks![0]!["content"]);
        }

        [Fact]
        public void Analyze_Extracts_Component_Usages()
        {
            var code = @"<MyGrid Items=""@Model.Items"" /><Shared.NavMenu />";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.razor");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var components = obj["componentUsages"] as JArray;
            Assert.NotNull(components);
            Assert.Equal(2, components!.Count);

            var names = components.Select(c => (string?)c!["component"]).ToArray();
            Assert.Contains("MyGrid", names);
            Assert.Contains("Shared.NavMenu", names);
        }

        [Fact]
        public void Analyze_Sets_File_Type_Flags_Correctly()
        {
            var code = "<div>Hello</div>";

            var resultCshtml = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var objCshtml = JObject.Parse(JsonConvert.SerializeObject(resultCshtml));
            Assert.True((bool)objCshtml["isCshtml"]!);
            Assert.False((bool)objCshtml["isRazorComponent"]!);

            var resultRazor = CshtmlExtractor.Analyze(code, @"C:\temp\Component.razor");
            var objRazor = JObject.Parse(JsonConvert.SerializeObject(resultRazor));
            Assert.False((bool)objRazor["isCshtml"]!);
            Assert.True((bool)objRazor["isRazorComponent"]!);
        }
    }
}
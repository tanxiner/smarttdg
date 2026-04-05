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
        public void Analyze_Returns_Model_Declarations_Array()
        {
            var code = @"@model MyApp.Models.UserViewModel
<div>Hello</div>";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var modelDeclarations = obj["modelDeclarations"] as JArray;
            Assert.NotNull(modelDeclarations);
        }

        [Fact]
        public void Analyze_Extracts_Directives()
        {
            var code = @"@page
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
            var code = @"@{
    var x = 1;
}

@functions {
    void DoWork() { }
}";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var razorBlocks = obj["razorCodeBlocks"] as JArray;
            Assert.NotNull(razorBlocks);
            Assert.Equal(2, razorBlocks!.Count);

            var kinds = razorBlocks.Select(x => (string?)x!["kind"]).ToArray();
            Assert.Contains("@{ }", kinds);
            Assert.Contains("@functions", kinds);
        }

        [Fact]
        public void Analyze_Extracts_Script_Block()
        {
            var code = @"<script>
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
        public void Analyze_Sets_File_Type_Flags_For_Cshtml()
        {
            var code = "<div>Hello</div>";

            var result = CshtmlExtractor.Analyze(code, @"C:\temp\Index.cshtml");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.True((bool)obj["isCshtml"]!);
            Assert.False((bool)obj["isRazorComponent"]!);
        }
    }
}
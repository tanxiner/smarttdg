using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class JsAnalyzerTests
    {
        [Fact]
        public void IsJsPath_Works()
        {
            Assert.True(JsAnalyzer.IsJsPath("app.js"));
            Assert.False(JsAnalyzer.IsJsPath("app.ts"));
            Assert.False(JsAnalyzer.IsJsPath("view.cshtml"));
        }

        [Fact]
        public void Analyze_Extracts_Functions_And_Exports()
        {
            var code = @"
export function loadUsers() {
    return fetch('/api/users');
}

const saveUser = (id) => {
    return id;
};";

            var result = JsAnalyzer.Analyze(code, @"C:\temp\app.js");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var exports = obj["exports"]!.ToObject<string[]>();
            Assert.NotNull(exports);
            Assert.Contains("loadUsers", exports!);

            var funcs = obj["funcs"]!;
            Assert.NotNull(funcs);
            Assert.True((int)funcs["count"]! >= 2);
        }

        [Fact]
        public void Analyze_Extracts_Api_Calls_And_Selectors()
        {
            var code = @"
fetch('/api/users');
axios.get('/api/orders');
document.querySelector('#main');
$('#saveBtn').click();";

            var result = JsAnalyzer.Analyze(code, @"C:\temp\app.js");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var apiCalls = obj["apiCalls"]!;
            Assert.NotNull(apiCalls);
            Assert.True((int)apiCalls["count"]! >= 2);

            var selectors = obj["selectors"]!.ToObject<string[]>();
            Assert.NotNull(selectors);
            Assert.Contains("#main", selectors!);
        }

        [Fact]
        public void Analyze_Detects_Url_Candidates_In_Summary()
        {
            var code = @"
const apiBaseUrl = 'https://api.example.com';
const userEndpoint = '/users';";

            var result = JsAnalyzer.Analyze(code, @"C:\temp\app.js");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var summary = obj["client_js_summary"]!;
            Assert.NotNull(summary);
            Assert.NotNull(summary["facts"]);
        }

        [Fact]
        public void Analyze_Invalid_Js_Does_Not_Crash()
        {
            var code = @"function x( {";

            var result = JsAnalyzer.Analyze(code, @"C:\temp\broken.js");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.Equal("broken.js", (string?)obj["file"]);
            Assert.NotNull(obj["client_js_summary"]);
        }

        [Fact]
        public void Analyze_Extracts_Event_Bindings()
        {
            var code = @"
document.getElementById('saveBtn').addEventListener('click', saveData);";

            var result = JsAnalyzer.Analyze(code, @"C:\temp\events.js");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var eventBindings = obj["eventBindings"]!;
            Assert.NotNull(eventBindings);
            Assert.True((int)eventBindings["count"]! >= 1);
        }
    }
}
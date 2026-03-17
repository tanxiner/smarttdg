using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class VisualBasicAnalyzerTests
    {
        [Fact]
        public void Analyze_Extracts_Basic_Vb_Class_Info()
        {
            var code = @"
Imports System

Namespace Demo.Services
    Public Class UserService
        Private _name As String

        Public Property Count As Integer

        Public Function GetUser(id As Integer) As String
            Return ""test""
        End Function
    End Class
End Namespace";

            var result = VisualBasicAnalyzer.Analyze(code, @"C:\temp\UserService.vb");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.Equal("UserService.vb", (string?)obj["file"]);
            Assert.Equal("VB", (string?)obj["language"]);

            var namespaces = obj["namespaces"]!.ToObject<string[]>();
            Assert.NotNull(namespaces);
            Assert.Contains("Demo.Services", namespaces!);

            var imports = obj["imports"]!.ToObject<string[]>();
            Assert.NotNull(imports);
            Assert.Contains("System", imports!);

            var classes = obj["classes"] as JArray;
            Assert.NotNull(classes);
            Assert.Single(classes!);

            var cls = classes![0]!;
            Assert.Equal("UserService", (string?)cls["name"]);
            Assert.Equal("Public", (string?)cls["modifiers"]);

            var methods = cls["Methods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("GetUser", methods!);

            var properties = cls["Properties"]!.ToObject<string[]>();
            Assert.NotNull(properties);
            Assert.Contains("Count", properties!);
        }

        [Fact]
        public void Analyze_Extracts_Inheritance_And_Interfaces()
        {
            var code = @"
Namespace Demo
    Public Interface ILogger
    End Interface

    Public Class BaseService
    End Class

    Public Class UserService
        Inherits BaseService
        Implements ILogger
    End Class
End Namespace";

            var result = VisualBasicAnalyzer.Analyze(code, @"C:\temp\UserService.vb");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var classes = obj["classes"] as JArray;
            Assert.NotNull(classes);

            var userService = classes!
                .FirstOrDefault(c => (string?)c!["name"] == "UserService");

            Assert.NotNull(userService);
            Assert.Equal("BaseService", (string?)userService!["baseType"]);

            var interfaces = userService["interfaces"]!.ToObject<string[]>();
            Assert.NotNull(interfaces);
            Assert.Contains("ILogger", interfaces!);
        }

        [Fact]
        public void Analyze_Builds_Vb_IR()
        {
            var code = @"
Namespace Demo.Core
    Public Class OrderService
        Private _counter As Integer
        Public Property Name As String

        Public Function SaveOrder(id As Integer) As Boolean
            Return True
        End Function
    End Class
End Namespace";

            var result = VisualBasicAnalyzer.Analyze(code, @"C:\temp\OrderService.vb");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var ir = obj["ir"]!;
            Assert.NotNull(ir);
            Assert.Equal("OrderService.vb", (string?)ir["file"]);
            Assert.Equal(@"C:\temp\OrderService.vb", (string?)ir["path"]);

            var types = ir["types"] as JArray;
            Assert.NotNull(types);
            Assert.Single(types!);

            var type = types![0]!;
            Assert.Equal("Class", (string?)type["kind"]);
            Assert.Equal("OrderService", (string?)type["name"]);
            Assert.Equal("Demo.Core", (string?)type["namespaceName"]);
        }

        [Fact]
        public void Analyze_Handles_Empty_Vb_Code()
        {
            var code = "";

            var result = VisualBasicAnalyzer.Analyze(code, @"C:\temp\Empty.vb");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.Equal("Empty.vb", (string?)obj["file"]);
            Assert.Equal("VB", (string?)obj["language"]);

            var classes = obj["classes"]!.ToObject<object[]>();
            Assert.NotNull(classes);
            Assert.Empty(classes!);

            var methods = obj["methods"]!.ToObject<object[]>();
            Assert.NotNull(methods);
            Assert.Empty(methods!);
        }
    }
}
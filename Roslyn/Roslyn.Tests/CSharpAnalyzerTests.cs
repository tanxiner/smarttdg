using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class CSharpAnalyzerTests
    {
        [Fact]
        public void Analyze_ExtractsBasicClassInfo()
        {
            var code = @"
using System;
using System.Collections.Generic;

namespace DemoApp.Services
{
    public class UserService
    {
        private string _name;

        public int Count { get; set; }

        public string GetUser(int id)
        {
            return ""test"";
        }
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\UserService.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            Assert.Equal("UserService.cs", (string?)obj["file"]);
            Assert.Equal("C#", (string?)obj["language"]);

            var namespaces = obj["namespaces"]!.ToObject<string[]>();
            Assert.NotNull(namespaces);
            Assert.Contains("DemoApp.Services", namespaces!);

            var imports = obj["imports"]!.ToObject<string[]>();
            Assert.NotNull(imports);
            Assert.Contains("System", imports!);
            Assert.Contains("System.Collections.Generic", imports!);

            var classes = obj["classes"]!;
            Assert.NotNull(classes);
            Assert.Single(classes);

            var firstClass = classes[0]!;
            Assert.Equal("UserService", (string?)firstClass["name"]);
            Assert.Equal("public", (string?)firstClass["modifiers"]);

            var methods = firstClass["Methods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("public GetUser(id: int): string", methods!);

            var properties = firstClass["Properties"]!.ToObject<string[]>();
            Assert.NotNull(properties);
            Assert.Contains("public Count: int", properties!);

            var fields = firstClass["Fields"]!.ToObject<string[]>();
            Assert.NotNull(fields);
            Assert.Contains("private _name: string", fields!);
        }

        [Fact]
        public void Analyze_ExtractsBaseType_And_Interfaces()
        {
            var code = @"
namespace Demo
{
    public interface ILogger {}

    public class BaseService {}

    public class UserService : BaseService, ILogger
    {
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\UserService.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var classes = obj["classes"]!;
            Assert.Equal(2, classes.Count());

            var userService = classes
                .FirstOrDefault(c => (string?)c!["name"] == "UserService");

            Assert.NotNull(userService);
            Assert.Equal("BaseService", (string?)userService!["baseType"]);

            var interfaces = userService["interfaces"]!.ToObject<string[]>();
            Assert.NotNull(interfaces);
            Assert.Contains("ILogger", interfaces!);
        }
        [Fact]
        public void Analyze_BuildsIRCorrectly()
        {
            var code = @"
namespace Demo.Core
{
    public class OrderService
    {
        private int _counter;
        public string Name { get; set; }

        public bool SaveOrder(int id)
        {
            return true;
        }
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\OrderService.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var ir = obj["ir"]!;
            Assert.NotNull(ir);
            Assert.Equal("OrderService.cs", (string?)ir["file"]);
            Assert.Equal(@"C:\temp\OrderService.cs", (string?)ir["path"]);

            var irNamespaces = ir["namespaces"]!.ToObject<string[]>();
            Assert.NotNull(irNamespaces);
            Assert.Contains("Demo.Core", irNamespaces!);

            var types = ir["types"]!;
            Assert.NotNull(types);
            Assert.Single(types);

            var type = types[0]!;
            Assert.Equal("OrderService", (string?)type["name"]);
            Assert.Equal("Demo.Core", (string?)type["namespaceName"]);
            Assert.Equal("public", (string?)type["modifiers"]);

            var methods = type["methods"]!;
            Assert.Single(methods);
            Assert.Equal("SaveOrder", (string?)methods[0]!["name"]);
            Assert.Equal("public", (string?)methods[0]!["modifiers"]);
            Assert.Equal("bool", (string?)methods[0]!["returnType"]);

            var methodParams = methods[0]!["parameters"]!;
            Assert.Single(methodParams);
            Assert.Equal("id", (string?)methodParams[0]!["name"]);
            Assert.Equal("int", (string?)methodParams[0]!["type"]);

            var properties = type["properties"]!;
            Assert.Single(properties);
            Assert.Equal("Name", (string?)properties[0]!["name"]);
            Assert.Equal("public", (string?)properties[0]!["modifiers"]);
            Assert.Equal("string", (string?)properties[0]!["type"]);

            var fields = type["fields"]!;
            Assert.Single(fields);
            Assert.Equal("_counter", (string?)fields[0]!["name"]);
            Assert.Equal("private", (string?)fields[0]!["modifiers"]);
            Assert.Equal("int", (string?)fields[0]!["type"]);
        }

        [Fact]
        public void Analyze_HandlesEmptyCode()
        {
            var code = "";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\Empty.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            Assert.Equal("Empty.cs", (string?)obj["file"]);
            Assert.Equal("C#", (string?)obj["language"]);

            var classes = obj["classes"]!.ToObject<object[]>();
            Assert.NotNull(classes);
            Assert.Empty(classes!);

            var methods = obj["methods"]!.ToObject<object[]>();
            Assert.NotNull(methods);
            Assert.Empty(methods!);

            var ir = obj["ir"]!;
            Assert.NotNull(ir);

            var types = ir["types"]!.ToObject<object[]>();
            Assert.NotNull(types);
            Assert.Empty(types!);
        }

        [Fact]
        public void Analyze_ExtractsMultipleClasses()
        {
            var code = @"
namespace Demo.Multi
{
    public class FirstService
    {
        public void Run() {}
    }

    public class SecondService
    {
        public int Value { get; set; }
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\Multi.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var classes = obj["classes"]!;
            Assert.Equal(2, classes.Count());

            var classNames = classes.Select(c => (string?)c!["name"]).ToArray();
            Assert.Contains("FirstService", classNames);
            Assert.Contains("SecondService", classNames);

            var methods = obj["methods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("public Run(): void", methods!);
        }

        [Fact]
        public void Analyze_ExtractsMethodParameters_Correctly()
        {
            var code = @"
namespace Demo.Params
{
    public class Calculator
    {
        public decimal Add(int a, decimal b)
        {
            return a + b;
        }
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\Calculator.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var classes = obj["classes"]!;
            Assert.Single(classes);

            var methods = classes[0]!["Methods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("public Add(a: int, b: decimal): decimal", methods!);

            var irMethods = obj["ir"]!["types"]![0]!["methods"]!;
            Assert.Single(irMethods);

            var parameters = irMethods[0]!["parameters"]!;
            Assert.Equal(2, parameters.Count());
            Assert.Equal("a", (string?)parameters[0]!["name"]);
            Assert.Equal("int", (string?)parameters[0]!["type"]);
            Assert.Equal("b", (string?)parameters[1]!["name"]);
            Assert.Equal("decimal", (string?)parameters[1]!["type"]);
        }

        [Fact]
        public void Analyze_ExtractsNestedNamespace_And_UsingStatements()
        {
            var code = @"
using System;
using System.Text;

namespace Company.Product.Module
{
    public class Formatter
    {
    }
}";

            var result = CSharpAnalyzer.Analyze(code, @"C:\temp\Formatter.cs");

            var json = JsonConvert.SerializeObject(result);
            var obj = JObject.Parse(json);

            var namespaces = obj["namespaces"]!.ToObject<string[]>();
            Assert.NotNull(namespaces);
            Assert.Contains("Company.Product.Module", namespaces!);

            var imports = obj["imports"]!.ToObject<string[]>();
            Assert.NotNull(imports);
            Assert.Contains("System", imports!);
            Assert.Contains("System.Text", imports!);
        }
    }
}
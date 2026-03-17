using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class DependencyExtractorTests
    {
        [Fact]
        public void Extract_CSharp_Usings_From_Directory()
        {
            var tempDir = Path.Combine(Path.GetTempPath(), Guid.NewGuid().ToString());
            Directory.CreateDirectory(tempDir);

            try
            {
                var file = Path.Combine(tempDir, "Test.cs");
                File.WriteAllText(file, @"
using System;
using System.Linq;

namespace Demo
{
    public class TestClass {}
}");

                var result = DependencyExtractor.Extract(tempDir, "C#");
                var obj = JObject.Parse(JsonConvert.SerializeObject(result));

                var deps = obj["dependencies"]!;
                Assert.NotNull(deps);

                var usings = deps["Usings"]!.ToObject<string[]>();
                Assert.NotNull(usings);
                Assert.Contains("System", usings!);
                Assert.Contains("System.Linq", usings!);

                var assemblies = deps["Assemblies"]!.ToObject<string[]>();
                Assert.NotNull(assemblies);
                Assert.NotEmpty(assemblies!);
            }
            finally
            {
                if (Directory.Exists(tempDir))
                    Directory.Delete(tempDir, true);
            }
        }

        [Fact]
        public void Extract_Vb_Imports_From_Directory()
        {
            var tempDir = Path.Combine(Path.GetTempPath(), Guid.NewGuid().ToString());
            Directory.CreateDirectory(tempDir);

            try
            {
                var file = Path.Combine(tempDir, "Test.vb");
                File.WriteAllText(file, @"
Imports System
Imports System.Linq

Namespace Demo
    Public Class TestClass
    End Class
End Namespace");

                var result = DependencyExtractor.Extract(tempDir, "VB");
                var obj = JObject.Parse(JsonConvert.SerializeObject(result));

                var deps = obj["dependencies"]!;
                Assert.NotNull(deps);

                var imports = deps["Imports"]!.ToObject<string[]>();
                Assert.NotNull(imports);
                Assert.Contains("System", imports!);
                Assert.Contains("System.Linq", imports!);

                var assemblies = deps["Assemblies"]!.ToObject<string[]>();
                Assert.NotNull(assemblies);
                Assert.NotEmpty(assemblies!);
            }
            finally
            {
                if (Directory.Exists(tempDir))
                    Directory.Delete(tempDir, true);
            }
        }

        [Fact]
        public void Extract_Invalid_Path_Returns_Error_Object()
        {
            var badPath = Path.Combine(Path.GetTempPath(), Guid.NewGuid().ToString(), "missing");

            var result = DependencyExtractor.Extract(badPath, "C#");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.Equal("Dependency analysis failed", (string?)obj["error"]);
            Assert.NotNull(obj["details"]);
        }
    }
}
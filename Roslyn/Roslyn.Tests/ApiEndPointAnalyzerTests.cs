using Microsoft.CodeAnalysis.CSharp;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class ApiEndpointAnalyzerTests
    {
        [Fact]
        public void Analyze_CSharp_WebApi_Controller_With_HttpGet_And_Route()
        {
            var code = @"
using System.Web.Http;

namespace Demo.Api
{
    public class UsersController : ApiController
    {
        [HttpGet]
        [Route(""users/{id}"")]
        public IHttpActionResult GetUser(int id)
        {
            return Ok();
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\UsersController.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var ep = arr[0]!;
            Assert.Equal("webapi", (string?)ep["Kind"]);
            Assert.Equal("UsersController", (string?)ep["ControllerOrServiceName"]);
            Assert.Equal("GetUser", (string?)ep["OperationName"]);
            Assert.Equal("/api/Users/users/{id}", (string?)ep["Route"]);

            var methods = ep["HttpMethods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("GET", methods!);
        }

        [Fact]
        public void Analyze_CSharp_Mvc_Controller_Detects_ActionResult_Method()
        {
            var code = @"
using System.Web.Mvc;

namespace Demo.Mvc
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\HomeController.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var ep = arr[0]!;
            Assert.Equal("mvc", (string?)ep["Kind"]);
            Assert.Equal("HomeController", (string?)ep["ControllerOrServiceName"]);
            Assert.Equal("Index", (string?)ep["OperationName"]);
            Assert.Equal("/api/Home/Index", (string?)ep["Route"]);
        }

        [Fact]
        public void Analyze_CSharp_Asmx_WebMethod_Detected()
        {
            var code = @"
using System.Web.Services;

namespace Demo.Services
{
    [WebService]
    public class LegacyService
    {
        [WebMethod]
        public string Ping()
        {
            return ""ok"";
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\LegacyService.asmx.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var ep = arr[0]!;
            Assert.Equal("asmx", (string?)ep["Kind"]);
            Assert.Equal("LegacyService", (string?)ep["ControllerOrServiceName"]);
            Assert.Equal("Ping", (string?)ep["OperationName"]);

            var methods = ep["HttpMethods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("GET", methods!);
            Assert.Contains("POST", methods!);
        }

        [Fact]
        public void Analyze_CSharp_Wcf_OperationContract_Detected()
        {
            var code = @"
using System.ServiceModel;

namespace Demo.Wcf
{
    [ServiceContract]
    public class OrderService
    {
        [OperationContract]
        public string SubmitOrder(int id)
        {
            return ""ok"";
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\OrderService.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var ep = arr[0]!;
            Assert.Equal("wcf", (string?)ep["Kind"]);
            Assert.Equal("OrderService", (string?)ep["ControllerOrServiceName"]);
            Assert.Equal("SubmitOrder", (string?)ep["OperationName"]);
            Assert.Equal("string", (string?)ep["ReturnType"]);

            var parameters = ep["Parameters"] as JArray;
            Assert.NotNull(parameters);
            Assert.Single(parameters!);
            Assert.Equal("id", (string?)parameters![0]!["Name"]);
            Assert.Equal("int", (string?)parameters![0]!["Type"]);
        }

        [Fact]
        public void Analyze_CSharp_Ashx_File_Returns_Handler_Endpoint()
        {
            var code = "";
            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\TestHandler.ashx");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var ep = arr[0]!;
            Assert.Equal("ashx", (string?)ep["Kind"]);
            Assert.Equal("TestHandler", (string?)ep["ControllerOrServiceName"]);
            Assert.Equal("ProcessRequest", (string?)ep["OperationName"]);
            Assert.Equal("/TestHandler.ashx", (string?)ep["Route"]);
        }

        [Fact]
        public void Analyze_CSharp_Infers_Http_Method_From_Method_Name()
        {
            var code = @"
using System.Web.Http;

namespace Demo.Api
{
    public class UsersController : ApiController
    {
        public IHttpActionResult DeleteUser(int id)
        {
            return Ok();
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\UsersController.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Single(arr);

            var methods = arr[0]!["HttpMethods"]!.ToObject<string[]>();
            Assert.NotNull(methods);
            Assert.Contains("DELETE", methods!);
        }

        [Fact]
        public void Analyze_CSharp_Skips_NonPublic_Methods()
        {
            var code = @"
using System.Web.Http;

namespace Demo.Api
{
    public class UsersController : ApiController
    {
        [HttpGet]
        private IHttpActionResult Hidden()
        {
            return Ok();
        }
    }
}";

            var tree = CSharpSyntaxTree.ParseText(code);
            var root = tree.GetCompilationUnitRoot();

            var result = ApiEndpointAnalyzer.Analyze(root, @"C:\temp\UsersController.cs");

            var json = JsonConvert.SerializeObject(result);
            var arr = JArray.Parse(json);

            Assert.Empty(arr);
        }
    }
}
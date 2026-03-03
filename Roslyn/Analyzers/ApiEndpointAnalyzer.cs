using Microsoft.CodeAnalysis.CSharp.Syntax;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Roslyn.Analyzers
{
    /// <summary>
    /// Discovery-based API endpoint detector for legacy ASP.NET target systems.
    /// Detects WebAPI, MVC, ASMX, ASHX and WCF endpoint candidates from C# source.
    /// </summary>
    public static class ApiEndpointAnalyzer
    {
        private const string ControllerSuffix = "Controller";
        private const string AttributeSuffix = "Attribute";
        public static List<ApiEndpoint> Analyze(CompilationUnitSyntax root, string filePath)
        {
            var endpoints = new List<ApiEndpoint>();
            var fileName = Path.GetFileName(filePath);
            var fileExt = Path.GetExtension(filePath).ToLowerInvariant();

            // .ashx file itself (no class body to walk)
            if (fileExt == ".ashx")
            {
                endpoints.Add(new ApiEndpoint
                {
                    Kind = "ashx",
                    ControllerOrServiceName = Path.GetFileNameWithoutExtension(filePath),
                    OperationName = "ProcessRequest",
                    FilePath = filePath,
                    Route = "/" + fileName,
                    HttpMethods = new[] { "GET", "POST" },
                    Parameters = Array.Empty<EndpointParam>(),
                    ReturnType = "void",
                    Evidence = "File extension .ashx indicates an HTTP generic handler"
                });
                return endpoints;
            }

            foreach (var classDecl in root.DescendantNodes().OfType<ClassDeclarationSyntax>())
            {
                var className = classDecl.Identifier.Text;
                var baseTypes = classDecl.BaseList?.Types
                    .Select(t => t.Type.ToString()).ToList() ?? new List<string>();
                var classAttrs = classDecl.AttributeLists
                    .SelectMany(al => al.Attributes)
                    .Select(a => a.Name.ToString()).ToList();

                var kind = DetectKind(baseTypes, classAttrs);
                if (kind == null) continue;

                var routePrefix = GetRoutePrefix(classDecl, kind);

                // ASHX code-behind (IHttpHandler / IHttpAsyncHandler)
                if (kind == "ashx")
                {
                    endpoints.Add(new ApiEndpoint
                    {
                        Kind = "ashx",
                        ControllerOrServiceName = className,
                        OperationName = "ProcessRequest",
                        FilePath = filePath,
                        Route = routePrefix ?? ("/" + fileName),
                        HttpMethods = new[] { "GET", "POST" },
                        Parameters = Array.Empty<EndpointParam>(),
                        ReturnType = "void",
                        Evidence = "Implements IHttpHandler or IHttpAsyncHandler"
                    });
                    continue;
                }

                // WCF: each [OperationContract] method
                if (kind == "wcf")
                {
                    foreach (var method in classDecl.Members.OfType<MethodDeclarationSyntax>())
                    {
                        var methodAttrs = method.AttributeLists
                            .SelectMany(al => al.Attributes)
                            .Select(a => a.Name.ToString()).ToList();
                        if (!methodAttrs.Any(a => NormalizeAttr(a) == "OperationContract")) continue;

                        endpoints.Add(new ApiEndpoint
                        {
                            Kind = "wcf",
                            ControllerOrServiceName = className,
                            OperationName = method.Identifier.Text,
                            FilePath = filePath,
                            Route = routePrefix ?? "",
                            HttpMethods = Array.Empty<string>(),
                            Parameters = ExtractParams(method),
                            ReturnType = method.ReturnType?.ToString() ?? "void",
                            Evidence = BuildEvidence(baseTypes, classAttrs, methodAttrs, kind)
                        });
                    }
                    continue;
                }

                // ASMX: each [WebMethod] method
                if (kind == "asmx")
                {
                    foreach (var method in classDecl.Members.OfType<MethodDeclarationSyntax>())
                    {
                        var methodAttrs = method.AttributeLists
                            .SelectMany(al => al.Attributes)
                            .Select(a => a.Name.ToString()).ToList();
                        if (!methodAttrs.Any(a => NormalizeAttr(a) == "WebMethod")) continue;

                        endpoints.Add(new ApiEndpoint
                        {
                            Kind = "asmx",
                            ControllerOrServiceName = className,
                            OperationName = method.Identifier.Text,
                            FilePath = filePath,
                            Route = routePrefix ?? ("/" + fileName + "/" + method.Identifier.Text),
                            HttpMethods = new[] { "GET", "POST" },
                            Parameters = ExtractParams(method),
                            ReturnType = method.ReturnType?.ToString() ?? "void",
                            Evidence = BuildEvidence(baseTypes, classAttrs, methodAttrs, kind)
                        });
                    }
                    continue;
                }

                // WebAPI / MVC: walk public action methods
                foreach (var method in classDecl.Members.OfType<MethodDeclarationSyntax>())
                {
                    var methodAttrs = method.AttributeLists
                        .SelectMany(al => al.Attributes)
                        .Select(a => a.Name.ToString()).ToList();

                    var httpMethods = ExtractHttpMethods(methodAttrs);
                    bool hasRouteAttr = methodAttrs.Any(a => NormalizeAttr(a) == "Route");
                    bool returnsAction = IsActionResult(method.ReturnType?.ToString() ?? "");

                    // Only include action-like methods
                    if (!httpMethods.Any() && !hasRouteAttr && !returnsAction) continue;

                    // Skip non-public methods
                    bool isPublic = method.Modifiers.Any(m => m.Text == "public");
                    if (!isPublic) continue;

                    var methodRoute = ExtractMethodRoute(method, routePrefix, className, kind);

                    endpoints.Add(new ApiEndpoint
                    {
                        Kind = kind,
                        ControllerOrServiceName = className,
                        OperationName = method.Identifier.Text,
                        FilePath = filePath,
                        Route = methodRoute,
                        HttpMethods = httpMethods.Any()
                            ? httpMethods.ToArray()
                            : InferHttpMethods(method.Identifier.Text),
                        Parameters = ExtractParams(method),
                        ReturnType = method.ReturnType?.ToString() ?? "void",
                        Evidence = BuildEvidence(baseTypes, classAttrs, methodAttrs, kind)
                    });
                }
            }

            return endpoints;
        }

        // ------------------------------------------------------------------ helpers

        private static string? DetectKind(List<string> baseTypes, List<string> classAttrs)
        {
            // ASHX code-behind
            if (baseTypes.Any(b => b == "IHttpHandler" || b == "IHttpAsyncHandler"))
                return "ashx";

            // WCF
            if (classAttrs.Any(a => NormalizeAttr(a) == "ServiceContract"))
                return "wcf";

            // ASMX
            if (classAttrs.Any(a => NormalizeAttr(a) == "WebService"))
                return "asmx";
            if (baseTypes.Any(b => b == "WebService" || b.EndsWith(".WebService")))
                return "asmx";

            // ASP.NET Core / WebAPI 2 attribute-annotated controller
            if (classAttrs.Any(a => NormalizeAttr(a) == "ApiController"))
                return "webapi";

            // WebAPI 2 (inherits ApiController)
            if (baseTypes.Any(b => b == "ApiController" || b.EndsWith(".ApiController")
                                || b == "ControllerBase" || b.EndsWith(".ControllerBase")))
                return "webapi";

            // MVC
            if (baseTypes.Any(b => b == "Controller" || b.EndsWith(".Controller")))
                return "mvc";

            return null;
        }

        private static string NormalizeAttr(string attr)
        {
            // Strip generic args, then strip trailing "Attribute" suffix
            var name = attr.Contains('<') ? attr.Substring(0, attr.IndexOf('<')) : attr;
            if (name.EndsWith(AttributeSuffix))
                name = name.Substring(0, name.Length - AttributeSuffix.Length);
            return name;
        }

        private static string? GetRoutePrefix(ClassDeclarationSyntax classDecl, string kind)
        {
            foreach (var attrList in classDecl.AttributeLists)
            {
                foreach (var attr in attrList.Attributes)
                {
                    var n = NormalizeAttr(attr.Name.ToString());
                    if (n == "Route" || n == "RoutePrefix")
                    {
                        var arg = attr.ArgumentList?.Arguments.FirstOrDefault();
                        if (arg != null)
                        {
                            var val = arg.ToString().Trim('"').TrimStart('~').TrimStart('/');
                            return "/" + val;
                        }
                    }
                }
            }
            // Conventional fallback for MVC/WebAPI
            if (kind == "mvc" || kind == "webapi")
            {
                var name = classDecl.Identifier.Text;
                if (name.EndsWith(ControllerSuffix))
                    name = name.Substring(0, name.Length - ControllerSuffix.Length);
                return "/api/" + name;
            }
            return null;
        }

        private static List<string> ExtractHttpMethods(List<string> methodAttrs)
        {
            var result = new List<string>();
            foreach (var a in methodAttrs)
            {
                switch (NormalizeAttr(a))
                {
                    case "HttpGet":     result.Add("GET");     break;
                    case "HttpPost":    result.Add("POST");    break;
                    case "HttpPut":     result.Add("PUT");     break;
                    case "HttpDelete":  result.Add("DELETE");  break;
                    case "HttpPatch":   result.Add("PATCH");   break;
                    case "HttpOptions": result.Add("OPTIONS"); break;
                    case "HttpHead":    result.Add("HEAD");    break;
                }
            }
            return result.Distinct().ToList();
        }

        private static string[] InferHttpMethods(string methodName)
        {
            var lname = methodName.ToLowerInvariant();
            if (lname.StartsWith("get"))                                          return new[] { "GET" };
            if (lname.StartsWith("post") || lname.StartsWith("create")
                                         || lname.StartsWith("add"))             return new[] { "POST" };
            if (lname.StartsWith("put")  || lname.StartsWith("update"))         return new[] { "PUT" };
            if (lname.StartsWith("delete") || lname.StartsWith("remove"))       return new[] { "DELETE" };
            if (lname.StartsWith("patch"))                                        return new[] { "PATCH" };
            return Array.Empty<string>();
        }

        private static bool IsActionResult(string returnType)
        {
            var t = returnType.TrimStart();
            return t == "ActionResult"
                || t.StartsWith("ActionResult<")
                || t == "IActionResult"
                || t == "IHttpActionResult"
                || t.StartsWith("Task<ActionResult")
                || t.StartsWith("Task<IActionResult")
                || t.StartsWith("Task<IHttpActionResult");
        }

        private static string ExtractMethodRoute(
            MethodDeclarationSyntax method, string? routePrefix, string className, string kind)
        {
            foreach (var attrList in method.AttributeLists)
            {
                foreach (var attr in attrList.Attributes)
                {
                    if (NormalizeAttr(attr.Name.ToString()) == "Route")
                    {
                        var arg = attr.ArgumentList?.Arguments.FirstOrDefault();
                        if (arg != null)
                        {
                            var val = arg.ToString().Trim('"');
                            if (val.StartsWith("~/")) val = val.Substring(1);
                            if (!val.StartsWith("/")) val = (routePrefix ?? "") + "/" + val;
                            return val;
                        }
                    }
                }
            }
            return (routePrefix ?? "") + "/" + method.Identifier.Text;
        }

        private static EndpointParam[] ExtractParams(MethodDeclarationSyntax method)
        {
            if (method.ParameterList == null) return Array.Empty<EndpointParam>();
            return method.ParameterList.Parameters
                .Select(p => new EndpointParam
                {
                    Name = p.Identifier.Text,
                    Type = p.Type?.ToString() ?? "object"
                })
                .ToArray();
        }

        private static string BuildEvidence(
            List<string> baseTypes, List<string> classAttrs, List<string> methodAttrs, string kind)
        {
            var parts = new List<string> { "kind=" + kind };
            if (baseTypes.Any())  parts.Add("base types: " + string.Join(", ", baseTypes));
            if (classAttrs.Any()) parts.Add("class attrs: " + string.Join(", ", classAttrs));
            if (methodAttrs.Any()) parts.Add("method attrs: " + string.Join(", ", methodAttrs));
            return string.Join("; ", parts);
        }
    }

    public class ApiEndpoint
    {
        public string Kind { get; set; } = "";
        public string ControllerOrServiceName { get; set; } = "";
        public string OperationName { get; set; } = "";
        public string FilePath { get; set; } = "";
        public string Route { get; set; } = "";
        public string[] HttpMethods { get; set; } = Array.Empty<string>();
        public EndpointParam[] Parameters { get; set; } = Array.Empty<EndpointParam>();
        public string ReturnType { get; set; } = "";
        public string Evidence { get; set; } = "";
    }

    public class EndpointParam
    {
        public string Name { get; set; } = "";
        public string Type { get; set; } = "";
    }
}

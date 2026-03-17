using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class SqlCommandExtractorTests
    {
        private static (SyntaxTree tree, SemanticModel model) CreateCompilationContext(
    string code,
    string filePath = @"C:\temp\Test.cs")
        {
            var tree = CSharpSyntaxTree.ParseText(code, path: filePath);

            var refs = new List<MetadataReference>
    {
        MetadataReference.CreateFromFile(typeof(object).Assembly.Location),
        MetadataReference.CreateFromFile(typeof(Enumerable).Assembly.Location),
        MetadataReference.CreateFromFile(typeof(System.Data.CommandType).Assembly.Location)
    };

            var compilation = CSharpCompilation.Create("TestCompilation")
                .AddSyntaxTrees(tree)
                .AddReferences(refs);

            var model = compilation.GetSemanticModel(tree);
            return (tree, model);
        }

        [Fact]
        public void AnalyzeDocument_Detects_SqlCommand_Constructor()
        {
            var code = @"
using System.Data.SqlClient;

namespace Demo.Data
{
    public class UserRepo
    {
        public void Load()
        {
            var cmd = new SqlCommand(""SELECT * FROM Users"");
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.NotNull(results);
            Assert.Contains(results, r =>
                r.Kind == "SqlCommandCtor" &&
                r.SqlText == "SELECT * FROM Users" &&
                r.ClassName == "UserRepo" &&
                r.MethodName == "Load");
        }

        [Fact]
        public void AnalyzeDocument_Detects_CommandText_Assignment()
        {
            var code = @"
using System.Data.SqlClient;

namespace Demo.Data
{
    public class UserRepo
    {
        public void Load()
        {
            var cmd = new SqlCommand();
            cmd.CommandText = ""SELECT * FROM Users WHERE Id = 1"";
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.Kind == "CommandTextAssignment" &&
                r.SqlText == "SELECT * FROM Users WHERE Id = 1");
        }

        [Fact]
        public void AnalyzeDocument_Detects_CommandType_StoredProcedure()
        {
            var code = @"
using System.Data;
using System.Data.SqlClient;

namespace Demo.Data
{
    public class UserRepo
    {
        public void Load()
        {
            var cmd = new SqlCommand();
            cmd.CommandType = CommandType.StoredProcedure;
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.Kind == "CommandTypeAssignment" &&
                r.CommandTypeIsStoredProcedure);
        }

        [Fact]
        public void AnalyzeDocument_Resolves_Const_String()
        {
            var code = @"
using System.Data.SqlClient;

namespace Demo.Data
{
    public class UserRepo
    {
        private const string Sql = ""SELECT * FROM Users"";

        public void Load()
        {
            var cmd = new SqlCommand(Sql);
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.Kind == "SqlCommandCtor" &&
                r.SqlText == "SELECT * FROM Users");
        }

        [Fact]
        public void AnalyzeDocument_Resolves_String_Concatenation()
        {
            var code = @"
using System.Data.SqlClient;

namespace Demo.Data
{
    public class UserRepo
    {
        public void Load()
        {
            const string a = ""SELECT * "";
            const string b = ""FROM Users"";
            var cmd = new SqlCommand(a + b);
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.SqlText == "SELECT * FROM Users");
        }
        [Fact]
        public void AnalyzeDocument_Detects_Dapper_Invocation()
        {
            var code = @"
namespace Dapper
{
    public static class SqlMapper
    {
        public static object Query(object connection, string sql) => null;
    }
}

namespace Demo.Data
{
    public class UserRepo
    {
        public void Load(object connection)
        {
            Dapper.SqlMapper.Query(connection, ""SELECT * FROM Users"");
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.Kind == "DapperInvocation" &&
                r.SqlText == "SELECT * FROM Users");
        }

        [Fact]
        public void AnalyzeDocument_Detects_EF_Invocation()
        {
            var code = @"
namespace Microsoft.EntityFrameworkCore
{
    public static class RelationalQueryableExtensions
    {
        public static object FromSqlRaw(object set, string sql) => null;
    }
}

namespace Demo.Data
{
    public class FakeDb
    {
        public object Users { get; } = new object();
    }

    public class UserRepo
    {
        public void Load(FakeDb db)
        {
            Microsoft.EntityFrameworkCore.RelationalQueryableExtensions.FromSqlRaw(
                db.Users,
                ""SELECT * FROM Users"");
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");

            var results = SqlCommandExtractor.AnalyzeDocument(tree, model, @"C:\temp\UserRepo.cs");

            Assert.Contains(results, r =>
                r.Kind == "EFInvocation" &&
                r.SqlText == "SELECT * FROM Users");
        }

        [Fact]
        public void AnalyzeDbWrapperCalls_Detects_Read_With_String_Variable()
        {
            var code = @"
namespace Demo.Data
{
    public class UserRepo
    {
        public object Load(dynamic db)
        {
            string spname = ""sp_TAMS_GetTarByTarId"";
            return db.Read(spname, null, null);
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");
            var root = tree.GetRoot();

            var results = SqlCommandExtractor.AnalyzeDbWrapperCalls(root, model, @"C:\temp\UserRepo.cs").ToList();

            Assert.NotEmpty(results);
            Assert.Contains(results, r =>
                r.Kind == "DbWrapperCall" &&
                r.SqlText == "sp_TAMS_GetTarByTarId" &&
                r.InferredStoredProcedures.Contains("sp_TAMS_GetTarByTarId"));
        }

        [Fact]
        public void AnalyzeDbWrapperCalls_Detects_Assigned_String_Variable()
        {
            var code = @"
namespace Demo.Data
{
    public class UserRepo
    {
        public object Load(dynamic db)
        {
            string spname;
            spname = ""sp_GetUsers"";
            return db.Execute(spname);
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");
            var root = tree.GetRoot();

            var results = SqlCommandExtractor.AnalyzeDbWrapperCalls(root, model, @"C:\temp\UserRepo.cs").ToList();

            Assert.Contains(results, r =>
                r.Kind == "DbWrapperCall" &&
                r.SqlText == "sp_GetUsers");
        }

        [Fact]
        public void AnalyzeDbWrapperCalls_Ignores_NonString_Variables()
        {
            var code = @"
namespace Demo.Data
{
    public class UserRepo
    {
        public object Load(dynamic db)
        {
            int x = 123;
            return db.Read(x);
        }
    }
}";

            var (tree, model) = CreateCompilationContext(code, @"C:\temp\UserRepo.cs");
            var root = tree.GetRoot();

            var results = SqlCommandExtractor.AnalyzeDbWrapperCalls(root, model, @"C:\temp\UserRepo.cs").ToList();

            Assert.Empty(results);
        }
    }
}
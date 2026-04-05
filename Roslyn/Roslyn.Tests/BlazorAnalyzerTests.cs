using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Xunit;

namespace Roslyn.Analyzers.Tests
{
    public class RazorComponentExtractorTests
    {
        [Fact]
        public void Path_Detection_Works()
        {
            Assert.True(RazorComponentExtractor.IsRazorComponentPath("Counter.razor"));
            Assert.True(RazorComponentExtractor.IsRazorComponentPath(@"C:\temp\Pages\Dashboard.razor"));
            Assert.False(RazorComponentExtractor.IsRazorComponentPath("Index.cshtml"));
            Assert.False(RazorComponentExtractor.IsRazorComponentPath("site.master"));
        }

        [Fact]
        public void Analyze_Sets_File_Type_Flag_Correctly()
        {
            var code = "<h1>Hello</h1>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Counter.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            Assert.True((bool)obj["isRazorComponent"]!);
            Assert.Equal("Counter.razor", (string?)obj["file"]);
            Assert.Equal(@"C:\temp\Counter.razor", (string?)obj["path"]);
        }

        [Fact]
        public void Analyze_Extracts_Directives_And_Injections()
        {
            var code = @"@page ""/counter""
@layout MainLayout
@using MyApp.Shared
@inject NavigationManager Nav
@typeparam TItem
@implements IDisposable
@attribute [Authorize]

<h1>Counter</h1>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Counter.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var directives = obj["directives"] as JArray;
            Assert.NotNull(directives);

            var directiveNames = directives!
                .Select(d => (string?)d!["directive"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("@page", directiveNames);
            Assert.Contains("@layout", directiveNames);
            Assert.Contains("@using", directiveNames);
            Assert.Contains("@inject", directiveNames);
            Assert.Contains("@typeparam", directiveNames);
            Assert.Contains("@implements", directiveNames);
            Assert.Contains("@attribute", directiveNames);

            var injections = obj["injections"] as JArray;
            Assert.NotNull(injections);
            Assert.Single(injections!);
            Assert.Equal("NavigationManager", (string?)injections![0]!["serviceType"]);
            Assert.Equal("Nav", (string?)injections![0]!["name"]);
        }

        [Fact]
        public void Analyze_Extracts_Code_Blocks_Parameters_And_Lifecycle_Methods()
        {
            var code = @"@page ""/users""

@code {
    [Parameter]
    public int UserId { get; set; }

    [CascadingParameter]
    public string Theme { get; set; }

    protected override void OnInitialized()
    {
    }

    protected override Task OnParametersSetAsync()
    {
        return Task.CompletedTask;
    }
}";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Users.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var codeBlocks = obj["codeBlocks"] as JArray;
            Assert.NotNull(codeBlocks);
            Assert.Single(codeBlocks!);
            Assert.Equal("@code", (string?)codeBlocks![0]!["kind"]);

            var parameters = obj["parameters"] as JArray;
            Assert.NotNull(parameters);
            Assert.Equal(2, parameters!.Count);

            var paramNames = parameters.Select(p => (string?)p!["name"]).ToArray();
            Assert.Contains("UserId", paramNames);
            Assert.Contains("Theme", paramNames);

            var userId = parameters.First(p => (string?)p!["name"] == "UserId");
            Assert.Equal("Parameter", (string?)userId!["attribute"]);
            Assert.Equal("int", (string?)userId!["type"]);

            var theme = parameters.First(p => (string?)p!["name"] == "Theme");
            Assert.Equal("CascadingParameter", (string?)theme!["attribute"]);
            Assert.Equal("string", (string?)theme!["type"]);

            var lifecycleMethods = obj["lifecycleMethods"] as JArray;
            Assert.NotNull(lifecycleMethods);

            var lifecycleNames = lifecycleMethods!
                .Select(x => (string?)x!["name"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("OnInitialized", lifecycleNames);
            Assert.Contains("OnParametersSetAsync", lifecycleNames);
        }

        [Fact]
        public void Analyze_Extracts_Event_Bindings_And_Bind_Attributes()
        {
            var code = @"<InputText @bind-Value=""Model.Name"" />
<input @bind=""searchText"" />
<button @onclick=""Save"">Save</button>
<select @onchange=""HandleChange""></select>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Form.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var eventBindings = obj["eventBindings"] as JArray;
            Assert.NotNull(eventBindings);
            Assert.True(eventBindings!.Count >= 1);

            var eventNames = eventBindings
                .Select(e => (string?)e!["eventName"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("@onclick", eventNames);

            var bindAttributes = obj["bindAttributes"] as JArray;
            Assert.NotNull(bindAttributes);
            Assert.True(bindAttributes!.Count >= 1);

            var bindNames = bindAttributes
                .Select(b => (string?)b!["bindName"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("@bind", bindNames);
        }

        [Fact]
        public void Analyze_Extracts_Forms_Inputs_Buttons_And_Links()
        {
            var code = @"<EditForm Model=""@person"" OnValidSubmit=""HandleValidSubmit"">
    <InputText id=""name"" @bind-Value=""person.Name"" class=""form-control"" />
    <button type=""submit"" class=""btn btn-primary"" @onclick=""Save"">Save</button>
    <a href=""/users/1"" class=""nav-link"">Profile</a>
    <NavLink href=""/dashboard"" Match=""NavLinkMatch.All"">Dashboard</NavLink>
</EditForm>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Form.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var forms = obj["forms"] as JArray;
            Assert.NotNull(forms);
            Assert.Single(forms!);
            Assert.Equal("EditForm", (string?)forms![0]!["tag"]);
            Assert.Equal("@person", (string?)forms![0]!["model"]);
            Assert.Equal("HandleValidSubmit", (string?)forms![0]!["onValidSubmit"]);

            var inputs = obj["inputs"] as JArray;
            Assert.NotNull(inputs);
            Assert.Single(inputs!);
            Assert.Equal("InputText", (string?)inputs![0]!["tag"]);
            Assert.Equal("name", (string?)inputs![0]!["id"]);
            Assert.Equal("person.Name", (string?)inputs![0]!["bind"]);

            var buttons = obj["buttons"] as JArray;
            Assert.NotNull(buttons);
            Assert.Single(buttons!);
            Assert.Equal("submit", (string?)buttons![0]!["type"]);
            Assert.Equal("Save", (string?)buttons![0]!["text"]);
            Assert.Equal("Save", (string?)buttons![0]!["onclick"]);

            var links = obj["links"] as JArray;
            Assert.NotNull(links);
            Assert.Equal(2, links!.Count);

            var tags = links.Select(l => (string?)l!["tag"]).ToArray();
            Assert.Contains("a", tags);
            Assert.Contains("NavLink", tags);
        }

        [Fact]
        public void Analyze_Extracts_Headings_Tables_Modals_DisplayRegions_And_ComponentUsages()
        {
            var code = @"<h2 id=""title"" class=""page-header"">User Dashboard</h2>

<MyGrid Items=""@Items"" />
<Shared.NavMenu />

<table id=""usersTable"" class=""table table-striped"">
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
        </tr>
    </thead>
</table>

<div id=""detailsModal"" class=""modal fade""></div>
<canvas id=""salesChart""></canvas>
<div class=""summary-panel""></div>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Dashboard.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var headings = obj["headings"] as JArray;
            Assert.NotNull(headings);
            Assert.Single(headings!);
            Assert.Equal("h2", (string?)headings![0]!["level"]);
            Assert.Equal("User Dashboard", (string?)headings![0]!["text"]);

            var tables = obj["tables"] as JArray;
            Assert.NotNull(tables);
            Assert.Single(tables!);

            var headers = ((JArray?)tables![0]!["headers"])!.Select(x => (string?)x).ToArray();
            Assert.Contains("Name", headers);
            Assert.Contains("Email", headers);

            var modals = obj["modals"] as JArray;
            Assert.NotNull(modals);
            Assert.Single(modals!);
            Assert.Equal("detailsModal", (string?)modals![0]!["id"]);

            var displayRegions = obj["displayRegions"] as JArray;
            Assert.NotNull(displayRegions);

            var regionTypes = displayRegions!
                .Select(x => (string?)x!["regionType"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("table-region", regionTypes);
            Assert.Contains("canvas-region", regionTypes);
            Assert.Contains("summary-region", regionTypes);

            var componentUsages = obj["componentUsages"] as JArray;
            Assert.NotNull(componentUsages);
            Assert.True(componentUsages!.Count >= 2);

            var componentNames = componentUsages
                .Select(c => (string?)c!["component"])
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("MyGrid", componentNames);
            Assert.Contains("Shared.NavMenu", componentNames);
        }

        [Fact]
        public void Analyze_Builds_Summary_Hints_Correctly()
        {
            var code = @"@page ""/dashboard""
@inject NavigationManager Nav

<EditForm Model=""@person"" OnValidSubmit=""Save"">
    <InputText @bind-Value=""person.Name"" />
    <button @onclick=""Save"">Save</button>
</EditForm>

<table>
    <tr><th>Name</th></tr>
</table>

<MyGrid Items=""@Items"" />

@code {
    [Parameter]
    public int Id { get; set; }

    protected override void OnInitialized()
    {
    }
}";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Dashboard.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var summaryHints = obj["summaryHints"];
            Assert.NotNull(summaryHints);

            Assert.True((bool)summaryHints!["hasRouteDirective"]!);
            Assert.True((bool)summaryHints!["hasInjection"]!);
            Assert.True((bool)summaryHints!["hasParameters"]!);
            Assert.True((bool)summaryHints!["hasLifecycleMethods"]!);
            Assert.True((bool)summaryHints!["hasForms"]!);
            Assert.True((bool)summaryHints!["hasTabularDisplay"]!);

            var clues = summaryHints["clues"] as JArray;
            Assert.NotNull(clues);

            var clueTexts = clues!
                .Select(c => (string?)c)
                .Where(x => x != null)
                .ToArray();

            Assert.Contains("declares a routable component", clueTexts);
            Assert.Contains("injects framework or application services", clueTexts);
            Assert.Contains("accepts component parameters", clueTexts);
            Assert.Contains("uses Blazor lifecycle methods", clueTexts);
            Assert.Contains("contains form or edit-form handling", clueTexts);
            Assert.Contains("contains tabular data display", clueTexts);
        }

        [Fact]
        public void Analyze_Removes_Code_Blocks_From_Markup_Extraction()
        {
            var code = @"@code {
    private string Hidden = ""ShouldNotAppear"";
    void BuildTable() { }
}

<h1>Visible Heading</h1>";

            var result = RazorComponentExtractor.Analyze(code, @"C:\temp\Test.razor");
            var obj = JObject.Parse(JsonConvert.SerializeObject(result));

            var headings = obj["headings"] as JArray;
            Assert.NotNull(headings);
            Assert.Single(headings!);
            Assert.Equal("Visible Heading", (string?)headings![0]!["text"]);

            var componentUsages = obj["componentUsages"] as JArray;
            Assert.NotNull(componentUsages);
            Assert.Empty(componentUsages!);
        }
    }
}
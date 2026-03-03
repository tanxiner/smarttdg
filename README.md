# SmartTDG

SmartTDG is a local technical documentation generator for legacy ASP.NET systems. It analyzes an uploaded zip or folder of source code and produces a single compiled `Complete_Documentation.md` containing:

- **Web Pages** – documentation for ASPX pages and their code-behind
- **Modules/Others** – documentation for utility classes and modules
- **Database Reference (SQL)** – documentation for stored procedures
- **API Reference** – discovery-based documentation for API endpoints (WebAPI, MVC, ASMX, ASHX, WCF)

## API Reference Generation

The pipeline automatically detects API endpoint candidates across all supported ASP.NET patterns:

| Pattern | Detection Criteria |
| :--- | :--- |
| **WebAPI** | Classes inheriting `ApiController` / `ControllerBase`, or annotated with `[ApiController]` |
| **MVC** | Classes inheriting `Controller` with action methods returning `ActionResult` / `IActionResult` |
| **ASMX** | Classes annotated with `[WebService]`; methods annotated with `[WebMethod]` |
| **ASHX** | `.ashx` files and classes implementing `IHttpHandler` / `IHttpAsyncHandler` |
| **WCF** | Classes annotated with `[ServiceContract]`; methods annotated with `[OperationContract]` |

For each detected endpoint the analyzer captures (best-effort): kind, controller/service name, operation name, source file, route, HTTP methods, parameters, return type, and detection evidence.

The API Reference section is appended automatically to `flask/backend/final_output/Complete_Documentation.md`. If no endpoints are detected the section is omitted and the pipeline continues without error.

## Pipeline Definition

All downstream Python scripts (diagram generation, splitters, analysis, and compilation) are executed in the order defined by the **single canonical pipeline file**:

```
flask/backend/pipeline.json
```

Both entrypoints read this file at runtime:

| Entrypoint | Role |
| :--- | :--- |
| `flask/backend/app.py` | Web UI – invoked when a user uploads a ZIP via the browser |
| `Roslyn/Program.cs` | CLI/batch – invoked directly via `dotnet run` |

### Adding, removing, or reordering steps

Edit `flask/backend/pipeline.json` only. Each step entry contains:

| Field | Description |
| :--- | :--- |
| `name` | Short identifier (used for log messages and job-status keys) |
| `script` | Path relative to `flask/backend/` using forward slashes |
| `phase` | Execution phase: `diagram`, `splitter`, `analysis`, or `compile` |
| `timeout_seconds` | *(optional)* Per-script timeout; omit or set to `0` for no timeout |

The `phase` field controls execution ordering in `app.py` (diagram → splitter → analysis → compile) and is informational in `Program.cs` (scripts run in array order regardless of phase).

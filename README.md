# SmartTDG

SmartTDG is a local technical documentation generator for legacy ASP.NET systems. It analyzes an uploaded zip or folder of source code and produces a single compiled `Technical_Documentation.md` containing:

- **Web Pages** – documentation for ASPX pages and their code-behind
- **Modules/Others** – documentation for utility classes and modules
- **Database Reference (SQL)** – documentation for stored procedures
- **API Reference** – discovery-based documentation for API endpoints (WebAPI, MVC, ASMX, ASHX, WCF)


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

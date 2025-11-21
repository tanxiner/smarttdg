import time
import os
import json
import graphviz
from langchain_ollama import OllamaLLM
import subprocess

# --- CONFIG ---
MODEL_NAME = "gpt-oss:latest"
OUTPUT_FILE = "technical_docs.md"
OUTPUT_FILE_SQL = "sql_docs.md"
llm = OllamaLLM(model=MODEL_NAME)
MAX_CHARS = 200_000

# Construct the path to the "all_analysis_results.json" file in the "My Documents" directory
input_path = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results.json")

# Construct the path to the "all_analysis_results.json" file in the "My Documents" directory
input_path_sql = os.path.join(os.path.expanduser("~"), "Documents", "sql_analysis_results.md")

# ----------------- MAIN PIPELINE -----------------
def preprocess_roslyn_output(roslyn_output):
    """
    Preprocess Roslyn output to include methods, fields, properties for PlantUML generation.
    Attaches file-level members to their classes if class exists; otherwise keeps them separate.
    """
    def first_or_default(lst, default=None):
        return lst[0] if lst else default

    architecture_info = {
        "files": [],
        "usings": set(),
        "namespaces": set(),
        "modules": set(),
        "dependencies": {},
        "assemblies": {},
        "inferred_assemblies": {},
        "file_dependencies": {},
        "method_calls": {},
        "cross_file_dependencies": {},
        "enum_names": set(),
        "struct_names": set(),
        "record_names": set(),
    }

    classes = []
    functions = []

    if not isinstance(roslyn_output, list):
        roslyn_output = [roslyn_output]

    for file_output in roslyn_output:
        if not isinstance(file_output, dict):
            continue

        file_name = file_output.get("file") or file_output.get("FileName") or "Unknown"
        architecture_info["files"].append(file_name)

        namespaces_list = file_output.get("namespaces") or []
        for ns in namespaces_list:
            if ns:
                architecture_info["namespaces"].add(ns)
                architecture_info["modules"].add(ns)

        # Normalize classes
        file_classes = file_output.get("classes") or []
        main_class = first_or_default(file_classes, {})
        main_class_name = main_class.get("Name") or main_class.get("name")

        # Attach file-level methods, fields, properties to the main class
        if main_class:
            # METHODS
            file_methods = file_output.get("methods") or []
            main_class.setdefault("Methods", []).extend(
                [{"Name": m} if isinstance(m, str) else m for m in file_methods]
            )
            for m in file_methods:
                if isinstance(m, str):
                    functions.append({
                        "Name": m,
                        "Class": main_class_name,
                        "FileName": file_name,
                        "Namespace": first_or_default(namespaces_list, "Unknown")
                    })

            # FIELDS
            file_fields = file_output.get("fields") or []
            main_class.setdefault("Fields", []).extend(file_fields)

            # PROPERTIES
            file_props = file_output.get("properties") or []
            main_class.setdefault("Properties", []).extend(file_props)

        # Add class info
        for cls in file_classes:
            if not isinstance(cls, dict):
                continue
            name = cls.get("Name") or cls.get("name")
            ns = cls.get("Namespace") or first_or_default(namespaces_list, "Unknown")
            cls["Namespace"] = ns
            cls["FileName"] = file_name
            classes.append(cls)

            # Attach nested methods if present
            for method in cls.get("Methods") or []:
                if isinstance(method, dict):
                    method.setdefault("Class", name)
                    method.setdefault("FileName", file_name)
                    method.setdefault("Namespace", ns)
                    functions.append(method)

        # INTERFACES
        for iface in file_output.get("interfaces") or []:
            if not isinstance(iface, dict):
                continue
            name = iface.get("Name") or iface.get("name")
            ns = iface.get("Namespace") or first_or_default(namespaces_list, "Unknown")
            iface["Namespace"] = ns
            iface["FileName"] = file_name
            classes.append(iface)
            for method in iface.get("Methods") or []:
                if isinstance(method, dict):
                    method.setdefault("Interface", name)
                    method.setdefault("FileName", file_name)
                    method.setdefault("Namespace", ns)
                    functions.append(method)

        # STRUCTS / ENUMS / RECORDS
        for struct in file_output.get("structs") or []:
            name = struct.get("Name") or struct.get("name")
            if name:
                architecture_info["struct_names"].add(name)

        for record in file_output.get("records") or []:
            name = record.get("Name") or record.get("name")
            if name:
                architecture_info["record_names"].add(name)

        for enum in file_output.get("enums") or []:
            name = enum.get("Name") or enum.get("name")
            if name:
                architecture_info["enum_names"].add(name)

        # Dependencies
        deps_root = file_output.get("dependencies", {})
        if isinstance(deps_root, dict):
            deps = deps_root.get("dependencies", {})
            if isinstance(deps, dict):
                for dep_type, dep_data in deps.items():
                    architecture_info.setdefault(dep_type, {})
                    if isinstance(dep_data, dict):
                        for k, v in dep_data.items():
                            architecture_info[dep_type][k] = v
                    elif isinstance(dep_data, list):
                        architecture_info[dep_type].setdefault(file_name, []).extend(dep_data)

    # Finalize sets
    for key in ["usings", "namespaces", "modules", "enum_names", "struct_names", "record_names"]:
        architecture_info[key] = sorted(architecture_info[key])

    architecture_info["files"] = sorted(set(architecture_info["files"]))

    return architecture_info, classes, functions





def generate_full_documentation(architecture_info, classes, functions):
    """
    Feeds everything at once to the AI to produce coherent documentation.
    Includes advanced dependency/callgraph information.
    """
    system_context = {
        "architecture": architecture_info,
        "classes": classes,
        "functions": functions
    }

    prompt = f"""
You are an expert technical writer creating documentation for a software system.

Here is the structured analysis output (from static analysis):
{json.dumps(system_context, indent=2)}

Write a comprehensive technical document that includes (Do not need to mention registration, login, or authentication for login):
1. A high-level overview describing its purpose and usage.
2. A section on key classes, structs, records, enums, and interfaces, summarizing their purpose and relationships.
3. A section on core functions/methods, explaining their roles and behaviors.
4. A concluding summary tying together how components collaborate.

Guidelines:
- Use clear professional language.
- Avoid code repetition unless helpful for clarity.
- Make it flow like a narrative — not disjointed summaries.
"""
    result = llm.invoke(prompt)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Cohesive documentation generated in {OUTPUT_FILE}")


def read_md_truncate(path, max_chars=MAX_CHARS):
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except Exception:
        text = raw.decode("utf-8", errors="replace")
    return text



def generate_sql_documentation(input_path_sql):
    md_text = read_md_truncate(input_path_sql)
    prompt = f"""
Do NOT include any commentary, and NO internal notes or thoughts. Do NOT spell out acronyms in full, just use the acronyms as it is.
You are an expert technical writer, product-focused systems architect, and database analyst. 
I will provide a consolidated SQL analysis of this system: a list of stored-procedure summaries. 
Your job is to read the whole analysis and write what the software is about — 
its purpose, main features, primary workflows, key actors, and the core data domains it touches. 
Focus on business and operational context, not SQL internals.

INPUT {md_text}

TASK — required outputs (Markdown only) Produce a single Markdown document containing the sections below, in this order. 
Be concise and avoid low-level SQL code unless absolutely necessary to justify a claim. 
Do NOT invent facts. Do not include any commentary, and NO internal notes or thoughts.
Use the acronyms exactly as they appear in the input. Do not expand, spell out, or provide definitions for any acronyms at any point. 
Wherever an acronym appears, leave it as-is without any additional explanation. Not even in the title or purpose.

1. Title & one-line purpose (Remember: never spell out acronyms anywhere, not even in title or the one-line purpose.)
- One-line purpose (<= 20 words).
2. Short overview (2–4 sentences)
- What the software does.
3. Features (bullet list)
- For each feature: 1–2 sentences of user-facing behavior and which procedures support it (cite proc names).
4. Primary workflows (each with):
- Workflow name
- Trigger/actor (who starts it)
- Ordered steps (1,2,3...) showing entry point → main stored procedure(s) → main data effects (reads/writes/tables)
- One-line evidence (proc names or source refs)
5. Key data domains and artifacts
- Complete list of main tables/entities (e.g., Personnel, Orders, Qualification, Logs) and what they represent in business terms.
- Note any staging/temp table patterns or heavy-use tables (if evident).


"""
    result = llm.invoke(prompt)

    with open(OUTPUT_FILE_SQL, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Cohesive documentation generated in {OUTPUT_FILE_SQL}")


def generate_dependency_diagram(architecture_info, output_file="dependency_diagram"):
    """
    Generates a dependency diagram for modules and their dependencies.
    Handles both C# and VB output formats.
    """
    dot = graphviz.Digraph(comment='Dependency Diagram', format='png')

    # Add nodes for each module/namespace
    for module in architecture_info.get("modules", []):
        dot.node(module, module)

    # Add edges for usings/imports
    deps_obj = architecture_info.get("dependencies", {})
    deps_inner = deps_obj.get("dependencies", {})

    # Collect dependencies from 'Usings' and 'Imports' (lists)
    dependency_list = set()
    for key in ["Usings", "Imports"]:
        values = deps_inner.get(key, [])
        if isinstance(values, list):
            dependency_list.update(values)

    # Draw edges from modules to their dependencies
    for module in architecture_info.get("modules", []):
        for dep in dependency_list:
            if dep and dep != module:  # avoid self-dependency
                dot.edge(module, dep)

    # Add cross-file dependencies
    for file, refs in architecture_info.get("cross_file_dependencies", {}).items():
        for ref in refs:
            dot.edge(file, ref)

    # Render diagram
    dot.render(output_file, cleanup=True)
    print(f"Dependency diagram generated: {output_file}.png")

def generate_class_diagram(classes, architecture_info=None, output_file="class_diagram"):
    """
    Generates a PlantUML class diagram including methods and properties (no fields).
    Handles both string and dict representations from Roslyn output.
    Deduplicates classes and edges.
    """
    plantuml_code = "@startuml\n"
    added_classes = set()
    added_edges = set()

    # Classes / Interfaces
    for cls in classes:
        class_name = cls.get("Name") or cls.get("name")
        if not class_name or class_name in added_classes:
            continue
        added_classes.add(class_name)

        # Methods
        methods = cls.get("Methods") or cls.get("methods") or []
        method_lines = []
        for m in methods:
            if isinstance(m, dict):
                method_name = m.get("Name") or m.get("name")
                if method_name:
                    method_lines.append(f"+ {method_name}()")
            elif isinstance(m, str):
                method_lines.append(f"+ {m}()")

        # Properties
        props = cls.get("Properties") or cls.get("properties") or []
        for p in props:
            if isinstance(p, dict):
                pname = p.get("Name") or p.get("name")
                if pname:
                    method_lines.append(f"+ {pname}")
            elif isinstance(p, str):
                method_lines.append(f"+ {p}")

        methods_str = "\n  ".join(method_lines)
        plantuml_code += f"class {class_name} {{\n  {methods_str}\n}}\n\n"

        # Inheritance
        base = cls.get("BaseClass") or cls.get("baseType")
        if base:
            edge = (class_name, base, "--|>")
            if edge not in added_edges:
                plantuml_code += f"{class_name} --|> {base}\n"
                added_edges.add(edge)

        # Interfaces
        for iface in cls.get("Interfaces") or cls.get("interfaces") or []:
            edge = (class_name, iface, "..|>")
            if edge not in added_edges:
                plantuml_code += f"{class_name} ..|> {iface}\n"
                added_edges.add(edge)

    # Structs, records, enums
    if architecture_info:
        for struct_name in architecture_info.get("struct_names", []):
            if struct_name not in added_classes:
                plantuml_code += f"struct {struct_name}\n"
                added_classes.add(struct_name)
        for record_name in architecture_info.get("record_names", []):
            if record_name not in added_classes:
                plantuml_code += f"class {record_name} <<record>>\n"
                added_classes.add(record_name)
        for enum_name in architecture_info.get("enum_names", []):
            if enum_name not in added_classes:
                plantuml_code += f"enum {enum_name}\n"
                added_classes.add(enum_name)

    plantuml_code += "@enduml\n"

    # === Find plantuml.jar ===
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):
        jar_path = os.path.join(current_dir, "plantuml.jar")
        if os.path.exists(jar_path):
            base_dir = current_dir
            break
        current_dir = os.path.dirname(current_dir)
    else:
        print("plantuml.jar not found")
        return

    # Output files
    puml_file = os.path.join(base_dir, f"{output_file}.puml")
    svg_file = os.path.join(base_dir, f"{output_file}.svg")

    # Write .puml
    with open(puml_file, "w") as f:
        f.write(plantuml_code)
    print(f"Class diagram source generated: {puml_file}")

    # Generate SVG
    try:
        subprocess.run(["java", "-jar", jar_path, "-tsvg", puml_file], check=True)
        print(f"SVG generated: {svg_file}")
    except FileNotFoundError:
        print("Java not found. Please install Java and add it to PATH.")
    except subprocess.CalledProcessError as e:
        print(f"PlantUML error: {e}")





# Load the JSON data from the file
try:
    # print(output_path)
    start_time = time.perf_counter()
    # print(f"Loading Roslyn output from: {input_path}")

    # # Load JSON data
    # with open(input_path, "r", encoding="utf-8") as f:
    #     roslyn_output = json.load(f)

    # # Ensure it's a list
    # if not isinstance(roslyn_output, list):
    #     roslyn_output = [roslyn_output]

    # # Count total classes/interfaces safely
    # total_classes = 0
    # for idx, file_output in enumerate(roslyn_output):
    #     if not isinstance(file_output, dict):
    #         print(f"Skipping top-level entry at index {idx}: not a dict, got {type(file_output)} -> {file_output}")
    #         continue
    #     total_classes += len(file_output.get("classes", [])) + len(file_output.get("interfaces", []))

    # print(f"Number of files in Roslyn output: {len(roslyn_output)}")
    # print(f"Total classes in input data: {total_classes}")

    # print("Preprocessing Roslyn output...")
    # architecture_info, classes, functions = preprocess_roslyn_output(roslyn_output)

    # print("Generating documentation...")
    # generate_full_documentation(architecture_info, classes, functions)
    #md_text = read_md_truncate(input_path_sql)
    #print(md_text)
    print(f"Start SQL Documentation")
    generate_sql_documentation(input_path_sql)
    
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"Documentation generation took {elapsed:.2f} seconds.")

    # Generate diagrams
    # generate_dependency_diagram(architecture_info)
    # generate_class_diagram(classes, architecture_info)

except Exception as e:
    print("Error:", e)




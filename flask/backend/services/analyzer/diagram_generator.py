import os
import json
import re
from typing import Dict, List, Any, Optional, Tuple


class DiagramGenerator:
    """
    Generate Mermaid diagrams from static analysis output.

    Key improvements in this version:
    - Class diagram is split ONLY when big (by namespace + paging).
    - Each class diagram includes ONLY Mermaid-safe member lines:
        - Properties/Fields: NameOnly
        - Methods: MethodName()
      (no types, no params, no {static})
    - Writes an index file ONLY when split.
    """

    # clamp to avoid browser lockups
    MAX_PAYLOAD_LINES = 2500

    # per class block
    MAX_METHODS_PER_CLASS = 25
    MAX_PROPERTIES_PER_CLASS = 25
    MAX_FIELDS_PER_CLASS = 15

    # class diagram splitting / readability
    SPLIT_THRESHOLD_CLASSES = 140            # ✅ ONLY split when total classes > this
    MAX_CLASSES_PER_NAMESPACE_DIAGRAM = 60   # if more, it will page (ns part1/part2...)
    MAX_CLASSES_PER_PAGE = 55                # paging size when a namespace is huge
    KEY_CLASSES_PER_NAMESPACE = 999999       # keep all by default (no pruning)
    INCLUDE_RELATIONSHIPS = True

    def __init__(self, analysis_data: List[Dict], output_dir: str = None):
        # Ensure analysis_data is a list of dicts, not strings
        self.analysis_data: List[Dict[str, Any]] = []
        if analysis_data:
            for item in analysis_data:
                parsed_item = item
                if isinstance(item, str):
                    try:
                        parsed_item = json.loads(item)
                    except Exception:
                        continue

                if isinstance(parsed_item, dict):
                    # sanitize nested 'classes' if they are strings
                    if "classes" in parsed_item and isinstance(parsed_item["classes"], list):
                        sanitized_classes = []
                        for cls in parsed_item["classes"]:
                            if isinstance(cls, str):
                                try:
                                    sanitized_classes.append(json.loads(cls))
                                except Exception:
                                    pass
                            elif isinstance(cls, dict):
                                sanitized_classes.append(cls)
                        parsed_item["classes"] = sanitized_classes

                    self.analysis_data.append(parsed_item)

        self.output_dir = output_dir or os.path.join(
            os.path.dirname(__file__), "..", "..", "analysis_output", "Diagrams"
        )
        os.makedirs(self.output_dir, exist_ok=True)

    # ---------------------------
    # Mermaid safety helpers
    # ---------------------------

    def _sanitize_class_name(self, name: str) -> str:
        """Sanitize class/type name for Mermaid classDiagram compatibility."""
        if not name or name == "null":
            return "Unknown"
        s = str(name).strip()
        s = s.replace("global::", "").replace("::", ".")
        s = s.replace("<", "_").replace(">", "_")
        s = s.replace("‹", "_").replace("›", "_").replace("«", "_").replace("»", "_")
        s = re.sub(r"[^A-Za-z0-9_]", "_", s)
        if s and s[0].isdigit():
            s = f"C_{s}"
        return s or "Unknown"

    def _sanitize_node_name(self, name: str) -> str:
        """Sanitize node name for Mermaid flowcharts (must not start with digit)."""
        if not name:
            return "N_Unknown"
        s = re.sub(r"[^\w\-\.]", "_", str(name))
        s = s.replace(".", "_")

        # Mermaid node IDs should not start with a digit
        if s and s[0].isdigit():
            s = "N_" + s

        # also avoid empty result
        return s or "N_Unknown"

    def _escape_label(self, s: Any) -> str:
        t = "" if s is None else str(s)
        t = t.replace('"', "'")      # avoid breaking ["..."]
        t = t.replace("[", "(").replace("]", ")")
        t = t.replace("\n", " ").replace("\r", " ")
        return t.strip()

    def _clamp_mermaid(self, lines: List[str], diagram_type: str) -> List[str]:
        """
        Clamp Mermaid output to avoid 'Maximum text size exceeded' and browser lockups.
        Keeps header + footer, truncates middle if too long.
        """
        if not lines:
            return lines

        has_open = lines[0].strip() == "```mermaid"
        has_close = lines[-1].strip() == "```"

        header = []
        footer = []
        body = lines[:]

        if has_open:
            header = lines[:2] if len(lines) >= 2 else lines[:1]
            body = lines[len(header):]
        if has_close and body:
            footer = [body[-1]]
            body = body[:-1]

        truncated = False
        if len(body) > self.MAX_PAYLOAD_LINES:
            body = body[: self.MAX_PAYLOAD_LINES]
            truncated = True

        out = header + body
        if truncated:
            out.append(f"%% NOTE: Diagram '{diagram_type}' truncated to {self.MAX_PAYLOAD_LINES} lines for rendering safety.")
        out += footer
        if has_close and (not out or out[-1].strip() != "```"):
            out.append("```")
        return out

    # ---------------------------
    # Public API
    # ---------------------------

    def generate_all_diagrams(self) -> Dict[str, str]:
        diagrams: Dict[str, str] = {}

        try:
            # ✅ FIX: call the wrapper that decides split vs single
            class_path = self.generate_class_diagram()
            diagrams["class_diagram"] = class_path

            # If split happened, include index too (if exists)
            idx_txt = os.path.join(self.output_dir, "class_diagrams_index.txt")
            if os.path.exists(idx_txt):
                diagrams["class_diagram_index"] = idx_txt

            diagrams["dependency_graph"] = self.generate_dependency_graph()
            diagrams["file_structure"] = self.generate_file_structure_diagram()
            diagrams["namespace_overview"] = self.generate_namespace_overview()
            diagrams["inheritance_hierarchy"] = self.generate_inheritance_hierarchy()
            diagrams["system_architecture"] = self.generate_system_architecture_graph()

            print(f"Generated {len(diagrams)} diagram outputs in: {self.output_dir}")
            return diagrams
        except Exception as e:
            print(f"Error generating diagrams: {e}")
            import traceback
            traceback.print_exc()
            return {}

    # ---------------------------
    # Core parsing helpers
    # ---------------------------

    def _strip_generics(self, s: str) -> str:
        """Remove generics safely (including nested) and leftover brackets."""
        if not s:
            return ""
        s = str(s).replace("&lt;", "<").replace("&gt;", ">")
        while True:
            new_s = re.sub(r"<[^<>]*>", "", s)
            if new_s == s:
                break
            s = new_s
        s = s.replace("<", "").replace(">", "")
        s = s.replace("‹", "").replace("›", "").replace("«", "").replace("»", "")
        return s.strip()

    def _normalize_text(self, x: Any) -> str:
        if x is None:
            return ""
        s = str(x)
        s = s.replace("\r", " ").replace("\n", " ").replace("\u0000", "")
        s = s.replace("`", "")
        s = s.replace("{", "").replace("}", "")
        s = self._strip_generics(s)
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def _to_member_name_only(self, raw: Any) -> str:
        """
        Mermaid-safe member formatter:
        - Prefer showing: Name : Type  (bool/int/string/etc)
        - If type can't be found, show only Name
        - Avoid junk like "static"
        """

        if raw is None:
            return ""

        # If analyzer gives structured member objects sometimes
        if isinstance(raw, dict):
            name = raw.get("name") or raw.get("Name") or raw.get("identifier") or ""
            typ = raw.get("type") or raw.get("Type") or raw.get("dataType") or ""
            name = self._normalize_text(name).strip()
            typ = self._normalize_text(typ).strip()
            if not name or name.lower() in ("static", "shared"):
                return ""
            return f"{name} : {self._normalize_type_name(typ)}" if typ else name

        s = self._normalize_text(raw).strip()
        if not s:
            return ""

        s = s.replace("global::", "").replace("::", ".").strip()

        # remove common modifiers (anywhere)
        s = re.sub(
            r"\b(public|private|protected|internal|friend|static|shared|readonly|const|dim|byval|byref)\b",
            "",
            s,
            flags=re.I
        ).strip()

        # if it became just "static"/"shared" -> skip
        if s.lower() in ("static", "shared"):
            return ""

        # VB style: "Name As Boolean"
        m = re.search(r"\b([A-Za-z_]\w*)\s+As\s+([A-Za-z_][\w\.<>]*)\b", s, flags=re.I)
        if m:
            name = m.group(1)
            typ = self._normalize_type_name(m.group(2))
            return f"{name} : {typ}" if typ else name

        # C#/UML style: "Name : Type"
        m = re.match(r"^([A-Za-z_]\w*)\s*:\s*([A-Za-z_][\w\.<>]*)", s)
        if m:
            name = m.group(1)
            typ = self._normalize_type_name(m.group(2))
            return f"{name} : {typ}" if typ else name

        # C# field style: "Type Name" (or "Type Name = ...")
        m = re.match(r"^([A-Za-z_][\w\.<>]*)\s+([A-Za-z_]\w*)\b", s)
        if m:
            typ = self._normalize_type_name(m.group(1))
            name = m.group(2)
            # only show type if it looks like a real type
            if typ:
                return f"{name} : {typ}"
            return name

        # C# property style: "bool IsOk { get; set; }"
        m = re.match(r"^([A-Za-z_][\w\.<>]*)\s+([A-Za-z_]\w*)\s*\{", s)
        if m:
            typ = self._normalize_type_name(m.group(1))
            name = m.group(2)
            return f"{name} : {typ}" if typ else name

        # fallback: just identifier
        m = re.search(r"([A-Za-z_]\w*)", s)
        return m.group(1) if m else ""

    def _normalize_type_name(self, t: str) -> str:
        if not t:
            return ""
        tt = self._strip_generics(str(t)).strip()

        # VB/.NET common -> shorter / consistent
        mapping = {
            "Boolean": "bool",
            "bool": "bool",
            "Int16": "short",
            "Int32": "int",
            "Int64": "long",
            "UInt16": "ushort",
            "UInt32": "uint",
            "UInt64": "ulong",
            "String": "string",
            "Char": "char",
            "Decimal": "decimal",
            "Double": "double",
            "Single": "float",
            "DateTime": "DateTime",
            "Object": "object",
        }

        # strip namespaces for System.*
        if "." in tt:
            # keep last segment (e.g., System.String -> String)
            last = tt.split(".")[-1]
            tt = last

        return mapping.get(tt, tt)
    def _to_method_signature(self, raw: Any) -> str:
        """
        Extract method name safely.
        Always returns MethodName()
        """
        s = self._normalize_text(raw)
        if not s:
            return ""

        s = s.replace("global::", "").replace("::", ".")

        # remove common modifiers
        s = re.sub(
            r"\b(public|private|protected|internal|friend|static|shared|virtual|override|abstract|sealed|async)\b",
            "",
            s,
            flags=re.I
        ).strip()

        # remove return type patterns
        s = re.split(r"\s+", s)

        for token in s:
            m = re.match(r"([A-Za-z_]\w*)\s*\(", token)
            if m:
                return f"{m.group(1)}()"

        # fallback: first identifier
        m = re.match(r"([A-Za-z_]\w*)", s[0]) if s else None
        if m:
            return f"{m.group(1)}()"

        return ""

    def _get_best_namespace(self, file_data: Dict[str, Any], cls: Dict[str, Any]) -> str:
        ns = cls.get("namespaceName")
        if isinstance(ns, str) and ns.strip():
            return ns.strip()

        for n in (file_data.get("namespaces") or []):
            if isinstance(n, str) and n.strip() and n != "Global":
                return n.strip()

        return "Global"

    def _type_id(self, ns: str, name: str) -> str:
        ns_s = self._sanitize_class_name(ns or "")
        nm_s = self._sanitize_class_name(name or "")
        if not ns_s or ns_s in ("Unknown", "Global"):
            return nm_s
        return f"{ns_s}__{nm_s}"

    def _extract_classes_flat(self) -> List[Dict[str, Any]]:
        classes: List[Dict[str, Any]] = []

        for file_data in self.analysis_data:
            if not isinstance(file_data, dict):
                continue

            for cls in (file_data.get("classes") or []):
                if not isinstance(cls, dict):
                    continue

                name = (cls.get("name") or "Unknown").strip()
                ns = self._get_best_namespace(file_data, cls)

                classes.append({
                    "name": name,
                    "ns": ns,
                    "methods": cls.get("Methods") or [],
                    "properties": cls.get("Properties") or [],
                    "fields": cls.get("Fields") or [],
                    "baseType": cls.get("baseType"),
                    "interfaces": cls.get("interfaces") or [],
                })

        seen = set()
        uniq: List[Dict[str, Any]] = []
        for c in classes:
            key = (c["ns"], c["name"])
            if key in seen:
                continue
            seen.add(key)
            uniq.append(c)

        return uniq

    # ---------------------------
    # Class diagram: split ONLY when big
    # ---------------------------

    def generate_class_diagram(self) -> str:
        """
        If small → write ONE file: class_diagram.md
        If big → write split parts and return first part path
        """
        classes = self._extract_classes_flat()

        # ✅ Only split if "big"
        if len(classes) <= self.SPLIT_THRESHOLD_CLASSES:
            out_path = os.path.join(self.output_dir, "class_diagram.md")

            # Optional: remove old split artifacts so you don't get confused
            self._cleanup_old_class_split_files(keep_single=True)

            self._write_class_diagram_file(
                fpath=out_path,
                diagram_title="Full Project",
                classes=classes,
                include_relationships=True
            )
            return out_path

        # big → split
        self._cleanup_old_class_split_files(keep_single=False)
        first_part = self.generate_class_diagrams_split()
        return first_part

    def _cleanup_old_class_split_files(self, keep_single: bool):
        """
        Avoid leftover files causing confusion.
        - keep_single=True: delete class_diagram__*.md + index.txt
        - keep_single=False: delete class_diagram.md (single)
        """
        try:
            for fn in os.listdir(self.output_dir):
                p = os.path.join(self.output_dir, fn)
                if not os.path.isfile(p):
                    continue

                if keep_single:
                    if fn.startswith("class_diagram__") and fn.endswith(".md"):
                        try:
                            os.remove(p)
                        except:
                            pass
                    if fn == "class_diagrams_index.txt":
                        try:
                            os.remove(p)
                        except:
                            pass
                else:
                    if fn == "class_diagram.md":
                        try:
                            os.remove(p)
                        except:
                            pass
        except:
            pass

    def generate_class_diagrams_split(self) -> str:
        """
        Generates multiple class diagrams:
        - grouped by namespace
        - each namespace paged if too large

        Writes:
        - class_diagram__<ns>.md or class_diagram__<ns>__p1.md, p2...
        - class_diagrams_index.txt (NOT markdown)

        Returns: first generated diagram path
        """
        classes = self._extract_classes_flat()

        by_ns: Dict[str, List[Dict[str, Any]]] = {}
        for c in classes:
            by_ns.setdefault(c.get("ns") or "Global", []).append(c)

        def clean_rel_name(x: str) -> str:
            x = self._strip_generics(x or "").strip()
            x = x.replace("global::", "").replace("::", ".")
            return x

        rel_degree: Dict[str, int] = {}
        for c in classes:
            cid = self._type_id(c.get("ns"), c.get("name"))
            rel_degree.setdefault(cid, 0)

            base = clean_rel_name(c.get("baseType") or "")
            if base and base.lower() != "null":
                rel_degree[cid] += 1

            for iface in (c.get("interfaces") or []):
                iface = clean_rel_name(iface)
                if iface:
                    rel_degree[cid] += 1

        generated_files: List[str] = []

        index_lines = [
            "Class Diagram Parts (text index)",
            "These are Mermaid files; open any .md part to render.",
            ""
        ]

        for ns in sorted(by_ns.keys(), key=lambda x: x.lower()):
            ns_classes = by_ns[ns]

            scored: List[Tuple[int, int, str, Dict[str, Any]]] = []
            for c in ns_classes:
                cid = self._type_id(c.get("ns"), c.get("name"))
                member_count = (
                    len(c.get("properties") or [])
                    + len(c.get("fields") or [])
                    + len(c.get("methods") or [])
                )
                degree = rel_degree.get(cid, 0)
                scored.append((degree, member_count, cid, c))
            scored.sort(key=lambda t: (-t[0], -t[1], t[2]))

            selected = [t[3] for t in scored[: self.KEY_CLASSES_PER_NAMESPACE]]

            if len(selected) <= self.MAX_CLASSES_PER_NAMESPACE_DIAGRAM:
                parts = [selected]
            else:
                parts = [
                    selected[i:i + self.MAX_CLASSES_PER_PAGE]
                    for i in range(0, len(selected), self.MAX_CLASSES_PER_PAGE)
                ]

            safe_ns = self._sanitize_node_name(ns)
            index_lines.append(f"[{ns}]")

            for pi, part_classes in enumerate(parts, start=1):
                if len(parts) == 1:
                    fname = f"class_diagram__{safe_ns}.md"
                    title = ns
                else:
                    fname = f"class_diagram__{safe_ns}__p{pi}.md"
                    title = f"{ns} (part {pi}/{len(parts)})"

                fpath = os.path.join(self.output_dir, fname)

                self._write_class_diagram_file(
                    fpath=fpath,
                    diagram_title=title,
                    classes=part_classes,
                    include_relationships=self.INCLUDE_RELATIONSHIPS
                )

                generated_files.append(fpath)
                index_lines.append(f" - {fname}")

            index_lines.append("")

        index_path = os.path.join(self.output_dir, "class_diagrams_index.txt")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(index_lines))

        return generated_files[0] if generated_files else index_path

    def _write_class_diagram_file(
        self,
        fpath: str,
        diagram_title: str,
        classes: List[Dict[str, Any]],
        include_relationships: bool = True
    ) -> None:
        """
        Write ONE Mermaid classDiagram file.

        IMPORTANT:
        - Do NOT write any Markdown header before ```mermaid
        - File must be "Mermaid-first"
        """
        mermaid_code: List[str] = ["```mermaid", "classDiagram"]

        def clean_rel_name(x: str) -> str:
            x = self._strip_generics(x or "").strip()
            x = x.replace("global::", "").replace("::", ".")
            return x

        for c in classes:
            cid = self._sanitize_class_name(self._type_id(c.get("ns"), c.get("name")))
            mermaid_code.append(f"    class {cid} {{")

            for prop in (c.get("properties") or [])[: self.MAX_PROPERTIES_PER_CLASS]:
                p = self._to_member_name_only(prop)
                if p:
                    mermaid_code.append(f"        +{p}")

            for field in (c.get("fields") or [])[: self.MAX_FIELDS_PER_CLASS]:
                ff = self._to_member_name_only(field)
                if ff:
                    mermaid_code.append(f"        +{ff}")

            for method in (c.get("methods") or [])[: self.MAX_METHODS_PER_CLASS]:
                sig = self._to_method_signature(method)
                if sig:
                    mermaid_code.append(f"        +{sig}")

            mermaid_code.append("    }")

        if include_relationships:
            for c in classes:
                child = self._sanitize_class_name(self._type_id(c.get("ns"), c.get("name")))

                base = clean_rel_name(c.get("baseType") or "")
                if base and base.lower() != "null":
                    base_id = self._sanitize_class_name(base)
                    mermaid_code.append(f"    {base_id} <|-- {child}")

                for iface in (c.get("interfaces") or []):
                    iface = clean_rel_name(iface)
                    if not iface:
                        continue
                    iface_id = self._sanitize_class_name(iface)
                    mermaid_code.append(f"    {iface_id} <|.. {child}")

        mermaid_code.append("```")
        mermaid_code = self._clamp_mermaid(mermaid_code, f"class_diagram: {diagram_title}")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(mermaid_code))
            f.write("\n")

    # ---------------------------
    # Dependency graph
    # ---------------------------

    def generate_dependency_graph(self) -> str:
        mermaid_code = ["```mermaid", "graph TB"]

        GROUP_DEPTH = 2
        MAX_EDGES_PER_FILE = 25
        MIN_GROUP_EDGE_WEIGHT = 3     # hide weak links (increase to 4/5 if still noisy)
        TOP_GROUP_EDGES = 120         # keep top strongest edges only

        EXTERNAL_PREFIXES = (
            "System", "Microsoft", "Newtonsoft", "nunit", "NUnit", "MSTest", "xunit", "Xunit",
            "Serilog", "log4net"
        )

        def is_external(imp: str) -> bool:
            return isinstance(imp, str) and any(imp.startswith(p) for p in EXTERNAL_PREFIXES)

        def norm_path(p: str) -> str:
            return (p or "").replace("\\", "/")

        def group_key(file_path: str) -> str:
            parts = [x for x in norm_path(file_path).split("/") if x]
            if not parts:
                return "Root"
            parts = parts[:-1]
            if not parts:
                return "Root"
            return "/".join(parts[:GROUP_DEPTH])

        # file -> group
        file_to_group: Dict[str, str] = {}
        token_to_group: Dict[str, str] = {}

        # build maps
        for fd in self.analysis_data:
            if not isinstance(fd, dict):
                continue
            file_path = fd.get("path", fd.get("file", "unknown"))
            g = group_key(file_path)
            file_node = self._sanitize_node_name(file_path)
            file_to_group[file_node] = g

            # namespace tokens -> group (not file!)
            for ns in (fd.get("namespaces") or []):
                if isinstance(ns, str) and ns and ns != "Global":
                    token_to_group.setdefault(ns, g)

            # folder dotted tokens -> group
            parts = [x for x in norm_path(file_path).split("/") if x][:-1]
            if parts:
                cum = []
                for part in parts[:6]:
                    cum.append(part)
                    token_to_group.setdefault(".".join(cum), g)

        def resolve_target_group(imp: str) -> Optional[str]:
            if not imp or not isinstance(imp, str) or is_external(imp):
                return None
            parts = imp.split(".")
            for k in range(len(parts), 0, -1):
                prefix = ".".join(parts[:k])
                if prefix in token_to_group:
                    return token_to_group[prefix]
            return None

        # external buckets (keep small)
        external_buckets = {
            "System": "System",
            "Microsoft": "Microsoft",
            "Newtonsoft": "Newtonsoft",
            "nunit": "Testing", "NUnit": "Testing", "MSTest": "Testing", "xunit": "Testing", "Xunit": "Testing",
            "Serilog": "Logging", "log4net": "Logging",
        }
        def ext_bucket(imp: str) -> str:
            for p, b in external_buckets.items():
                if imp.startswith(p):
                    return b
            return "Other"

        # count group edges (weighted)
        g_edges: Dict[tuple, int] = {}
        ext_edges: Dict[tuple, int] = {}

        for fd in self.analysis_data:
            if not isinstance(fd, dict):
                continue
            file_path = fd.get("path", fd.get("file", "unknown"))
            src_file = self._sanitize_node_name(file_path)
            gsrc = file_to_group.get(src_file, "Root")

            imports = fd.get("imports", []) or []
            seen = set()
            count = 0

            for imp in imports:
                if not imp or not isinstance(imp, str):
                    continue

                gtgt = resolve_target_group(imp)
                if gtgt and gtgt != gsrc:
                    if gtgt not in seen:
                        g_edges[(gsrc, gtgt)] = g_edges.get((gsrc, gtgt), 0) + 1
                        seen.add(gtgt)
                        count += 1
                elif is_external(imp):
                    b = ext_bucket(imp)
                    if b not in seen:
                        ext_edges[(gsrc, b)] = ext_edges.get((gsrc, b), 0) + 1
                        seen.add(b)
                        count += 1

                if count >= MAX_EDGES_PER_FILE:
                    break

        # prune weak group edges
        g_edges = {k: w for k, w in g_edges.items() if w >= MIN_GROUP_EDGE_WEIGHT}

        # keep only top strongest edges
        g_items = sorted(g_edges.items(), key=lambda kv: kv[1], reverse=True)[:TOP_GROUP_EDGES]
        g_edges = dict(g_items)

        # nodes
        groups = sorted(set([k[0] for k in g_edges.keys()] + [k[1] for k in g_edges.keys()] + [k[0] for k in ext_edges.keys()]))

        gid: Dict[str, str] = {g: self._sanitize_node_name(f"grp_{g}") for g in groups}
        eid: Dict[str, str] = {}
        for _, b in ext_edges.keys():
            eid.setdefault(b, self._sanitize_node_name(f"ext_{b}"))

        # render groups
        mermaid_code.append('    subgraph G["🔧 Folder Dependency"]')
        mermaid_code.append("        direction TB")
        for g in groups:
            mermaid_code.append(f'        {gid[g]}["📦 {self._escape_label(g)}"]:::group')
        mermaid_code.append("    end")

        # render externals
        if eid:
            mermaid_code.append('    subgraph X["🌐 External"]')
            mermaid_code.append("        direction TB")
            for b in sorted(eid.keys()):
                mermaid_code.append(f'        {eid[b]}["📦 {b}"]:::external')
            mermaid_code.append("    end")

        # edges with weights
        for (a, b), w in sorted(g_edges.items(), key=lambda kv: kv[1], reverse=True):
            mermaid_code.append(f"    {gid[a]} -->|x{w}| {gid[b]}")

        for (a, b), w in sorted(ext_edges.items(), key=lambda kv: kv[1], reverse=True)[:60]:
            mermaid_code.append(f"    {gid[a]} -.->|x{w}| {eid[b]}")

        # styles
        mermaid_code.extend([
            "    classDef group fill:#eef2ff,stroke:#4338ca,stroke-width:1px",
            "    classDef external fill:#fff3e0,stroke:#ef6c00,stroke-width:1px",
            "```"
        ])

        mermaid_code = self._clamp_mermaid(mermaid_code, "dependency_graph")

        output_file = os.path.join(self.output_dir, "dependency_graph.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(mermaid_code))

        return output_file

    # ---------------------------
    # File structure
    # ---------------------------

    def generate_file_structure_diagram(self) -> str:
        mermaid_code = ["```mermaid", "graph LR"]

        MAX_DEPTH = 5
        MAX_CHILDREN_PER_DIR = 8
        IGNORE_DIRS = {
            ".git", ".vs", ".vscode", "bin", "obj", "node_modules",
            "__pycache__", ".idea", ".pytest_cache", ".mypy_cache"
        }
        FILETYPE_ORDER = [".aspx", ".vb", ".cs", ".js", ".ts", ".sql", ".config", ".json", ".md", ".txt"]

        def norm_path(p: str) -> str:
            return (p or "").replace("\\", "/")

        def split_parts(p: str) -> List[str]:
            return [x for x in norm_path(p).split("/") if x]

        def clean_part(s: Any) -> str:
            if s is None:
                return ""
            s = str(s).replace("\u00A0", " ").replace("\r", "").replace("\n", "")
            s = s.strip()
            s = re.sub(r"\s+", " ", s)
            return s

        def is_ignored_dir(name: str) -> bool:
            return clean_part(name).lower() in IGNORE_DIRS

        def file_icon(name: str) -> str:
            n = (name or "").lower()
            if n.endswith(".aspx"):
                return "🟦"
            if n.endswith(".vb") or n.endswith(".cs"):
                return "🧩"
            if n.endswith(".js") or n.endswith(".ts"):
                return "🟨"
            if n.endswith(".sql"):
                return "🗄️"
            if n.endswith(".config") or n.endswith(".json"):
                return "⚙️"
            return "📄"

        def type_key(name: str) -> int:
            lower = (name or "").lower()
            for i, ext in enumerate(FILETYPE_ORDER):
                if lower.endswith(ext):
                    return i
            return len(FILETYPE_ORDER) + 1

        tree = {"_files": [], "_dirs": {}}

        for file_data in self.analysis_data:
            if not isinstance(file_data, dict):
                continue

            raw_path = file_data.get("path") or file_data.get("file") or ""
            if not raw_path:
                continue

            parts_raw = split_parts(raw_path)
            parts = [clean_part(p) for p in parts_raw]
            parts = [p for p in parts if p]
            if not parts:
                continue

            folder_parts = parts[:-1]
            if any(is_ignored_dir(d) for d in folder_parts):
                continue

            filename = clean_part(parts[-1])
            if not filename:
                continue

            cur = tree
            for d in folder_parts:
                d = clean_part(d)
                if not d:
                    continue
                cur = cur["_dirs"].setdefault(d, {"_files": [], "_dirs": {}})
            cur["_files"].append(filename)

        # def count_types(node: dict) -> Dict[str, int]:
        #     counts: Dict[str, int] = {}

        #     for f in node.get("_files", []) or []:
        #         ext = "." + f.split(".")[-1].lower() if "." in f else "(noext)"
        #         counts[ext] = counts.get(ext, 0) + 1

        #     for sub in (node.get("_dirs", {}) or {}).values():
        #         sub_counts = count_types(sub)
        #         for k, v in sub_counts.items():
        #             counts[k] = counts.get(k, 0) + v

        #     return counts

        # def fmt_counts(counts: Dict[str, int]) -> str:
        #     if not counts:
        #         return ""
        #     items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        #     top = items[:3]
        #     return " | ".join([f"{v}{k}" for k, v in top])

        def count_total_files(node: dict) -> int:
            total = len(node.get("_files", []) or [])
            for sub in (node.get("_dirs", {}) or {}).values():
                total += count_total_files(sub)
            return total

        used_nodes: set[str] = set()

        def add_node(node_id: str, label: str):
            if node_id in used_nodes:
                return
            used_nodes.add(node_id)
            mermaid_code.append(f'    {node_id}["{label}"]')

        def add_edge(a: str, b: str, dashed: bool = False):
            mermaid_code.append(f"    {a} {'-.->' if dashed else '-->'} {b}")

        def walk(dir_node: dict, dir_name: str, parent_id: str, depth: int):
            dir_name = clean_part(dir_name)

            total_files = count_total_files(dir_node)

            label = f"📁 {dir_name}"
            label += f" ({total_files})"

            dir_id = self._sanitize_node_name(f"{parent_id}__dir__{dir_name}")
            add_node(dir_id, label)
            add_edge(parent_id, dir_id)

            if depth >= MAX_DEPTH:
               
                if total_files > 0:
                    more_id = self._sanitize_node_name(f"{dir_id}__collapsed")
                    add_node(more_id, f"… (collapsed {total_files} files)")
                    mermaid_code.append(f"    class {more_id} summary_node")
                    add_edge(dir_id, more_id, dashed=True)
                return

            subdirs_items = list((dir_node.get("_dirs", {}) or {}).items())
            subdirs_items = [(clean_part(k), v) for k, v in subdirs_items if clean_part(k)]
            subdirs_items.sort(key=lambda kv: kv[0].lower())

            for sub_name, sub_node in subdirs_items:
                walk(sub_node, sub_name, dir_id, depth + 1)

            raw_files = dir_node.get("_files", []) or []
            cleaned_files = [clean_part(f) for f in raw_files if clean_part(f)]
            files = sorted(set(cleaned_files), key=lambda n: (type_key(n), n.lower()))

            shown = files[:MAX_CHILDREN_PER_DIR]
            hidden = max(0, len(files) - len(shown))

            for f in shown:
                fid = self._sanitize_node_name(f"{dir_id}__file__{f}")
                add_node(fid, f"{file_icon(f)} {f}")
                mermaid_code.append(f"    class {fid} file_node")
                add_edge(dir_id, fid)

            if hidden > 0:
                more_id = self._sanitize_node_name(f"{dir_id}__morefiles")
                add_node(more_id, f"… +{hidden} more files")
                mermaid_code.append(f"    class {more_id} summary_node")
                add_edge(dir_id, more_id, dashed=True)

        add_node("ROOT", "📦 Project")
        mermaid_code.append("    class ROOT root_node")

        top_items = list((tree.get("_dirs", {}) or {}).items())
        top_items = [(clean_part(k), v) for k, v in top_items if clean_part(k)]
        top_items.sort(key=lambda kv: kv[0].lower())

        for top_name, top_node in top_items:
            walk(top_node, top_name, "ROOT", 1)

        root_raw = tree.get("_files", []) or []
        root_clean = [clean_part(f) for f in root_raw if clean_part(f)]
        root_files = sorted(set(root_clean), key=lambda n: (type_key(n), n.lower()))

        shown_root = root_files[:MAX_CHILDREN_PER_DIR]
        hidden_root = max(0, len(root_files) - len(shown_root))

        for f in shown_root:
            fid = self._sanitize_node_name(f"ROOT__file__{f}")
            add_node(fid, f"{file_icon(f)} {f}")
            mermaid_code.append(f"    class {fid} file_node")
            add_edge("ROOT", fid)

        if hidden_root > 0:
            more_id = self._sanitize_node_name("ROOT__morefiles")
            add_node(more_id, f"… +{hidden_root} more files")
            mermaid_code.append(f"    class {more_id} summary_node")
            add_edge("ROOT", more_id, dashed=True)

        mermaid_code.extend([
            "    classDef root_node fill:#e3f2fd,stroke:#1565c0,stroke-width:1px",
            "    classDef file_node fill:#ffffff,stroke:#999999,stroke-width:1px",
            "    classDef summary_node fill:#eeeeee,stroke:#777777,stroke-dasharray: 3 3,color:#444",
        ])

        mermaid_code.append("```")

        output_file = os.path.join(self.output_dir, "file_structure.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(self._clamp_mermaid(mermaid_code, "file_structure")))

        return output_file

    # ---------------------------
    # Namespace overview
    # ---------------------------

    def generate_namespace_overview(self) -> str:
        mermaid_code = [
            "```mermaid",
            "%%{init: {\"flowchart\": {\"htmlLabels\": false}} }%%",
            "graph LR"
        ]

        MAX_CLASSES_PER_NS = 18
        namespaces: Dict[str, Dict[str, List[str]]] = {}

        for file_data in self.analysis_data:
            if not isinstance(file_data, dict):
                continue

            file_namespaces = file_data.get("namespaces", []) or ["Global"]

            for ns in file_namespaces:
                ns = ns if isinstance(ns, str) else "Global"
                namespaces.setdefault(ns, {"classes": [], "files": []})

                namespaces[ns]["files"].append(file_data.get("file", "unknown"))

                for cls in file_data.get("classes", []) or []:
                    if isinstance(cls, dict):
                        namespaces[ns]["classes"].append(cls.get("name", "Unknown"))

        for ns in namespaces:
            namespaces[ns]["classes"] = sorted(set([c for c in namespaces[ns]["classes"] if isinstance(c, str)]))

        for ns_name in sorted(namespaces.keys()):
            ns_content = namespaces[ns_name]
            safe_ns = self._sanitize_node_name(ns_name)

            mermaid_code.append(f"    subgraph {safe_ns}[\"📦 {ns_name}\"]")
            mermaid_code.append("        direction TB")

            classes = ns_content["classes"]
            shown = classes[:MAX_CLASSES_PER_NS]
            hidden_count = max(0, len(classes) - len(shown))

            for class_name in shown:
                safe_class = self._sanitize_node_name(f"{ns_name}_{class_name}")
                mermaid_code.append(f"        {safe_class}[\"🔷 {class_name}\"]")

            if hidden_count > 0:
                more_node = self._sanitize_node_name(f"{ns_name}__more")
                mermaid_code.append(f"        {more_node}[\"… +{hidden_count} more\"]")
                mermaid_code.append(f"        class {more_node} more_node")

            mermaid_code.append("    end")

        mermaid_code.extend([
            "    classDef more_node fill:#eeeeee,stroke:#999999,stroke-dasharray: 3 3,color:#444"
        ])

        mermaid_code.append("```")

        output_file = os.path.join(self.output_dir, "namespace_overview.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(self._clamp_mermaid(mermaid_code, "namespace_overview")))

        return output_file

    # ---------------------------
    # Inheritance hierarchy
    # ---------------------------

    def generate_inheritance_hierarchy(self) -> str:
        mermaid_code = [
            "```mermaid",
            "%%{init: {\"flowchart\": {\"htmlLabels\": false}} }%%",
            "classDiagram"
        ]

        HIDE_SYSTEM_BASES = True
        MAX_NODES = 220

        class_nodes: Dict[str, Dict[str, str]] = {}
        interface_nodes: Dict[str, Dict[str, str]] = {}
        inherits_edges: set[Tuple[str, str]] = set()
        implements_edges: set[Tuple[str, str]] = set()

        def clean_name(x: Any) -> str:
            return (x or "").strip() if isinstance(x, str) else ""

        def is_system(x: str) -> bool:
            return x.startswith("System.") or x.startswith("Microsoft.")

        def file_ns(file_data: dict) -> str:
            nss = (file_data.get("namespaces") or [])
            for n in nss:
                if isinstance(n, str) and n and n != "Global":
                    return n
            return "Global"

        for fd in self.analysis_data:
            if not isinstance(fd, dict):
                continue

            ns = file_ns(fd)

            for cls in (fd.get("classes") or []):
                if not isinstance(cls, dict):
                    continue
                name = clean_name(cls.get("name", ""))
                if not name:
                    continue

                class_nodes[name] = {"ns": ns}

                base = clean_name(cls.get("baseType") or "")
                if base and base != "null":
                    if not (HIDE_SYSTEM_BASES and is_system(base)):
                        inherits_edges.add((base, name))

                for iface in (cls.get("interfaces") or []):
                    iface = clean_name(iface)
                    if not iface:
                        continue
                    interface_nodes.setdefault(iface, {"ns": ns})
                    implements_edges.add((iface, name))

        involved = set()
        for p, c in inherits_edges:
            involved.add(p)
            involved.add(c)
        for i, c in implements_edges:
            involved.add(i)
            involved.add(c)

        if len(involved) > MAX_NODES:
            degree = {n: 0 for n in involved}
            for p, c in inherits_edges:
                if p in degree:
                    degree[p] += 1
                if c in degree:
                    degree[c] += 1
            for i, c in implements_edges:
                if i in degree:
                    degree[i] += 1
                if c in degree:
                    degree[c] += 1

            keep = set(sorted(degree.keys(), key=lambda k: -degree[k])[:MAX_NODES])
            inherits_edges = {(p, c) for (p, c) in inherits_edges if p in keep and c in keep}
            implements_edges = {(i, c) for (i, c) in implements_edges if i in keep and c in keep}
            involved = keep

        for iface in sorted(interface_nodes.keys()):
            if iface not in involved:
                continue
            mermaid_code.append(f"    class {self._sanitize_class_name(iface)} {{")
            mermaid_code.append("    }")
            mermaid_code.append(f"    <<interface>> {self._sanitize_class_name(iface)}")

        for cls in sorted(class_nodes.keys()):
            if cls not in involved:
                continue
            mermaid_code.append(f"    class {self._sanitize_class_name(cls)}")

        for parent, child in sorted(inherits_edges):
            mermaid_code.append(f"    {self._sanitize_class_name(parent)} <|-- {self._sanitize_class_name(child)}")

        for iface, cls in sorted(implements_edges):
            mermaid_code.append(f"    {self._sanitize_class_name(iface)} <|.. {self._sanitize_class_name(cls)}")

        mermaid_code.append("```")

        output_file = os.path.join(self.output_dir, "inheritance_hierarchy.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(self._clamp_mermaid(mermaid_code, "inheritance_hierarchy")))

        return output_file

    # ---------------------------
    # System architecture graph
    # ---------------------------

    def generate_system_architecture_graph(self) -> str:
        mermaid_code = [
            "```mermaid",
            "%%{init: {\"flowchart\": {\"htmlLabels\": false}} }%%",
            "graph TB"
        ]

        # ---------------------------
        # knobs
        # ---------------------------
        TOP_EDGES_PER_LAYER = 5
        TOP_FILES_PER_LAYER = 6
        SHOW_FILES_IN_LAYER = False
        GROUP_EXTERNAL_BUCKETS = True

        EXTERNAL_PREFIXES = (
            "System", "Microsoft", "Newtonsoft", "Serilog", "log4net",
            "nunit", "NUnit", "MSTest", "xunit", "Xunit"
        )

        external_buckets = {
            "System": "System",
            "Microsoft": "Microsoft",
            "Newtonsoft": "Newtonsoft",
            "Serilog": "Logging",
            "log4net": "Logging",
            "nunit": "Testing", "NUnit": "Testing", "MSTest": "Testing",
            "xunit": "Testing", "Xunit": "Testing",
        }

        def norm_path(p: str) -> str:
            return (p or "").replace("\\", "/")

        def fname(fd: dict) -> str:
            return (fd.get("file") or norm_path(fd.get("path", "")).split("/")[-1] or "unknown").strip()

        def fpath(fd: dict) -> str:
            return norm_path(fd.get("path") or fd.get("file") or "").strip()

        def is_external_import(imp: str) -> bool:
            return isinstance(imp, str) and imp.startswith(EXTERNAL_PREFIXES)

        def ext_bucket(imp: str) -> str:
            if not GROUP_EXTERNAL_BUCKETS:
                return "External"
            for p, b in external_buckets.items():
                if imp.startswith(p):
                    return b
            return "Other"

        # ---------------------------
        # Better layer classifier
        # ---------------------------
        def classify_layer(fd: dict) -> str:
            n = fname(fd).lower()
            p = fpath(fd).lower()

            # Database / SQL
            if n.endswith(".sql") or any(x in p for x in ["/sql", "/storedproc", "/storedprocedures", "/db/scripts", "/database", "/migrations"]):
                return "Database"

            # Web UI (WebForms / Views / Pages / Static)
            if any(n.endswith(ext) for ext in [".aspx", ".ascx", ".master", ".cshtml", ".razor", ".html"]):
                return "UI"
            if any(x in p for x in ["/views", "/pages", "/webforms", "/ui", "/wwwroot", "/static"]):
                return "UI"

            # API / Controllers / Endpoints / Handlers
            if any(x in n for x in ["controller", "endpoint", "handler", "route", "api"]):
                return "API"
            if any(x in p for x in ["/controllers", "/endpoints", "/handlers", "/api"]):
                return "API"

            # Background jobs / schedulers / workers
            if any(x in n for x in ["job", "worker", "scheduler", "cron", "queue", "consumer"]):
                return "Jobs"
            if any(x in p for x in ["/jobs", "/workers", "/scheduler", "/cron", "/queue"]):
                return "Jobs"

            # Data access / repositories / DAL
            if any(x in n for x in ["repository", "repo", "dao", "dal", "dbaccess", "datasource"]):
                return "DataAccess"
            if any(x in p for x in ["/dal", "/dao", "/repository", "/repositories", "/dataaccess", "/data/db", "/dbaccess"]):
                return "DataAccess"

            # Domain / Models / Entities
            if any(x in n for x in ["model", "entity", "dto", "vo", "pojo"]):
                return "Domain"
            if any(x in p for x in ["/models", "/entities", "/domain", "/dto", "/contracts"]):
                return "Domain"

            # Utilities / shared helpers
            if any(x in n for x in ["util", "helper", "common", "constants", "extensions"]):
                return "Shared"
            if any(x in p for x in ["/util", "/utils", "/helper", "/helpers", "/common", "/shared"]):
                return "Shared"

            # Services / business logic
            if any(x in n for x in ["service", "manager", "processor", "workflow", "engine"]):
                return "Service"
            if any(x in p for x in ["/services", "/business", "/logic", "/managers", "/workflows"]):
                return "Service"

            return "Other"

        # ---------------------------
        # Build namespace->layer map (for resolving imports to layers)
        # ---------------------------
        token_to_layer: Dict[str, str] = {}
        layer_files: Dict[str, List[str]] = {}
        layer_file_count: Dict[str, int] = {}

        for fd in self.analysis_data:
            if not isinstance(fd, dict):
                continue
            layer = classify_layer(fd)
            layer_file_count[layer] = layer_file_count.get(layer, 0) + 1
            layer_files.setdefault(layer, []).append(fname(fd))

            for ns in (fd.get("namespaces", []) or []):
                if isinstance(ns, str) and ns and ns != "Global":
                    token_to_layer.setdefault(ns, layer)

            # also map folder-like dotted prefixes
            parts = [x for x in norm_path(fpath(fd)).split("/") if x][:-1]
            if parts:
                cum = []
                for part in parts[:6]:
                    cum.append(part)
                    token_to_layer.setdefault(".".join(cum), layer)

        def resolve_import_layer(imp: str) -> str:
            if not imp or not isinstance(imp, str):
                return "Unknown"
            if is_external_import(imp):
                return "External:" + ext_bucket(imp)

            parts = imp.split(".")
            for k in range(len(parts), 0, -1):
                prefix = ".".join(parts[:k])
                if prefix in token_to_layer:
                    return token_to_layer[prefix]
            return "Unknown"

        # ---------------------------
        # Count edges between layers
        # ---------------------------
        edge_counts: Dict[Tuple[str, str], int] = {}
        ext_counts: Dict[Tuple[str, str], int] = {}

        for fd in self.analysis_data:
            if not isinstance(fd, dict):
                continue
            src_layer = classify_layer(fd)
            imports = fd.get("imports") or fd.get("usings") or []

            seen = set()
            for imp in imports:
                if not imp or not isinstance(imp, str):
                    continue
                tgt_layer = resolve_import_layer(imp)

                if tgt_layer.startswith("External:"):
                    bucket = tgt_layer.split(":", 1)[1]
                    key = (src_layer, bucket)
                    if key not in seen:
                        ext_counts[key] = ext_counts.get(key, 0) + 1
                        seen.add(key)
                    continue

                if tgt_layer in ("Unknown", src_layer):
                    continue

                key = (src_layer, tgt_layer)
                if key not in seen:
                    edge_counts[key] = edge_counts.get(key, 0) + 1
                    seen.add(key)

        # ---------------------------
        # Render nodes (with counts + top files)
        # ---------------------------
        layers_order = ["UI", "API", "Jobs", "Service", "Domain", "Shared", "DataAccess", "Database", "Other"]
        present_layers = [l for l in layers_order if layer_file_count.get(l, 0) > 0]

        def layer_node_id(layer: str) -> str:
            return self._sanitize_node_name(f"layer_{layer}")

        def short_list(items: List[str], n: int) -> List[str]:
            # show stable + readable examples
            items2 = sorted(set([x for x in items if isinstance(x, str) and x.strip()]), key=lambda s: s.lower())
            return items2[:n]

        mermaid_code.append('    subgraph ARCH["🔧 System Architecture"]')
        mermaid_code.append("        direction TB")

        LAYER_DESC = {
            "UI": "Web pages|Views",
            "API": "Controllers|Endpoints",
            "Jobs": "Schedulers|Background Workers",
            "Service": "Business logic",
            "Domain": "Models|DTOs|Entities",
            "Shared": "Utilities|Common",
            "DataAccess": "Repos|DAL|DAO",
            "Database": "SQL|SPs",
            "Other": "Unclassified",
        }

        for layer in present_layers:
            count = layer_file_count.get(layer, 0)
            desc = LAYER_DESC.get(layer, "")
            # no file names, just meaning
            label = f"{layer} ({count})"
            if desc:
                label += f"\n{desc}"

            mermaid_code.append(
                f'        {layer_node_id(layer)}["{self._escape_label(label)}"]:::layer')

        mermaid_code.append("    end")

        # external nodes
        if ext_counts:
            mermaid_code.append('    subgraph EXT["🌐 External"]')
            mermaid_code.append("        direction TB")
            ext_nodes = sorted(set([b for (_, b) in ext_counts.keys()]))
            for b in ext_nodes:
                mermaid_code.append(f'        {self._sanitize_node_name("ext_"+b)}["{b}"]:::external')
            mermaid_code.append("    end")

        # ---------------------------
        # Render edges (top per source)
        # ---------------------------
        # violations (these are usually “architecture smells”)
        def edge_warning(src: str, tgt: str) -> str:
            # tune these rules as you like
            if src == "UI" and tgt in ("Database", "DataAccess"):
                return " ⚠"
            if src == "API" and tgt == "Database":
                return " ⚠"
            if src == "Domain" and tgt in ("DataAccess", "Database"):
                return " ⚠"
            return ""

        # internal edges: keep top per source layer
        for src in present_layers:
            outgoing = [((s, t), c) for (s, t), c in edge_counts.items() if s == src]
            outgoing.sort(key=lambda x: -x[1])
            for (s, t), c in outgoing[:TOP_EDGES_PER_LAYER]:
                if t not in present_layers:
                    continue
                warn = edge_warning(s, t)
                mermaid_code.append(
                    f"    {layer_node_id(s)} -->|x{c}{warn}| {layer_node_id(t)}"
                )

        # external edges (limit)
        ext_items = sorted(ext_counts.items(), key=lambda kv: kv[1], reverse=True)[:40]
        for (src, bucket), c in ext_items:
            if src not in present_layers:
                continue
            mermaid_code.append(
                f"    {layer_node_id(src)} -.->|x{c}| {self._sanitize_node_name('ext_'+bucket)}"
            )

        # ---------------------------
        # Styles
        # ---------------------------
        mermaid_code.extend([
            "    classDef layer fill:#e3f2fd,stroke:#1565c0,stroke-width:1px",
            "    classDef external fill:#fff3e0,stroke:#ef6c00,stroke-width:1px",
            "```"
        ])

        mermaid_code = self._clamp_mermaid(mermaid_code, "system_architecture")

        output_file = os.path.join(self.output_dir, "system_architecture.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(mermaid_code))

        return output_file


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))

    analyzer_temp_dir = os.environ.get("ANALYZER_TEMP_DIR")

    if analyzer_temp_dir:
        analysis_file = os.path.join(analyzer_temp_dir, "static_analysis_output", "all_analysis_results.json")
    else:
        analysis_file = os.path.join(backend_dir, "static_analysis_output", "all_analysis_results.json")

    if not os.path.exists(analysis_file):
        print(f"Static analysis file not found: {analysis_file}")
        return {}

    try:
        with open(analysis_file, "r", encoding="utf-8") as f:
            analysis_data = json.load(f)

        print(f"Loaded analysis data for {len(analysis_data)} files")

        generator = DiagramGenerator(analysis_data)
        diagrams = generator.generate_all_diagrams()

        print("\n=== Generated Diagram Outputs ===")
        for diagram_type, file_path in diagrams.items():
            print(f"✅ {diagram_type}: {file_path}")

        return diagrams

    except Exception as e:
        print(f"Error processing analysis data: {e}")
        import traceback
        traceback.print_exc()
        return {}


if __name__ == "__main__":
    main()
import os
import json
from pathlib import Path
from typing import Dict, List, Any, Set
import re

class DiagramGenerator:
    """Generate various diagrams from static analysis output."""
    
    def __init__(self, analysis_data: List[Dict], output_dir: str = None):
        # Ensure analysis_data is a list of dicts, not strings
        self.analysis_data = []
        if analysis_data:
            for item in analysis_data:
                parsed_item = item
                if isinstance(item, str):
                    try:
                        parsed_item = json.loads(item)
                    except:
                        continue # Skip invalid JSON strings
                
                if isinstance(parsed_item, dict):
                    # sanitize nested 'classes' if they are strings
                    if 'classes' in parsed_item and isinstance(parsed_item['classes'], list):
                        sanitized_classes = []
                        for cls in parsed_item['classes']:
                            if isinstance(cls, str):
                                try:
                                    sanitized_classes.append(json.loads(cls))
                                except:
                                    pass
                            elif isinstance(cls, dict):
                                sanitized_classes.append(cls)
                        parsed_item['classes'] = sanitized_classes
                    
                    self.analysis_data.append(parsed_item)
                    
        self.output_dir = output_dir or os.path.join(
            os.path.dirname(__file__), "..", "..", "analysis_output", "Diagrams"
        )
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_all_diagrams(self) -> Dict[str, str]:
        """Generate all available diagrams and return file paths."""
        diagrams = {}
        
        try:
            diagrams['class_diagram'] = self.generate_class_diagram()
            diagrams['dependency_graph'] = self.generate_dependency_graph()
            diagrams['file_structure'] = self.generate_file_structure_diagram()
            diagrams['namespace_overview'] = self.generate_namespace_overview()
            diagrams['inheritance_hierarchy'] = self.generate_inheritance_hierarchy()
            # diagrams['method_call_flow'] = self.generate_method_call_flow()
            
            print(f"Generated {len(diagrams)} diagrams in: {self.output_dir}")
            return diagrams
        except Exception as e:
            print(f"Error generating diagrams: {e}")
            import traceback
            traceback.print_exc()
            return {}
    
    def generate_class_diagram(self) -> str:
        """Generate a Mermaid class diagram showing all classes and their relationships."""
        mermaid_code = ["```mermaid", "classDiagram"]
        
        # Extract all classes
        classes = []
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            if 'classes' in file_data:
                for cls in file_data['classes']:
                    # Double check it is a dict (handled in __init__ but safe to check)
                    if not isinstance(cls, dict): continue
                    
                    classes.append({
                        'name': cls.get('name', 'Unknown'),
                        'file': file_data.get('file', 'unknown'),
                        'methods': cls.get('Methods', []),
                        'properties': cls.get('Properties', []),
                        'baseType': cls.get('baseType'),
                        'interfaces': cls.get('interfaces', []),
                        'modifiers': cls.get('modifiers', '')
                    })
        
        # Add class definitions
        for cls in classes:
            safe_name = self._sanitize_class_name(cls['name'])
            mermaid_code.append(f"    class {safe_name} {{")
            
            # Add properties
            for prop in cls.get('properties', []):
                mermaid_code.append(f"        +{prop}")
            
            # Add methods
            for method in cls.get('methods', []):
                method_name = method.split('(')[0] if '(' in method else method
                mermaid_code.append(f"        +{method_name}()")
            
            mermaid_code.append("    }")
            
            # Add inheritance relationships
            if cls.get('baseType') and cls['baseType'] != 'null':
                base_safe = self._sanitize_class_name(cls['baseType'])
                mermaid_code.append(f"    {base_safe} <|-- {safe_name}")
            
            # Add interface implementations
            for interface in cls.get('interfaces', []):
                if_safe = self._sanitize_class_name(interface)
                mermaid_code.append(f"    {if_safe} <|.. {safe_name}")
        
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "class_diagram.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def generate_dependency_graph(self) -> str:
        """Generate a dependency graph showing imports and file relationships."""
        mermaid_code = ["```mermaid", "graph TD"]
        
        # Track all files and their dependencies
        file_deps = {}
        
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            filename = file_data.get('file', 'unknown')
            safe_filename = self._sanitize_node_name(filename)
            
            # Add imports as dependencies
            imports = file_data.get('imports', [])
            if imports:
                file_deps[safe_filename] = []
                for imp in imports:
                    # Simplify system imports
                    if imp.startswith('System'):
                        imp_parts = imp.split('.')
                        imp_display = '.'.join(imp_parts[:2]) if len(imp_parts) > 1 else imp
                    else:
                        imp_display = imp
                    
                    safe_import = self._sanitize_node_name(imp_display)
                    file_deps[safe_filename].append(safe_import)
                    mermaid_code.append(f"    {safe_import} --> {safe_filename}")
        
        # Add file type styling
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            filename = file_data.get('file', 'unknown')
            safe_filename = self._sanitize_node_name(filename)
            
            if filename.endswith('.aspx'):
                mermaid_code.append(f"    {safe_filename}[\"📄 {filename}\"]")
                mermaid_code.append(f"    class {safe_filename} aspx_file")
            elif filename.endswith('.vb'):
                mermaid_code.append(f"    {safe_filename}[\"📝 {filename}\"]")
                mermaid_code.append(f"    class {safe_filename} vb_file")
            elif filename.endswith('.js'):
                mermaid_code.append(f"    {safe_filename}[\"📜 {filename}\"]")
                mermaid_code.append(f"    class {safe_filename} js_file")
        
        # Add styling
        mermaid_code.extend([
            "    classDef aspx_file fill:#e1f5fe",
            "    classDef vb_file fill:#f3e5f5", 
            "    classDef js_file fill:#fff3e0"
        ])
        
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "dependency_graph.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def generate_file_structure_diagram(self) -> str:
        """Generate a file structure/organization diagram."""
        mermaid_code = ["```mermaid", "graph TD"]
        
        # Group files by directory structure
        file_structure = {}
        
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            file_path = file_data.get('path', file_data.get('file', 'unknown'))
            path_parts = file_path.split('\\') if '\\' in file_path else file_path.split('/')
            
            current = file_structure
            for part in path_parts[:-1]:  # directories
                if part not in current:
                    current[part] = {}
                current = current[part]
            
            # Add the file
            filename = path_parts[-1]
            current[filename] = file_data
        
        # Generate mermaid from structure
        def add_structure_nodes(structure, parent_id="root", level=0):
            for name, content in structure.items():
                safe_name = self._sanitize_node_name(f"{parent_id}_{name}")
                
                if isinstance(content, dict) and not content.get('file'):
                    # Directory
                    mermaid_code.append(f"    {safe_name}[\"📁 {name}\"]")
                    if parent_id != "root":
                        mermaid_code.append(f"    {parent_id} --> {safe_name}")
                    add_structure_nodes(content, safe_name, level + 1)
                else:
                    # File
                    file_icon = "📄" if name.endswith('.aspx') else "📝" if name.endswith('.vb') else "📜"
                    mermaid_code.append(f"    {safe_name}[\"🔸 {name}\"]")
                    if parent_id != "root":
                        mermaid_code.append(f"    {parent_id} --> {safe_name}")
        
        add_structure_nodes(file_structure)
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "file_structure.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def generate_namespace_overview(self) -> str:
        """Generate namespace organization diagram."""
        mermaid_code = ["```mermaid", "graph LR"]
        
        # Collect namespaces and their contents
        namespaces = {}
        
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            file_namespaces = file_data.get('namespaces', [])
            if not file_namespaces:
                file_namespaces = ['Global']  # Default namespace
            
            for ns in file_namespaces:
                if ns not in namespaces:
                    namespaces[ns] = {'classes': [], 'files': []}
                
                namespaces[ns]['files'].append(file_data.get('file', 'unknown'))
                
                if 'classes' in file_data:
                    for cls in file_data['classes']:
                        if isinstance(cls, dict):
                            namespaces[ns]['classes'].append(cls.get('name', 'Unknown'))
        
        # Generate diagram
        for ns_name, ns_content in namespaces.items():
            safe_ns = self._sanitize_node_name(ns_name)
            mermaid_code.append(f"    {safe_ns}[\"📦 {ns_name}\"]")
            
            for class_name in ns_content['classes']:
                safe_class = self._sanitize_node_name(f"{ns_name}_{class_name}")
                mermaid_code.append(f"    {safe_class}[\"🔷 {class_name}\"]")
                mermaid_code.append(f"    {safe_ns} --> {safe_class}")
        
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "namespace_overview.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def generate_inheritance_hierarchy(self) -> str:
        """Generate inheritance hierarchy diagram."""
        mermaid_code = ["```mermaid", "graph TD"]
        
        # Track inheritance relationships
        inheritance = {}
        all_classes = set()
        
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            if 'classes' in file_data:
                for cls in file_data['classes']:
                    if isinstance(cls, dict):
                        class_name = cls.get('name', 'Unknown')
                        all_classes.add(class_name)
                        
                        base_type = cls.get('baseType')
                        if base_type and base_type != 'null':
                            inheritance[class_name] = base_type
                            all_classes.add(base_type)
        
        # Add nodes and relationships
        for class_name in all_classes:
            safe_name = self._sanitize_class_name(class_name)
            
            # Determine if it's a system class or custom class
            if class_name.startswith('System.'):
                mermaid_code.append(f"    {safe_name}[\"🔶 {class_name}\"]")
                mermaid_code.append(f"    class {safe_name} system_class")
            else:
                mermaid_code.append(f"    {safe_name}[\"📋 {class_name}\"]")
                mermaid_code.append(f"    class {safe_name} custom_class")
        
        # Add inheritance arrows
        for child, parent in inheritance.items():
            safe_child = self._sanitize_class_name(child)
            safe_parent = self._sanitize_class_name(parent)
            mermaid_code.append(f"    {safe_parent} --> {safe_child}")
        
        # Add styling
        mermaid_code.extend([
            "    classDef system_class fill:#ffecb3",
            "    classDef custom_class fill:#c8e6c9"
        ])
        
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "inheritance_hierarchy.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def generate_method_call_flow(self) -> str:
        """Generate method call flow diagram."""
        mermaid_code = ["```mermaid", "sequenceDiagram"]
        
        # Extract methods and their relationships
        classes_with_methods = {}
        
        for file_data in self.analysis_data:
            if not isinstance(file_data, dict): continue
            
            if 'classes' in file_data:
                for cls in file_data['classes']:
                    if isinstance(cls, dict):
                        class_name = cls.get('name', 'Unknown')
                        methods = cls.get('Methods', [])
                        if methods:
                            classes_with_methods[class_name] = methods
        
        # Generate sequence diagram for first few classes as example
        class_names = list(classes_with_methods.keys())[:3]  # Limit to first 3 for readability
        
        for i, class_name in enumerate(class_names):
            safe_class = self._sanitize_class_name(class_name)
            mermaid_code.append(f"    participant {safe_class}")
        
        # Add method calls (simplified example flow)
        if len(class_names) >= 2:
            for i in range(len(class_names) - 1):
                from_class = self._sanitize_class_name(class_names[i])
                to_class = self._sanitize_class_name(class_names[i + 1])
                
                methods = classes_with_methods[class_names[i + 1]]
                if methods:
                    method_name = methods[0]  # Use first method as example
                    mermaid_code.append(f"    {from_class}->>+{to_class}: {method_name}()")
                    mermaid_code.append(f"    {to_class}-->>-{from_class}: result")
        
        mermaid_code.append("```")
        
        output_file = os.path.join(self.output_dir, "method_call_flow.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(mermaid_code))
        
        return output_file
    
    def _sanitize_class_name(self, name: str) -> str:
        """Sanitize class name for Mermaid compatibility."""
        if not name or name == 'null':
            return 'Unknown'
        # Replace dots and special characters
        return re.sub(r'[^\w]', '_', name)
    
    def _sanitize_node_name(self, name: str) -> str:
        """Sanitize node name for Mermaid compatibility."""
        if not name:
            return 'Unknown'
        # Replace special characters but keep more readable format
        return re.sub(r'[^\w\-\.]', '_', name).replace('.', '_')

def main():
    """Main function to generate diagrams from static analysis output."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(script_dir, "..", "..", "..")
    
    # Load static analysis data
    analysis_file = os.path.join(backend_dir, "static_analysis_output", "all_analysis_results.json")
    
    if not os.path.exists(analysis_file):
        print(f"Static analysis file not found: {analysis_file}")
        return
    
    try:
        with open(analysis_file, 'r', encoding='utf-8') as f:
            analysis_data = json.load(f)
        
        print(f"Loaded analysis data for {len(analysis_data)} files")
        
        # Generate diagrams
        generator = DiagramGenerator(analysis_data)
        diagrams = generator.generate_all_diagrams()
        
        # Print summary
        print("\n=== Generated Diagrams ===")
        for diagram_type, file_path in diagrams.items():
            print(f"✅ {diagram_type}: {file_path}")
        
        return diagrams
        
    except Exception as e:
        print(f"Error processing analysis data: {e}")
        return {}

if __name__ == "__main__":
    main()
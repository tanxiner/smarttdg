import graphviz

def generate_dependency_diagram(architecture_info, output_file="dependency_diagram"):
    dot = graphviz.Digraph(comment='Dependency Diagram', format='png')

    # Add nodes for each module
    for module in architecture_info["modules"]:
        dot.node(module, module)

    # Add edges for dependencies
    for module, dependencies in architecture_info["dependencies"].items():
        for dependency in dependencies:
            dot.edge(module, dependency)

    # Save the diagram
    dot.render(output_file)
    print(f"Dependency diagram generated: {output_file}")

# Example usage
# generate_dependency_diagram(architecture_info)

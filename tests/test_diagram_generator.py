from diagram_generator import DiagramGenerator


def make_gen():
    return DiagramGenerator([])


def test_sanitize_class_name_handles_null_special_chars_and_leading_digit():
    gen = make_gen()
    assert gen._sanitize_class_name("null") == "Unknown"
    assert gen._sanitize_class_name("123-My<Class>") == "C_123_My_Class_"


def test_sanitize_node_name_prefixes_leading_digit():
    gen = make_gen()
    assert gen._sanitize_node_name("123.node-name") == "N_123_node-name"


def test_strip_generics_removes_nested_generics():
    gen = make_gen()
    assert gen._strip_generics("List<Dictionary<string, int>>") == "List"


def test_normalize_text_removes_noise():
    gen = make_gen()
    assert gen._normalize_text("Hello\r\nWorld `{x}`") == "Hello World x"


def test_to_member_name_only_supports_dict_input():
    gen = make_gen()
    result = gen._to_member_name_only({"name": "IsActive", "type": "Boolean"})
    assert result == "IsActive : bool"


def test_to_member_name_only_supports_vb_style():
    gen = make_gen()
    assert gen._to_member_name_only("UserName As String") == "UserName : string"


def test_to_member_name_only_supports_csharp_field_style():
    gen = make_gen()
    assert gen._to_member_name_only("Int32 Count") == "Count : int"


def test_normalize_type_name_maps_dotnet_names():
    gen = make_gen()
    assert gen._normalize_type_name("System.String") == "string"
    assert gen._normalize_type_name("Int32") == "int"


def test_to_method_signature_extracts_method_name():
    gen = make_gen()
    assert gen._to_method_signature("public async Task SaveChanges(int id)") == "SaveChanges()"


def test_clamp_mermaid_truncates_long_body():
    gen = make_gen()
    gen.MAX_PAYLOAD_LINES = 3
    lines = [
        "```mermaid",
        "graph LR",
        "A-->B",
        "B-->C",
        "C-->D",
        "D-->E",
        "```",
    ]
    out = gen._clamp_mermaid(lines, "dependency_graph")
    assert out[0] == "```mermaid"
    assert out[-1] == "```"
    assert any("truncated" in line for line in out)
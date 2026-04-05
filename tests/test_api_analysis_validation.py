from services.analyzer.api_analysis import api_analysis as aa


def valid_api_output():
    return """# API Endpoint: GET /users/{id}

| Field | Value |
|------|------|
| Kind | Controller Action |
| Controller / Service | UsersController |
| Operation | GetUser |
| Source File | UsersController.cs |
| Route | /users/{id} |
| HTTP Methods | GET |

### Parameters
| Name | Type |
| :--- | :--- |
| id | int |

### Return Type
UserDto

### Purpose & Behaviour
Returns the user record for the supplied identifier and responds with a not found result when no matching user exists.
"""


def test_clean_response_removes_think_tags_code_fences_and_tail():
    raw = """
# API Endpoint: GET /users

| Field | Value |
|------|------|
| Kind | Controller Action |
| Controller / Service | UsersController |
| Operation | GetUsers |
| Source File | UsersController.cs |
| Route | /users |
| HTTP Methods | GET |

### Parameters
| Name | Type |
| :--- | :--- |
| page | int |

### Return Type
PagedResult<UserDto>

### Purpose & Behaviour
Returns a paginated list of users.
I hope this helps
"""
    cleaned = aa.clean_response(raw)

    assert "<think>" not in cleaned
    assert "```" not in cleaned
    assert "I hope this helps" not in cleaned
    assert cleaned.startswith("# API Endpoint: GET /users")


def test_extract_expected_endpoint_title_reads_heading():
    prompt = """Some prompt text

# API Endpoint: POST /orders/create

More text
"""
    assert aa.extract_expected_endpoint_title(prompt) == "POST /orders/create"


def test_extract_expected_endpoint_title_falls_back_when_missing():
    assert aa.extract_expected_endpoint_title("no heading here") == "Unknown_Endpoint"


def test_build_injected_api_output_adds_missing_title():
    fields = {
        "endpoint_title": "GET /users/{id}",
        "kind": "Controller Action",
        "controller": "UsersController",
        "operation": "GetUser",
        "source_file": "UsersController.cs",
        "route": "/users/{id}",
        "http_methods": "GET",
        "return_type": "UserDto",
        "parameters_table": "| Name | Type |\n| :--- | :--- |\n| id | int |",
    }
    out = aa.build_injected_api_output("Returns the requested user.", fields)

    assert out.startswith("# API Endpoint: GET /users/{id}")


def test_build_injected_api_output_keeps_existing_title_behavior():
    fields = {
        "endpoint_title": "GET /users/{id}",
        "kind": "Controller Action",
        "controller": "UsersController",
        "operation": "GetUser",
        "source_file": "UsersController.cs",
        "route": "/users/{id}",
        "http_methods": "GET",
        "return_type": "UserDto",
        "parameters_table": "| Name | Type |\n| :--- | :--- |\n| id | int |",
    }
    text = valid_api_output()
    out = aa.build_injected_api_output(text, fields)
    assert out.startswith("# API Endpoint: GET /users/{id}")


def test_validate_output_accepts_valid_document():
    ok, reason = aa.validate_output(valid_api_output())
    assert ok is True
    assert reason == "Passed"


def test_validate_output_rejects_too_short_text():
    ok, reason = aa.validate_output("too short")
    assert ok is False
    assert "too short" in reason.lower()


def test_validate_output_rejects_missing_required_section():
    text = valid_api_output().replace("### Return Type", "### Something Else")
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "missing required section" in reason.lower()


def test_validate_output_rejects_missing_parameters_table():
    text = valid_api_output().replace("| Name | Type |", "| Param | Type |")
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "missing parameters table" in reason.lower()


def test_validate_output_rejects_prompt_instruction_leakage():
    text = valid_api_output() + "\nDo not write anything after this section"
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "copied prompt instructions" in reason.lower()


def test_validate_output_rejects_code_block():
    text = valid_api_output() + "\n```csharp\npublic class X {}\n```"
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "code block" in reason.lower()


def test_validate_output_rejects_forbidden_code_keyword():
    text = valid_api_output() + "\npublic partial class UsersController"
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "detected code keyword" in reason.lower()


def test_validate_output_rejects_conversational_ending():
    text = valid_api_output() + "\nWould you like me to generate more endpoints?"
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "conversational ending" in reason.lower()


def test_validate_output_rejects_duplicate_table_rows():
    text = """# API Endpoint: GET /users

| Field | Value |
|------|------|
| Kind | Controller Action |
| Controller / Service | UsersController |
| Operation | GetUsers |
| Source File | UsersController.cs |
| Route | /users |
| HTTP Methods | GET |

### Parameters
| Name | Type |
| :--- | :--- |
| id | int |
| id | int |
| id | int |
| id | int |
| id | int |
| id | int |

### Return Type
UserDto

### Purpose & Behaviour
Returns user data for the supplied identifier with a detailed description long enough to avoid the short-output validator.
"""
    ok, reason = aa.validate_output(text)

    assert ok is False
    assert "duplicate table row" in reason.lower()


def test_detect_excessive_duplicate_lines_flags_repetition():
    repeated_line = "This endpoint returns the same repeated explanation for every section in a way that is intentionally long."
    text = "\n".join([repeated_line] * 8)

    bad, reason = aa.detect_excessive_duplicate_lines(text)

    assert bad is True
    assert "repeated line detected" in reason.lower()


def test_detect_duplicate_table_rows_flags_repetition():
    text = "\n".join([
        "| Name | Type |",
        "| :--- | :--- |",
        "| id | int |",
        "| id | int |",
        "| id | int |",
        "| id | int |",
        "| id | int |",
        "| id | int |",
    ])
    bad, reason = aa.detect_duplicate_table_rows(text)

    assert bad is True
    assert "duplicate table row" in reason.lower()
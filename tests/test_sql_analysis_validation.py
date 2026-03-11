from services.analyzer.sql_analysis import sql_analysis as sa


def valid_sql_output():
    return """# Procedure: GetUsers

### Purpose
Retrieves user records for administration and reporting.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | int | User identifier |

### Logic Flow
Validates the input parameter, queries the user table, and returns matching records.

### Data Interactions
* **Reads:** Users
* **Writes:** None
"""


def test_standardize_sql_headings_normalizes_common_variants():
    text = """## procedure: GetUsers
# purpose
Something here
## parameters
Something here
# logic flow
Something here
## data interactions
- Users
"""
    out = sa.standardize_sql_headings(text)

    assert "# Procedure: GetUsers" in out
    assert "### Purpose" in out
    assert "### Parameters" in out
    assert "### Logic Flow" in out
    assert "### Data Interactions" in out


def test_strip_global_context_and_below_removes_global_context_section():
    text = """# Procedure: GetUsers

### 1. Business Purpose
Purpose text

### Global Context
Some huge context block

### 2. Inputs and Outputs
Input text
"""
    out = sa.strip_global_context_and_below(text)

    assert "### Global Context" not in out
    assert "Some huge context block" not in out


def test_clean_response_removes_think_tags_code_fences_and_trailing_phrases():
    raw = """<think>hidden</think>
```markdown
# Procedure: GetUsers

### Purpose
Purpose text

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | int | User identifier |

### Logic Flow
Logic text

### Data Interactions
* **Reads:** Users
* **Writes:** None
Would you like me to document another procedure?
```
"""

    out = sa.clean_response(raw)

    assert "<think>" not in out
    assert "```" not in out
    assert "I hope this helps" not in out
    assert out.startswith("# Procedure: GetUsers")

def test_extract_expected_procedure_name_reads_heading():
    prompt = """Some intro

# Procedure: EAlertQ_EnQueue

Other text
"""
    assert sa.extract_expected_procedure_name(prompt) == "EAlertQ_EnQueue"

def test_extract_expected_procedure_name_falls_back_when_missing():
    assert sa.extract_expected_procedure_name("no procedure heading") == "Unknown_Procedure"

def test_enforce_sql_template_adds_missing_title():
    text = """### 1. Business Purpose
Purpose text

2. Inputs and Outputs

Input text
"""
    out = sa.enforce_sql_template(text, "GetUsers")

    assert out.startswith("# Procedure: GetUsers")

def test_enforce_sql_template_keeps_existing_title():
    text = valid_sql_output()
    out = sa.enforce_sql_template(text, "ShouldNotReplace")
    assert out.startswith("# Procedure: GetUsers")

def test_validate_output_accepts_valid_document():
    ok, reason = sa.validate_output(valid_sql_output())

    assert ok is True
    assert reason == "Passed"

def test_validate_output_rejects_too_short_text():
    ok, reason = sa.validate_output("too short")

    assert ok is False
    assert "output empty" in reason.lower()

def test_validate_output_rejects_missing_required_section():
    text = valid_sql_output().replace("### Data Interactions", "### Something Else")
    ok, reason = sa.validate_output(text)

    assert ok is False
    assert "missing required section" in reason.lower()

def test_validate_output_rejects_raw_sql():
    text = valid_sql_output() + "\nSELECT * FROM Users\nUPDATE Users SET Name = 'X'"
    ok, reason = sa.validate_output(text)

    assert ok is False
    assert "raw sql" in reason.lower()

def test_validate_output_rejects_raw_sql_create_and_begin():
    text = valid_sql_output() + "\nCREATE PROCEDURE dbo.GetUsers AS\nBEGIN\nSELECT 1\nEND"
    ok, reason = sa.validate_output(text)

    assert ok is False
    assert "raw sql" in reason.lower()

def test_validate_output_rejects_conversational_ending():
    text = valid_sql_output() + "\nWould you like me to document another procedure?"
    ok, reason = sa.validate_output(text)

    assert ok is False
    assert "conversational ending" in reason.lower()

def test_detect_excessive_duplicate_lines_flags_repetition():
    repeated_line = "This procedure applies the same repeated explanation in every section and this sentence is intentionally long."
    text = "\n".join([repeated_line] * 8)

    bad, reason = sa.detect_excessive_duplicate_lines(text)

    assert bad is True
    assert "repeated normalized line detected" in reason.lower()

def test_detect_repeated_line_chunks_flags_repetition():
    chunk = "\n".join([
    "Line A repeated chunk",
    "Line B repeated chunk",
    "Line C repeated chunk",
    ])
    text = f"{chunk}\n\n{chunk}\n\n{chunk}"

    bad, reason = sa.detect_repeated_line_chunks(text)

    assert bad is True
    assert "repeated line chunk" in reason.lower()
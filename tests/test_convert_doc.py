import convert_doc as cd


def test_strip_md_heading_prefix_removes_hashes():
    assert cd.strip_md_heading_prefix("### My Title") == "My Title"


def test_clean_inline_removes_links_and_inline_code():
    assert cd.clean_inline("See [Login](https://example.com) and `pytest -v`") == "See Login and pytest -v"


def test_looks_like_chapter_title_detects_pages_procedures_and_filenames():
    assert cd.looks_like_chapter_title("Page: Login.aspx") is True
    assert cd.looks_like_chapter_title("Procedure: GetUsers") is True
    assert cd.looks_like_chapter_title("Helper.cs") is True
    assert cd.looks_like_chapter_title("This is a normal paragraph.") is False


def test_heading_helpers_detect_correct_levels():
    assert cd.is_md_h1("# Title") is True
    assert cd.is_md_h1("## Title") is False
    assert cd.is_md_h2("## Section") is True
    assert cd.is_md_h3("### Subsection") is True


def test_md_heading_text_cleans_hashes_and_inline_markup():
    assert cd.md_heading_text("## `Table` of [Contents](x)") == "Table of Contents"


def test_md_bullet_text_supports_multiple_bullet_styles():
    assert cd.md_bullet_text("- Alpha") == "Alpha"
    assert cd.md_bullet_text("* Beta") == "Beta"
    assert cd.md_bullet_text("+ Gamma") == "Gamma"
    assert cd.md_bullet_text("• Delta") == "Delta"
    assert cd.md_bullet_text("Not a bullet") == ""


def test_find_toc_range_finds_toc_block():
    lines = [
        "# Technical Documentation",
        "",
        "## Table of Contents",
        "### Web Pages",
        "- Login.aspx",
        "- Dashboard.aspx",
        "Page: Login.aspx",
        "Actual body starts",
    ]
    assert cd.find_toc_range(lines) == (2, 6)


def test_collect_toc_structure_groups_items_by_category():
    md = """# Technical Documentation

## Table of Contents
### Web Pages
- Login.aspx
- Dashboard.aspx
### Database Reference
- GetUsers

Page: Login.aspx
Body starts here
"""
    toc = cd.collect_toc_structure(md)
    assert toc == [
        ("Web Pages", ["Login.aspx", "Dashboard.aspx"]),
        ("Database Reference", ["GetUsers"]),
    ]


def test_toc_item_to_chapter_title_maps_correctly():
    assert cd.toc_item_to_chapter_title("Login.aspx") == "Page: Login.aspx"
    assert cd.toc_item_to_chapter_title("Helper.cs") == "Helper.cs"
    assert cd.toc_item_to_chapter_title("GetUsers") == "Procedure: GetUsers"


def test_slug_bookmark_is_safe_and_prefixed_when_needed():
    result = cd.slug_bookmark("123 very long title with spaces and symbols !!!")
    assert result.startswith("S_")
    assert len(result) <= 40


def test_table_detection_helpers_work():
    assert cd.is_table_line("| A | B |") is True
    assert cd.is_table_sep("| --- | :---: |") is True
    assert cd.is_table_sep("| A | B |") is False


def test_parse_table_reads_rows():
    lines = [
        "| Name | Type |",
        "| --- | --- |",
        "| id | int |",
        "| name | nvarchar |",
        "Next paragraph",
    ]
    rows, next_i = cd.parse_table(lines, 0)
    assert rows == [
        ["Name", "Type"],
        ["id", "int"],
        ["name", "nvarchar"],
    ]
    assert next_i == 4


def test_parse_table_returns_none_for_non_table():
    rows, next_i = cd.parse_table(["Not a table"], 0)
    assert rows is None
    assert next_i == 0
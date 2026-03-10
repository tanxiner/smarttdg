
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
import compile as c
def setup_function():
    c._USED_SLUGS.clear()


def test_get_file_order_uses_last_number():
    assert c.get_file_order("Part10_Section2.md") == 2


def test_get_file_order_returns_zero_when_no_number():
    assert c.get_file_order("Intro.md") == 0


def test_clean_title_removes_known_prefixes():
    assert c.clean_title("Page: Login") == "Login"
    assert c.clean_title("Module: Utils") == "Utils"
    assert c.clean_title("Procedure: GetUsers") == "GetUsers"


def test_clean_title_handles_none_and_extra_spaces():
    assert c.clean_title(None) == ""
    assert c.clean_title("  Page:   My    Screen   ") == "My Screen"


def test_make_slug_builds_stable_slug():
    slug = c.make_slug("Web Pages", "Login_Page", 1, "User Login")
    assert slug == "web-pages-loginpage-1-user-login"


def test_make_slug_falls_back_when_empty():
    slug = c.make_slug("!!!", "@@@", 5, "###")
    assert slug == "5"


def test_ensure_unique_slug_appends_suffix():
    assert c._ensure_unique_slug("abc") == "abc"
    assert c._ensure_unique_slug("abc") == "abc-2"
    assert c._ensure_unique_slug("abc") == "abc-3"


def test_normalize_whitespace_collapses_extra_blank_lines():
    text = "Hello   \n\n\n\nWorld   "
    assert c.normalize_whitespace(text) == "Hello\n\nWorld"


def test_process_folder_without_h1_creates_single_section(tmp_path):
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "Intro.md").write_text("Plain body content\n\nMore text", encoding="utf-8")

    toc_lines = []
    body_content = []

    c.process_folder(str(folder), "Web Pages", toc_lines, body_content)

    joined_toc = "\n".join(toc_lines)
    joined_body = "".join(body_content)

    assert "### Web Pages" in joined_toc
    assert "- [Intro](#web-pages-intro-1-intro)" in joined_toc
    assert "<a id='web-pages-intro-1-intro'></a>" in joined_body
    assert "Plain body content" in joined_body


def test_process_folder_with_multiple_h1_creates_multiple_entries(tmp_path):
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "Login.md").write_text(
        "# Page: Login\nFirst\n\n# Page: Login Again\nSecond",
        encoding="utf-8",
    )

    toc_lines = []
    body_content = []

    c.process_folder(str(folder), "Web Pages", toc_lines, body_content)

    joined_toc = "\n".join(toc_lines)
    joined_body = "".join(body_content)

    assert joined_toc.count("- [Login](#") == 2
    assert "web-pages-login-1-login" in joined_body
    assert "web-pages-login-2-login" in joined_body
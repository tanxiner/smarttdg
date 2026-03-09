from app import app, _zip_prefix_from_request


def test_zip_prefix_from_request_valid_filename():
    with app.test_request_context("/download/md_documentation?zipFilename=Project.zip"):
        assert _zip_prefix_from_request() == "Project_"


def test_zip_prefix_from_request_supports_lowercase_param_name():
    with app.test_request_context("/download/md_documentation?zipfilename=MyApp.zip"):
        assert _zip_prefix_from_request() == "MyApp_"


def test_zip_prefix_from_request_sanitizes_bad_characters():
    with app.test_request_context("/download/md_documentation?zipFilename=My Project<>:/?.zip"):
        assert _zip_prefix_from_request() == "My_Project_"


def test_zip_prefix_from_request_returns_empty_when_missing():
    with app.test_request_context("/download/md_documentation"):
        assert _zip_prefix_from_request() == ""


def test_zip_prefix_from_request_returns_empty_when_only_invalid_chars():
    with app.test_request_context("/download/md_documentation?zipFilename=<>:\"/\\\\|?*.zip"):
        assert _zip_prefix_from_request() == ""
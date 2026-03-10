from app import app, _zip_prefix_from_request


def test_zip_prefix_from_request_valid_filename():
    with app.test_request_context("/download/md_documentation?zipFilename=Project.zip"):
        assert _zip_prefix_from_request() == "Project_"


def test_zip_prefix_from_request_supports_lowercase_param_name():
    with app.test_request_context("/download/md_documentation?zipfilename=MyApp.zip"):
        assert _zip_prefix_from_request() == "MyApp_"


def test_zip_prefix_from_request_sanitizes_bad_characters():
    with app.test_request_context(
        "/download/md_documentation",
        query_string={"zipFilename": "My Project<>.zip"},
    ):
        assert _zip_prefix_from_request() == "My_Project_"


def test_zip_prefix_from_request_returns_empty_for_path_like_value():
    with app.test_request_context(
        "/download/md_documentation",
        query_string={"zipFilename": "My Project<>:/?.zip"},
    ):
        assert _zip_prefix_from_request() == ""


def test_zip_prefix_from_request_returns_empty_when_missing():
    with app.test_request_context("/download/md_documentation"):
        assert _zip_prefix_from_request() == ""


def test_zip_prefix_from_request_returns_empty_when_only_invalid_chars():
    with app.test_request_context("/download/md_documentation?zipFilename=<>:\"/\\\\|?*.zip"):
        assert _zip_prefix_from_request() == ""


def test_md_download_route_returns_response():
    client = app.test_client()
    response = client.get("/download/md_documentation?zipFilename=Demo.zip")
    assert response.status_code in (200, 404)


def test_docx_download_route_returns_response():
    client = app.test_client()
    response = client.get("/download/word_documentation?zipFilename=Demo.zip")
    assert response.status_code in (200, 404)
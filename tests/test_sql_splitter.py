import sql_splitter as ss


def test_get_dynamic_acronyms_extracts_uppercase_tokens():
    text = "SELECT * FROM TAMS_USER WHERE API_ID = 1 AND SBS_CODE = 'X'"
    result = ss.get_dynamic_acronyms(text)
    assert '"API_ID"' in result
    assert '"SBS_CODE"' in result
    assert '"TAMS_USER"' in result


def test_get_dynamic_acronyms_excludes_sql_keywords_and_numbers():
    text = "SELECT 123 FROM USERS WHERE ID = 5"
    result = ss.get_dynamic_acronyms(text)
    assert '"SELECT"' not in result
    assert '"FROM"' not in result
    assert '"WHERE"' not in result
    assert '"123"' not in result


def test_extract_proc_name_from_create_procedure():
    sql = """
    CREATE PROCEDURE [dbo].[GetUsers]
    AS
    BEGIN
        SELECT 1
    END
    """
    assert ss.extract_proc_name(sql) == "GetUsers"


def test_extract_proc_name_from_alter_proc_without_schema():
    sql = """
    ALTER PROC UpdateRoster
    AS
    BEGIN
        SELECT 1
    END
    """
    assert ss.extract_proc_name(sql) == "UpdateRoster"


def test_extract_proc_name_returns_unknown_when_missing():
    assert ss.extract_proc_name("SELECT * FROM Users") == "Unknown_Proc"


def test_sanitize_filename_removes_invalid_characters():
    assert ss.sanitize_filename('abc<>:"/\\\\|?*def') == "abcdef"


def test_read_procedures_splits_multiple_procs_by_go(tmp_path):
    sql_file = tmp_path / "sample.sql"
    sql_file.write_text(
        """
CREATE PROCEDURE dbo.FirstProc
AS
BEGIN
    SELECT 1
END
GO

ALTER PROCEDURE [dbo].[SecondProc]
AS
BEGIN
    SELECT 2
END
GO
""",
        encoding="utf-8",
    )

    procedures = ss.read_procedures(str(sql_file))
    assert len(procedures) == 2
    assert "FirstProc" in procedures[0]
    assert "SecondProc" in procedures[1]


def test_read_procedures_handles_last_proc_without_trailing_go(tmp_path):
    sql_file = tmp_path / "sample2.sql"
    sql_file.write_text(
        """
CREATE PROCEDURE dbo.LastProc
AS
BEGIN
    SELECT 1
END
""",
        encoding="utf-8",
    )

    procedures = ss.read_procedures(str(sql_file))
    assert len(procedures) == 1
    assert "LastProc" in procedures[0]
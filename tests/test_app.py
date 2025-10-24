import pytest

import DAL


@pytest.fixture
def dal(tmp_path, monkeypatch):
    """Provide the DAL module backed by a throwaway SQLite database."""
    test_db_path = tmp_path / "projects_test.db"
    monkeypatch.setattr(DAL, "DB_PATH", test_db_path)
    DAL.init_db()
    return DAL


@pytest.fixture
def client(dal, tmp_path, monkeypatch):
    """Create a Flask test client with uploads redirected to a temp directory."""
    import app as flask_app

    uploads_path = tmp_path / "uploads"
    monkeypatch.setattr(flask_app, "UPLOAD_FOLDER", uploads_path)
    uploads_path.mkdir(parents=True, exist_ok=True)

    flask_app.app.config.update({"TESTING": True})
    with flask_app.app.test_client() as test_client:
        yield test_client


def test_home_page_renders(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"See my projects" in response.data


def test_projects_page_displays_saved_project(client, dal):
    sample_title = "Pytest Demo Project"
    dal.insert_project(
        title=sample_title,
        description="Example entry created during testing.",
        image_file_name="demo.png",
        repo_url="https://example.com/repo",
        demo_url=None,
    )

    response = client.get("/projects")
    assert response.status_code == 200
    assert sample_title.encode() in response.data


def test_insert_project_persists_row(dal):
    dal.insert_project(
        title="Data Layer Check",
        description="Verifies DAL can persist projects.",
        image_file_name="dal-example.png",
        repo_url=None,
        demo_url="https://example.com/demo",
    )

    projects = list(dal.fetch_projects())
    assert len(projects) == 1
    saved = projects[0]
    assert saved["title"] == "Data Layer Check"
    assert saved["image_file_name"] == "dal-example.png"

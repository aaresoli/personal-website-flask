import pytest

import DAL


@pytest.fixture
def dal(tmp_path, monkeypatch):
    """Back the DAL module with a temp SQLite database for isolation."""
    test_db_path = tmp_path / "projects_test.db"
    monkeypatch.setattr(DAL, "DB_PATH", test_db_path)
    DAL.init_db()
    return DAL


@pytest.fixture
def client(dal, tmp_path, monkeypatch):
    """Expose a Flask test client with uploads redirected to a temp directory."""
    import app as flask_app

    uploads_path = tmp_path / "uploads"
    monkeypatch.setattr(flask_app, "UPLOAD_FOLDER", uploads_path)
    uploads_path.mkdir(parents=True, exist_ok=True)

    flask_app.app.config.update({"TESTING": True})
    with flask_app.app.test_client() as test_client:
        yield test_client

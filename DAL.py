"""Simple SQLite-based data access layer for project records."""

from __future__ import annotations

import sqlite3 as sqlite
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Mapping

DB_PATH = Path(__file__).resolve().parent / "projects.db"


@contextmanager
def get_connection():
    """Yield a SQLite connection with row access by column name."""
    conn = sqlite.connect(DB_PATH)
    conn.row_factory = sqlite.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """Ensure the projects table exists."""
    schema = """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        image_file_name TEXT NOT NULL,
        repo_url TEXT,
        demo_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    with get_connection() as conn:
        conn.execute(schema)
        conn.commit()


def fetch_projects() -> Iterable[Mapping[str, object]]:
    """Return all projects ordered by most recent first."""
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, title, description, image_file_name, repo_url, demo_url "
            "FROM projects "
            "ORDER BY "
            "CASE title "
            "  WHEN 'X (Twitter) Clone' THEN 0 "
            "  WHEN 'Messaging App' THEN 1 "
            "  WHEN 'Cryptography in Supply Chain' THEN 2 "
            "  ELSE 3 "
            "END, "
            "created_at DESC, id DESC"
        )
        return cursor.fetchall()


def insert_project(
    title: str,
    description: str,
    image_file_name: str,
    repo_url: str | None = None,
    demo_url: str | None = None,
) -> None:
    """Insert a new project row."""
    query = """
    INSERT INTO projects (title, description, image_file_name, repo_url, demo_url)
    VALUES (?, ?, ?, ?, ?)
    """
    with get_connection() as conn:
        conn.execute(query, (title, description, image_file_name, repo_url, demo_url))
        conn.commit()

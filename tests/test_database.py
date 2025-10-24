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


def test_fetch_projects_orders_recent_first(dal):
    dal.insert_project(
        title="First",
        description="First entry",
        image_file_name="first.png",
        repo_url=None,
        demo_url=None,
    )
    dal.insert_project(
        title="Second",
        description="Second entry",
        image_file_name="second.png",
        repo_url=None,
        demo_url=None,
    )

    projects = list(dal.fetch_projects())
    titles = [row["title"] for row in projects]
    assert titles[0] == "Second"

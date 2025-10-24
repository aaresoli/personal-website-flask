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

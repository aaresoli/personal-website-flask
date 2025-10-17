"""Flask application that serves the personal website via Jinja templates."""

from flask import Flask, redirect, render_template, request, url_for

import DAL

DAL.init_db()

app = Flask(__name__)


@app.route("/")
def home():
    """Render the landing page."""
    return render_template("index.html", page="home")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html", page="about")


@app.route("/resume")
def resume():
    """Render the resume page."""
    return render_template("resume.html", page="resume")


@app.route("/projects")
def projects():
    """Render the projects page."""
    project_rows = DAL.fetch_projects()
    return render_template("projects.html", page="projects", projects=project_rows)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render the project submission form and persist new projects."""
    form_error = None
    form_data = {}
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        image_file_name = request.form.get("image_file_name", "").strip()
        repo_url = request.form.get("repo_url", "").strip() or None
        demo_url = request.form.get("demo_url", "").strip() or None
        form_data = {
            "title": title,
            "description": description,
            "image_file_name": image_file_name,
            "repo_url": repo_url or "",
            "demo_url": demo_url or "",
        }

        if title and description and image_file_name:
            DAL.insert_project(
                title=title,
                description=description,
                image_file_name=image_file_name,
                repo_url=repo_url,
                demo_url=demo_url,
            )
            return redirect(url_for("projects"))
        form_error = "Please provide a title, description, and image file name."

    return render_template(
        "contact.html",
        page="contact",
        form_error=form_error,
        form_data=form_data,
    )


@app.route("/thank-you")
def thankyou():
    """Render the confirmation page shown after form submission."""
    return render_template("thankyou.html", page="thankyou")


if __name__ == "__main__":
    # Enable reloader & debugger for local development usage.
    app.run(debug=True)

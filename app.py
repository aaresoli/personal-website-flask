"""Flask application that serves the personal website via Jinja templates."""

from pathlib import Path
from uuid import uuid4

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

import DAL

DAL.init_db()

app = Flask(__name__)

UPLOAD_FOLDER = Path(app.root_path) / "static" / "images"
ALLOWED_IMAGE_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "gif",
    "webp",
    "svg",
}
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


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


@app.route("/projects/new", methods=["GET", "POST"])
def new_project():
    """Render the project submission form and persist new projects."""
    form_error = None
    form_data = {}
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        repo_url = request.form.get("repo_url", "").strip() or None
        demo_url = request.form.get("demo_url", "").strip() or None
        form_data = {
            "title": title,
            "description": description,
            "repo_url": repo_url or "",
            "demo_url": demo_url or "",
        }
        image_file = request.files.get("image_file")
        image_file_name = None

        image_target_path = None
        if image_file and image_file.filename:
            original_name = secure_filename(image_file.filename)
            suffix = Path(original_name).suffix.lower()
            extension = suffix.lstrip(".")
            if extension not in ALLOWED_IMAGE_EXTENSIONS:
                form_error = (
                    "Please upload an image file (png, jpg, jpeg, gif, webp, or svg)."
                )
            else:
                image_file_name = f"{uuid4().hex}{suffix}"
                image_target_path = UPLOAD_FOLDER / image_file_name
        else:
            form_error = "An image file is required."

        if not title or not description:
            form_error = form_error or "Please complete the title and description."

        if not form_error and image_file_name and image_target_path:
            image_file.save(image_target_path)
            DAL.insert_project(
                title=title,
                description=description,
                image_file_name=image_file_name,
                repo_url=repo_url,
                demo_url=demo_url,
            )
            return redirect(url_for("projects"))

    return render_template(
        "add_project.html",
        page="add_project",
        form_error=form_error,
        form_data=form_data,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render the contact form and log submissions before redirecting to thanks."""
    if request.method == "POST":
        app.logger.info("Contact submission: %s", dict(request.form))
        return redirect(url_for("thankyou"))

    return render_template("contact.html", page="contact")


@app.route("/thank-you")
def thankyou():
    """Render the confirmation page shown after form submission."""
    return render_template("thankyou.html", page="thankyou")


if __name__ == "__main__":
    # Enable reloader & debugger for local development usage.
    app.run(debug=True)

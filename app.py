"""Flask application that serves the personal website via Jinja templates."""

from flask import Flask, redirect, render_template, request, url_for

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
    return render_template("projects.html", page="projects")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render the contact form and log submissions before redirecting to thanks."""
    if request.method == "POST":
        # Persisting to storage/email can be plugged in later; capture payload for now.
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

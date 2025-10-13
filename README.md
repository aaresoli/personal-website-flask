# Aashish Personal Website (Flask)

Multi-page, responsive, accessible website now delivered with Flask so the layout and routing are handled server-side.

## Highlights
- Flask routes render Jinja templates that extend a shared `base.html`, keeping navigation and metadata consistent.
- Static assets live under `static/` for CSS, JS, and imagery while templates use `url_for` so links stay portable.
- Contact form runs the existing HTML5 + JS validation and posts to the Flask endpoint, which logs the payload and redirects to the thank-you page.

## Structure
- `app.py` — Flask entrypoint and route definitions
- `templates/` — Jinja templates (`base.html`, `index.html`, `about.html`, `resume.html`, `projects.html`, `contact.html`, `thankyou.html`)
- `static/css/style.css` — Shared styling
- `static/js/script.js` — Nav highlighting, form validation
- `static/images/` — Site imagery
- `.prompt/dev_notes.md` — AI prompts & reflection per assignment

## Setup & Run
1. `source venv/bin/activate` (or create your own venv and `pip install -r requirements.txt` if you prefer a fresh environment)
2. `python app.py`

Visit `http://127.0.0.1:5000/` in your browser. The contact form submission will log to the Flask console and redirect to `/thank-you`.

# Aashish Personal Website (Flask)

Multi-page, responsive, accessible website delivered with Flask. Content now comes from a lightweight SQLite layer so projects can be added without editing templates.

## Highlights
- `DAL.py` bootstraps the `projects.db` database and provides helpers to fetch/insert project rows.
- `/projects` renders a responsive HTML table backed by live database data (Title, Description, Image, optional repo/demo links).
- `/projects/new` provides an “Add Project” form: uploading a title/description/image saves the file to `static/images/`, writes the record to SQLite, and the project appears instantly, while `/contact` remains a public-facing contact form.
- Navigation includes a GitHub CTA that points at the Flask repo (`personal-website-flask`).
- Static assets stay under `static/` while Jinja templates extend `templates/base.html` to keep shared layout and metadata consistent.

## Structure
- `app.py` — Flask entrypoint, route definitions, and DAL integration.
- `DAL.py` — Data access layer for SQLite (`projects.db`).
- `projects.db` — SQLite database seeded with three sample projects.
- `templates/` — Jinja templates (`base.html`, `index.html`, `about.html`, `resume.html`, `projects.html`, `contact.html`, `thankyou.html`).
- `static/css/style.css` — Shared styling (includes project table + alert styles).
- `static/js/script.js` — Nav highlighting and client-side validation helpers.
- `static/images/` — Site imagery used in the project table.
- `.prompt/dev_notes.md` — AI prompts log & reflections.

## Setup & Run
1. Create/activate a virtual environment (recommended to avoid Debian’s externally-managed guard):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
2. Launch the app:
   ```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000/` in your browser. Reach out via `/contact`, or add a new project from `/projects/new` by uploading an image (PNG/JPG/GIF/SVG/WebP) and confirming it appears under `/projects` right away—no manual file moves required.

## Containerized Deployment
Build the Docker image (from the project root):
```bash
docker build -t aidd-flask .
```

Run the container and publish port 5000:
```bash
docker run --rm -p 5000:5000 aidd-flask
```

Uploaded images and SQLite data live inside the container by default. To persist them between runs, mount the project database (and optionally the `static/images/` directory) as volumes:
```bash
docker run --rm -p 5000:5000 \
  -v "$(pwd)/projects.db:/app/projects.db" \
  -v "$(pwd)/static/images:/app/static/images" \
  aidd-flask
```

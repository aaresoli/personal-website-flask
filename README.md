# Aashish Personal Website

Multi-page, responsive, accessible website built for coursework.

## Highlights
- Slate + indigo theme managed via CSS custom properties for easy retuning.
- Project cards and resume content share modular components to stay consistent.
- Contact form enforces HTML5 rules plus password confirmation, then routes to `thankyou.html` client-side for static hosting compatibility.

## Structure
- `index.html` — Home
- `about.html` — About Me
- `resume.html` — Resume (print-friendly)
- `projects.html` — Projects
- `contact.html` — Contact form (HTML5 validation + JS password match)
- `thankyou.html` — Redirect target after successful submit
- `styles.css` — Shared styling
- `script.js` — Nav highlighting, form validation
- `images/` — Placeholder assets
- `.prompt/dev_notes.md` — AI prompts & reflection per assignment

## How to run
Open `index.html` in any browser. No build step required.  
The contact form validates locally and then redirects to `thankyou.html`, so no backend is necessary.

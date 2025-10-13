# .prompt/dev_notes.md

## AI Prompts Log

### Prompt 1
**You:** "Generate a clean, responsive multi-page personal site (Home, About, Resume, Projects, Contact, Thank You) using semantic HTML, one shared CSS, and minimal JS for form validation. Must include accessible labels, skip link, and active nav highlighting."
**AI Output (excerpt):** Boilerplate HTML files, a `styles.css` with CSS variables and grid layout, and `script.js` for active link + form validation.
**Action:** Accepted with edits — tightened typography, added print CSS for resume, and improved button contrast.

### Prompt 2
**You:** "Create HTML form with first/last name, email, password, confirm password. Use HTML attributes (`required`, `minlength`, types) and JS to show inline errors and enforce password match. Redirect to thankyou page on success."
**AI Output (excerpt):** Sample form and event listener that prevents submit if invalid, otherwise redirects.
**Action:** Accepted with minor changes — added `aria-live` regions, kept native browser validation messages, added visual focus outline.

### Prompt 3
**You:** "Design modern CSS with variables, card components, responsive grid, and a simple hero layout. Keep it professional and accessible."
**AI Output (excerpt):** CSS variables, responsive grids, buttons, and card styles.
**Action:** Modified — refined spacing, borders, and mobile breakpoints; added sticky header and subtle backdrop blur.

### Prompt 4
**You:** "Convert the personal website into a Flask project with templates, static asset folders, and Python routing."
**AI Output (excerpt):** Suggested `app.py` with multiple routes, a base layout, and reorganized static folders.
**Action:** Accepted the general structure, rewired the contact POST handler to log and redirect, and tightened template variables so active navigation states work with both Flask and the existing JS.

## Reflection (≈150 words)
AI accelerated the initial scaffolding and saved time on repetitive structure: every page started with consistent semantic markup, and the assistant reminded me to include skip links, accessible labels, and touches like footer year injection. When I swapped the project to Flask, the assistant again provided a solid draft that wired routes, templates, and static assets so I could focus on polishing the experience. Still, the drafts surfaced familiar quirks. Color choices initially missed contrast guidelines, spacing collapsed on narrow viewports, and the resume layout ignored print styling; more recently, template suggestions mixed redundant active-nav logic with JavaScript I already trusted. I had to audit each section, rewrite portions of the CSS, and reconcile Python-side state with client-side validation so the form behaved predictably. Treating AI output as a starting point rather than a finished product let me keep momentum while staying accountable for accessibility, code clarity, and deployment fit.

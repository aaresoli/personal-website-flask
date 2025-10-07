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

## Reflection (≈150 words)
AI accelerated the initial scaffolding and saved time on repetitive structure: every page started with consistent semantic markup, and the assistant reminded me to include skip links, accessible labels, and small touches like footer year injection. Where it really shined was jumping me past blank screens so I could iterate on styling instead of wiring boilerplate. Still, the early drafts exposed common AI quirks. Color choices initially missed contrast guidelines, spacing collapsed on narrow viewports, and the resume layout ignored print styling. I had to audit each section, rewrite portions of the CSS, and tighten the JavaScript so native validation remained intact while custom password matching behaved predictably. Balancing AI input with my own judgment meant treating the suggestions as drafts: I compared outputs against course requirements, kept what aligned, and consciously overruled anything that felt noisy or brittle. Documenting those decisions helped me stay accountable for the final experience.

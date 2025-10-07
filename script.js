/* =========================================================================
   Personal Site – Client JS
   - Form validation (HTML5 + custom password confirmation)
   - Inline error messaging + aria-invalid
   - Active nav state via [aria-current="page"]
   - Footer year injection
   Last updated: 2025-10-07
   ======================================================================= */

document.addEventListener('DOMContentLoaded', () => {
  // -----------------------------
  // 1) ACTIVE NAV & FOOTER YEAR
  // -----------------------------
  (function setActiveNavAndYear() {
    const pageMap = {
      home: 'index.html',
      about: 'about.html',
      resume: 'resume.html',
      projects: 'projects.html',
      contact: 'contact.html',
      thankyou: 'thankyou.html'
    };

    // Mark current page in the primary nav
    const current = (() => {
      const datasetPage = document.body?.dataset?.page;
      if (datasetPage && pageMap[datasetPage]) {
        return pageMap[datasetPage];
      }

      // Strip query/hash; default to index.html
      const file = location.pathname.split('/').pop();
      return file && file.trim() !== '' ? file : 'index.html';
    })();

    document.querySelectorAll('.site-nav a[href]').forEach(a => {
      const hrefFile = (a.getAttribute('href') || '').split('/').pop();
      if (hrefFile === current) {
        a.setAttribute('aria-current', 'page');
      } else {
        a.removeAttribute('aria-current');
      }
    });

    // Footer © year
    const y = document.getElementById('year');
    if (y) y.textContent = new Date().getFullYear();
  })();

  // -----------------------------
  // 2) FORM VALIDATION
  // -----------------------------
  const form = document.getElementById('contactForm');
  if (!form) return; // No form on this page

  // Ensure native validation is enabled even if novalidate was left in HTML
  form.removeAttribute('novalidate');

  // Helper: find the error <small> for a field
  function getErrorNode(field) {
    const fieldWrapper = field.closest('.form-field');
    if (!fieldWrapper) return null;
    return fieldWrapper.querySelector('.error');
  }

  // Helper: compute a friendly validation message
  function getErrorMessage(field) {
    const name = field.getAttribute('aria-label') || field.name || 'This field';
    const v = field.validity;
    if (v.valueMissing) return 'This field is required.';
    if (field.type === 'email' && v.typeMismatch) return 'Enter a valid email address.';
    if (v.tooShort) return `Must be at least ${field.minLength} characters.`;
    if (v.patternMismatch) return field.getAttribute('title') || 'Please match the requested format.';
    if (v.rangeUnderflow) return `Must be at least ${field.getAttribute('min')}.`;
    if (v.rangeOverflow) return `Must be at most ${field.getAttribute('max')}.`;
    if (v.stepMismatch) return 'Please enter a valid value.';
    return field.validationMessage || 'Please fix this field.';
  }

  // Set or clear the visible error for a field
  function renderFieldValidity(field) {
    const error = getErrorNode(field);
    const isValid = field.checkValidity();
    field.setAttribute('aria-invalid', isValid ? 'false' : 'true');
    if (error) error.textContent = isValid ? '' : getErrorMessage(field);
    return isValid;
  }

  // Custom rule: ensure password and confirm password stay in sync
  function enforcePasswordConfirmation() {
    const pw = form.querySelector('#password');
    const confirm = form.querySelector('#confirmPassword');
    if (!pw || !confirm) return true;

    if (confirm.value && pw.value !== confirm.value) {
      confirm.setCustomValidity('Passwords must match.');
    } else {
      confirm.setCustomValidity('');
    }

    return confirm.checkValidity();
  }

  // Validate all known fields in the form
  function validateAllFields() {
    // Choose all controls that can be validated
    const fields = form.querySelectorAll('input, select, textarea');
    let allValid = true;

    const passwordsMatch = enforcePasswordConfirmation();
    if (!passwordsMatch) allValid = false;

    fields.forEach(field => {
      const ok = renderFieldValidity(field);
      if (!ok) allValid = false;
    });

    return allValid;
  }

  // Live validation: clear/set messages while typing or blurring
  form.addEventListener('input', (e) => {
    const target = e.target;
    if (!(target instanceof HTMLElement)) return;

    if (target.id === 'password' || target.id === 'confirmPassword') {
      enforcePasswordConfirmation();
    }

    // Re-render this field’s message
    if (target.matches('input, select, textarea')) {
      renderFieldValidity(target);
    }
  });

  form.addEventListener('blur', (e) => {
    const target = e.target;
    if (target && target.matches && target.matches('input, select, textarea')) {
      renderFieldValidity(target);
    }
  }, true);

  // Submit handler
  form.addEventListener('submit', (e) => {
    const ok = validateAllFields();

    if (!ok) {
      e.preventDefault();

      // Focus/scroll to first invalid field for accessibility
      const firstInvalid = form.querySelector('[aria-invalid="true"]');
      if (firstInvalid && typeof firstInvalid.focus === 'function') {
        firstInvalid.focus({ preventScroll: false });
      }
      return;
    }

    // Static hosting can't process POSTs; simulate success client-side.
    e.preventDefault();
    window.location.assign('thankyou.html');
  });
});

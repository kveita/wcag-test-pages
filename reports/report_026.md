# WCAG Test Page 026 — Accessibility Audit Report

**Page URL:** `pages/page_026.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 4
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 4
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 4
- **False positives:** 0

## Expected Violations

1. **Form — WCAG 2.1.1, 4.1.2** ❌ Missing
   - Issue: Link with href='#' has no destination
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

2. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

3. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use <thead>, <th> elements with proper scope attributes.

4. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **form-label-missing — WCAG 2.1.1, 4.1.2**
  - Detected: Link with href='#' has no destination
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input field with no associated label or aria-label
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Table uses layout= attribute or CSS that breaks column headers association
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: JavaScript widget responds to click but not to keyboard Enter/Space

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_026.html](pages/page_026.html)*
# WCAG Test Page 056 — Accessibility Audit Report

**Page URL:** `pages/page_056.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 5
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 5
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 5
- **False positives:** 0

## Expected Violations

1. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Page has fixed width layout that breaks when user zooms to 200%
   - Fix: Remove fixed width or allow text wrapping.

2. **ARIA — WCAG 4.1.3** ❌ Missing
   - Issue: aria-live region updates but total announcements exceed live region limits without wrapping
   - Fix: Remove aria-hidden from the live region container.

3. **Form — WCAG 1.4.1** ❌ Missing
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

4. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Use <thead>, <th> elements with proper scope attributes.

5. **Image — WCAG 2.4.4, 1.1.1** ❌ Missing
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

## Detected Violations (Audit)

- ❌ **table-layout-fixed — WCAG 1.4.10**
  - Detected: Page has fixed width layout that breaks when user zooms to 200%
- ❌ **aria-hidden-live — WCAG 4.1.3**
  - Detected: aria-live region updates but total announcements exceed live region limits without wrapping
- ❌ **form-label-missing — WCAG 1.4.1**
  - Detected: Action buttons use only red vs green to distinguish, no icon or text label
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Complex table with merged cells and no scope attributes on header cells
- ❌ **img-no-alt-description — WCAG 2.4.4, 1.1.1**
  - Detected: Link with only an image icon, but the image has no accessible name

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_056.html](pages/page_056.html)*
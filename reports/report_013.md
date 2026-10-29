# WCAG Test Page 013 — Accessibility Audit Report

**Page URL:** `pages/page_013.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 3
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 3
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 3
- **False positives:** 0

## Expected Violations

1. **Heading — WCAG 1.2.2, 1.2.4** ❌ Missing
   - Issue: Video has no captions track and no transcript provided
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

3. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input id='user' but label for='name' — form control not linked to label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.2.2, 1.2.4**
  - Detected: Video has no captions track and no transcript provided
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input id='user' but label for='name' — form control not linked to label

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_013.html](pages/page_013.html)*
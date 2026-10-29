# WCAG Test Page 084 — Accessibility Audit Report

**Page URL:** `pages/page_084.html`
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

1. **Image — WCAG 2.4.4, 1.1.1** ❌ Missing
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

2. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Form — WCAG 1.4.1** ❌ Missing
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

4. **Heading — WCAG 1.3.2** ❌ Missing
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **img-no-alt-description — WCAG 2.4.4, 1.1.1**
  - Detected: Link with only an image icon, but the image has no accessible name
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian
- ❌ **form-label-missing — WCAG 1.4.1**
  - Detected: Action buttons use only red vs green to distinguish, no icon or text label
- ❌ **heading-skip — WCAG 1.3.2**
  - Detected: Content order in HTML is different from visual order — screen reader reads in wrong order

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_084.html](pages/page_084.html)*
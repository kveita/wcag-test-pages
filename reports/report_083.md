# WCAG Test Page 083 — Accessibility Audit Report

**Page URL:** `pages/page_083.html`
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

1. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

3. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Photo of landscape with no alt text — screen reader has no fallback
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

4. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input field with no associated label or aria-label
- ❌ **img-no-alt-description — WCAG 1.1.1**
  - Detected: Photo of landscape with no alt text — screen reader has no fallback
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_083.html](pages/page_083.html)*
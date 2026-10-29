# WCAG Test Page 043 — Accessibility Audit Report

**Page URL:** `pages/page_043.html`
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

1. **Heading — WCAG 2.5.5** ❌ Missing
   - Issue: Large page with tiny in-page navigation links (under 44x44px)
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input placeholder replaces label — fails when placeholders are styled away
   - Fix: Add a visible label element in addition to the placeholder.

4. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.5.5**
  - Detected: Large page with tiny in-page navigation links (under 44x44px)
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings
- ❌ **form-placeholder-only — WCAG 1.1.1, 4.1.2**
  - Detected: Input placeholder replaces label — fails when placeholders are styled away
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Content that reads as a heading but uses <p> or <div> with bold styling

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_043.html](pages/page_043.html)*
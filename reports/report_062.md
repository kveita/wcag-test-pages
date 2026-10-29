# WCAG Test Page 062 — Accessibility Audit Report

**Page URL:** `pages/page_062.html`
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

1. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.4.4** ❌ Missing
   - Issue: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Use <thead>, <th> elements with proper scope attributes.

4. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Background parallax effect without reduced-motion media query support
- ❌ **heading-skip — WCAG 1.4.4**
  - Detected: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Complex table with merged cells and no scope attributes on header cells
- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_062.html](pages/page_062.html)*
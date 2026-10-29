# WCAG Test Page 010 — Accessibility Audit Report

**Page URL:** `pages/page_010.html`
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

1. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 2.4.7** ❌ Missing
   - Issue: Focus outline clipped or hidden by overflow: hidden on parent elements
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Use <thead>, <th> elements with proper scope attributes.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Background parallax effect without reduced-motion media query support
- ❌ **heading-skip — WCAG 2.4.7**
  - Detected: Focus outline clipped or hidden by overflow: hidden on parent elements
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Page jumps from h1 to h3, skipping h2
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Complex table with merged cells and no scope attributes on header cells

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_010.html](pages/page_010.html)*
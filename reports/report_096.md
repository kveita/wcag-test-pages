# WCAG Test Page 096 — Accessibility Audit Report

**Page URL:** `pages/page_096.html`
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

1. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Page has fixed width layout that breaks when user zooms to 200%
   - Fix: Remove fixed width or allow text wrapping.

2. **Color/Contrast — WCAG 2.3.1** ❌ Missing
   - Issue: Page flashes content rapidly (flashing colors) at frequencies > 2 Hz, risk of seizure
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

3. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **table-layout-fixed — WCAG 1.4.10**
  - Detected: Page has fixed width layout that breaks when user zooms to 200%
- ❌ **color-no-contrast — WCAG 2.3.1**
  - Detected: Page flashes content rapidly (flashing colors) at frequencies > 2 Hz, risk of seizure
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Content that reads as a heading but uses <p> or <div> with bold styling

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_096.html](pages/page_096.html)*
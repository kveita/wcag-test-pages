# WCAG Test Page 016 — Accessibility Audit Report

**Page URL:** `pages/page_016.html`
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

1. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

2. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Document has no lang attribute — screen reader may mispronounce content
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Light gray text on white background
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Heading — WCAG 2.5.5** ❌ Missing
   - Issue: Large page with tiny in-page navigation links (under 44x44px)
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Document has no lang attribute — screen reader may mispronounce content
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Light gray text on white background
- ❌ **heading-skip — WCAG 2.5.5**
  - Detected: Large page with tiny in-page navigation links (under 44x44px)

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_016.html](pages/page_016.html)*
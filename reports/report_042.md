# WCAG Test Page 042 — Accessibility Audit Report

**Page URL:** `pages/page_042.html`
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

1. **Heading — WCAG 2.5.5** ❌ Missing
   - Issue: Large page with tiny in-page navigation links (under 44x44px)
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 2.4.7, 1.4.11** ❌ Missing
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.5.5**
  - Detected: Large page with tiny in-page navigation links (under 44x44px)
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
- ❌ **color-no-contrast — WCAG 2.4.7, 1.4.11**
  - Detected: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_042.html](pages/page_042.html)*
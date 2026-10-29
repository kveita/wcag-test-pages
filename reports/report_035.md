# WCAG Test Page 035 — Accessibility Audit Report

**Page URL:** `pages/page_035.html`
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

1. **Text — WCAG 1.4.8** ❌ Missing
   - Issue: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
   - Fix: Use text-align: left or right instead of justify.

2. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 1.4.1** ❌ Missing
   - Issue: Error message indicated only by red color, no text indicator
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Scrolling — WCAG 2.1.1** ❌ Missing
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scrollable areas can be scrolled via keyboard.

## Detected Violations (Audit)

- ❌ **text-justified — WCAG 1.4.8**
  - Detected: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **color-no-contrast — WCAG 1.4.1**
  - Detected: Error message indicated only by red color, no text indicator
- ❌ **scroll-blocked — WCAG 2.1.1**
  - Detected: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_035.html](pages/page_035.html)*
# WCAG Test Page 050 — Accessibility Audit Report

**Page URL:** `pages/page_050.html`
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

1. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Light gray text on white background
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

2. **Scrolling — WCAG 2.1.1** ❌ Missing
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scrollable areas can be scrolled via keyboard.

3. **Color/Contrast — WCAG 2.4.7, 1.4.11** ❌ Missing
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Light gray text on white background
- ❌ **scroll-blocked — WCAG 2.1.1**
  - Detected: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
- ❌ **color-no-contrast — WCAG 2.4.7, 1.4.11**
  - Detected: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Line-height is set to 1.0 or 1 — tight line spacing reduces readability

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_050.html](pages/page_050.html)*
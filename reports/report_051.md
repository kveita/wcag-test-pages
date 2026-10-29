# WCAG Test Page 051 — Accessibility Audit Report

**Page URL:** `pages/page_051.html`
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
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

2. **Color/Contrast — WCAG 2.4.7, 1.4.11** ❌ Missing
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

3. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

5. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
- ❌ **color-no-contrast — WCAG 2.4.7, 1.4.11**
  - Detected: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_051.html](pages/page_051.html)*
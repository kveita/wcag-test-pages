# WCAG Test Page 012 — Accessibility Audit Report

**Page URL:** `pages/page_012.html`
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

1. **Image — WCAG 2.4.4, 1.1.1** ❌ Missing
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

2. **Color/Contrast — WCAG 2.4.7, 1.4.11** ❌ Missing
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

3. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Heading — WCAG 1.4.4** ❌ Missing
   - Issue: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **img-no-alt-description — WCAG 2.4.4, 1.1.1**
  - Detected: Link with only an image icon, but the image has no accessible name
- ❌ **color-no-contrast — WCAG 2.4.7, 1.4.11**
  - Detected: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Page jumps from h1 to h3, skipping h2
- ❌ **heading-skip — WCAG 1.4.4**
  - Detected: Browser zoom is disabled via CSS @media or viewport meta prevents zoom

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_012.html](pages/page_012.html)*
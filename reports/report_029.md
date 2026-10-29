# WCAG Test Page 029 — Accessibility Audit Report

**Page URL:** `pages/page_029.html`
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

1. **Color/Contrast — WCAG 2.3.1** ❌ Missing
   - Issue: Page flashes content rapidly (flashing colors) at frequencies > 2 Hz, risk of seizure
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

2. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input placeholder replaces label — fails when placeholders are styled away
   - Fix: Add a visible label element in addition to the placeholder.

3. **Heading — WCAG 1.2.2, 1.2.4** ❌ Missing
   - Issue: Video has no captions track and no transcript provided
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Scrolling — WCAG 2.1.1** ❌ Missing
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scrollable areas can be scrolled via keyboard.

## Detected Violations (Audit)

- ❌ **color-no-contrast — WCAG 2.3.1**
  - Detected: Page flashes content rapidly (flashing colors) at frequencies > 2 Hz, risk of seizure
- ❌ **form-placeholder-only — WCAG 1.1.1, 4.1.2**
  - Detected: Input placeholder replaces label — fails when placeholders are styled away
- ❌ **heading-skip — WCAG 1.2.2, 1.2.4**
  - Detected: Video has no captions track and no transcript provided
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: JavaScript widget responds to click but not to keyboard Enter/Space
- ❌ **scroll-blocked — WCAG 2.1.1**
  - Detected: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_029.html](pages/page_029.html)*
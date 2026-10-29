# WCAG Test Page 036 — Accessibility Audit Report

**Page URL:** `pages/page_036.html`
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

1. **Link — WCAG 2.4.4** ❌ Missing
   - Issue: Link text is just 'here' — contextless
   - Fix: Replace with descriptive text: 'Learn more about X'.

2. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Light gray text on white background
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Heading — WCAG 1.4.2** ❌ Missing
   - Issue: Background audio plays automatically on page load, no stop/pause button
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **link-placeholder — WCAG 2.4.4**
  - Detected: Link text is just 'here' — contextless
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: JavaScript widget responds to click but not to keyboard Enter/Space
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Light gray text on white background
- ❌ **heading-skip — WCAG 1.4.2**
  - Detected: Background audio plays automatically on page load, no stop/pause button
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_036.html](pages/page_036.html)*
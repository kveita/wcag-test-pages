# WCAG Test Page 087 — Accessibility Audit Report

**Page URL:** `pages/page_087.html`
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

1. **Text — WCAG 1.4.8** ❌ Missing
   - Issue: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
   - Fix: Use text-align: left or right instead of justify.

2. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

4. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Document has no lang attribute — screen reader may mispronounce content
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **text-justified — WCAG 1.4.8**
  - Detected: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Document has no lang attribute — screen reader may mispronounce content
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_087.html](pages/page_087.html)*
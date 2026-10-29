# WCAG Test Page 032 — Accessibility Audit Report

**Page URL:** `pages/page_032.html`
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

1. **Image — WCAG 2.4.4, 1.1.1** ❌ Missing
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

2. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Photo of landscape with no alt text — screen reader has no fallback
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

5. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use <thead>, <th> elements with proper scope attributes.

## Detected Violations (Audit)

- ❌ **img-no-alt-description — WCAG 2.4.4, 1.1.1**
  - Detected: Link with only an image icon, but the image has no accessible name
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support
- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **img-no-alt-description — WCAG 1.1.1**
  - Detected: Photo of landscape with no alt text — screen reader has no fallback
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Table uses layout= attribute or CSS that breaks column headers association

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_032.html](pages/page_032.html)*
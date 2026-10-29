# WCAG Test Page 092 — Accessibility Audit Report

**Page URL:** `pages/page_092.html`
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

1. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Letter spacing on body text exceeds 0.12em — harms readability for some users
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Letter spacing on body text exceeds 0.12em — harms readability for some users

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_092.html](pages/page_092.html)*
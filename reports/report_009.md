# WCAG Test Page 009 — Accessibility Audit Report

**Page URL:** `pages/page_009.html`
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

1. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Letter spacing on body text exceeds 0.12em — harms readability for some users
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.3.2** ❌ Missing
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Text — WCAG 1.4.8** ❌ Missing
   - Issue: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
   - Fix: Use text-align: left or right instead of justify.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Letter spacing on body text exceeds 0.12em — harms readability for some users
- ❌ **heading-skip — WCAG 1.3.2**
  - Detected: Content order in HTML is different from visual order — screen reader reads in wrong order
- ❌ **text-justified — WCAG 1.4.8**
  - Detected: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_009.html](pages/page_009.html)*
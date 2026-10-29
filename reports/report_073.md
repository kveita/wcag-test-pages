# WCAG Test Page 073 — Accessibility Audit Report

**Page URL:** `pages/page_073.html`
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

1. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use <thead>, <th> elements with proper scope attributes.

2. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add alt="" to indicate the image is decorative.

3. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

5. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Table uses layout= attribute or CSS that breaks column headers association
- ❌ **img-decorative-missing-alt — WCAG 1.1.1**
  - Detected: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Line-height is set to 1.0 or 1 — tight line spacing reduces readability

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_073.html](pages/page_073.html)*
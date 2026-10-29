# WCAG Test Page 069 — Accessibility Audit Report

**Page URL:** `pages/page_069.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 2
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 2
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 2
- **False positives:** 0

## Expected Violations

1. **Heading — WCAG 2.4.3** ❌ Missing
   - Issue: Focus order is non-linear — user tabs through navigation in an illogical order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.3.2** ❌ Missing
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.4.3**
  - Detected: Focus order is non-linear — user tabs through navigation in an illogical order
- ❌ **heading-skip — WCAG 1.3.2**
  - Detected: Content order in HTML is different from visual order — screen reader reads in wrong order

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_069.html](pages/page_069.html)*
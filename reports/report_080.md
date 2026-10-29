# WCAG Test Page 080 — Accessibility Audit Report

**Page URL:** `pages/page_080.html`
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

1. **Link — WCAG 2.4.4** ❌ Missing
   - Issue: Link text is just 'here' — contextless
   - Fix: Replace with descriptive text: 'Learn more about X'.

2. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Page has fixed width layout that breaks when user zooms to 200%
   - Fix: Remove fixed width or allow text wrapping.

## Detected Violations (Audit)

- ❌ **link-placeholder — WCAG 2.4.4**
  - Detected: Link text is just 'here' — contextless
- ❌ **table-layout-fixed — WCAG 1.4.10**
  - Detected: Page has fixed width layout that breaks when user zooms to 200%

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_080.html](pages/page_080.html)*
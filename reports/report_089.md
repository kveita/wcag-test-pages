# WCAG Test Page 089 — Accessibility Audit Report

**Page URL:** `pages/page_089.html`
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

1. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use <thead>, <th> elements with proper scope attributes.

2. **ARIA — WCAG 4.1.3** ❌ Missing
   - Issue: Live region has aria-hidden='true' applied, preventing screen reader announcements
   - Fix: Remove aria-hidden from the live region container.

## Detected Violations (Audit)

- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Table uses layout= attribute or CSS that breaks column headers association
- ❌ **aria-hidden-live — WCAG 4.1.3**
  - Detected: Live region has aria-hidden='true' applied, preventing screen reader announcements

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_089.html](pages/page_089.html)*
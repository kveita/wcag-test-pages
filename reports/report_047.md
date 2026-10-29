# WCAG Test Page 047 — Accessibility Audit Report

**Page URL:** `pages/page_047.html`
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

1. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Light gray text on white background
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

2. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input placeholder replaces label — fails when placeholders are styled away
   - Fix: Add a visible label element in addition to the placeholder.

## Detected Violations (Audit)

- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Light gray text on white background
- ❌ **form-placeholder-only — WCAG 1.1.1, 4.1.2**
  - Detected: Input placeholder replaces label — fails when placeholders are styled away

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_047.html](pages/page_047.html)*
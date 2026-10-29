# WCAG Test Page 021 — Accessibility Audit Report

**Page URL:** `pages/page_021.html`
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

1. **Heading — WCAG 1.4.4** ❌ Missing
   - Issue: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **ARIA — WCAG 4.1.3** ❌ Missing
   - Issue: aria-live region updates but total announcements exceed live region limits without wrapping
   - Fix: Remove aria-hidden from the live region container.

3. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.4.4**
  - Detected: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
- ❌ **aria-hidden-live — WCAG 4.1.3**
  - Detected: aria-live region updates but total announcements exceed live region limits without wrapping
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_021.html](pages/page_021.html)*
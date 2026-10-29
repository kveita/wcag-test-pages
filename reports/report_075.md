# WCAG Test Page 075 — Accessibility Audit Report

**Page URL:** `pages/page_075.html`
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

1. **Heading — WCAG 2.5.2** ❌ Missing
   - Issue: Moving carousels shift focus without user request
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add alt="" to indicate the image is decorative.

3. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Photo of landscape with no alt text — screen reader has no fallback
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.5.2**
  - Detected: Moving carousels shift focus without user request
- ❌ **img-decorative-missing-alt — WCAG 1.1.1**
  - Detected: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
- ❌ **img-no-alt-description — WCAG 1.1.1**
  - Detected: Photo of landscape with no alt text — screen reader has no fallback

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_075.html](pages/page_075.html)*
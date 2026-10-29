# WCAG Test Page 038 — Accessibility Audit Report

**Page URL:** `pages/page_038.html`
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

1. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add alt="" to indicate the image is decorative.

2. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Form — WCAG 1.4.1** ❌ Missing
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

4. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

## Detected Violations (Audit)

- ❌ **img-decorative-missing-alt — WCAG 1.1.1**
  - Detected: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support
- ❌ **form-label-missing — WCAG 1.4.1**
  - Detected: Action buttons use only red vs green to distinguish, no icon or text label
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Background parallax effect without reduced-motion media query support
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input field with no associated label or aria-label

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_038.html](pages/page_038.html)*
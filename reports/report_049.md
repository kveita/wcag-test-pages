# WCAG Test Page 049 — Accessibility Audit Report

**Page URL:** `pages/page_049.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 4
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 4
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 4
- **False positives:** 0

## Expected Violations

1. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Form — WCAG 1.1.1** ❌ Missing
   - Issue: Element has role='img' but contains only decorative text, no aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

3. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add alt="" to indicate the image is decorative.

4. **Scrolling — WCAG 2.1.1** ❌ Missing
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scrollable areas can be scrolled via keyboard.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: Animated GIF/video plays without user control and without reduced-motion support
- ❌ **form-label-missing — WCAG 1.1.1**
  - Detected: Element has role='img' but contains only decorative text, no aria-label
- ❌ **img-decorative-missing-alt — WCAG 1.1.1**
  - Detected: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
- ❌ **scroll-blocked — WCAG 2.1.1**
  - Detected: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_049.html](pages/page_049.html)*
# WCAG Test Page 064 — Accessibility Audit Report

**Page URL:** `pages/page_064.html`
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

1. **Media — WCAG 1.4.2** ❌ Missing
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Remove autoplay or provide a prominent pause control.

2. **Heading — WCAG 2.4.3** ❌ Missing
   - Issue: Focus order is non-linear — user tabs through navigation in an illogical order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Heading — WCAG 4.1.3** ❌ Missing
   - Issue: Live region announcement is too brief for screen reader users to process
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Heading — WCAG 1.3.2** ❌ Missing
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input id='user' but label for='name' — form control not linked to label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

## Detected Violations (Audit)

- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped
- ❌ **heading-skip — WCAG 2.4.3**
  - Detected: Focus order is non-linear — user tabs through navigation in an illogical order
- ❌ **heading-skip — WCAG 4.1.3**
  - Detected: Live region announcement is too brief for screen reader users to process
- ❌ **heading-skip — WCAG 1.3.2**
  - Detected: Content order in HTML is different from visual order — screen reader reads in wrong order
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input id='user' but label for='name' — form control not linked to label

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_064.html](pages/page_064.html)*
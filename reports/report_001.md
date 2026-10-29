# WCAG Test Page 001 — Accessibility Audit Report

**Page URL:** `pages/page_001.html`
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

1. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

2. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

3. **Form — WCAG 1.4.1** ❌ Missing
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

4. **Heading — WCAG 2.5.5** ❌ Missing
   - Issue: Large page with tiny in-page navigation links (under 44x44px)
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Media — WCAG 1.4.2** ❌ Missing
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Remove autoplay or provide a prominent pause control.

## Detected Violations (Audit)

- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability
- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input field with no associated label or aria-label
- ❌ **form-label-missing — WCAG 1.4.1**
  - Detected: Action buttons use only red vs green to distinguish, no icon or text label
- ❌ **heading-skip — WCAG 2.5.5**
  - Detected: Large page with tiny in-page navigation links (under 44x44px)
- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_001.html](pages/page_001.html)*
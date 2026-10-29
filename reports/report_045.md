# WCAG Test Page 045 — Accessibility Audit Report

**Page URL:** `pages/page_045.html`
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

1. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

2. **Media — WCAG 1.4.2** ❌ Missing
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Remove autoplay or provide a prominent pause control.

3. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use <thead>, <th> elements with proper scope attributes.

4. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **form-label-missing — WCAG 1.1.1, 4.1.2**
  - Detected: Input field with no associated label or aria-label
- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Table uses layout= attribute or CSS that breaks column headers association
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Content that reads as a heading but uses <p> or <div> with bold styling

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_045.html](pages/page_045.html)*
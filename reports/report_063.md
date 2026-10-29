# WCAG Test Page 063 — Accessibility Audit Report

**Page URL:** `pages/page_063.html`
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

2. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **ARIA — WCAG 4.1.3** ❌ Missing
   - Issue: Live region has aria-hidden='true' applied, preventing screen reader announcements
   - Fix: Remove aria-hidden from the live region container.

4. **Form — WCAG 1.1.1** ❌ Missing
   - Issue: Element has role='img' but contains only decorative text, no aria-label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

5. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Page jumps from h1 to h3, skipping h2
- ❌ **aria-hidden-live — WCAG 4.1.3**
  - Detected: Live region has aria-hidden='true' applied, preventing screen reader announcements
- ❌ **form-label-missing — WCAG 1.1.1**
  - Detected: Element has role='img' but contains only decorative text, no aria-label
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_063.html](pages/page_063.html)*
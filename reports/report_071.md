# WCAG Test Page 071 — Accessibility Audit Report

**Page URL:** `pages/page_071.html`
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

1. **Form — WCAG 1.4.1** ❌ Missing
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add <label for='input-id'>Label text</label> or aria-label='Label'.

2. **Heading — WCAG 2.1.2** ❌ Missing
   - Issue: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **form-label-missing — WCAG 1.4.1**
  - Detected: Action buttons use only red vs green to distinguish, no icon or text label
- ❌ **heading-skip — WCAG 2.1.2**
  - Detected: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_071.html](pages/page_071.html)*
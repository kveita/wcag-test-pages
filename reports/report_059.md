# WCAG Test Page 059 — Accessibility Audit Report

**Page URL:** `pages/page_059.html`
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

1. **ARIA — WCAG 4.1.3** ❌ Missing
   - Issue: Live region has aria-hidden='true' applied, preventing screen reader announcements
   - Fix: Remove aria-hidden from the live region container.

2. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

4. **Image — WCAG 2.4.4, 1.1.1** ❌ Missing
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Provide descriptive alt text: alt="A clear description of the image".

5. **Image — WCAG 1.1.1** ❌ Missing
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add alt="" to indicate the image is decorative.

## Detected Violations (Audit)

- ❌ **aria-hidden-live — WCAG 4.1.3**
  - Detected: Live region has aria-hidden='true' applied, preventing screen reader announcements
- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian
- ❌ **img-no-alt-description — WCAG 2.4.4, 1.1.1**
  - Detected: Link with only an image icon, but the image has no accessible name
- ❌ **img-decorative-missing-alt — WCAG 1.1.1**
  - Detected: Decorative image with empty alt but aria-label also empty — screen readers announce nothing

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_059.html](pages/page_059.html)*
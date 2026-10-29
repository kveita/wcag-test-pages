# WCAG Test Page 006 — Accessibility Audit Report

**Page URL:** `pages/page_006.html`
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

1. **Heading — WCAG 2.4.7** ❌ Missing
   - Issue: Focus outline clipped or hidden by overflow: hidden on parent elements
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Media — WCAG 1.4.2** ❌ Missing
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Remove autoplay or provide a prominent pause control.

3. **Heading — WCAG 2.4.3** ❌ Missing
   - Issue: Focus order is non-linear — user tabs through navigation in an illogical order
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.4.7**
  - Detected: Focus outline clipped or hidden by overflow: hidden on parent elements
- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped
- ❌ **heading-skip — WCAG 2.4.3**
  - Detected: Focus order is non-linear — user tabs through navigation in an illogical order

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_006.html](pages/page_006.html)*
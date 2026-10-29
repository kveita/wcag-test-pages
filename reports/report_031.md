# WCAG Test Page 031 — Accessibility Audit Report

**Page URL:** `pages/page_031.html`
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

1. **Heading — WCAG 2.1.2** ❌ Missing
   - Issue: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Media — WCAG 1.4.2** ❌ Missing
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Remove autoplay or provide a prominent pause control.

3. **Color/Contrast — WCAG 1.4.3, 1.4.6** ❌ Missing
   - Issue: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.1.2**
  - Detected: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
- ❌ **audio-autoplay — WCAG 1.4.2**
  - Detected: Autoplayed sound is purely decorative but cannot be stopped
- ❌ **color-no-contrast — WCAG 1.4.3, 1.4.6**
  - Detected: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_031.html](pages/page_031.html)*
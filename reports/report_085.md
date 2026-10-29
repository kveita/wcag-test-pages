# WCAG Test Page 085 — Accessibility Audit Report

**Page URL:** `pages/page_085.html`
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

1. **Heading — WCAG 1.2.2, 1.2.4** ❌ Missing
   - Issue: Video has no captions track and no transcript provided
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.3.1, 2.4.6** ❌ Missing
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Form — WCAG 1.1.1, 4.1.2** ❌ Missing
   - Issue: Input placeholder replaces label — fails when placeholders are styled away
   - Fix: Add a visible label element in addition to the placeholder.

4. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Color/Contrast — WCAG 2.4.7, 1.4.11** ❌ Missing
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Increase text contrast; use dark text on light backgrounds or vice versa.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.2.2, 1.2.4**
  - Detected: Video has no captions track and no transcript provided
- ❌ **heading-skip — WCAG 1.3.1, 2.4.6**
  - Detected: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
- ❌ **form-placeholder-only — WCAG 1.1.1, 4.1.2**
  - Detected: Input placeholder replaces label — fails when placeholders are styled away
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Page jumps from h1 to h3, skipping h2
- ❌ **color-no-contrast — WCAG 2.4.7, 1.4.11**
  - Detected: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_085.html](pages/page_085.html)*
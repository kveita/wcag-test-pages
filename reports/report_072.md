# WCAG Test Page 072 — Accessibility Audit Report

**Page URL:** `pages/page_072.html`
**Run Date:** 2026-10-29T02:47:49Z
**Total Expected Violations:** 2
**Total Detected Violations:** 0
**WCAG 2.2 Level:** AAA

## Summary

- **Expected violations:** 2
- **Detected (found by audit):** 0
- **Missing (expected but not found):** 2
- **False positives:** 0

## Expected Violations

1. **Heading — WCAG 1.4.12** ❌ Missing
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 2.1.1** ❌ Missing
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
- ❌ **heading-skip — WCAG 2.1.1**
  - Detected: JavaScript widget responds to click but not to keyboard Enter/Space

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_072.html](pages/page_072.html)*
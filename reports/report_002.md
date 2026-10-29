# WCAG Test Page 002 — Accessibility Audit Report

**Page URL:** `pages/page_002.html`
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

1. **Heading — WCAG 2.4.7** ❌ Missing
   - Issue: Focus outline clipped or hidden by overflow: hidden on parent elements
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Table — WCAG 1.3.1** ❌ Missing
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Use <thead>, <th> elements with proper scope attributes.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 2.4.7**
  - Detected: Focus outline clipped or hidden by overflow: hidden on parent elements
- ❌ **table-layout — WCAG 1.3.1**
  - Detected: Complex table with merged cells and no scope attributes on header cells

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_002.html](pages/page_002.html)*
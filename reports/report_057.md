# WCAG Test Page 057 — Accessibility Audit Report

**Page URL:** `pages/page_057.html`
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
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 1.4.12**
  - Detected: Sticky header overlays content when scrolling, partially obscuring the page headings
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Content that reads as a heading but uses <p> or <div> with bold styling

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_057.html](pages/page_057.html)*
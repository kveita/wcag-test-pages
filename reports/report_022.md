# WCAG Test Page 022 — Accessibility Audit Report

**Page URL:** `pages/page_022.html`
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

1. **Link — WCAG 2.4.4** ❌ Missing
   - Issue: Link text is just 'here' — contextless
   - Fix: Replace with descriptive text: 'Learn more about X'.

2. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

3. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

## Detected Violations (Audit)

- ❌ **link-placeholder — WCAG 2.4.4**
  - Detected: Link text is just 'here' — contextless
- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Page jumps from h1 to h3, skipping h2

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_022.html](pages/page_022.html)*
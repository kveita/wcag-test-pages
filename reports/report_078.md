# WCAG Test Page 078 — Accessibility Audit Report

**Page URL:** `pages/page_078.html`
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

1. **Heading — WCAG 3.1.1** ❌ Missing
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

2. **Heading — WCAG 1.4.2** ❌ Missing
   - Issue: Background audio plays automatically on page load, no stop/pause button
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

3. **Link — WCAG 2.4.4** ❌ Missing
   - Issue: Link text is just 'here' — contextless
   - Fix: Replace with descriptive text: 'Learn more about X'.

4. **Heading — WCAG 1.3.1** ❌ Missing
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Restructure to use sequential heading levels: h1 → h2 → h3, etc.

5. **Table — WCAG 1.4.10** ❌ Missing
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Use <thead>, <th> elements with proper scope attributes.

## Detected Violations (Audit)

- ❌ **heading-skip — WCAG 3.1.1**
  - Detected: Partial lang attribute like lang='en-US' but page is actually Norwegian
- ❌ **heading-skip — WCAG 1.4.2**
  - Detected: Background audio plays automatically on page load, no stop/pause button
- ❌ **link-placeholder — WCAG 2.4.4**
  - Detected: Link text is just 'here' — contextless
- ❌ **heading-skip — WCAG 1.3.1**
  - Detected: Content that reads as a heading but uses <p> or <div> with bold styling
- ❌ **table-layout — WCAG 1.4.10**
  - Detected: Table has width='100%' and content is squished, breaking readability

## Recommendations

- Fix all 0 detected violations
- Consider adding skip links and proper heading hierarchy
- Ensure all form controls have associated labels
- Add alt text to all images
- Test with screen readers like NVDA or VoiceOver

*Audit run: 2026-10-29T02:47:49Z*
*Page: [pages/page_078.html](pages/page_078.html)*
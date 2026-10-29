# WCAG Test Page 78 — Accessibility Audit Report

**Page URL:** `pages/page_078.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Language — WCAG 3.1.1**
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Set the correct language: lang='no'.
2. **Media — WCAG 1.4.2**
   - Issue: Background audio plays automatically on page load, no stop/pause button
   - Fix: Remove autoplay or add a prominent pause control.
3. **Link — WCAG 2.4.4**
   - Issue: Link text is just 'here' — contextless
   - Fix: Use descriptive text: 'Read the spring gardening guide'.
4. **Heading — WCAG 1.3.1**
   - Issue: Content that reads as a heading but uses <p> or <div> with bold styling
   - Fix: Use <h2> for section headers.
5. **Table — WCAG 1.4.10**
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Remove fixed width or allow content wrapping.

## General Recommendations

- Ensure all text meets minimum contrast ratios (4.5:1 for normal text, 7:1 for large text)
- Use semantic HTML elements (h1-h6, main, nav, aside, section) for proper document structure
- Provide text alternatives for all non-text content (images, icons, charts)
- Make all form controls keyboard accessible with visible focus indicators
- Respect user preferences for reduced motion
- Ensure language attributes are set on the HTML element
- Provide skip links for keyboard users to bypass repeated content
- Use ARIA only when native HTML cannot achieve the same result

---
*Generated for testing wcag-skill and accessibility auditing tools.*

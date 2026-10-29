# WCAG Test Page 73 — Accessibility Audit Report

**Page URL:** `pages/page_073.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Table — WCAG 1.3.1**
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use proper <thead> <th> elements for data tables.
2. **Image — WCAG 1.1.1**
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add empty alt='' (alt empty string for decorative).
3. **Heading — WCAG 1.3.1, 2.4.6**
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure headings so each h2 is preceded by an h1 and levels increment by one.
4. **Table — WCAG 1.4.10**
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Remove fixed width or allow content wrapping.
5. **Text — WCAG 1.4.12**
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Set line-height to at least 1.5.

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

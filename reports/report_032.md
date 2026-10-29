# WCAG Test Page 32 — Accessibility Audit Report

**Page URL:** `pages/page_032.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Link — WCAG 2.4.4, 1.1.1**
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Add aria-label='Read more about spring gardening'.
2. **Motion — WCAG 2.1.1**
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Add a pause button and respect prefers-reduced-motion.
3. **Heading — WCAG 1.3.1, 2.4.6**
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure headings so each h2 is preceded by an h1 and levels increment by one.
4. **Image — WCAG 1.1.1**
   - Issue: Photo of landscape with no alt text — screen reader has no fallback
   - Fix: Provide descriptive alt='Lush green mountain valley with river'.
5. **Table — WCAG 1.3.1**
   - Issue: Table uses layout= attribute or CSS that breaks column headers association
   - Fix: Use proper <thead> <th> elements for data tables.

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

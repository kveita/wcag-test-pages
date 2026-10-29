# WCAG Test Page 92 — Accessibility Audit Report

**Page URL:** `pages/page_092.html`
**Total Violations Found:** 3
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 3 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Heading — WCAG 1.3.1, 2.4.6**
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure headings so each h2 is preceded by an h1 and levels increment by one.
2. **Motion — WCAG 2.1.1**
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Add a pause button and respect prefers-reduced-motion.
3. **Text — WCAG 1.4.12**
   - Issue: Letter spacing on body text exceeds 0.12em — harms readability for some users
   - Fix: Keep letter-spacing between -0.05em and 0.12em.

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

# WCAG Test Page 25 — Accessibility Audit Report

**Page URL:** `pages/page_025.html`
**Total Violations Found:** 3
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 3 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Link — WCAG 2.4.4**
   - Issue: Link text is just 'here' — contextless
   - Fix: Use descriptive text: 'Read the spring gardening guide'.
2. **Layout — WCAG 1.4.10**
   - Issue: Page has fixed width layout that breaks when user zooms to 200%
   - Fix: Use fluid/percentage widths.
3. **Heading — WCAG 1.3.1**
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Use proper sequential heading levels.

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

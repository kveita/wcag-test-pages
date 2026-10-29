# WCAG Test Page 3 — Accessibility Audit Report

**Page URL:** `pages/page_003.html`
**Total Violations Found:** 2
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 2 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Color/Contrast — WCAG 1.4.3, 1.4.6**
   - Issue: Light gray text on white background
   - Fix: Darken to #333333 or use #3498db.
2. **ARIA — WCAG 4.1.3**
   - Issue: Live region has aria-hidden='true' applied, preventing screen reader announcements
   - Fix: Remove aria-hidden from the live region container.

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

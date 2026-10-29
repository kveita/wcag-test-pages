# WCAG Test Page 34 — Accessibility Audit Report

**Page URL:** `pages/page_034.html`
**Total Violations Found:** 4
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 4 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Color/Contrast — WCAG 1.4.3, 1.4.6**
   - Issue: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1
   - Fix: Use #3498db for text on the #e74c3c background.
2. **Link — WCAG 2.1.1, 4.1.2**
   - Issue: Link with href='#' has no destination
   - Fix: Remove href='#' or use a real anchor.
3. **Script — WCAG 2.4.3**
   - Issue: Focus order is non-linear — user tabs through navigation in an illogical order
   - Fix: Ensure tab order matches visual reading order.
4. **Text — WCAG 1.4.3, 1.4.6**
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase to 16px minimum or use #333 for 14px text.

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

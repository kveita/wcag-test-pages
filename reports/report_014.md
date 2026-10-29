# WCAG Test Page 14 — Accessibility Audit Report

**Page URL:** `pages/page_014.html`
**Total Violations Found:** 4
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 4 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Form — WCAG 1.1.1, 4.1.2**
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label> or aria-label='Search products'.
2. **Image — WCAG 1.1.1**
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add empty alt='' (alt empty string for decorative).
3. **Script — WCAG 2.4.3**
   - Issue: Focus order is non-linear — user tabs through navigation in an illogical order
   - Fix: Ensure tab order matches visual reading order.
4. **Media — WCAG 1.4.2**
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Stop the sound or let users disable it.

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

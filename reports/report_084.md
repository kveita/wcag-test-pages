# WCAG Test Page 84 — Accessibility Audit Report

**Page URL:** `pages/page_084.html`
**Total Violations Found:** 4
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 4 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Link — WCAG 2.4.4, 1.1.1**
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Add aria-label='Read more about spring gardening'.
2. **Language — WCAG 3.1.1**
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Set the correct language: lang='no'.
3. **Color-Only — WCAG 1.4.1**
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add text labels like 'Delete'/'Save' or icons alongside colors.
4. **Screen Reader — WCAG 1.3.2**
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Reorder DOM elements so focus order matches visual reading order.

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

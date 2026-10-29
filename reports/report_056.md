# WCAG Test Page 56 — Accessibility Audit Report

**Page URL:** `pages/page_056.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Layout — WCAG 1.4.10**
   - Issue: Page has fixed width layout that breaks when user zooms to 200%
   - Fix: Use fluid/percentage widths.
2. **ARIA — WCAG 4.1.3**
   - Issue: aria-live region updates but total announcements exceed live region limits without wrapping
   - Fix: Use aria-busy='true' on parent and manage updates with live regions properly.
3. **Color-Only — WCAG 1.4.1**
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add text labels like 'Delete'/'Save' or icons alongside colors.
4. **Table — WCAG 1.3.1**
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Add scope='col'/'row' to all th elements.
5. **Link — WCAG 2.4.4, 1.1.1**
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Add aria-label='Read more about spring gardening'.

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

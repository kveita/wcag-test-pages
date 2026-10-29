# WCAG Test Page 59 — Accessibility Audit Report

**Page URL:** `pages/page_059.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **ARIA — WCAG 4.1.3**
   - Issue: Live region has aria-hidden='true' applied, preventing screen reader announcements
   - Fix: Remove aria-hidden from the live region container.
2. **Text — WCAG 1.4.12**
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Set line-height to at least 1.5.
3. **Language — WCAG 3.1.1**
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Set the correct language: lang='no'.
4. **Link — WCAG 2.4.4, 1.1.1**
   - Issue: Link with only an image icon, but the image has no accessible name
   - Fix: Add aria-label='Read more about spring gardening'.
5. **Image — WCAG 1.1.1**
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add empty alt='' (alt empty string for decorative).

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

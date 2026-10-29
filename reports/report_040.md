# WCAG Test Page 40 — Accessibility Audit Report

**Page URL:** `pages/page_040.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Link — WCAG 2.1.1, 4.1.2**
   - Issue: Link with href='#' has no destination
   - Fix: Remove href='#' or use a real anchor.
2. **Image — WCAG 1.1.1**
   - Issue: Image alt='image' — meaningless to screen reader users
   - Fix: Use descriptive alt or add aria-label.
3. **Script — WCAG 2.1.1**
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Add keydown handler for Enter and Space keys.
4. **Motion — WCAG 2.1.1**
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Add @media (prefers-reduced-motion: reduce) { .parallax { transform: none !important; } }.
5. **Script — WCAG 2.5.2**
   - Issue: Moving carousels shift focus without user request
   - Fix: Avoid auto-advancing carousels, or let user control when to move.

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

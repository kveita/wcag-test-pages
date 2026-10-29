# WCAG Test Page 38 — Accessibility Audit Report

**Page URL:** `pages/page_038.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Image — WCAG 1.1.1**
   - Issue: Decorative image with empty alt but aria-label also empty — screen readers announce nothing
   - Fix: Add empty alt='' (alt empty string for decorative).
2. **Motion — WCAG 2.1.1**
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Add a pause button and respect prefers-reduced-motion.
3. **Color-Only — WCAG 1.4.1**
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add text labels like 'Delete'/'Save' or icons alongside colors.
4. **Motion — WCAG 2.1.1**
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Add @media (prefers-reduced-motion: reduce) { .parallax { transform: none !important; } }.
5. **Form — WCAG 1.1.1, 4.1.2**
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label> or aria-label='Search products'.

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

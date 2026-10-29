# WCAG Test Page 83 — Accessibility Audit Report

**Page URL:** `pages/page_083.html`
**Total Violations Found:** 4
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 4 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Scrolling — WCAG 1.4.12**
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Make sticky headers collapsible or reduce height.
2. **Form — WCAG 1.1.1, 4.1.2**
   - Issue: Input field with no associated label or aria-label
   - Fix: Add <label> or aria-label='Search products'.
3. **Image — WCAG 1.1.1**
   - Issue: Photo of landscape with no alt text — screen reader has no fallback
   - Fix: Provide descriptive alt='Lush green mountain valley with river'.
4. **Motion — WCAG 2.1.1**
   - Issue: Animated GIF/video plays without user control and without reduced-motion support
   - Fix: Add a pause button and respect prefers-reduced-motion.

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

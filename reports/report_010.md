# WCAG Test Page 10 — Accessibility Audit Report

**Page URL:** `pages/page_010.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Motion — WCAG 2.1.1**
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Add @media (prefers-reduced-motion: reduce) { .parallax { transform: none !important; } }.
2. **Layout — WCAG 2.4.7**
   - Issue: Focus outline clipped or hidden by overflow: hidden on parent elements
   - Fix: Ensure focus is not clipped by overflow: hidden.
3. **Text — WCAG 1.4.3, 1.4.6**
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase to 16px minimum or use #333 for 14px text.
4. **Heading — WCAG 1.3.1**
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Use proper sequential heading levels.
5. **Table — WCAG 1.3.1**
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Add scope='col'/'row' to all th elements.

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

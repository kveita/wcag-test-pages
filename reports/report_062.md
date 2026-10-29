# WCAG Test Page 62 — Accessibility Audit Report

**Page URL:** `pages/page_062.html`
**Total Violations Found:** 4
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 4 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Motion — WCAG 2.1.1**
   - Issue: Background parallax effect without reduced-motion media query support
   - Fix: Add @media (prefers-reduced-motion: reduce) { .parallax { transform: none !important; } }.
2. **Layout — WCAG 1.4.4**
   - Issue: Browser zoom is disabled via CSS @media or viewport meta prevents zoom
   - Fix: Remove user-scalable=no or minimum-scale 1.0.
3. **Table — WCAG 1.3.1**
   - Issue: Complex table with merged cells and no scope attributes on header cells
   - Fix: Add scope='col'/'row' to all th elements.
4. **Table — WCAG 1.4.10**
   - Issue: Table has width='100%' and content is squished, breaking readability
   - Fix: Remove fixed width or allow content wrapping.

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

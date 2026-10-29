# WCAG Test Page 50 — Accessibility Audit Report

**Page URL:** `pages/page_050.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Color/Contrast — WCAG 1.4.3, 1.4.6**
   - Issue: Light gray text on white background
   - Fix: Darken to #333333 or use #3498db.
2. **Scrolling — WCAG 2.1.1**
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scroll containers can be scrolled via keyboard.
3. **Keyboard — WCAG 2.4.7, 1.4.11**
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Ensure visible focus ring has 3:1+ contrast ratio.
4. **Scrolling — WCAG 1.4.12**
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Make sticky headers collapsible or reduce height.
5. **Text — WCAG 1.4.12**
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Set line-height to at least 1.5.

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

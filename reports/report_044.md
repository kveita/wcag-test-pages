# WCAG Test Page 44 — Accessibility Audit Report

**Page URL:** `pages/page_044.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Motion — WCAG 2.3.1**
   - Issue: Page flashes content rapidly (flashing colors) at frequencies > 2 Hz, risk of seizure
   - Fix: Remove the flash pattern or slow it to < 2 Hz.
2. **Text — WCAG 1.4.12**
   - Issue: Line-height is set to 1.0 or 1 — tight line spacing reduces readability
   - Fix: Set line-height to at least 1.5.
3. **Scrolling — WCAG 2.1.1**
   - Issue: Page contains horizontally scrolling content that cannot be scrolled via keyboard (scroll container with overflow-x but no keyboard scroll buttons)
   - Fix: Ensure all scroll containers can be scrolled via keyboard.
4. **Text — WCAG 1.4.8**
   - Issue: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
   - Fix: Use text-align: left or right instead of justify.
5. **Screen Reader — WCAG 1.1.1**
   - Issue: Element has role='img' but contains only decorative text, no aria-label
   - Fix: Remove role='img' or add an accessible name.

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

# WCAG Test Page 7 — Accessibility Audit Report

**Page URL:** `pages/page_007.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Script — WCAG 2.1.1**
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Add keydown handler for Enter and Space keys.
2. **Keyboard — WCAG 2.1.2**
   - Issue: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
   - Fix: Add a 'close' or 'escape' handler that returns focus to the trigger element.
3. **Screen Reader — WCAG 1.3.2**
   - Issue: Content order in HTML is different from visual order — screen reader reads in wrong order
   - Fix: Reorder DOM elements so focus order matches visual reading order.
4. **Form — WCAG 1.1.1, 4.1.2**
   - Issue: Input id='user' but label for='name' — form control not linked to label
   - Fix: Match label for with input id='user'.
5. **Keyboard — WCAG 2.4.7, 1.4.11**
   - Issue: Focus indicator is visible only via outline but has outline: none and replaces with background color that fails 3:1 contrast
   - Fix: Ensure visible focus ring has 3:1+ contrast ratio.

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

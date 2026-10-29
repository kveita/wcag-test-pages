# WCAG Test Page 36 — Accessibility Audit Report

**Page URL:** `pages/page_036.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Link — WCAG 2.4.4**
   - Issue: Link text is just 'here' — contextless
   - Fix: Use descriptive text: 'Read the spring gardening guide'.
2. **Script — WCAG 2.1.1**
   - Issue: JavaScript widget responds to click but not to keyboard Enter/Space
   - Fix: Add keydown handler for Enter and Space keys.
3. **Color/Contrast — WCAG 1.4.3, 1.4.6**
   - Issue: Light gray text on white background
   - Fix: Darken to #333333 or use #3498db.
4. **Media — WCAG 1.4.2**
   - Issue: Background audio plays automatically on page load, no stop/pause button
   - Fix: Remove autoplay or add a prominent pause control.
5. **Motion — WCAG 2.1.1**
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

# WCAG Test Page 87 — Accessibility Audit Report

**Page URL:** `pages/page_087.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Text — WCAG 1.4.8**
   - Issue: Text is justified with letter-spacing changes, breaking word boundaries for users with dyslexia
   - Fix: Use text-align: left or right instead of justify.
2. **Scrolling — WCAG 1.4.12**
   - Issue: Sticky header overlays content when scrolling, partially obscuring the page headings
   - Fix: Make sticky headers collapsible or reduce height.
3. **Text — WCAG 1.4.3, 1.4.6**
   - Issue: Body text is 11px with #666 color — contrast ratio 3.8:1, fails 4.5:1
   - Fix: Increase to 16px minimum or use #333 for 14px text.
4. **Language — WCAG 3.1.1**
   - Issue: Document has no lang attribute — screen reader may mispronounce content
   - Fix: Add lang='en' (or appropriate language) to <html>.
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

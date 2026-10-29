# WCAG Test Page 71 — Accessibility Audit Report

**Page URL:** `pages/page_071.html`
**Total Violations Found:** 3
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 3 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Color-Only — WCAG 1.4.1**
   - Issue: Action buttons use only red vs green to distinguish, no icon or text label
   - Fix: Add text labels like 'Delete'/'Save' or icons alongside colors.
2. **Keyboard — WCAG 2.1.2**
   - Issue: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
   - Fix: Add a 'close' or 'escape' handler that returns focus to the trigger element.
3. **Language — WCAG 3.1.1**
   - Issue: Partial lang attribute like lang='en-US' but page is actually Norwegian
   - Fix: Set the correct language: lang='no'.

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

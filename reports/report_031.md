# WCAG Test Page 31 — Accessibility Audit Report

**Page URL:** `pages/page_031.html`
**Total Violations Found:** 3
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 3 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Keyboard — WCAG 2.1.2**
   - Issue: Focus can be trapped in a modal or overlay — no way to return focus to the trigger element
   - Fix: Add a 'close' or 'escape' handler that returns focus to the trigger element.
2. **Media — WCAG 1.4.2**
   - Issue: Autoplayed sound is purely decorative but cannot be stopped
   - Fix: Stop the sound or let users disable it.
3. **Color/Contrast — WCAG 1.4.3, 1.4.6**
   - Issue: Red text (#e74c3c) on red background (#e74c3c) — ratio 1:1, fails 4.5:1
   - Fix: Use #3498db for text on the #e74c3c background.

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

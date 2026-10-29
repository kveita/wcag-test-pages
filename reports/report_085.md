# WCAG Test Page 85 — Accessibility Audit Report

**Page URL:** `pages/page_085.html`
**Total Violations Found:** 5
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 5 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Media — WCAG 1.2.2, 1.2.4**
   - Issue: Video has no captions track and no transcript provided
   - Fix: Add <track kind='captions'> or link to transcript page.
2. **Heading — WCAG 1.3.1, 2.4.6**
   - Issue: h2 appears directly after h1 without an h1 first, or heading hierarchy is non-sequential
   - Fix: Restructure headings so each h2 is preceded by an h1 and levels increment by one.
3. **Form — WCAG 1.1.1, 4.1.2**
   - Issue: Input placeholder replaces label — fails when placeholders are styled away
   - Fix: Add visible label element alongside placeholder.
4. **Heading — WCAG 1.3.1**
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Use proper sequential heading levels.
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

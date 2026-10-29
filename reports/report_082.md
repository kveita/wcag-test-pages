# WCAG Test Page 82 — Accessibility Audit Report

**Page URL:** `pages/page_082.html`
**Total Violations Found:** 3
**WCAG 2.2 Level:** AAA (target)
**Audit Date:** 2026-10-29

## Summary

This page was generated with 3 intentional WCAG 2.2 AAA accessibility violations to serve as a test fixture for evaluating accessibility audit tools and the wcag-skill. Each violation is documented below with its associated WCAG success criterion, a description of the issue, and a proposed fix.

## Detected Violations

1. **Layout — WCAG 2.4.7**
   - Issue: Focus outline clipped or hidden by overflow: hidden on parent elements
   - Fix: Ensure focus is not clipped by overflow: hidden.
2. **Heading — WCAG 1.3.1**
   - Issue: Page jumps from h1 to h3, skipping h2
   - Fix: Use proper sequential heading levels.
3. **Media — WCAG 1.4.2**
   - Issue: Background audio plays automatically on page load, no stop/pause button
   - Fix: Remove autoplay or add a prominent pause control.

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

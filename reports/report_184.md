# WCAG Test Page 184 — Accessibility Audit Report

**Page URL:** `pages/page_184.html`
**Run Date:** 2026-10-29
**Total Expected Violations:** 0
**Total Detected Violations:** 16

## Summary
- Expected: 0 | Detected: 16 | Coverage: 1600%

## Expected Violations


## Detected Violations

- **color-no-contrast** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.contrast-red-on-red
- **color-no-contrast** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.contrast-gray-on-white
- **color-red-green** (WCAG ['1.4.1'])
  - Selector: \.color-pill
- **link-placeholder** (WCAG ['2.4.4'])
  - Selector: link-placeholder
- **link-placeholder** (WCAG ['2.4.4'])
  - Selector: link-placeholder
- **link-empty-href** (WCAG ['2.1.1', '4.1.2'])
  - Selector: a[href="#"]
- **form-input-id-mismatch** (WCAG ['1.1.1', '4.1.2'])
  - Selector: input
- **heading-missing** (WCAG ['1.3.1'])
  - Selector: p[style*="font-weight: bold"]
- **table-layout** (WCAG ['1.3.1'])
  - Selector: table
- **table-layout-fixed** (WCAG ['1.4.10'])
  - Selector: table[style*="width: 100%"]
- **table-complex** (WCAG ['1.3.1'])
  - Selector: th
- **aria-live-overflow** (WCAG ['4.1.3'])
  - Selector: [role="alert"][aria-hidden]
- **aria-hidden-live** (WCAG ['4.1.3'])
  - Selector: [role="alert"][aria-hidden]
- **sr-decorative-role** (WCAG ['1.1.1'])
  - Selector: [role="img"]
- **language-unset** (WCAG ['3.1.1'])
  - Selector: <html
- **scroll-small-target** (WCAG ['2.5.5'])
  - Selector: a

## Fixes

- [color-no-contrast] Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.
- [color-no-contrast] Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.
- [color-red-green] Add text labels or icons alongside color indicators.
- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-empty-href] Remove href='#' or use a real URL.
- [form-input-id-mismatch] Ensure label for='X' matches input id='X'.
- [heading-missing] Use <h1>-<h6> for heading elements.
- [table-layout] Use proper <thead> <th> for table headers.
- [table-layout-fixed] Remove fixed width or allow text wrapping.
- [table-complex] Add scope='col'/'row' to header cells.
- [aria-live-overflow] Manage live region updates properly.
- [aria-hidden-live] Remove aria-hidden from live regions.
- [sr-decorative-role] Add aria-label or remove role='img'.
- [language-unset] Add lang='en' to <html>.
- [scroll-small-target] Increase to 44x44 CSS px.

*Page: [pages/page_{pid}.html](pages/page_{pid}.html)*
# WCAG Test Page 237 — Accessibility Audit Report

**Page URL:** `pages/page_237.html`
**Run Date:** 2026-10-29
**Total Expected Violations:** 6
**Total Detected Violations:** 19

## Summary
- Expected: 6 | Detected: 19 | Coverage: 317%

## Expected Violations

- [❌ Missing] Image has meaningless alt text 'image' — WCAG 1.1.1
- [❌ Missing] Link text 'Click here for more info' is not descriptive — WCAG 2.4.4
- [❌ Missing] Link contains placeholder text 'here' — WCAG 2.4.4
- [❌ Missing] Input field with no associated label — WCAG 1.3.1, 4.1.2
- [❌ Missing] Skipped heading level detected — WCAG 1.3.1
- [❌ Missing] Table has width='100%' and content is squished — WCAG 1.4.10

## Detected Violations

- **link-placeholder** (WCAG ['2.4.4'])
  - Selector: link-placeholder
- **link-placeholder** (WCAG ['2.4.4'])
  - Selector: link-placeholder
- **link-empty-href** (WCAG ['2.1.1', '4.1.2'])
  - Selector: a[href="#"]
- **form-input-id-mismatch** (WCAG ['1.1.1', '4.1.2'])
  - Selector: input
- **heading-skip** (WCAG ['1.3.1'])
  - Selector: h2
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
- **scroll-blocked** (WCAG ['2.1.1'])
  - Selector: overflow
- **scroll-small-target** (WCAG ['2.5.5'])
  - Selector: a
- **motion-flash** (WCAG ['2.3.1'])
  - Selector: \.motion-flash
- **motion-parallax** (WCAG ['2.1.1'])
  - Selector: \.motion-parallax
- **motion-autoplay-video** (WCAG ['2.1.1'])
  - Selector: video
- **video-auto-caption** (WCAG ['1.2.2', '1.2.4'])
  - Selector: video

## Fixes

- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-empty-href] Remove href='#' or use a real URL.
- [form-input-id-mismatch] Ensure label for='X' matches input id='X'.
- [heading-skip] Restructure heading hierarchy so each level follows sequentially.
- [heading-missing] Use <h1>-<h6> for heading elements.
- [table-layout] Use proper <thead> <th> for table headers.
- [table-layout-fixed] Remove fixed width or allow text wrapping.
- [table-complex] Add scope='col'/'row' to header cells.
- [aria-live-overflow] Manage live region updates properly.
- [aria-hidden-live] Remove aria-hidden from live regions.
- [sr-decorative-role] Add aria-label or remove role='img'.
- [language-unset] Add lang='en' to <html>.
- [scroll-blocked] Ensure keyboard-accessible scrolling.
- [scroll-small-target] Increase to 44x44 CSS px.
- [motion-flash] Remove flash pattern or slow to < 3 Hz.
- [motion-parallax] Add @media (prefers-reduced-motion: reduce).
- [motion-autoplay-video] Add pause button and respect reduced motion.
- [video-auto-caption] Add <track kind='captions'> or transcript.

*Page: [pages/page_{pid}.html](pages/page_{pid}.html)*
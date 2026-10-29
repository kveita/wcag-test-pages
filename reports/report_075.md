# WCAG Test Page 075 — Accessibility Audit Report

**Page URL:** `pages/page_075.html`
**Run Date:** 2026-10-29
**Total Expected Violations:** 3
**Total Detected Violations:** 30

## Summary
- Expected: 3 | Detected: 30 | Coverage: 1000%

## Expected Violations

- [❌ Missing] Moving carousels shift focus without user request — WCAG 2.5.2
- [❌ Missing] Decorative image with empty alt but aria-label also empty — screen readers annou — WCAG 1.1.1
- [❌ Missing] Photo of landscape with no alt text — screen reader has no fallback — WCAG 1.1.1

## Detected Violations

- **color-no-contrast** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.contrast-red-on-red
- **color-no-contrast** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.contrast-gray-on-white
- **color-no-contrast** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.contrast-light-gray-on-white
- **color-red-green** (WCAG ['1.4.1'])
  - Selector: \.color-pill
- **img-meaningless-alt** (WCAG ['1.1.1'])
  - Selector: img[alt="image"]
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
- **text-small** (WCAG ['1.4.3', '1.4.6'])
  - Selector: \.small-text
- **text-justified** (WCAG ['1.4.8'])
  - Selector: \.justified-text
- **text-spaced** (WCAG ['1.4.12'])
  - Selector: \.spaced-text
- **text-no-line-height** (WCAG ['1.4.12'])
  - Selector: \.tight-text
- **layout-fixed-width** (WCAG ['1.4.10'])
  - Selector: \.layout-fixed
- **keyboard-focus-invisible** (WCAG ['2.4.7', '1.4.11'])
  - Selector: :focus
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

- [color-no-contrast] Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.
- [color-no-contrast] Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.
- [color-no-contrast] Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.
- [color-red-green] Add text labels or icons alongside color indicators.
- [img-meaningless-alt] Replace alt='image' with descriptive text.
- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-placeholder] Replace 'click here' with descriptive link text like 'Learn more about X'.
- [link-empty-href] Remove href='#' or use a real URL.
- [form-input-id-mismatch] Ensure label for='X' matches input id='X'.
- [heading-skip] Restructure heading hierarchy so each level follows sequentially.
- [heading-missing] Use <h1>-<h6> for heading elements.
- [table-layout] Use proper <thead> <th> for table headers.
- [table-layout-fixed] Remove fixed width or allow text wrapping.
- [table-complex] Add scope='col'/'row' to header cells.
- [text-small] Increase font size to 14px minimum or improve contrast to 7:1.
- [text-justified] Use text-align: left or right instead of justify.
- [text-spaced] Reduce letter-spacing to 0.12em or less.
- [text-no-line-height] Set line-height to at least 1.5.
- [layout-fixed-width] Use percentage-based widths.
- [keyboard-focus-invisible] Add visible focus indicator with 3:1 contrast ratio.
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
# WCAG Test Pages

A test suite of 100 random webpages designed to test WCAG 2.2 Level AAA accessibility auditing. Each page contains intentional accessibility violations to evaluate automated and manual testing tools.

## Structure

- `pages/` — HTML test pages (100 pages, `page_001.html` through `page_100.html`)
- `reports/` — Markdown audit reports for each page (100 reports, `report_001.md` through `report_100.md`)

## Violations Covered

Each page contains 2-5 random accessibility violations, covering categories such as:

- Color contrast (1.4.3, 1.4.6)
- Color-only information (1.4.1)
- Missing image alt text (1.1.1)
- Link accessibility (2.4.4, 1.1.1)
- Form labeling (1.1.1, 4.1.2)
- Heading hierarchy (1.3.1)
- Table accessibility (1.3.1)
- Animation/motion (2.1.1, 1.4.2)
- Text readability (1.4.8, 1.4.12)
- ARIA issues (4.1.3)
- Language attributes (3.1.1)
- Layout and zoom (1.4.4, 1.4.10)
- Keyboard navigation (2.1.1, 2.4.3)
- Screen reader compatibility (1.3.2)

## Usage

1. Clone this repository
2. Open each page in a browser and/or run accessibility audits
3. Compare findings with the expected report in `reports/`
4. Use to test accessibility scanning tools, browser extensions, and AI-powered auditors

## WCAG 2.2 Reference

- [WCAG 2.2 Overview](https://www.w3.org/WAI/WCAG22/quickref/)
- Level A — minimum level of conformance
- Level AA — most commonly required level
- Level AAA — most stringent level

## License

Public domain — for testing and educational purposes.

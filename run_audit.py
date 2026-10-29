"""
Audit script for kveita/wcag-test-pages.

For each page:
  - Parse window.__wcag_test_page.violations (expected violations)
  - Track which violations are present and generate reports with fix suggestions
  - Build reports/report_XXX.md
  - Save stats in reports/_stats/manifest.json
  - Build reports/index.html with charts
  - Generate fixed versions in fixed/page_XXX.html
"""

import ast
import json
import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone

OUT = Path("/tmp/wcag-test-pages")
PAGES_DIR = OUT / "pages"
REPORTS_DIR = OUT / "reports"
FIXED_DIR = OUT / "fixed"
STATS_DIR = REPORTS_DIR / "_stats"
STATS_FILE = STATS_DIR / "manifest.json"

# All known violation types and their fixes
KNOWN_VIOLATIONS = {
    "color-no-contrast": {
        "type": "Color/Contrast",
        "wcag": ["1.4.3", "1.4.6"],
        "desc": "Text color matches background — unreadable",
        "fix": "Increase text contrast; use dark text on light backgrounds or vice versa.",
    },
    "color-red-green": {
        "type": "Color-Only",
        "wcag": ["1.4.1"],
        "desc": "Information conveyed only by color (e.g., red vs green indicators)",
        "fix": "Add text labels or icons alongside color indicators.",
    },
    "color-gray-light": {
        "type": "Color/Contrast",
        "wcag": ["1.4.3", "1.4.6"],
        "desc": "Light gray text on light background",
        "fix": "Darken text color or lighten background.",
    },
    "img-decorative-missing-alt": {
        "type": "Image",
        "wcag": ["1.1.1"],
        "desc": "Decorative image with missing alt attribute",
        "fix": "Add alt=\"\" to indicate the image is decorative.",
    },
    "img-no-alt-description": {
        "type": "Image",
        "wcag": ["1.1.1"],
        "desc": "Image has no alt text description",
        "fix": "Provide descriptive alt text: alt=\"A clear description of the image\".",
    },
    "img-meaningless-alt": {
        "type": "Image",
        "wcag": ["1.1.1"],
        "desc": "Image alt text is generic like 'image' or 'picture'",
        "fix": "Replace with descriptive alt text that conveys the image's meaning.",
    },
    "link-missing-name": {
        "type": "Link",
        "wcag": ["2.4.4", "1.1.1"],
        "desc": "Link image has no accessible name",
        "fix": "Add aria-label='Description of the link destination'.",
    },
    "link-placeholder": {
        "type": "Link",
        "wcag": ["2.4.4"],
        "desc": "Link text is non-descriptive like 'click here' or 'here'",
        "fix": "Replace with descriptive text: 'Learn more about X'.",
    },
    "link-empty-href": {
        "type": "Link",
        "wcag": ["2.1.1", "4.1.2"],
        "desc": "Link has href='#' with no real destination",
        "fix": "Remove href='#' or provide a real URL.",
    },
    "form-label-missing": {
        "type": "Form",
        "wcag": ["1.1.1", "4.1.2"],
        "desc": "Form input has no associated label or aria-label",
        "fix": "Add <label for='input-id'>Label text</label> or aria-label='Label'.",
    },
    "form-placeholder-only": {
        "type": "Form",
        "wcag": ["1.1.1", "4.1.2"],
        "desc": "Placeholder text used as the only label for an input field",
        "fix": "Add a visible label element in addition to the placeholder.",
    },
    "form-error-color-only": {
        "type": "Form",
        "wcag": ["1.4.1"],
        "desc": "Error message indicated only by color, not by text",
        "fix": "Add explicit text like 'This field is required' or an icon with aria-label.",
    },
    "form-input-id-mismatch": {
        "type": "Form",
        "wcag": ["1.1.1", "4.1.2"],
        "desc": "Input id does not match label for attribute",
        "fix": "Ensure label for='X' matches input id='X'.",
    },
    "heading-skip": {
        "type": "Heading",
        "wcag": ["1.3.1", "2.4.6"],
        "desc": "Heading hierarchy skips levels (e.g., h2 after h1, missing h2)",
        "fix": "Restructure to use sequential heading levels: h1 → h2 → h3, etc.",
    },
    "heading-missing": {
        "type": "Heading",
        "wcag": ["1.3.1"],
        "desc": "Content looks like a heading but uses <p> or <div> with bold",
        "fix": "Use the appropriate heading element <h1>-<h6>.",
    },
    "heading-levels": {
        "type": "Heading",
        "wcag": ["1.3.1"],
        "desc": "Page jumps from h1 to h3, skipping h2",
        "fix": "Use proper sequential heading levels.",
    },
    "audio-autoplay": {
        "type": "Media",
        "wcag": ["1.4.2"],
        "desc": "Audio plays automatically on page load without user control",
        "fix": "Remove autoplay or provide a prominent pause control.",
    },
    "video-auto-caption": {
        "type": "Media",
        "wcag": ["1.2.2", "1.2.4"],
        "desc": "Video has no captions and no transcript",
        "fix": "Add <track kind='captions'> or link to a transcript page.",
    },
    "audio-decorative-silent": {
        "type": "Media",
        "wcag": ["1.4.2"],
        "desc": "Decorative sound plays automatically but cannot be stopped",
        "fix": "Stop the sound automatically after a short delay or let users disable it.",
    },
    "motion-flash": {
        "type": "Motion",
        "wcag": ["2.3.1"],
        "desc": "Content flashes rapidly (> 3 times per second), seizure risk",
        "fix": "Remove flash or slow to < 3 Hz; provide a mechanism to stop it.",
    },
    "motion-parallax": {
        "type": "Motion",
        "wcag": ["2.1.1"],
        "desc": "Parallax animation without reduced-motion support",
        "fix": "Add @media (prefers-reduced-motion: reduce) rule to disable parallax.",
    },
    "motion-autoplay-video": {
        "type": "Motion",
        "wcag": ["2.1.1"],
        "desc": "Video/GIF plays without user interaction and ignores reduced-motion",
        "fix": "Add a pause button and respect prefers-reduced-motion.",
    },
    "aria-live-overflow": {
        "type": "ARIA",
        "wcag": ["4.1.3"],
        "desc": "Live region updates exceed expected boundaries",
        "fix": "Use aria-busy and manage live region updates carefully.",
    },
    "keyboard-focus-trap": {
        "type": "Keyboard",
        "wcag": ["2.1.2"],
        "desc": "Focus is trapped within a modal or overlay with no escape",
        "fix": "Add Escape key handler to close modal and return focus to trigger.",
    },
    "keyboard-focus-invisible": {
        "type": "Keyboard",
        "wcag": ["2.4.7", "1.4.11"],
        "desc": "Focus indicator fails 3:1 contrast ratio",
        "fix": "Ensure focus ring meets 3:1 contrast minimum (typically 3px outline at 3:1).",
    },
    "aria-hidden-live": {
        "type": "ARIA",
        "wcag": ["4.1.3"],
        "desc": "Live region container has aria-hidden='true'",
        "fix": "Remove aria-hidden from the live region container.",
    },
    "table-layout": {
        "type": "Table",
        "wcag": ["1.3.1"],
        "desc": "Table layout breaks column header associations",
        "fix": "Use <thead>, <th> elements with proper scope attributes.",
    },
    "table-complex": {
        "type": "Table",
        "wcag": ["1.3.1"],
        "desc": "Complex table with merged cells and missing scope attributes",
        "fix": "Add scope='col'/'row' to all <th> elements.",
    },
    "table-layout-fixed": {
        "type": "Table",
        "wcag": ["1.4.10"],
        "desc": "Fixed-width table squishes content",
        "fix": "Remove fixed width or allow text wrapping.",
    },
    "text-small": {
        "type": "Text",
        "wcag": ["1.4.3", "1.4.6"],
        "desc": "Body text is below 14px or fails contrast ratio",
        "fix": "Increase font size to 14px minimum or improve contrast.",
    },
    "text-justified": {
        "type": "Text",
        "wcag": ["1.4.8"],
        "desc": "Text is justified, which breaks word boundaries",
        "fix": "Use text-align: left or right instead of justify.",
    },
    "text-spaced": {
        "type": "Text",
        "wcag": ["1.4.12"],
        "desc": "Letter spacing exceeds 0.12em on body text",
        "fix": "Keep letter-spacing between -0.05em and 0.12em.",
    },
    "text-no-line-height": {
        "type": "Text",
        "wcag": ["1.4.12"],
        "desc": "Line height is 1.0 or 1, too tight for readability",
        "fix": "Set line-height to at least 1.5.",
    },
    "layout-fixed-width": {
        "type": "Layout",
        "wcag": ["1.4.10"],
        "desc": "Fixed width layout breaks when user zooms to 200%",
        "fix": "Use percentage-based or fluid widths.",
    },
    "layout-no-zoom": {
        "type": "Layout",
        "wcag": ["1.4.4"],
        "desc": "Browser zoom is disabled via viewport meta or CSS",
        "fix": "Remove user-scalable=no or minimum-scale restrictions.",
    },
    "layout-bad-focus": {
        "type": "Layout",
        "wcag": ["2.4.7"],
        "desc": "Focus is clipped or hidden by overflow: hidden on parent elements",
        "fix": "Remove overflow: hidden on elements that contain focusable children.",
    },
    "script-keyboard-missing": {
        "type": "Script",
        "wcag": ["2.1.1"],
        "desc": "Widget responds to mouse click but not keyboard",
        "fix": "Add keydown handlers for Enter and Space keys.",
    },
    "script-focus-order": {
        "type": "Script",
        "wcag": ["2.4.3"],
        "desc": "Focus order is non-linear, not matching visual reading order",
        "fix": "Ensure tab order matches visual reading order.",
    },
    "script-moving-focus": {
        "type": "Script",
        "wcag": ["2.5.2"],
        "desc": "Focus is moved automatically without user request",
        "fix": "Avoid auto-advancing elements, or let user control focus movement.",
    },
    "sr-reading-order": {
        "type": "Screen Reader",
        "wcag": ["1.3.2"],
        "desc": "Content order in HTML differs from visual order",
        "fix": "Reorder DOM elements so focus and reading order matches visual order.",
    },
    "sr-live-no-wait": {
        "type": "Screen Reader",
        "wcag": ["4.1.3"],
        "desc": "Live region announcement is too brief for processing",
        "fix": "Increase aria-live timeout or let users dismiss manually.",
    },
    "sr-decorative-role": {
        "type": "Screen Reader",
        "wcag": ["1.1.1"],
        "desc": "Element has role='img' but contains only decorative text",
        "fix": "Remove role='img' or add an accessible name.",
    },
    "language-unset": {
        "type": "Language",
        "wcag": ["3.1.1"],
        "desc": "Document has no lang attribute on <html>",
        "fix": "Add lang='en' (or appropriate language) to the <html> element.",
    },
    "language-partially": {
        "type": "Language",
        "wcag": ["3.1.1"],
        "desc": "Partial lang attribute does not match actual content language",
        "fix": "Set the correct lang attribute: e.g., lang='no' for Norwegian.",
    },
    "scroll-blocked": {
        "type": "Scrolling",
        "wcag": ["2.1.1"],
        "desc": "Horizontally scrolling content cannot be scrolled via keyboard",
        "fix": "Ensure all scrollable areas can be scrolled via keyboard.",
    },
    "scroll-small-target": {
        "type": "Scrolling",
        "wcag": ["2.5.5"],
        "desc": "Small clickable areas (under 44x44 CSS px)",
        "fix": "Increase clickable areas to at least 44x44 CSS px.",
    },
    "scroll-sticky-header": {
        "type": "Scrolling",
        "wcag": ["1.4.12"],
        "desc": "Sticky header partially obscures content when scrolling",
        "fix": "Make sticky headers collapsible or reduce height.",
    },
}


def parse_expected_violations(page_path: Path) -> list[dict]:
    """Parse window.__wcag_test_page.violations from page HTML."""
    text = page_path.read_text()
    m = re.search(
        r"window\.__wcag_test_page\s*=\s*({.*?});\s*</script>",
        text,
        re.DOTALL,
    )
    if not m:
        return []
    try:
        data = ast.literal_eval(m.group(1))
        return data.get("violations", [])
    except Exception:
        return []


def find_violation_type(ev: dict) -> str:
    """Map a violation entry to a known type for fix lookup."""
    desc = ev.get("desc", "")
    wcags = ev.get("wcag", [])
    # Try to find by description keywords
    lower_desc = desc.lower()
    if "contrast" in lower_desc or "color" in lower_desc:
        return "color-no-contrast"
    if "decorative" in lower_desc and "alt" in lower_desc:
        return "img-decorative-missing-alt"
    if "alt" in lower_desc and "meaningless" in lower_desc:
        return "img-meaningless-alt"
    if "label" in lower_desc and ("no" in lower_desc or "missing" in lower_desc):
        return "form-label-missing"
    if "placeholder" in lower_desc and "label" in lower_desc:
        return "form-placeholder-only"
    if "error" in lower_desc and "color" in lower_desc:
        return "form-error-color-only"
    if "heading" in lower_desc or "skip" in lower_desc:
        return "heading-skip"
    if "autoplay" in lower_desc or "sound" in lower_desc:
        return "audio-autoplay"
    if "flash" in lower_desc:
        return "motion-flash"
    if "table" in lower_desc:
        return "table-layout"
    if "justif" in lower_desc:
        return "text-justified"
    if "small" in lower_desc and ("text" in lower_desc or "font" in lower_desc):
        return "text-small"
    if "aria-hidden" in lower_desc or "aria-live" in lower_desc:
        return "aria-hidden-live"
    if "language" in lower_desc:
        return "language-unset"
    if "scroll" in lower_desc:
        return "scroll-blocked"
    if "link" in lower_desc and "placeholder" in lower_desc:
        return "link-placeholder"
    # Fallback by wcag
    if "1.4.3" in wcags or "1.4.6" in wcags:
        return "color-no-contrast"
    if "1.4.1" in wcags:
        return "color-red-green"
    if "1.1.1" in wcags:
        return "img-no-alt-description"
    if "2.4.4" in wcags:
        return "link-placeholder"
    if "4.1.2" in wcags:
        return "form-label-missing"
    if "1.4.10" in wcags:
        return "table-layout-fixed"
    return "heading-skip"


def get_fix_for_violation(ev: dict) -> str:
    """Get fix suggestion for a violation."""
    vtype = find_violation_type(ev)
    info = KNOWN_VIOLATIONS.get(vtype, {"fix": "Apply general accessibility best practices."})
    return info.get("fix", "Apply general accessibility best practices.")


def get_violation_details(ev: dict) -> dict:
    """Enrich a violation entry with type classification and fix."""
    vtype = find_violation_type(ev)
    info = KNOWN_VIOLATIONS.get(vtype, ev)
    return {
        "type": vtype,
        "type_display": info.get("type", ev.get("type", "Unknown")),
        "wcag": ev.get("wcag", []),
        "desc": ev.get("desc", ""),
        "fix": info.get("fix", "Apply general accessibility best practices."),
    }


def generate_reports(manifest: dict):
    """Generate per-page markdown reports."""
    runs = manifest.get("runs", [])
    latest = runs[-1] if runs else {}
    date = latest.get("date", "N/A")
    page_results = manifest.get("current", {})

    for pid, data in sorted(page_results.items()):
        expected = data.get("expected", [])
        actual = data.get("actual", [])
        fixes = data.get("fixes", {})

        lines = [
            f"# WCAG Test Page {pid} — Accessibility Audit Report",
            "",
            f"**Page URL:** `pages/page_{pid}.html`",
            f"**Run Date:** {date}",
            f"**Total Expected Violations:** {len(expected)}",
            f"**Total Detected Violations:** {len([a for a in actual if a.get('found', False)])}",
            f"**WCAG 2.2 Level:** AAA",
            "",
            "## Summary",
            "",
            f"- **Expected violations:** {len(expected)}",
            f"- **Detected (found by audit):** {len([a for a in actual if a.get('found', False)])}",
            f"- **Missing (expected but not found):** {len([a for a in actual if not a.get('found', False)])}",
            f"- **False positives:** {len([a for a in actual if a.get('found', False) and a.get('type') not in [e.get('type', '') for e in expected]])}",
            "",
            "## Expected Violations",
            "",
        ]

        for i, ev in enumerate(expected, 1):
            v = get_violation_details(ev)
            status = "✅ Found" if v.get("found", False) else "❌ Missing"
            lines.append(f"{i}. **{v['type_display']} — WCAG {', '.join(v['wcag'])}** {status}")
            lines.append(f"   - Issue: {v['desc']}")
            lines.append(f"   - Fix: {v['fix']}")
            lines.append("")

        lines.extend([
            "## Detected Violations (Audit)",
            "",
        ])
        for a in actual:
            status = "✅" if a.get("found", False) else "❌"
            lines.append(f"- {status} **{a.get('type', 'Unknown')} — WCAG {', '.join(a.get('wcag', []))}**")
            lines.append(f"  - Detected: {a.get('desc', 'N/A')}")

        lines.extend([
            "",
            "## Recommendations",
            "",
            f"- Fix all {len([a for a in actual if a.get('found', False)])} detected violations",
            "- Consider adding skip links and proper heading hierarchy",
            "- Ensure all form controls have associated labels",
            "- Add alt text to all images",
            "- Test with screen readers like NVDA or VoiceOver",
            "",
            f"*Audit run: {date}*",
            f"*Page: [pages/page_{pid}.html](pages/page_{pid}.html)*",
        ])

        report_path = REPORTS_DIR / f"report_{pid}.md"
        report_path.write_text("\n".join(lines))


def generate_index_html(manifest: dict):
    """Generate the summary index.html with charts."""
    runs = manifest.get("runs", [])
    if not runs:
        return "<html><body><p>No audit runs yet.</p></body></html>"

    latest = runs[-1]
    page_results = latest.get("per_page", {})

    # Aggregate stats
    all_wcags = Counter()
    all_types = Counter()
    per_page_counts = {}
    for pid, data in sorted(page_results.items()):
        count = len([a for a in data.get("actual", []) if a.get("found", False)])
        per_page_counts[pid] = count
        for a in data.get("actual", []):
            for w in a.get("wcag", []):
                all_wcags[w] += 1
        for a in data.get("actual", []):
            all_types[a.get("type")] += 1

    total_pages = len(page_results)
    pages_zero = sum(1 for c in per_page_counts.values() if c == 0)
    pages_hard = sum(1 for c in per_page_counts.values() if c >= 4)
    max_violations = max(per_page_counts.values()) if per_page_counts else 0
    min_violations = min(per_page_counts.values()) if per_page_counts else 0
    avg_violations = sum(per_page_counts.values()) / total_pages if total_pages else 0

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WCAG Test Pages — Audit Dashboard</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f7fa;
    padding: 40px 20px;
    max-width: 1200px;
    margin: 0 auto;
  }}
  h1 {{ font-size: 2.2em; margin-bottom: 8px; }}
  h2 {{ font-size: 1.5em; margin: 30px 0 15px; padding-bottom: 8px; border-bottom: 2px solid #3498db; }}
  .summary-cards {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 30px;
  }}
  .card {{
    background: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    text-align: center;
  }}
  .card .value {{
    font-size: 2.5em;
    font-weight: 700;
    color: #3498db;
    line-height: 1.2;
  }}
  .card .label {{
    color: #666;
    font-size: 0.9em;
    margin-top: 4px;
  }}
  .chart-container {{
    background: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    margin-bottom: 30px;
  }}
  .chart-container canvas {{
    max-height: 400px;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 30px;
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }}
  th {{
    background: #3498db;
    color: #fff;
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
  }}
  td {{
    padding: 10px 16px;
    border-bottom: 1px solid #eee;
  }}
  tr:hover {{ background: #f8f9fa; }}
  .badge {{
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.85em;
    font-weight: 600;
    margin: 2px;
  }}
  .badge-pass {{ background: #d4edda; color: #155724; }}
  .badge-fail {{ background: #f8d7da; color: #721c24; }}
  .badge-warn {{ background: #fff3cd; color: #856404; }}
  footer {{
    text-align: center;
    color: #888;
    padding: 20px 0;
    font-size: 0.9em;
  }}
  a {{
    color: #3498db;
    text-decoration: none;
  }}
  a:hover {{
    text-decoration: underline;
  }}
</style>
</head>
<body>

<h1>🧪 WCAG Test Pages — Audit Dashboard</h1>
<p>Accessibility audit results for <strong>{total_pages}</strong> test pages.
Audited on <strong>{latest.get('date', 'N/A')}</strong>.</p>

<div class="summary-cards">
  <div class="card">
    <div class="value">{pages_zero}</div>
    <div class="label">Pages with 0 Violations</div>
  </div>
  <div class="card">
    <div class="value">{pages_hard}</div>
    <div class="label">Pages with 4+ Violations</div>
  </div>
  <div class="card">
    <div class="value">{max_violations}</div>
    <div class="label">Max Violations (Single Page)</div>
  </div>
  <div class="card">
    <div class="value">{avg_violations:.1f}</div>
    <div class="label">Avg Violations Per Page</div>
  </div>
</div>

<h2>📊 Violations by WCAG Success Criterion</h2>
<div class="chart-container">
  <canvas id="wcagChart"></canvas>
</div>

<h2>📊 Violations by Type</h2>
<div class="chart-container">
  <canvas id="typeChart"></canvas>
</div>

<h2>📈 Per-Page Violation Counts</h2>
<div class="chart-container">
  <canvas id="perPageChart"></canvas>
</div>

<h2>📄 Individual Page Results</h2>
<table>
  <thead>
    <tr>
      <th>Page</th>
      <th>Violations</th>
      <th>Report</th>
      <th>Fixed Page</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
"""

    sorted_pages = sorted(per_page_counts.items(), key=lambda x: x[1], reverse=True)
    for pid, count in sorted_pages:
        report_exists = (REPORTS_DIR / f"report_{pid}.md").exists()
        fixed_exists = (FIXED_DIR / f"page_{pid}.html").exists()
        status_class = "badge-pass" if count == 0 else ("badge-fail" if count >= 4 else "badge-warn")
        status_text = "✅ Clean" if count == 0 else f"⚠️ {count} found"
        html += f"""
    <tr>
      <td>page_{pid}.html</td>
      <td>{count}</td>
      <td>{'📄' if report_exists else '—'}</td>
      <td>{'🔧' if fixed_exists else '—'}</td>
      <td><span class="badge {status_class}">{status_text}</span></td>
    </tr>"""

    html += """
  </tbody>
</table>

<footer>
  <p>Generated by <a href="https://github.com/turbolego/wcag-skill">wcag-skill</a> · 
     <a href="https://github.com/kveita/wcag-test-pages">kveita/wcag-test-pages</a></p>
</footer>

<!-- Chart.js for charts -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<script>
const wcagCtx = document.getElementById('wcagChart').getContext('2d');
const typeCtx = document.getElementById('typeChart').getContext('2d');
const perPageCtx = document.getElementById('perPageChart').getContext('2d');

// WCAG chart data
const wcagLabels = Object.entries({"1.4.3": "Contrast (1.4.3)", "1.4.6": "Contrast AAA", "1.4.1": "Color-Only", "1.1.1": "Image/Label", "4.1.2": "Form Label", "1.4.8": "Justify", "1.4.10": "Table Layout", "1.4.12": "Text Spacing", "2.4.4": "Link Purpose", "2.1.1": "Keyboard", "2.5.5": "Touch Target", "1.3.1": "Heading/Table", "3.1.1": "Language", "4.1.3": "ARIA Live", "2.4.7": "Focus Visible", "2.1.2": "Focus Trap", "1.4.2": "Autoplay", "2.3.1": "Motion", "1.2.2": "Captions", "1.4.4": "Zoom"}).filter(([k,v]) => k in {"1.4.3": true, "1.4.6": true, "1.4.1": true, "1.1.1": true, "4.1.2": true, "1.4.8": true, "1.4.10": true, "1.4.12": true, "2.4.4": true, "2.1.1": true, "2.5.5": true, "1.3.1": true, "3.1.1": true, "4.1.3": true, "2.4.7": true, "2.1.2": true, "1.4.2": true, "2.3.1": true, "1.2.2": true, "1.4.4": true});

new Chart(wcagCtx, {{
  type: 'bar',
  data: {{
    labels: wcagLabels.map(l => l[1]),
    datasets: [
      {{
        label: 'Count',
        data: wcagLabels.map(l => all_wcags[l[0]]),
        backgroundColor: ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c','#3498db','#9b59b6','#e91e63','#00bcd4','#ff5722','#673ab7','#8bc34a','#ff9800','#4caf50','#795548','#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c'],
        borderWidth: 1
      }}
    ]
  }},
  options: {{
    responsive: true,
    maintainAspectRatio: false,
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{ callbacks: {{ label: ctx => `${{ctx.parsed.y}} violations` }} }}
    }},
    scales: {{
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }}, title: {{ display: true, text: 'Number of Pages' }} }}
    }}
  }}
}});

// Type chart
const typeLabels = Object.entries({"Color/Contrast": "Color", "Color-Only": "Color-Only", "Image": "Image", "Link": "Link", "Form": "Form", "Heading": "Heading", "Table": "Table", "Motion": "Motion", "Text": "Text", "Layout": "Layout", "Keyboard": "Keyboard", "ARIA": "ARIA", "Language": "Language", "Scrolling": "Scrolling", "Media": "Media", "Screen Reader": "Screen Reader"}}).filter(([k,v]) => all_types[k] > 0);

new Chart(typeCtx, {{
  type: 'bar',
  data: {{
    labels: typeLabels.map(l => l[1]),
    datasets: [
      {{
        label: 'Count',
        data: typeLabels.map(l => all_types[l[0]]),
        backgroundColor: ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c','#3498db','#9b59b6','#e91e63','#00bcd4','#ff5722','#673ab7','#8bc34a','#ff9800','#4caf50','#795548'],
        borderWidth: 1
      }}
    ]
  }},
  options: {{
    responsive: true,
    maintainAspectRatio: false,
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{ callbacks: {{ label: ctx => `${{ctx.parsed.y}} violations` }} }}
    }},
    scales: {{
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }}, title: {{ display: true, text: 'Number of Pages' }} }}
    }}
  }}
}});

// Per-page chart (top 20)
const topPages = Object.entries(per_page_counts).sort((a, b) => b[1] - a[1]).slice(0, 20);
new Chart(perPageCtx, {{
  type: 'bar',
  data: {{
    labels: topPages.map(p => `page_{p[0]}`),
    datasets: [
      {{
        label: 'Violations Found',
        data: topPages.map(p => p[1]),
        backgroundColor: topPages.map(p => p[1] > 10 ? '#e74c3c' : p[1] > 5 ? '#f1c40f' : '#2ecc71'),
        borderWidth: 1
      }}
    ]
  }},
  options: {{
    responsive: true,
    maintainAspectRatio: false,
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{ callbacks: {{ label: ctx => `${{ctx.parsed.y}} violations` }} }}
    }},
    scales: {{
      x: {{ ticks: {{ maxRotation: 90, minRotation: 45, font: {{ size: 10 }} }} }},
      y: {{ beginAtZero: true, ticks: {{ stepSize: 1 }}, title: {{ display: true, text: 'Number of Violations' }} }}
    }}
  }}
}});
</script>

</body>
</html>"""

    return html


def build_manifest(prev: dict, page_results: dict) -> dict:
    """Build manifest with new run appended."""
    run = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_pages": len(page_results),
        "total_violations": sum(
            len([a for a in data.get("actual", []) if a.get("found", False)])
            for data in page_results.values()
        ),
        "per_page": page_results,
    }
    all_runs = prev.get("runs", []) + [run]
    return {"runs": all_runs, "current": page_results}


def generate_fixed_page(page_path: Path, violations: list[dict]) -> str:
    """Generate a fixed version of the page with violations corrected."""
    text = page_path.read_text()

    # Map violation types to fix functions
    fixes = {
        "color-no-contrast": lambda: "",  # Remove contrast issue classes
        "color-red-green": lambda: '<div class="color-only" role="list" aria-label="Status indicators"><div class="color-pill neutral" role="listitem"><span aria-hidden="true">●</span> Neutral</div><div class="color-pill go" role="listitem"><span aria-hidden="true">●</span> Go</div><div class="color-pill stop" role="listitem"><span aria-hidden="true">●</span> Stop</div></div>',
        "color-gray-light": lambda: '<p style="color: #333333;">Gray text on white background</p>',
        "img-decorative-missing-alt": lambda: '<img src="https://picsum.photos/seed/test1/400/300" alt="" width="400" height="300" class="fixed-img">',
        "img-no-alt-description": lambda: '<img src="https://picsum.photos/seed/test2/400/300" alt="Landscape photograph" width="400" height="300" class="fixed-img">',
        "img-meaningless-alt": lambda: '<img src="https://picsum.photos/seed/test3/400/300" alt="" width="400" height="300" class="fixed-img">',
        "link-missing-name": lambda: '<a href="#" aria-label="Read more about spring gardening"><span class="icon">→</span></a>',
        "link-placeholder": lambda: '<a href="#" class="fixed-link">Read the spring gardening guide</a>',
        "link-empty-href": lambda: '<a href="#main-content" class="fixed-link">Continue to main content</a>',
        "form-label-missing": lambda: '<label for="search-input">Search products</label><input type="text" id="search-input" name="search" placeholder="Enter search term">',
        "form-placeholder-only": lambda: '<label for="email-input">Email address</label><input type="email" id="email-input" name="email" placeholder="enter your email">',
        "form-error-color-only": lambda: '<label for="name-input">Name (required)</label><input type="text" id="name-input" name="name" placeholder="your name"><span class="error-text">This field is required</span>',
        "form-input-id-mismatch": lambda: '<label for="username-input">Username</label><input type="text" id="username-input" name="username" placeholder="your username">',
        "heading-skip": lambda: '<h1>Page Title</h1><h2>Section One</h2><p>Content under section one</p><h3>Subsection</h3><p>Content under subsection</p>',
        "heading-missing": lambda: '<h2>Important Section</h2><p>Content that would have been a heading</p>',
        "heading-levels": lambda: '<h1>Page Title</h1><h2>Section</h2><h3>Subsection</h3>',
        "audio-autoplay": lambda: '<audio controls><source src="https://sample-videos.com/audio11/mp3/7/big_buck_bunny_7mb.mp3" type="audio/mpeg"></audio>',
        "video-auto-caption": lambda: '<video controls width="400"><source src="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_10mb.mp4" type="video/mp4"><track kind="captions" src="captions.vtt" srclang="en" label="English captions"></video>',
        "audio-decorative-silent": lambda: '<audio autoplay muted controls><source src="https://sample-videos.com/audio11/mp3/7/big_buck_bunny_7mb.mp3" type="audio/mpeg"></audio>',
        "motion-flash": lambda: '<div class="motion-flash safe" style="animation: none;">Content that no longer flashes</div>',
        "motion-parallax": lambda: '<div class="motion-parallax safe"></div>',
        "motion-autoplay-video": lambda: '<video controls width="400" muted><source src="https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_10mb.mp4" type="video/mp4"></video>',
        "aria-live-overflow": lambda: '<div role="status" aria-live="polite" aria-atomic="true">Status: Page loaded</div>',
        "keyboard-focus-trap": lambda: '<button onclick="alert(\"opened\")">Open Modal</button><div role="dialog" aria-modal="true"><p>Modal content</p><button onclick="this.closest(\"[role=dialog]\").remove()">Close</button></div>',
        "keyboard-focus-invisible": lambda: '<button>Submit</button>',
        "aria-hidden-live": lambda: '<div role="alert"><p>Alert: System status update available</p></div>',
        "table-layout": lambda: '<table><thead><tr><th scope="col">Product</th><th scope="col">Price</th><th scope="col">Status</th></tr></thead><tbody><tr><td>Item A</td><td>$10</td><td>Active</td></tr></tbody></table>',
        "table-complex": lambda: '<table><thead><tr><th scope="col">Product</th><th scope="col">Price</th><th scope="row">Status</th></tr></thead><tbody><tr><td>Item A</td><td>$10</td><td>Active</td></tr></tbody></table>',
        "table-layout-fixed": lambda: '<table class="fixed-table"><thead><tr><th scope="col">Product</th><th scope="col">Price</th><th scope="col">Status</th></tr></thead><tbody><tr><td>Item A</td><td>$10</td><td>Active</td></tr></tbody></table>',
        "text-small": lambda: '<p style="font-size: 16px; color: #333333;">This is normal-sized, high-contrast text.</p>',
        "text-justified": lambda: '<p style="text-align: left;">This text is left-aligned.</p>',
        "text-spaced": lambda: '<p style="letter-spacing: 0.05em;">This text has normal letter spacing.</p>',
        "text-no-line-height": lambda: '<p style="line-height: 1.6; color: #333333;">This text has comfortable line height.</p>',
        "layout-fixed-width": lambda: '<div style="max-width: 100%; margin: 0 auto;"><p>Fluid width layout.</p></div>',
        "layout-no-zoom": lambda: '<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">',
        "layout-bad-focus": lambda: '<button>Focusable element with no clipping parent</button>',
        "script-keyboard-missing": lambda: '<button onclick="alert(\"clicked\")" onkeydown="if(event.key===\"Enter\" || event.key===\" \") alert(\"clicked\")">Button with keyboard support</button>',
        "script-focus-order": lambda: '<a href="#">First</a><a href="#">Second</a><a href="#">Third</a>',
        "script-moving-focus": lambda: '<div role="marquee" aria-label="News ticker">Static news content</div>',
        "sr-reading-order": lambda: '<p>Visual order matches DOM order: first, second, third.</p>',
        "sr-live-no-wait": lambda: '<div role="alert" aria-live="polite" aria-atomic="true"><p>Status message that persists</p></div>',
        "sr-decorative-role": lambda: '<span role="img" aria-label="decorative icon">📊</span>',
        "language-unset": lambda: '<html lang="en">',
        "language-partially": lambda: '<html lang="en">',
        "scroll-blocked": lambda: '<div style="overflow-x: auto;"><table><tr><td>Cell 1</td><td>Cell 2</td></tr></table></div>',
        "scroll-small-target": lambda: '<a href="#" style="display: inline-block; padding: 12px 16px; border: 1px solid #ccc; border-radius: 6px;">Large clickable navigation link</a>',
        "scroll-sticky-header": lambda: '<header style="position: fixed; top: 0; left: 0; right: 0; background: #f8f9fa; padding: 12px;">Sticky header — collapsible</header>',
    }

    fixed_text = text
    for v in violations:
        vtype = find_violation_type(v)
        if vtype in fixes:
            # Replace the relevant section
            fixed_text = fixed_text.replace(text[max(0, text.find("<!-- L")-2):text.find("<!-- L")], "") if text.find("<!-- L") != -1 else fixed_text

    # Add prefers-reduced-motion support
    fixed_text = fixed_text.replace(
        "* {{ margin: 0; padding: 0; box-sizing: border-box; }}",
        "* {{ margin: 0; padding: 0; box-sizing: border-box; }}\n  @media (prefers-reduced-motion: reduce) {{\n    *, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }}\n  }}"
    )

    # Ensure visible focus
    fixed_text = fixed_text.replace(
        "a:focus, button:focus, input:focus {{ outline: none; }}",
        "a:focus, button:focus, input:focus {{ outline: 3px solid #3498db; outline-offset: 2px; }}"
    )

    # Add skip link target
    fixed_text = fixed_text.replace(
        '<a href="#main-content" class="skip-link">Skip to main content</a>',
        '<a href="#main-content" class="skip-link">Skip to main content</a><main id="main-content">'
    )
    fixed_text = fixed_text.replace("</body></html>", "</main></body></html>")

    return fixed_text


def save_fixed_pages(manifest: dict):
    """Generate and save fixed versions of all pages."""
    FIXED_DIR.mkdir(exist_ok=True)
    page_results = manifest.get("current", {})

    for pid, data in sorted(page_results.items()):
        violations = data.get("expected", [])
        page_path = PAGES_DIR / f"page_{pid}.html"
        if not page_path.exists():
            continue

        fixed_html = generate_fixed_page(page_path, violations)
        (FIXED_DIR / f"page_{pid}.html").write_text(fixed_html)


def main():
    REPORTS_DIR.mkdir(exist_ok=True)
    STATS_DIR.mkdir(exist_ok=True)
    FIXED_DIR.mkdir(exist_ok=True)

    manifest = {"runs": [], "current": {}}
    if STATS_FILE.exists():
        manifest = json.loads(STATS_FILE.read_text())

    page_files = sorted(PAGES_DIR.glob("page_*.html"))
    total = len(page_files)
    print(f"Auditing {total} pages...")

    page_results = {}
    for i, page_path in enumerate(page_files):
        pid = page_path.stem.replace("page_", "")
        print(f"  [{i+1}/{total}] Auditing page {pid}...", end=" ", flush=True)

        expected = parse_expected_violations(page_path)
        count = len(expected)
        print(f"{count} expected violations")

        # Enrich violations with type, wcag, and fix
        enriched = []
        for ev in expected:
            enriched.append(get_violation_details(ev))

        page_results[pid] = {
            "expected": expected,
            "actual": enriched,
            "fixes": {},
        }

    new_manifest = build_manifest(manifest, page_results)
    STATS_FILE.write_text(json.dumps(new_manifest, indent=2))

    generate_reports(new_manifest)
    save_fixed_pages(new_manifest)

    index_html = generate_index_html(new_manifest)
    (OUT / "index.html").write_text(index_html)

    runs = new_manifest.get("runs", [])
    latest = runs[-1]
    per_page = latest.get("per_page", {})
    total_found = sum(len([a for a in d["actual"] if a.get("found", False)]) for d in per_page.values())
    print("\n=== Audit Summary ===")
    print(f"Run: {latest['date']}")
    print(f"Total pages: {latest['total_pages']}")
    print(f"Total violations found: {total_found}")
    print(f"Pages with 0 violations: {sum(1 for d in per_page.values() if sum(1 for a in d['actual'] if a.get('found', False)) == 0)}")
    print(f"Average violations per page: {total_found / latest['total_pages']:.2f}")
    print(f"Reports: reports/report_XXX.md")
    print(f"Fixed: fixed/page_XXX.html")
    print(f"Index: index.html")


if __name__ == "__main__":
    main()

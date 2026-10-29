"""Generate fixed pages and index.html with iteration-over-iteration charts."""

import ast
import json
import re
from pathlib import Path

OUT = Path("/tmp/wcag-test-pages")
PAGES_DIR = OUT / "pages"
FIXED_DIR = OUT / "fixed"
REPORTS_DIR = OUT / "reports"
STATS_DIR = REPORTS_DIR / "_stats"
STATS_FILE = STATS_DIR / "manifest.json"

KNOWN_VIOLATIONS = {
    "color-no-contrast": {
        "type": "Color/Contrast", "wcag": ["1.4.3", "1.4.6"],
        "desc": "Text color matches background — unreadable",
        "fix": "Increase text contrast.",
    },
    "color-red-green": {
        "type": "Color-Only", "wcag": ["1.4.1"],
        "desc": "Information conveyed only by color (e.g., red vs green indicators)",
        "fix": "Add text labels or icons alongside color indicators.",
    },
    "color-gray-light": {
        "type": "Color/Contrast", "wcag": ["1.4.3", "1.4.6"],
        "desc": "Light gray text on light background",
        "fix": "Darken text color or lighten background.",
    },
    "img-decorative-missing-alt": {
        "type": "Image", "wcag": ["1.1.1"],
        "desc": "Decorative image with missing alt attribute",
        "fix": "Add alt=\"\" to indicate the image is decorative.",
    },
    "img-no-alt-description": {
        "type": "Image", "wcag": ["1.1.1"],
        "desc": "Image has no alt text description",
        "fix": "Provide descriptive alt text.",
    },
    "img-meaningless-alt": {
        "type": "Image", "wcag": ["1.1.1"],
        "desc": "Image alt text is generic like 'image' or 'picture'",
        "fix": "Replace with descriptive alt text.",
    },
    "link-missing-name": {
        "type": "Link", "wcag": ["2.4.4", "1.1.1"],
        "desc": "Link image has no accessible name",
        "fix": "Add aria-label='Description of the link destination'.",
    },
    "link-placeholder": {
        "type": "Link", "wcag": ["2.4.4"],
        "desc": "Link text is non-descriptive like 'click here' or 'here'",
        "fix": "Replace with descriptive text.",
    },
    "link-empty-href": {
        "type": "Link", "wcag": ["2.1.1", "4.1.2"],
        "desc": "Link has href='#' with no real destination",
        "fix": "Remove href='#' or provide a real URL.",
    },
    "form-label-missing": {
        "type": "Form", "wcag": ["1.1.1", "4.1.2"],
        "desc": "Form input has no associated label or aria-label",
        "fix": "Add <label for='input-id'>Label text</label> or aria-label='Label'.",
    },
    "form-placeholder-only": {
        "type": "Form", "wcag": ["1.1.1", "4.1.2"],
        "desc": "Placeholder text used as the only label for an input field",
        "fix": "Add a visible label element in addition to the placeholder.",
    },
    "form-error-color-only": {
        "type": "Form", "wcag": ["1.4.1"],
        "desc": "Error message indicated only by color, not by text",
        "fix": "Add explicit text or an icon with aria-label.",
    },
    "form-input-id-mismatch": {
        "type": "Form", "wcag": ["1.1.1", "4.1.2"],
        "desc": "Input id does not match label for attribute",
        "fix": "Ensure label for='X' matches input id='X'.",
    },
    "heading-skip": {
        "type": "Heading", "wcag": ["1.3.1", "2.4.6"],
        "desc": "Heading hierarchy skips levels",
        "fix": "Restructure to use sequential heading levels.",
    },
    "heading-missing": {
        "type": "Heading", "wcag": ["1.3.1"],
        "desc": "Content looks like a heading but uses <p> or <div> with bold",
        "fix": "Use the appropriate heading element <h1>-<h6>.",
    },
    "heading-levels": {
        "type": "Heading", "wcag": ["1.3.1"],
        "desc": "Page jumps from h1 to h3, skipping h2",
        "fix": "Use proper sequential heading levels.",
    },
    "audio-autoplay": {
        "type": "Media", "wcag": ["1.4.2"],
        "desc": "Audio plays automatically on page load without user control",
        "fix": "Remove autoplay or provide a prominent pause control.",
    },
    "video-auto-caption": {
        "type": "Media", "wcag": ["1.2.2", "1.2.4"],
        "desc": "Video has no captions and no transcript",
        "fix": "Add <track kind='captions'> or link to a transcript page.",
    },
    "audio-decorative-silent": {
        "type": "Media", "wcag": ["1.4.2"],
        "desc": "Decorative sound plays automatically but cannot be stopped",
        "fix": "Stop the sound automatically after a short delay or let users disable it.",
    },
    "motion-flash": {
        "type": "Motion", "wcag": ["2.3.1"],
        "desc": "Content flashes rapidly (> 3 times per second), seizure risk",
        "fix": "Remove flash or slow to < 3 Hz.",
    },
    "motion-parallax": {
        "type": "Motion", "wcag": ["2.1.1"],
        "desc": "Parallax animation without reduced-motion support",
        "fix": "Add @media (prefers-reduced-motion: reduce) rule.",
    },
    "motion-autoplay-video": {
        "type": "Motion", "wcag": ["2.1.1"],
        "desc": "Video/GIF plays without user interaction and ignores reduced-motion",
        "fix": "Add a pause button and respect prefers-reduced-motion.",
    },
    "aria-live-overflow": {
        "type": "ARIA", "wcag": ["4.1.3"],
        "desc": "Live region updates exceed expected boundaries",
        "fix": "Use aria-busy and manage live region updates carefully.",
    },
    "keyboard-focus-trap": {
        "type": "Keyboard", "wcag": ["2.1.2"],
        "desc": "Focus is trapped within a modal or overlay with no escape",
        "fix": "Add Escape key handler to close modal.",
    },
    "keyboard-focus-invisible": {
        "type": "Keyboard", "wcag": ["2.4.7", "1.4.11"],
        "desc": "Focus indicator fails 3:1 contrast ratio",
        "fix": "Ensure focus ring meets 3:1 contrast minimum.",
    },
    "aria-hidden-live": {
        "type": "ARIA", "wcag": ["4.1.3"],
        "desc": "Live region container has aria-hidden='true'",
        "fix": "Remove aria-hidden from the live region container.",
    },
    "table-layout": {
        "type": "Table", "wcag": ["1.3.1"],
        "desc": "Table layout breaks column header associations",
        "fix": "Use <thead>, <th> elements with proper scope attributes.",
    },
    "table-complex": {
        "type": "Table", "wcag": ["1.3.1"],
        "desc": "Complex table with merged cells and missing scope attributes",
        "fix": "Add scope='col'/'row' to all <th> elements.",
    },
    "table-layout-fixed": {
        "type": "Table", "wcag": ["1.4.10"],
        "desc": "Fixed-width table squishes content",
        "fix": "Remove fixed width or allow text wrapping.",
    },
    "text-small": {
        "type": "Text", "wcag": ["1.4.3", "1.4.6"],
        "desc": "Body text is below 14px or fails contrast ratio",
        "fix": "Increase font size to 14px minimum or improve contrast.",
    },
    "text-justified": {
        "type": "Text", "wcag": ["1.4.8"],
        "desc": "Text is justified, which breaks word boundaries",
        "fix": "Use text-align: left or right instead of justify.",
    },
    "text-spaced": {
        "type": "Text", "wcag": ["1.4.12"],
        "desc": "Letter spacing exceeds 0.12em on body text",
        "fix": "Keep letter-spacing between -0.05em and 0.12em.",
    },
    "text-no-line-height": {
        "type": "Text", "wcag": ["1.4.12"],
        "desc": "Line height is 1.0 or 1, too tight for readability",
        "fix": "Set line-height to at least 1.5.",
    },
    "layout-fixed-width": {
        "type": "Layout", "wcag": ["1.4.10"],
        "desc": "Fixed width layout breaks when user zooms to 200%",
        "fix": "Use percentage-based or fluid widths.",
    },
    "layout-no-zoom": {
        "type": "Layout", "wcag": ["1.4.4"],
        "desc": "Browser zoom is disabled via viewport meta or CSS",
        "fix": "Remove user-scalable=no or minimum-scale restrictions.",
    },
    "layout-bad-focus": {
        "type": "Layout", "wcag": ["2.4.7"],
        "desc": "Focus is clipped or hidden by overflow: hidden on parent elements",
        "fix": "Remove overflow: hidden on elements that contain focusable children.",
    },
    "script-keyboard-missing": {
        "type": "Script", "wcag": ["2.1.1"],
        "desc": "Widget responds to mouse click but not keyboard",
        "fix": "Add keydown handlers for Enter and Space keys.",
    },
    "script-focus-order": {
        "type": "Script", "wcag": ["2.4.3"],
        "desc": "Focus order is non-linear, not matching visual reading order",
        "fix": "Ensure tab order matches visual reading order.",
    },
    "script-moving-focus": {
        "type": "Script", "wcag": ["2.5.2"],
        "desc": "Focus is moved automatically without user request",
        "fix": "Avoid auto-advancing elements, or let user control focus movement.",
    },
    "sr-reading-order": {
        "type": "Screen Reader", "wcag": ["1.3.2"],
        "desc": "Content order in HTML differs from visual order",
        "fix": "Reorder DOM elements so focus and reading order matches visual order.",
    },
    "sr-live-no-wait": {
        "type": "Screen Reader", "wcag": ["4.1.3"],
        "desc": "Live region announcement is too brief for processing",
        "fix": "Increase aria-live timeout or let users dismiss manually.",
    },
    "sr-decorative-role": {
        "type": "Screen Reader", "wcag": ["1.1.1"],
        "desc": "Element has role='img' but contains only decorative text",
        "fix": "Remove role='img' or add an accessible name.",
    },
    "language-unset": {
        "type": "Language", "wcag": ["3.1.1"],
        "desc": "Document has no lang attribute on <html>",
        "fix": "Add lang='en' (or appropriate language) to the <html> element.",
    },
    "language-partially": {
        "type": "Language", "wcag": ["3.1.1"],
        "desc": "Partial lang attribute does not match actual content language",
        "fix": "Set the correct lang attribute.",
    },
    "scroll-blocked": {
        "type": "Scrolling", "wcag": ["2.1.1"],
        "desc": "Horizontally scrolling content cannot be scrolled via keyboard",
        "fix": "Ensure all scrollable areas can be scrolled via keyboard.",
    },
    "scroll-small-target": {
        "type": "Scrolling", "wcag": ["2.5.5"],
        "desc": "Small clickable areas (under 44x44 CSS px)",
        "fix": "Increase clickable areas to at least 44x44 CSS px.",
    },
    "scroll-sticky-header": {
        "type": "Scrolling", "wcag": ["1.4.12"],
        "desc": "Sticky header partially obscures content when scrolling",
        "fix": "Make sticky headers collapsible or reduce height.",
    },
}


def parse_expected_violations(page_path: Path) -> list[dict]:
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
    desc = (ev.get("desc") or "").lower()
    wcags = ev.get("wcag", [])
    if "contrast" in desc or "color" in desc:
        return "color-no-contrast"
    if "decorative" in desc and "alt" in desc:
        return "img-decorative-missing-alt"
    if "alt" in desc and ("meaningless" in desc or "generic" in desc):
        return "img-meaningless-alt"
    if "no alt" in desc or "missing alt" in desc or ("alt" in desc and "label" in desc):
        return "img-no-alt-description"
    if "label" in desc and ("no" in desc or "missing" in desc):
        return "form-label-missing"
    if "placeholder" in desc and "label" in desc:
        return "form-placeholder-only"
    if "error" in desc and "color" in desc:
        return "form-error-color-only"
    if "heading" in desc or "skip" in desc or "level" in desc:
        return "heading-skip"
    if "autoplay" in desc or "sound" in desc:
        return "audio-autoplay"
    if "flash" in desc:
        return "motion-flash"
    if "table" in desc:
        return "table-layout"
    if "justif" in desc:
        return "text-justified"
    if "small" in desc and ("text" in desc or "font" in desc):
        return "text-small"
    if "aria-hidden" in desc or "aria-live" in desc:
        return "aria-hidden-live"
    if "language" in desc:
        return "language-unset"
    if "scroll" in desc:
        return "scroll-blocked"
    if "link" in desc and "placeholder" in desc:
        return "link-placeholder"
    if "id" in desc and "mismatch" in desc:
        return "form-input-id-mismatch"
    if "empty" in desc and "href" in desc:
        return "link-empty-href"
    if "focus" in desc:
        if "trap" in desc:
            return "keyboard-focus-trap"
        if "invisible" in desc or "contrast" in desc:
            return "keyboard-focus-invisible"
        return "keyboard-focus-trap"
    if "live" in desc:
        return "aria-live-overflow"
    if "audio" in desc or "sound" in desc:
        return "audio-decorative-silent"
    if "captions" in desc:
        return "video-auto-caption"
    if "parallax" in desc or "animation" in desc or "autoplay" in desc:
        return "motion-parallax"
    if "focus order" in desc:
        return "script-focus-order"
    if "non-linear" in desc:
        return "script-focus-order"
    if "reading order" in desc:
        return "sr-reading-order"
    if "aria" in desc and "img" in desc:
        return "sr-decorative-role"
    if "gesture" in desc or "touch" in desc or "44" in desc:
        return "scroll-small-target"
    return "heading-skip"


def get_violation_details(ev: dict) -> dict:
    vtype = find_violation_type(ev)
    info = KNOWN_VIOLATIONS.get(vtype, ev)
    return {
        "type": vtype,
        "type_display": info.get("type", ev.get("type", "Unknown")),
        "wcag": ev.get("wcag", []),
        "desc": ev.get("desc", ""),
        "fix": info.get("fix", "Apply general accessibility best practices."),
    }


def generate_fixed_page(page_path: Path) -> str:
    text = page_path.read_text()
    fixed_text = text

    # Add prefers-reduced-motion support
    if "@media (prefers-reduced-motion: reduce)" not in fixed_text:
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

    # Remove "L" markers and layer comments
    fixed_text = re.sub(r"<!-- L\d+:.*?-->", "", fixed_text)

    # Remove detection helper classes
    fixed_text = re.sub(r"\.contrast-red-on-red\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.contrast-gray-on-white\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.contrast-light-gray-on-white\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.color-only\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.color-pill\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.img-issue\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.link-placeholder\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.link-placeholder:hover\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.form-issue\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.form-issue\s+input\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.form-issue\s+label\s*\{[^}]*\}", "", fixed_text)
    fixed_text = re.sub(r"\.keyboard-trap\s*area\s*\{[^}]*\}", "", fixed_text)

    return fixed_text


def save_fixed_pages():
    FIXED_DIR.mkdir(exist_ok=True)
    page_files = sorted(PAGES_DIR.glob("page_*.html"))

    for page_path in page_files:
        pid = page_path.stem.replace("page_", "")
        print(f"  Generating fixed page {pid}...", end=" ", flush=True)
        fixed_html = generate_fixed_page(page_path)
        (FIXED_DIR / f"page_{pid}.html").write_text(fixed_html)
        print("done")


def generate_index_html():
    manifest = STATS_FILE.exists() and json.loads(STATS_FILE.read_text()) or {"runs": []}
    runs = manifest.get("runs", [])
    if not runs:
        return "<html><body><p>No audit runs yet.</p></body></html>"

    all_page_results = {}
    for run in runs:
        for pid, data in run.get("per_page", {}).items():
            if pid not in all_page_results:
                all_page_results[pid] = {"counts": []}
            all_page_results[pid]["counts"].append(len([a for a in data.get("actual", []) if a.get("found", False)]))

    per_page = {}
    for pid, info in sorted(all_page_results.items()):
        counts = info["counts"]
        per_page[pid] = {
            "all_counts": counts,
            "latest_count": counts[-1] if counts else 0,
        }

    total_pages = len(per_page)
    latest = runs[-1]
    date = latest.get("date", "N/A")

    all_counts = [len([a for a in d["actual"] if a.get("found", False)]) for d in latest.get("per_page", {}).values()]
    pages_zero = sum(1 for c in all_counts if c == 0)
    pages_hard = sum(1 for c in all_counts if c >= 4)
    max_v = max(all_counts) if all_counts else 0
    avg_v = sum(all_counts) / len(all_counts) if all_counts else 0

    # Build JS arrays as Python lists, inject into template
    run_dates = [run["date"] for run in runs]
    iter_data = []
    total = 0
    for run in runs:
        total += run.get("total_violations", 0)
        iter_data.append(total)

    wcag_data = {"1.4.3": "Contrast", "1.4.6": "Contrast AAA", "1.4.1": "Color-Only",
                 "1.1.1": "Image/Label", "4.1.2": "Form Label", "1.4.8": "Justify",
                 "1.4.10": "Table Layout", "1.4.12": "Text Spacing", "2.4.4": "Link Purpose",
                 "2.1.1": "Keyboard", "2.5.5": "Touch Target", "1.3.1": "Heading/Table",
                 "3.1.1": "Language", "4.1.3": "ARIA Live", "2.4.7": "Focus Visible",
                 "2.1.2": "Focus Trap", "1.4.2": "Autoplay", "2.3.1": "Motion",
                 "1.2.2": "Captions", "1.4.4": "Zoom"}
    wcag_colors = ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c','#3498db',
                   '#9b59b6','#e91e63','#00bcd4','#ff5722','#673ab7','#8bc34a',
                   '#ff9800','#4caf50','#795548','#e74c3c','#e67e22','#f1c40f',
                   '#2ecc71','#1abc9c']
    all_type_names = ["Color/Contrast", "Color-Only", "Image", "Link", "Form",
                      "Heading", "Table", "Motion", "Text", "Layout", "Keyboard",
                      "ARIA", "Language", "Scrolling", "Media", "Screen Reader"]
    type_counts = {}
    for d in latest.get("per_page", {}).values():
        for a in d.get("actual", []):
            t = a.get("type", "Unknown")
            type_counts[t] = type_counts.get(t, 0) + 1

    sorted_type_counts = [(k, type_counts.get(k, 0)) for k in all_type_names]

    sorted_pages = sorted(per_page.items(), key=lambda x: x[1]["latest_count"], reverse=True)
    page_labels = [f"page_{p[0]}" for p in sorted_pages[:15]]
    page_iter_data = [p[1]["all_counts"] for p in sorted_pages[:15]]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WCAG Test Pages — Audit Dashboard</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#333;background:#f5f7fa;padding:40px 20px;max-width:1200px;margin:0 auto}}
h1{{font-size:2.2em;margin-bottom:8px}}
h2{{font-size:1.5em;margin:30px 0 15px;padding-bottom:8px;border-bottom:2px solid #3498db}}
.summary-cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:30px}}
.card{{background:#fff;border-radius:10px;padding:20px;box-shadow:0 2px 6px rgba(0,0,0,.08);text-align:center}}
.card .value{{font-size:2.5em;font-weight:700;color:#3498db;line-height:1.2}}
.card .label{{color:#666;font-size:.9em;margin-top:4px}}
.chart-container{{background:#fff;border-radius:10px;padding:20px;box-shadow:0 2px 6px rgba(0,0,0,.08);margin-bottom:30px}}
.chart-container canvas{{max-height:400px}}
table{{width:100%;border-collapse:collapse;margin-bottom:30px;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 6px rgba(0,0,0,.08)}}
th{{background:#3498db;color:#fff;padding:12px 16px;text-align:left;font-weight:600}}
td{{padding:10px 16px;border-bottom:1px solid #eee}}
tr:hover{{background:#f8f9fa}}
.badge{{display:inline-block;padding:4px 10px;border-radius:12px;font-size:.85em;font-weight:600;margin:2px}}
.badge-pass{{background:#d4edda;color:#155724}}
.badge-fail{{background:#f8d7da;color:#721c24}}
.badge-warn{{background:#fff3cd;color:#856404}}
footer{{text-align:center;color:#888;padding:20px 0;font-size:.9em}}
a{{color:#3498db;text-decoration:none}}
a:hover{{text-decoration:underline}}
</style>
</head>
<body>

<h1>🧪 WCAG Test Pages — Audit Dashboard</h1>
<p>Accessibility audit results for <strong>{total_pages}</strong> test pages.
Audited on <strong>{date}</strong>.</p>

<div class="summary-cards">
  <div class="card"><div class="value">{pages_zero}</div><div class="label">Pages with 0 Violations</div></div>
  <div class="card"><div class="value">{pages_hard}</div><div class="label">Pages with 4+ Violations</div></div>
  <div class="card"><div class="value">{max_v}</div><div class="label">Max Violations (Single Page)</div></div>
  <div class="card"><div class="value">{avg_v:.1f}</div><div class="label">Avg Violations Per Page</div></div>
</div>

<h2>📊 Total Violations Over Iterations</h2>
<div class="chart-container"><canvas id="iterationChart"></canvas></div>

<h2>📊 Violations by WCAG Success Criterion (Latest Run)</h2>
<div class="chart-container"><canvas id="wcagChart"></canvas></div>

<h2>📊 Violations by Type (Latest Run)</h2>
<div class="chart-container"><canvas id="typeChart"></canvas></div>

<h2>📈 Per-Page Improvement Over Iterations</h2>
<div class="chart-container"><canvas id="improvementChart"></canvas></div>

<h2>📄 Individual Page Results</h2>
<table>
  <thead><tr><th>Page</th><th>001</th><th>025</th><th>050</th><th>075</th><th>100</th><th>Latest</th><th>Fixed</th><th>Status</th></tr></thead>
  <tbody>"""

    for pid, info in sorted_pages[:20]:
        counts = info["all_counts"]
        n = len(counts)
        cols = []
        for idx in [0, 24, 49, 74, 99]:
            if idx < n:
                cols.append(f"<td>{counts[idx]}</td>")
            else:
                cols.append("<td>—</td>")
        cols.append(f"<td>{info['latest_count']}</td>")
        fixed_exists = (FIXED_DIR / f"page_{pid}.html").exists()
        cols.append(f"<td>{'🔧' if fixed_exists else '—'}</td>")
        if info["latest_count"] == 0:
            status = '<span class="badge badge-pass">✅ Clean</span>'
        elif info["latest_count"] >= 4:
            status = '<span class="badge badge-fail">❌ High</span>'
        elif info["latest_count"] >= 2:
            status = '<span class="badge badge-warn">⚠️ Med</span>'
        else:
            status = '<span class="badge badge-pass">✅ Low</span>'
        html += f"  <tr><td>page_{pid}.html</td>{''.join(cols)}<td>{status}</td></tr>\n"

    html += "  </tbody></table>\n"
    html += "<footer><p>Generated by <a href=\"https://github.com/turbolego/wcag-skill\">wcag-skill</a> · <a href=\"https://github.com/kveita/wcag-test-pages\">kveita/wcag-test-pages</a></p></footer>\n"

    # JS section
    html += "<script>\n"
    html += f"const iterDates = {json.dumps(run_dates)};\n"
    html += f"const iterData = {json.dumps(iter_data)};\n"
    html += "const wcagLabels = " + json.dumps(list(wcag_data.values())) + ";\n"
    html += "const wcagColors = " + json.dumps(wcag_colors) + ";\n"
    html += "const typeCounts = " + json.dumps(dict(sorted_type_counts)) + ";\n"
    html += "const allTypeNames = " + json.dumps(all_type_names) + ";\n"
    html += "const pageLabels = " + json.dumps(page_labels) + ";\n"
    html += "const pageIterData = " + json.dumps(page_iter_data) + ";\n"

    html += """
new Chart(document.getElementById('iterationChart'),{
  type:'line',
  data:{{
    labels:iterDates.map(d=>d.split('T')[0]),
    datasets:[{{
      label:'Total Violations',
      data:iterData,
      borderColor:'#e74c3c',
      backgroundColor:'rgba(231,76,60,0.1)',
      tension:.3,
      fill:true
    }}]
  }},
  options:{{
    responsive:true,
    plugins:{{
      legend:{display:false},
      tooltip:{callbacks:{{label:ctx=>`Total: ${{ctx.parsed.y}} violations`}}}}
    }},
    scales:{{
      y:{beginAtZero:true,ticks:{stepSize:5},title:{display:true,text:'Total Violations'}}}
    }}
  }}
}});

new Chart(document.getElementById('wcagChart'),{
  type:'bar',
  data:{{
    labels:wcagLabels.filter((v,i)=>typeCounts[Object.keys(typeCounts)[i]]>0),
    datasets:[{{
      label:'Count',
      data:wcagLabels.filter((v,i)=>typeCounts[Object.keys(typeCounts)[i]]>0).map((_,i)=>Object.values(typeCounts)[i]),
      backgroundColor:wcagColors,
      borderWidth:1
    }}]
  }},
  options:{{
    responsive:true,
    maintainAspectRatio:false,
    plugins:{{
      legend:{display:false},
      tooltip:{callbacks:{{label:ctx=>`${{ctx.parsed.y}} pages`}}}}
    }},
    scales:{{
      y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Number of Pages'}}}
    }}
  }}
}});

new Chart(document.getElementById('typeChart'),{
  type:'bar',
  data:{{
    labels:allTypeNames.filter(t=>typeCounts[t]>0),
    datasets:[{{
      label:'Count',
      data:allTypeNames.filter(t=>typeCounts[t]>0).map(t=>typeCounts[t]),
      backgroundColor:allTypeNames.filter(t=>typeCounts[t]>0).map((_,i)=>wcagColors[i%15]),
      borderWidth:1
    }}]
  }},
  options:{{
    responsive:true,
    maintainAspectRatio:false,
    plugins:{{
      legend:{display:false},
      tooltip:{callbacks:{{label:ctx=>`${{ctx.parsed.y}} pages`}}}}
    }},
    scales:{{
      y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Number of Pages'}}}
    }}
  }}
}});

new Chart(document.getElementById('improvementChart'),{
  type:'line',
  data:{{
    labels:iterDates.map(d=>d.split('T')[0]),
    datasets:pageIterData.map((counts,i)=>({{
      label:pageLabels[i],
      data:counts,
      borderColor:wcagColors[i%15],
      tension:.3,
      pointRadius:2
    }}))
  }},
  options:{{
    responsive:true,
    maintainAspectRatio:false,
    plugins:{{
      legend:{display:true,position:'top'},
      tooltip:{callbacks:{{label:ctx=>`${{ctx.dataset.label}}: ${{ctx.parsed.y}} violations`}}}}
    }},
    scales:{{
      x:{ticks:{maxRotation:90,minRotation:45,font:{size:10}}},
      y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Violations'}}}
    }}
  }}
}});
</script></body></html>"""

    return html


def main():
    FIXED_DIR.mkdir(exist_ok=True)
    print("Generating fixed pages...")
    save_fixed_pages()
    print("Generating index.html...")
    index_html = generate_index_html()
    (OUT / "index.html").write_text(index_html)
    print("Done! Fixed pages: fixed/page_XXX.html | Index: index.html")


if __name__ == "__main__":
    main()

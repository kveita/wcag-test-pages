import json, ast, re
from pathlib import Path
from collections import Counter

OUT = Path("/tmp/wcag-test-pages")
PAGES_DIR = OUT / "pages"
FIXED_DIR = OUT / "fixed"
REPORTS_DIR = OUT / "reports"
STATS_DIR = REPORTS_DIR / "_stats"
STATS_FILE = STATS_DIR / "manifest.json"

VIOLATION_PATTERNS = [
    {"type":"color-no-contrast","wcag":["1.4.3","1.4.6"],"selector": r'\.contrast-red-on-red'},
    {"type":"color-no-contrast","wcag":["1.4.3","1.4.6"],"selector": r'\.contrast-gray-on-white'},
    {"type":"color-no-contrast","wcag":["1.4.3","1.4.6"],"selector": r'\.contrast-light-gray-on-white'},
    {"type":"color-red-green","wcag":["1.4.1"],"selector": r'\.color-pill'},
    {"type":"img-decorative-missing-alt","wcag":["1.1.1"],"selector": r'img[alt=""][aria-label=""]'},
    {"type":"img-meaningless-alt","wcag":["1.1.1"],"selector": r'img[alt="image"]'},
    {"type":"img-no-alt-description","wcag":["1.1.1"],"selector": r'img:not([alt=""])'},
    {"type":"link-placeholder","wcag":["2.4.4"],"text": "here"},
    {"type":"link-placeholder","wcag":["2.4.4"],"text": "click here"},
    {"type":"link-empty-href","wcag":["2.1.1","4.1.2"],"selector": r'a[href="#"]'},
    {"type":"form-label-missing","wcag":["1.1.1","4.1.2"],"selector": r'input:not([aria-label])'},
    {"type":"form-placeholder-only","wcag":["1.1.1","4.1.2"],"selector": r'input[placeholder]'},
    {"type":"form-error-color-only","wcag":["1.4.1"],"selector": r'\.error-text'},
    {"type":"form-input-id-mismatch","wcag":["1.1.1","4.1.2"],"selector": r'input'},
    {"type":"heading-skip","wcag":["1.3.1"],"selector": r'h2'},
    {"type":"heading-missing","wcag":["1.3.1"],"selector": r'p[style*="font-weight: bold"]'},
    {"type":"table-layout","wcag":["1.3.1"],"selector": r'table'},
    {"type":"table-layout-fixed","wcag":["1.4.10"],"selector": r'table[style*="width: 100%"]'},
    {"type":"table-complex","wcag":["1.3.1"],"selector": r'th'},
    {"type":"text-small","wcag":["1.4.3","1.4.6"],"selector": r'\.small-text'},
    {"type":"text-justified","wcag":["1.4.8"],"selector": r'\.justified-text'},
    {"type":"text-spaced","wcag":["1.4.12"],"selector": r'\.spaced-text'},
    {"type":"text-no-line-height","wcag":["1.4.12"],"selector": r'\.tight-text'},
    {"type":"layout-fixed-width","wcag":["1.4.10"],"selector": r'\.layout-fixed'},
    {"type":"layout-no-zoom","wcag":["1.4.4"],"selector": r'meta[name="viewport"]'},
    {"type":"keyboard-focus-invisible","wcag":["2.4.7","1.4.11"],"selector": r':focus'},
    {"type":"script-keyboard-missing","wcag":["2.1.1"],"selector": r'button[onclick]'},
    {"type":"aria-live-overflow","wcag":["4.1.3"],"selector": r'[role="alert"][aria-hidden]'},
    {"type":"aria-hidden-live","wcag":["4.1.3"],"selector": r'[role="alert"][aria-hidden]'},
    {"type":"sr-decorative-role","wcag":["1.1.1"],"selector": r'[role="img"]'},
    {"type":"language-unset","wcag":["3.1.1"],"selector": r'<html'},
    {"type":"scroll-blocked","wcag":["2.1.1"],"selector": r'overflow'},
    {"type":"scroll-small-target","wcag":["2.5.5"],"selector": r'a'},
    {"type":"motion-flash","wcag":["2.3.1"],"selector": r'\.motion-flash'},
    {"type":"motion-parallax","wcag":["2.1.1"],"selector": r'\.motion-parallax'},
    {"type":"motion-autoplay-video","wcag":["2.1.1"],"selector": r'video'},
    {"type":"audio-autoplay","wcag":["1.4.2"],"selector": r'audio[autoplay]'},
    {"type":"audio-decorative-silent","wcag":["1.4.2"],"selector": r'audio[autoplay]'},
    {"type":"video-auto-caption","wcag":["1.2.2","1.2.4"],"selector": r'video'},
]

FIX_MAP = {
    "color-no-contrast": "Increase text contrast ratio to 7:1 minimum; use dark text on light backgrounds or vice versa.",
    "color-red-green": "Add text labels or icons alongside color indicators.",
    "color-gray-light": "Darken text color or lighten background color.",
    "img-decorative-missing-alt": "Add alt='' to decorative images.",
    "img-meaningless-alt": "Replace alt='image' with descriptive text.",
    "img-no-alt-description": "Add descriptive alt text to the image.",
    "link-placeholder": "Replace 'click here' with descriptive link text like 'Learn more about X'.",
    "link-empty-href": "Remove href='#' or use a real URL.",
    "form-label-missing": "Add <label for='input-id'>Label text</label> or aria-label='Label'.",
    "form-placeholder-only": "Add a visible <label> element alongside the placeholder.",
    "form-error-color-only": "Add explicit text error message.",
    "form-input-id-mismatch": "Ensure label for='X' matches input id='X'.",
    "heading-skip": "Restructure heading hierarchy so each level follows sequentially.",
    "heading-missing": "Use <h1>-<h6> for heading elements.",
    "table-layout": "Use proper <thead> <th> for table headers.",
    "table-layout-fixed": "Remove fixed width or allow text wrapping.",
    "table-complex": "Add scope='col'/'row' to header cells.",
    "text-small": "Increase font size to 14px minimum or improve contrast to 7:1.",
    "text-justified": "Use text-align: left or right instead of justify.",
    "text-spaced": "Reduce letter-spacing to 0.12em or less.",
    "text-no-line-height": "Set line-height to at least 1.5.",
    "layout-fixed-width": "Use percentage-based widths.",
    "layout-no-zoom": "Remove user-scalable=no restrictions.",
    "keyboard-focus-invisible": "Add visible focus indicator with 3:1 contrast ratio.",
    "script-keyboard-missing": "Add keydown handlers for Enter and Space keys.",
    "aria-live-overflow": "Manage live region updates properly.",
    "aria-hidden-live": "Remove aria-hidden from live regions.",
    "sr-decorative-role": "Add aria-label or remove role='img'.",
    "language-unset": "Add lang='en' to <html>.",
    "scroll-blocked": "Ensure keyboard-accessible scrolling.",
    "scroll-small-target": "Increase to 44x44 CSS px.",
    "motion-flash": "Remove flash pattern or slow to < 3 Hz.",
    "motion-parallax": "Add @media (prefers-reduced-motion: reduce).",
    "motion-autoplay-video": "Add pause button and respect reduced motion.",
    "audio-autoplay": "Remove autoplay or add pause control.",
    "audio-decorative-silent": "Stop sound automatically or let users disable.",
    "video-auto-caption": "Add <track kind='captions'> or transcript.",
}


def parse_expected(text):
    m = re.search(r'window\.__wcag_test_page\s*=\s*({.*?});\s*</script>', text, re.DOTALL)
    if not m: return []
    try:
        data = ast.literal_eval(m.group(1))
        return data.get("violations", [])
    except Exception:
        return []


def detect(text):
    found = []
    for p in VIOLATION_PATTERNS:
        sel = p.get("selector")
        txt = p.get("text")
        if sel and re.search(sel, text, re.IGNORECASE | re.DOTALL):
            found.append(p)
        elif txt and txt.lower() in text.lower():
            found.append(p)
    return found


def generate_fixed_page(page_path):
    text = page_path.read_text()
    fixed_text = text
    if "@media (prefers-reduced-motion: reduce)" not in fixed_text:
        fixed_text = fixed_text.replace(
            "* {{ margin: 0; padding: 0; box-sizing: border-box; }}",
            "* {{ margin: 0; padding: 0; box-sizing: border-box; }}\n  @media (prefers-reduced-motion: reduce) {{\n    *, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }}\n  }}"
        )
    fixed_text = fixed_text.replace(
        "a:focus, button:focus, input:focus {{ outline: none; }}",
        "a:focus, button:focus, input:focus {{ outline: 3px solid #3498db; outline-offset: 2px; }}"
    )
    fixed_text = fixed_text.replace(
        '<a href="#main-content" class="skip-link">Skip to main content</a>',
        '<a href="#main-content" class="skip-link">Skip to main content</a><main id="main-content">'
    )
    fixed_text = fixed_text.replace("</body></html>", "</main></body></html>")
    fixed_text = re.sub(r"<!-- L\d+:.*?-->", "", fixed_text)
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
        violations = detect(page_path.read_text())
        if violations:
            (FIXED_DIR / f"page_{pid}.html").write_text(generate_fixed_page(page_path))
            print(f"  Fixed page {pid} ({len(violations)} issues)")


def build_index_html():
    manifest = STATS_FILE.exists() and json.loads(STATS_FILE.read_text()) or {"runs": []}
    runs = manifest.get("runs", [])
    if not runs: return "<html><body><p>No audit runs yet.</p></body></html>"
    wcag_data = {"1.4.3": "Contrast", "1.4.6": "Contrast AAA", "1.4.1": "Color-Only",
                 "1.1.1": "Image/Label", "4.1.2": "Form Label", "1.4.8": "Justify",
                 "1.4.10": "Table Layout", "1.4.12": "Text Spacing", "2.4.4": "Link Purpose",
                 "2.1.1": "Keyboard", "2.5.5": "Touch Target", "1.3.1": "Heading/Table",
                 "3.1.1": "Language", "4.1.3": "ARIA Live", "2.4.7": "Focus Visible",
                 "2.1.2": "Focus Trap", "1.4.2": "Autoplay", "2.3.1": "Motion",
                 "1.2.2": "Captions", "1.4.4": "Zoom"}
    wcag_colors = ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#1abc9c','#3498db',
                   '#9b59b6','#e91e63','#00bcd4','#ff5722','#673ab7','#8bc34a',
                   '#ff9800','#4caf50','#795548']
    all_type_names = ["Color/Contrast", "Color-Only", "Image", "Link", "Form",
                      "Heading", "Table", "Motion", "Text", "Layout", "Keyboard",
                      "ARIA", "Language", "Scrolling", "Media", "Screen Reader"]
    per_page = {}
    for run in runs:
        for pid, data in run.get("per_page", {}).items():
            if pid not in per_page: per_page[pid] = {"counts": []}
            per_page[pid]["counts"].append(len(data.get("actual", [])))
    for pid, info in per_page.items(): info["latest_count"] = info["counts"][-1] if info["counts"] else 0
    total_pages = len(per_page)
    latest = runs[-1]
    date = latest.get("date", "N/A")
    all_counts = [info["latest_count"] for info in per_page.values()]
    pages_zero = sum(1 for c in all_counts if c == 0)
    pages_hard = sum(1 for c in all_counts if c >= 4)
    max_v = max(all_counts) if all_counts else 0
    avg_v = sum(all_counts) / len(all_counts) if all_counts else 0
    type_counts = {}
    for d in latest.get("per_page", {}).values():
        for a in d.get("actual", []):
            t = a.get("type", "Unknown")
            type_counts[t] = type_counts.get(t, 0) + 1
    sorted_type_counts = [(k, type_counts.get(k, 0)) for k in all_type_names]
    sorted_pages = sorted(per_page.items(), key=lambda x: x[1]["latest_count"], reverse=True)
    page_labels = [f"page_{p[0]}" for p in sorted_pages[:15]]
    page_iter_data = [p[1]["counts"] for p in sorted_pages[:15]]
    run_dates = [run["date"] for run in runs]
    iter_data = []
    total = 0
    for run in runs: total += run.get("total_violations", 0); iter_data.append(total)
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
        counts = info["counts"]
        n = len(counts)
        cols = []
        for idx in [0, 24, 49, 74, 99]:
            cols.append(f"<td>{counts[idx]}</td>" if idx < n else "<td>—</td>")
        cols.append(f"<td>{info['latest_count']}</td>")
        fixed_exists = (FIXED_DIR / f"page_{pid}.html").exists()
        cols.append(f"<td>{'🔧' if fixed_exists else '—'}</td>")
        if info["latest_count"] == 0: status = '<span class="badge badge-pass">✅ Clean</span>'
        elif info["latest_count"] >= 4: status = '<span class="badge badge-fail">❌ High</span>'
        elif info["latest_count"] >= 2: status = '<span class="badge badge-warn">⚠️ Med</span>'
        else: status = '<span class="badge badge-pass">✅ Low</span>'
        html += f"  <tr><td>page_{pid}.html</td>{''.join(cols)}<td>{status}</td></tr>\n"
    html += "  </tbody></table>\n"
    html += "<footer><p>Generated by <a href=\"https://github.com/turbolego/wcag-skill\">wcag-skill</a> · <a href=\"https://github.com/kveita/wcag-test-pages\">kveita/wcag-test-pages</a></p></footer>\n"
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
  type:'line',data:{labels:iterDates.map(d=>d.split('T')[0]),datasets:[{label:'Total Violations',data:iterData,borderColor:'#e74c3c',backgroundColor:'rgba(231,76,60,0.1)',tension:.3,fill:true}]},
  options:{responsive:true,plugins:{legend:{display:false},tooltip:{callbacks:{{label:ctx=>`Total: ${{ctx.parsed.y}} violations`}}}},scales:{y:{beginAtZero:true,ticks:{stepSize:5},title:{display:true,text:'Total Violations'}}}}}
}});

new Chart(document.getElementById('wcagChart'),{
  type:'bar',data:{labels:wcagLabels.filter((v,i)=>typeCounts[Object.keys(typeCounts)[i]]>0),datasets:[{label:'Count',data:wcagLabels.filter((v,i)=>typeCounts[Object.keys(typeCounts)[i]]>0).map((_,i)=>Object.values(typeCounts)[i]),backgroundColor:wcagColors,borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{{label:ctx=>`${{ctx.parsed.y}} pages`}}}},scales:{y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Number of Pages'}}}}}}
}});

new Chart(document.getElementById('typeChart'),{
  type:'bar',data:{labels:allTypeNames.filter(t=>typeCounts[t]>0),datasets:[{label:'Count',data:allTypeNames.filter(t=>typeCounts[t]>0).map(t=>typeCounts[t]),backgroundColor:allTypeNames.filter(t=>typeCounts[t]>0).map((_,i)=>wcagColors[i%15]),borderWidth:1}]},
  options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{{label:ctx=>`${{ctx.parsed.y}} pages`}}}},scales:{y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Number of Pages'}}}}}}
}});

new Chart(document.getElementById('improvementChart'),{
  type:'line',data:{labels:iterDates.map(d=>d.split('T')[0]),datasets:pageIterData.map((counts,i)=>({label:pageLabels[i],data:counts,borderColor:wcagColors[i%15],tension:.3,pointRadius:2}))},
  options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:true,position:'top'},tooltip:{callbacks:{{label:ctx=>`${{ctx.dataset.label}}: ${{ctx.parsed.y}} violations`}}}},scales:{x:{ticks:{maxRotation:90,minRotation:45,font:{size:10}}},y:{beginAtZero:true,ticks:{stepSize:1},title:{display:true,text:'Violations'}}}}}
}});
</script></body></html>"""
    return html


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    FIXED_DIR.mkdir(exist_ok=True)
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)

    page_files = sorted(PAGES_DIR.glob("page_*.html"))
    total = len(page_files)
    print(f"Scanning {total} pages for violations...")
    page_results = {}
    all_wcags = Counter()
    all_types = Counter()
    for path in page_files:
        pid = path.stem.replace("page_", "")
        text = path.read_text()
        expected = parse_expected(text)
        detected = detect(text)
        for p in detected:
            for w in p["wcag"]: all_wcags[w] += 1
            all_types[p["type"]] += 1
        page_results[pid] = {"expected": expected, "actual": detected}
        print(f"  page {pid}: {len(expected)} expected, {len(detected)} detected")

    manifest = {
        "runs": [{
            "date": "2026-10-29T04:00:00Z",
            "total_pages": total,
            "total_violations": sum(len(v["actual"]) for v in page_results.values()),
            "per_page": {pid: {"expected": data["expected"], "actual": data["actual"],
                                  "stats": {"coverage": "N/A", "accuracy": "N/A"}}
                         for pid, data in page_results.items()},
        }],
    }
    STATS_FILE.write_text(json.dumps(manifest, indent=2))

    for pid, data in sorted(page_results.items()):
        expected = data["expected"]
        actual = data["actual"]
        lines = [
            f"# WCAG Test Page {pid} — Accessibility Audit Report",
            "",
            f"**Page URL:** `pages/page_{pid}.html`",
            "**Run Date:** 2026-10-29",
            f"**Total Expected Violations:** {len(expected)}",
            f"**Total Detected Violations:** {len(actual)}",
            "",
            "## Summary",
            f"- Expected: {len(expected)} | Detected: {len(actual)} | Coverage: {len(actual)/max(len(expected),1)*100:.0f}%",
            "",
            "## Expected Violations",
            "",
        ]
        for ev in expected:
            found = any(p["type"] == ev["type"] for p in actual)
            status = "✅ Found" if found else "❌ Missing"
            lines.append(f"- [{status}] {ev.get('desc','')[:80]} — WCAG {', '.join(ev.get('wcag',[]))}")
        lines.extend(["", "## Detected Violations", ""])
        for p in actual:
            lines.append(f"- **{p['type']}** (WCAG {p['wcag']})")
            lines.append(f"  - Selector: {p.get('selector', p['type'])}")
        lines.extend(["", "## Fixes", ""])
        for p in actual:
            lines.append(f"- [{p['type']}] {FIX_MAP.get(p['type'], 'Review best practices.')}")
        lines.extend(["", "*Page: [pages/page_{pid}.html](pages/page_{pid}.html)*"])
        (REPORTS_DIR / f"report_{pid}.md").write_text("\n".join(lines))

    print(f"\n=== Summary ===")
    print(f"Total expected: {sum(len(d['expected']) for d in page_results.values())}")
    print(f"Total detected: {sum(len(d['actual']) for d in page_results.values())}")
    print(f"By type: {dict(all_types.most_common(10))}")
    print(f"By WCAG: {dict(all_wcags.most_common(10))}")

    print("Generating fixed pages...")
    save_fixed_pages()

    print("Generating index.html...")
    index_html = build_index_html()
    (OUT / "index.html").write_text(index_html)
    print("Done! Fixed pages: fixed/page_XXX.html | Index: index.html")


if __name__ == "__main__":
    main()

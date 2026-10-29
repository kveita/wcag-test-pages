import ast, json, re
from pathlib import Path
from collections import Counter

OUT = Path("/tmp/wcag-test-pages")
PAGES_DIR = OUT / "pages"
REPORTS_DIR = OUT / "reports"
STATS_FILE = REPORTS_DIR / "_stats" / "manifest.json"

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


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)

    pages = sorted(PAGES_DIR.glob("page_*.html"))
    total = len(pages)
    print(f"Scanning {total} pages for violations...")

    page_results = {}
    all_wcags = Counter()
    all_types = Counter()

    for path in pages:
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
            "date": "2026-10-29T03:00:00Z",
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
            lines.append(f"  - Desc: {p.get('desc', p['type'])}")
            if 'selector' in p: lines.append(f"  - Selector: {p['selector']}")

        lines.extend(["", "## Fixes", ""])
        for p in actual:
            lines.append(f"- [{p['type']}] {FIX_MAP.get(p['type'], 'Review best practices.')}")

        lines.extend(["", "*Page: [pages/page_{pid}.html](pages/page_{pid}.html)*"])
        (REPORTS_DIR / f"report_{pid}.md").write_text("\n".join(lines))

    print("\n=== Summary ===")
    print(f"Total expected: {sum(len(d['expected']) for d in page_results.values())}")
    print(f"Total detected: {sum(len(d['actual']) for d in page_results.values())}")
    print(f"By type: {dict(all_types.most_common(10))}")
    print(f"By WCAG: {dict(all_wcags.most_common(10))}")


if __name__ == "__main__":
    main()

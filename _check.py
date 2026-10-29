import json
m = json.loads(open("reports/_stats/manifest.json").read())
r = m["runs"][-1]
print(r["total_pages"], r["total_violations"])
print(sum(len(p.get("actual",[])) for p in r["per_page"].values()))

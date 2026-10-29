import json, sys
d = json.load(sys.stdin)
print(d.get("status"), d.get("commit","")[:10])

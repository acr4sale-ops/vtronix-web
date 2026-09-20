#!/usr/bin/env python3
"""Requests every URL in vtronix-url-map.json against a local base URL and
reports anything that isn't a 200, or a single 301 landing on a 200."""
import json
import sys
import urllib.request
import urllib.error

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3210"
MAP_PATH = sys.argv[2] if len(sys.argv) > 2 else "vtronix-url-map.json"

with open(MAP_PATH) as f:
    data = json.load(f)

urls = []
urls.extend(p["keep_as"] for p in data["pages"])
urls.extend(c["keep_as"] for c in data["categories"])
urls.extend(p["url"] for p in data["products"])

# Extra paths worth checking: old slugs / old query links / legacy paths.
extra_checks = [
    "/contact", "/products", "/index",
    "/products.html?cat=control-boards",
    "/products.html?cat=thermostats-residential",
    "/category/thermostats-residential",
    "/category/discontinued-items",
    "/product-page/w100",
    "/product-page/tb7980b1005",
    "/product-page/lakepro-1",
    "/products/w100-1",
]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def check(path, max_hops=5):
    opener = urllib.request.build_opener(NoRedirect)
    hops = [path]
    current = BASE + path
    for _ in range(max_hops):
        req = urllib.request.Request(current, method="GET", headers={"User-Agent": "url-check"})
        try:
            resp = opener.open(req, timeout=10)
            return resp.status, hops
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                loc = e.headers.get("Location", "")
                current = BASE + loc if loc.startswith("/") else loc
                hops.append(loc)
                continue
            return e.code, hops
        except Exception as e:
            return "ERR:" + str(e), hops
    return "ERR:too many redirects", hops

bad = []
multi_hop = []
for path in urls + extra_checks:
    status, hops = check(path)
    if status != 200:
        bad.append((path, status, hops))
    elif len(hops) > 2:
        multi_hop.append((path, hops))

print("checked", len(urls) + len(extra_checks), "urls")
print("non-200 (after following one hop):", len(bad))
for path, status, hops in bad:
    print("  BAD", status, path, "->", hops)
print("multi-hop (more than one redirect):", len(multi_hop))
for path, hops in multi_hop:
    print("  MULTI", path, "->", hops)

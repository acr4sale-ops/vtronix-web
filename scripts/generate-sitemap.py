#!/usr/bin/env python3
"""Generates sitemap.xml at the repo root: the main pages, every category and
every product, at their live www.vtronix.com URLs.
Run from anywhere: python3 scripts/generate-sitemap.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from _seo import CATEGORIES, HOST, PAGES  # noqa: E402

GEN_PATH = os.path.join(ROOT, "scripts", "generate-product-pages.py")
ns = {"__name__": "not_main", "__file__": GEN_PATH}
with open(GEN_PATH) as f:
    exec(compile(f.read(), GEN_PATH, "exec"), ns)

urls = [path for path, _, _ in PAGES.values()]
urls.extend("/category/" + slug for slug in CATEGORIES)
urls.extend("/product-page/" + p["slug"] for p in ns["PRODUCTS"])

entries = "\n".join("  <url><loc>{}{}</loc></url>".format(HOST, path) for path in urls)
xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    "{}\n"
    "</urlset>\n"
).format(entries)

out_path = os.path.join(ROOT, "sitemap.xml")
with open(out_path, "w") as f:
    f.write(xml)
print("wrote", out_path, "with", len(urls), "urls")

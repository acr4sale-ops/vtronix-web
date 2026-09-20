#!/usr/bin/env python3
"""Generates sitemap.xml at the repo root from the site's static pages,
categories and the product list in generate-product-pages.py.
Run from anywhere: python3 scripts/generate-sitemap.py
Also invoked automatically by the Vercel build command (see vercel.json).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN_PATH = os.path.join(ROOT, "scripts", "generate-product-pages.py")
HOST = "https://www.vtronix.com"

ns = {"__name__": "not_main", "__file__": GEN_PATH}
with open(GEN_PATH) as f:
    exec(compile(f.read(), GEN_PATH, "exec"), ns)
PRODUCTS = ns["PRODUCTS"]
CATEGORIES = ns["CATEGORIES"]

# Pages with real content, even where a section still carries a [CONFIRM]
# note. Certifications and the 4 legal pages are excluded on purpose: they
# are pure placeholder shells today (noindex is set on those pages too) and
# don't belong in the sitemap until real text replaces every [CONFIRM].
STATIC_PAGES = [
    "/", "/factory", "/about", "/links", "/contact-us",
    "/custom-controls", "/capabilities", "/brands", "/applications",
    "/documentation", "/request-a-quote",
]

APPLICATION_SLUGS = [
    "air-handlers", "fan-coil-units", "water-source-heat-pumps",
    "mini-splits", "ecm-motor-control", "energy-savings",
]

urls = []
urls.extend(STATIC_PAGES)
urls.extend("/applications/" + slug for slug in APPLICATION_SLUGS)
urls.extend("/category/" + slug for slug, _ in CATEGORIES)
urls.extend("/product-page/" + p["slug"] for p in PRODUCTS)

entries = "\n".join(
    "  <url><loc>{}{}</loc></url>".format(HOST, path) for path in urls
)
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

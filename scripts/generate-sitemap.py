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

# Phase 1: only pages with real, launch-ready content. New V2 pages (Custom
# Controls, Applications, Capabilities, Brands, Certifications, Documentation,
# Request a Quote, and the legal shells) get added here as each later phase
# gives them real copy — see the addendum's phase plan. Listing a thin stub
# in the sitemap before it has content would be worse for SEO than leaving
# it out.
STATIC_PAGES = [
    "/", "/factory", "/about", "/links", "/contact-us",
]

urls = []
urls.extend(STATIC_PAGES)
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

#!/usr/bin/env python3
"""Generates category/<slug>.html (served at /category/<slug>, matching the
live www.vtronix.com URLs) from products.html, giving each category its own
title, meta description and canonical. products.js reads data-cat to pick
the category. Run from anywhere: python3 scripts/generate-category-pages.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from _seo import CATEGORIES, head_tags, set_head  # noqa: E402

OUT_DIR = os.path.join(ROOT, "category")

# Shown only on the mini-split controls category. Other categories stay a
# plain product list.
MINI_SPLIT_INTRO = (
    '      <p class="category-intro">Vtronix mini split controls include wall-mounted wired controllers and wireless remotes for ductless systems. '
    'Review the models below for specifications and request a quote. Our sister brand also offers '
    '<a href="https://www.classic-america.com/" target="_blank" rel="noopener">Classic America ductless mini-split heat pumps</a>, '
    'along with WiFi window air conditioners and mini-split remotes.</p>\n'
)


def main():
    with open(os.path.join(ROOT, "products.html")) as f:
        template = f.read()
    marker = '<body class="section-white" style="background:#fff;">'
    assert marker in template
    search_row = '      <div class="shop-search">'
    assert search_row in template

    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, (title, desc) in CATEGORIES.items():
        page = set_head(template, head_tags("/category/" + slug, title, desc))
        page = page.replace(
            marker,
            '<body data-cat="{}" class="section-white shop-page" style="background:#fff;">'.format(slug),
            1,
        )
        if slug == "mini-split-controls":
            page = page.replace(search_row, MINI_SPLIT_INTRO + search_row, 1)
        out_path = os.path.join(OUT_DIR, slug + ".html")
        with open(out_path, "w") as f:
            f.write(page)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generates category/<slug>.html (served at /category/<slug>, matching the
live www.vtronix.com URLs) from products.html.

Each page includes, in the HTML itself:
- one H1, the category name
- an <a href> to every product in that category

products.js still filters and sorts in the browser, and reads data-cat to
pick the category. Run from anywhere:
python3 scripts/generate-category-pages.py
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from _seo import CATEGORIES, head_tags, set_head  # noqa: E402

OUT_DIR = os.path.join(ROOT, "category")

# Same fallback mark products.js draws when a product has no photo.
ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="#5b6b78" stroke-width="1.4">'
    '<rect x="4" y="4" width="16" height="16" rx="2"/>'
    '<circle cx="12" cy="12" r="3.2"/>'
    '<path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/>'
    "</svg>"
)


def _read(name):
    with open(os.path.join(ROOT, "assets", "js", name)) as f:
        return f.read()


def load_catalog():
    data = _read("products-data.js")
    details_js = _read("products-detail-data.js")

    products = []
    for sku, brand, discontinued in re.findall(
        r'\{\s*sku:\s*"([^"]+)",\s*brand:\s*"([^"]+)"(,\s*discontinued:\s*true)?\s*\}',
        data,
    ):
        products.append({"sku": sku, "brand": brand, "discontinued": bool(discontinued)})

    labels = dict(re.findall(r'\{\s*slug:\s*"([^"]+)",\s*label:\s*"([^"]+)"\s*\}', data))

    order_body = re.search(r"var VTRONIX_CATEGORY_ORDER = \{([\s\S]*?)\n\};", data)
    if not order_body:
        raise SystemExit("could not parse VTRONIX_CATEGORY_ORDER")
    order = {}
    for slug, inner in re.findall(r'"([a-z0-9-]+)"\s*:\s*\[([^\]]*)\]', order_body.group(1)):
        order[slug] = re.findall(r'"([^"]+)"', inner)
    order["all-products"] = [p["sku"] for p in products]

    details = {}
    for sku, slug, image in re.findall(
        r'"([^"]+)"\s*:\s*\{\s*slug:\s*"([^"]+)",\s*image:\s*"([^"]+)"\s*\}',
        details_js,
    ):
        details[sku] = {"slug": slug, "image": image}

    return products, labels, order, details


def product_card(product, detail):
    sku = html.escape(product["sku"])
    brand = html.escape(product["brand"])
    disc = " discontinued" if product["discontinued"] else ""
    disc_label = " (Discontinued)" if product["discontinued"] else ""
    if detail and detail.get("image"):
        media = '<img src="{}" alt="{} product photo" loading="lazy" decoding="async" />'.format(
            html.escape(detail["image"], quote=True), sku
        )
    else:
        media = ICON
    if not detail or not detail.get("slug"):
        raise SystemExit("no product URL for " + product["sku"])
    href = "/product-page/" + detail["slug"]
    return (
        '<a class="product-card" href="{}">\n'
        '          <div class="product-thumb">\n'
        '            <span class="product-tag{}">{}</span>\n'
        "            {}\n"
        "          </div>\n"
        '          <div class="product-info">\n'
        '            <div class="sku">{}{}</div>\n'
        '            <div class="rule"></div>\n'
        "          </div>\n"
        "        </a>"
    ).format(html.escape(href, quote=True), disc, brand, media, sku, disc_label)


def main():
    with open(os.path.join(ROOT, "products.html")) as f:
        template = f.read()
    marker = '<body class="section-white" style="background:#fff;">'
    grid = '<div class="product-grid" id="productGrid"></div>'
    search = '<div class="shop-search">'
    assert marker in template and grid in template and search in template

    products, labels, order, details = load_catalog()
    by_sku = {p["sku"]: p for p in products}
    if set(labels) != set(CATEGORIES):
        raise SystemExit("category slugs in products-data.js and _seo.py differ")

    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, (title, desc) in CATEGORIES.items():
        label = labels[slug]
        cards = []
        for sku in order[slug]:
            if sku not in by_sku:
                raise SystemExit("{} lists unknown SKU {}".format(slug, sku))
            cards.append(product_card(by_sku[sku], details.get(sku)))

        page = set_head(template, head_tags("/category/" + slug, title, desc))
        page = page.replace(
            marker,
            '<body data-cat="{}" class="section-white shop-page" style="background:#fff;">'.format(slug),
            1,
        )
        page = page.replace(
            '<a href="/category/{0}" data-cat="{0}">'.format(slug),
            '<a href="/category/{0}" data-cat="{0}" class="active">'.format(slug),
            1,
        )
        page = page.replace(
            search,
            '<h1 id="categoryHeading" class="h3">{}</h1>\n      {}'.format(html.escape(label), search),
            1,
        )
        page = page.replace(
            grid,
            '<div class="product-grid" id="productGrid">\n        {}\n      </div>'.format(
                "\n        ".join(cards)
            ),
            1,
        )
        if page.count("<h1") != 1:
            raise SystemExit("{} would have {} h1 tags".format(slug, page.count("<h1")))
        out_path = os.path.join(OUT_DIR, slug + ".html")
        with open(out_path, "w") as f:
            f.write(page)
        print("wrote", out_path, "with", len(cards), "product links")


if __name__ == "__main__":
    main()

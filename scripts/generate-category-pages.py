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
from _seo import CATEGORIES, head_tags, organization_script, set_head  # noqa: E402

OUT_DIR = os.path.join(ROOT, "category")

# Factual intros built only from the models listed on each page and the
# wording on those models' product pages. No prices, ratings, or extra specs.
CATEGORY_INTROS = {
    "commercial-thermostats": [
        "This page lists eight Honeywell products under Thermostats - Commercial. Three of them are ZonePRO thermostats. TB7980A1006 is described on its product page as a ZonePRO modulating thermostat with 0-10 Vdc control. TB6980A1007 is described as a ZonePRO floating control thermostat with a single output. TB7980B1005 does not use a one-line summary. Its page lists floating control outputs for the T6980, proportional control outputs for the T7980, a digital display in F or C with an output bar graph, PI control algorithms, single or dual-output models, vertical mounting, a two-hour night setback override, remote sensor capability, room or discharge air control, minimum and maximum set point limits, a minimum damper open percentage, 12-second backlighting, and a two-year warranty.",
        "Two SuitePRO fan coil thermostats are on the same list. TB8575A1000 is a 24 Vac model for 2-pipe or 4-pipe systems, with a 3-speed fan and manual or automatic heat or cool changeover. TB6575A1000 is a 120/240 V, 3-speed fan coil thermostat for 2-pipe or 4-pipe systems, with manual or automatic heat/cool changeover. The adapter plate 50033847-001 is listed with them. Its page describes a Honeywell adapter plate used with the TB6575 and TB8575 series fan coil thermostats to mount them to a vertical single-gang or double-gang junction box.",
        "TC300B-G is identified on its page as the TC300 commercial thermostat. TC500A-N is identified as a commercial connected touchscreen wireless thermostat, with staging given as 5H/3C for heat pump and 3H/3C for conventional systems. Each card on this page links to that model's product page. Those pages show the model number, the Honeywell label, a product photo, and the description or feature list noted above. Where a file is attached, the page also links install instructions, a brochure, a product overview, or a submittal sheet. None of these commercial thermostat pages displays a price. To ask about a model, use Request a Quote on its product page.",
    ],
    "residential-thermostats": [
        "This page lists fifteen residential thermostat products and accessories. LAKEPRO-1 is the Vtronix model. Its product page describes a Wi-Fi enabled programmable thermostat that requires a C wire, and it links an English manual and a Spanish manual. The other thermostats on the list are Honeywell models, together with one wiring module and three cover plates.",
        "TH1110DH1003 is the horizontal PRO 1000 non-programmable thermostat, and TH1110DV1009 is the vertical PRO 1000. Both pages describe a backlit, 1H/1C, dual-powered thermostat. TH4110U2005 is the T4 Pro programmable thermostat for 1H/1C heat pump or 1H/1C conventional systems. TH6210U2001 is the T6 Pro programmable thermostat for 2H/1C heat pump or 1H/1C conventional systems. TH5110D1022 is listed as a Honeywell digital thermostat. TH6220D1028 is listed as a Honeywell FocusPRO programmable thermostat.",
        "TH8110R1008 is a VisionPRO 8000 with RedLINK technology, programmable, 1H/1C, and a touchscreen. TH8320R1003 is a VisionPRO 8000 with RedLINK technology, with stages up to 3 heat / 2 cool. TH8321WF1001 is a Wi-Fi VisionPRO 8000, programmable, 3H/2C, and a touchscreen, and its page states that it needs a C wire. TH9320WF5003 is a Wi-Fi 9000 color touch screen programmable thermostat, and its page also states that it needs a C wire.",
        "THP9045A1023 is shown as THP9045A1023/U, a Honeywell Wiresaver wiring module for Wi-Fi and Prestige thermostats. 32003796-001 is a wallplate cover for all TH8000 series thermostats, for use with TH8000 VisionPRO series thermostats. The page lists it as an accessory in Premier White, 7 7/8 inches wide by 5 1/2 inches tall. THP2400A1027W is a Honeywell cover plate for TH9320WF5003. THP2400A1068 is a Honeywell 6 inch by 6 inch white coverplate for T series thermostats. Each card links to its product page. Those pages show the model, the brand label, a photo, and the wording above. They do not show a price. Use Request a Quote on a product page to ask Vtronix about a model.",
    ],
    "mini-split-controls": [
        "This page lists sixteen mini split controls. The cards label seven as Mini-Split Control Wireless and nine as Mini-Split Control Wired. The wireless models are KT-E03, KT-E08, KT-828 Gold, KT-S828 Silver, Q-338-F, Q-380EW, and XE8400A. KT-E03 is a mini split universal remote with 4000 codes, a large display, and One KEY. KT-E08 is a mini split universal remote with 6000 codes and an LCD display. KT-828 Gold and KT-S828 Silver are both described as mini split universal remotes with 2000 codes, a large display, and Deg C or F. Q-338-F is a mini split universal remote control in Deg F. Q-380EW is a mini split universal remote control in Deg C or F. XE8400A is listed as LCD5004-030, a wireless LCD control for mini-splits, described as remote LCD 5.2, cool only, with sweep, and a small board.",
        "The wired models are DT03PLUS-001, DT04-HC-220, DT04-HC-120, DT04PLUS-001, DT05PLUS, DT05HW, LCDWIREII, WLTH-010, and WLTH-020. DT03PLUS-001 is also identified as XE8200A1007, a wired control for mini-splits with an LED display, cool only, with sweep, and a remote marked optional. DT04PLUS-001 is a wired control for mini-splits with an LED display, cool only, with sweep, and a remote marked optional. DT04-HC-120 and DT04-HC-220 are listed as wired mini-split controls. Each of those two product pages shows the model number as its description and does not add further specifications. DT05PLUS is a fan coil control with an LED display, cool only, with sweep, and a remote marked optional. DT05HW is a temperature and dehumidification control. LCDWIREII is a fan coil control with a backlit LCD display and a remote marked optional.",
        "WLTH-010 and WLTH-020 are flush-mount fan coil controls with an LED, cool only, and a window sensor. WLTH-010 is 120 VAC and WLTH-020 is 220 VAC. Every card links to its product page, where the model, the wired or wireless label, the photo, and any download link are shown. Prices are not shown on these pages. Use Request a Quote on a product page to contact Vtronix.",
    ],
}


def _intro_html(slug):
    paragraphs = CATEGORY_INTROS.get(slug)
    if not paragraphs:
        return ""
    words = sum(len(p.split()) for p in paragraphs)
    if not 250 <= words <= 400:
        raise SystemExit("{} intro is {} words; expected 250-400".format(slug, words))
    body = "\n        ".join("<p>{}</p>".format(html.escape(p)) for p in paragraphs)
    return (
        '<div class="category-intro" data-intro="{}">\n        {}\n      </div>\n      '.format(
            html.escape(slug, quote=True), body
        )
    )

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
            '<h1 id="categoryHeading" class="h3">{}</h1>\n      {}{}'.format(
                html.escape(label), _intro_html(slug), search
            ),
            1,
        )
        if "application/ld+json" not in page:
            page = page.replace("</head>", organization_script() + "\n</head>", 1)
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

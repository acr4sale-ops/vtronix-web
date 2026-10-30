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
    "fan-coil-thermostats": [
        "This page lists fan coil thermostats, floating and modulating controls, and fan coil valves and actuators. The ZonePRO cards are TB7980B1005, TB7980A1006, and TB6980A1007. TB7980A1006 is described as a ZonePRO modulating thermostat with 0-10 Vdc control. TB6980A1007 is a ZonePRO floating control thermostat with a single output. The TB7980B1005 page lists floating outputs for the T6980, proportional outputs for the T7980, a digital display in F or C with an output bar graph, PI control algorithms, vertical mounting, a two-hour night setback override, remote sensor capability, set point limits, a minimum damper open percentage, 12-second backlighting, and a two-year warranty.",
        "SuitePRO cards are TB8575A1000, TB6575A1000, and TB6575B1000. TB8575A1000 is 24 Vac, for 2-pipe or 4-pipe systems, with a 3-speed fan and manual or automatic heat or cool changeover. TB6575A1000 and TB6575B1000 are 120/240 V, 3-speed fan coil thermostats for 2-pipe or 4-pipe systems with manual or automatic heat/cool changeover. T6811DP08 is an LCD thermostat, 120 Vac, for 2-pipe fan coil control. T6373B1148 is listed with a Honeywell label. That product page does not add a specification sentence beyond the model number.",
        "TF85L-200 is a T200 digital fan-coil thermostat, heat/cool, manual changeover, horizontal, no time delay, degrees F, 24 Vac. TF85L-201 is a T201 with auto changeover and the same horizontal, no-delay, degrees F, 24 Vac description. T5575B-STD is a backlit LCD heat/cool model with a heat valve, no time delay, degrees C or F, and 120-240 Vac. TE63M-001 and TE63M-002 are vertical, cool only, 3-speed, with a status light, at 120 Vac and 220 Vac. TF63M-001 and TF63M-002 are the horizontal pair at 120 Vac and 220 Vac. PI02 and PI03-AUX are digital low-voltage floating thermostats, vertical, with internal and remote sensors. PI04 is the modulating version, 0-10 V or 2-10 V, with the same vertical sensor description.",
        "Valve cards use the wording on their pages. V8043E1145 is a 3/4 inch NPT normally closed zone valve, 3.5 Cv, 24 V. VC4013ZZ00 is a two-position actuator, 6 VA, 200-240 Vac. VC8011ZZ00 is 24 Vac, 6 VA, 60 psi. VCZAL1100 is 3/4 inch female NPT, 4.7 Cv, and VCZAR1100 is 1 inch female NPT, 6.6 Cv. VU444A1007 is a two-position actuator for VU52 normally open and VU54 bodies, 120 V 60 Hz. VU52S2028 is a two-way valve, 1/2 inch sweat, 3.5 Cv. No price is shown. Use Request a Quote to ask about a model.",
    ],
    "energy-savings": [
        "This page lists five energy savings products: HESK120V, HESK220V, i-Save, i-save1001, and i-save1002. HESK120V and HESK220V are energy savings kits. Each product page says the kit includes the main board and two door switches, part 520025-000. HESK120V is specified at 120 Vac, 50/60 Hz. HESK220V is specified at 220 Vac, 50/60 Hz. The specification linked from those pages covers both model numbers and states that supply voltage is 120 or 220 Vac by model.",
        "That specification says the kit can send a dry contact to a digital thermostat to raise the cooling setpoint when the room is not occupied, or it can turn off the line-voltage input to the air conditioner. It names a passive infrared detector and a door sensor. Ratings written on the HESK pages from that sheet include 4 VA maximum consumption, two sets of magnetic door contacts with 18 inch leads, a mini-split relay rated 10 A at 240 Vac resistive, a fan-coil relay rated 3 A at 240 Vac resistive, and a board size of 3 3/4 by 3 3/4 by 1 3/4 inches. After the door closes, the sheet's operation section says movement detected within 15 minutes keeps the system in normal mode.",
        "i-Save is described on its page as the i-Save 2 hotel room energy savings control system. i-save1001 is a hotel room energy savings key card system at 120 Vac. i-save1002 is the key card system at 220 Vac. Those three hotel cards are separate from the two HESK kits. Every card on this page links to a product page with the model, the Energy Savings label, a photo, and the description for that model. Where a file is attached, the page includes a download. No price is shown on these pages. Use Request a Quote on a product page to contact Vtronix.",
    ],
    "control-boards": [
        "This page lists the control boards and related kits. R200A/S3 is described as an R200A control board for a hot water or electric heat air handler. R201 is an AHU control board, two speed. R85A-001 is described as a UL approved 3-speed fan board, with 24 V input, 120-277 V, and 11 A fan control. R100A is an air-conditioning control board with high-pressure and low-pressure switch inputs. RAB-A24.11BE3 is a magnetic starter, 220 V. W100 is listed as a chiller controller.",
        "CB600V is a thermostat interface board for an ECM motor. EW40030 and EW40040 are wire kits for an ECM motor, with a 30 inch line-volt cable and a 40 inch line-volt cable. R650 is identified on its page as an ECM motor flyer. CBX02003 is a fan blower post-purge time delay of 65 seconds. CBX99100 is a fan delay board. R60A is a fan delay board with a 30 second on delay, a 30 second off delay, and a 2.5 by 3 inch size. R60B-45/S2 is a fan delay board with a 1 second on delay, a 45 second off delay, and a 2.5 by 2.5 inch size.",
        "R60B-45/S2-R60BLEADS is that R60B board plus a wire harness, with the same 1 second and 45 second delays and the same 2.5 by 2.5 inch size. R60BLEADS is the wire harness by itself. R502 is a heater timing board. R401 is listed as water source heat pump boards. The cards keep those model numbers and the labels shown on this page, and each card links to the matching product page. Several of those pages also link a specification or manual. No price is printed on the product pages. Use Request a Quote on a product page to ask Vtronix about a board.",
    ],
    "temperature-controls": [
        "This page lists nine temperature controls. W100 is described as a chiller controller. T775A2009 is an electronic temperature controller with 1 temperature input, 1 SPDT relay, and 1 sensor included. AHU Control is described as phase monitoring and a star-delta motor starter. FT101 is a freezer thermostat with fan, defrost, and compressor control. MSI is a master-slave network control of up to 64 air-conditioning units.",
        "Outdoor Control is described as an outdoor control for a compressor. TC102 is a storage tank controller with an input for heat/cool and 2 stage outputs. W110 is lead-lag control of 2 air-conditioning units with a high temperature sensor. Zone Control II controls up to 4 dampers. Those sentences are the descriptions on the product pages linked from this grid.",
        "Each card shows a label and the model, and the link goes to that product page, where the photo and any documentation link are shown. T775A2009 carries the Honeywell label. W100 carries the Air Conditioning Control label. AHU Control, FT101, MSI, Outdoor Control, TC102, W110, and Zone Control II use the Temperature Controls label. The sidebar on this page marks Temperature Controls. No price is shown. To ask about one of the nine models, use Request a Quote on its product page. The same nine models are also cards on the all-products page, which lists the wider catalog beside the other categories in the sidebar. Where a product page has a file, it is the download or manual linked next to the description as well.",
    ],
    "discontinued": [
        "This page lists eight discontinued items. The cards are ECONO3-001, TE80SB-501, TE86SB-501, TF65L-001, TF65L-002-STD, TF65L-002-SWP, TF85L-10011, and TF85L-11011. ECONO3-001 is also identified as XE8100A, a wired control for mini-splits, cool only, with sweep. TE80SB-501 is programmable, 7 day, vertical, heat/cool, power stealing, 24 Vac. TE86SB-501 is a TE86 non-programmable thermostat, vertical, heat/cool, power stealing, 24 Vac.",
        "TF65L-001 is a digital fan-coil thermostat, cool only, horizontal, no time delay, degrees C, 120 Vac. TF65L-002-STD is cool only, horizontal, with a 3 minute delay, degrees C, 220 Vac. TF65L-002-SWP is cool only with sweep, horizontal, with a 3 minute delay, degrees C, 200 Vac. TF85L-10011 is a T200 digital fan-coil thermostat, heat/cool, auto changeover, horizontal, no time delay, degrees F, 24 Vac. TF85L-11011 is a T201 with that same auto-changeover, horizontal, no-delay, degrees F, 24 Vac description.",
        "The product titles include the word discontinued, and this category is the discontinued set. ECONO3-001 uses the Mini-Split Control Wired label. TE80SB-501 and TE86SB-501 use the Vtronix label. The TF65L and TF85L models use the Digital - 3 Speed Fan, On/Off label. Each card still links to its product page, which keeps the description above, the photo, and a documentation link where one was published. No price is shown. Use Request a Quote on a product page to ask Vtronix about a listed model. Current fan-coil thermostats, including the TF85L-200 and TF85L-201 cards, and current mini-split controls stay on their own category pages rather than in this discontinued list. The heading on this page is Discontinued Items, and the sidebar marks that category.",
    ],
    "all-products": [
        "This page is the full product grid. The sidebar groups the same catalog into control boards, residential thermostats, commercial thermostats, fan coil controls, mini split controls, energy savings, temperature controls, and discontinued items. The cards here keep the model number, the label, and the link to each product page. Residential examples on those pages include the PRO 1000 pair TH1110DH1003 and TH1110DV1009, the T4 Pro TH4110U2005, the T6 Pro TH6210U2001, and the Vtronix LAKEPRO-1 Wi-Fi programmable thermostat that requires a C wire.",
        "Commercial cards include the ZonePRO models TB7980B1005, TB7980A1006, and TB6980A1007, the SuitePRO fan coil thermostats TB8575A1000 and TB6575A1000, and TC500A-N, described as a commercial connected touchscreen wireless thermostat for 5H/3C heat pump or 3H/3C conventional systems. Fan coil cards also include digital and electronic 3-speed thermostats such as TF85L-200, T5575B-STD, and the TE63M and TF63M pairs, plus valves and actuators such as VCZAR1100 and V8043E1145.",
        "Control-board cards include R200A/S3 for a hot water or electric heat air handler, R201 two-speed AHU control, R100A with high-pressure and low-pressure inputs, the R60 fan delay boards, and R401 water source heat pump boards. Mini split cards include wired controls such as DT03PLUS-001 and wireless remotes such as KT-E03. Energy savings cards are the HESK120V and HESK220V kits and the i-Save hotel room controls. Temperature-control cards include T775A2009, FT101, W110 lead-lag control, and Zone Control II. Discontinued cards remain listed for reference. No product page in this catalog shows a price. Use Request a Quote on a product page to contact Vtronix.",
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

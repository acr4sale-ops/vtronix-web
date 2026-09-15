#!/usr/bin/env python3
"""
Generates static product detail pages under products/<slug>.html from PRODUCTS below.
Run from anywhere: python3 scripts/generate-product-pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "products")

PRODUCTS = [
    {
        "sku": "TB7980B1005",
        "slug": "tb7980b1005",
        "brand": "Honeywell",
        "image": "TB7980B1005.jpg",
        "features": [
            "Floating control output(s) (T6980)",
            "Proportional control output(s) (T7980)",
            "Digital display (F or C and output bar graph)",
            "PI control algorithms",
            "Single or dual-output models",
            "Vertical mounting",
            "Night setback override (2-hour)",
            "Remote sensor capable",
            "Room or discharge air control",
            "Minimum and maximum set point limits",
            "Minimum damper open %",
            "12-second backlighting",
            "Two-year warranty",
        ],
        "description": None,
        "docs": [
            {"label": "Install Instructions", "href": "https://s3.amazonaws.com/s3.supplyhouse.com/product_files/TB7980B1005-Install.pdf"},
            {"label": "Product Overview", "href": "https://s3.amazonaws.com/s3.supplyhouse.com/product_files/TB7980B1005-Product-Overview.pdf"},
        ],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TH6210U2001",
        "slug": "th6210u2001",
        "brand": "Honeywell",
        "image": "TH6210U2001.jpg",
        "features": [],
        "description": "T6 Pro Programmable Thermostat, 2H/1C Heat Pump, 1H/1C Conventional, TH6210U2001",
        "docs": [
            {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_46f28dee08b44caf845642687a5e4907.pdf"},
        ],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "W100",
        "slug": "w100",
        "brand": "Air Conditioning Control",
        "image": "W100.jpg",
        "features": [],
        "description": "W100 Chiller Controller.",
        "docs": [
            {"label": "Manual", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/6a435f_5e8d6f28e33441d3bb98138c82e58ed6.pdf"},
        ],
        "cat_query": "control-boards",
    },
    {
        "sku": "W110",
        "slug": "w110",
        "brand": "Temperature Controls",
        "image": "W110.jpg",
        "features": [],
        "description": "W110 Lead Lag Control of 2 A/C units with high temp sensor.",
        "docs": [
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_12678dadbd4c4aaab96511ac8bae5fbc.pdf"},
        ],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "i-Save",
        "slug": "i-save",
        "brand": "Energy Savings",
        "image": "i-Save.jpg",
        "features": [],
        "description": "i-Save 2 Hotel Room Energy Savings Control System.",
        "docs": [
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_ba7485888fd04e2babdea2e907075664.pdf"},
        ],
        "cat_query": "energy-savings",
    },
    {
        "sku": "DT03PLUS-001",
        "slug": "dt03plus-001",
        "brand": "Mini-Split Control Wired",
        "image": "DT03PLUS-001.jpg",
        "features": [],
        "description": "XE8200A1007. Wired Control for mini-splits, LED Display, Cool Only, with sweep. Remote optional.",
        "docs": [
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_9378fa9dc0004dee904f05fdcae67611.pdf"},
        ],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "VCZAR1100",
        "slug": "vczar1100",
        "brand": "Honeywell",
        "image": "VCZAR1100.jpg",
        "features": [],
        "description": '1" Female NPT VC Valve Assembly (6.6 Cv)',
        "docs": [
            {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_dd10112d23ee49a2a286350a704b21d6.pdf"},
            {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_2d56eb49591547b6a0dd52b3a4939243.pdf"},
        ],
        "cat_query": "fan-coil-controls",
    },
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{sku} | Vtronix</title>
<link rel="icon" type="image/svg+xml" href="../assets/img/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/css/style.css" />
</head>
<body class="section-white" style="background:#fff;">

<header class="site-header">
  <div class="wrap">
    <a href="../index.html" class="logo"><img src="../assets/img/logo.png" alt="Vtronix" /></a>
    <nav class="main-nav">
      <a href="../index.html">Home</a>
      <a href="../factory.html">Factory</a>
      <a href="../about.html">About Us</a>
      <a href="../products.html" class="active">Products</a>
      <a href="../links.html">Links</a>
      <a href="../contact.html">Contact Us</a>
    </nav>
    <button class="nav-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</header>

<main class="section-white">
  <div class="wrap shop-layout" style="padding-top:34px;">

    <aside class="shop-categories">
      <h4>Categories</h4>
      <ul>
{sidebar}
      </ul>
    </aside>

    <div>
      <p class="breadcrumb">
        <a href="../index.html">Home</a><span class="sep">/</span><a href="../products.html?cat={cat_query}">All Products</a><span class="sep">/</span><span class="current">{sku}</span>
      </p>

      <div class="product-detail">
        <div class="product-detail-media">
          <img src="../assets/img/products/{image}" alt="{sku} product photo" loading="lazy" />
        </div>

        <div>
          <span class="product-detail-tag">{brand}</span>
          <h1>{sku}</h1>

{body}

{docs}

          <a class="btn btn-light" href="../contact.html"><span>Request a Quote</span><span class="arrow">&rarr;</span></a>
        </div>
      </div>
    </div>

  </div>
</main>

<footer class="site-footer" style="background:#000; color:#fff;">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand">VTRONIX<span class="reg">&reg;</span></div>
      <p>PO Box 267096,<br />Weston FL 33326</p>
      <p><a href="mailto:sales@vtronix.com">sales@vtronix.com</a></p>
      <p><a href="tel:3054717600">305-471-7600</a></p>
    </div>
    <div>
      <h4>General</h4>
      <a href="../about.html">About</a>
      <a href="../factory.html">Factory</a>
      <a href="../links.html">Links</a>
      <a href="../contact.html">Contact Us</a>
    </div>
    <div>
      <h4>Products</h4>
      <a href="../products.html?cat=control-boards">Control Boards</a>
      <a href="../products.html?cat=thermostats-residential">Residential Thermostats</a>
      <a href="../products.html?cat=thermostats-commercial">Commercial Thermostats</a>
      <a href="../products.html?cat=fan-coil-controls">Fan Coil Thermostats</a>
    </div>
    <div>
      <h4>&nbsp;</h4>
      <a href="../products.html?cat=mini-split-controls">Mini Split Controls</a>
      <a href="../products.html?cat=energy-savings">Energy Savings</a>
      <a href="../products.html?cat=temperature-controls">Temperature Controls</a>
      <a href="../products.html">All Products</a>
    </div>
  </div>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
"""


def build_body(p):
    if p["features"]:
        items = "\n".join('          <li>{}</li>'.format(f) for f in p["features"])
        return '        <p class="section-label">Features</p>\n        <ul class="feature-list">\n{}\n        </ul>'.format(items)
    return '        <p class="lead" style="margin-bottom:28px; color:#444;">{}</p>'.format(p["description"] or "")


CATEGORIES = [
    ("control-boards", "Control Boards"),
    ("thermostats-residential", "Thermostats - Residential"),
    ("thermostats-commercial", "Thermostats - Commercial"),
    ("fan-coil-controls", "Fan Coil Controls"),
    ("mini-split-controls", "Mini Split Controls"),
    ("energy-savings", "Energy Savings"),
    ("temperature-controls", "Temperature Controls"),
    ("all-products", "All Products"),
    ("discontinued-items", "Discontinued Items"),
]


def build_sidebar(p):
    rows = []
    for slug, label in CATEGORIES:
        href = "../products.html" if slug == "all-products" else "../products.html?cat=" + slug
        cls = ' class="active"' if slug == p["cat_query"] else ""
        rows.append('        <li><a href="{href}"{cls}>{label}</a></li>'.format(href=href, cls=cls, label=label))
    return "\n".join(rows)


PDF_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
    '<path d="M14 2v6h6"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/>'
    "</svg>"
)


def build_docs(p):
    if not p["docs"]:
        return ""
    links = "\n".join(
        '          <a href="{href}" target="_blank" rel="noopener">{icon} {label}</a>'.format(icon=PDF_ICON, **d)
        for d in p["docs"]
    )
    return '        <p class="section-label">Documentation</p>\n        <div class="pdf-links">\n{}\n        </div>'.format(links)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for p in PRODUCTS:
        html = TEMPLATE.format(
            sku=p["sku"],
            brand=p["brand"],
            image=p["image"],
            cat_query=p["cat_query"],
            body=build_body(p),
            docs=build_docs(p),
            sidebar=build_sidebar(p),
        )
        out_path = os.path.join(OUT_DIR, p["slug"] + ".html")
        with open(out_path, "w") as f:
            f.write(html)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

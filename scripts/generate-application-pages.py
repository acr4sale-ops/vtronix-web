#!/usr/bin/env python3
"""Generates static application pages under applications/<slug>.html.
Run from anywhere: python3 scripts/generate-application-pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "applications")
GEN_PATH = os.path.join(ROOT, "scripts", "generate-product-pages.py")

ns = {"__name__": "not_main", "__file__": GEN_PATH}
with open(GEN_PATH) as f:
    exec(compile(f.read(), GEN_PATH, "exec"), ns)
PRODUCTS_BY_SLUG = {p["slug"]: p for p in ns["PRODUCTS"]}

APPLICATIONS = [
    {
        "slug": "air-handlers",
        "title": "Air handler controls",
        "need": "Air handlers need a control that can stage fan speeds, sequence heating and cooling, and coordinate with the rest of the system, in a board built for the panel it mounts in.",
        "products": ["r200a", "r201", "r85a", "ahu-control", "cbx99100", "r60a"],
    },
    {
        "slug": "fan-coil-units",
        "title": "Fan coil controls and thermostats",
        "need": "Fan coil units need a thermostat that can drive a 2, 3 or 4-pipe valve or ECM fan, at a range of setpoints and speed steps, in a form factor that fits the existing wall plate.",
        "products": ["tf85l-200", "t5575b-std", "te63m-001", "tf63m-001", "pi02", "pi03-aux", "pi04"],
    },
    {
        "slug": "water-source-heat-pumps",
        "title": "Water source heat pump boards",
        "need": "Water source heat pumps need a board that manages compressor staging, water valve timing and safety lockouts across a wide entering-water-temperature range.",
        "products": ["r401"],
    },
    {
        "slug": "mini-splits",
        "title": "Mini split wired and wireless controls",
        "need": "Mini splits need a wired or wireless control that talks to the indoor unit's own protocol, with the setpoint, mode and fan-speed options installers and homeowners expect.",
        "products": ["dt03plus-001", "dt04-hc-120", "dt05plus", "lcdwireii", "wlth-010", "kt-828-gold", "q-338-f"],
    },
    {
        "slug": "ecm-motor-control",
        "title": "ECM motor control",
        "need": "ECM motors need a control that can vary speed smoothly across the motor's full range, without the hunting or nuisance trips a mismatched driver can cause.",
        "products": ["cb600v", "ew40030", "ew40040", "r650"],
    },
    {
        "slug": "energy-savings",
        "title": "Energy-saving controls for hotels and buildings",
        "need": "Hotels and buildings need occupancy-based controls that cut conditioning when a room is empty, without a guest ever noticing a comfort tradeoff.",
        "products": ["hesk120v", "hesk220v", "i-save", "zone-control-ii"],
    },
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} | Vtronix</title>
<meta name="description" content="{need}" />
<link rel="canonical" href="https://www.vtronix.com/applications/{slug}" />
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/style.css" />
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Organization", "name": "Vtronix", "url": "https://www.vtronix.com", "foundingDate": "2001", "logo": "https://www.vtronix.com/assets/img/logo.png", "address": {{"@type": "PostalAddress", "postOfficeBoxNumber": "267096", "addressLocality": "Weston", "addressRegion": "FL", "postalCode": "33326", "addressCountry": "US"}}, "contactPoint": {{"@type": "ContactPoint", "telephone": "+1-305-471-7600", "email": "sales@vtronix.com", "contactType": "sales"}}}}</script>
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <a href="/" class="logo"><img src="/assets/img/logo.png" alt="Vtronix" /></a>
    <nav class="main-nav">
      <a href="/custom-controls">Custom Controls</a>
      <a href="/category/all-products">Products</a>
      <a href="/applications" class="active">Applications</a>
      <a href="/factory">Manufacturing</a>
      <a href="/about">About</a>
      <a href="/documentation">Documentation</a>
      <a class="nav-cta" href="/request-a-quote">Request a Quote</a>
    </nav>
    <button class="nav-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</header>

<main>

  <section class="section-tight">
    <div class="wrap accent-block">
      <p class="breadcrumb" style="color:var(--gray-text); margin-bottom:18px;"><a href="/applications" style="color:var(--gray-text);">Applications</a><span class="sep" style="margin:0 8px;">/</span><span style="color:var(--white);">{title}</span></p>
      <p class="eyebrow">Applications</p>
      <h1 class="h1">{title}</h1>
      <p class="lead">{need}</p>
    </div>
  </section>

  <section class="section-tight" style="border-top:1px solid var(--gray-line-soft);">
    <div class="wrap">
      <p class="eyebrow">Products that fit</p>
      <div class="featured-grid">
{cards}
      </div>
    </div>
  </section>

  <section class="section-tight" style="border-top:1px solid var(--gray-line-soft);">
    <div class="wrap">
      <p class="eyebrow">Documentation</p>
      <div class="pdf-links" style="margin-bottom:0;">
{docs}
      </div>
    </div>
  </section>

  <section class="section-tight" style="border-top:1px solid var(--gray-line-soft);">
    <div class="wrap accent-block">
      <p class="eyebrow">Need something different</p>
      <p class="lead">If none of these fit exactly, we design the control that does. <a href="/custom-controls" style="text-decoration:underline; text-decoration-color:rgba(255,255,255,.3);">See how a custom project runs &rarr;</a></p>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand">VTRONIX<span class="reg">&reg;</span></div>
      <p>PO Box 267096,<br />Weston FL 33326</p>
      <p style="margin-top:10px;">Miami Gardens, Florida<br />Operations and warehouse</p>
      <p><a href="mailto:sales@vtronix.com">sales@vtronix.com</a></p>
      <p><a href="tel:3054717600">305-471-7600</a></p>
    </div>
    <div>
      <h4>General</h4>
      <a href="/custom-controls">Custom Controls</a>
      <a href="/capabilities">Capabilities</a>
      <a href="/about">About</a>
      <a href="/factory">Factory</a>
      <a href="/brands">Our Brands</a>
      <a href="/certifications">Certifications</a>
      <a href="/links">Links</a>
      <a href="/contact-us">Contact Us</a>
    </div>
    <div>
      <h4>Products</h4>
      <a href="/category/control-boards">Control Boards</a>
      <a href="/category/residential-thermostats">Residential Thermostats</a>
      <a href="/category/commercial-thermostats">Commercial Thermostats</a>
      <a href="/category/fan-coil-thermostats">Fan Coil Thermostats</a>
    </div>
    <div>
      <h4>&nbsp;</h4>
      <a href="/category/mini-split-controls">Mini Split Controls</a>
      <a href="/category/energy-savings">Energy Savings</a>
      <a href="/category/temperature-controls">Temperature Controls</a>
      <a href="/category/all-products">All Products</a>
    </div>
    <div>
      <h4>Legal</h4>
      <a href="/warranty-returns">Warranty and Returns</a>
      <a href="/privacy">Privacy</a>
      <a href="/terms">Terms</a>
      <a href="/accessibility">Accessibility</a>
    </div>
  </div>
</footer>

<script src="/assets/js/main.js"></script>
</body>
</html>
"""

PDF_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
    '<path d="M14 2v6h6"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/>'
    "</svg>"
)


def build_cards(slugs):
    rows = []
    for slug in slugs:
        p = PRODUCTS_BY_SLUG[slug]
        rows.append(
            '        <a class="featured-card" href="/product-page/{slug}">'
            '<div class="featured-thumb"><img src="/assets/img/products/{image}" alt="{sku} {brand}" loading="lazy" /></div>'
            '<div class="featured-info"><span class="tag">{brand}</span><div class="name">{sku}</div></div></a>'.format(
                slug=slug, image=p["image"], sku=p["sku"], brand=p["brand"]
            )
        )
    return "\n".join(rows)


def build_docs(slugs):
    rows = []
    seen = set()
    for slug in slugs:
        p = PRODUCTS_BY_SLUG[slug]
        for d in p.get("docs") or []:
            if d["href"] in seen:
                continue
            seen.add(d["href"])
            rows.append(
                '        <a href="{href}" target="_blank" rel="noopener">{icon} {sku} {label}</a>'.format(
                    href=d["href"], icon=PDF_ICON, sku=p["sku"], label=d["label"]
                )
            )
    return "\n".join(rows) if rows else '        <p style="color:var(--gray-text); font-size:14px;">See each product page for its manual.</p>'


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for a in APPLICATIONS:
        html = TEMPLATE.format(
            title=a["title"],
            need=a["need"],
            slug=a["slug"],
            cards=build_cards(a["products"]),
            docs=build_docs(a["products"]),
        )
        out_path = os.path.join(OUT_DIR, a["slug"] + ".html")
        with open(out_path, "w") as f:
            f.write(html)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

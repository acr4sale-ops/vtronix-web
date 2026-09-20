#!/usr/bin/env python3
"""Generates the four legal page shells (headings only, no invented legal
text, per the brief). Run from anywhere: python3 scripts/generate-legal-pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    {
        "slug": "warranty-returns",
        "title": "Warranty and Returns",
        "sections": ["Warranty coverage", "How to request a return", "Return shipping", "Refunds and replacements"],
    },
    {
        "slug": "privacy",
        "title": "Privacy Policy",
        "sections": ["Information we collect", "How we use it", "Cookies and analytics", "Your choices", "Contact us about privacy"],
    },
    {
        "slug": "terms",
        "title": "Terms of Use",
        "sections": ["Acceptance of terms", "Use of this site", "Product information and orders", "Limitation of liability", "Governing law"],
    },
    {
        "slug": "accessibility",
        "title": "Accessibility",
        "sections": ["Our commitment", "Standards we aim to meet", "Known limitations", "Contact us about accessibility"],
    },
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} | Vtronix</title>
<meta name="description" content="Vtronix {title_lower}." />
<link rel="canonical" href="https://www.vtronix.com/{slug}" />
<meta name="robots" content="noindex" />
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
      <a href="/applications">Applications</a>
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
      <p class="eyebrow">Legal</p>
      <h1 class="h1">{title}</h1>
      <p class="lead confirm" style="display:inline-block; margin-top:6px;">[CONFIRM: owner or counsel to supply this page's text. Headings only below - Vtronix V2 does not write legal terms.]</p>
    </div>
  </section>

  <section class="section-tight" style="border-top:1px solid var(--gray-line-soft);">
    <div class="wrap">
{sections}
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

SECTION_BLOCK = """      <div style="padding:26px 0; border-bottom:1px solid var(--gray-line-soft);">
        <h2 class="h3" style="font-size:18px; font-weight:600; margin:0 0 10px;">{heading}</h2>
        <p class="lead confirm" style="display:inline-block; margin:0;">[CONFIRM: text]</p>
      </div>"""


def main():
    for page in PAGES:
        sections = "\n".join(SECTION_BLOCK.format(heading=h) for h in page["sections"])
        html = TEMPLATE.format(
            title=page["title"],
            title_lower=page["title"].lower(),
            slug=page["slug"],
            sections=sections,
        )
        out_path = os.path.join(ROOT, page["slug"] + ".html")
        with open(out_path, "w") as f:
            f.write(html)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

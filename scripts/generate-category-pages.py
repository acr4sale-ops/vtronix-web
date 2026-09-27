#!/usr/bin/env python3
"""Generates category/<slug>.html for every product category from products.html,
giving each /category/* URL its own title, description and canonical (matching the
live Wix titles) instead of every category sharing the "All Products" head.
products.js still reads the category from the URL path, so the body is unchanged.
Run from anywhere: python3 scripts/generate-category-pages.py
Also invoked automatically by the Vercel build command (see vercel.json).
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN_PATH = os.path.join(ROOT, "scripts", "generate-product-pages.py")
OUT_DIR = os.path.join(ROOT, "category")
HOST = "https://www.vtronix.com"

ns = {"__name__": "not_main", "__file__": GEN_PATH}
with open(GEN_PATH) as f:
    exec(compile(f.read(), GEN_PATH, "exec"), ns)
CATEGORIES = ns["CATEGORIES"]

DESCRIPTIONS = {
    "all-products": "Browse every Vtronix HVAC control: control boards, residential and commercial thermostats, fan coil and mini split controls, energy savings and temperature controls.",
    "control-boards": "Vtronix HVAC control boards, ECM motor controls and wire kits for air handlers, fan coils and heat pumps. Specifications and manuals.",
    "residential-thermostats": "Residential thermostats from Vtronix and Honeywell, including programmable, non-programmable and Wi-Fi models. Specifications and manuals.",
    "commercial-thermostats": "Commercial thermostats from Vtronix and Honeywell for light commercial HVAC systems. Specifications, documentation and ordering.",
    "fan-coil-thermostats": "Fan coil thermostats and controls from Vtronix for 2-pipe and 4-pipe fan coil units, plus valves and accessories.",
    "mini-split-controls": "Wired controls and interfaces for ductless mini split systems from Vtronix. Specifications, documentation and ordering.",
    "energy-savings": "Vtronix energy savings controls, including i-Save hotel room occupancy systems. Specifications, documentation and ordering.",
    "temperature-controls": "Vtronix temperature controls, sensors and controllers for HVAC equipment. Specifications, documentation and ordering.",
    "discontinued": "Discontinued and obsolete Vtronix HVAC controls, with manuals and recommended replacement parts.",
}

OLD_HEAD = "<title>All Products | Vtronix</title>\n"


def main():
    with open(os.path.join(ROOT, "products.html")) as f:
        base = f.read()
    if OLD_HEAD not in base:
        raise SystemExit("products.html <title> changed; update generate-category-pages.py")
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, label in CATEGORIES:
        url = "{}/category/{}".format(HOST, slug)
        title = "{} | Vtronix".format(label)
        desc = html.escape(DESCRIPTIONS[slug])
        head = (
            "<title>{t}</title>\n"
            '<meta name="description" content="{d}" />\n'
            '<link rel="canonical" href="{u}" />\n'
            '<meta property="og:type" content="website" />\n'
            '<meta property="og:site_name" content="Vtronix" />\n'
            '<meta property="og:title" content="{t}" />\n'
            '<meta property="og:description" content="{d}" />\n'
            '<meta property="og:url" content="{u}" />\n'
            '<meta property="og:image" content="{h}/assets/img/logo.png" />\n'
        ).format(t=html.escape(title), d=desc, u=url, h=HOST)
        out_path = os.path.join(OUT_DIR, slug + ".html")
        with open(out_path, "w") as f:
            f.write(base.replace(OLD_HEAD, head, 1))
        print("wrote", out_path)


if __name__ == "__main__":
    main()

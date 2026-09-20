#!/usr/bin/env python3
"""One-time site-wide footer update: adds the Miami Gardens line, links to
the new pages (Capabilities, Brands, Certifications, legal shells) to the
existing footer layout, per the brief's 'gains the new links plus the
Miami Gardens line' instruction. Run once from repo root."""
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADDRESS_OLD = "<p>PO Box 267096,<br />Weston FL 33326</p>"
ADDRESS_NEW = (
    "<p>PO Box 267096,<br />Weston FL 33326</p>\n"
    '      <p style="margin-top:10px;">Miami Gardens, Florida<br />Operations and warehouse</p>'
)

FOOTER_TAIL_OLD = (
    '<h4>General</h4>\n'
    '      <a href="/about">About</a>\n'
    '      <a href="/factory">Factory</a>\n'
    '      <a href="/links">Links</a>\n'
    '      <a href="/contact-us">Contact Us</a>\n'
    '    </div>\n'
    '    <div>\n'
    '      <h4>Products</h4>\n'
    '      <a href="/category/control-boards">Control Boards</a>\n'
    '      <a href="/category/residential-thermostats">Residential Thermostats</a>\n'
    '      <a href="/category/commercial-thermostats">Commercial Thermostats</a>\n'
    '      <a href="/category/fan-coil-thermostats">Fan Coil Thermostats</a>\n'
    '    </div>\n'
    '    <div>\n'
    '      <h4>&nbsp;</h4>\n'
    '      <a href="/category/mini-split-controls">Mini Split Controls</a>\n'
    '      <a href="/category/energy-savings">Energy Savings</a>\n'
    '      <a href="/category/temperature-controls">Temperature Controls</a>\n'
    '      <a href="/category/all-products">All Products</a>\n'
    '    </div>\n'
    '  </div>\n'
    '</footer>'
)

FOOTER_TAIL_NEW = (
    '<h4>General</h4>\n'
    '      <a href="/custom-controls">Custom Controls</a>\n'
    '      <a href="/capabilities">Capabilities</a>\n'
    '      <a href="/about">About</a>\n'
    '      <a href="/factory">Factory</a>\n'
    '      <a href="/brands">Our Brands</a>\n'
    '      <a href="/certifications">Certifications</a>\n'
    '      <a href="/links">Links</a>\n'
    '      <a href="/contact-us">Contact Us</a>\n'
    '    </div>\n'
    '    <div>\n'
    '      <h4>Products</h4>\n'
    '      <a href="/category/control-boards">Control Boards</a>\n'
    '      <a href="/category/residential-thermostats">Residential Thermostats</a>\n'
    '      <a href="/category/commercial-thermostats">Commercial Thermostats</a>\n'
    '      <a href="/category/fan-coil-thermostats">Fan Coil Thermostats</a>\n'
    '    </div>\n'
    '    <div>\n'
    '      <h4>&nbsp;</h4>\n'
    '      <a href="/category/mini-split-controls">Mini Split Controls</a>\n'
    '      <a href="/category/energy-savings">Energy Savings</a>\n'
    '      <a href="/category/temperature-controls">Temperature Controls</a>\n'
    '      <a href="/category/all-products">All Products</a>\n'
    '    </div>\n'
    '    <div>\n'
    '      <h4>Legal</h4>\n'
    '      <a href="/warranty-returns">Warranty and Returns</a>\n'
    '      <a href="/privacy">Privacy</a>\n'
    '      <a href="/terms">Terms</a>\n'
    '      <a href="/accessibility">Accessibility</a>\n'
    '    </div>\n'
    '  </div>\n'
    '</footer>'
)

files = glob.glob(os.path.join(ROOT, "*.html"))
files += glob.glob(os.path.join(ROOT, "products", "*.html"))
files += glob.glob(os.path.join(ROOT, "applications", "*.html"))

updated, skipped = 0, []
for path in files:
    with open(path) as f:
        src = f.read()
    if "<footer" not in src:
        continue
    orig = src
    src = src.replace(ADDRESS_OLD, ADDRESS_NEW)
    src = src.replace(FOOTER_TAIL_OLD, FOOTER_TAIL_NEW)
    if src != orig:
        with open(path, "w") as f:
            f.write(src)
        updated += 1
    else:
        skipped.append(os.path.relpath(path, ROOT))

print("updated:", updated)
print("skipped (no match, check manually):", len(skipped))
for s in skipped:
    print(" ", s)

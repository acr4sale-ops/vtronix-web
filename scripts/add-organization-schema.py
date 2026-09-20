#!/usr/bin/env python3
"""One-time sweep: inserts Organization JSON-LD before </head> on every page
that doesn't already have it. Per Part 4: 'Organization on every page
(founding date 2001)'. Run once from repo root."""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Vtronix",
    "url": "https://www.vtronix.com",
    "foundingDate": "2001",
    "logo": "https://www.vtronix.com/assets/img/logo.png",
    "address": {
        "@type": "PostalAddress",
        "postOfficeBoxNumber": "267096",
        "addressLocality": "Weston",
        "addressRegion": "FL",
        "postalCode": "33326",
        "addressCountry": "US",
    },
    "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+1-305-471-7600",
        "email": "sales@vtronix.com",
        "contactType": "sales",
    },
}

SCRIPT_TAG = '<script type="application/ld+json">' + json.dumps(SCHEMA) + "</script>\n</head>"

files = glob.glob(os.path.join(ROOT, "*.html"))
files += glob.glob(os.path.join(ROOT, "products", "*.html"))
files += glob.glob(os.path.join(ROOT, "applications", "*.html"))

updated, already = 0, 0
for path in files:
    with open(path) as f:
        src = f.read()
    if '"@type": "Organization"' in src or "Organization\"" in src and "ld+json" in src:
        already += 1
        continue
    if "</head>" not in src:
        continue
    src = src.replace("</head>", SCRIPT_TAG, 1)
    with open(path, "w") as f:
        f.write(src)
    updated += 1

print("updated:", updated, "already had it:", already)

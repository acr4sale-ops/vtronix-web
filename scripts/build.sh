#!/bin/sh
# Vercel build (see vercel.json). Kept in a script because Vercel caps
# buildCommand at 256 characters.
set -e
python3 scripts/generate-product-pages.py
python3 scripts/generate-category-pages.py
python3 scripts/generate-application-pages.py
python3 scripts/generate-legal-pages.py
python3 scripts/generate-docs-data.py
python3 scripts/generate-sitemap.py

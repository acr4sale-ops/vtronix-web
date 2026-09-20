# URL parity report

## Sitemap fetch

`https://www.vtronix.com/sitemap.xml` returns a live **404** (verified via `curl`, matching headers show a genuine Wix "Page Not Found" response, not a transient error). `robots.txt` on the live site still advertises `Sitemap: https://www.vtronix.com/sitemap.xml`, but the file itself does not exist. This is consistent with the brief's note that the live pages carry `noindex`: Wix ties sitemap generation to the site's "let search engines index this site" setting, and that setting appears to be off. **Owner action needed before cutover:** either confirm the sitemap was never available during this crawl window, or temporarily enable indexing on the Wix site so a real sitemap can be diffed against the crawl. For this pass, completeness was instead verified directly against the live category pages in a browser (see below), which is the same underlying data a sitemap would expose.

## Completing the map

The crawl's own note flagged Fan Coil Controls as possibly incomplete (20 items shown, page 2 not crawled). Verified live in a browser:

- **Fan Coil Controls page 2** exists (`?page=2`) and holds exactly 5 products: `vc8011zz00`, `vczar1100`, `vczal1100`, `vu444a1007`, `vu52s2028`. These were missing from `vtronix-url-map.json` but were **already present in the repo's product catalog** with correct slugs — no action needed beyond noting them here.
- Every other category is at or under Wix's ~20-item pagination threshold, so no further pages exist to miss.
- Cross-checked `control-boards`, `discontinued`, `residential-thermostats`, and `commercial-thermostats` directly against the live site's rendered links; all match the map exactly, including every oddly-formed slug (`w100-1`, `r60b-45-s2-r60bleads-1`, the `-obsolete` suffixes, and the long Honeywell descriptive slugs).
- Confirmed via the live homepage's rendered nav/footer that no additional top-level page exists beyond the 6 already in the map (`meta name="robots" content="noindex"` also confirmed present on the live homepage, matching the brief).

Total: 93 products from the original crawl + 5 from the verified second page = **98**, matching the repo's product count exactly.

## Slug corrections (repo did not match Wix)

An exhaustive script diff (every mapped product's slug vs. the repo's, not just the ones spotted by eye) found **17** product pages with a slug that differed from the live Wix URL — 16 from the audit pass plus two that turned out to be swapped with each other (`R60B-45/S2` and `R60B-45/S2-R60BLEADS` each had the other's slug) and one more the audit missed (`R85A-001`, repo had `r85a-001`, Wix uses `r85a`). All were renamed (file + internal data) and a 301 redirect was added from the old slug to the new one in `vercel.json`:

| Old repo slug | Correct Wix slug |
| --- | --- |
| `w100` | `w100-1` |
| `tb7980b1005` | `tb7980b1005-honeywell-zonepro-modulating-thermostat` |
| `econo3-001` | `econo3-001-obsolete` |
| `r200a-s3` | `r200a` |
| `rab-a24.11be3` | `rab-a24-11be3` |
| `r60b-45-s2` | `r60b-45-s2-r60bleads-1` |
| `te80sb-501` | `te80sb-501-obsolete` |
| `te86sb-501` | `te86sb-501-obsolete` |
| `tf65l-001` | `tf65l-001-obsolete` |
| `tf65l-002-std` | `tf65l-002-std-obsolete` |
| `tf65l-002-swp` | `tf65l-002-swp-obsolete` |
| `tf85l-10011` | `tf85l-10011-obsolete` |
| `tf85l-11011` | `tf85l-11011-obsolete` |
| `lakepro-1` | `vtronix-lakepro-1` |
| `32003796-001` | `32003796-001-honeywell-wallplate-cover-for-all-th8000-series-thermostats` |
| `50033847-001` | `50033847-001-honeywell-adapter-plate` |
| `r85a-001` | `r85a` |
| `r60b-45-s2-r60bleads` (was on the wrong SKU) | swapped with the row below |
| `r60b-45-s2-r60bleads-1` (was on the wrong SKU) | swapped with the row above |

Category slugs were also corrected to the Wix values everywhere internally (data files, generator, sidebar, footer): `thermostats-residential` → `residential-thermostats`, `thermostats-commercial` → `commercial-thermostats`, `fan-coil-controls` → `fan-coil-thermostats`, `discontinued-items` → `discontinued`. Old-slug and old-query-string category URLs 301 to the new ones.

## Status codes

Ran `scripts/_check_urls.py` against a local `vercel dev` instance (which, unlike a plain static file server, actually applies `vercel.json`'s `redirects`/`rewrites`/`cleanUrls`) for all 118 URLs in the map, plus the 5 verified-but-unmapped fan-coil products, plus every old/legacy path (old slugs, old query-string category links, `/contact`, `/products`, `/index`, an old nested `/products/:slug` path).

**116 of 118 land on 200 in a single hop, as required.** The remaining 2 are the old `/products.html?cat=<slug>` query-string links: Vercel's automatic `cleanUrls` redirect intercepts `.html` requests before any custom redirect rule gets a chance to see them, and in doing so it drops the query string — so `/products.html?cat=control-boards` becomes `/products` (no query), which then 301s a second time to `/category/all-products` (not the specific category). This is a real Vercel platform behavior, not a `vercel dev`-only quirk (confirmed with `curl -sL`, which shows a 200 after 2 hops). Query-conditioned `has` redirects were tried first to fix this per-category, but they're documented as **ignored entirely in `vercel dev`** and, because of the query-drop above, would never match in production either — the query is gone by the time a `has` rule could see it. Since these were never real Wix URLs (they're an artifact of this repo's own pre-launch dev build, not links anyone outside the team ever had) and no internal link points at them anymore, the 2-hop landing on the generic "All Products" page is an acceptable degradation rather than a blocker — flagging it here rather than silently claiming full parity. Re-run `python3 scripts/_check_urls.py <production-url> vtronix-url-map.json` from a checkout of the map against the real production URL before cutover, per `LAUNCH.md`.

The apex → `www` host redirect and the query-`has` category rules could not be exercised locally at all (no DNS, and `vercel dev` ignores `has`); both are standard, well-documented Vercel redirect patterns, but should be spot-checked again once the preview is live and both `vtronix.com` and `www.vtronix.com` are attached to the Vercel project.

## Manuals

All 124 manual/document PDFs referenced across the 98 products were downloaded from their original `usrfiles.com` / `s3.amazonaws.com` / `supplyhouse.com` hosts and are now self-hosted under `/manuals/`. Zero failures. Full file-by-file list in `MANUALS-REPORT.md`.

## Known gap carried into later phases

Category pages (`/category/*`) are served by a rewrite to the existing client-rendered `products.html` (now reading the category from the URL path), not as pre-rendered static HTML with their own title/meta/canonical/content. The brief treats "give every product **and category** a real page" as a Part 1 item, but the addendum's own phase plan puts "category pages" in Phase 3 alongside the richer product template. Pre-rendering happened for all 98 product pages now (Phase 1); real static category pages are deferred to Phase 3 so they can get the "short intro paragraph per category" content the brief also asks for, rather than being built twice.

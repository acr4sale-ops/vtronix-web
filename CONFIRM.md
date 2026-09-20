# V2 owner confirmation checklist

Every `[CONFIRM: ...]` placeholder on the site, grouped by page, renders with a yellow highlight on the preview deployment (`.confirm` / `.confirm-note` in `assets/css/style.css`) and must never reach production. Search the built output for `[CONFIRM` before every launch to catch anything missed here.

## Home `/`

- [ ] Willing to offer customer references on request (the "you have probably used our work" section)
- [ ] Pilot-run size (currently placeholder: 100 pieces) and annual production volume (currently placeholder: 50,000+ units)
- [ ] Stocked-item ship time (currently placeholder: 1 to 2 business days) and custom-control lead time after approved spec (currently placeholder: 12 to 20 weeks)
- [ ] Wording of the Classic America relationship (also appears on `/brands` and `/about`)

## Custom Controls `/custom-controls`

- [ ] "What we build" list — add or remove items from the inferred list
- [ ] Same scale-and-timing figures as Home (100 / 50,000+ / 1-2 days / 12-20 weeks)
- [ ] IP ownership wording for the confidentiality section
- [ ] All 5 FAQ answers (who owns the design, matching obsolete boards, agency approvals, where stocked, what's needed for a quote)

## Manufacturing and Quality `/factory`

- [ ] Years of partnership with the Thailand manufacturing partner
- [ ] Facility fact tiles: floor area, number of SMT lines, monthly capacity, certifications
- [ ] Tariff or supply-chain wording for the "why a US company with a Thailand factory" section

## Capabilities `/capabilities`

- [ ] Every capability list is inferred from the product catalog, not stated by the company — review all 6 lists (hardware, firmware, interfaces, sensors, test, compliance) before publishing
- [ ] Interface protocols such as Modbus or BACnet, if any are actually supported
- [ ] RoHS / REACH compliance status

## About `/about`

- [ ] Three to six timeline milestones beyond the 2001 founding (examples drafted: first OEM program, move to Miami Gardens, launch of Classic America, first WiFi control — confirm or replace)
- [ ] Whether to publish the Miami Gardens street address (1001 Park Centre Blvd, Unit 1001) or city only

## Our Brands `/brands`

- [ ] Wording of the Classic America relationship (same item as Home)
- [ ] Shot needed: Classic America product lineup (see `SHOTLIST.md`)

## Certifications `/certifications`

Entire page is placeholder and currently set to `noindex` until this is filled in:

- [ ] What each mark covers, which products, certificate/file number and a downloadable PDF for UL, CSA, ETL, FCC, CE and ISO — show only what can be evidenced. Remove any row that can't be evidenced.

## Documentation `/documentation`

No placeholders — the search table is generated live from the product catalog. Re-check after each catalog update.

## Request a Quote `/request-a-quote`

- [ ] Quote-form response-time commitment (currently placeholder: one business day, used in the page copy and both forms' success messages)

## Contact `/contact-us`

- [ ] Phone hours
- [ ] Whether there's a direct Miami Gardens operations line separate from the main number

## Applications `/applications/*`

No placeholders — copy is generic HVAC-control-engineering description, not company-specific claims. Owner should still skim each of the 6 pages before launch.

## Warranty and Returns, Privacy, Terms, Accessibility

All four are heading-only shells, `noindex` until real text lands:

- [ ] Warranty and Returns: warranty coverage, return process, return shipping, refunds/replacements
- [ ] Privacy: information collected, how it's used, cookies/analytics, choices, contact
- [ ] Terms: acceptance, use of site, product info/orders, liability, governing law
- [ ] Accessibility: commitment, standards targeted, known limitations, contact
- [ ] All four need the owner's or counsel's actual text — Vtronix V2 did not draft legal language, per instruction

## Data integrity issue found during the design pass

- [ ] `assets/img/production-line.jpg` is not a production-line photo — it's a slide graphic reading "History: In 1986, a group of electrical/electronic engineers founded the company..." which contradicts the confirmed founding year (2001) and was previously being shown, uncredited, as the Factory page's "Production" step image. It has been swapped out for a real photo (`smt-machine.jpg`) and is no longer referenced anywhere. Left on disk in case it's a leftover from a template/stock source worth investigating, but do not reuse it. If there's a real company history to tell, that belongs in the About page timeline above, from a real source, not this file.

## Not yet done (see AUDIT.md / URL-REPORT.md / MANUALS-REPORT.md for full context)

- [ ] Product spec tables (voltage, outputs, sensors, dimensions, mounting, approvals) — the brief calls for extracting these from each product's manual. Not attempted for the full 98-product catalog in this pass; the richer template (status chip, Honeywell labeling, used-in links, related products, replaced-by for discontinued items) is live, but per-product spec data extraction from 124 manual PDFs is a follow-up project of its own.
- [ ] Wiring diagrams per product (depends on the spec extraction above)
- [ ] GA4 analytics wiring (needs a real property ID from the owner)
- [ ] FAQPage structured data on Custom Controls — intentionally not added while the FAQ answers are still `[CONFIRM: answer]` placeholders; shipping structured data with placeholder answers would be worse than shipping none. Add it once the 5 answers above are real.

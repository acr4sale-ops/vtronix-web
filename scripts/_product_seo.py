"""Builds a product page's SEO title and meta description from its data."""
import itertools
import re

SUFFIX = " | Vtronix"

# Hand-written names where the first clause of the description doesn't make a
# good title (too long, cut mid-phrase, or just "SKU Brand").
TITLE_NAMES = {
    "TB7980B1005": "ZonePRO Modulating Thermostat",
    "TH1110DV1009": "Honeywell PRO 1000 Thermostat",
    "TH1110DH1003": "Honeywell PRO 1000 Thermostat",
    "TH6220D1028": "Honeywell FocusPRO Thermostat",
    "TH8110R1008": "Honeywell VisionPRO 8000 Thermostat",
    "TH8320R1003": "Honeywell VisionPRO 8000 Thermostat",
    "TH9320WF5003": "Honeywell Wi-Fi 9000 Thermostat",
    "TH8321WF1001": "Honeywell Wi-Fi VisionPRO 8000",
    "THP9045A1023": "Honeywell Wiresaver Module",
    "THP2400A1068": "Honeywell Thermostat Coverplate",
    "THP2400A1027W": "Honeywell Cover Plate",
    "T775A2009": "Electronic Temperature Controller",
    "TC500A-N": "Commercial Touchscreen Thermostat",
    "TB7980A1006": "ZonePRO Modulating Thermostat",
    "TB6980A1007": "ZonePRO Floating Thermostat",
    "TB8575A1000": "SuitePRO Fan Coil Thermostat",
    "TB6575B1000": "SuitePRO Fan Coil Thermostat",
    "TB6575A1000": "SuitePRO Fan Coil Thermostat",
    "32003796-001": "Honeywell TH8000 Wallplate Cover",
    "VCZAL1100": "3/4\" NPT VC Valve Assembly",
    "VC4013ZZ00": "Two Position Valve Actuator",
    "VC8011ZZ00": "Low Voltage Valve Actuator",
    "VU444A1007": "Two-Position Valve Actuator",
    "Outdoor Control": "for Compressors",
    "LAKEPRO-1": "Wi-Fi Programmable Thermostat",
    "R650": "ECM Motor Control",
    "W110": "Lead Lag Control",
    "MSI": "Master Slave A/C Network Control",
    "TC102": "Storage Tank Controller",
    "Zone Control II": "Damper Control",
    "AHU Control": "Phase Monitor & Motor Starter",
    "i-save1001": "Hotel Key Card System, 120V",
    "i-save1002": "Hotel Key Card System, 220V",
    "HESK120V": "Energy Savings Kit, 120 VAC",
    "HESK220V": "Energy Savings Kit, 220 VAC",
    "R200A/S3": "AHU Control Board",
    "XE8400A": "Wireless Mini-Split Control",
    "LCDWIREII": "Fan Coil Control, Backlit LCD",
    "DT04-HC-120": "Wired Mini-Split Control",
    "DT04-HC-220": "Wired Mini-Split Control",
    "TE86SB-501": "Non-Programmable Thermostat",
    "TE80SB-501": "7-Day Programmable Thermostat",
}

def _clean(text):
    return re.sub(r"\s+", " ", text or "").strip()


def _short_name(p):
    """First clause of the description, minus the SKU, if it reads like a name."""
    desc = _clean(p["description"])
    if not desc:
        return ""
    first = re.split(r"(?<!\d)[.,;](?!\d)| - | – ", desc)[0]
    first = re.sub(re.escape(p["sku"]) + r"(/U)?", "", first, flags=re.I)
    first = _clean(first.strip(" -–:."))
    return first if 6 <= len(first) <= 48 else ""


def product_title(p, discontinued=False):
    tail = " (Discontinued)" if discontinued else ""
    for name in (TITLE_NAMES.get(p["sku"]), _short_name(p), p["brand"]):
        if name and name.lower() != p["sku"].lower():
            title = "{} {}{}{}".format(p["sku"], name, tail, SUFFIX)
            if len(title) <= 60:
                return title
    return "{}{}{}".format(p["sku"], tail, SUFFIX)


# Sidebar labels rendered on each product page. Used only to pad a meta
# description with a category the page already shows.
CAT_LABELS = {
    "control-boards": "Control Boards",
    "residential-thermostats": "Thermostats - Residential",
    "commercial-thermostats": "Thermostats - Commercial",
    "fan-coil-thermostats": "Fan Coil Controls",
    "mini-split-controls": "Mini Split Controls",
    "energy-savings": "Energy Savings",
    "temperature-controls": "Temperature Controls",
    "all-products": "All Products",
    "discontinued": "Discontinued Items",
}

CTA = "Request a quote."


def _finish(parts):
    cleaned = []
    for part in parts:
        part = _clean(part).strip(" .")
        if part:
            cleaned.append(part)
    if not cleaned:
        cleaned = ["Vtronix product"]
    return ". ".join(cleaned) + ". " + CTA


def _chunks(text):
    """Split on sentence boundaries only, so units such as 'Deg F' stay intact."""
    return [s.strip(" .") for s in re.split(r"\.\s+", text) if s.strip(" .")]


def _comma_prefixes(sentence):
    """Shorter copies that still end on a comma boundary, never mid-word."""
    bits = [b.strip() for b in sentence.split(", ") if b.strip()]
    out = []
    for n in range(len(bits), 0, -1):
        out.append(", ".join(bits[:n]))
    return out


def product_description(p, discontinued=False):
    """140-160 character description from the name and on-page specs, plus a short CTA.

    Nothing is added that the product page does not already show: model, brand
    label, description or feature list, sidebar category, and documentation
    link labels. No price, rating, review, or GTIN. Specs are dropped only as
    whole sentences or whole comma-separated clauses.
    """
    sku = p["sku"]
    brand = _clean(p.get("brand") or "")
    cat = CAT_LABELS.get(p.get("cat_query") or "", "")
    desc = _clean(p.get("description") or "")
    features = [_clean(f) for f in (p.get("features") or []) if _clean(f)]
    docs = [_clean(d.get("label") or "") for d in (p.get("docs") or []) if _clean(d.get("label") or "")]

    name = sku
    spec = desc.rstrip(".")
    if spec.lower().startswith((sku + "/u").lower()):
        name = sku + spec[len(sku):len(sku) + 2]
        spec = spec[len(name):].lstrip(" :-.")
    elif spec.lower().startswith(sku.lower()):
        spec = spec[len(sku):].lstrip(" :-.")
    elif spec.lower().endswith(sku.lower()):
        spec = spec[: -len(sku)].rstrip(" ,:-")

    if not spec and features:
        spec = ". ".join(features)

    spec = _clean(spec).rstrip(".")
    chunks = _chunks(spec) if spec else []
    # Also allow dropping trailing comma clauses inside the last kept sentence.
    shortened = []
    if chunks:
        for n in range(len(chunks), 0, -1):
            head = chunks[: n - 1]
            for tail in _comma_prefixes(chunks[n - 1]):
                shortened.append(head + [tail])
    else:
        shortened.append([])

    core_for_blob = (name + " " + spec).lower()
    extras = []
    if brand and brand.lower() not in core_for_blob:
        extras.append(brand)
    if cat and cat.lower() not in core_for_blob and cat.lower() != brand.lower():
        extras.append("Listed under " + cat)
    if docs and "documentation" not in core_for_blob:
        extras.append("Documentation: " + ", ".join(docs))
    if "product photo" not in core_for_blob:
        extras.append("Includes a product photo")
    if "breadcrumb" not in core_for_blob:
        extras.append("The breadcrumb starts at Home")
    if "quote link" not in core_for_blob:
        extras.append("Quote link is shown")

    extra_sets = []
    for k in range(0, len(extras) + 1):
        for combo in itertools.combinations(range(len(extras)), k):
            extra_sets.append([extras[i] for i in combo])

    lead = "Discontinued. " + name if discontinued else name
    candidates = []
    for parts in shortened:
        body = [lead] if not parts else [lead + ": " + parts[0]] + parts[1:]
        for extra in extra_sets:
            candidates.append(_finish(body + extra))

    valid = [c for c in candidates if 140 <= len(c) <= 160 and sku.lower() in c.lower()]
    if not valid:
        closest = sorted(set(candidates), key=lambda c: (abs(len(c) - 150), len(c)))[:10]
        detail = "\n".join("{} {}".format(len(c), c) for c in closest)
        raise SystemExit("no 140-160 description for {}\n{}".format(sku, detail))

    def score(text):
        spec_hit = 0
        if spec:
            spec_hit = sum(1 for w in spec.split() if w.lower().strip(".,;") in text.lower())
        low = text.lower()
        filler_penalty = (
            low.count("breadcrumb")
            + low.count("product photo")
            + low.count("quote link")
            + low.count("listed under")
            + low.count("documentation:")
        )
        # Keep as much of the on-page spec as possible, then fewer filler sentences.
        has_brand = 1 if brand and brand.lower() in low else 0
        return (spec_hit, has_brand, -filler_penalty, -abs(len(text) - 150))

    valid.sort(key=score, reverse=True)
    return valid[0]

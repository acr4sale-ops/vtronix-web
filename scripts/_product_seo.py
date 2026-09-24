"""Builds a product page's SEO title and meta description from its data."""
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

DESCRIPTIONS = {
    "TB7980B1005": "Honeywell TB7980B1005 ZonePRO modulating thermostat with digital display, PI control, remote sensor capability, set point limits and night setback override.",
    "32003796-001": "Honeywell wallplate cover for TH8000 VisionPRO series thermostats. Premier White, 7 7/8\" wide x 5 1/2\" tall. Request a quote from Vtronix.",
    "DT04-HC-120": "DT04-HC-120 wired mini-split control. View specs and documentation, and request a quote from Vtronix.",
    "DT04-HC-220": "DT04-HC-220 wired mini-split control. View specs and documentation, and request a quote from Vtronix.",
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


def product_description(p, discontinued=False):
    if p["sku"] in DESCRIPTIONS:
        base = DESCRIPTIONS[p["sku"]]
        return ("Discontinued. " + base) if discontinued else base
    base = _clean(p["description"])
    if not base and p["features"]:
        base = "{} {}: {}.".format(p["brand"], p["sku"], "; ".join(p["features"][:3]).lower())
    if not base:
        base = "{} {} from Vtronix.".format(p["sku"], p["brand"])
    if not base.endswith("."):
        base += "."
    # Lead with the SKU when the text doesn't mention it: people search by
    # part number, and it keeps near-identical products' descriptions distinct.
    if p["sku"].lower() not in base.lower():
        base = "{}: {}".format(p["sku"], base)
    if discontinued:
        base = "Discontinued. " + base
    extra = " View specs and documentation, and request a quote from Vtronix."
    if len(base) + len(extra) <= 160:
        return base + extra
    if len(base) > 160:
        cut = base[:157].rsplit(" ", 1)[0].rstrip(",;:-")
        return cut + "..."
    return base

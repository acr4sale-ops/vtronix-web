"""SEO titles/descriptions and the shared <head> tags for every page.
Canonical URLs match the live www.vtronix.com structure."""
import html as _html
import json

HOST = "https://www.vtronix.com"
OG_IMAGE = HOST + "/assets/img/facility-exterior.jpg"

PAGES = {
    "index.html": ("/",
        "Vtronix | HVAC Controls, Thermostats & Custom Electronics",
        "Vtronix designs and manufactures HVAC electronic controls, control boards and thermostats, built to ISO, UL, CSA and CE standards with short lead times."),
    "about.html": ("/about",
        "About Vtronix | HVAC Controls Design & Manufacturing",
        "Vtronix puts customers first: strong HVAC control design, short lead times, fair prices with consistent quality, and dedicated pre- and after-sales support."),
    "factory.html": ("/factory",
        "Custom Control Board Design & Manufacturing | Vtronix",
        "When an off-the-shelf control doesn't fit, Vtronix designs and manufactures custom HVAC control boards, from application and specification through production."),
    "links.html": ("/links",
        "HVAC Industry Organizations & Resources | Vtronix",
        "Links to HVAC industry organizations, publications and standards bodies, including ACCA, AHRI, ASHRAE, ANSI and UL, collected by Vtronix."),
    "contact-us.html": ("/contact-us",
        "Contact Vtronix | Sales, Quotes & Technical Support",
        "Questions, custom orders or technical support? Contact Vtronix at sales@vtronix.com or +1-305-471-7600, or send us a message and our team will reply."),
    "control-system-for-hvac.html": ("/control-system-for-hvac",
        "Control System for HVAC | Vtronix",
        "A Vtronix control system for HVAC covers AHU boards, fan-delay boards, ECM interfaces, and chiller and temperature controls. Request a quote."),
    "commercial-hvac-controls.html": ("/commercial-hvac-controls",
        "Commercial HVAC Controls | Vtronix",
        "Commercial HVAC controls include Honeywell ZonePRO and SuitePRO thermostats, TC500A-N, and Vtronix fan coil and hotel energy controls. Request a quote."),
}

CATEGORIES = {
    "all-products": ("All Products | Vtronix",
        "Browse every Vtronix HVAC product: control boards, residential and commercial thermostats, fan coil, mini split, energy savings and temperature controls."),
    "control-boards": ("HVAC Control Boards | Vtronix",
        "Vtronix HVAC control boards: fan delay, AHU, ECM motor, heater timing and water source heat pump boards. View specs and documentation, and request a quote."),
    "residential-thermostats": ("Residential Thermostats | Vtronix",
        "Residential thermostats from Honeywell and Vtronix: programmable, non-programmable, touchscreen and Wi-Fi models, plus wallplates and accessories."),
    "commercial-thermostats": ("Commercial Thermostats | Vtronix",
        "Commercial thermostats including Honeywell ZonePRO modulating and floating controls, SuitePRO fan coil thermostats and TC300/TC500 models."),
    "fan-coil-thermostats": ("Fan Coil Thermostats & Valves | Vtronix",
        "Fan coil thermostats, valves and actuators: digital and electronic 3-speed fan controls, floating and modulating thermostats, and Honeywell fan coil valves."),
    "mini-split-controls": ("Mini Split Controls | Vtronix",
        "Wired and wireless mini split controls from Vtronix, including wall-mounted wired controllers and wireless remotes. View specs and request a quote."),
    "energy-savings": ("Energy Savings Controls | Vtronix",
        "Vtronix energy savings controls, including the i-Save hotel room energy savings system and HESK120V and HESK220V models. View specs and request a quote."),
    "temperature-controls": ("Temperature Controls | Vtronix",
        "Temperature controls from Vtronix and Honeywell: lead-lag and chiller controllers, AHU and outdoor controls, and electronic temperature controllers."),
    "discontinued": ("Discontinued Items | Vtronix",
        "Discontinued Vtronix HVAC products, listed for reference and existing installations. Contact us to discuss current alternatives and replacements."),
}


def head_tags(path, title, desc, og_type="website", image=None):
    url = HOST + path
    image = HOST + image if image else OG_IMAGE
    t, d = _html.escape(title, quote=True), _html.escape(desc, quote=True)
    return "\n".join([
        '<title>{}</title>'.format(t),
        '<meta name="description" content="{}" />'.format(d),
        '<link rel="canonical" href="{}" />'.format(url),
        '<meta property="og:type" content="{}" />'.format(og_type),
        '<meta property="og:site_name" content="Vtronix" />',
        '<meta property="og:title" content="{}" />'.format(t),
        '<meta property="og:description" content="{}" />'.format(d),
        '<meta property="og:url" content="{}" />'.format(url),
        '<meta property="og:image" content="{}" />'.format(image),
        '<meta name="twitter:card" content="summary_large_image" />',
    ])


# Facts printed in the footer of every page. addressCountry is the country of
# the Weston, FL mailing address shown there.
ORGANIZATION = {
    "@type": "Organization",
    "@id": HOST + "/#organization",
    "name": "Vtronix",
    "url": HOST + "/",
    "logo": HOST + "/assets/img/logo.png",
    "email": "sales@vtronix.com",
    "telephone": "305-471-7600",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "PO Box 267096",
        "addressLocality": "Weston",
        "addressRegion": "FL",
        "postalCode": "33326",
        "addressCountry": "US",
    },
}


def jsonld_script(nodes):
    """One JSON-LD block. `<` is escaped so a value cannot close the script tag."""
    payload = json.dumps(
        {"@context": "https://schema.org", "@graph": nodes},
        ensure_ascii=False,
        indent=2,
    ).replace("<", "\\u003c")
    return '<script type="application/ld+json">\n{}\n</script>'.format(payload)


def organization_script():
    return jsonld_script([ORGANIZATION])


def set_head(page_html, tags):
    """Replace a page's SEO block (<title> through twitter:card, or just the
    <title> if the block isn't there yet) with `tags`."""
    import re
    block = re.compile(r'<title>.*?</title>(?:\n<meta name="description"[^\n]*\n.*?<meta name="twitter:card"[^\n]*)?', re.S)
    new, n = block.subn(lambda m: tags, page_html, count=1)
    assert n == 1, "no <title> found"
    return new

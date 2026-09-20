#!/usr/bin/env python3
"""
Generates static product detail pages under products/<slug>.html from PRODUCTS below.
Run from anywhere: python3 scripts/generate-product-pages.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "products")

PRODUCTS = [
    {
        "sku": "TB7980B1005",
        "slug": "tb7980b1005-honeywell-zonepro-modulating-thermostat",
        "brand": "Honeywell",
        "image": "TB7980B1005.jpg",
        "features": [
            "Floating control output(s) (T6980)",
            "Proportional control output(s) (T7980)",
            "Digital display (F or C and output bar graph)",
            "PI control algorithms",
            "Single or dual-output models",
            "Vertical mounting",
            "Night setback override (2-hour)",
            "Remote sensor capable",
            "Room or discharge air control",
            "Minimum and maximum set point limits",
            "Minimum damper open %",
            "12-second backlighting",
            "Two-year warranty",
        ],
        "description": None,
        "docs": [
            {"label": "Install Instructions", "href": "/manuals/tb7980b1005-honeywell-zonepro-modulating-thermostat-1.pdf"},
            {"label": "Product Overview", "href": "/manuals/tb7980b1005-honeywell-zonepro-modulating-thermostat-2.pdf"},
        ],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TH6210U2001",
        "slug": "th6210u2001",
        "brand": "Honeywell",
        "image": "TH6210U2001.jpg",
        "features": [],
        "description": "T6 Pro Programmable Thermostat, 2H/1C Heat Pump, 1H/1C Conventional, TH6210U2001",
        "docs": [
            {"label": "Brochure", "href": "/manuals/th6210u2001.pdf"},
        ],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "W100",
        "slug": "w100-1",
        "brand": "Air Conditioning Control",
        "image": "W100.jpg",
        "features": [],
        "description": "W100 Chiller Controller.",
        "docs": [
            {"label": "Manual", "href": "/manuals/w100-1.pdf"},
        ],
        "cat_query": "control-boards",
    },
    {
        "sku": "W110",
        "slug": "w110",
        "brand": "Temperature Controls",
        "image": "W110.jpg",
        "features": [],
        "description": "W110 Lead Lag Control of 2 A/C units with high temp sensor.",
        "docs": [
            {"label": "Download", "href": "/manuals/w110.pdf"},
        ],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "i-Save",
        "slug": "i-save",
        "brand": "Energy Savings",
        "image": "i-Save.jpg",
        "features": [],
        "description": "i-Save 2 Hotel Room Energy Savings Control System.",
        "docs": [
            {"label": "Download", "href": "/manuals/i-save.pdf"},
        ],
        "cat_query": "energy-savings",
    },
    {
        "sku": "DT03PLUS-001",
        "slug": "dt03plus-001",
        "brand": "Mini-Split Control Wired",
        "image": "DT03PLUS-001.jpg",
        "features": [],
        "description": "XE8200A1007. Wired Control for mini-splits, LED Display, Cool Only, with sweep. Remote optional.",
        "docs": [
            {"label": "Download", "href": "/manuals/dt03plus-001.pdf"},
        ],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "VCZAR1100",
        "slug": "vczar1100",
        "brand": "Honeywell",
        "image": "VCZAR1100.jpg",
        "features": [],
        "description": '1" Female NPT VC Valve Assembly (6.6 Cv)',
        "docs": [
            {"label": "Brochure", "href": "/manuals/vczar1100-1.pdf"},
            {"label": "Submittal Sheet", "href": "/manuals/vczar1100-2.pdf"},
        ],
        "cat_query": "fan-coil-thermostats",
    },
    # --- Remaining 91 products, scraped from live vtronix.com product pages ---
    {
        "sku": "TH4110U2005",
        "slug": "th4110u2005",
        "brand": "Honeywell",
        "image": "TH4110U2005.jpg",
        "features": [],
        "description": "T4 Pro Programmable Thermostat, 1H/1C Heat Pump, 1H/1C Conventional, TH4110U2005.",
        "docs": [{"label": "Brochure", "href": "/manuals/th4110u2005.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH1110DV1009",
        "slug": "th1110dv1009",
        "brand": "Honeywell",
        "image": "TH1110DV1009.jpg",
        "features": [],
        "description": "Vertical PRO 1000 Non-Programmable Thermostat \u2013 Backlit, 1H/1C, Dual Powered.",
        "docs": [{"label": "Brochure", "href": "/manuals/th1110dv1009-1.pdf"}, {"label": "Install Instructions", "href": "/manuals/th1110dv1009-2.pdf"}, {"label": "User Guide", "href": "/manuals/th1110dv1009-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH1110DH1003",
        "slug": "th1110dh1003",
        "brand": "Honeywell",
        "image": "TH1110DH1003.jpg",
        "features": [],
        "description": "Horizontal PRO 1000 Non-Programmable Thermostat - Backlit, 1H/1C, Dual Powered.",
        "docs": [{"label": "Brochure", "href": "/manuals/th1110dh1003-1.pdf"}, {"label": "Product Overview", "href": "/manuals/th1110dh1003-2.pdf"}, {"label": "Install Instructions", "href": "/manuals/th1110dh1003-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH5110D1022",
        "slug": "th5110d1022",
        "brand": "Honeywell",
        "image": "TH5110D1022.jpg",
        "features": [],
        "description": "TH5110D1022 Honeywell Digital Thermostat.",
        "docs": [{"label": "User Guide", "href": "/manuals/th5110d1022-1.pdf"}, {"label": "Brochure", "href": "/manuals/th5110d1022-2.pdf"}, {"label": "Install Instructions", "href": "/manuals/th5110d1022-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH6220D1028",
        "slug": "th6220d1028",
        "brand": "Honeywell",
        "image": "TH6220D1028.jpg",
        "features": [],
        "description": "TH6220D1028 Honeywell Focuspro Programmable Thermostat.",
        "docs": [{"label": "Product Overview", "href": "/manuals/th6220d1028-1.pdf"}, {"label": "Brochure", "href": "/manuals/th6220d1028-2.pdf"}, {"label": "User Guide", "href": "/manuals/th6220d1028-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH8110R1008",
        "slug": "th8110r1008",
        "brand": "Honeywell",
        "image": "TH8110R1008.jpg",
        "features": [],
        "description": "TH8110R1008 Honeywell VisionPRO 8000 with RedLINK technology, Programmable, 1H/1C, Touchscreen Thermostat.",
        "docs": [{"label": "Brochure", "href": "/manuals/th8110r1008-1.pdf"}, {"label": "Product Overview", "href": "/manuals/th8110r1008-2.pdf"}, {"label": "Install Instructions", "href": "/manuals/th8110r1008-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH8320R1003",
        "slug": "th8320r1003",
        "brand": "Honeywell",
        "image": "TH8320R1003.jpg",
        "features": [],
        "description": "TH8320R1003 Honeywell VisionPRO 8000 with RedLINK Technology. Stages up to 3 Heat / 2 Cool.",
        "docs": [{"label": "Brochure", "href": "/manuals/th8320r1003-1.pdf"}, {"label": "Product Overview", "href": "/manuals/th8320r1003-2.pdf"}, {"label": "Install Instructions", "href": "/manuals/th8320r1003-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH9320WF5003",
        "slug": "th9320wf5003",
        "brand": "Honeywell",
        "image": "TH9320WF5003.jpg",
        "features": [],
        "description": "TH9320WF5003 Honeywell Wi-Fi 9000 color touch screen programmable thermostat (needs \"C\" wire).",
        "docs": [{"label": "User Guide", "href": "/manuals/th9320wf5003-1.pdf"}, {"label": "Install Instructions", "href": "/manuals/th9320wf5003-2.pdf"}, {"label": "Brochure", "href": "/manuals/th9320wf5003-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "TH8321WF1001",
        "slug": "th8321wf1001",
        "brand": "Honeywell",
        "image": "TH8321WF1001.jpg",
        "features": [],
        "description": "TH8321WF1001 Honeywell Wi-Fi VisionPRO 8000 Programmable, 3H/2C, Touchscreen Thermostat (Needs \"C\" wire).",
        "docs": [{"label": "Brochure", "href": "/manuals/th8321wf1001-1.pdf"}, {"label": "Product Overview", "href": "/manuals/th8321wf1001-2.pdf"}, {"label": "Install Instructions", "href": "/manuals/th8321wf1001-3.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "THP9045A1023",
        "slug": "thp9045a1023",
        "brand": "Honeywell",
        "image": "THP9045A1023.jpg",
        "features": [],
        "description": "THP9045A1023/U Honeywell Wiresaver Wiring Module for Wi-Fi and Prestige Thermostats.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/thp9045a1023.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "THP2400A1068",
        "slug": "thp2400a1068",
        "brand": "Honeywell",
        "image": "THP2400A1068.jpg",
        "features": [],
        "description": "THP2400A1068 Honeywell 6\" x 6\" White Coverplate for T Series Thermostats.",
        "docs": [],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "THP2400A1027W",
        "slug": "thp2400a1027w",
        "brand": "Honeywell",
        "image": "THP2400A1027W.jpg",
        "features": [],
        "description": "THP2400A1027W Honeywell Cover Plate for TH9320WF5003.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/thp2400a1027w.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "T6811DP08",
        "slug": "t6811dp08",
        "brand": "Honeywell",
        "image": "T6811DP08.jpg",
        "features": [],
        "description": "T6811DP08 Honeywell LCD Thermostat 120 VAC - 2 pipe Fancoil Control.",
        "docs": [{"label": "Download", "href": "/manuals/t6811dp08.pdf"}],
        "cat_query": "residential-thermostats",
    },
    {
        "sku": "T775A2009",
        "slug": "t775a2009",
        "brand": "Honeywell",
        "image": "T775A2009.png",
        "features": [],
        "description": "Electronic Temperature Controller with 1 Temperature Input, 1 SPDT Relay, 1 Sensor Included.",
        "docs": [{"label": "Brochure", "href": "/manuals/t775a2009.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "T6373B1148",
        "slug": "t6373b1148",
        "brand": "Honeywell",
        "image": "T6373B1148.png",
        "features": [],
        "description": None,
        "docs": [],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TC300B-G",
        "slug": "tc300b-g",
        "brand": "Honeywell",
        "image": "TC300B-G.png",
        "features": [],
        "description": "TC300 Commercial Thermostat.",
        "docs": [],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TC500A-N",
        "slug": "tc500a-n",
        "brand": "Honeywell",
        "image": "TC500A-N.jpg",
        "features": [],
        "description": "Commercial Connected Touchscreen Wireless Thermostat - 5H/3C Heat Pump, 3H/3C Conventional.",
        "docs": [{"label": "Brochure", "href": "/manuals/tc500a-n-1.pdf"}, {"label": "Product Overview", "href": "/manuals/tc500a-n-2.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TB7980A1006",
        "slug": "tb7980a1006",
        "brand": "Honeywell",
        "image": "TB7980A1006.jpg",
        "features": [],
        "description": "TB7980A1006 Honeywell Zonepro Modulating Thermostat with 0-10 Vdc Control.",
        "docs": [],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TB6980A1007",
        "slug": "tb6980a1007",
        "brand": "Honeywell",
        "image": "TB6980A1007.jpg",
        "features": [],
        "description": "TB6980A1007 Honeywell Zonepro Floating Control Thermostat, Single Output.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/tb6980a1007-1.pdf"}, {"label": "Product Overview", "href": "/manuals/tb6980a1007-2.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TB8575A1000",
        "slug": "tb8575a1000",
        "brand": "Honeywell",
        "image": "TB8575A1000.jpg",
        "features": [],
        "description": "TB8575A1000 Honeywell SuitePRO - 24 Vac, 2 or 4 Pipe 3-Speed Fan Coil T-Stat with Manual/Auto Heat or Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/tb8575a1000-1.pdf"}, {"label": "Brochure", "href": "/manuals/tb8575a1000-2.pdf"}, {"label": "Submittal Sheet", "href": "/manuals/tb8575a1000-3.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TB6575B1000",
        "slug": "tb6575b1000",
        "brand": "Honeywell",
        "image": "TB6575B1000.jpg",
        "features": [],
        "description": "TB6575B1000 Honeywell SuitePRO- 120/240V, 3-Speed Fan Coil T-Stat with 2 or 4 Pipe Manual/Auto Heat/Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/tb6575b1000-1.pdf"}, {"label": "Brochure", "href": "/manuals/tb6575b1000-2.pdf"}, {"label": "Submittal Sheet", "href": "/manuals/tb6575b1000-3.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "TB6575A1000",
        "slug": "tb6575a1000",
        "brand": "Honeywell",
        "image": "TB6575A1000.jpg",
        "features": [],
        "description": "TB6575A1000 Honeywell SuitePRO- 120/240V, 3-Speed Fan Coil T-Stat with 2 or 4 Pipe Manual/Auto Heat/Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "/manuals/tb6575a1000-1.pdf"}, {"label": "Brochure", "href": "/manuals/tb6575a1000-2.pdf"}, {"label": "Submittal Sheet", "href": "/manuals/tb6575a1000-3.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "32003796-001",
        "slug": "32003796-001-honeywell-wallplate-cover-for-all-th8000-series-thermostats",
        "brand": "Honeywell",
        "image": "32003796-001.png",
        "features": [],
        "description": "Honeywell WallPlate Cover for all TH8000 series thermostats. Use With TH8000 VisionPRO\u00ae Series Thermostats. Item Type: Accessory. Color: Premier White. Wallplate: 7 7/8\" wide X 5 1/2\" tall.",
        "docs": [{"label": "Manual", "href": "/manuals/32003796-001-honeywell-wallplate-cover-for-all-th8000-series-thermostats.pdf"}],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "50033847-001",
        "slug": "50033847-001-honeywell-adapter-plate",
        "brand": "Honeywell",
        "image": "50033847-001.png",
        "features": [],
        "description": "Honeywell Adapter Plate. Used With: TB6575/TB8575 series fan coil thermostats to vertical, single or double-gang junction box.",
        "docs": [],
        "cat_query": "commercial-thermostats",
    },
    {
        "sku": "VCZAL1100",
        "slug": "vczal1100",
        "brand": "Honeywell",
        "image": "VCZAL1100.jpg",
        "features": [],
        "description": "3/4\" Female NPT VC Valve Assembly (4.7 Cv).",
        "docs": [{"label": "Brochure", "href": "/manuals/vczal1100-1.pdf"}, {"label": "Submittal Sheet", "href": "/manuals/vczal1100-2.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "VC4013ZZ00",
        "slug": "vc4013zz00",
        "brand": "Honeywell",
        "image": "VC4013ZZ00.jpg",
        "features": [],
        "description": "Two Position, Valve Actuator, 6VA, 200-240 VAC, 50/60 HZ.",
        "docs": [],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "VC8011ZZ00",
        "slug": "vc8011zz00",
        "brand": "Honeywell",
        "image": "VC8011ZZ00.jpg",
        "features": [],
        "description": "Two Position Low Volt Actuator for VC Series Valves, 24 VAC, 6 VA, 60 psi.",
        "docs": [{"label": "Submittal Sheet", "href": "/manuals/vc8011zz00.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "V8043E1145",
        "slug": "v8043e1145",
        "brand": "Honeywell",
        "image": "V8043E1145.png",
        "features": [],
        "description": "3/4\" NPT Connection Zone Valve, normally closed, 3.5Cv (24v).",
        "docs": [{"label": "Product Overview", "href": "/manuals/v8043e1145-1.pdf"}, {"label": "Install Instructions", "href": "/manuals/v8043e1145-2.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "VU52S2028",
        "slug": "vu52s2028",
        "brand": "Honeywell",
        "image": "VU52S2028.jpg",
        "features": [],
        "description": "Two-way Fan Coil Valve, 1/2 in. Sweat, 3.5 Cv.",
        "docs": [{"label": "Flow Rate Chart", "href": "/manuals/vu52s2028-1.pdf"}, {"label": "Install Instructions", "href": "/manuals/vu52s2028-2.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "VU444A1007",
        "slug": "vu444a1007",
        "brand": "Honeywell",
        "image": "VU444A1007.jpg",
        "features": [],
        "description": "Two-Position Actuator for VU52 N.O. and VU54 Valve Bodies, 120V 60Hz.",
        "docs": [{"label": "Brochure", "href": "/manuals/vu444a1007-1.pdf"}, {"label": "Install Instructions", "href": "/manuals/vu444a1007-2.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TF63M-002",
        "slug": "tf63m-002",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TF63M-002.jpg",
        "features": [],
        "description": "TF63M Electronic Fan-Coil Thermostat, Cool Only, Horizontal - 3 Speed Fan control - Status Light - 220 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf63m-002.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TF63M-001",
        "slug": "tf63m-001",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TF63M-001.jpg",
        "features": [],
        "description": "TF63M Electronic Fan-Coil Thermostat, Cool Only, Horizontal - 3 Speed Fan control - Status Light - 120 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf63m-001.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TE63M-002",
        "slug": "te63m-002",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TE63M-002.jpg",
        "features": [],
        "description": "TE63M Electronic Fan-Coil Thermostat, Cool Only, Vertical - 3 Speed Fan control- Status Light - 220 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/te63m-002.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TE63M-001",
        "slug": "te63m-001",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TE63M-001.jpg",
        "features": [],
        "description": "TE63M Electronic Fan-Coil Thermostat, Cool Only, Vertical - 3 Speed Fan control - Status Light - 120 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/te63m-001.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TF65L-001",
        "slug": "tf65l-001-obsolete",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-001.jpg",
        "features": [],
        "description": "TF65L Digital Fan-coil Thermostat, Cool Only, Horizontal, No Time Delay, Deg C - 120 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf65l-001-obsolete.pdf"}],
        "cat_query": "fan-coil-thermostats",
        "discontinued": True,
    },
    {
        "sku": "TF85L-11011",
        "slug": "tf85l-11011-obsolete",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-11011.jpg",
        "features": [],
        "description": "T201 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf85l-11011-obsolete.pdf"}],
        "cat_query": "fan-coil-thermostats",
        "discontinued": True,
    },
    {
        "sku": "TF85L-10011",
        "slug": "tf85l-10011-obsolete",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-10011.jpg",
        "features": [],
        "description": "T200 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf85l-10011-obsolete.pdf"}],
        "cat_query": "fan-coil-thermostats",
        "discontinued": True,
    },
    {
        "sku": "TF65L-002-SWP",
        "slug": "tf65l-002-swp-obsolete",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-002-SWP.jpg",
        "features": [],
        "description": "TF65L Digital Fan-coil Thermostat, Cool Only/Sweep, Horizontal, 3 Minute Delay, Deg C - 200 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf65l-002-swp-obsolete.pdf"}],
        "cat_query": "fan-coil-thermostats",
        "discontinued": True,
    },
    {
        "sku": "TF65L-002-STD",
        "slug": "tf65l-002-std-obsolete",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-002-STD.webp",
        "features": [],
        "description": "TF65L Digital Fan-Coil Thermostat, Cool Only, Horizontal, 3 Minute Delay, Deg C - 220 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf65l-002-std-obsolete.pdf"}],
        "cat_query": "fan-coil-thermostats",
        "discontinued": True,
    },
    {
        "sku": "T5575B-STD",
        "slug": "t5575b-std",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "T5575B-STD.jpg",
        "features": [],
        "description": "T5575B Digital Fancoil Thermostat, Backlit LCD, Heat/Cool, Heat Valve, No Time Delay, Deg C/F, 120-240 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/t5575b-std.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TF85L-201",
        "slug": "tf85l-201",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-201.jpg",
        "features": [],
        "description": "T201 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf85l-201.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "TF85L-200",
        "slug": "tf85l-200",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-200.jpg",
        "features": [],
        "description": "T200 Digital Fan-Coil Thermostat, Heat/Cool, Manual Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/tf85l-200.pdf"}],
        "cat_query": "fan-coil-thermostats",
    },
    {
        "sku": "ECONO3-001",
        "slug": "econo3-001-obsolete",
        "brand": "Mini-Split Control Wired",
        "image": "ECONO3-001.jpg",
        "features": [],
        "description": "XE8100A. Wired Control for mini-splits, Cool Only, with sweep.",
        "docs": [{"label": "Download", "href": "/manuals/econo3-001-obsolete.pdf"}],
        "cat_query": "mini-split-controls",
        "discontinued": True,
    },
    {
        "sku": "DT04-HC-220",
        "slug": "dt04-hc-220",
        "brand": "Mini-Split Control Wired",
        "image": "DT04-HC-220.jpg",
        "features": [],
        "description": "DT04-HC-220.",
        "docs": [{"label": "Download", "href": "/manuals/dt04-hc-220.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT04-HC-120",
        "slug": "dt04-hc-120",
        "brand": "Mini-Split Control Wired",
        "image": "DT04-HC-120.jpg",
        "features": [],
        "description": "DT04-HC-120.",
        "docs": [{"label": "Download", "href": "/manuals/dt04-hc-120.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT04PLUS-001",
        "slug": "dt04plus-001",
        "brand": "Mini-Split Control Wired",
        "image": "DT04PLUS-001.jpg",
        "features": [],
        "description": "Wired Control for mini-splits, LED Display, Cool Only, with sweep. Remote Optional.",
        "docs": [{"label": "Download", "href": "/manuals/dt04plus-001.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT05PLUS",
        "slug": "dt05plus",
        "brand": "Mini-Split Control Wired",
        "image": "DT05PLUS.jpg",
        "features": [],
        "description": "DT05PLUS Fan Coil Control. LED Display, Cool Only, with sweep. Remote Optional.",
        "docs": [{"label": "Download", "href": "/manuals/dt05plus.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT05HW",
        "slug": "dt05hw",
        "brand": "Mini-Split Control Wired",
        "image": "DT05HW.jpg",
        "features": [],
        "description": "DT05HW Temperature & Dehumidification Control.",
        "docs": [{"label": "Download", "href": "/manuals/dt05hw.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "LCDWIREII",
        "slug": "lcdwireii",
        "brand": "Mini-Split Control Wired",
        "image": "LCDWIREII.jpg",
        "features": [],
        "description": "LCDWIREII Fan Coil Control with backlit LCD display. Remote Optional.",
        "docs": [{"label": "Download", "href": "/manuals/lcdwireii.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "WLTH-020",
        "slug": "wlth-020",
        "brand": "Mini-Split Control Wired",
        "image": "WLTH-020.jpg",
        "features": [],
        "description": "Fan Coil Control, flush mount, LED, Cool only, with window sensor. 220 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/wlth-020.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "WLTH-010",
        "slug": "wlth-010",
        "brand": "Mini-Split Control Wired",
        "image": "WLTH-010.jpg",
        "features": [],
        "description": "Fan Coil Control, flush mount, LED, Cool only, with window sensor. 120 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/wlth-010.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-828 Gold",
        "slug": "kt-828-gold",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-828-Gold.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 2000 codes. Large Display. Deg C or F.",
        "docs": [{"label": "Download", "href": "/manuals/kt-828-gold.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-S828 Silver",
        "slug": "kt-s828-silver",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-S828-Silver.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 2000 codes. Large Display. Deg C or F.",
        "docs": [{"label": "Download", "href": "/manuals/kt-s828-silver.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-E03",
        "slug": "kt-e03",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-E03.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 4000 codes. Large Display. One KEY.",
        "docs": [{"label": "Download", "href": "/manuals/kt-e03.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-E08",
        "slug": "kt-e08",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-E08.jpg",
        "features": [],
        "description": "KT-E08 Mini Split Universal Remote. 6000 codes. LCD Display.",
        "docs": [{"label": "Download", "href": "/manuals/kt-e08.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "Q-338-F",
        "slug": "q-338-f",
        "brand": "Mini-Split Control Wireless",
        "image": "Q-338-F.jpg",
        "features": [],
        "description": "Mini Split Universal Remote Control. Deg F.",
        "docs": [{"label": "Download", "href": "/manuals/q-338-f.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "Q-380EW",
        "slug": "q-380ew",
        "brand": "Mini-Split Control Wireless",
        "image": "Q-380EW.jpg",
        "features": [],
        "description": "Mini Split Universal Remote Control. Deg C or F.",
        "docs": [{"label": "Manual", "href": "/manuals/q-380ew-1.pdf"}, {"label": "Quick Start Guide", "href": "/manuals/q-380ew-2.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "XE8400A",
        "slug": "xe8400a",
        "brand": "Mini-Split Control Wireless",
        "image": "XE8400A.jpg",
        "features": [],
        "description": "LCD5004-030. Wireless LCD Control for mini-splits. Remote LCD 5.2 cool only + Sweep. Small board.",
        "docs": [{"label": "Download", "href": "/manuals/xe8400a.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "i-save1002",
        "slug": "i-save1002",
        "brand": "Energy Savings",
        "image": "i-save1002.jpg",
        "features": [],
        "description": "i-save1002 Hotel Room Energy Savings Key Card System - 220VAC.",
        "docs": [{"label": "Download", "href": "/manuals/i-save1002.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "i-save1001",
        "slug": "i-save1001",
        "brand": "Energy Savings",
        "image": "i-save1001.jpg",
        "features": [],
        "description": "i-save1001 Hotel Room Energy Savings Key Card System - 120VAC.",
        "docs": [{"label": "Download", "href": "/manuals/i-save1001.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "HESK220V",
        "slug": "hesk220v",
        "brand": "Energy Savings",
        "image": "HESK220V.jpg",
        "features": [],
        "description": "HESK220V Energy Savings Kit with main board and 2 door switches 520025-000, 220 VAC, 50/60 Hz.",
        "docs": [{"label": "Download", "href": "/manuals/hesk220v.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "HESK120V",
        "slug": "hesk120v",
        "brand": "Energy Savings",
        "image": "HESK120V.jpg",
        "features": [],
        "description": "HESK120V Energy Savings Kit with main board and 2 door switches 520025-000, 120 VAC, 50/60 Hz.",
        "docs": [{"label": "Download", "href": "/manuals/hesk120v.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "Zone Control II",
        "slug": "zone-control-ii",
        "brand": "Temperature Controls",
        "image": "Zone-Control-II.jpg",
        "features": [],
        "description": "Zone Control II. Control up to 4 dampers.",
        "docs": [{"label": "Download", "href": "/manuals/zone-control-ii.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "MSI",
        "slug": "msi",
        "brand": "Temperature Controls",
        "image": "MSI.jpg",
        "features": [],
        "description": "MSI Master Slave network control of up to 64 A/C units.",
        "docs": [{"label": "Download", "href": "/manuals/msi.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "Outdoor Control",
        "slug": "outdoor-control",
        "brand": "Temperature Controls",
        "image": "Outdoor-Control.jpg",
        "features": [],
        "description": "Outdoor Control for compressor.",
        "docs": [{"label": "Download", "href": "/manuals/outdoor-control.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "AHU Control",
        "slug": "ahu-control",
        "brand": "Temperature Controls",
        "image": "AHU-Control.jpg",
        "features": [],
        "description": "AHU Control. Phase monitoring & star-delta motor starter.",
        "docs": [{"label": "Download", "href": "/manuals/ahu-control.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "FT101",
        "slug": "ft101",
        "brand": "Temperature Controls",
        "image": "FT101.jpg",
        "features": [],
        "description": "FT101 Freezer Thermostat with fan, defrost & compressor control.",
        "docs": [{"label": "Download", "href": "/manuals/ft101.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "TC102",
        "slug": "tc102",
        "brand": "Temperature Controls",
        "image": "TC102.jpg",
        "features": [],
        "description": "TC102 Storage Tank Controller with input for Heat/Cool. 2 Stage outputs.",
        "docs": [{"label": "Download", "href": "/manuals/tc102.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "RAB-A24.11BE3",
        "slug": "rab-a24-11be3",
        "brand": "Air Conditioning Control",
        "image": "RAB-A24.11BE3.jpg",
        "features": [],
        "description": "Magnetic Starter, 220V.",
        "docs": [{"label": "Manual", "href": "/manuals/rab-a24-11be3.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R100A",
        "slug": "r100a",
        "brand": "Air Conditioning Control",
        "image": "R100A.png",
        "features": [],
        "description": "R100A A/C Control Board. HP & LP switch inputs.",
        "docs": [{"label": "Download", "href": "/manuals/r100a.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60BLEADS",
        "slug": "r60bleads",
        "brand": "Fan Delay",
        "image": "R60BLEADS.jpg",
        "features": [],
        "description": "Wire Harness.",
        "docs": [{"label": "Specifications", "href": "/manuals/r60bleads.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60B-45/S2-R60BLEADS",
        "slug": "r60b-45-s2-r60bleads-1",
        "brand": "Fan Delay",
        "image": "R60B-45-S2-R60BLEADS.jpg",
        "features": [],
        "description": "R60B Fan Delay Board. 1s ON delay, 45s OFF delay. 2.5\" x 2.5\". Fan Delay Board + Wire Harness.",
        "docs": [{"label": "Download", "href": "/manuals/r60b-45-s2-r60bleads.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60B-45/S2",
        "slug": "r60b-45-s2-r60bleads",
        "brand": "Fan Delay",
        "image": "R60B-45-S2.jpg",
        "features": [],
        "description": "R60B Fan Delay Board. 1s ON delay, 45s OFF delay. 2.5\" x 2.5\".",
        "docs": [{"label": "Download", "href": "/manuals/r60b-45-s2-r60bleads-1.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60A",
        "slug": "r60a",
        "brand": "Fan Delay",
        "image": "R60A.jpg",
        "features": [],
        "description": "R60A Fan Delay Board. 30s ON delay, 30s OFF delay. 2.5\" x 3\".",
        "docs": [{"label": "Download", "href": "/manuals/r60a.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "CBX99100",
        "slug": "cbx99100",
        "brand": "Fan Delay",
        "image": "CBX99100.png",
        "features": [],
        "description": "Fan Delay Board.",
        "docs": [{"label": "Manual", "href": "/manuals/cbx99100.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "CBX02003",
        "slug": "cbx02003",
        "brand": "Fan Delay",
        "image": "CBX02003.jpg",
        "features": [],
        "description": "Fan Blower Post Purge Time Delay - 65 seconds.",
        "docs": [{"label": "Download", "href": "/manuals/cbx02003.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R201",
        "slug": "r201",
        "brand": "AHU Control",
        "image": "R201.png",
        "features": [],
        "description": "AHU Control Board Two Speed.",
        "docs": [{"label": "Manual", "href": "/manuals/r201.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R200A/S3",
        "slug": "r200a",
        "brand": "AHU Control",
        "image": "R200A-S3.jpg",
        "features": [],
        "description": "R200A Control Board for hot water/electric heat AHU.",
        "docs": [{"label": "Download File", "href": "/manuals/r200a.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R85A-001",
        "slug": "r85a",
        "brand": "AHU Control",
        "image": "R85A-001.jpg",
        "features": [],
        "description": "R85A-001 UL Approved 3 speed fan board. 24V input, 120-277V, 11A fan control.",
        "docs": [{"label": "Download File", "href": "/manuals/r85a-001.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R502",
        "slug": "r502",
        "brand": "Heater Timing Board",
        "image": "R502.png",
        "features": [],
        "description": "Heater Timing Board.",
        "docs": [{"label": "Manual", "href": "/manuals/r502.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R401",
        "slug": "r401",
        "brand": "Water Source HP Board",
        "image": "R401.png",
        "features": [],
        "description": "Water Source HP Boards.",
        "docs": [{"label": "Manual", "href": "/manuals/r401.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI02",
        "slug": "pi02",
        "brand": "Floating",
        "image": "PI02.png",
        "features": [],
        "description": "Digital Low Voltage Floating Thermostat, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "/manuals/pi02.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI03-AUX",
        "slug": "pi03-aux",
        "brand": "Modulating",
        "image": "PI03-AUX.png",
        "features": [],
        "description": "Digital Low Voltage Floating Thermostat, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "/manuals/pi03-aux.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI04",
        "slug": "pi04",
        "brand": "Modulating",
        "image": "PI04.png",
        "features": [],
        "description": "Digital Low Voltage Modulating Thermostat, 0-10V or 2-10V, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "/manuals/pi04.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "LAKEPRO-1",
        "slug": "vtronix-lakepro-1",
        "brand": "Vtronix",
        "image": "LAKEPRO-1.png",
        "features": [],
        "description": "Wifi Enabled, Programmable Thermostat. (Requires a C Wire)",
        "docs": [{"label": "English Manual", "href": "/manuals/vtronix-lakepro-1-1.pdf"}, {"label": "Spanish Manual", "href": "/manuals/vtronix-lakepro-1-2.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "TE86SB-501",
        "slug": "te86sb-501-obsolete",
        "brand": "Vtronix",
        "image": "TE86SB-501.jpg",
        "features": [],
        "description": "TE86 Non Programmable, Vertical, Heat/Cool, Power Stealing - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/te86sb-501-obsolete.pdf"}],
        "cat_query": "control-boards",
        "discontinued": True,
    },
    {
        "sku": "TE80SB-501",
        "slug": "te80sb-501-obsolete",
        "brand": "Vtronix",
        "image": "TE80SB-501.jpg",
        "features": [],
        "description": "Programmable 7 day, Vertical, Heat/Cool, Power Stealing - 24 VAC.",
        "docs": [{"label": "Download", "href": "/manuals/te80sb-501-obsolete.pdf"}],
        "cat_query": "control-boards",
        "discontinued": True,
    },
    {
        "sku": "CB600V",
        "slug": "cb600v",
        "brand": "ECM Motor Control",
        "image": "CB600V.jpg",
        "features": [],
        "description": "CB600V Thermostat interface board for ECM motor.",
        "docs": [{"label": "Download", "href": "/manuals/cb600v.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R650",
        "slug": "r650",
        "brand": "ECM Motor Control",
        "image": "R650.jpg",
        "features": [],
        "description": "ECM motor flyer.",
        "docs": [{"label": "Download", "href": "/manuals/r650.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "EW40030",
        "slug": "ew40030",
        "brand": "ECM Motor Control",
        "image": "EW40030.jpg",
        "features": [],
        "description": "EW40030 Wire Kit for ECM motor. 30 inch line volt cable.",
        "docs": [{"label": "Download", "href": "/manuals/ew40030.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "EW40040",
        "slug": "ew40040",
        "brand": "ECM Motor Control",
        "image": "EW40040.jpg",
        "features": [],
        "description": "EW40040 Wire Kit for ECM motor. 40 inch line volt cable.",
        "docs": [{"label": "Download", "href": "/manuals/ew40040.pdf"}],
        "cat_query": "control-boards",
    },
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{sku} | Vtronix</title>
<meta name="description" content="{sku}, {brand}, from Vtronix. Specifications, documentation and ordering." />
<link rel="canonical" href="https://www.vtronix.com/product-page/{slug}" />
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/style.css" />
<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Organization", "name": "Vtronix", "url": "https://www.vtronix.com", "foundingDate": "2001", "logo": "https://www.vtronix.com/assets/img/logo.png", "address": {{"@type": "PostalAddress", "postOfficeBoxNumber": "267096", "addressLocality": "Weston", "addressRegion": "FL", "postalCode": "33326", "addressCountry": "US"}}, "contactPoint": {{"@type": "ContactPoint", "telephone": "+1-305-471-7600", "email": "sales@vtronix.com", "contactType": "sales"}}}}</script>
{item_schema}
</head>
<body class="section-white" style="background:#fff;">

<header class="site-header">
  <div class="wrap">
    <a href="/" class="logo"><img src="/assets/img/logo.png" alt="Vtronix" /></a>
    <nav class="main-nav">
      <a href="/custom-controls">Custom Controls</a>
      <a href="/category/all-products" class="active">Products</a>
      <a href="/applications">Applications</a>
      <a href="/factory">Manufacturing</a>
      <a href="/about">About</a>
      <a href="/documentation">Documentation</a>
      <a class="nav-cta" href="/request-a-quote">Request a Quote</a>
    </nav>
    <button class="nav-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</header>

<main class="section-white">
  <div class="wrap shop-layout" style="padding-top:34px;">

    <aside class="shop-categories">
      <h4>Categories</h4>
      <ul>
{sidebar}
      </ul>
    </aside>

    <div>
      <p class="breadcrumb">
        <a href="/">Home</a><span class="sep">/</span><a href="/category/{cat_query}">All Products</a><span class="sep">/</span><span class="current">{sku}</span>
      </p>

      <div class="product-detail">
        <div class="product-detail-media">
{media}
        </div>

        <div>
          <span class="product-detail-tag">{brand}</span>{status_tag}
          <h1>{sku}</h1>

{honeywell}
{body}

{docs}

{used_in}
{replaced}
          <a class="btn btn-light" href="/request-a-quote"><span>Request a Quote</span><span class="arrow">&rarr;</span></a>
        </div>
      </div>
{related}
    </div>

  </div>
</main>

<footer class="site-footer" style="background:#000; color:#fff;">
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


APPLICATION_BY_SLUG = {
    "r200a": [("Air handler controls", "air-handlers")],
    "r201": [("Air handler controls", "air-handlers")],
    "r85a": [("Air handler controls", "air-handlers")],
    "ahu-control": [("Air handler controls", "air-handlers")],
    "cbx99100": [("Air handler controls", "air-handlers")],
    "r60a": [("Air handler controls", "air-handlers")],
    "tf85l-200": [("Fan coil controls and thermostats", "fan-coil-units")],
    "t5575b-std": [("Fan coil controls and thermostats", "fan-coil-units")],
    "te63m-001": [("Fan coil controls and thermostats", "fan-coil-units")],
    "tf63m-001": [("Fan coil controls and thermostats", "fan-coil-units")],
    "pi02": [("Fan coil controls and thermostats", "fan-coil-units")],
    "pi03-aux": [("Fan coil controls and thermostats", "fan-coil-units")],
    "pi04": [("Fan coil controls and thermostats", "fan-coil-units")],
    "r401": [("Water source heat pump boards", "water-source-heat-pumps")],
    "dt03plus-001": [("Mini split wired and wireless controls", "mini-splits")],
    "dt04-hc-120": [("Mini split wired and wireless controls", "mini-splits")],
    "dt05plus": [("Mini split wired and wireless controls", "mini-splits")],
    "lcdwireii": [("Mini split wired and wireless controls", "mini-splits")],
    "wlth-010": [("Mini split wired and wireless controls", "mini-splits")],
    "kt-828-gold": [("Mini split wired and wireless controls", "mini-splits")],
    "q-338-f": [("Mini split wired and wireless controls", "mini-splits")],
    "cb600v": [("ECM motor control", "ecm-motor-control")],
    "ew40030": [("ECM motor control", "ecm-motor-control")],
    "ew40040": [("ECM motor control", "ecm-motor-control")],
    "r650": [("ECM motor control", "ecm-motor-control")],
    "hesk120v": [("Energy-saving controls for hotels and buildings", "energy-savings")],
    "hesk220v": [("Energy-saving controls for hotels and buildings", "energy-savings")],
    "i-save": [("Energy-saving controls for hotels and buildings", "energy-savings")],
    "zone-control-ii": [("Energy-saving controls for hotels and buildings", "energy-savings")],
}


def build_item_schema(p):
    brand_name = "Honeywell" if p["brand"] == "Honeywell" else "Vtronix"
    product = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": p["sku"],
        "sku": p["sku"],
        "brand": {"@type": "Brand", "name": brand_name},
        "url": "https://www.vtronix.com/product-page/" + p["slug"],
    }
    if p.get("image"):
        product["image"] = "https://www.vtronix.com/assets/img/products/" + p["image"]
    if p.get("description"):
        product["description"] = p["description"]
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.vtronix.com/"},
            {"@type": "ListItem", "position": 2, "name": "All Products", "item": "https://www.vtronix.com/category/" + p["cat_query"]},
            {"@type": "ListItem", "position": 3, "name": p["sku"]},
        ],
    }
    tag = '<script type="application/ld+json">{}</script>'.format(json.dumps(product))
    tag += '\n<script type="application/ld+json">{}</script>'.format(json.dumps(breadcrumb))
    return tag


def build_status_tag(p):
    if p["slug"].endswith("-obsolete"):
        return '<span class="product-detail-tag" style="background:#9a2020; margin-left:8px;">Discontinued</span>'
    return '<span class="product-detail-tag" style="background:#2a7d2a; margin-left:8px;">Active</span>'


def build_honeywell_notice(p):
    if p["brand"] != "Honeywell":
        return ""
    return (
        '        <div style="border:1px solid #ddd; border-radius:3px; padding:14px 16px; margin-bottom:24px; '
        'background:#fafafa; font-size:13.5px; color:#555;">'
        "Honeywell product, supplied by Vtronix. Not a Vtronix design."
        "</div>"
    )


def build_used_in(p):
    apps = APPLICATION_BY_SLUG.get(p["slug"])
    if not apps:
        return ""
    links = "".join(
        '<a href="/applications/{slug}" style="margin-right:16px;">{title} &rarr;</a>'.format(slug=slug, title=title)
        for title, slug in apps
    )
    return '        <p class="section-label">Used in</p>\n        <p style="margin:0 0 28px;">{}</p>'.format(links)


def build_replaced_notice(p):
    if not p["slug"].endswith("-obsolete"):
        return ""
    return (
        '        <div style="border:1px solid #ddd; border-radius:3px; padding:14px 16px; margin-bottom:24px; '
        'background:#fafafa; font-size:14px;">'
        'This item is discontinued. <a href="/request-a-quote">Contact us for a replacement &rarr;</a>'
        "</div>"
    )


def build_related(p):
    same_cat = [
        o for o in PRODUCTS
        if o["cat_query"] == p["cat_query"] and o["slug"] != p["slug"]
    ][:3]
    if not same_cat:
        return ""
    cards = "\n".join(
        '        <a class="featured-card" style="border-color:#ddd; background:#fff;" href="/product-page/{slug}">'
        '<div class="featured-thumb"><img src="/assets/img/products/{image}" alt="{sku} {brand}" loading="lazy" /></div>'
        '<div class="featured-info" style="background:#fff;"><span class="tag" style="color:#4a9bdc;">{brand}</span>'
        '<div class="name" style="color:#111;">{sku}</div></div></a>'.format(
            slug=o["slug"], image=o["image"], sku=o["sku"], brand=o["brand"]
        )
        for o in same_cat
    )
    return (
        '      <div style="margin-top:50px;">\n'
        '        <p class="section-label" style="margin-bottom:16px;">Related products</p>\n'
        '        <div class="featured-grid">\n{}\n        </div>\n'
        "      </div>"
    ).format(cards)


def build_body(p):
    if p["features"]:
        items = "\n".join('          <li>{}</li>'.format(f) for f in p["features"])
        return '        <p class="section-label">Features</p>\n        <ul class="feature-list">\n{}\n        </ul>'.format(items)
    return '        <p class="lead" style="margin-bottom:28px; color:#444;">{}</p>'.format(p["description"] or "")


CATEGORIES = [
    ("control-boards", "Control Boards"),
    ("residential-thermostats", "Thermostats - Residential"),
    ("commercial-thermostats", "Thermostats - Commercial"),
    ("fan-coil-thermostats", "Fan Coil Controls"),
    ("mini-split-controls", "Mini Split Controls"),
    ("energy-savings", "Energy Savings"),
    ("temperature-controls", "Temperature Controls"),
    ("all-products", "All Products"),
    ("discontinued", "Discontinued Items"),
]


def build_sidebar(p):
    rows = []
    for slug, label in CATEGORIES:
        href = "/category/" + slug
        cls = ' class="active"' if slug == p["cat_query"] else ""
        rows.append('        <li><a href="{href}"{cls}>{label}</a></li>'.format(href=href, cls=cls, label=label))
    return "\n".join(rows)


PLACEHOLDER_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="#5b6b78" stroke-width="1.4" '
    'style="width:38%;height:38%;opacity:.55;">'
    '<rect x="4" y="4" width="16" height="16" rx="2"/><circle cx="12" cy="12" r="3.2"/>'
    '<path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/>'
    "</svg>"
)


def build_media(p):
    if p.get("image"):
        return '          <img src="/assets/img/products/{}" alt="{} product photo" loading="lazy" />'.format(
            p["image"], p["sku"]
        )
    return "          " + PLACEHOLDER_ICON


PDF_ICON = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
    '<path d="M14 2v6h6"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/>'
    "</svg>"
)


def build_docs(p):
    if not p["docs"]:
        return ""
    links = "\n".join(
        '          <a href="{href}" target="_blank" rel="noopener">{icon} {label}</a>'.format(icon=PDF_ICON, **d)
        for d in p["docs"]
    )
    return '        <p class="section-label">Documentation</p>\n        <div class="pdf-links">\n{}\n        </div>'.format(links)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for p in PRODUCTS:
        html = TEMPLATE.format(
            sku=p["sku"],
            slug=p["slug"],
            brand=p["brand"],
            cat_query=p["cat_query"],
            body=build_body(p),
            docs=build_docs(p),
            sidebar=build_sidebar(p),
            media=build_media(p),
            item_schema=build_item_schema(p),
            status_tag=build_status_tag(p),
            honeywell=build_honeywell_notice(p),
            used_in=build_used_in(p),
            replaced=build_replaced_notice(p),
            related=build_related(p),
        )
        out_path = os.path.join(OUT_DIR, p["slug"] + ".html")
        with open(out_path, "w") as f:
            f.write(html)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

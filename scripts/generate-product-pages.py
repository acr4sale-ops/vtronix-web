#!/usr/bin/env python3
"""
Generates static product detail pages under products/<slug>.html from PRODUCTS below.
Run from anywhere: python3 scripts/generate-product-pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "products")

PRODUCTS = [
    {
        "sku": "TB7980B1005",
        "slug": "tb7980b1005",
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
            {"label": "Install Instructions", "href": "https://s3.amazonaws.com/s3.supplyhouse.com/product_files/TB7980B1005-Install.pdf"},
            {"label": "Product Overview", "href": "https://s3.amazonaws.com/s3.supplyhouse.com/product_files/TB7980B1005-Product-Overview.pdf"},
        ],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TH6210U2001",
        "slug": "th6210u2001",
        "brand": "Honeywell",
        "image": "TH6210U2001.jpg",
        "features": [],
        "description": "T6 Pro Programmable Thermostat, 2H/1C Heat Pump, 1H/1C Conventional, TH6210U2001",
        "docs": [
            {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_46f28dee08b44caf845642687a5e4907.pdf"},
        ],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "W100",
        "slug": "w100",
        "brand": "Air Conditioning Control",
        "image": "W100.jpg",
        "features": [],
        "description": "W100 Chiller Controller.",
        "docs": [
            {"label": "Manual", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/6a435f_5e8d6f28e33441d3bb98138c82e58ed6.pdf"},
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
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_12678dadbd4c4aaab96511ac8bae5fbc.pdf"},
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
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_ba7485888fd04e2babdea2e907075664.pdf"},
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
            {"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_9378fa9dc0004dee904f05fdcae67611.pdf"},
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
            {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_dd10112d23ee49a2a286350a704b21d6.pdf"},
            {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_2d56eb49591547b6a0dd52b3a4939243.pdf"},
        ],
        "cat_query": "fan-coil-controls",
    },
    # --- Remaining 91 products, scraped from live vtronix.com product pages ---
    {
        "sku": "TH4110U2005",
        "slug": "th4110u2005",
        "brand": "Honeywell",
        "image": "TH4110U2005.jpg",
        "features": [],
        "description": "T4 Pro Programmable Thermostat, 1H/1C Heat Pump, 1H/1C Conventional, TH4110U2005.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_bdd56732ca7e407f8764618b56deeeaf.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH1110DV1009",
        "slug": "th1110dv1009",
        "brand": "Honeywell",
        "image": "TH1110DV1009.jpg",
        "features": [],
        "description": "Vertical PRO 1000 Non-Programmable Thermostat \u2013 Backlit, 1H/1C, Dual Powered.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_305db0a33dca4770927b427274a040c5.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d048d1695de84961bc1b1c12adc3e154.pdf"}, {"label": "User Guide", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_0da6772d0e9143678c99fb21b1b8feea.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH1110DH1003",
        "slug": "th1110dh1003",
        "brand": "Honeywell",
        "image": "TH1110DH1003.jpg",
        "features": [],
        "description": "Horizontal PRO 1000 Non-Programmable Thermostat - Backlit, 1H/1C, Dual Powered.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_caef5d125da949ca80732d66af8b4329.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f5b6466daff04d709b86c66b698d7a40.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6e905bb94f3b4b18ab782caae1e0b026.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH5110D1022",
        "slug": "th5110d1022",
        "brand": "Honeywell",
        "image": "TH5110D1022.jpg",
        "features": [],
        "description": "TH5110D1022 Honeywell Digital Thermostat.",
        "docs": [{"label": "User Guide", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_e5960db5effa41fe95c4cc388e562936.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_a5a6adb7f5334beeacab17bacc735a63.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_937675afc5614579bab518dacd3d5fd0.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH6220D1028",
        "slug": "th6220d1028",
        "brand": "Honeywell",
        "image": "TH6220D1028.jpg",
        "features": [],
        "description": "TH6220D1028 Honeywell Focuspro Programmable Thermostat.",
        "docs": [{"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_07a0e78ae2bb44008aa4ebd972dd34b6.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_70139746b50244f19bfc82618b5a5a25.pdf"}, {"label": "User Guide", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_e32d83b2a6e54b1fbbc803caf5333869.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH8110R1008",
        "slug": "th8110r1008",
        "brand": "Honeywell",
        "image": "TH8110R1008.jpg",
        "features": [],
        "description": "TH8110R1008 Honeywell VisionPRO 8000 with RedLINK technology, Programmable, 1H/1C, Touchscreen Thermostat.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d11c2005db394d538dd55044f866d197.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_af3057f0acb04e1f8a7f6b3aa1ac74ab.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_af00460104784c9d93bda2fc2110a99d.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH8320R1003",
        "slug": "th8320r1003",
        "brand": "Honeywell",
        "image": "TH8320R1003.jpg",
        "features": [],
        "description": "TH8320R1003 Honeywell VisionPRO 8000 with RedLINK Technology. Stages up to 3 Heat / 2 Cool.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f546b9feaf2c47d2a55e7dcb0261e600.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_402b686973844969a9faef5a83b6f121.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_e3864b24a2234198af25965569e93eeb.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH9320WF5003",
        "slug": "th9320wf5003",
        "brand": "Honeywell",
        "image": "TH9320WF5003.jpg",
        "features": [],
        "description": "TH9320WF5003 Honeywell Wi-Fi 9000 color touch screen programmable thermostat (needs \"C\" wire).",
        "docs": [{"label": "User Guide", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_1e318f5e4b8a4edba49ca985b0a4db5a.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_32e8e17d8348404da31f7f514a73d2d8.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_4f9552ec46a44e0eaa50f352dc62b3bc.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "TH8321WF1001",
        "slug": "th8321wf1001",
        "brand": "Honeywell",
        "image": "TH8321WF1001.jpg",
        "features": [],
        "description": "TH8321WF1001 Honeywell Wi-Fi VisionPRO 8000 Programmable, 3H/2C, Touchscreen Thermostat (Needs \"C\" wire).",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c4e34484bba044bdac6753faeae4e238.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c7704f0df32e46f9b20c0e9178658336.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d1e51de5bef84635b57df0f06229287d.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "THP9045A1023",
        "slug": "thp9045a1023",
        "brand": "Honeywell",
        "image": "THP9045A1023.jpg",
        "features": [],
        "description": "THP9045A1023/U Honeywell Wiresaver Wiring Module for Wi-Fi and Prestige Thermostats.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c580e7d02afe4588a0a383f0aa2d9419.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "THP2400A1068",
        "slug": "thp2400a1068",
        "brand": "Honeywell",
        "image": "THP2400A1068.jpg",
        "features": [],
        "description": "THP2400A1068 Honeywell 6\" x 6\" White Coverplate for T Series Thermostats.",
        "docs": [],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "THP2400A1027W",
        "slug": "thp2400a1027w",
        "brand": "Honeywell",
        "image": "THP2400A1027W.jpg",
        "features": [],
        "description": "THP2400A1027W Honeywell Cover Plate for TH9320WF5003.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6ed677a825bf43d18f51cbda1453f1eb.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "T6811DP08",
        "slug": "t6811dp08",
        "brand": "Honeywell",
        "image": "T6811DP08.jpg",
        "features": [],
        "description": "T6811DP08 Honeywell LCD Thermostat 120 VAC - 2 pipe Fancoil Control.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_5592f4c386d6421f9af640938a6924cf.pdf"}],
        "cat_query": "thermostats-residential",
    },
    {
        "sku": "T775A2009",
        "slug": "t775a2009",
        "brand": "Honeywell",
        "image": "T775A2009.png",
        "features": [],
        "description": "Electronic Temperature Controller with 1 Temperature Input, 1 SPDT Relay, 1 Sensor Included.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_85018cfe90bd4309b2350401c3a0105a.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "T6373B1148",
        "slug": "t6373b1148",
        "brand": "Honeywell",
        "image": "T6373B1148.png",
        "features": [],
        "description": None,
        "docs": [],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TC300B-G",
        "slug": "tc300b-g",
        "brand": "Honeywell",
        "image": "TC300B-G.png",
        "features": [],
        "description": "TC300 Commercial Thermostat.",
        "docs": [],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TC500A-N",
        "slug": "tc500a-n",
        "brand": "Honeywell",
        "image": "TC500A-N.jpg",
        "features": [],
        "description": "Commercial Connected Touchscreen Wireless Thermostat - 5H/3C Heat Pump, 3H/3C Conventional.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_e19d0e137ed241b494907f29790c575e.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_76c513def033475bb2cfcf5f398ce1e6.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TB7980A1006",
        "slug": "tb7980a1006",
        "brand": "Honeywell",
        "image": "TB7980A1006.jpg",
        "features": [],
        "description": "TB7980A1006 Honeywell Zonepro Modulating Thermostat with 0-10 Vdc Control.",
        "docs": [],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TB6980A1007",
        "slug": "tb6980a1007",
        "brand": "Honeywell",
        "image": "TB6980A1007.jpg",
        "features": [],
        "description": "TB6980A1007 Honeywell Zonepro Floating Control Thermostat, Single Output.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_cf11289c01d942d59901d4ddb4db3727.pdf"}, {"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d8aae609d1e34f92bcc72b912f832900.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TB8575A1000",
        "slug": "tb8575a1000",
        "brand": "Honeywell",
        "image": "TB8575A1000.jpg",
        "features": [],
        "description": "TB8575A1000 Honeywell SuitePRO - 24 Vac, 2 or 4 Pipe 3-Speed Fan Coil T-Stat with Manual/Auto Heat or Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_a49373f5e37c4d1ebdb04fbcf9d9ed05.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_b987b1d09ca04e59bbcf9445546ba34a.pdf"}, {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_4dea70c9c0a14cfe95e2c738dc152b49.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TB6575B1000",
        "slug": "tb6575b1000",
        "brand": "Honeywell",
        "image": "TB6575B1000.jpg",
        "features": [],
        "description": "TB6575B1000 Honeywell SuitePRO- 120/240V, 3-Speed Fan Coil T-Stat with 2 or 4 Pipe Manual/Auto Heat/Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_780aeae953974171a93070ab0df48198.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c3e6fd85a8fa4c35a0607e630a738495.pdf"}, {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_b22c7baa3bd74954adc7aa91747debdb.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "TB6575A1000",
        "slug": "tb6575a1000",
        "brand": "Honeywell",
        "image": "TB6575A1000.jpg",
        "features": [],
        "description": "TB6575A1000 Honeywell SuitePRO- 120/240V, 3-Speed Fan Coil T-Stat with 2 or 4 Pipe Manual/Auto Heat/Cool Changeover.",
        "docs": [{"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_ab6ad30e376e436982851560cdbb67c4.pdf"}, {"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_11070c5d85604eca876716f6a4daa0b0.pdf"}, {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_0d923ae546b444c396861b18810d902b.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "32003796-001",
        "slug": "32003796-001",
        "brand": "Honeywell",
        "image": "32003796-001.png",
        "features": [],
        "description": "Honeywell WallPlate Cover for all TH8000 series thermostats. Use With TH8000 VisionPRO\u00ae Series Thermostats. Item Type: Accessory. Color: Premier White. Wallplate: 7 7/8\" wide X 5 1/2\" tall.",
        "docs": [{"label": "Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_25bab64af19c41a3985cf6c09622eb53.pdf"}],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "50033847-001",
        "slug": "50033847-001",
        "brand": "Honeywell",
        "image": "50033847-001.png",
        "features": [],
        "description": "Honeywell Adapter Plate. Used With: TB6575/TB8575 series fan coil thermostats to vertical, single or double-gang junction box.",
        "docs": [],
        "cat_query": "thermostats-commercial",
    },
    {
        "sku": "VCZAL1100",
        "slug": "vczal1100",
        "brand": "Honeywell",
        "image": "VCZAL1100.jpg",
        "features": [],
        "description": "3/4\" Female NPT VC Valve Assembly (4.7 Cv).",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_ae727fd749ab4a02a333d0ddb6c2bdd7.pdf"}, {"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_543ec3b482b34049917c33d489dc5f46.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "VC4013ZZ00",
        "slug": "vc4013zz00",
        "brand": "Honeywell",
        "image": "VC4013ZZ00.jpg",
        "features": [],
        "description": "Two Position, Valve Actuator, 6VA, 200-240 VAC, 50/60 HZ.",
        "docs": [],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "VC8011ZZ00",
        "slug": "vc8011zz00",
        "brand": "Honeywell",
        "image": "VC8011ZZ00.jpg",
        "features": [],
        "description": "Two Position Low Volt Actuator for VC Series Valves, 24 VAC, 6 VA, 60 psi.",
        "docs": [{"label": "Submittal Sheet", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f3d7f75e9c21478bae6bf0983d2f33fd.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "V8043E1145",
        "slug": "v8043e1145",
        "brand": "Honeywell",
        "image": "V8043E1145.png",
        "features": [],
        "description": "3/4\" NPT Connection Zone Valve, normally closed, 3.5Cv (24v).",
        "docs": [{"label": "Product Overview", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f67d67cd827e44b793d64811e52fd2f7.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_fefbf6cc6529470d95c04943f0341f1c.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "VU52S2028",
        "slug": "vu52s2028",
        "brand": "Honeywell",
        "image": "VU52S2028.jpg",
        "features": [],
        "description": "Two-way Fan Coil Valve, 1/2 in. Sweat, 3.5 Cv.",
        "docs": [{"label": "Flow Rate Chart", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f5d0562203194641bd40ccaceb9c2cc5.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d799c2180fe549838307c25b99a060a6.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "VU444A1007",
        "slug": "vu444a1007",
        "brand": "Honeywell",
        "image": "VU444A1007.jpg",
        "features": [],
        "description": "Two-Position Actuator for VU52 N.O. and VU54 Valve Bodies, 120V 60Hz.",
        "docs": [{"label": "Brochure", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_078773f28456442cb22cc08d50e6081c.pdf"}, {"label": "Install Instructions", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_bc22ddd683444aed9cf68396bfc92444.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TF63M-002",
        "slug": "tf63m-002",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TF63M-002.jpg",
        "features": [],
        "description": "TF63M Electronic Fan-Coil Thermostat, Cool Only, Horizontal - 3 Speed Fan control - Status Light - 220 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_d60781262d334e7f997b2492d75c3d83.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TF63M-001",
        "slug": "tf63m-001",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TF63M-001.jpg",
        "features": [],
        "description": "TF63M Electronic Fan-Coil Thermostat, Cool Only, Horizontal - 3 Speed Fan control - Status Light - 120 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_da0745767a5248be9183034ec5c10227.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TE63M-002",
        "slug": "te63m-002",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TE63M-002.jpg",
        "features": [],
        "description": "TE63M Electronic Fan-Coil Thermostat, Cool Only, Vertical - 3 Speed Fan control- Status Light - 220 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_80f34a9445e84d4ca9a6c38fc28a88ff.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TE63M-001",
        "slug": "te63m-001",
        "brand": "Electronic - 3 Speed Fan",
        "image": "TE63M-001.jpg",
        "features": [],
        "description": "TE63M Electronic Fan-Coil Thermostat, Cool Only, Vertical - 3 Speed Fan control - Status Light - 120 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_da0745767a5248be9183034ec5c10227.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TF65L-001",
        "slug": "tf65l-001",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-001.jpg",
        "features": [],
        "description": "TF65L Digital Fan-coil Thermostat, Cool Only, Horizontal, No Time Delay, Deg C - 120 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c3b26405568f43d3aba071fba02eac8d.pdf"}],
        "cat_query": "fan-coil-controls",
        "discontinued": True,
    },
    {
        "sku": "TF85L-11011",
        "slug": "tf85l-11011",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-11011.jpg",
        "features": [],
        "description": "T201 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_3678daf7e0b940e6afe9f28a9a88c84b.pdf"}],
        "cat_query": "fan-coil-controls",
        "discontinued": True,
    },
    {
        "sku": "TF85L-10011",
        "slug": "tf85l-10011",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-10011.jpg",
        "features": [],
        "description": "T200 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_b0bbe3fcc68a4b1aadcebc863e755edf.pdf"}],
        "cat_query": "fan-coil-controls",
        "discontinued": True,
    },
    {
        "sku": "TF65L-002-SWP",
        "slug": "tf65l-002-swp",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-002-SWP.jpg",
        "features": [],
        "description": "TF65L Digital Fan-coil Thermostat, Cool Only/Sweep, Horizontal, 3 Minute Delay, Deg C - 200 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_de642e2753564cc2929bb21b9cb238d9.pdf"}],
        "cat_query": "fan-coil-controls",
        "discontinued": True,
    },
    {
        "sku": "TF65L-002-STD",
        "slug": "tf65l-002-std",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF65L-002-STD.webp",
        "features": [],
        "description": "TF65L Digital Fan-Coil Thermostat, Cool Only, Horizontal, 3 Minute Delay, Deg C - 220 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_de642e2753564cc2929bb21b9cb238d9.pdf"}],
        "cat_query": "fan-coil-controls",
        "discontinued": True,
    },
    {
        "sku": "T5575B-STD",
        "slug": "t5575b-std",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "T5575B-STD.jpg",
        "features": [],
        "description": "T5575B Digital Fancoil Thermostat, Backlit LCD, Heat/Cool, Heat Valve, No Time Delay, Deg C/F, 120-240 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f2d4f7c8b79a44b8826bb2be5d366212.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TF85L-201",
        "slug": "tf85l-201",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-201.jpg",
        "features": [],
        "description": "T201 Digital Fan-Coil Thermostat, Heat/Cool, Auto Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_38e1c9e7fc584e0d83566499bcd22aa3.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "TF85L-200",
        "slug": "tf85l-200",
        "brand": "Digital - 3 Speed Fan, On/Off",
        "image": "TF85L-200.jpg",
        "features": [],
        "description": "T200 Digital Fan-Coil Thermostat, Heat/Cool, Manual Changeover, Horizontal, No Time Delay, Deg F - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_fa431215c6c64bc5bce1c66e00332414.pdf"}],
        "cat_query": "fan-coil-controls",
    },
    {
        "sku": "ECONO3-001",
        "slug": "econo3-001",
        "brand": "Mini-Split Control Wired",
        "image": "ECONO3-001.jpg",
        "features": [],
        "description": "XE8100A. Wired Control for mini-splits, Cool Only, with sweep.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6814a83e38f94045bb6b116574c1a1d6.pdf"}],
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
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_72d787493e3a476fa45258d999661e54.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT04-HC-120",
        "slug": "dt04-hc-120",
        "brand": "Mini-Split Control Wired",
        "image": "DT04-HC-120.jpg",
        "features": [],
        "description": "DT04-HC-120.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_65b4635d7edd4080b09f0a6ee0db04ee.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT04PLUS-001",
        "slug": "dt04plus-001",
        "brand": "Mini-Split Control Wired",
        "image": "DT04PLUS-001.jpg",
        "features": [],
        "description": "Wired Control for mini-splits, LED Display, Cool Only, with sweep. Remote Optional.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_eef6a3b3670542deb6f6fb542dbad1c3.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT05PLUS",
        "slug": "dt05plus",
        "brand": "Mini-Split Control Wired",
        "image": "DT05PLUS.jpg",
        "features": [],
        "description": "DT05PLUS Fan Coil Control. LED Display, Cool Only, with sweep. Remote Optional.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_da00b0e94110481eb0ffc21777b172b6.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "DT05HW",
        "slug": "dt05hw",
        "brand": "Mini-Split Control Wired",
        "image": "DT05HW.jpg",
        "features": [],
        "description": "DT05HW Temperature & Dehumidification Control.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_b73bef5a754c43c6aa1c88f21d1c404d.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "LCDWIREII",
        "slug": "lcdwireii",
        "brand": "Mini-Split Control Wired",
        "image": "LCDWIREII.jpg",
        "features": [],
        "description": "LCDWIREII Fan Coil Control with backlit LCD display. Remote Optional.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_71e18e7b04874ca3a8e7eb66826e7c30.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "WLTH-020",
        "slug": "wlth-020",
        "brand": "Mini-Split Control Wired",
        "image": "WLTH-020.jpg",
        "features": [],
        "description": "Fan Coil Control, flush mount, LED, Cool only, with window sensor. 220 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_eba19691da1f4acd8ca2d87fb0664250.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "WLTH-010",
        "slug": "wlth-010",
        "brand": "Mini-Split Control Wired",
        "image": "WLTH-010.jpg",
        "features": [],
        "description": "Fan Coil Control, flush mount, LED, Cool only, with window sensor. 120 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_35321256469040f3965c75b74139c899.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-828 Gold",
        "slug": "kt-828-gold",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-828-Gold.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 2000 codes. Large Display. Deg C or F.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_9794f3a4fde9413d8ee0796800d22bcd.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-S828 Silver",
        "slug": "kt-s828-silver",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-S828-Silver.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 2000 codes. Large Display. Deg C or F.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_9794f3a4fde9413d8ee0796800d22bcd.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-E03",
        "slug": "kt-e03",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-E03.jpg",
        "features": [],
        "description": "Mini Split Universal Remote. 4000 codes. Large Display. One KEY.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_92d41b7611dc444a8a545ae82ccf7dff.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "KT-E08",
        "slug": "kt-e08",
        "brand": "Mini-Split Control Wireless",
        "image": "KT-E08.jpg",
        "features": [],
        "description": "KT-E08 Mini Split Universal Remote. 6000 codes. LCD Display.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_a1cde4cc0233475782b41b2b52b131d9.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "Q-338-F",
        "slug": "q-338-f",
        "brand": "Mini-Split Control Wireless",
        "image": "Q-338-F.jpg",
        "features": [],
        "description": "Mini Split Universal Remote Control. Deg F.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_aca9bdd7e3b64e7087e3105f4251b5ac.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "Q-380EW",
        "slug": "q-380ew",
        "brand": "Mini-Split Control Wireless",
        "image": "Q-380EW.jpg",
        "features": [],
        "description": "Mini Split Universal Remote Control. Deg C or F.",
        "docs": [{"label": "Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_8e5e348020af4210ac8501006d8a69b3.pdf"}, {"label": "Quick Start Guide", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6291a85ac6724975b5c86b3df584efe7.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "XE8400A",
        "slug": "xe8400a",
        "brand": "Mini-Split Control Wireless",
        "image": "XE8400A.jpg",
        "features": [],
        "description": "LCD5004-030. Wireless LCD Control for mini-splits. Remote LCD 5.2 cool only + Sweep. Small board.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_32a00c46a4c140128f174715b7b169aa.pdf"}],
        "cat_query": "mini-split-controls",
    },
    {
        "sku": "i-save1002",
        "slug": "i-save1002",
        "brand": "Energy Savings",
        "image": "i-save1002.jpg",
        "features": [],
        "description": "i-save1002 Hotel Room Energy Savings Key Card System - 220VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_298a49562acd498a9d945ba410e64f44.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "i-save1001",
        "slug": "i-save1001",
        "brand": "Energy Savings",
        "image": "i-save1001.jpg",
        "features": [],
        "description": "i-save1001 Hotel Room Energy Savings Key Card System - 120VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_492a309bfd25456ab05220cd789bea83.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "HESK220V",
        "slug": "hesk220v",
        "brand": "Energy Savings",
        "image": "HESK220V.jpg",
        "features": [],
        "description": "HESK220V Energy Savings Kit with main board and 2 door switches 520025-000, 220 VAC, 50/60 Hz.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_01e2f396aa9f4f26bb792af71ad2da7c.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "HESK120V",
        "slug": "hesk120v",
        "brand": "Energy Savings",
        "image": "HESK120V.jpg",
        "features": [],
        "description": "HESK120V Energy Savings Kit with main board and 2 door switches 520025-000, 120 VAC, 50/60 Hz.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f3af1ce2158b453b9756d34f80b756f9.pdf"}],
        "cat_query": "energy-savings",
    },
    {
        "sku": "Zone Control II",
        "slug": "zone-control-ii",
        "brand": "Temperature Controls",
        "image": "Zone-Control-II.jpg",
        "features": [],
        "description": "Zone Control II. Control up to 4 dampers.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_56fc9d2d17cc49a5a33bdcdbf4f0e568.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "MSI",
        "slug": "msi",
        "brand": "Temperature Controls",
        "image": "MSI.jpg",
        "features": [],
        "description": "MSI Master Slave network control of up to 64 A/C units.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_87f2981094714f1096f33cfebdd69536.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "Outdoor Control",
        "slug": "outdoor-control",
        "brand": "Temperature Controls",
        "image": "Outdoor-Control.jpg",
        "features": [],
        "description": "Outdoor Control for compressor.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_93321e5536314350bf4db872f1621e7d.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "AHU Control",
        "slug": "ahu-control",
        "brand": "Temperature Controls",
        "image": "AHU-Control.jpg",
        "features": [],
        "description": "AHU Control. Phase monitoring & star-delta motor starter.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_61cf3a2197364e75a6513b1d33deb385.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "FT101",
        "slug": "ft101",
        "brand": "Temperature Controls",
        "image": "FT101.jpg",
        "features": [],
        "description": "FT101 Freezer Thermostat with fan, defrost & compressor control.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_68cffefd7cee4ec2b82e09eb7095a05a.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "TC102",
        "slug": "tc102",
        "brand": "Temperature Controls",
        "image": "TC102.jpg",
        "features": [],
        "description": "TC102 Storage Tank Controller with input for Heat/Cool. 2 Stage outputs.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_8ef14456423b4d029124f08ed591d6f9.pdf"}],
        "cat_query": "temperature-controls",
    },
    {
        "sku": "RAB-A24.11BE3",
        "slug": "rab-a24.11be3",
        "brand": "Air Conditioning Control",
        "image": "RAB-A24.11BE3.jpg",
        "features": [],
        "description": "Magnetic Starter, 220V.",
        "docs": [{"label": "Manual", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/87c6fa_5271857e0e82442ca48071b97e9fd94f.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R100A",
        "slug": "r100a",
        "brand": "Air Conditioning Control",
        "image": "R100A.png",
        "features": [],
        "description": "R100A A/C Control Board. HP & LP switch inputs.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_33e5e75228bd47acabd16d458571cb2b.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60BLEADS",
        "slug": "r60bleads",
        "brand": "Fan Delay",
        "image": "R60BLEADS.jpg",
        "features": [],
        "description": "Wire Harness.",
        "docs": [{"label": "Specifications", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_38437165c956497380dbc4d7fa7daa1e.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60B-45/S2-R60BLEADS",
        "slug": "r60b-45-s2-r60bleads",
        "brand": "Fan Delay",
        "image": "R60B-45-S2-R60BLEADS.jpg",
        "features": [],
        "description": "R60B Fan Delay Board. 1s ON delay, 45s OFF delay. 2.5\" x 2.5\". Fan Delay Board + Wire Harness.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_0decb433b6ef459b859032d971bee89a.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60B-45/S2",
        "slug": "r60b-45-s2",
        "brand": "Fan Delay",
        "image": "R60B-45-S2.jpg",
        "features": [],
        "description": "R60B Fan Delay Board. 1s ON delay, 45s OFF delay. 2.5\" x 2.5\".",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_0decb433b6ef459b859032d971bee89a.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R60A",
        "slug": "r60a",
        "brand": "Fan Delay",
        "image": "R60A.jpg",
        "features": [],
        "description": "R60A Fan Delay Board. 30s ON delay, 30s OFF delay. 2.5\" x 3\".",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_dc8159ded056410fb548b900af9331c0.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "CBX99100",
        "slug": "cbx99100",
        "brand": "Fan Delay",
        "image": "CBX99100.png",
        "features": [],
        "description": "Fan Delay Board.",
        "docs": [{"label": "Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_de691f492892421a9476a604d7912b9b.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "CBX02003",
        "slug": "cbx02003",
        "brand": "Fan Delay",
        "image": "CBX02003.jpg",
        "features": [],
        "description": "Fan Blower Post Purge Time Delay - 65 seconds.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_c2de4540d0524dc9975cf228f409c3f0.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R201",
        "slug": "r201",
        "brand": "AHU Control",
        "image": "R201.png",
        "features": [],
        "description": "AHU Control Board Two Speed.",
        "docs": [{"label": "Manual", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/87c6fa_177a9418877144d9a1f583a06d4d777c.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R200A/S3",
        "slug": "r200a-s3",
        "brand": "AHU Control",
        "image": "R200A-S3.jpg",
        "features": [],
        "description": "R200A Control Board for hot water/electric heat AHU.",
        "docs": [{"label": "Download File", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/87c6fa_3c6e3c413d044101aa4c773b069dc9b8.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R85A-001",
        "slug": "r85a-001",
        "brand": "AHU Control",
        "image": "R85A-001.jpg",
        "features": [],
        "description": "R85A-001 UL Approved 3 speed fan board. 24V input, 120-277V, 11A fan control.",
        "docs": [{"label": "Download File", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/87c6fa_52d5e0762f494cbea6ad95448426cbf0.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R502",
        "slug": "r502",
        "brand": "Heater Timing Board",
        "image": "R502.png",
        "features": [],
        "description": "Heater Timing Board.",
        "docs": [{"label": "Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6f45322778fc467ab466c0e8f185f2b2.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R401",
        "slug": "r401",
        "brand": "Water Source HP Board",
        "image": "R401.png",
        "features": [],
        "description": "Water Source HP Boards.",
        "docs": [{"label": "Manual", "href": "https://87c6fa8c-9fd7-4729-b266-02f0e07e2b4a.usrfiles.com/ugd/87c6fa_1178729f2f9a47edab63676a8ce9a3a2.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI02",
        "slug": "pi02",
        "brand": "Floating",
        "image": "PI02.png",
        "features": [],
        "description": "Digital Low Voltage Floating Thermostat, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_bc169865e5134dcb89d1ec52d5d410f8.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI03-AUX",
        "slug": "pi03-aux",
        "brand": "Modulating",
        "image": "PI03-AUX.png",
        "features": [],
        "description": "Digital Low Voltage Floating Thermostat, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_bc169865e5134dcb89d1ec52d5d410f8.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "PI04",
        "slug": "pi04",
        "brand": "Modulating",
        "image": "PI04.png",
        "features": [],
        "description": "Digital Low Voltage Modulating Thermostat, 0-10V or 2-10V, Vertical, Internal & Remote Sensor.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_5fac02c77e414775b265f8c9721a042e.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "LAKEPRO-1",
        "slug": "lakepro-1",
        "brand": "Vtronix",
        "image": "LAKEPRO-1.png",
        "features": [],
        "description": "Wifi Enabled, Programmable Thermostat. (Requires a C Wire)",
        "docs": [{"label": "English Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6f1d472f00b14ce38af11f026fad537d.pdf"}, {"label": "Spanish Manual", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_dfd5b64225084dc6b5add4f42169fd72.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "TE86SB-501",
        "slug": "te86sb-501",
        "brand": "Vtronix",
        "image": "TE86SB-501.jpg",
        "features": [],
        "description": "TE86 Non Programmable, Vertical, Heat/Cool, Power Stealing - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_6330c8ecdc484ffc8365e771b3d6da97.pdf"}],
        "cat_query": "control-boards",
        "discontinued": True,
    },
    {
        "sku": "TE80SB-501",
        "slug": "te80sb-501",
        "brand": "Vtronix",
        "image": "TE80SB-501.jpg",
        "features": [],
        "description": "Programmable 7 day, Vertical, Heat/Cool, Power Stealing - 24 VAC.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_7a6ff822c472443f8872946fdb8ebec6.pdf"}],
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
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_3d7906d836654c1ca24121a6f9d33125.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "R650",
        "slug": "r650",
        "brand": "ECM Motor Control",
        "image": "R650.jpg",
        "features": [],
        "description": "ECM motor flyer.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_f5255e379d564e59a0d786f5fce05299.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "EW40030",
        "slug": "ew40030",
        "brand": "ECM Motor Control",
        "image": "EW40030.jpg",
        "features": [],
        "description": "EW40030 Wire Kit for ECM motor. 30 inch line volt cable.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_447a84d2d6dd41158f8065d278249156.pdf"}],
        "cat_query": "control-boards",
    },
    {
        "sku": "EW40040",
        "slug": "ew40040",
        "brand": "ECM Motor Control",
        "image": "EW40040.jpg",
        "features": [],
        "description": "EW40040 Wire Kit for ECM motor. 40 inch line volt cable.",
        "docs": [{"label": "Download", "href": "https://6a435fb3-c576-4667-9b8d-e7b49b78ed75.usrfiles.com/ugd/6a435f_447a84d2d6dd41158f8065d278249156.pdf"}],
        "cat_query": "control-boards",
    },
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{sku} | Vtronix</title>
<link rel="icon" type="image/svg+xml" href="../assets/img/favicon.svg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/css/style.css" />
</head>
<body class="section-white" style="background:#fff;">

<header class="site-header">
  <div class="wrap">
    <a href="../index.html" class="logo"><img src="../assets/img/logo.png" alt="Vtronix" /></a>
    <nav class="main-nav">
      <a href="../index.html">Home</a>
      <a href="../factory.html">Factory</a>
      <a href="../about.html">About Us</a>
      <a href="../products.html" class="active">Products</a>
      <a href="../links.html">Links</a>
      <a href="../contact.html">Contact Us</a>
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
        <a href="../index.html">Home</a><span class="sep">/</span><a href="../products.html?cat={cat_query}">All Products</a><span class="sep">/</span><span class="current">{sku}</span>
      </p>

      <div class="product-detail">
        <div class="product-detail-media">
{media}
        </div>

        <div>
          <span class="product-detail-tag">{brand}</span>
          <h1>{sku}</h1>

{body}

{docs}

          <a class="btn btn-light" href="../contact.html"><span>Request a Quote</span><span class="arrow">&rarr;</span></a>
        </div>
      </div>
    </div>

  </div>
</main>

<footer class="site-footer" style="background:#000; color:#fff;">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand">VTRONIX<span class="reg">&reg;</span></div>
      <p>PO Box 267096,<br />Weston FL 33326</p>
      <p><a href="mailto:sales@vtronix.com">sales@vtronix.com</a></p>
      <p><a href="tel:3054717600">305-471-7600</a></p>
    </div>
    <div>
      <h4>General</h4>
      <a href="../about.html">About</a>
      <a href="../factory.html">Factory</a>
      <a href="../links.html">Links</a>
      <a href="../contact.html">Contact Us</a>
    </div>
    <div>
      <h4>Products</h4>
      <a href="../products.html?cat=control-boards">Control Boards</a>
      <a href="../products.html?cat=thermostats-residential">Residential Thermostats</a>
      <a href="../products.html?cat=thermostats-commercial">Commercial Thermostats</a>
      <a href="../products.html?cat=fan-coil-controls">Fan Coil Thermostats</a>
    </div>
    <div>
      <h4>&nbsp;</h4>
      <a href="../products.html?cat=mini-split-controls">Mini Split Controls</a>
      <a href="../products.html?cat=energy-savings">Energy Savings</a>
      <a href="../products.html?cat=temperature-controls">Temperature Controls</a>
      <a href="../products.html">All Products</a>
    </div>
  </div>
</footer>

<script src="../assets/js/main.js"></script>
</body>
</html>
"""


def build_body(p):
    if p["features"]:
        items = "\n".join('          <li>{}</li>'.format(f) for f in p["features"])
        return '        <p class="section-label">Features</p>\n        <ul class="feature-list">\n{}\n        </ul>'.format(items)
    return '        <p class="lead" style="margin-bottom:28px; color:#444;">{}</p>'.format(p["description"] or "")


CATEGORIES = [
    ("control-boards", "Control Boards"),
    ("thermostats-residential", "Thermostats - Residential"),
    ("thermostats-commercial", "Thermostats - Commercial"),
    ("fan-coil-controls", "Fan Coil Controls"),
    ("mini-split-controls", "Mini Split Controls"),
    ("energy-savings", "Energy Savings"),
    ("temperature-controls", "Temperature Controls"),
    ("all-products", "All Products"),
    ("discontinued-items", "Discontinued Items"),
]


def build_sidebar(p):
    rows = []
    for slug, label in CATEGORIES:
        href = "../products.html" if slug == "all-products" else "../products.html?cat=" + slug
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
        return '          <img src="../assets/img/products/{}" alt="{} product photo" loading="lazy" />'.format(
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
            brand=p["brand"],
            cat_query=p["cat_query"],
            body=build_body(p),
            docs=build_docs(p),
            sidebar=build_sidebar(p),
            media=build_media(p),
        )
        out_path = os.path.join(OUT_DIR, p["slug"] + ".html")
        with open(out_path, "w") as f:
            f.write(html)
        print("wrote", out_path)


if __name__ == "__main__":
    main()

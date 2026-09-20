/* Vtronix product catalog — SKU + brand data, captured from the live site.
   Category membership and per-category display order live in
   VTRONIX_CATEGORY_ORDER below: Wix products can belong to more than one
   category, and the same product can sit in a different relative position
   in each category's listing, so a single shared "category" field can't
   reproduce it — each category needs its own explicit order. */

var VTRONIX_PRODUCTS = [
  { sku: "TB7980B1005", brand: "Honeywell" },
  { sku: "32003796-001", brand: "Honeywell" },
  { sku: "50033847-001", brand: "Honeywell" },
  { sku: "TH6210U2001", brand: "Honeywell" },
  { sku: "TH4110U2005", brand: "Honeywell" },
  { sku: "T775A2009", brand: "Honeywell" },
  { sku: "T6373B1148", brand: "Honeywell" },
  { sku: "RAB-A24.11BE3", brand: "Air Conditioning Control" },
  { sku: "R60BLEADS", brand: "Fan Delay" },
  { sku: "R60B-45/S2-R60BLEADS", brand: "Fan Delay" },
  { sku: "R60B-45/S2", brand: "Fan Delay" },
  { sku: "R201", brand: "AHU Control" },
  { sku: "CBX99100", brand: "Fan Delay" },
  { sku: "R502", brand: "Heater Timing Board" },
  { sku: "R401", brand: "Water Source HP Board" },
  { sku: "W100", brand: "Air Conditioning Control" },
  { sku: "Zone Control II", brand: "Temperature Controls" },
  { sku: "MSI", brand: "Temperature Controls" },
  { sku: "Outdoor Control", brand: "Temperature Controls" },
  { sku: "AHU Control", brand: "Temperature Controls" },
  { sku: "W110", brand: "Temperature Controls" },
  { sku: "FT101", brand: "Temperature Controls" },
  { sku: "TC102", brand: "Temperature Controls" },
  { sku: "i-Save", brand: "Energy Savings" },
  { sku: "i-save1002", brand: "Energy Savings" },
  { sku: "i-save1001", brand: "Energy Savings" },
  { sku: "HESK220V", brand: "Energy Savings" },
  { sku: "HESK120V", brand: "Energy Savings" },
  { sku: "ECONO3-001", brand: "Mini-Split Control Wired", discontinued: true },
  { sku: "DT03PLUS-001", brand: "Mini-Split Control Wired" },
  { sku: "DT04-HC-220", brand: "Mini-Split Control Wired" },
  { sku: "DT04-HC-120", brand: "Mini-Split Control Wired" },
  { sku: "DT04PLUS-001", brand: "Mini-Split Control Wired" },
  { sku: "DT05PLUS", brand: "Mini-Split Control Wired" },
  { sku: "DT05HW", brand: "Mini-Split Control Wired" },
  { sku: "LCDWIREII", brand: "Mini-Split Control Wired" },
  { sku: "WLTH-020", brand: "Mini-Split Control Wired" },
  { sku: "WLTH-010", brand: "Mini-Split Control Wired" },
  { sku: "KT-828 Gold", brand: "Mini-Split Control Wireless" },
  { sku: "KT-S828 Silver", brand: "Mini-Split Control Wireless" },
  { sku: "KT-E03", brand: "Mini-Split Control Wireless" },
  { sku: "KT-E08", brand: "Mini-Split Control Wireless" },
  { sku: "Q-338-F", brand: "Mini-Split Control Wireless" },
  { sku: "Q-380EW", brand: "Mini-Split Control Wireless" },
  { sku: "XE8400A", brand: "Mini-Split Control Wireless" },
  { sku: "TC300B-G", brand: "Honeywell" },
  { sku: "TC500A-N", brand: "Honeywell" },
  { sku: "THP2400A1068", brand: "Honeywell" },
  { sku: "TH5110D1022", brand: "Honeywell" },
  { sku: "TH8320R1003", brand: "Honeywell" },
  { sku: "TH6220D1028", brand: "Honeywell" },
  { sku: "THP9045A1023", brand: "Honeywell" },
  { sku: "THP2400A1027W", brand: "Honeywell" },
  { sku: "TH8110R1008", brand: "Honeywell" },
  { sku: "TH9320WF5003", brand: "Honeywell" },
  { sku: "TH8321WF1001", brand: "Honeywell" },
  { sku: "TH1110DV1009", brand: "Honeywell" },
  { sku: "TH1110DH1003", brand: "Honeywell" },
  { sku: "TE86SB-501", brand: "Vtronix", discontinued: true },
  { sku: "TE80SB-501", brand: "Vtronix", discontinued: true },
  { sku: "LAKEPRO-1", brand: "Vtronix" },
  { sku: "PI02", brand: "Floating" },
  { sku: "PI03-AUX", brand: "Modulating" },
  { sku: "PI04", brand: "Modulating" },
  { sku: "TB7980A1006", brand: "Honeywell" },
  { sku: "TB6980A1007", brand: "Honeywell" },
  { sku: "TB8575A1000", brand: "Honeywell" },
  { sku: "TB6575B1000", brand: "Honeywell" },
  { sku: "TB6575A1000", brand: "Honeywell" },
  { sku: "T6811DP08", brand: "Honeywell" },
  { sku: "TF63M-002", brand: "Electronic - 3 Speed Fan" },
  { sku: "TF63M-001", brand: "Electronic - 3 Speed Fan" },
  { sku: "TE63M-002", brand: "Electronic - 3 Speed Fan" },
  { sku: "TE63M-001", brand: "Electronic - 3 Speed Fan" },
  { sku: "VU444A1007", brand: "Honeywell" },
  { sku: "TF65L-001", brand: "Digital - 3 Speed Fan, On/Off", discontinued: true },
  { sku: "TF85L-11011", brand: "Digital - 3 Speed Fan, On/Off", discontinued: true },
  { sku: "TF85L-10011", brand: "Digital - 3 Speed Fan, On/Off", discontinued: true },
  { sku: "TF65L-002-SWP", brand: "Digital - 3 Speed Fan, On/Off", discontinued: true },
  { sku: "TF65L-002-STD", brand: "Digital - 3 Speed Fan, On/Off", discontinued: true },
  { sku: "T5575B-STD", brand: "Digital - 3 Speed Fan, On/Off" },
  { sku: "TF85L-201", brand: "Digital - 3 Speed Fan, On/Off" },
  { sku: "TF85L-200", brand: "Digital - 3 Speed Fan, On/Off" },
  { sku: "CB600V", brand: "ECM Motor Control" },
  { sku: "R100A", brand: "Air Conditioning Control" },
  { sku: "R200A/S3", brand: "AHU Control" },
  { sku: "R650", brand: "ECM Motor Control" },
  { sku: "R60A", brand: "Fan Delay" },
  { sku: "R85A-001", brand: "AHU Control" },
  { sku: "CBX02003", brand: "Fan Delay" },
  { sku: "EW40030", brand: "ECM Motor Control" },
  { sku: "EW40040", brand: "ECM Motor Control" },
  { sku: "VCZAR1100", brand: "Honeywell" },
  { sku: "VCZAL1100", brand: "Honeywell" },
  { sku: "VC4013ZZ00", brand: "Honeywell" },
  { sku: "VC8011ZZ00", brand: "Honeywell" },
  { sku: "V8043E1145", brand: "Honeywell" },
  { sku: "VU52S2028", brand: "Honeywell" }
];

var VTRONIX_CATEGORIES = [
  { slug: "control-boards", label: "Control Boards" },
  { slug: "residential-thermostats", label: "Thermostats - Residential" },
  { slug: "commercial-thermostats", label: "Thermostats - Commercial" },
  { slug: "fan-coil-thermostats", label: "Fan Coil Controls" },
  { slug: "mini-split-controls", label: "Mini Split Controls" },
  { slug: "energy-savings", label: "Energy Savings" },
  { slug: "temperature-controls", label: "Temperature Controls" },
  { slug: "all-products", label: "All Products" },
  { slug: "discontinued", label: "Discontinued Items" }
];

/* Explicit per-category display order, exactly as shown on vtronix.com.
   A SKU can appear in more than one list (Wix allows multi-category
   products), and its relative order can differ between the two —
   discontinued items are left out of their live category listing and
   only ever appear under "discontinued-items" and "all-products". */
var VTRONIX_CATEGORY_ORDER = {
  "control-boards": [
    "R200A/S3", "R201", "R85A-001",
    "R100A", "RAB-A24.11BE3", "W100",
    "CB600V", "EW40030", "EW40040", "R650",
    "CBX02003", "CBX99100", "R60A", "R60B-45/S2", "R60B-45/S2-R60BLEADS", "R60BLEADS",
    "R502",
    "R401"
  ],
  "residential-thermostats": [
    "LAKEPRO-1",
    "TH1110DH1003", "TH1110DV1009", "TH4110U2005", "TH5110D1022", "TH6210U2001",
    "TH6220D1028", "TH8110R1008", "TH8320R1003", "TH8321WF1001", "TH9320WF5003",
    "THP9045A1023", "32003796-001", "THP2400A1027W", "THP2400A1068"
  ],
  "commercial-thermostats": [
    "TB7980B1005", "TB7980A1006", "TB6980A1007", "TB8575A1000", "TB6575A1000",
    "TC300B-G", "TC500A-N", "50033847-001"
  ],
  "fan-coil-thermostats": [
    "TB7980B1005", "TF85L-200", "TF85L-201", "T5575B-STD",
    "TE63M-001", "TE63M-002", "TF63M-001", "TF63M-002",
    "PI02", "PI03-AUX", "PI04",
    "T6373B1148", "T6811DP08", "TB6575A1000", "TB6575B1000", "TB6980A1007", "TB7980A1006", "TB8575A1000",
    "V8043E1145", "VC4013ZZ00", "VC8011ZZ00", "VCZAR1100", "VCZAL1100", "VU444A1007", "VU52S2028"
  ],
  "mini-split-controls": [
    "KT-E03", "KT-E08", "KT-828 Gold", "KT-S828 Silver", "Q-338-F", "Q-380EW", "XE8400A",
    "DT03PLUS-001", "DT04-HC-220", "DT04-HC-120", "DT04PLUS-001", "DT05PLUS", "DT05HW",
    "LCDWIREII", "WLTH-010", "WLTH-020"
  ],
  "energy-savings": [
    "HESK120V", "HESK220V", "i-Save", "i-save1001", "i-save1002"
  ],
  "temperature-controls": [
    "W100", "T775A2009", "AHU Control", "FT101", "MSI", "Outdoor Control", "TC102", "W110", "Zone Control II"
  ],
  "discontinued": [
    "ECONO3-001", "TE80SB-501", "TE86SB-501",
    "TF65L-001", "TF65L-002-STD", "TF65L-002-SWP", "TF85L-10011", "TF85L-11011"
  ]
};

/* "All Products" mirrors the exact order captured from the live site,
   which is its own curated sequence rather than a concatenation of the
   category lists above — so it's listed explicitly rather than derived. */
VTRONIX_CATEGORY_ORDER["all-products"] = VTRONIX_PRODUCTS.map(function (p) {
  return p.sku;
});

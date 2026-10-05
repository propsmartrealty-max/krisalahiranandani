#!/usr/bin/env python3
"""
Krisala Hiranandani Township Hinjewadi
Programmatic XML Sitemap Index & Sharded Sub-Sitemaps Generator (10,000 URLs)
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime

BASE_URL = "https://krisalahiranandanitownships.com"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "sitemaps")
INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sitemap-index.xml")

SILOS = [
    {
        "name": "configurations",
        "file": "sitemap-configurations.xml",
        "bases": ["2-bhk-luxury-apartments", "3-bhk-royale-residences", "4-bhk-palatial-homes", "5-bhk-signature-penthouses", "duplex-sky-villas"],
        "modifiers": ["floor-plans", "carpet-area-specs", "tower-layout-blueprints", "sample-flat-video", "possession-dates", "price-breakdown", "vaastu-compliant", "corner-units", "balcony-views", "luxury-finishes"],
        "localities": ["hinjewadi-phase-1", "hinjewadi-phase-2", "hinjewadi-phase-3", "mahalunge-smart-city", "mahalunge-riverfront", "north-hinjewadi", "darumbre-marunji", "baner-balewadi-belt", "wakad-extension", "hadapsar-comparison", "near-metro-station", "near-expressway", "near-wipro-circle", "near-infosys-campus", "punawale-annexe", "tathawade-corridor", "sahydari-view", "racecourse-facing", "podium-facing", "executive-enclave"]
    },
    {
        "name": "pricing",
        "file": "sitemap-pricing.xml",
        "bases": ["price-list-2026", "all-inclusive-cost-sheet", "stamp-duty-gst-breakup", "construction-linked-payment-plan", "down-payment-offers"],
        "modifiers": ["79-lakhs-2-bhk", "1-25-crore-3-bhk", "2-10-crore-4-bhk", "3-20-crore-5-bhk", "2-65-crore-duplex", "bank-pre-approved-loans", "sbi-home-loan-interest", "hdfc-bank-approval", "icici-bank-eligibility", "axis-bank-schemes"],
        "localities": ["hinjewadi", "mahalunge", "darumbre", "marunji", "wakad", "baner", "pune-it-park", "north-hinjewadi", "pune-west", "pune-mumbai-expressway", "metro-corridor", "nri-investors", "it-executives", "direct-developer-price", "zero-brokerage", "exclusive-discounts", "festive-offers", "pre-launch-benefits", "eoi-booking-token", "schedule-site-visit"]
    },
    {
        "name": "it-workplaces",
        "file": "sitemap-it-workplaces.xml",
        "bases": ["commute-to-infosys-phase-1-2", "distance-to-wipro-circle", "travel-time-to-tcs-sahyadri-park", "commute-to-cognizant-phase-3", "proximity-to-barclays-global"],
        "modifiers": ["2-bhk-homes", "3-bhk-residences", "4-bhk-duplexes", "5-bhk-penthouses", "it-professionals-housing", "shuttle-bus-routes", "walking-commute-options", "signal-free-drive", "work-life-balance", "top-rated-township"],
        "localities": ["rajiv-gandhi-infotech-park", "mahalunge-tech-corridor", "embassy-tech-zone", "quadron-business-park", "tech-mahindra-campus", "capgemini-office", "accenture-hinjewadi", "credit-suisse-pune", "nvidia-ai-center", "ibm-software-labs", "synechron-office", "dassault-systemes", "e-zest-solutions", "atos-syntel-campus", "persistent-systems", "kpso-tech-hub", "blueridge-seze", "megapolis-circle", "phase-3-terminal", "wipro-phase-2"]
    },
    {
        "name": "connectivity",
        "file": "sitemap-connectivity.xml",
        "bases": ["mumbai-pune-expressway-access", "hinjewadi-metro-line-3-megapolis", "pmrda-128m-ring-road-junction", "mahalunge-hinjewadi-bridge", "pune-international-airport-commute"],
        "modifiers": ["signal-free-corridor", "5-mins-drive", "3-mins-access", "zero-traffic-route", "arterial-road-widening", "metro-feeder-services", "darumbre-underpass", "expressway-toll-bypass", "baner-connectivity", "hadapsar-bypass-link"],
        "localities": ["hinjewadi", "mahalunge", "marunji", "darumbre", "wakad", "punawale", "tathawade", "ravet", "balewadi", "baner", "somatane-phata", "dehu-road", "talegaon-industrial", "chakan-auto-hub", "shivajinagar-station", "pune-railway-station", "hadapsar-corridor", "kharadi-it-belt", "magarpatta-city", "purandar-airport"]
    },
    {
        "name": "comparisons",
        "file": "sitemap-comparisons.xml",
        "bases": ["vs-godrej-river-royale-mahalunge", "vs-vtp-earth-one-mahalunge", "vs-lodha-sylvan-hinjewadi", "vs-kolte-patil-life-republic", "vs-shapoorji-joyville-hinjewadi"],
        "modifiers": ["price-comparison", "carpet-area-difference", "amenity-benchmark", "construction-quality-mivan", "neoclassical-vs-modern", "racecourse-vs-standard-open-space", "appreciation-forecast", "rera-possession-timeline", "green-building-teri", "location-connectivity-advantage"],
        "localities": ["2-bhk-comparison", "3-bhk-comparison", "4-bhk-comparison", "5-bhk-comparison", "duplex-comparison", "hinjewadi-phase-1", "hinjewadi-phase-2", "hinjewadi-phase-3", "mahalunge-projects", "north-hinjewadi", "wakad-projects", "baner-projects", "balewadi-projects", "hadapsar-comparison", "gated-community-ratings", "resale-value-comparison", "rental-yield-benchmark", "maintenance-cost-analysis", "developer-track-record", "final-verdict-guide"]
    },
    {
        "name": "amenities",
        "file": "sitemap-amenities.xml",
        "bases": ["della-8-acre-private-racecourse", "international-polo-club", "50000-sqft-neoclassical-clubhouse", "olympic-length-swimming-pool", "teri-certified-water-hydrology"],
        "modifiers": ["horse-riding-academy", "equestrian-stables", "sports-arenas-cricket-football", "indoor-badminton-squash", "co-working-business-lounge", "sky-observatory-deck", "zen-meditation-gardens", "organic-urban-farming", "pet-park-agility-zone", "children-adventure-playscape"],
        "localities": ["sector-arcadia-amenities", "sector-icon-exclusive-club", "della-resort-privileges", "concierge-lifestyle", "wellness-lifestyle", "senior-citizen-enclaves", "ev-charging-infrastructure", "3-tier-biometric-security", "lotus-ponds-jogging-tracks", "banquet-hall-facilities", "amphitheatre-events", "spa-sauna-jacuzzi", "cycling-velodrome", "tennis-courts", "pickleball-arena", "skating-rink", "climbing-wall", "yoga-deck", "reflexology-path", "lifestyle-sanctuary"]
    },
    {
        "name": "investment-roi",
        "file": "sitemap-investment-roi.xml",
        "bases": ["capital-appreciation-forecast-2026-2035", "gross-rental-yield-analysis", "it-hub-tenant-demand", "resale-value-trends-hinjewadi", "nri-real-estate-investment-guide"],
        "modifiers": ["14-to-18-percent-cagr", "5-percent-rental-yield", "metro-line-3-impact", "pmrda-ring-road-multiplier", "tax-benefits-80c-24b", "repatriation-nre-nro", "wealth-creation-strategy", "commercial-corridor-growth", "first-mover-township-advantage", "inflation-hedge-asset"],
        "localities": ["2-bhk-roi", "3-bhk-roi", "4-bhk-roi", "duplex-roi", "della-plot-roi", "hinjewadi-it-boom", "pune-real-estate-market", "dubai-nri-investors", "usa-nri-buyers", "singapore-nri-investors", "london-nri-investors", "tech-leader-portfolio", "passive-rental-income", "ready-reckoner-rates", "capital-gains-exemption", "property-management-services", "high-net-worth-estates", "family-office-allocation", "long-term-wealth", "investment-whitepaper"]
    },
    {
        "name": "sustainability",
        "file": "sitemap-sustainability.xml",
        "bases": ["teri-50-year-green-rating", "igbc-platinum-township-certification", "zero-discharge-circular-water-ecology", "rainwater-harvesting-reservoirs", "solar-clean-energy-microgrid"],
        "modifiers": ["30-percent-lower-utility-bills", "pure-air-aqi-advantage", "microclimate-cooling-facades", "ev-corridor-charging", "solid-waste-vermicomposting", "indigenous-native-tree-canopies", "natural-biofiltration-swales", "acoustic-noise-isolation", "water-resilient-living", "carbon-neutral-footprint"],
        "localities": ["sector-arcadia-green", "sector-icon-eco-living", "della-green-sanctuary", "hinjewadi-nature-haven", "sahyadri-breeze-corridors", "sustainable-family-lifestyle", "organic-gardens", "green-building-benefits", "low-maintenance-eco-design", "healthy-resident-index", "eco-friendly-architecture", "clean-groundwater-aquifers", "solar-streetlights", "energy-efficient-elevators", "low-voc-materials", "green-mobility-hubs", "water-conservation-model", "environmental-clearance", "circular-economy-pune", "future-ready-township"]
    },
    {
        "name": "construction",
        "file": "sitemap-construction.xml",
        "bases": ["mivan-aluminium-formwork-engineering", "earthquake-resistant-seismic-zone-iii", "soundproof-acoustic-double-glazing", "italian-marble-flooring-specifications", "high-speed-destination-controlled-elevators"],
        "modifiers": ["monolithic-shear-wall-structure", "zero-leakage-construction", "laser-measured-floor-levels", "fire-retardant-electricals", "schindler-otis-smart-lifts", "grohe-kohler-cp-fittings", "toughened-glass-balustrades", "anti-termite-treated-foundations", "waterproofing-10-year-warranty", "heavy-duty-granite-counters"],
        "localities": ["tower-a-construction-updates", "tower-b-status", "tower-c-progress", "tower-d-milestones", "sector-icon-craftsmanship", "sector-arcadia-engineering", "hiranandani-quality-hallmark", "krisala-engineering-rigor", "precision-build-quality", "structural-safety-audit", "precast-boundary-walls", "concrete-core-strength", "advanced-curing-technology", "flawless-smooth-wall-finish", "concealed-plumbing-pipes", "modular-switchgear", "generator-backup-100-percent", "video-security-surveillance", "water-pressure-pumps", "lifetime-durability-homes"]
    },
    {
        "name": "rera-legal",
        "file": "sitemap-rera-legal.xml",
        "bases": ["maharera-registration-pr1260002502438", "sector-icon-rera-pr1260002600818", "phase-wise-possession-schedule", "carpet-area-regulatory-verification", "clear-marketable-title-search-report"],
        "modifiers": ["q4-2028-possession", "q2-2029-possession", "rera-approved-bank-loans", "encumbrance-free-land-title", "7-12-extract-verification", "environmental-noc-clearance", "fire-safety-noc-approval", "airport-authority-height-noc", "pmrda-sanctioned-layout", "commencement-certificate-cc"],
        "localities": ["darumbre-survey-numbers", "marunji-gat-numbers", "north-hinjewadi-approval", "krisala-joint-venture-agreement", "hiranandani-development-rights", "buyer-rights-and-guarantees", "rera-escrow-account-transparency", "zero-risk-booking-process", "legal-due-diligence-guide", "allotment-letter-terms", "agreement-for-sale-draft", "stamp-duty-calculation-rules", "registration-office-haveli", "sub-registrar-pune-west", "rera-complaint-free-record", "legal-faq-homebuyers", "nri-power-of-attorney", "gst-input-tax-rules", "oc-handover-timeline", "official-compliance-dossier"]
    }
]

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(ROOT_DIR, "public", "sitemaps")
INDEX_PATH = os.path.join(ROOT_DIR, "sitemap-index.xml")

def generate_sharded_sitemaps():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    sub_sitemaps = []
    total_urls = 0

    print("=" * 60)
    print("Generating 10,000 Programmatic URLs Across 10 Sharded Sitemaps...")
    print("=" * 60)

    for silo in SILOS:
        filename = silo["file"]
        root_filepath = os.path.join(ROOT_DIR, filename)
        public_filepath = os.path.join(OUTPUT_DIR, filename)
        silo_urls = []

        # Generate exactly 1,000 programmatic combinations: 5 bases * 10 modifiers * 20 localities = 1,000
        for b in silo["bases"]:
            for m in silo["modifiers"]:
                for loc in silo["localities"]:
                    slug = f"krisala-hiranandani-{b}-{m}-{loc}"
                    url = f"{BASE_URL}/explore/{slug}"
                    silo_urls.append(url)

        # Build XML
        root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        for u in silo_urls:
            url_elem = ET.SubElement(root, "url")
            loc_elem = ET.SubElement(url_elem, "loc")
            loc_elem.text = u
            lastmod = ET.SubElement(url_elem, "lastmod")
            lastmod.text = today
            changefreq = ET.SubElement(url_elem, "changefreq")
            changefreq.text = "weekly"
            priority = ET.SubElement(url_elem, "priority")
            priority.text = "0.8"

        tree = ET.ElementTree(root)
        ET.indent(tree, space="  ", level=0)
        xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
        full_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>\n{xml_str}'
        
        # Write to root directory (Googlebot directory scope root /)
        with open(root_filepath, "w", encoding="utf-8") as f:
            f.write(full_xml)
            
        # Also write to public/sitemaps for backward compatibility
        with open(public_filepath, "w", encoding="utf-8") as f:
            f.write(full_xml)

        print(f"  [✓] {filename}: {len(silo_urls)} URLs generated (Root: {root_filepath})")
        # Sub-sitemaps linked directly at root level to satisfy sitemaps.org directory scope
        sub_sitemaps.append(f"{BASE_URL}/{filename}")
        total_urls += len(silo_urls)

    # Build Master Sitemap Index
    index_root = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Include primary root sitemaps
    primary_sitemaps = [
        f"{BASE_URL}/sitemap.xml",
        f"{BASE_URL}/image-sitemap.xml",
        f"{BASE_URL}/video-sitemap.xml"
    ]
    for p in primary_sitemaps:
        s_elem = ET.SubElement(index_root, "sitemap")
        loc_elem = ET.SubElement(s_elem, "loc")
        loc_elem.text = p
        lastmod = ET.SubElement(s_elem, "lastmod")
        lastmod.text = today

    # Include the 10 sharded programmatic sitemaps (all at root domain level)
    for s in sub_sitemaps:
        s_elem = ET.SubElement(index_root, "sitemap")
        loc_elem = ET.SubElement(s_elem, "loc")
        loc_elem.text = s
        lastmod = ET.SubElement(s_elem, "lastmod")
        lastmod.text = today

    index_tree = ET.ElementTree(index_root)
    ET.indent(index_tree, space="  ", level=0)
    index_xml_str = ET.tostring(index_root, encoding="utf-8").decode("utf-8")
    full_index_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>\n{index_xml_str}'
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(full_index_xml)
    print(f"\n[✓] Master Sitemap Index generated with XSL stylesheet: {INDEX_PATH}")
    print(f"    Referencing 3 core sitemaps + 10 programmatic sub-sitemaps ({total_urls} programmatic URLs)")
    print("=" * 60)

if __name__ == "__main__":
    generate_sharded_sitemaps()

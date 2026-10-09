#!/usr/bin/env python3
"""
Krisala Hiranandani Township Hinjewadi
Enterprise Programmatic XML Sitemap & Dynamic Index Engine (15,000+ URLs)
Complies with Google Webmaster & Sitemaps XML 0.9 + Image Sitemap 1.1 Protocols
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime

BASE_URL = "https://krisalahiranandanitownships.com"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(ROOT_DIR, "public", "sitemaps")
INDEX_PATH = os.path.join(ROOT_DIR, "sitemap-index.xml")
MAIN_SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")

# 15 Granular Semantic Intent Silos for High-Intent Real Estate Keywords
SILOS = [
    {
        "name": "configurations",
        "file": "sitemap-configurations.xml",
        "hubs": ["/arcadia", "/icon"],
        "bases": ["2-bhk-luxury-apartments", "3-bhk-royale-residences", "4-bhk-palatial-homes", "5-bhk-signature-penthouses", "duplex-sky-villas"],
        "modifiers": ["floor-plans", "carpet-area-specs", "tower-layout-blueprints", "sample-flat-video", "possession-dates", "price-breakdown", "vaastu-compliant", "corner-units", "balcony-views", "luxury-finishes"],
        "localities": ["hinjewadi-phase-1", "hinjewadi-phase-2", "hinjewadi-phase-3", "mahalunge-smart-city", "mahalunge-riverfront", "north-hinjewadi", "darumbre-marunji", "baner-balewadi-belt", "wakad-extension", "hadapsar-comparison", "near-metro-station", "near-expressway", "near-wipro-circle", "near-infosys-campus", "punawale-annexe", "tathawade-corridor", "sahydari-view", "racecourse-facing", "podium-facing", "executive-enclave"]
    },
    {
        "name": "pricing",
        "file": "sitemap-pricing.xml",
        "hubs": ["/pricing"],
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
        "hubs": ["/connectivity"],
        "bases": ["mumbai-pune-expressway-access", "hinjewadi-metro-line-3-megapolis", "pmrda-128m-ring-road-junction", "mahalunge-hinjewadi-bridge", "pune-international-airport-commute"],
        "modifiers": ["signal-free-corridor", "5-mins-drive", "3-mins-access", "zero-traffic-route", "arterial-road-widening", "metro-feeder-services", "darumbre-underpass", "expressway-toll-bypass", "baner-connectivity", "hadapsar-bypass-link"],
        "localities": ["hinjewadi", "mahalunge", "marunji", "darumbre", "wakad", "punawale", "tathawade", "ravet", "balewadi", "baner", "somatane-phata", "dehu-road", "talegaon-industrial", "chakan-auto-hub", "shivajinagar-station", "pune-railway-station", "hadapsar-corridor", "kharadi-it-belt", "magarpatta-city", "purandar-airport"]
    },
    {
        "name": "comparisons",
        "file": "sitemap-comparisons.xml",
        "hubs": ["/compare"],
        "bases": ["vs-godrej-river-royale-mahalunge", "vs-vtp-earth-one-mahalunge", "vs-lodha-sylvan-hinjewadi", "vs-kolte-patil-life-republic", "vs-shapoorji-joyville-hinjewadi"],
        "modifiers": ["price-comparison", "carpet-area-difference", "amenity-benchmark", "construction-quality-mivan", "neoclassical-vs-modern", "racecourse-vs-standard-open-space", "appreciation-forecast", "rera-possession-timeline", "green-building-teri", "location-connectivity-advantage"],
        "localities": ["2-bhk-comparison", "3-bhk-comparison", "4-bhk-comparison", "5-bhk-comparison", "duplex-comparison", "hinjewadi-phase-1", "hinjewadi-phase-2", "hinjewadi-phase-3", "mahalunge-projects", "north-hinjewadi", "wakad-projects", "baner-projects", "balewadi-projects", "hadapsar-comparison", "gated-community-ratings", "resale-value-comparison", "rental-yield-benchmark", "maintenance-cost-analysis", "developer-track-record", "final-verdict-guide"]
    },
    {
        "name": "amenities",
        "file": "sitemap-amenities.xml",
        "hubs": ["/amenities", "/racecourse"],
        "bases": ["della-8-acre-private-racecourse", "international-polo-club", "50000-sqft-neoclassical-clubhouse", "olympic-length-swimming-pool", "teri-certified-water-hydrology"],
        "modifiers": ["horse-riding-academy", "equestrian-stables", "sports-arenas-cricket-football", "indoor-badminton-squash", "co-working-business-lounge", "sky-observatory-deck", "zen-meditation-gardens", "organic-urban-farming", "pet-park-agility-zone", "children-adventure-playscape"],
        "localities": ["sector-arcadia-amenities", "sector-icon-exclusive-club", "della-resort-privileges", "concierge-lifestyle", "wellness-lifestyle", "senior-citizen-enclaves", "ev-charging-infrastructure", "3-tier-biometric-security", "lotus-ponds-jogging-tracks", "banquet-hall-facilities", "amphitheatre-events", "spa-sauna-jacuzzi", "cycling-velodrome", "tennis-courts", "pickleball-arena", "skating-rink", "climbing-wall", "yoga-deck", "reflexology-path", "lifestyle-sanctuary"]
    },
    {
        "name": "investment-roi",
        "file": "sitemap-investment-roi.xml",
        "hubs": ["/knowledge-hub"],
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
        "hubs": ["/privacy-policy"],
        "bases": ["maharera-registration-pr1260002502438", "sector-icon-rera-pr1260002600818", "phase-wise-possession-schedule", "carpet-area-regulatory-verification", "clear-marketable-title-search-report"],
        "modifiers": ["q4-2028-possession", "q2-2029-possession", "rera-approved-bank-loans", "encumbrance-free-land-title", "7-12-extract-verification", "environmental-noc-clearance", "fire-safety-noc-approval", "airport-authority-height-noc", "pmrda-sanctioned-layout", "commencement-certificate-cc"],
        "localities": ["darumbre-survey-numbers", "marunji-gat-numbers", "north-hinjewadi-approval", "krisala-joint-venture-agreement", "hiranandani-development-rights", "buyer-rights-and-guarantees", "rera-escrow-account-transparency", "zero-risk-booking-process", "legal-due-diligence-guide", "allotment-letter-terms", "agreement-for-sale-draft", "stamp-duty-calculation-rules", "registration-office-haveli", "sub-registrar-pune-west", "rera-complaint-free-record", "legal-faq-homebuyers", "nri-power-of-attorney", "gst-input-tax-rules", "oc-handover-timeline", "official-compliance-dossier"]
    },
    {
        "name": "nri-desk",
        "file": "sitemap-nri-desk.xml",
        "hubs": ["/nri"],
        "bases": ["nri-real-estate-investment-pune", "fema-compliant-property-buying-guide", "nre-nro-capital-repatriation-rules", "dubai-uae-nri-property-investment", "usa-canada-nri-property-buying"],
        "modifiers": ["5-percent-rental-yield", "100-percent-digital-kyc-remote-poa", "pre-approved-nri-home-loans", "dtaa-double-tax-avoidance", "turnkey-tenant-management-services", "high-cagr-capital-appreciation", "virtual-4k-drone-walkthrough", "maharera-verified-title-docket", "dr-niranjan-hiranandani-township", "della-equestrian-polo-plots"],
        "localities": ["hinjewadi-phase-3", "mahalunge-smart-city", "north-hinjewadi", "darumbre-marunji", "baner-balewadi", "wakad-extension", "dubai-nri-buyers", "abu-dhabi-investors", "singapore-expats", "london-uk-nris", "california-bay-area-nris", "seattle-tech-nris", "texas-dallas-buyers", "toronto-canada-nris", "sydney-australia-nris", "it-leadership-portfolios", "family-office-investments", "luxury-duplex-penthouses", "simplex-executive-suites", "ready-possession-villa-plots"]
    },
    {
        "name": "amenities-lifestyle",
        "file": "sitemap-amenities-lifestyle.xml",
        "hubs": ["/amenities", "/racecourse"],
        "bases": ["8-acre-private-racecourse-polo-club", "50000-sqft-neoclassical-clubhouse", "olympic-temperature-controlled-lap-pool", "teri-50-year-water-reservoirs", "pro-turf-tennis-pickleball-arenas"],
        "modifiers": ["horse-riding-academy-training", "air-cooled-equine-stables", "technogym-biometric-fitness-center", "ayurvedic-spa-turkish-hammam", "indoor-wooden-badminton-squash", "fifa-certified-box-cricket-football", "15-acre-central-botanical-park", "1000-seater-roman-amphitheatre", "adventure-kids-playscape-splash-park", "smart-coworking-zoom-video-pods"],
        "localities": ["sector-arcadia-residents", "sector-icon-sky-villas", "the-della-collection-plots", "hinjewadi-tech-executives", "north-hinjewadi-living", "mahalunge-hi-tech-city", "pune-west-luxury-lifestyle", "equestrian-enthusiasts", "wellness-and-longevity", "sustainable-family-living", "senior-citizen-enclaves", "pet-friendly-township", "ev-mobility-infrastructure", "ai-3-tier-surveillance", "high-street-retail-arcade", "jogging-and-cycling-velodrome", "meditation-and-yoga-decks", "lotus-ponds-and-wetlands", "igbc-platinum-green-living", "zero-tanker-water-security"]
    },
    {
        "name": "colosseum",
        "file": "sitemap-colosseum.xml",
        "hubs": ["/colosseum"],
        "bases": ["the-colosseum-phase-4-pre-launch", "roman-neoclassical-luxury-towers", "diwali-pre-launch-benefits-5-to-9-lakhs", "amphitheater-podium-residences", "270-degree-racecourse-facing-homes"],
        "modifiers": ["2-bhk-grande-765-sqft", "3-bhk-royale-1085-sqft", "3-bhk-regalia-1215-sqft", "4-bhk-palatial-1600-sqft", "eoi-token-2-70-lakhs", "eoi-token-3-60-lakhs", "priority-allotment-window", "expressway-facing-balconies", "mivan-shear-wall-structure", "igbc-platinum-pre-certified"],
        "localities": ["hinjewadi-phase-1", "hinjewadi-phase-2", "hinjewadi-phase-3", "mahalunge-smart-city", "north-hinjewadi-darumbre", "marunji-boulevard", "wakad-it-executives", "baner-homebuyers", "balewadi-investors", "punawale-corridor", "tathawade-annexe", "mumbai-investors", "dubai-nri-desk", "tech-leaders-enclave", "pre-launch-exclusive", "diwali-2026-offer", "first-access-pass", "possession-2028-2029", "flawless-title-docket", "maharera-registered"]
    },
    {
        "name": "micromarkets",
        "file": "sitemap-micromarkets.xml",
        "hubs": ["/neighborhood"],
        "bases": ["luxury-apartments-hinjewadi-phase-1", "premium-flats-hinjewadi-phase-2", "gated-community-hinjewadi-phase-3", "waterfront-homes-mahalunge-smart-city", "nature-residences-north-hinjewadi"],
        "modifiers": ["near-metro-line-3-station", "near-wipro-circle", "near-infosys-phase-2", "near-pmrda-ring-road", "near-mumbai-pune-expressway", "near-della-adventure-racecourse", "with-italian-marble", "with-clubhouse-amenities", "with-zero-traffic-commute", "with-teri-green-certification"],
        "localities": ["marunji-gateway", "darumbre-interchange", "wakad-bridge-link", "balewadi-high-street-access", "baner-pashan-link", "punawale-connector", "tathawade-it-belt", "ravet-pradhikaran", "somatane-phata", "kasarsai-dam-belt", "maan-village-corridor", "blueridge-adjacent", "megapolis-circle", "quadron-tech-park", "embassy-zone", "tcs-sahyadri-belt", "cognizant-circle", "barclays-hq", "tech-mahindra-campus", "capgemini-park"]
    },
    {
        "name": "villa-plots",
        "file": "sitemap-villa-plots.xml",
        "hubs": ["/della"],
        "bases": ["the-della-collection-villa-plots", "equestrian-estate-plots-hinjewadi", "resort-living-villa-land", "custom-g-plus-2-luxury-villas", "polo-club-facing-villa-parcels"],
        "modifiers": ["2000-sqft-exclusive-plot", "3000-sqft-estate-parcel", "5000-sqft-presidential-plot", "8-acre-racecourse-access", "della-5-star-resort-privileges", "clear-demarcated-title", "maharera-approved-plots", "high-cagr-land-appreciation", "nri-preferred-villa-land", "private-gated-security"],
        "localities": ["hinjewadi-darumbre", "mahalunge-annexe", "north-hinjewadi-greens", "sahyadri-valley-facing", "equestrian-polo-grounds", "pune-mumbai-corridor", "dubai-nri-investors", "bay-area-tech-leaders", "london-hni-clients", "singapore-expats", "c-suite-executives", "family-office-estates", "exclusive-100-plots", "immediate-possession-ready", "zero-encumbrance-land", "direct-developer-allotment", "private-club-membership", "helipad-accessibility", "equine-stable-access", "lifetime-legacy-asset"]
    }
]

# Core Static Pages with High E-E-A-T & Google Dynamic Content Attributes
CORE_STATIC_PAGES = [
    {
        "url": f"{BASE_URL}/",
        "changefreq": "daily",
        "priority": "1.0",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
            "title": "Krisala Hiranandani Township Hinjewadi Aerial View",
            "caption": "105-Acre Krisala Hiranandani Township in Pune featuring Premium 2, 3, and 4 BHK Apartments and Della Villa Plots"
        }
    },
    {
        "url": f"{BASE_URL}/colosseum",
        "changefreq": "daily",
        "priority": "0.95",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_exterior.webp",
            "title": "Codename The Colosseum Phase 4 Krisala Hiranandani",
            "caption": "Roman-inspired luxury towers offering 2, 3, 4 BHK residences starting ₹82.99L with exclusive Diwali early bird benefits"
        }
    },
    {
        "url": f"{BASE_URL}/arcadia",
        "changefreq": "weekly",
        "priority": "0.95",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_exterior.webp",
            "title": "Sector Arcadia Residences at Krisala Hiranandani",
            "caption": "Premium 2 and 3 BHK luxury residences in Sector Arcadia, North Hinjewadi with neoclassical architecture"
        }
    },
    {
        "url": f"{BASE_URL}/icon",
        "changefreq": "weekly",
        "priority": "0.95",
        "image": {
            "loc": f"{BASE_URL}/public/icon_official/icon_towers_sunset_grand_elevation.webp",
            "title": "Sector Icon Ultra-Luxury Residences and Sky Duplexes",
            "caption": "3 and 4 BHK ultra-luxury residences and double-height duplex penthouses overlooking the 8-acre racecourse"
        }
    },
    {
        "url": f"{BASE_URL}/della",
        "changefreq": "weekly",
        "priority": "0.95",
        "image": {
            "loc": f"{BASE_URL}/public/township_grand/della_resort_villas_equestrian_official.webp",
            "title": "The Della Collection Equestrian Villa Plots",
            "caption": "Equestrian-themed resort-style luxury villa plots with 8-acre private racecourse and international polo club"
        }
    },
    {
        "url": f"{BASE_URL}/pricing",
        "changefreq": "daily",
        "priority": "0.95",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
            "title": "Krisala Hiranandani Official Price List and Cost Sheets 2026",
            "caption": "MahaRERA verified 2026 price list, CLP payment schedule, stamp duty breakup, and bank pre-approved loans"
        }
    },
    {
        "url": f"{BASE_URL}/racecourse",
        "changefreq": "weekly",
        "priority": "0.90",
        "image": {
            "loc": f"{BASE_URL}/public/imported/della-racecource.webp",
            "title": "8-Acre Private Racecourse and International Polo Club Hinjewadi",
            "caption": "India's first residential private racecourse inside a 105-acre township in Pune"
        }
    },
    {
        "url": f"{BASE_URL}/masterplan",
        "changefreq": "monthly",
        "priority": "0.90",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/masterplan/master_layout_hq.webp",
            "title": "Interactive Masterplan 2.0 Krisala Hiranandani",
            "caption": "105-Acre interactive township masterplan and sector zoning with GPS-calibrated sector points"
        }
    },
    {
        "url": f"{BASE_URL}/amenities",
        "changefreq": "weekly",
        "priority": "0.90",
        "image": {
            "loc": f"{BASE_URL}/public/imported/clubhouse-neoclassical.webp",
            "title": "50,000 Sq.Ft. Neoclassical Clubhouse and 52+ Luxury Amenities",
            "caption": "Olympic lap pool, equestrian academy, Roman amphitheatre, sports arenas, and wellness spas"
        }
    },
    {
        "url": f"{BASE_URL}/nri",
        "changefreq": "weekly",
        "priority": "0.90",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
            "title": "NRI Real Estate Investment Desk: Dubai, USA, Singapore, UK",
            "caption": "FEMA-compliant property investment, virtual 4K walkthroughs, NRE/NRO repatriation, and turnkey tenancy management"
        }
    },
    {
        "url": f"{BASE_URL}/connectivity",
        "changefreq": "weekly",
        "priority": "0.90",
        "image": {
            "loc": f"{BASE_URL}/public/imported/proximity-to-pune-mumbai.webp",
            "title": "Strategic Transit Connectivity: Expressway, Metro Line 3, Ring Road",
            "caption": "Signal-free access to Hinjewadi IT Park, Mumbai-Pune Expressway (5 mins), and upcoming PMRDA 128m Ring Road"
        }
    },
    {
        "url": f"{BASE_URL}/compare",
        "changefreq": "weekly",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/gallery/gallery_living_hq.webp",
            "title": "Krisala Hiranandani vs Pune West Real Estate Benchmarks",
            "caption": "Comprehensive comparison with Godrej River Royale, VTP Earth One, Lodha Sylvan, and Kolte Patil Life Republic"
        }
    },
    {
        "url": f"{BASE_URL}/everlyn",
        "changefreq": "weekly",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_exterior.webp",
            "title": "Everlyn Residences at Krisala Hiranandani",
            "caption": "Sector Arcadia and Sector Icon high-rise residences with wellness amenities and lakefront nature trails"
        }
    },
    {
        "url": f"{BASE_URL}/gallery",
        "changefreq": "weekly",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/gallery/gallery_living_hq.webp",
            "title": "4K Architectural Gallery & Drone Tour",
            "caption": "High-definition photography and architectural renderings of interiors, neoclassical facades, and landscaping"
        }
    },
    {
        "url": f"{BASE_URL}/neighborhood",
        "changefreq": "weekly",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/imported/proximity-to-pune-mumbai.webp",
            "title": "Hinjewadi & Mahalunge Strategic Neighborhood Location Map",
            "caption": "Interactive location map and social infrastructure including schools, multi-specialty hospitals, and tech parks"
        }
    },
    {
        "url": f"{BASE_URL}/knowledge-hub",
        "changefreq": "daily",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
            "title": "Krisala Hiranandani Knowledge Hub Research & Insights",
            "caption": "Comprehensive macroeconomic, infrastructure, rental yield, and MahaRERA real estate research reports"
        }
    },
    {
        "url": f"{BASE_URL}/blog",
        "changefreq": "daily",
        "priority": "0.85",
        "image": {
            "loc": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
            "title": "Pune Real Estate Insights & Market Trends Blog",
            "caption": "Hinjewadi, Mahalunge, Baner, and Wakad residential property analysis and pricing trends"
        }
    },
    {
        "url": f"{BASE_URL}/privacy-policy",
        "changefreq": "monthly",
        "priority": "0.50",
        "image": None
    }
]

# Tier-1 Strategic Programmatic Corridors to feature directly in Main Sitemap (sitemap.xml)
TIER1_PROGRAMMATIC_CORRIDORS = [
    # Flagship Enclaves & Projects
    ("the-colosseum", "The Colosseum Phase 4 Pre-Launch Residences", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.90"),
    ("sector-icon", "Sector Icon Ultra-Luxury Flagship Residences & Duplexes", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.90"),
    ("sector-arcadia", "Sector Arcadia Neoclassical Towers 2 & 3 BHK", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.90"),
    ("della-equestrian", "The Della Collection 8-Acre Private Racecourse & Polo Club", "https://krisalahiranandanitownships.com/public/township_grand/della_resort_villas_equestrian_official.webp", "0.90"),
    ("sector-everlyn", "Sector Everlyn Lakefront Nature Residences", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("everland", "Hiranandani Everland & Everlyn Flagship Precinct", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("kasarsai-dam", "Kasarsai Dam & Scenic Eco Waterfront Horizon", "https://krisalahiranandanitownships.com/public/township_grand/township_aerial_birds_eye_master_view.webp", "0.80"),
    ("metro-line-3-depot", "Pune Metro Line 3 Megapolis Station Feeder", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),

    # Unit Configurations
    ("2-bhk", "2 BHK Luxury Neoclassical Apartments Hinjewadi Pune", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.90"),
    ("3-bhk", "3 BHK Grande & Royale Residences Hinjewadi Pune", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.90"),
    ("4-bhk", "4 BHK Palatial Presidential Suites Hinjewadi Pune", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.90"),
    ("5-bhk", "5 BHK Imperial Signature Penthouses Hinjewadi Pune", "https://krisalahiranandanitownships.com/public/icon_official/icon_floating_deck_clubhouse_facade.webp", "0.85"),
    ("duplex", "Presidential Sky Duplex Penthouses 18ft Ceilings Hinjewadi", "https://krisalahiranandanitownships.com/public/icon_official/icon_floating_deck_clubhouse_facade.webp", "0.85"),
    ("simplex", "Simplex Executive Luxury Suites Hinjewadi Pune", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("della-plots", "The Della Collection Equestrian Villa Plots Hinjewadi", "https://krisalahiranandanitownships.com/public/township_grand/della_resort_villas_equestrian_official.webp", "0.90"),

    # High-Intent IT Hub Commute Corridors
    ("apartments-near-infosys-hinjewadi", "Apartments Near Infosys Hinjewadi Phase 1 & 2", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-wipro-circle-hinjewadi", "Apartments Near Wipro Circle Hinjewadi Phase 1", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-tcs-sahyadri-park-hinjewadi", "Apartments Near TCS Sahyadri Park Hinjewadi Phase 3", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-cognizant-hinjewadi", "Apartments Near Cognizant Hinjewadi Phase 3", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-barclays-hinjewadi", "Apartments Near Barclays Global Service Centre Hinjewadi", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-tech-mahindra-hinjewadi", "Apartments Near Tech Mahindra Hinjewadi Phase 3", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-capgemini-hinjewadi", "Apartments Near Capgemini Hinjewadi Phase 2", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-quadron-business-park", "Apartments Near Quadron Business Park Hinjewadi", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-embassy-tech-zone", "Apartments Near Embassy Tech Zone Hinjewadi Phase 2", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),

    # High-Intent Transit & Arterial Corridors
    ("apartments-near-mumbai-pune-expressway", "Apartments Near Mumbai Pune Expressway Toll Plaza", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-hinjewadi-metro-line-3", "Apartments Near Hinjewadi Metro Line 3 Station", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-pmrda-ring-road", "Apartments Near Proposed PMRDA 128m Ring Road Junction", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-mahalunge-hinjewadi-bridge", "Apartments Near Maan-Mahalunge Hinjewadi Link Road", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),
    ("apartments-near-pune-international-airport", "Township Commute to Pune International Airport", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.80"),
    ("apartments-near-darumbre-interchange", "Apartments in Darumbre North Hinjewadi Interchange", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.85"),

    # Strategic Micro-Market Corridors
    ("luxury-apartments-in-hinjewadi-phase-1", "Luxury Apartments in Hinjewadi Phase 1 Pune", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("luxury-apartments-in-hinjewadi-phase-2", "Luxury Apartments in Hinjewadi Phase 2 Pune", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("luxury-apartments-in-hinjewadi-phase-3", "Luxury Apartments in Hinjewadi Phase 3 Pune", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.85"),
    ("luxury-apartments-in-north-hinjewadi", "Luxury Apartments in North Hinjewadi Darumbre", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("luxury-apartments-in-mahalunge-smart-city", "Luxury Apartments in Mahalunge Hi-Tech Smart City", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("luxury-apartments-in-marunji-darumbre", "Luxury Apartments in Marunji & Darumbre Corridor", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("luxury-apartments-in-wakad-extension", "Luxury Apartments in Wakad Extension Pune", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.85"),
    ("luxury-apartments-in-baner-balewadi-belt", "Township Residences Near Baner Balewadi Belt", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.85"),
    ("luxury-apartments-in-punawale-annexe", "Luxury Apartments in Punawale & Marunji Annexe", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("luxury-apartments-in-tathawade-corridor", "Luxury Apartments Near Tathawade Education Hub", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),

    # Competitor Comparison Portals
    ("vs-godrej-river-royale-mahalunge", "Krisala Hiranandani vs Godrej River Royale Mahalunge", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.85"),
    ("vs-vtp-earth-one-mahalunge", "Krisala Hiranandani vs VTP Earth One Mahalunge", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.85"),
    ("vs-lodha-sylvan-hinjewadi", "Krisala Hiranandani vs Lodha Sylvan Hinjewadi", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.85"),
    ("vs-kolte-patil-life-republic", "Krisala Hiranandani vs Kolte Patil Life Republic", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.85"),
    ("vs-shapoorji-joyville-hinjewadi", "Krisala Hiranandani vs Shapoorji Pallonji Joyville", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.85"),

    # Strategic USPs & Key Specifications
    ("della-8-acre-private-racecourse", "8-Acre Private Racecourse & Equestrian Polo Club Hinjewadi", "https://krisalahiranandanitownships.com/public/imported/della-racecource.webp", "0.85"),
    ("50000-sqft-neoclassical-clubhouse", "50,000 Sq.Ft. Neoclassical Clubhouse & Sports Amenities", "https://krisalahiranandanitownships.com/public/imported/clubhouse-neoclassical.webp", "0.85"),
    ("teri-50-year-water-green-rating", "TERI 50-Year Water Certification & IGBC Platinum Living", "https://krisalahiranandanitownships.com/public/imported/TERI-50-Year-Logo-Horizontal-Orientation.webp", "0.85"),
    ("mivan-aluminium-formwork-engineering", "Mivan Aluminium Formwork Engineering & Shear Wall Structure", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.85"),
    ("maharera-registration-pr1260002502438", "MahaRERA Registration PR1260002502438 Legal Verification", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("nri-real-estate-investment-pune", "NRI Real Estate Investment Guide Pune FEMA Compliance", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("price-list-2026", "Verified 2026 Price List & All-Inclusive Cost Sheets", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("construction-linked-payment-plan", "Construction Linked Payment Plan (CLP) & Bank Offers", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.85"),
    ("gross-rental-yield-analysis", "Gross Rental Yield & IT Tenant Demand Forecast 2026-2035", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.85"),
    ("the-colosseum-diwali-pre-launch", "Codename The Colosseum Diwali Early Bird Pre-Launch Offer", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.90")
]


def generate_main_sitemap():
    """Generates the primary sitemap.xml with Core Pages + Tier-1 Strategic Corridors with Google Image tags."""
    today_iso = datetime.now().strftime("%Y-%m-%dT00:00:00+00:00")
    
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    ET.register_namespace('image', 'http://www.google.com/schemas/sitemap-image/1.1')

    root = ET.Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")

    # Add core static pages
    for page in CORE_STATIC_PAGES:
        url_elem = ET.SubElement(root, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        loc_elem = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        loc_elem.text = page["url"]
        lastmod = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
        lastmod.text = today_iso
        changefreq = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq")
        changefreq.text = page["changefreq"]
        priority = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}priority")
        priority.text = page["priority"]

        if page.get("image"):
            img = page["image"]
            img_elem = ET.SubElement(url_elem, "{http://www.google.com/schemas/sitemap-image/1.1}image")
            img_loc = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}loc")
            img_loc.text = img["loc"]
            img_title = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}title")
            img_title.text = img["title"]
            img_cap = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}caption")
            img_cap.text = img["caption"]

    # Add Tier-1 Strategic Programmatic Corridors
    for slug, title, img_url, prio in TIER1_PROGRAMMATIC_CORRIDORS:
        url_elem = ET.SubElement(root, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        loc_elem = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        loc_elem.text = f"{BASE_URL}/explore/{slug}"
        lastmod = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
        lastmod.text = today_iso
        changefreq = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}changefreq")
        changefreq.text = "weekly"
        priority = ET.SubElement(url_elem, "{http://www.sitemaps.org/schemas/sitemap/0.9}priority")
        priority.text = prio

        img_elem = ET.SubElement(url_elem, "{http://www.google.com/schemas/sitemap-image/1.1}image")
        img_loc = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}loc")
        img_loc.text = img_url
        img_title = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}title")
        img_title.text = f"{title} | Krisala Hiranandani"
        img_cap = ET.SubElement(img_elem, "{http://www.google.com/schemas/sitemap-image/1.1}caption")
        img_cap.text = f"Official verified guide and specifications for {title} at Krisala Hiranandani Township Hinjewadi, Pune"

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
    full_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>\n{xml_str}'

    with open(MAIN_SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(full_xml)

    public_main = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(public_main, "w", encoding="utf-8") as f:
        f.write(full_xml)

    total_main = len(CORE_STATIC_PAGES) + len(TIER1_PROGRAMMATIC_CORRIDORS)
    print(f"  [✓] Main Sitemap (sitemap.xml): {total_main} URLs generated with Google Image Annotations.")


def generate_sharded_sitemaps():
    """Generates the 15 programmatic sub-sitemaps (15,000 URLs) and Master Index."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    sub_sitemaps = []
    total_urls = 0

    print("=" * 65)
    print("Generating 15,000 Programmatic URLs Across 15 Sharded Sitemaps...")
    print("=" * 65)

    for silo in SILOS:
        filename = silo["file"]
        root_filepath = os.path.join(ROOT_DIR, filename)
        public_filepath = os.path.join(OUTPUT_DIR, filename)
        silo_urls = []

        # Add canonical parent hubs at top if present
        hubs = silo.get("hubs", [])
        for hub in hubs:
            silo_urls.append((f"{BASE_URL}{hub}", "daily", "0.95"))

        # Generate exactly 1,000 programmatic combinations: 5 bases * 10 modifiers * 20 localities = 1,000
        for b in silo["bases"]:
            for m in silo["modifiers"]:
                for loc in silo["localities"]:
                    slug = f"krisala-hiranandani-{b}-{m}-{loc}"
                    url = f"{BASE_URL}/explore/{slug}"
                    silo_urls.append((url, "weekly", "0.80"))

        # Build XML
        root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        for u, freq, prio in silo_urls:
            url_elem = ET.SubElement(root, "url")
            loc_elem = ET.SubElement(url_elem, "loc")
            loc_elem.text = u
            lastmod = ET.SubElement(url_elem, "lastmod")
            lastmod.text = today
            changefreq = ET.SubElement(url_elem, "changefreq")
            changefreq.text = freq
            priority = ET.SubElement(url_elem, "priority")
            priority.text = prio

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

        print(f"  [✓] {filename}: {len(silo_urls)} URLs generated")
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

    # Include all 15 sharded programmatic sitemaps (all at root domain level)
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

    public_index = os.path.join(OUTPUT_DIR, "sitemap-index.xml")
    with open(public_index, "w", encoding="utf-8") as f:
        f.write(full_index_xml)

    print(f"\n[✓] Master Sitemap Index generated: {INDEX_PATH}")
    print(f"    Referencing 3 core sitemaps + 15 programmatic sub-sitemaps ({total_urls} programmatic URLs)")
    print("=" * 65)


if __name__ == "__main__":
    generate_main_sitemap()
    generate_sharded_sitemaps()

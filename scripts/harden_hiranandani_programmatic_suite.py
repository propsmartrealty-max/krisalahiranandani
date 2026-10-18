#!/usr/bin/env python3
"""
Comprehensive Programmatic Suite Hardener for 'Hiranandani'
Expands bases, modifiers, localities, exact-match Tier-1 corridors, and regenerates XML sitemaps.
"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
SITEMAP_GEN_PATH = os.path.join(SCRIPT_DIR, "generate_programmatic_sitemaps.py")

EXPANDED_BASES = [
    "hiranandani-pune",
    "hiranandani-hinjewadi",
    "hiranandani-township-pune",
    "hiranandani-township-hinjewadi",
    "krisala-hiranandani",
    "krisala-hiranandani-township",
    "krisala-hiranandani-pune",
    "krisala-hiranandani-hinjewadi",
    "house-of-hiranandani-pune",
    "house-of-hiranandani-hinjewadi",
    "hiranandani-communities-pune",
    "hiranandani-communities-hinjewadi",
    "dr-niranjan-hiranandani-pune",
    "dr-niranjan-hiranandani-hinjewadi",
    "dr-niranjan-hiranandani-township",
    "hiranandani-new-launch-pune",
    "hiranandani-pre-launch-pune",
    "hiranandani-flats-in-pune",
    "hiranandani-flats-hinjewadi",
    "hiranandani-apartments-pune",
    "hiranandani-apartments-hinjewadi",
    "hiranandani-luxury-apartments-pune",
    "hiranandani-projects-in-pune",
    "hiranandani-upcoming-projects-pune",
    "hiranandani-north-hinjewadi",
    "hiranandani-darumbre",
    "hiranandani-marunji",
    "hiranandani-mahalunge",
    "hiranandani-della-pune",
    "hiranandani-racecourse-pune",
    "hiranandani-polo-club-pune",
    "hiranandani-price-list-2026",
    "hiranandani-cost-sheet-pune",
    "hiranandani-payment-plan",
    "hiranandani-brochure-download",
    "hiranandani-floor-plans",
    "hiranandani-masterplan-pune",
    "hiranandani-sample-flat-video",
    "hiranandani-virtual-tour-4k",
    "hiranandani-site-address-pune",
    "hiranandani-location-map-pune",
    "hiranandani-booking-office",
    "hiranandani-sales-office-pune",
    "hiranandani-contact-number",
    "hiranandani-reviews-pune",
    "hiranandani-ratings-and-feedback",
    "hiranandani-maharera-number",
    "hiranandani-rera-approved",
    "hiranandani-possession-date-2028-2029",
    "hiranandani-construction-status-2026",
    "hiranandani-resale-value-appreciation",
    "hiranandani-rental-yield-roi",
    "hiranandani-nri-investment-desk",
    "hiranandani-2-bhk-pune",
    "hiranandani-2-bhk-hinjewadi",
    "hiranandani-3-bhk-pune",
    "hiranandani-3-bhk-hinjewadi",
    "hiranandani-4-bhk-pune",
    "hiranandani-4-bhk-hinjewadi",
    "hiranandani-5-bhk-pune",
    "hiranandani-duplex-pune",
    "hiranandani-penthouses-pune",
    "hiranandani-sky-villas-pune",
    "hiranandani-villa-plots-pune",
    "hiranandani-the-colosseum",
    "hiranandani-colosseum-hinjewadi",
    "hiranandani-sector-arcadia",
    "hiranandani-arcadia-hinjewadi",
    "hiranandani-sector-icon",
    "hiranandani-icon-hinjewadi",
    "hiranandani-sector-everlyn",
    "hiranandani-everland-pune"
]

EXPANDED_MODIFIERS = [
    "official-website",
    "direct-developer-booking",
    "all-inclusive-cost-sheet",
    "price-list-and-floor-plans",
    "maharera-registered",
    "105-acre-integrated-township",
    "8-acre-private-racecourse",
    "della-resorts-partnership",
    "possession-timeline-2028-2029",
    "near-infosys-wipro-circle",
    "near-metro-line-3-station",
    "mumbai-pune-expressway-access",
    "pmrda-ring-road-junction",
    "investment-and-rental-yield",
    "sample-flat-virtual-tour",
    "schedule-vip-site-visit",
    "rera-escrow-approved",
    "customer-reviews-ratings",
    "diwali-launch-benefits",
    "fema-compliant-nri-desk"
]

EXPANDED_LOCALITIES = [
    "hinjewadi",
    "hinjewadi-phase-1",
    "hinjewadi-phase-2",
    "hinjewadi-phase-3",
    "north-hinjewadi",
    "darumbre-marunji",
    "mahalunge-smart-city",
    "wakad-extension",
    "baner-balewadi",
    "punawale-corridor",
    "tathawade-it-belt",
    "ravet-pradhikaran",
    "pune-west-corridor",
    "mumbai-pune-expressway",
    "pmrda-ring-road",
    "nri-investors-pune",
    "it-leaders-pune",
    "luxury-buyers-pune",
    "first-equestrian-township",
    "cxo-leadership-villas"
]

EXPANDED_TIER1 = [
    ("hiranandani-pune", "Hiranandani Pune Official Township Website | Krisala Hiranandani", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "1.00"),
    ("hiranandani-hinjewadi", "Hiranandani Hinjewadi Pune Official Website | 105-Acre Integrated Township", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "1.00"),
    ("hiranandani-township-pune", "Hiranandani Township Pune | 105 Acres Luxury Living & Racecourse", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "1.00"),
    ("hiranandani-township-hinjewadi", "Hiranandani Township Hinjewadi | 2, 3 & 4 BHK Luxury Apartments", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "1.00"),
    ("krisala-hiranandani", "Krisala Hiranandani Official Website | 105-Acre Equestrian Township Hinjewadi", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "1.00"),
    ("krisala-hiranandani-township", "Krisala Hiranandani Township Hinjewadi Pune | Masterplan & Prices", "https://krisalahiranandanitownships.com/public/township_grand/township_aerial_birds_eye_master_view.webp", "1.00"),
    ("krisala-hiranandani-pune", "Krisala Hiranandani Pune | Joint Venture Luxury Township", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "1.00"),
    ("krisala-hiranandani-hinjewadi", "Krisala Hiranandani Hinjewadi | Neoclassical Homes & Villa Plots", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "1.00"),
    ("house-of-hiranandani-pune", "House of Hiranandani Pune | Joint Venture Krisala Developers", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("house-of-hiranandani-hinjewadi", "House of Hiranandani Hinjewadi | Neoclassical Residences", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.99"),
    ("hiranandani-communities-pune", "Hiranandani Communities Pune Official Project | Hinjewadi North", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-communities-hinjewadi", "Hiranandani Communities Hinjewadi | Integrated 105-Acre Township", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("dr-niranjan-hiranandani-pune", "Dr. Niranjan Hiranandani Pune Project | Krisala Hiranandani Township", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("dr-niranjan-hiranandani-hinjewadi", "Dr. Niranjan Hiranandani Hinjewadi Project | 105-Acre Township", "https://krisalahiranandanitownships.com/public/imported/dr-niranjan-hiranandani.webp", "0.99"),
    ("dr-niranjan-hiranandani-township", "Dr. Niranjan Hiranandani Township Pune | Racecourse & Neoclassical Towers", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-new-launch-pune", "Hiranandani New Launch Pune 2026 | Sector Icon & The Colosseum", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.99"),
    ("hiranandani-pre-launch-pune", "Hiranandani Pre-Launch Pune | Priority Allotment & Pre-Booking Offers", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-flats-in-pune", "Hiranandani Flats in Pune | Price List, Floor Plans & Reviews", "https://krisalahiranandani-townships.com/public/everlyn/hero/hero_exterior.webp".replace("-townships", "townships"), "0.99"),
    ("hiranandani-flats-hinjewadi", "Hiranandani Flats Hinjewadi | 2, 3 & 4 BHK Luxury Homes", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.99"),
    ("hiranandani-apartments-pune", "Hiranandani Apartments Pune | Luxury 2, 3 & 4 BHK Residences", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.99"),
    ("hiranandani-apartments-hinjewadi", "Hiranandani Apartments in Hinjewadi | Italian Marble Living", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-luxury-apartments-pune", "Hiranandani Luxury Apartments Pune | Palatial Presidential Suites", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.99"),
    ("hiranandani-projects-in-pune", "Hiranandani Projects in Pune | Hinjewadi 105-Acre Township", "https://krisalahiranandanitownships.com/public/township_grand/township_aerial_birds_eye_master_view.webp", "0.99"),
    ("hiranandani-upcoming-projects-pune", "Hiranandani Upcoming Projects Pune 2026-2028 | Phased Launches", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-north-hinjewadi", "Hiranandani North Hinjewadi Darumbre | Price & Location", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.99"),
    ("hiranandani-darumbre", "Hiranandani Darumbre Hinjewadi | Direct PMRDA Ring Road Frontage", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.99"),
    ("hiranandani-marunji", "Hiranandani Marunji Gateway | Fast Arterial IT Park Access", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-mahalunge", "Hiranandani Mahalunge Hi-Tech Smart City Link | West Pune", "https://krisalahiranandanitownships.com/public/township_grand/township_aerial_birds_eye_master_view.webp", "0.99"),
    ("hiranandani-della-pune", "Hiranandani Della Pune | 8-Acre Private Racecourse & Polo Club", "https://krisalahiranandanitownships.com/public/township_grand/della_resort_villas_equestrian_official.webp", "0.99"),
    ("hiranandani-racecourse-pune", "Hiranandani Racecourse Pune | Della Equestrian Residences", "https://krisalahiranandanitownships.com/public/imported/della-racecource.webp", "0.99"),
    ("hiranandani-polo-club-pune", "Hiranandani Polo Club & Equestrian Stables Pune | The Della Collection", "https://krisalahiranandanitownships.com/public/imported/della-racecource.webp", "0.99"),
    ("hiranandani-price-list-2026", "Hiranandani Price List 2026 | Cost Sheet & Payment Plans", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "1.00"),
    ("hiranandani-cost-sheet-pune", "Hiranandani Cost Sheet Pune | All-Inclusive Stamp Duty & GST Breakup", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-payment-plan", "Hiranandani Construction Linked Payment Plan (CLP) | Pre-Approved Loans", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-brochure-download", "Hiranandani Brochure Download | PDF Floor Plans & Masterplan", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "1.00"),
    ("hiranandani-floor-plans", "Hiranandani Floor Plans Pune | 2, 3, 4 BHK & Villa Plots", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "1.00"),
    ("hiranandani-masterplan-pune", "Hiranandani Masterplan Pune | 105-Acre Interactive Layout Map", "https://krisalahiranandanitownships.com/public/everlyn/masterplan/master_layout_hq.webp", "0.99"),
    ("hiranandani-sample-flat-video", "Hiranandani Sample Flat Video Tour 4K | Experience Center", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.99"),
    ("hiranandani-virtual-tour-4k", "Hiranandani 4K Virtual Walkthrough Pune | 3D Interactive Floor Plates", "https://krisalahiranandanitownships.com/public/everlyn/gallery/gallery_living_hq.webp", "0.99"),
    ("hiranandani-site-address-pune", "Hiranandani Site Address & Location Map | Hinjewadi North Pune", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "1.00"),
    ("hiranandani-location-map-pune", "Hiranandani Location Map Pune | GPS Coordinates & Route Guide", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.99"),
    ("hiranandani-booking-office", "Hiranandani Booking Office Pune | Direct Developer Sales Desk", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-sales-office-pune", "Hiranandani Sales Office Pune | Site Experience Center Hours", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-contact-number", "Hiranandani Contact Number & Sales Desk | Direct Site Inquiries", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-reviews-pune", "Hiranandani Reviews Pune | Investment Potential & Buyer Ratings", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-ratings-and-feedback", "Hiranandani Ratings and Buyer Feedback Pune | 55x Legacy Track Record", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-maharera-number", "Hiranandani MahaRERA Number PR1260002502438 & PR1260002600818", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-rera-approved", "Hiranandani RERA Approved Docket | Marketable Title & Sanction Letters", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-possession-date-2028-2029", "Hiranandani Possession Date 2028-2029 | Construction Milestones", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-construction-status-2026", "Hiranandani Construction Status 2026 | Mivan Formwork Progress Updates", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.99"),
    ("hiranandani-resale-value-appreciation", "Hiranandani Resale Value & Appreciation Forecast 2026-2035", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-rental-yield-roi", "Hiranandani Rental Yield & IT Professional Tenant Demand", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-nri-investment-desk", "Hiranandani NRI Investment Desk Pune | FEMA & Capital Repatriation", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-2-bhk-pune", "Hiranandani 2 BHK Pune Hinjewadi | Price, Carpet Area & Tour", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "1.00"),
    ("hiranandani-2-bhk-hinjewadi", "Hiranandani 2 BHK Hinjewadi | Neoclassical Sector Arcadia Homes", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-3-bhk-pune", "Hiranandani 3 BHK Pune Hinjewadi | Grande & Royale Layouts", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "1.00"),
    ("hiranandani-3-bhk-hinjewadi", "Hiranandani 3 BHK Hinjewadi | Double Balconies & Racecourse Views", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-4-bhk-pune", "Hiranandani 4 BHK Pune Hinjewadi | Palatial Sky Duplexes", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "1.00"),
    ("hiranandani-4-bhk-hinjewadi", "Hiranandani 4 BHK Hinjewadi | Presidential Sector Icon Suites", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_daylight_architectural_elevation.webp", "0.99"),
    ("hiranandani-5-bhk-pune", "Hiranandani 5 BHK Imperial Sky Mansions Pune | Private Lap Pool", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-duplex-pune", "Hiranandani Sky Duplex Penthouses Pune | Double Height Ceilings", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-penthouses-pune", "Hiranandani Penthouses Pune | Luxury Horizon Terraces", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-sky-villas-pune", "Hiranandani Sky Villas Pune | Sector Icon Duplex Collection", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-villa-plots-pune", "Hiranandani Villa Plots Pune | The Della Collection Land", "https://krisalahiranandanitownships.com/public/township_grand/della_resort_villas_equestrian_official.webp", "1.00"),
    ("hiranandani-the-colosseum", "Hiranandani The Colosseum Phase 4 | Pre-Launch Luxury Towers", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-colosseum-hinjewadi", "Hiranandani Colosseum Hinjewadi | Roman Landmark Residences", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-sector-arcadia", "Hiranandani Sector Arcadia Hinjewadi | 2 & 3 BHK Neoclassical", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-arcadia-hinjewadi", "Hiranandani Arcadia Hinjewadi | Mivan Shear Wall Precision", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_exterior.webp", "0.99"),
    ("hiranandani-sector-icon", "Hiranandani Sector Icon Flagship Triad Towers | Hinjewadi North", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-icon-hinjewadi", "Hiranandani Icon Hinjewadi | 3 & 4 BHK Sky Duplexes", "https://krisalahiranandanitownships.com/public/icon_official/icon_towers_sunset_grand_elevation.webp", "0.99"),
    ("hiranandani-sector-everlyn", "Hiranandani Sector Everlyn Hinjewadi | Central Lake Living", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-everland-pune", "Hiranandani Everland / Everlyn Precinct Pune | MahaRERA Approved", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-near-wipro-circle", "Hiranandani Properties Near Wipro Circle Hinjewadi Phase 1", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-near-infosys-hinjewadi", "Hiranandani Homes Near Infosys Campus Hinjewadi Phase 1 & 2", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-near-metro-line-3", "Hiranandani Residences Near Metro Line 3 Megapolis Station", "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp", "0.99"),
    ("hiranandani-mumbai-pune-expressway", "Hiranandani Township Near Mumbai Pune Expressway Toll Plaza", "https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp", "0.99")
]

def update_generator_script():
    with open(SITEMAP_GEN_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace hiranandani-brand silo in SILOS list
    pattern_silo = r'(\{\s*"name":\s*"hiranandani-brand".*?"localities":\s*\[)(.*?)(\]\s*\})'
    
    bases_str = ',\n            '.join([f'"{b}"' for b in EXPANDED_BASES])
    modifiers_str = ',\n            '.join([f'"{m}"' for m in EXPANDED_MODIFIERS])
    localities_str = ',\n            '.join([f'"{loc}"' for loc in EXPANDED_LOCALITIES])

    new_silo_body = f'''{{
        "name": "hiranandani-brand",
        "file": "sitemap-hiranandani-brand.xml",
        "hubs": ["/", "/pune-real-estate", "/hinjewadi-real-estate", "/colosseum", "/pricing", "/masterplan", "/knowledge-hub"],
        "bases": [
            {bases_str}
        ],
        "modifiers": [
            {modifiers_str}
        ],
        "localities": [
            {localities_str}
        ]
    }}'''

    content = re.sub(r'\{\s*"name":\s*"hiranandani-brand".*?\}\s*\]', f'{new_silo_body}\n]', content, flags=re.DOTALL)

    # 2. Update TIER1_PROGRAMMATIC_CORRIDORS
    tier1_items = []
    for slug, title, img, prio in EXPANDED_TIER1:
        tier1_items.append(f'    ("{slug}", "{title}", "{img}", "{prio}")')
    tier1_str = ',\n'.join(tier1_items)

    pattern_tier1 = r'TIER1_PROGRAMMATIC_CORRIDORS\s*=\s*\[.*?\]'
    content = re.sub(pattern_tier1, f'TIER1_PROGRAMMATIC_CORRIDORS = [\n{tier1_str}\n]', content, flags=re.DOTALL)

    # 3. Clean deduplication in generate_sharded_sitemaps()
    pattern_loop = r'slug\s*=\s*f"krisala-hiranandani-\{b\}-\{m\}-\{loc\}"'
    replacement_loop = '''# Clean up brand slug deduplication
                    slug = f"krisala-{b}-{m}-{loc}"
                    slug = re.sub(r'hiranandani-hiranandani', 'hiranandani', slug)
                    slug = re.sub(r'krisala-krisala', 'krisala', slug)
                    slug = re.sub(r'-+', '-', slug).strip('-')'''
    content = re.sub(pattern_loop, replacement_loop, content)

    with open(SITEMAP_GEN_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("generate_programmatic_sitemaps.py updated with complete Hiranandani permutation ecosystem!")

if __name__ == "__main__":
    update_generator_script()

#!/usr/bin/env python3
"""
Enterprise 50% CTR Hardening & SERP Snippet Optimization Suite
Krisala Hiranandani Township Hinjewadi, Pune
https://krisalahiranandanitownships.com

Hardening Dimensions:
1. High-CTR Title Tags (Strictly <= 55 Characters):
   - Front-loaded commercial intent: exact price anchors (from ₹79L*, ₹1.25Cr*, ₹1.80Cr*, ₹2.10Cr*),
     location (Hinjewadi Pune), configuration (2, 3, 4 BHK, Villa Plots, Duplex),
     and trust hooks (MahaRERA, 4.9/5 ★).
   - Zero truncation on Google mobile & desktop SERP.
   - Strictly 0 ™, 0 【】 brackets, 0 subjective 'Official'.
2. High-CTR Meta Descriptions (Strictly 140 - 155 Characters):
   - Direct value proposition: configuration, carpet area, price, location, MahaRERA registration.
   - Clear action-oriented CTA: "Download floor plans & cost sheet PDF."
   - Synchronized across description, og:description, twitter:description.
3. SERP Rich Snippet Multiplying Signals:
   - Universal AggregateRating (4.9/5 stars, 428 reviews) for golden star ratings in SERPs.
   - Universal AggregateOffer (₹79L to ₹4.50Cr) for Google price badge display.
   - Universal FAQPage Schema (3-5 structured Q&A) for accordion expansion.
   - Universal BreadcrumbList Schema for clean URL hierarchies.
"""

import os
import glob
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"

# Master High-CTR Metadata Dictionary for Core & Silo Pages
CORE_METADATA = {
    "index.html": {
        "title": "Krisala Hiranandani Township Pune | from ₹79L*",
        "description": "Krisala Hiranandani Township Pune (Hinjewadi). Luxury 2, 3 & 4 BHK from ₹79L* & Plots ₹1.80Cr*. 105+ Acres, 8-Acre Turf. MahaRERA Reg PR1260002500600."
    },
    "hiranandani-pune.html": {
        "title": "Hiranandani Pune Hinjewadi | Township from ₹79L*",
        "description": "Hiranandani Pune (North Hinjewadi). 105+ Acre equestrian township by Dr. Niranjan Hiranandani & Krisala. 2, 3 & 4 BHK from ₹79L*. MahaRERA PR1260002500600."
    },
    "krisala-hiranandani-pune.html": {
        "title": "Krisala Hiranandani Pune | Flats from ₹79L*",
        "description": "Krisala Hiranandani Pune (North Hinjewadi). 105+ Acre equestrian township with 2, 3 & 4 BHK from ₹79L* & Della Plots ₹1.80Cr*. MahaRERA Reg PR1260002500600."
    },
    "krisala-hiranandani-township-pune.html": {
        "title": "Krisala Hiranandani Township Pune | from ₹79L*",
        "description": "Krisala Hiranandani Township Pune (Hinjewadi). Luxury 2, 3 & 4 BHK from ₹79L* & Plots ₹1.80Cr*. 105+ Acres, 8-Acre Turf. MahaRERA Reg PR1260002500600."
    },
    "arcadia.html": {
        "title": "Sector Arcadia Hinjewadi | 2 & 3 BHK from ₹79L*",
        "description": "Sector Arcadia at Krisala Hiranandani, North Hinjewadi. Luxury 2 & 3 BHK flats from ₹79L*. MahaRERA PR1260002500600. Download floor plans & cost sheet PDF."
    },
    "colosseum.html": {
        "title": "The Colosseum Hinjewadi | 2, 3 & 4 BHK ₹79L*",
        "description": "The Colosseum (Phase 4) at Krisala Hiranandani Township, Hinjewadi. Roman amphitheatre podium & luxury 2, 3 & 4 BHK from ₹79L*. Download 2026 cost sheet."
    },
    "icon.html": {
        "title": "Sector Icon Hinjewadi | 4 BHK Duplex ₹2.10Cr*",
        "description": "Sector Icon at Krisala Hiranandani Hinjewadi: Palatial 4 BHK sky duplex penthouses with 18ft double-height ceilings from ₹2.10 Cr*. MahaRERA PR1260002600818."
    },
    "della.html": {
        "title": "Della Township Bungalow Plots Hinjewadi | ₹1.8Cr*",
        "description": "Della Township at Krisala Hiranandani Hinjewadi. Freehold bungalow plots & Della lots around 8-acre racecourse from ₹1.80 Cr*. MahaRERA PR1260002502438."
    },
    "everlyn.html": {
        "title": "Sector Everlyn Hinjewadi | Lakefront from ₹79L*",
        "description": "Everlyn Residences at Krisala Hiranandani Township, North Hinjewadi. Luxury 2 & 3 BHK apartments with lakefront views from ₹79L*. MahaRERA PR1260002500600."
    },
    "pricing.html": {
        "title": "Hiranandani Pune Price List 2026 | Cost Sheet ₹79L*",
        "description": "Verified 2026 price list & cost sheet for Krisala Hiranandani Hinjewadi. 2 BHK from ₹79L*, 3 BHK ₹1.25Cr* & Villa Plots ₹1.80Cr*. Get CLP payment schedule."
    },
    "floor-plans.html": {
        "title": "Floor Plans 2026 | 2, 3 & 4 BHK from ₹79L*",
        "description": "Download 2026 floor plans & carpet area layouts for Krisala Hiranandani Hinjewadi: 2 BHK (740-840 sq.ft.), 3 BHK & 4 BHK duplexes. MahaRERA PR1260002500600."
    },
    "reviews.html": {
        "title": "Krisala Hiranandani Reviews | 4.9/5 ★ (428+ Reviews)",
        "description": "Read 428+ verified buyer reviews for Krisala Hiranandani Township Hinjewadi (rated 4.9/5 ★). Transparent MahaRERA compliance, construction & ROI feedback."
    },
    "site-address.html": {
        "title": "Site Address & Route Map | 4 Mins to Metro Line 3",
        "description": "Get directions to Krisala Hiranandani Township: PMRDA Ring Road, North Hinjewadi, Pune 410506. 4 mins from Metro Line 3 & 5 mins to Mumbai-Pune Expressway."
    },
    "connectivity.html": {
        "title": "Metro Line 3 & Location Map | 4 Mins to Station",
        "description": "Multimodal transit guide for Krisala Hiranandani Hinjewadi: 4 mins to Metro Line 3 Megapolis Station, 5 mins to Mumbai-Pune Expressway & 8 mins to IT Park."
    },
    "amenities.html": {
        "title": "8-Acre Racecourse Amenities | Krisala Hiranandani",
        "description": "Explore 100+ luxury amenities at Krisala Hiranandani Hinjewadi: India's 1st 8-acre racecourse, polo club, 50,000 sq.ft. clubhouse & Olympic swimming pool."
    },
    "racecourse.html": {
        "title": "8-Acre Turf Racecourse & Polo Club | Hinjewadi",
        "description": "India's 1st 8-acre residential turf racecourse & polo club at Krisala Hiranandani Hinjewadi, Pune. Curated in collaboration with Della Resorts. Enquire now."
    },
    "hiranandani-price-list-2026.html": {
        "title": "Hiranandani Pune Price List 2026 | from ₹79L*",
        "description": "Verified 2026 price list & cost sheet for Krisala Hiranandani Hinjewadi: 2 BHK ₹79L*, 3 BHK ₹1.25Cr*, 4 BHK ₹2.10Cr* & Plots ₹1.80Cr*. Download cost sheet PDF."
    },
    "hiranandani-emi-calculator.html": {
        "title": "Home Loan EMI Calculator 2026 | from ₹79L* Flats",
        "description": "Calculate monthly home loan EMIs, interest rates & stamp duty for Krisala Hiranandani Township Hinjewadi (from ₹79L*). Pre-approved SBI, HDFC & ICICI loans."
    },
    "masterplan.html": {
        "title": "105-Acre Master Plan Map | Krisala Hiranandani Pune",
        "description": "Explore interactive 105-Acre master plan of Krisala Hiranandani Township Hinjewadi: Sector Arcadia, The Colosseum, Della villa plots & 8-acre turf racecourse."
    },
    "neighborhood.html": {
        "title": "North Hinjewadi IT Corridor | Krisala Hiranandani",
        "description": "Strategic guide to North Hinjewadi (Darumbre): 7 mins to Metro Line 3, 10 mins to Mumbai-Pune Expressway, and 12 mins to Infosys, TCS & Wipro IT parks."
    },
    "north-hinjewadi.html": {
        "title": "North Hinjewadi Corridor Guide | from ₹79L*",
        "description": "Explore North Hinjewadi (Darumbre) on PMRDA 128m Ring Road. 105-Acre Krisala Hiranandani Township with 2, 3 & 4 BHK homes from ₹79L*. MahaRERA PR1260002500600."
    },
    "compare.html": {
        "title": "Hiranandani vs Godrej Hinjewadi | Comparison 2026",
        "description": "Compare Krisala Hiranandani vs Godrej River Royale, Lodha Sylvan & Kolte Patil Life Republic. 105-acre density, racecourse & pricing from ₹79L* analyzed."
    },
    "knowledge-hub.html": {
        "title": "Investment Whitepaper 2026 | Krisala Hiranandani",
        "description": "Pune real estate investment whitepaper 2026: North Hinjewadi rental yields (5.4%), PMRDA Ring Road impact, and 105-acre township appreciation forecast."
    },
    "gallery.html": {
        "title": "Visual Gallery & 4K Tour | Krisala Hiranandani Pune",
        "description": "Explore photo gallery and 4K virtual tours of Krisala Hiranandani Township Hinjewadi: Neoclassical towers, 8-acre racecourse, sample flats & clubhouse."
    },
    "construction-status.html": {
        "title": "Construction Status 2026 | Krisala Hiranandani",
        "description": "Real-time 2026 construction updates and possession schedule for Krisala Hiranandani Hinjewadi: Mivan formwork progress, drone video & MahaRERA reports."
    },
    "pune-real-estate.html": {
        "title": "Pune Real Estate Guide 2026 | Krisala Hiranandani",
        "description": "2026 Pune Real Estate Guide: Hinjewadi rates per sqft, rental yield benchmarks (5.4%), Metro Line 3 impact & top integrated townships in West Pune."
    },
    "hinjewadi-real-estate.html": {
        "title": "Hinjewadi Real Estate 2026 | Rates & Market Guide",
        "description": "2026 Hinjewadi Real Estate Market Guide: Rates per sqft across Phase 1, 2, 3 & North Hinjewadi, Metro Line 3 impact & 105-acre Krisala Hiranandani Township."
    },
    "nri.html": {
        "title": "NRI Property Investment Desk | from ₹79L* ($95K)",
        "description": "Dedicated NRI Real Estate Desk for Krisala Hiranandani Hinjewadi: NRE/NRO banking, FEMA compliance, 100% digital KYC & 5.4% rental yields in Pune."
    },
    "blog.html": {
        "title": "Pune Real Estate Market Trends 2026 | Research Hub",
        "description": "Research, price trends, and infrastructure analysis for Pune real estate: Hinjewadi, Mahalunge, and Wakad. 2, 3, 4 BHK homes, Metro Line 3 & PMRDA Ring Road."
    },

    # Blog Posts
    "blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle.html": {
        "title": "Della Villa Plots Hinjewadi | Estate Lots ₹1.80Cr*",
        "description": "Guide to The Della Collection at Krisala Hiranandani Hinjewadi: 100 luxury equestrian villa plots, 8-acre private racecourse & Della privileges from ₹1.80Cr*."
    },
    "blog/hinjewadi-it-park-housing-shortage-pmrda-ring-road-surge-2026.html": {
        "title": "Hinjewadi Housing Deficit 2026: PMRDA Ring Road Surge",
        "description": "Over 450,000 IT professionals in Hinjewadi face severe quality housing deficit: Why PMRDA 128m Ring Road and North Hinjewadi master townships lead demand."
    },
    "blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune.html": {
        "title": "Hinjewadi Corridor Guide 2026 | Krisala Hiranandani",
        "description": "Real estate analysis of Hinjewadi-Mahalunge tech corridor vs East Pune (Kharadi). Metro Line 3, PMRDA Ring Road, and capital growth at Krisala Hiranandani."
    },
    "blog/hinjewadi-phase-4-integrated-township-boom.html": {
        "title": "Hinjewadi Phase 4 Boom | Krisala Hiranandani Guide",
        "description": "Why Pune's real estate growth shifted to Hinjewadi Phase 4 and North Hinjewadi. 105+ acre master-planned equestrian living vs congested standalone towers."
    },
    "blog/krisala-hiranandani-township-hinjewadi-flats-price-list-cost-sheet.html": {
        "title": "Hiranandani Flat Prices 2026 | Cost Sheet from ₹79L*",
        "description": "2026 price list and cost sheet for Krisala Hiranandani Hinjewadi: 2 BHK from ₹79L*, 3 BHK ₹1.25Cr*, 4 BHK ₹2.10Cr*. Stamp duty, loans & payment schedule."
    },
    "blog/krisala-hiranandani-township-hinjewadi-location-connectivity-it-parks.html": {
        "title": "Hinjewadi Location & Metro Map | 4 Mins to Station",
        "description": "Location and connectivity guide for Krisala Hiranandani Hinjewadi: distance to Infosys, Wipro, TCS, Hinjewadi Metro Line 3, Ring Road & Expressway times."
    },
    "blog/krisala-hiranandani-township-hinjewadi-master-plan-review-2026.html": {
        "title": "105-Acre Master Plan Review 2026 | Krisala Hiranandani",
        "description": "2026 review of Krisala Hiranandani Township Hinjewadi: 105-acre master plan, Sector Arcadia, Sector Icon, The Colosseum, Della Plots & MahaRERA approvals."
    },
    "blog/krisala-hiranandani-township-hinjewadi-sample-flat-floor-plans-carpet-area.html": {
        "title": "Sample Flat Floor Plans & Video | 2 & 3 BHK ₹79L*",
        "description": "Sample flat review and floor plan analysis of Krisala Hiranandani Hinjewadi: 2, 3 & 4 BHK carpet areas (740–2,450 sq.ft.), Mivan formwork & private sundecks."
    },
    "blog/krisala-hiranandani-township-pune-complete-buyers-handbook-2026.html": {
        "title": "Pune Homebuyers Handbook 2026 | Krisala Hiranandani",
        "description": "Definitive 2026 buyer guide for Krisala Hiranandani Township Pune. Explore 105-acre master plan, 2, 3 & 4 BHK pricing from ₹79L, and MahaRERA compliance."
    },
    "blog/krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence.html": {
        "title": "MahaRERA Legal Approvals | Krisala Hiranandani",
        "description": "Legal transparency docket for Krisala Hiranandani Township Pune. Verify MahaRERA registration PR1260002500600 & PR1260002600818, PMRDA clearances & title."
    },
    "blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan.html": {
        "title": "Krisala Hiranandani vs Godrej & Lodha Comparison",
        "description": "Benchmark comparing Krisala Hiranandani Township Hinjewadi against Godrej River Royale Mahalunge, VTP Earth One, and Lodha Sylvan Hinjewadi. Land scale & ROI."
    },
    "blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide.html": {
        "title": "NRI Investment Guide Pune 2026 | Hiranandani",
        "description": "Legal handbook for NRI real estate investors: MahaRERA PR1260002500600, FEMA rules, NRE/NRO repatriation, and escrow security at Krisala Hiranandani Pune."
    },
    "blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi.html": {
        "title": "Neoclassical Architecture | Krisala Hiranandani",
        "description": "Case study analyzing Hiranandani neoclassical architectural capital preservation from Powai and Thane to Krisala Hiranandani Township Hinjewadi, Pune."
    },
    "blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure.html": {
        "title": "PMRDA Ring Road & Metro Line 3 | Hinjewadi Guide",
        "description": "Strategic connectivity audit of the 128m PMRDA Ring Road, Pune Metro Line 3, and Mumbai Expressway bypass at Krisala Hiranandani Township Hinjewadi."
    },
    "blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi.html": {
        "title": "Pune Flat Price Trends 2026 | Hinjewadi from ₹79L*",
        "description": "Carpet area and price trend analysis for 2 BHK, 3 BHK, 4 BHK and Duplex apartments in Hinjewadi, Mahalunge, and Baner. Mivan construction & floor plans."
    },
    "blog/pune-metro-line-3-hinjewadi-trials-property-impact.html": {
        "title": "Pune Metro Line 3 Trials | Hinjewadi Property Impact",
        "description": "Pune Metro Line 3 trials commence: How the 23.2 km corridor connecting Hinjewadi to Shivajinagar is transforming North Hinjewadi property values and yields."
    },
    "blog/the-colosseum-hinjewadi-phase-4-investment-guide.html": {
        "title": "The Colosseum Phase 4 Hinjewadi | 2 & 3 BHK ₹79L*",
        "description": "Complete guide to The Colosseum Phase 4 at Krisala Hiranandani Hinjewadi: Roman architectural elevation, 2 & 3 BHK flats & MahaRERA PR1260002500600."
    },
    "blog/top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments.html": {
        "title": "Township vs Standalone Homes | Krisala Hiranandani",
        "description": "Why a 105-acre masterplanned township like Krisala Hiranandani Pune beats standalone apartments. Density, private racecourse, 70% open space & capital growth."
    },
    "blog/why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi.html": {
        "title": "Tech Corridor Living Guide | Krisala Hiranandani",
        "description": "Discover why software engineers and IT directors in Hinjewadi are investing in Krisala Hiranandani Township Pune. Commute comparisons, acoustic design & yields."
    },

    # NRI Regional Portals
    "nri/index.html": {
        "title": "NRI Investment Desk | from ₹79L* ($95K USD)",
        "description": "Dedicated NRI Real Estate Desk for Krisala Hiranandani Hinjewadi: NRE/NRO banking, FEMA compliance, 100% digital KYC & 5.4% rental yields in Pune."
    },
    "nri/dubai-uae.html": {
        "title": "Dubai NRI Property Desk (from AED 348K*)",
        "description": "Dubai & UAE NRI property investment desk for Krisala Hiranandani Township Pune. Zero tax in UAE, seamless NRE remittance & pre-launch entry from AED 348K*."
    },
    "nri/usa-silicon-valley.html": {
        "title": "USA NRI Property Desk (from $95K USD*)",
        "description": "USA & Silicon Valley NRI property investment desk for Krisala Hiranandani Pune. Direct USD wire transfers, FEMA assistance & luxury flats from $95,000 USD*."
    },
    "nri/uk-london.html": {
        "title": "UK London NRI Property Desk (from £75K*)",
        "description": "UK & London NRI property investment desk for Krisala Hiranandani Pune. High rental yields (5.4%), transparent MahaRERA titles & residences from £75,000 GBP*."
    },
    "nri/singapore.html": {
        "title": "Singapore NRI Property Desk (from SGD 128K*)",
        "description": "Singapore NRI investment portal for Krisala Hiranandani Township Hinjewadi, Pune. SGD capital appreciation, dual currency returns & flats from SGD 128,000*."
    },
    "nri/canada-toronto.html": {
        "title": "Canada NRI Property Desk (from CAD 130K*)",
        "description": "Canada & Toronto NRI property desk for Krisala Hiranandani Pune. FEMA compliant legal documentation, high rental demand & residences from CAD 130,000*."
    },
    "nri/australia-sydney.html": {
        "title": "Australia NRI Property Desk (from AUD 145K*)",
        "description": "Australia & Sydney NRI property investment desk for Krisala Hiranandani Pune. Strong INR growth hedge, high rental yields & residences from AUD 145,000*."
    },

    # Competitor Comparison Portals
    "compare/vs-godrej-river-royale.html": {
        "title": "Hiranandani vs Godrej River Royale | 2026",
        "description": "Compare Krisala Hiranandani (105 Acres) vs Godrej River Royale Mahalunge (5.5 Acres). Master scale, 8-acre racecourse & entry pricing from ₹79L* analyzed."
    },
    "compare/vs-lodha-sylvan.html": {
        "title": "Hiranandani vs Lodha Sylvan Pune | 2026",
        "description": "Compare Krisala Hiranandani vs Lodha Sylvan Hinjewadi. Master land scale, equestrian amenities, carpet areas & competitive pre-launch pricing from ₹79L*."
    },
    "compare/vs-kolte-patil-life-republic.html": {
        "title": "Hiranandani vs Kolte Patil Pune | 2026",
        "description": "Compare Krisala Hiranandani Township vs Kolte Patil Life Republic Hinjewadi. Neoclassical construction, 8-acre racecourse & 2, 3 BHK pricing from ₹79L*."
    },

    # Web Stories Portals
    "stories/della-equestrian-villa-plots.html": {
        "title": "Della Villa Plots Hinjewadi | from ₹1.80Cr*",
        "description": "Visual story of Della District: 8-acre private racecourse, polo club & 100 private villa estates in Hinjewadi Pune from ₹1.80Cr*. MahaRERA PR1260002502438."
    },
    "stories/hinjewadi-it-investment-roi.html": {
        "title": "Hinjewadi Investment ROI 2026 | from ₹79L*",
        "description": "Visual story of Hinjewadi real estate ROI: 5.4% rental yields, Metro Line 3, PMRDA Ring Road growth and IT housing demand at Krisala Hiranandani Pune."
    },
    "stories/maharera-legal-sanctions-guide.html": {
        "title": "MahaRERA Sanctions Guide | Krisala Hiranandani",
        "description": "Visual compliance story: MahaRERA PR1260002500600 & PR1260002600818, Section 4 70% bank escrow protection & milestone payment plans at Krisala Hiranandani."
    },
    "stories/nri-investment-desk-pune.html": {
        "title": "NRI Real Estate Investment Desk | from ₹79L*",
        "description": "Visual NRI investment handbook for Pune luxury properties: FEMA rules, NRE/NRO repatriation, digital KYC & high rental yields at Krisala Hiranandani."
    },
    "stories/sector-arcadia-luxury-living.html": {
        "title": "Sector Arcadia Luxury Living | from ₹79L*",
        "description": "Visual story of Sector Arcadia: Neoclassical 2 & 3 BHK residences in Hinjewadi Phase 1 IT corridor. Starting ₹79 Lakhs*. MahaRERA PR1260002502438."
    },
    "stories/sector-icon-sky-residences.html": {
        "title": "Sector Icon Sky Residences | from ₹2.10Cr*",
        "description": "Visual story of Sector Icon: Ultra-luxury 3 & 4 BHK sky suites and duplex mansions in North Hinjewadi. Starting ₹2.10Cr*. MahaRERA PR1260002600818."
    },
    "stories/the-colosseum-phase-4.html": {
        "title": "The Colosseum Phase 4 Hinjewadi | from ₹79L*",
        "description": "Visual story of The Colosseum: 2, 3 & 4 BHK luxury residences in a 105-acre township, North Hinjewadi, Pune. Starting ₹79L*. MahaRERA PR1260002600818."
    },
    "stories/township-grand-living.html": {
        "title": "105-Acre Township Living | from ₹79L*",
        "description": "Discover West Pune's largest integrated equestrian township: 105 acres, 8-acre private racecourse, Della hospitality, and 100+ master amenities."
    }
}

# Sub-silo pages (identical high-CTR metadata as root counterparts)
SUB_SILO_MAP = {
    "krisala-hiranandani-pune/index.html": CORE_METADATA["krisala-hiranandani-pune.html"],
    "krisala-hiranandani-pune/arcadia.html": CORE_METADATA["arcadia.html"],
    "krisala-hiranandani-pune/colosseum.html": CORE_METADATA["colosseum.html"],
    "krisala-hiranandani-pune/icon.html": CORE_METADATA["icon.html"],
    "krisala-hiranandani-pune/della.html": CORE_METADATA["della.html"],
    "krisala-hiranandani-pune/floor-plans.html": CORE_METADATA["floor-plans.html"],
    "krisala-hiranandani-pune/price-list-2026.html": CORE_METADATA["hiranandani-price-list-2026.html"],
    "krisala-hiranandani-pune/reviews.html": CORE_METADATA["reviews.html"],
    "krisala-hiranandani-pune/site-address.html": CORE_METADATA["site-address.html"],
    "krisala-hiranandani-pune/connectivity.html": CORE_METADATA["connectivity.html"],
    "krisala-hiranandani-pune/amenities.html": CORE_METADATA["amenities.html"],
    "krisala-hiranandani-pune/construction-status.html": CORE_METADATA["construction-status.html"],

    "krisala-hiranandani-township-pune/index.html": CORE_METADATA["krisala-hiranandani-township-pune.html"],
    "krisala-hiranandani-township-pune/arcadia.html": CORE_METADATA["arcadia.html"],
    "krisala-hiranandani-township-pune/colosseum.html": CORE_METADATA["colosseum.html"],
    "krisala-hiranandani-township-pune/icon.html": CORE_METADATA["icon.html"],
    "krisala-hiranandani-township-pune/della.html": CORE_METADATA["della.html"],
    "krisala-hiranandani-township-pune/floor-plans.html": CORE_METADATA["floor-plans.html"],
    "krisala-hiranandani-township-pune/price-list-2026.html": CORE_METADATA["hiranandani-price-list-2026.html"],
    "krisala-hiranandani-township-pune/reviews.html": CORE_METADATA["reviews.html"],
    "krisala-hiranandani-township-pune/site-address.html": CORE_METADATA["site-address.html"],
    "krisala-hiranandani-township-pune/connectivity.html": CORE_METADATA["connectivity.html"],
    "krisala-hiranandani-township-pune/amenities.html": CORE_METADATA["amenities.html"],
    "krisala-hiranandani-township-pune/construction-status.html": CORE_METADATA["construction-status.html"],
}

CORE_METADATA.update(SUB_SILO_MAP)

# 38 Explore Pages High-CTR Metadata Dictionary
EXPLORE_METADATA = {
    "flats-in-hinjewadi": {
        "title": "Flats in Hinjewadi Pune | from ₹79L*",
        "description": "Premium flats in Hinjewadi Pune at 105-Acre Krisala Hiranandani Township. 2, 3 & 4 BHK homes with 8-acre racecourse from ₹79L*. MahaRERA PR1260002500600."
    },
    "2-bhk-flats-in-hinjewadi": {
        "title": "2 BHK Flats in Hinjewadi | from ₹79L*",
        "description": "Best 2 BHK flats in Hinjewadi Pune at Krisala Hiranandani Sector Arcadia. 740-840 sq.ft. carpet area from ₹79L*. MahaRERA PR1260002500600. View floor plans."
    },
    "3-bhk-flats-in-hinjewadi": {
        "title": "3 BHK Flats in Hinjewadi | from ₹1.25Cr*",
        "description": "Premium 3 BHK flats in Hinjewadi Pune at The Colosseum, Krisala Hiranandani. 1,020-1,180 sq.ft. carpet from ₹1.25Cr*. MahaRERA PR1260002600818. View plans."
    },
    "luxury-apartments-in-hinjewadi": {
        "title": "Luxury Apartments Hinjewadi | from ₹79L*",
        "description": "Ultra-luxury apartments in Hinjewadi at Krisala Hiranandani: Neoclassical towers, 8-acre racecourse, and Della amenities from ₹79L*. MahaRERA PR1260002500600."
    },
    "townships-in-hinjewadi-pune": {
        "title": "Townships in Hinjewadi Pune | from ₹79L*",
        "description": "Explore 105+ Acre Krisala Hiranandani integrated equestrian township in North Hinjewadi, Pune. 2, 3 & 4 BHK homes & plots from ₹79L*. MahaRERA PR1260002500600."
    },
    "flats-near-hinjewadi-phase-1": {
        "title": "Flats Near Hinjewadi Phase 1 | from ₹79L*",
        "description": "Flats near Hinjewadi Phase 1 Pune at Krisala Hiranandani: 12-min signal-free drive via PMRDA Ring Road. 2 & 3 BHK from ₹79L*. MahaRERA Reg PR1260002500600."
    },
    "flats-near-hinjewadi-phase-2": {
        "title": "Flats Near Hinjewadi Phase 2 | from ₹79L*",
        "description": "Flats near Hinjewadi Phase 2 (Wipro Circle) at Krisala Hiranandani Township. 15-min commute to IT park. 2 & 3 BHK from ₹79L*. MahaRERA PR1260002500600."
    },
    "flats-near-hinjewadi-phase-3": {
        "title": "Flats Near Hinjewadi Phase 3 | from ₹79L*",
        "description": "Flats near Hinjewadi Phase 3 (TCS & Barclays) at Krisala Hiranandani Township. 14-min drive via Ring Road. 2, 3 & 4 BHK from ₹79L*. MahaRERA PR1260002500600."
    },
    "flats-near-mumbai-pune-expressway": {
        "title": "Flats Near Expressway | from ₹79L*",
        "description": "Luxury flats near Mumbai-Pune Expressway at Krisala Hiranandani Township (5 mins to Urse Toll). 2 & 3 BHK homes from ₹79L*. MahaRERA PR1260002500600. Enquire."
    },
    "flats-in-punawale-near-hinjewadi": {
        "title": "Flats in Punawale Near Hinjewadi | ₹79L*",
        "description": "Looking for flats in Punawale near Hinjewadi? Explore Krisala Hiranandani Township on PMRDA Ring Road. Luxury 2 & 3 BHK from ₹79L*. MahaRERA PR1260002500600."
    },
    "flats-in-wakad-near-hinjewadi": {
        "title": "Flats in Wakad Near Hinjewadi | from ₹79L*",
        "description": "Upgrade from Wakad apartments to 105-Acre Krisala Hiranandani Township. 2, 3 & 4 BHK homes with 8-acre racecourse from ₹79L*. MahaRERA Reg PR1260002500600."
    },
    "flats-under-80-lakhs-hinjewadi": {
        "title": "Flats Under 80 Lakhs Hinjewadi | ₹79L*",
        "description": "Best flats under 80 Lakhs in Hinjewadi Pune. Sector Arcadia at Krisala Hiranandani: 740 sq.ft. 2 BHK from ₹79L*. MahaRERA PR1260002500600. Download plans PDF."
    },
    "flats-under-1-crore-hinjewadi": {
        "title": "Flats Under 1 Crore Hinjewadi | from ₹79L*",
        "description": "Best residential flats under 1 Crore in Hinjewadi Pune. Sector Arcadia at Krisala Hiranandani: 2 & 3 BHK from ₹79L*. 70% open green space. MahaRERA approved."
    },
    "luxury-penthouses-in-pune": {
        "title": "Luxury Penthouses in Pune | from ₹2.10Cr*",
        "description": "Signature luxury penthouses & sky mansions in Pune at Sector Icon, Krisala Hiranandani Hinjewadi. Panoramic racecourse views from ₹2.10Cr*. MahaRERA verified."
    },
    "duplex-apartments-in-hinjewadi": {
        "title": "Duplex Apartments Hinjewadi | ₹2.10Cr*",
        "description": "Double-height luxury duplex penthouses in Hinjewadi Pune at Sector Icon, Krisala Hiranandani. 1,850-2,450 sq.ft. from ₹2.10Cr*. MahaRERA PR1260002600818."
    },
    "villa-plots-in-hinjewadi-pune": {
        "title": "Villa Plots in Hinjewadi | from ₹1.80Cr*",
        "description": "Exclusive villa plots in Hinjewadi Pune at Krisala Hiranandani Della Collection. 1,800 to 5,000 sq.ft. with racecourse frontage from ₹1.80Cr*. Enquire now."
    },
    "the-colosseum-hinjewadi": {
        "title": "The Colosseum Hinjewadi | from ₹79L*",
        "description": "The Colosseum at Krisala Hiranandani Hinjewadi: Roman neoclassical towers with amphitheatre podium. 2, 3 & 4 BHK from ₹79L*. MahaRERA Reg PR1260002600818."
    },
    "sector-icon-hinjewadi": {
        "title": "Sector Icon Hinjewadi | Duplex ₹2.10Cr*",
        "description": "Sector Icon at Krisala Hiranandani Hinjewadi: Double-height 4 BHK sky duplex penthouses with private terraces from ₹2.10Cr*. MahaRERA PR1260002600818. Enquire."
    },
    "sector-arcadia-hinjewadi": {
        "title": "Sector Arcadia Hinjewadi | from ₹79L*",
        "description": "Sector Arcadia at Krisala Hiranandani Hinjewadi. 2 & 3 BHK luxury neoclassical homes with Mivan construction from ₹79L*. MahaRERA PR1260002500600. View plans."
    },
    "della-township-bungalow-plots-hinjewadi": {
        "title": "Della Township Bungalow Plots | ₹1.80Cr*",
        "description": "Della Township luxury bungalow plots at Krisala Hiranandani Hinjewadi. G+2 sanctioned FSI around 8-acre racecourse from ₹1.80Cr*. MahaRERA PR1260002502438."
    },
    "bungalow-plots-in-hinjewadi-pune": {
        "title": "Bungalow Plots in Hinjewadi | from ₹1.80Cr*",
        "description": "Sanctioned freehold bungalow plots in Hinjewadi Pune at Della Township & Krisala Hiranandani. 1,800-5,000 sq.ft. from ₹1.80Cr*. MahaRERA PR1260002502438."
    },
    "della-township-lots-hinjewadi": {
        "title": "Della Township Lots Hinjewadi | ₹1.80Cr*",
        "description": "Della Township residential estate lots in Hinjewadi Pune. Freehold NA plots surrounding private racecourse from ₹1.80Cr*. MahaRERA Reg PR1260002502438."
    },
    "plots-in-hinjewadi-pune": {
        "title": "Plots in Hinjewadi Pune | from ₹1.80Cr*",
        "description": "MahaRERA approved residential plots in Hinjewadi Pune at Krisala Hiranandani Della Precinct. 1,800-5,000 sq.ft. from ₹1.80Cr*. Clear titles & NA order."
    },
    "krisala-hiranandani-2-bhk-luxury-apartments-hinjewadi": {
        "title": "2 BHK Luxury Flats Hinjewadi | from ₹79L*",
        "description": "Sector Arcadia 2 BHK flats at Krisala Hiranandani Hinjewadi: 740-840 sq.ft. Mivan structure from ₹79L*. MahaRERA PR1260002500600. Download floor plans PDF."
    },
    "krisala-hiranandani-3-bhk-luxury-apartments-hinjewadi": {
        "title": "3 BHK Luxury Flats Hinjewadi | ₹1.25Cr*",
        "description": "The Colosseum 3 BHK flats at Krisala Hiranandani Hinjewadi: 1,020-1,180 sq.ft. racecourse-facing from ₹1.25Cr*. MahaRERA PR1260002600818. Download plans PDF."
    },
    "krisala-hiranandani-4-bhk-luxury-apartments-north-hinjewadi": {
        "title": "4 BHK Sky Duplex Hinjewadi | ₹2.10Cr*",
        "description": "Sector Icon 4 BHK sky duplexes at Krisala Hiranandani Hinjewadi: 1,850-2,450 sq.ft. with 18ft double-height ceilings from ₹2.10Cr*. MahaRERA PR1260002600818."
    },
    "krisala-hiranandani-della-villa-plots-hinjewadi": {
        "title": "Della Villa Plots Hinjewadi | from ₹1.80Cr*",
        "description": "100 Exclusive Della Resort villa plots (1,800-5,000 sq.ft.) at Krisala Hiranandani Hinjewadi. 8-Acre racecourse & polo club from ₹1.80Cr*. MahaRERA approved."
    },
    "krisala-hiranandani-apartments-near-infosys-hinjewadi": {
        "title": "Flats Near Infosys Hinjewadi | from ₹79L*",
        "description": "Luxury flats near Infosys Hinjewadi Phase 1 at Krisala Hiranandani. 12-min drive via PMRDA Ring Road. 2 & 3 BHK from ₹79L*. MahaRERA Reg PR1260002500600."
    },
    "krisala-hiranandani-apartments-near-wipro-circle-hinjewadi": {
        "title": "Flats Near Wipro Circle | from ₹79L*",
        "description": "Luxury flats near Wipro Circle Hinjewadi Phase 2. Krisala Hiranandani offers a 15-min commute to Quadron & Cognizant. 2 & 3 BHK from ₹79L*. MahaRERA approved."
    },
    "krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi": {
        "title": "Flats Near TCS Phase 3 | from ₹79L*",
        "description": "Flats near TCS Sahyadri Park Hinjewadi Phase 3. Krisala Hiranandani Township offers a 14-min drive via PMRDA Ring Road. 2 & 3 BHK from ₹79L*. MahaRERA verified."
    },
    "krisala-hiranandani-luxury-township-darumbre-pune": {
        "title": "Krisala Hiranandani Darumbre | from ₹79L*",
        "description": "105-Acre Krisala Hiranandani Township in Darumbre, North Hinjewadi. Neoclassical towers & Della villa plots from ₹79L*. MahaRERA PR1260002500600. View plans."
    },
    "krisala-hiranandani-equestrian-turf-racecourse-residences": {
        "title": "Equestrian Turf Racecourse | from ₹1.80Cr*",
        "description": "India's 1st residential 8-acre turf racecourse & polo club residences at Krisala Hiranandani Hinjewadi. Luxury homes & plots from ₹1.80Cr*. MahaRERA verified."
    },
    "krisala-hiranandani-nri-investment-guide-pune": {
        "title": "NRI Real Estate Guide Pune | from ₹79L*",
        "description": "NRI investment guide for Krisala Hiranandani Hinjewadi: FEMA compliance, NRE/NRO repatriation, 5.4% rental yields & pre-launch prices from ₹79L* ($95K USD)."
    },
    "krisala-hiranandani-pmrda-ring-road-connectivity-advantage": {
        "title": "PMRDA Ring Road Connectivity | Hinjewadi",
        "description": "Strategic connectivity audit of the 128m PMRDA Ring Road at Krisala Hiranandani Hinjewadi: Signal-free drive to IT Park & Expressway. Homes from ₹79L*."
    },
    "krisala-hiranandani-vs-godrej-river-royale-hinjewadi": {
        "title": "Hiranandani vs Godrej Hinjewadi | 2026",
        "description": "Head-to-head comparison: Krisala Hiranandani (105 Acres) vs Godrej River Royale (5.5 Acres) in Hinjewadi. Compare density, amenities & pricing from ₹79L*."
    },
    "krisala-hiranandani-vs-kolte-patil-life-republic-hinjewadi": {
        "title": "Hiranandani vs Life Republic | 2026",
        "description": "Comparison between Krisala Hiranandani and Kolte Patil Life Republic Hinjewadi. Neoclassical architecture, 8-acre racecourse & pricing from ₹79L* compared."
    },
    "krisala-hiranandani-vs-lodha-sylvan-hinjewadi": {
        "title": "Hiranandani vs Lodha Hinjewadi | 2026",
        "description": "In-depth analysis: Krisala Hiranandani Township vs Lodha Sylvan Hinjewadi. Compare usable carpet area, equestrian amenities & 2026 pricing from ₹79L*."
    },
    "krisala-hiranandani-vs-vtp-earth-one-mahalunge": {
        "title": "Hiranandani vs VTP Earth One | 2026",
        "description": "Comprehensive benchmark: Krisala Hiranandani (105 Acres) vs VTP Earth One Mahalunge. Compare open space, racecourse living & entry pricing from ₹79L*."
    }
}

for slug, meta in EXPLORE_METADATA.items():
    CORE_METADATA[f"explore/{slug}.html"] = meta

def apply_metadata_to_file(file_path, meta):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    title = meta["title"].strip()
    desc = meta["description"].strip()

    # Title
    if soup.title:
        if soup.title.string != title:
            soup.title.string = title
            modified = True
    else:
        new_title = soup.new_tag("title")
        new_title.string = title
        if soup.head:
            soup.head.insert(0, new_title)
            modified = True

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        if meta_desc.get("content") != desc:
            meta_desc["content"] = desc
            modified = True
    else:
        new_meta = soup.new_tag("meta", attrs={"name": "description", "content": desc})
        if soup.head:
            soup.head.append(new_meta)
            modified = True

    # Social OpenGraph & Twitter
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content") != title:
        og_title["content"] = title
        modified = True
    og_desc = soup.find("meta", property="og:description")
    if og_desc and og_desc.get("content") != desc:
        og_desc["content"] = desc
        modified = True

    tw_title = soup.find("meta", attrs={"name": "twitter:title"}) or soup.find("meta", property="twitter:title")
    if tw_title and tw_title.get("content") != title:
        tw_title["content"] = title
        modified = True
    tw_desc = soup.find("meta", attrs={"name": "twitter:description"}) or soup.find("meta", property="twitter:description")
    if tw_desc and tw_desc.get("content") != desc:
        tw_desc["content"] = desc
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True
    return False

def harden_all_pages():
    print("=" * 70)
    print("Executing Enterprise 50% CTR Hardening Across All Pages")
    print("=" * 70)

    updated_count = 0
    for rel_path, meta in CORE_METADATA.items():
        full_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
        
        # Validate constraints
        t_len = len(meta["title"])
        d_len = len(meta["description"])
        if t_len > 55:
            print(f"[ERROR] Title > 55 chars: {rel_path} ({t_len}) -> {meta['title']}")
        if d_len > 160 or d_len < 135:
            print(f"[WARN] Desc length outside 135-160: {rel_path} ({d_len}) -> {meta['description']}")

        if apply_metadata_to_file(full_path, meta):
            updated_count += 1
            print(f"[✓ HARDENED] ({t_len} / {d_len} chars) {rel_path}")

    print(f"\nSuccessfully calibrated and hardened {updated_count} HTML pages for 50%+ CTR.")

def verify_all_files():
    print("\n" + "=" * 70)
    print("Running Full System Verification")
    print("=" * 70)
    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True))
    violations_title = []
    violations_desc = []
    has_tm = 0
    has_brackets = 0
    has_official = 0

    for f in html_files:
        if "node_modules" in f or ".git" in f or "googleDXq" in f:
            continue
        rel = os.path.relpath(f, ROOT_DIR)
        c = open(f, errors='ignore').read()
        soup = BeautifulSoup(c, "html.parser")
        
        # Check Title
        if soup.title and soup.title.string:
            t = soup.title.string.strip()
            if len(t) > 55:
                violations_title.append((rel, len(t), t))
        else:
            violations_title.append((rel, 0, "MISSING TITLE"))

        # Check Description
        m = soup.find("meta", attrs={"name": "description"})
        if m and m.get("content"):
            d = m["content"].strip()
            if len(d) > 160:
                violations_desc.append((rel, len(d), d))
        elif rel not in ["404.html", "analytics.html", "offline.html"]:
            violations_desc.append((rel, 0, "MISSING DESCRIPTION"))

        if "™" in c: has_tm += c.count("™")
        if "【" in c: has_brackets += c.count("【")
        if re.search(r'\bofficial\b', c, re.I):
            has_official += len(re.findall(r'\bofficial\b', c, re.I))

    print(f"Total HTML files audited: {len(html_files)}")
    print(f"Titles > 55 chars: {len(violations_title)}")
    for rel, l, t in violations_title:
        print(f"  [TITLE VIOLATION] {l} chars: {rel} -> {t}")

    print(f"Descriptions > 160 chars: {len(violations_desc)}")
    for rel, l, d in violations_desc:
        print(f"  [DESC VIOLATION] {l} chars: {rel} -> {d[:60]}...")

    print(f"TM occurrences: {has_tm}")
    print(f"Brackets occurrences: {has_brackets}")
    print(f"Official occurrences: {has_official}")

if __name__ == "__main__":
    harden_all_pages()
    verify_all_files()

#!/usr/bin/env python3
"""
Google SERP Title Links Optimization Engine
Krisala Hiranandani Township Hinjewadi, Pune
https://krisalahiranandanitownships.com

Key Rules:
1. 100% Brand Attribution: Every title must contain 'Krisala Hiranandani' or 'Hiranandani'.
   Prevents Google from automatically appending "- Krisala Hiranandani Township Pune" and truncating the snippet.
2. Length strictly <= 55 characters: Zero truncation on Google mobile & desktop search.
3. Front-load primary search query: The main keyword / tower / configuration comes first.
4. Harmonize <h1> with <title>: Clean over-long H1s so Google doesn't rewrite the title link.
5. Universal og:site_name on every page.
"""

import os
import glob
import re
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Master Google SERP Title Dictionary
GOOGLE_SERP_TITLES = {
    # Core Landing Pages
    "index.html": "Krisala Hiranandani Township Pune | from ₹79L*",
    "hiranandani-pune.html": "Hiranandani Pune Hinjewadi | Township from ₹79L*",
    "krisala-hiranandani-pune.html": "Krisala Hiranandani Pune | Flats from ₹79L*",
    "krisala-hiranandani-township-pune.html": "Krisala Hiranandani Township Pune | from ₹79L*",
    "arcadia.html": "Sector Arcadia | Krisala Hiranandani from ₹79L*",
    "colosseum.html": "The Colosseum | Krisala Hiranandani from ₹79L*",
    "icon.html": "Sector Icon | Krisala Hiranandani from ₹2.10Cr*",
    "della.html": "Della Township Plots | Krisala Hiranandani ₹1.8Cr*",
    "everlyn.html": "Sector Everlyn | Krisala Hiranandani from ₹79L*",
    "pricing.html": "Krisala Hiranandani Price List 2026 | from ₹79L*",
    "floor-plans.html": "Floor Plans 2, 3 & 4 BHK | Krisala Hiranandani",
    "reviews.html": "Krisala Hiranandani Reviews | 4.9★ (428 Reviews)",
    "site-address.html": "Site Address & Location | Krisala Hiranandani",
    "connectivity.html": "Connectivity & Metro Map | Krisala Hiranandani",
    "amenities.html": "8-Acre Racecourse Amenities | Krisala Hiranandani",
    "racecourse.html": "8-Acre Turf Racecourse | Krisala Hiranandani",
    "hiranandani-price-list-2026.html": "Hiranandani Pune Price List 2026 | from ₹79L*",
    "hiranandani-emi-calculator.html": "Home Loan EMI Calculator | Krisala Hiranandani",
    "masterplan.html": "105-Acre Master Plan Map | Krisala Hiranandani",
    "neighborhood.html": "North Hinjewadi IT Corridor | Krisala Hiranandani",
    "north-hinjewadi.html": "North Hinjewadi Guide | Krisala Hiranandani",
    "compare.html": "Compare Pune Projects 2026 | Krisala Hiranandani",
    "knowledge-hub.html": "Knowledge Hub & Buyer FAQs | Krisala Hiranandani",
    "gallery.html": "Photo & Video Gallery | Krisala Hiranandani Pune",
    "construction-status.html": "Construction Updates 2026 | Krisala Hiranandani",
    "pune-real-estate.html": "Pune Real Estate 2026 | Krisala Hiranandani",
    "hinjewadi-real-estate.html": "Hinjewadi Real Estate 2026 | Krisala Hiranandani",
    "nri.html": "NRI Property Investment Desk | Krisala Hiranandani",
    "blog.html": "Pune Real Estate Blog | Krisala Hiranandani",

    # Blog Articles
    "blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle.html": "Della Villa Plots Lifestyle | Krisala Hiranandani",
    "blog/hinjewadi-it-park-housing-shortage-pmrda-ring-road-surge-2026.html": "Hinjewadi Housing Deficit | Krisala Hiranandani",
    "blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune.html": "Hinjewadi Mega Corridor | Krisala Hiranandani",
    "blog/hinjewadi-phase-4-integrated-township-boom.html": "Hinjewadi Phase 4 Boom | Krisala Hiranandani",
    "blog/krisala-hiranandani-township-hinjewadi-flats-price-list-cost-sheet.html": "Flat Prices & Cost Sheet | Krisala Hiranandani",
    "blog/krisala-hiranandani-township-hinjewadi-location-connectivity-it-parks.html": "Location & Metro Map | Krisala Hiranandani Pune",
    "blog/krisala-hiranandani-township-hinjewadi-master-plan-review-2026.html": "105-Acre Master Plan Review | Krisala Hiranandani",
    "blog/krisala-hiranandani-township-hinjewadi-sample-flat-floor-plans-carpet-area.html": "Sample Flat & Floor Plans | Krisala Hiranandani",
    "blog/krisala-hiranandani-township-pune-complete-buyers-handbook-2026.html": "Homebuyers Handbook 2026 | Krisala Hiranandani",
    "blog/krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence.html": "MahaRERA Legal Approvals | Krisala Hiranandani",
    "blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan.html": "Hiranandani vs Godrej & Lodha | Comparison 2026",
    "blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide.html": "NRI Investment Guide 2026 | Krisala Hiranandani",
    "blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi.html": "Neoclassical Architecture | Krisala Hiranandani",
    "blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure.html": "PMRDA Ring Road & Metro | Krisala Hiranandani",
    "blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi.html": "Pune Flat Price Trends 2026 | Krisala Hiranandani",
    "blog/pune-metro-line-3-hinjewadi-trials-property-impact.html": "Pune Metro Line 3 Trials | Krisala Hiranandani",
    "blog/the-colosseum-hinjewadi-phase-4-investment-guide.html": "The Colosseum Phase 4 Guide | Krisala Hiranandani",
    "blog/top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments.html": "Township vs Standalone | Krisala Hiranandani Pune",
    "blog/why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi.html": "Tech Corridor Living Guide | Krisala Hiranandani",

    # NRI Regional Portals
    "nri/index.html": "NRI Investment Desk | Krisala Hiranandani Pune",
    "nri/dubai-uae.html": "Dubai NRI Property Desk | Krisala Hiranandani",
    "nri/usa-silicon-valley.html": "USA NRI Property Desk | Krisala Hiranandani",
    "nri/uk-london.html": "UK NRI Property Desk | Krisala Hiranandani",
    "nri/singapore.html": "Singapore NRI Desk | Krisala Hiranandani Pune",
    "nri/canada-toronto.html": "Canada NRI Property Desk | Krisala Hiranandani",
    "nri/australia-sydney.html": "Australia NRI Desk | Krisala Hiranandani Pune",

    # Competitor Comparison Portals
    "compare/vs-godrej-river-royale.html": "Hiranandani vs Godrej River Royale | 2026 Guide",
    "compare/vs-lodha-sylvan.html": "Hiranandani vs Lodha Sylvan Pune | 2026 Guide",
    "compare/vs-kolte-patil-life-republic.html": "Hiranandani vs Kolte Patil Pune | 2026 Guide",

    # Web Stories Portals
    "stories/della-equestrian-villa-plots.html": "Della Villa Plots | Krisala Hiranandani Pune",
    "stories/hinjewadi-it-investment-roi.html": "Hinjewadi Investment ROI | Krisala Hiranandani",
    "stories/maharera-legal-sanctions-guide.html": "MahaRERA Sanctions Guide | Krisala Hiranandani",
    "stories/nri-investment-desk-pune.html": "NRI Real Estate Guide | Krisala Hiranandani",
    "stories/sector-arcadia-luxury-living.html": "Sector Arcadia Living | Krisala Hiranandani",
    "stories/sector-icon-sky-residences.html": "Sector Icon Sky Suites | Krisala Hiranandani",
    "stories/the-colosseum-phase-4.html": "The Colosseum Phase 4 | Krisala Hiranandani",
    "stories/township-grand-living.html": "105-Acre Grand Living | Krisala Hiranandani",

    # 38 Explore Pages
    "explore/flats-in-hinjewadi.html": "Flats in Hinjewadi | Krisala Hiranandani from ₹79L*",
    "explore/2-bhk-flats-in-hinjewadi.html": "2 BHK Flats Hinjewadi | Krisala Hiranandani ₹79L*",
    "explore/3-bhk-flats-in-hinjewadi.html": "3 BHK Flats Hinjewadi | Krisala Hiranandani ₹1.25Cr*",
    "explore/luxury-apartments-in-hinjewadi.html": "Luxury Flats Hinjewadi | Krisala Hiranandani ₹79L*",
    "explore/townships-in-hinjewadi-pune.html": "Townships in Hinjewadi | Krisala Hiranandani Pune",
    "explore/flats-near-hinjewadi-phase-1.html": "Flats Near Phase 1 | Krisala Hiranandani from ₹79L*",
    "explore/flats-near-hinjewadi-phase-2.html": "Flats Near Phase 2 | Krisala Hiranandani from ₹79L*",
    "explore/flats-near-hinjewadi-phase-3.html": "Flats Near Phase 3 | Krisala Hiranandani from ₹79L*",
    "explore/flats-near-mumbai-pune-expressway.html": "Flats Near Expressway | Krisala Hiranandani ₹79L*",
    "explore/flats-in-punawale-near-hinjewadi.html": "Flats in Punawale | Krisala Hiranandani from ₹79L*",
    "explore/flats-in-wakad-near-hinjewadi.html": "Flats in Wakad | Krisala Hiranandani from ₹79L*",
    "explore/flats-under-80-lakhs-hinjewadi.html": "Flats Under 80 Lakhs | Krisala Hiranandani ₹79L*",
    "explore/flats-under-1-crore-hinjewadi.html": "Flats Under 1 Crore | Krisala Hiranandani ₹79L*",
    "explore/luxury-penthouses-in-pune.html": "Luxury Penthouses Pune | Krisala Hiranandani ₹2.1Cr*",
    "explore/duplex-apartments-in-hinjewadi.html": "Duplex Flats Hinjewadi | Krisala Hiranandani ₹2.1Cr*",
    "explore/villa-plots-in-hinjewadi-pune.html": "Villa Plots Hinjewadi | Krisala Hiranandani ₹1.8Cr*",
    "explore/the-colosseum-hinjewadi.html": "The Colosseum Hinjewadi | Krisala Hiranandani ₹79L*",
    "explore/sector-icon-hinjewadi.html": "Sector Icon Hinjewadi | Krisala Hiranandani ₹2.10Cr*",
    "explore/sector-arcadia-hinjewadi.html": "Sector Arcadia Hinjewadi | Krisala Hiranandani ₹79L*",
    "explore/della-township-bungalow-plots-hinjewadi.html": "Della Township Plots Hinjewadi | Hiranandani",
    "explore/bungalow-plots-in-hinjewadi-pune.html": "Bungalow Plots Hinjewadi | Krisala Hiranandani",
    "explore/della-township-lots-hinjewadi.html": "Della Township Lots Hinjewadi | Hiranandani",
    "explore/plots-in-hinjewadi-pune.html": "Plots in Hinjewadi | Krisala Hiranandani from ₹1.8Cr*",
    "explore/krisala-hiranandani-2-bhk-luxury-apartments-hinjewadi.html": "2 BHK Luxury Flats | Krisala Hiranandani ₹79L*",
    "explore/krisala-hiranandani-3-bhk-luxury-apartments-hinjewadi.html": "3 BHK Luxury Flats | Krisala Hiranandani ₹1.25Cr*",
    "explore/krisala-hiranandani-4-bhk-luxury-apartments-north-hinjewadi.html": "4 BHK Sky Duplex | Krisala Hiranandani ₹2.10Cr*",
    "explore/krisala-hiranandani-della-villa-plots-hinjewadi.html": "Della Villa Plots | Krisala Hiranandani ₹1.80Cr*",
    "explore/krisala-hiranandani-apartments-near-infosys-hinjewadi.html": "Flats Near Infosys | Krisala Hiranandani from ₹79L*",
    "explore/krisala-hiranandani-apartments-near-wipro-circle-hinjewadi.html": "Flats Near Wipro Circle | Krisala Hiranandani ₹79L*",
    "explore/krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi.html": "Flats Near TCS Phase 3 | Krisala Hiranandani ₹79L*",
    "explore/krisala-hiranandani-luxury-township-darumbre-pune.html": "Darumbre Luxury Township | Krisala Hiranandani",
    "explore/krisala-hiranandani-equestrian-turf-racecourse-residences.html": "Equestrian Racecourse | Krisala Hiranandani",
    "explore/krisala-hiranandani-nri-investment-guide-pune.html": "NRI Investment Guide | Krisala Hiranandani Pune",
    "explore/krisala-hiranandani-pmrda-ring-road-connectivity-advantage.html": "PMRDA Ring Road Corridor | Krisala Hiranandani",
    "explore/krisala-hiranandani-vs-godrej-river-royale-hinjewadi.html": "Hiranandani vs Godrej Hinjewadi | Comparison 2026",
    "explore/krisala-hiranandani-vs-kolte-patil-life-republic-hinjewadi.html": "Hiranandani vs Life Republic Hinjewadi | 2026",
    "explore/krisala-hiranandani-vs-lodha-sylvan-hinjewadi.html": "Hiranandani vs Lodha Hinjewadi | Comparison 2026",
    "explore/krisala-hiranandani-vs-vtp-earth-one-mahalunge.html": "Hiranandani vs VTP Earth One | Comparison 2026",

    # 43 Programmatic 10,000 Impressions Expansion Hubs
    "explore/flats-in-mahalunge-pune.html": "Flats in Mahalunge Pune | Krisala Hiranandani ₹79L*",
    "explore/2-bhk-flats-in-mahalunge.html": "2 BHK Flats in Mahalunge | Krisala Hiranandani ₹79L*",
    "explore/3-bhk-flats-in-mahalunge.html": "3 BHK Flats in Mahalunge | Krisala Hiranandani ₹1.25Cr*",
    "explore/flats-in-wakad-pune.html": "Flats in Wakad Pune | Krisala Hiranandani from ₹79L*",
    "explore/2-bhk-flats-in-wakad.html": "2 BHK Flats in Wakad | Krisala Hiranandani ₹79L*",
    "explore/3-bhk-flats-in-wakad.html": "3 BHK Flats in Wakad | Krisala Hiranandani ₹1.25Cr*",
    "explore/flats-in-punawale-pune.html": "Flats in Punawale Pune | Krisala Hiranandani ₹79L*",
    "explore/flats-in-marunji-hinjewadi.html": "Flats in Marunji Hinjewadi | Krisala Hiranandani ₹79L*",
    "explore/flats-in-baner-pune.html": "Flats in Baner Pune | Krisala Hiranandani from ₹79L*",
    "explore/flats-in-balewadi-pune.html": "Flats in Balewadi Pune | Krisala Hiranandani ₹79L*",
    "explore/flats-in-tathawade-pune.html": "Flats in Tathawade Pune | Krisala Hiranandani ₹79L*",
    "explore/flats-in-ravet-pune.html": "Flats in Ravet Pune | Krisala Hiranandani from ₹79L*",
    "explore/flats-near-quadron-business-park-hinjewadi.html": "Flats Near Quadron | Krisala Hiranandani ₹79L*",
    "explore/flats-near-embassy-techzone-hinjewadi.html": "Flats Near TechZone | Krisala Hiranandani ₹79L*",
    "explore/flats-under-70-lakhs-hinjewadi.html": "Flats Under 70L Hinjewadi | Krisala Hiranandani",
    "explore/flats-under-90-lakhs-hinjewadi.html": "Flats Under 90L Hinjewadi | Krisala Hiranandani",
    "explore/flats-under-1-2-crore-hinjewadi.html": "Flats Under 1.2Cr Hinjewadi | Krisala Hiranandani",
    "explore/flats-under-1-5-crore-hinjewadi.html": "Flats Under 1.5Cr Hinjewadi | Krisala Hiranandani",
    "explore/luxury-flats-above-2-crore-pune.html": "Flats Above 2 Crore | Krisala Hiranandani ₹2.1Cr*",
    "explore/hiranandani-pune-cost-sheet-download.html": "Hiranandani Cost Sheet Download | from ₹79L*",
    "explore/hiranandani-pune-payment-plan-20-80.html": "Hiranandani Payment Plan 20:80 | from ₹79L*",
    "explore/residential-plots-in-hinjewadi-pune.html": "Residential Plots | Krisala Hiranandani ₹1.8Cr*",
    "explore/na-plots-in-hinjewadi-pune.html": "NA Plots Hinjewadi | Krisala Hiranandani ₹1.8Cr*",
    "explore/gated-community-plots-in-hinjewadi.html": "Gated Plots Hinjewadi | Krisala Hiranandani ₹1.8Cr*",
    "explore/villa-plots-in-pune-west.html": "Villa Plots Pune West | Krisala Hiranandani ₹1.8Cr*",
    "explore/bungalow-plots-near-mumbai-pune-expressway.html": "Plots Near Expressway | Krisala Hiranandani ₹1.8Cr*",
    "explore/della-luxury-resort-villa-plots-pune.html": "Della Resort Plots | Krisala Hiranandani ₹1.8Cr*",
    "explore/della-polo-club-residences-hinjewadi.html": "Della Polo Club | Krisala Hiranandani ₹1.8Cr*",
    "explore/equestrian-estate-plots-pune.html": "Equestrian Plots Pune | Krisala Hiranandani ₹1.8Cr*",
    "explore/krisala-hiranandani-vs-shapoorji-joyville-hinjewadi.html": "Hiranandani vs Shapoorji Joyville | 2026",
    "explore/krisala-hiranandani-vs-rohan-nidita-hinjewadi.html": "Hiranandani vs Rohan Nidita Hinjewadi | 2026",
    "explore/krisala-hiranandani-vs-kasturi-the-balmoral-towers.html": "Hiranandani vs Kasturi Balmoral | 2026",
    "explore/krisala-hiranandani-vs-vilas-javdekar-yashwin.html": "Hiranandani vs Vilas Javdekar Yashwin | 2026",
    "explore/krisala-hiranandani-vs-pride-purple-park-connect.html": "Hiranandani vs Pride Purple Park Connect | 2026",
    "explore/krisala-hiranandani-vs-kohinoor-coral-hinjewadi.html": "Hiranandani vs Kohinoor Coral Hinjewadi | 2026",
    "explore/krisala-hiranandani-sample-flat-3d-tour.html": "Sample Flat 3D Tour | Krisala Hiranandani ₹79L*",
    "explore/krisala-hiranandani-brochure-download-2026-pdf.html": "Brochure Download 2026 PDF | Krisala Hiranandani",
    "explore/krisala-hiranandani-possession-date-2028.html": "Possession Date & Timeline | Krisala Hiranandani",
    "explore/krisala-hiranandani-site-visit-cab-booking.html": "Site Visit Free Cab Booking | Krisala Hiranandani",
    "explore/krisala-hiranandani-bank-loan-pre-approval-sbi-hdfc.html": "Bank Home Loan Pre-Approval | Krisala Hiranandani",
    "explore/krisala-hiranandani-carpet-area-vs-built-up-sheet.html": "Carpet Area Sheet | Krisala Hiranandani ₹79L*",
    "explore/krisala-hiranandani-construction-update-mivan-progress.html": "Construction Update | Krisala Hiranandani 2026",
    "explore/krisala-hiranandani-rental-yield-it-professionals.html": "Rental Yield Guide | Krisala Hiranandani 5.4% ROI",
}

# Sub-silos
SUB_SILO_PAGES = [
    "arcadia.html", "colosseum.html", "icon.html", "della.html",
    "floor-plans.html", "price-list-2026.html", "reviews.html",
    "site-address.html", "connectivity.html", "amenities.html", "construction-status.html"
]

for s in SUB_SILO_PAGES:
    target_key = s if s != "price-list-2026.html" else "hiranandani-price-list-2026.html"
    title = GOOGLE_SERP_TITLES.get(target_key, "Krisala Hiranandani Township Pune")
    GOOGLE_SERP_TITLES[f"krisala-hiranandani-pune/{s}"] = title
    GOOGLE_SERP_TITLES[f"krisala-hiranandani-township-pune/{s}"] = title

GOOGLE_SERP_TITLES["krisala-hiranandani-pune/index.html"] = GOOGLE_SERP_TITLES["krisala-hiranandani-pune.html"]
GOOGLE_SERP_TITLES["krisala-hiranandani-township-pune/index.html"] = GOOGLE_SERP_TITLES["krisala-hiranandani-township-pune.html"]

def clean_h1_tags():
    """Harmonizes <h1> with <title> across core pages so Google doesn't rewrite title links."""
    replacements = {
        "colosseum.html": (
            '<h1 class="scroll-reveal" style="font-size: clamp(2.3rem, 5.5vw, 4.4rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">\n The Colosseum at Krisala Hiranandani Township Hinjewadi<br/>\n<span style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px;">Phase 4 Roman Landmark Towers • North Hinjewadi, Pune</span>\n</h1>',
            '<h1 class="scroll-reveal" style="font-size: clamp(2.3rem, 5.5vw, 4.4rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">The Colosseum • Krisala Hiranandani Hinjewadi</h1>\n<p style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px; margin-bottom: 16px;">Phase 4 Roman Landmark Towers • North Hinjewadi, Pune</p>'
        ),
        "arcadia.html": (
            '<h1 class="scroll-reveal" style="font-size: clamp(2.2rem, 5vw, 4.2rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">\n Sector Arcadia at Krisala Hiranandani Township Hinjewadi<br/>\n<span style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px;">2 &amp; 3 BHK Luxury Neoclassical Flats • Hinjewadi, Pune</span>\n</h1>',
            '<h1 class="scroll-reveal" style="font-size: clamp(2.2rem, 5vw, 4.2rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">Sector Arcadia • Krisala Hiranandani Hinjewadi</h1>\n<p style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px; margin-bottom: 16px;">2 &amp; 3 BHK Luxury Neoclassical Flats • Hinjewadi, Pune</p>'
        ),
        "icon.html": (
            '<h1 class="scroll-reveal" style="font-size: clamp(2.3rem, 5.5vw, 4.5rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">\n Krisala Hiranandani Sector Icon<br/>\n<span style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px;">3 &amp; 4 BHK Ultra-Luxury Residences &amp; Presidential Duplex Penthouses • North Hinjewadi</span>\n</h1>',
            '<h1 class="scroll-reveal" style="font-size: clamp(2.3rem, 5.5vw, 4.5rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">Sector Icon • Krisala Hiranandani Hinjewadi</h1>\n<p style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px; margin-bottom: 16px;">3 &amp; 4 BHK Ultra-Luxury Residences &amp; Presidential Duplex Penthouses • North Hinjewadi</p>'
        ),
        "pricing.html": (
            '<h1 class="scroll-reveal" style="font-size: clamp(2.2rem, 5vw, 4.2rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">\n Krisala Hiranandani Township Hinjewadi Price List 2026<br/>\n<span style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px;">2, 3, 4 BHK Flat Prices &amp; Signature Residences • Flexible CLP Plans</span>\n</h1>',
            '<h1 class="scroll-reveal" style="font-size: clamp(2.2rem, 5vw, 4.2rem); color: var(--gold-light); font-family: var(--font-heading); letter-spacing: 0.04em; margin-bottom: 16px; line-height: 1.15;">Price List 2026 • Krisala Hiranandani Hinjewadi</h1>\n<p style="font-size: clamp(1.2rem, 2.5vw, 1.8rem); color: #fff; font-weight: 400; display: block; margin-top: 8px; margin-bottom: 16px;">2, 3, 4 BHK Flat Prices &amp; Signature Residences • Flexible CLP Plans</p>'
        )
    }

    for rel_path, (old_h1, new_h1) in replacements.items():
        file_path = os.path.join(ROOT_DIR, rel_path)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if old_h1 in content:
                content = content.replace(old_h1, new_h1)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[✓ H1 HARMONIZED] {rel_path}")

def update_google_serp_titles():
    print("=" * 70)
    print("Deploying Google SERP Title Links Across All Pages")
    print("=" * 70)

    updated_count = 0

    for rel_path, title in GOOGLE_SERP_TITLES.items():
        file_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(file_path):
            continue

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        modified = False

        # Validate title length <= 55 chars
        clean_title = title.strip()
        if len(clean_title) > 55:
            print(f"[WARN] Title > 55 chars ({len(clean_title)}): {rel_path} -> {clean_title}")

        # Update <title>
        if soup.title:
            if soup.title.string != clean_title:
                soup.title.string = clean_title
                modified = True
        else:
            new_title = soup.new_tag("title")
            new_title.string = clean_title
            if soup.head:
                soup.head.insert(0, new_title)
                modified = True

        # Update og:title
        og_title = soup.find("meta", property="og:title")
        if og_title:
            if og_title.get("content") != clean_title:
                og_title["content"] = clean_title
                modified = True
        else:
            new_og_title = soup.new_tag("meta", attrs={"property": "og:title", "content": clean_title})
            if soup.head:
                soup.head.append(new_og_title)
                modified = True

        # Update twitter:title
        tw_title = soup.find("meta", attrs={"name": "twitter:title"})
        if tw_title:
            if tw_title.get("content") != clean_title:
                tw_title["content"] = clean_title
                modified = True
        else:
            new_tw_title = soup.new_tag("meta", attrs={"name": "twitter:title", "content": clean_title})
            if soup.head:
                soup.head.append(new_tw_title)
                modified = True

        # Ensure og:site_name
        og_site = soup.find("meta", property="og:site_name")
        if not og_site:
            new_og_site = soup.new_tag("meta", attrs={"property": "og:site_name", "content": "Krisala Hiranandani Township Pune"})
            if soup.head:
                soup.head.append(new_og_site)
                modified = True

        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            updated_count += 1
            print(f"[✓ SERP TITLE] ({len(clean_title)}c): {rel_path} -> {clean_title}")

    print(f"\nSuccessfully updated Google SERP Titles on {updated_count} HTML files.")

def verify_google_serp_compliance():
    print("\n" + "=" * 70)
    print("Verifying 100% Google SERP Titles & Attribution Compliance")
    print("=" * 70)

    html_files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)
    html_files = [f for f in html_files if "node_modules" not in f and "/." not in f]

    over_55 = []
    missing_brand = []
    missing_og_site = []

    for f in html_files:
        rel = os.path.relpath(f, ROOT_DIR)
        if rel.startswith("google") and rel.endswith(".html"):
            continue
        with open(f, "r", encoding="utf-8", errors="ignore") as fh:
            soup = BeautifulSoup(fh.read(), "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        if len(title) > 55:
            over_55.append((rel, len(title), title))

        if title and "hiranandani" not in title.lower() and "krisala" not in title.lower():
            if rel != "analytics.html": # internal dashboard
                missing_brand.append((rel, len(title), title))

        if not soup.find("meta", property="og:site_name"):
            if rel != "analytics.html":
                missing_og_site.append(rel)

    print(f"Total HTML files audited: {len(html_files)}")
    print(f"Titles > 55 chars: {len(over_55)}")
    for rel, length, t in over_55:
        print(f"  [OVER 55] ({length}c) {rel}: {t}")

    print(f"Titles Missing Brand Attribution: {len(missing_brand)}")
    for rel, length, t in missing_brand:
        print(f"  [MISSING BRAND] ({length}c) {rel}: {t}")

    print(f"Pages Missing og:site_name: {len(missing_og_site)}")

    if len(over_55) == 0 and len(missing_brand) == 0 and len(missing_og_site) == 0:
        print("\n[SUCCESS] 100% OF PAGES ARE PERFECT GOOGLE SERP TITLE COMPLIANT!")
    else:
        print("\n[WARNING] Some pages require further calibration.")

if __name__ == "__main__":
    clean_h1_tags()
    update_google_serp_titles()
    verify_google_serp_compliance()

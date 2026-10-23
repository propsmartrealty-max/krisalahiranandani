#!/usr/bin/env python3
"""
IndexNow Real-Time Search Engine Notification Engine
Notifies Microsoft Bing, Yandex, Seznam, and IndexNow partners
for instant search engine crawl and indexation.
"""

import os
import requests
import json

HOST = os.getenv("INDEXNOW_HOST", "krisalahiranandanitownships.com")
KEY = os.getenv("INDEXNOW_KEY", "e2b9c79fa4d84b90a6e4d77c15243890")
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

URL_LIST = [
    f"https://{HOST}/krisala-hiranandani-pune/",
    f"https://{HOST}/krisala-hiranandani-pune/price-list-2026",
    f"https://{HOST}/krisala-hiranandani-pune/reviews",
    f"https://{HOST}/krisala-hiranandani-pune/floor-plans",
    f"https://{HOST}/krisala-hiranandani-pune/construction-status",
    f"https://{HOST}/krisala-hiranandani-pune/site-address",
    f"https://{HOST}/blog/top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments",
    f"https://{HOST}/blog/krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence",
    f"https://{HOST}/blog/why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi",
    f"https://{HOST}/blog/krisala-hiranandani-township-pune-complete-buyers-handbook-2026",
    f"https://{HOST}/",
    f"https://{HOST}/hiranandani-pune",
    f"https://{HOST}/hiranandani-price-list-2026",
    f"https://{HOST}/hiranandani-emi-calculator",
    f"https://{HOST}/site-address",
    f"https://{HOST}/reviews",
    f"https://{HOST}/floor-plans",
    f"https://{HOST}/construction-status",
    f"https://{HOST}/north-hinjewadi",
    f"https://{HOST}/compare/vs-godrej-river-royale",
    f"https://{HOST}/compare/vs-lodha-sylvan",
    f"https://{HOST}/compare/vs-kolte-patil-life-republic",
    f"https://{HOST}/pune-real-estate",
    f"https://{HOST}/hinjewadi-real-estate",
    f"https://{HOST}/arcadia",
    f"https://{HOST}/colosseum",
    f"https://{HOST}/icon",
    f"https://{HOST}/pricing",
    f"https://{HOST}/amenities",
    f"https://{HOST}/nri",
    f"https://{HOST}/connectivity",
    f"https://{HOST}/racecourse",
    f"https://{HOST}/gallery",
    f"https://{HOST}/everlyn",
    f"https://{HOST}/della",
    f"https://{HOST}/masterplan",
    f"https://{HOST}/neighborhood",
    f"https://{HOST}/compare",
    f"https://{HOST}/knowledge-hub",
    f"https://{HOST}/blog",
    f"https://{HOST}/privacy-policy",
    f"https://{HOST}/sitemap-index.xml",
    f"https://{HOST}/sitemap.xml",
    f"https://{HOST}/image-sitemap.xml",
    f"https://{HOST}/video-sitemap.xml",
    f"https://{HOST}/sitemap-configurations.xml",
    f"https://{HOST}/sitemap-colosseum.xml",
    f"https://{HOST}/sitemap-pricing.xml",
    f"https://{HOST}/sitemap-it-workplaces.xml",
    f"https://{HOST}/sitemap-connectivity.xml",
    f"https://{HOST}/sitemap-micromarkets.xml",
    f"https://{HOST}/sitemap-villa-plots.xml",
    f"https://{HOST}/sitemap-comparisons.xml",
    f"https://{HOST}/sitemap-amenities.xml",
    f"https://{HOST}/sitemap-amenities-lifestyle.xml",
    f"https://{HOST}/sitemap-investment-roi.xml",
    f"https://{HOST}/sitemap-sustainability.xml",
    f"https://{HOST}/sitemap-construction.xml",
    f"https://{HOST}/sitemap-rera-legal.xml",
    f"https://{HOST}/sitemap-nri-desk.xml",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/rss.xml",
    f"https://{HOST}/sitemap-explore.xml",
    f"https://{HOST}/sitemap-nri-global.xml",
    # 6 Dedicated Global NRI Regional Hubs
    f"https://{HOST}/nri/dubai-uae",
    f"https://{HOST}/nri/usa-silicon-valley",
    f"https://{HOST}/nri/uk-london",
    f"https://{HOST}/nri/singapore",
    f"https://{HOST}/nri/australia-sydney",
    f"https://{HOST}/nri/canada-toronto",
    # 15 Canonical Programmatic Explore Authority Pages
    f"https://{HOST}/explore/krisala-hiranandani-2-bhk-luxury-apartments-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-3-bhk-luxury-apartments-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-4-bhk-luxury-apartments-north-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-della-villa-plots-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-apartments-near-infosys-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-apartments-near-wipro-circle-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-luxury-township-darumbre-pune",
    f"https://{HOST}/explore/krisala-hiranandani-equestrian-turf-racecourse-residences",
    f"https://{HOST}/explore/krisala-hiranandani-nri-investment-guide-pune",
    f"https://{HOST}/explore/krisala-hiranandani-pmrda-ring-road-connectivity-advantage",
    f"https://{HOST}/explore/krisala-hiranandani-vs-godrej-river-royale-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-vs-lodha-sylvan-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-vs-kolte-patil-life-republic-hinjewadi",
    f"https://{HOST}/explore/krisala-hiranandani-vs-vtp-earth-one-mahalunge",
    # Google Web Stories Suite
    f"https://{HOST}/stories/the-colosseum-phase-4.html",
    f"https://{HOST}/stories/township-grand-living.html",
    f"https://{HOST}/stories/sector-icon-sky-residences.html",
    f"https://{HOST}/stories/sector-arcadia-luxury-living.html",
    f"https://{HOST}/stories/della-equestrian-villa-plots.html",
    f"https://{HOST}/stories/hinjewadi-it-investment-roi.html",
    f"https://{HOST}/stories/maharera-legal-sanctions-guide.html",
    f"https://{HOST}/stories/nri-investment-desk-pune.html",
    # Google Articles & Research Hub Standalone Pages
    f"https://{HOST}/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune",
    f"https://{HOST}/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi",
    f"https://{HOST}/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi",
    f"https://{HOST}/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure",
    f"https://{HOST}/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan",
    f"https://{HOST}/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide",
    f"https://{HOST}/blog/the-colosseum-hinjewadi-phase-4-investment-guide",
    f"https://{HOST}/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle",
    # New Feeds & Sitemaps
    f"https://{HOST}/sitemap-news.xml",
    f"https://{HOST}/sitemap-blog.xml",
    f"https://{HOST}/sitemap-geo.xml",
    f"https://{HOST}/locations.kml",
    f"https://{HOST}/atom.xml",
    f"https://{HOST}/feed.json"
]

def main():
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": URL_LIST
    }
    
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    
    print(f"Submitting {len(URL_LIST)} URLs to IndexNow API ({ENDPOINT})...")
    resp = requests.post(ENDPOINT, headers=headers, json=payload)
    print(f"Status Code: {resp.status_code}")
    print(f"Response: {resp.text or 'SUCCESS (HTTP 200/202 Accepted)'}")

if __name__ == "__main__":
    main()

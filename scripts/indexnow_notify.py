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
    f"https://{HOST}/",
    f"https://{HOST}/hiranandani-pune",
    f"https://{HOST}/hiranandani-price-list-2026",
    f"https://{HOST}/hiranandani-emi-calculator",
    f"https://{HOST}/site-address",
    f"https://{HOST}/reviews",
    f"https://{HOST}/floor-plans",
    f"https://{HOST}/construction-status",
    f"https://{HOST}/north-hinjewadi",
    f"https://{HOST}/contact",
    f"https://{HOST}/explore",
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
    f"https://{HOST}/della-racecourse",
    f"https://{HOST}/masterplan",
    f"https://{HOST}/neighborhood",
    f"https://{HOST}/compare",
    f"https://{HOST}/knowledge-hub",
    f"https://{HOST}/blog",
    f"https://{HOST}/privacy-policy",
    f"https://{HOST}/terms-and-conditions",
    f"https://{HOST}/disclaimer",
    f"https://{HOST}/refund-cancellation-policy",
    # Global NRI Regional Hubs
    f"https://{HOST}/nri/dubai-uae",
    f"https://{HOST}/nri/usa-silicon-valley",
    f"https://{HOST}/nri/uk-london",
    f"https://{HOST}/nri/singapore",
    f"https://{HOST}/nri/australia-sydney",
    f"https://{HOST}/nri/canada-toronto",
    # Top Canonical Explore Priority Hubs (full 69-URL set loaded dynamically from sitemap-explore.xml)
    f"https://{HOST}/explore/hiranandani-marunji",
    f"https://{HOST}/explore/hiranandani-pune-payment-plan-20-80",
    f"https://{HOST}/explore/2-bhk-flats-in-hinjewadi",
    f"https://{HOST}/explore/3-bhk-flats-in-hinjewadi",
    f"https://{HOST}/explore/4-bhk-flats-in-hinjewadi",
    f"https://{HOST}/explore/della-township-bungalow-plots-hinjewadi",
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
    f"https://{HOST}/blog/top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments",
    f"https://{HOST}/blog/krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence",
    f"https://{HOST}/blog/why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi",
    f"https://{HOST}/blog/krisala-hiranandani-township-pune-complete-buyers-handbook-2026",
    f"https://{HOST}/blog/pune-metro-line-3-hinjewadi-trials-property-impact",
    f"https://{HOST}/blog/hinjewadi-phase-4-integrated-township-boom",
    f"https://{HOST}/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune",
    f"https://{HOST}/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi",
    f"https://{HOST}/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi",
    f"https://{HOST}/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure",
    f"https://{HOST}/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan",
    f"https://{HOST}/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide",
    f"https://{HOST}/blog/the-colosseum-hinjewadi-phase-4-investment-guide",
    f"https://{HOST}/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle",
    # Canonical Feeds, AI Facts & Sitemaps
    f"https://{HOST}/sitemap-index.xml",
    f"https://{HOST}/sitemap.xml",
    f"https://{HOST}/sitemap-explore.xml",
    f"https://{HOST}/sitemap-news.xml",
    f"https://{HOST}/sitemap-blog.xml",
    f"https://{HOST}/sitemap-stories.xml",
    f"https://{HOST}/sitemap-nri-global.xml",
    f"https://{HOST}/sitemap-geo.xml",
    f"https://{HOST}/image-sitemap.xml",
    f"https://{HOST}/video-sitemap.xml",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/llms-full.txt",
    f"https://{HOST}/ai-facts.json",
    f"https://{HOST}/locations.kml",
    f"https://{HOST}/rss.xml",
    f"https://{HOST}/atom.xml",
    f"https://{HOST}/feed.json"
]

def main():
    # Dynamically read all URLs from sitemap-explore.xml and sitemap.xml
    import xml.etree.ElementTree as ET
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    explore_sitemap_path = os.path.join(root_dir, "sitemap-explore.xml")

    all_urls = list(URL_LIST)
    if os.path.exists(explore_sitemap_path):
        try:
            tree = ET.parse(explore_sitemap_path)
            for loc in tree.getroot().findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                if loc.text and loc.text not in all_urls:
                    all_urls.append(loc.text)
        except Exception as e:
            print(f"[WARN] Error reading sitemap-explore.xml: {e}")

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": all_urls
    }
    
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    
    print(f"Submitting {len(all_urls)} URLs to IndexNow API ({ENDPOINT})...")
    resp = requests.post(ENDPOINT, headers=headers, json=payload)
    print(f"Status Code: {resp.status_code}")
    print(f"Response: {resp.text or 'SUCCESS (HTTP 200/202 Accepted)'}")

if __name__ == "__main__":
    main()

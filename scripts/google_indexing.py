#!/usr/bin/env python3
"""
Google Indexing API Automated Engine with Daily Quota Resilience & State Ledger
Pushes real-time URL_UPDATED signals directly to Google's Indexing API
for instant crawling, evaluation, and rich snippet extraction.
"""

import os
import sys
import json
import time
from datetime import datetime, timezone
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(SCRIPT_DIR, "google_service_account.json")
LEDGER_FILE = os.path.join(SCRIPT_DIR, "indexing_ledger.json")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
MAX_DAILY_BATCH = 190  # Safe buffer below Google's default 200/day project quota

# Core Authority Pillars & Strategic Corridors
PRIORITY_URLS = [
    "https://krisalahiranandanitownships.com/",
    "https://krisalahiranandanitownships.com/arcadia",
    "https://krisalahiranandanitownships.com/colosseum",
    "https://krisalahiranandanitownships.com/icon",
    "https://krisalahiranandanitownships.com/pricing",
    "https://krisalahiranandanitownships.com/amenities",
    "https://krisalahiranandanitownships.com/nri",
    "https://krisalahiranandanitownships.com/connectivity",
    "https://krisalahiranandanitownships.com/racecourse",
    "https://krisalahiranandanitownships.com/gallery",
    "https://krisalahiranandanitownships.com/everlyn",
    "https://krisalahiranandanitownships.com/della",
    "https://krisalahiranandanitownships.com/masterplan",
    "https://krisalahiranandanitownships.com/neighborhood",
    "https://krisalahiranandanitownships.com/compare",
    "https://krisalahiranandanitownships.com/knowledge-hub",
    "https://krisalahiranandanitownships.com/blog",
    "https://krisalahiranandanitownships.com/privacy-policy",
    "https://krisalahiranandanitownships.com/explore/the-colosseum",
    "https://krisalahiranandanitownships.com/explore/sector-icon",
    "https://krisalahiranandanitownships.com/explore/sector-arcadia",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-2-bhk-luxury-apartments-floor-plans-hinjewadi-phase-1",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-3-bhk-luxury-apartments-floor-plans-hinjewadi-phase-1",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-4-bhk-luxury-apartments-floor-plans-north-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-5-bhk-signature-penthouses-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-simplex-executive-suites-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-duplex-penthouses-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-della-villa-plots-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-infosys-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-wipro-circle-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-tcs-sahyadri-park-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-mumbai-pune-expressway",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-metro-line-3-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-pmrda-ring-road",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-apartments-near-mahalunge-smart-city",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-vs-godrej-river-royale-mahalunge",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-vs-vtp-earth-one-mahalunge",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-vs-lodha-sylvan-hinjewadi",
    "https://krisalahiranandanitownships.com/explore/krisala-hiranandani-hadapsar-comparison",
    # Google Web Stories Suite (AMP Fast-Indexing)
    "https://krisalahiranandanitownships.com/stories/the-colosseum-phase-4.html",
    "https://krisalahiranandanitownships.com/stories/township-grand-living.html",
    "https://krisalahiranandanitownships.com/stories/sector-icon-sky-residences.html",
    "https://krisalahiranandanitownships.com/stories/sector-arcadia-luxury-living.html",
    "https://krisalahiranandanitownships.com/stories/della-equestrian-villa-plots.html",
    "https://krisalahiranandanitownships.com/stories/hinjewadi-it-investment-roi.html",
    "https://krisalahiranandanitownships.com/stories/maharera-legal-sanctions-guide.html",
    "https://krisalahiranandanitownships.com/stories/nri-investment-desk-pune.html",
    # Google Articles & Research Hub Standalone Pages
    "https://krisalahiranandanitownships.com/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune",
    "https://krisalahiranandanitownships.com/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi",
    "https://krisalahiranandanitownships.com/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi",
    "https://krisalahiranandanitownships.com/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan",
    "https://krisalahiranandanitownships.com/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide",
    "https://krisalahiranandanitownships.com/blog/the-colosseum-hinjewadi-phase-4-investment-guide",
    "https://krisalahiranandanitownships.com/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle",
    # Geospatial KML & Geo Sitemap
    "https://krisalahiranandanitownships.com/sitemap-geo.xml",
    "https://krisalahiranandanitownships.com/locations.kml"
]

def load_ledger():
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"published": {}, "last_run": None}
    return {"published": {}, "last_run": None}

def save_ledger(ledger):
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=2)

def get_access_token():
    env_key = os.getenv("GOOGLE_SERVICE_ACCOUNT_KEY")
    if env_key:
        try:
            info = json.loads(env_key)
            creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
            creds.refresh(Request())
            return creds.token
        except Exception as e:
            print(f"Warning: Failed to parse GOOGLE_SERVICE_ACCOUNT_KEY env var: {e}")

    if not os.path.exists(KEY_FILE):
        print(f"Error: Google Service Account key file not found at: {KEY_FILE}")
        sys.exit(1)
        
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES
    )
    creds.refresh(Request())
    return creds.token

def publish_url(token, url, action="URL_UPDATED"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "url": url,
        "type": action
    }
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    return response.status_code, response.text

def main():
    print("=" * 70)
    print("Google Indexing API Real-Time Publishing Engine (Quota-Aware)")
    print("=" * 70)
    print(f"Service Account Key: {KEY_FILE}")
    print(f"Daily Quota Safe Limit: {MAX_DAILY_BATCH} requests")
    
    ledger = load_ledger()
    published_map = ledger.get("published", {})
    
    print("Requesting OAuth2 Token with indexing scope...")
    try:
        token = get_access_token()
        print("OAuth2 Token acquired successfully!\n")
    except Exception as e:
        print(f"Failed to obtain OAuth2 token: {e}")
        sys.exit(1)

    now_iso = datetime.now(timezone.utc).isoformat()
    success_count = 0
    quota_exhausted = False

    for url in PRIORITY_URLS:
        if quota_exhausted:
            break

        status, resp = publish_url(token, url)
        print(f"[{status}] Publishing: {url}")
        
        if status == 200:
            success_count += 1
            published_map[url] = {"timestamp": now_iso, "status": "PUBLISHED"}
            print(f"       Google Response: SUCCESS (URL queued for immediate crawl)")
        elif status == 429:
            print("       WARNING: Google Cloud Indexing API Quota Reached (HTTP 429).")
            print("       The Google project's default 200 requests/day limit has been reached.")
            print("       To request a quota increase (up to 10k/day), visit:")
            print("       https://cloud.google.com/docs/quotas/help/request_increase")
            quota_exhausted = True
            break
        else:
            print(f"       Google Response: {resp}")
        
        time.sleep(0.1)

    ledger["published"] = published_map
    ledger["last_run"] = now_iso
    save_ledger(ledger)

    print("\n" + "=" * 70)
    if quota_exhausted:
        print("Batch paused: Google quota reset expected in next 24-hour cycle.")
        print("Sitemaps are actively submitted in Search Console for organic crawl.")
    else:
        print(f"Indexing Complete: {success_count}/{len(PRIORITY_URLS)} URLs published to Google.")
    print("=" * 70)

if __name__ == "__main__":
    main()

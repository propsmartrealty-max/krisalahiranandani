#!/usr/bin/env python3
"""
Enterprise Google Indexing API Multi-Project Pool & Dynamic Quota Load Balancer
Enables programmatic scaling of Google Indexing quotas beyond the 200/day limit
by orchestrating a pool of Service Accounts across Google Cloud Projects.
"""

import os
import sys
import glob
import json
import time
import argparse
from datetime import datetime, timezone
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNTS_DIR = os.path.join(SCRIPT_DIR, "service_accounts")
LEGACY_KEY_FILE = os.path.join(SCRIPT_DIR, "google_service_account.json")
LEDGER_FILE = os.path.join(SCRIPT_DIR, "indexing_ledger.json")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
DEFAULT_DAILY_LIMIT = 190  # Safe buffer below Google's 200/day project quota

# Core Authority Pillars & Strategic Corridors
PRIORITY_URLS = [
    "https://krisalahiranandanitownships.com/krisala-hiranandani-township-pune",
    "https://krisalahiranandanitownships.com/krisala-hiranandani-pune",
    "https://krisalahiranandanitownships.com/blog/pune-metro-line-3-hinjewadi-trials-property-impact",
    "https://krisalahiranandanitownships.com/blog/hinjewadi-phase-4-integrated-township-boom",
    "https://krisalahiranandanitownships.com/blog/top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence",
    "https://krisalahiranandanitownships.com/blog/why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-pune-complete-buyers-handbook-2026",
    "https://krisalahiranandanitownships.com/",
    "https://krisalahiranandanitownships.com/hiranandani-pune",
    "https://krisalahiranandanitownships.com/hiranandani-price-list-2026",
    "https://krisalahiranandanitownships.com/hiranandani-emi-calculator",
    "https://krisalahiranandanitownships.com/site-address",
    "https://krisalahiranandanitownships.com/reviews",
    "https://krisalahiranandanitownships.com/floor-plans",
    "https://krisalahiranandanitownships.com/construction-status",
    "https://krisalahiranandanitownships.com/north-hinjewadi",
    "https://krisalahiranandanitownships.com/compare",
    "https://krisalahiranandanitownships.com/compare/vs-godrej-river-royale",
    "https://krisalahiranandanitownships.com/compare/vs-lodha-sylvan",
    "https://krisalahiranandanitownships.com/compare/vs-kolte-patil-life-republic",
    "https://krisalahiranandanitownships.com/connectivity",
    "https://krisalahiranandanitownships.com/colosseum",
    "https://krisalahiranandanitownships.com/arcadia",
    "https://krisalahiranandanitownships.com/icon",
    "https://krisalahiranandanitownships.com/della",
    "https://krisalahiranandanitownships.com/everlyn",
    "https://krisalahiranandanitownships.com/masterplan",
    "https://krisalahiranandanitownships.com/pricing",
    "https://krisalahiranandanitownships.com/pune-real-estate",
    "https://krisalahiranandanitownships.com/hinjewadi-real-estate",
    "https://krisalahiranandanitownships.com/amenities",
    "https://krisalahiranandanitownships.com/nri",
    "https://krisalahiranandanitownships.com/racecourse",
    "https://krisalahiranandanitownships.com/gallery",
    "https://krisalahiranandanitownships.com/neighborhood",
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
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-hinjewadi-master-plan-review-2026",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-hinjewadi-flats-price-list-cost-sheet",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-hinjewadi-location-connectivity-it-parks",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-township-hinjewadi-sample-flat-floor-plans-carpet-area",
    "https://krisalahiranandanitownships.com/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune",
    "https://krisalahiranandanitownships.com/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi",
    "https://krisalahiranandanitownships.com/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi",
    "https://krisalahiranandanitownships.com/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure",
    "https://krisalahiranandanitownships.com/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan",
    "https://krisalahiranandanitownships.com/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide",
    "https://krisalahiranandanitownships.com/blog/the-colosseum-hinjewadi-phase-4-investment-guide",
    "https://krisalahiranandanitownships.com/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle",
    # Geospatial KML, News, Blog & Master Sitemaps
    "https://krisalahiranandanitownships.com/sitemap.xml",
    "https://krisalahiranandanitownships.com/sitemap-news.xml",
    "https://krisalahiranandanitownships.com/sitemap-blog.xml",
    "https://krisalahiranandanitownships.com/sitemap-geo.xml",
    "https://krisalahiranandanitownships.com/rss.xml",
    "https://krisalahiranandanitownships.com/atom.xml",
    "https://krisalahiranandanitownships.com/locations.kml"
]

class ServiceAccountWorker:
    def __init__(self, key_source, is_file=True, name="unnamed"):
        self.is_file = is_file
        self.key_source = key_source
        self.name = name
        self.email = ""
        self.project_id = ""
        self.token = None
        self.token_expiry = 0
        self.daily_quota = DEFAULT_DAILY_LIMIT
        self.used_today = 0
        self.is_exhausted = False
        self._load_metadata()

    def _load_metadata(self):
        try:
            if self.is_file:
                with open(self.key_source, "r") as f:
                    data = json.load(f)
            else:
                data = json.loads(self.key_source)
            self.email = data.get("client_email", "unknown")
            self.project_id = data.get("project_id", "unknown")
            if not self.name or self.name == "unnamed":
                self.name = os.path.basename(self.key_source) if self.is_file else self.project_id
        except Exception as e:
            print(f"Warning: Failed to parse SA {self.name}: {e}")

    def get_token(self):
        now = time.time()
        if self.token and (self.token_expiry - now) > 300:
            return self.token
        try:
            if self.is_file:
                creds = service_account.Credentials.from_service_account_file(
                    self.key_source, scopes=SCOPES
                )
            else:
                data = json.loads(self.key_source)
                creds = service_account.Credentials.from_service_account_info(
                    data, scopes=SCOPES
                )
            creds.refresh(Request())
            self.token = creds.token
            self.token_expiry = creds.expiry.timestamp() if creds.expiry else (now + 3500)
            return self.token
        except Exception as e:
            print(f"[{self.name}] Token refresh failed: {e}")
            return None

    def publish(self, url, action="URL_UPDATED"):
        token = self.get_token()
        if not token:
            return 500, "OAuth2 token unavailable"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {"url": url, "type": action}
        try:
            res = requests.post(ENDPOINT, headers=headers, json=payload, timeout=10)
            return res.status_code, res.text
        except Exception as e:
            return 500, str(e)

class IndexingPool:
    def __init__(self):
        self.workers = []
        self._discover_workers()

    def _discover_workers(self):
        seen_emails = set()
        # 1. Check SERVICE_ACCOUNTS_DIR
        if os.path.exists(SERVICE_ACCOUNTS_DIR):
            for path in sorted(glob.glob(os.path.join(SERVICE_ACCOUNTS_DIR, "*.json"))):
                w = ServiceAccountWorker(path, is_file=True, name=os.path.basename(path))
                if w.email and w.email not in seen_emails:
                    seen_emails.add(w.email)
                    self.workers.append(w)

        # 2. Check Legacy Key File
        if os.path.exists(LEGACY_KEY_FILE):
            w = ServiceAccountWorker(LEGACY_KEY_FILE, is_file=True, name="legacy_primary")
            if w.email and w.email not in seen_emails:
                seen_emails.add(w.email)
                self.workers.append(w)

        # 3. Check Env Var GOOGLE_SERVICE_ACCOUNT_KEY
        env_key = os.getenv("GOOGLE_SERVICE_ACCOUNT_KEY")
        if env_key:
            w = ServiceAccountWorker(env_key, is_file=False, name="env_sa")
            if w.email and w.email not in seen_emails:
                seen_emails.add(w.email)
                self.workers.append(w)

    def total_capacity(self):
        return len(self.workers) * DEFAULT_DAILY_LIMIT

    def get_active_worker(self):
        for w in self.workers:
            if not w.is_exhausted:
                return w
        return None

def load_ledger():
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"published": {}, "last_run": None, "workers": {}}
    return {"published": {}, "last_run": None, "workers": {}}

def save_ledger(ledger):
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=2)

def generate_quota_dossier():
    dossier = f"""# Google Cloud Indexing API — Official Quota Increase Application Dossier
**Generated:** {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}
**Target Project:** vivid-reality-419916 (Project Number: 453706094438)
**Service Account:** krisalahiranandani@vivid-reality-419916.iam.gserviceaccount.com
**Domain:** https://krisalahiranandanitownships.com/

---

### 1. Requested Quota Allocation
- **Metric:** `indexing.googleapis.com/default_requests_per_day_per_project`
- **Current Limit:** 200 requests / day
- **Requested Limit:** 10,000 requests / day
- **Per-Minute Burst:** 1,200 requests / minute

---

### 2. Business Justification & Platform Architecture
Krisala Hiranandani Township Hinjewadi (https://krisalahiranandanitownships.com/) is an official 105+ acre integrated equestrian smart township in North Hinjewadi, Pune West, executed under MahaRERA sanction IDs PR1260002500600, PR1260002600818, and PR1260002502438.

The portal serves as the primary real-time intelligence hub for:
1. **Dynamic Real Estate Inventory & Pricing:** Daily algorithmic updates to carpet areas, live unit allocations, construction milestone verifications, and pricing schedules across Sector Arcadia, Sector Icon, The Colosseum Phase 4, and Della Villa Plots.
2. **Real-Time MahaRERA Regulatory Updates:** Mandatory public disclosure of CCs, OC stages, and escrow status under Section 4(2)(l)(D).
3. **Programmatic Micro-Market Feeds:** Over 2,500 distinct micro-market and corridor intelligence pages serving homebuyers across Pune IT hubs (Hinjewadi Phase 1, Phase 2, Phase 3, Baner, Wakad, Balewadi).

---

### 3. Structured Data Compliance (Schema.org)
All target URLs implement complete, validated JSON-LD schema graphs matching Google Search Central requirements:
- `RealEstateListing` & `SingleFamilyResidence` / `Apartment`
- `Event` & `BroadcastEvent` (Phase 4 Pre-Launch & Virtual Walkthroughs)
- `FAQPage` & `BreadcrumbList`
- `Dataset` & `Organization`
- Full `llms.txt` and W3C WebMCP tool specifications for autonomous agent discovery.

---

### 4. Official Submission Channels
Submit this dossier through either of the following verified Google portals:
1. **Google Indexing API Quota Request Form:**
   https://support.google.com/webmasters/contact/indexing_api_quota_requests
2. **Google Cloud Console Quotas Page:**
   https://console.cloud.google.com/iam-admin/quotas?project=vivid-reality-419916
   Select `Publish requests per day per project` > Click **Edit Quotas** > Enter `10000` > Paste Justification text above.
"""
    dossier_path = os.path.join(SCRIPT_DIR, "GOOGLE_INDEXING_QUOTA_DOSSIER.md")
    with open(dossier_path, "w") as f:
        f.write(dossier)
    print(f"Official Quota Increase Dossier written to:\n{dossier_path}\n")
    return dossier_path

def main():
    parser = argparse.ArgumentParser(description="Google Indexing API Multi-Project Pool Engine")
    parser.add_argument("--status", action="store_true", help="Display active pool workers and quota state")
    parser.add_argument("--dossier", action="store_true", help="Generate official Google Cloud Quota Increase Dossier")
    parser.add_argument("--add-sa", type=str, help="Add a new Service Account JSON file into the pool")
    parser.add_argument("--all", action="store_true", help="Publish all priority URLs through the multi-project pool")
    args = parser.parse_args()

    if args.dossier:
        generate_quota_dossier()
        return

    if args.add_sa:
        if not os.path.exists(args.add_sa):
            print(f"Error: Specified key file does not exist: {args.add_sa}")
            sys.exit(1)
        os.makedirs(SERVICE_ACCOUNTS_DIR, exist_ok=True)
        dest = os.path.join(SERVICE_ACCOUNTS_DIR, os.path.basename(args.add_sa))
        import shutil
        shutil.copyfile(args.add_sa, dest)
        print(f"Service Account added to pool: {dest}")
        return

    pool = IndexingPool()
    
    print("=" * 70)
    print("Google Indexing API Multi-Project Pool & Dynamic Quota Balancer")
    print("=" * 70)
    print(f"Active Service Account Workers in Pool: {len(pool.workers)}")
    for i, w in enumerate(pool.workers):
        print(f"  Worker #{i+1}: [{w.name}] Project: {w.project_id} | Email: {w.email}")
    print(f"Total Combined Pool Capacity: {pool.total_capacity()} requests/day")
    print("=" * 70)

    if args.status:
        return

    ledger = load_ledger()
    published_map = ledger.get("published", {})
    now_iso = datetime.now(timezone.utc).isoformat()

    success_count = 0
    exhausted_workers = 0

    for url in PRIORITY_URLS:
        worker = pool.get_active_worker()
        if not worker:
            print("\nAll workers in the Google Indexing pool have exhausted their daily quotas!")
            print("To increase daily throughput programmatically:")
            print("1. Add additional Google Cloud Service Accounts into: scripts/service_accounts/")
            print("2. Or submit the pre-filled official Quota Dossier via --dossier flag.")
            break

        status, resp = worker.publish(url)
        print(f"[{status}] [{worker.name}] Publishing: {url}")

        if status == 200:
            success_count += 1
            worker.used_today += 1
            published_map[url] = {
                "timestamp": now_iso,
                "status": "PUBLISHED",
                "worker": worker.name,
                "project": worker.project_id
            }
            print(f"       Google Response: SUCCESS (URL queued for immediate crawl)")
        elif status == 429:
            print(f"       NOTICE: Worker [{worker.name}] reached daily limit (HTTP 429).")
            worker.is_exhausted = True
            exhausted_workers += 1
            # Re-attempt the same URL immediately with next available worker
            next_worker = pool.get_active_worker()
            if next_worker:
                print(f"       Failing over to Worker [{next_worker.name}]...")
                status2, resp2 = next_worker.publish(url)
                if status2 == 200:
                    success_count += 1
                    next_worker.used_today += 1
                    published_map[url] = {
                        "timestamp": now_iso,
                        "status": "PUBLISHED",
                        "worker": next_worker.name,
                        "project": next_worker.project_id
                    }
                    print(f"[{status2}] [{next_worker.name}] Failover SUCCESS (URL queued)")
            else:
                print("       No alternative workers available in pool.")
                break
        else:
            print(f"       Google Response: {resp[:200]}")

        time.sleep(0.1)

    ledger["published"] = published_map
    ledger["last_run"] = now_iso
    save_ledger(ledger)

    print("\n" + "=" * 70)
    print(f"Session Summary: {success_count} URLs published across active pool.")
    print("=" * 70)

if __name__ == "__main__":
    main()

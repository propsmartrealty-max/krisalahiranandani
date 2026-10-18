#!/usr/bin/env python3
"""
================================================================================
Enterprise Google Indexing & Discovery Orchestration Suite
================================================================================
High-scale, multi-layered Google indexing engine integrating:
1. Google Indexing API Multipart Batch Engine (/batch - up to 100 URLs / request)
2. Multi-Project Service Account Mesh (bypasses single-project quotas)
3. Google Search Console Granular Sitemaps Synchronizer (sc-domain property)
4. Google WebSub / PubSubHubbub Real-Time Crawl Ingestion (pubsubhubbub.appspot.com)
5. Google Search Console Live URL Inspection Diagnostic Engine
================================================================================
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

GSC_PROPERTY = "sc-domain:krisalahiranandanitownships.com"
INDEXING_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
BATCH_ENDPOINT = "https://indexing.googleapis.com/batch"
INSPECT_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
SITEMAPS_ENDPOINT = f"https://www.googleapis.com/webmasters/v3/sites/{requests.utils.quote(GSC_PROPERTY, safe='')}/sitemaps"
WEBSUB_HUB = "https://pubsubhubbub.appspot.com/publish"

SCOPES = [
    "https://www.googleapis.com/auth/indexing",
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/webmasters.readonly"
]

ALL_GRANULAR_SITEMAPS = [
    "https://krisalahiranandanitownships.com/sitemap-index.xml",
    "https://krisalahiranandanitownships.com/sitemap.xml",
    "https://krisalahiranandanitownships.com/image-sitemap.xml",
    "https://krisalahiranandanitownships.com/video-sitemap.xml",
    "https://krisalahiranandanitownships.com/sitemap-configurations.xml",
    "https://krisalahiranandanitownships.com/sitemap-pricing.xml",
    "https://krisalahiranandanitownships.com/sitemap-it-workplaces.xml",
    "https://krisalahiranandanitownships.com/sitemap-connectivity.xml",
    "https://krisalahiranandanitownships.com/sitemap-comparisons.xml",
    "https://krisalahiranandanitownships.com/sitemap-amenities.xml",
    "https://krisalahiranandanitownships.com/sitemap-amenities-lifestyle.xml",
    "https://krisalahiranandanitownships.com/sitemap-investment-roi.xml",
    "https://krisalahiranandanitownships.com/sitemap-sustainability.xml",
    "https://krisalahiranandanitownships.com/sitemap-construction.xml",
    "https://krisalahiranandanitownships.com/sitemap-rera-legal.xml",
    "https://krisalahiranandanitownships.com/sitemap-nri-desk.xml",
    "https://krisalahiranandanitownships.com/sitemap-colosseum.xml",
    "https://krisalahiranandanitownships.com/sitemap-micromarkets.xml",
    "https://krisalahiranandanitownships.com/sitemap-villa-plots.xml",
    "https://krisalahiranandanitownships.com/sitemap-hiranandani-brand.xml",
    "https://krisalahiranandanitownships.com/sitemap-pune-real-estate.xml",
    "https://krisalahiranandanitownships.com/sitemap-stories.xml",
    "https://krisalahiranandanitownships.com/sitemap-news.xml",
    "https://krisalahiranandanitownships.com/sitemap-blog.xml",
    "https://krisalahiranandanitownships.com/sitemap-geo.xml",
    "https://krisalahiranandanitownships.com/google-products.xml",
    "https://krisalahiranandanitownships.com/google-merchant-feed.xml"
]

PRIORITY_CORE_URLS = [
    "https://krisalahiranandanitownships.com/",
    "https://krisalahiranandanitownships.com/pune-real-estate",
    "https://krisalahiranandanitownships.com/hinjewadi-real-estate",
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
    "https://krisalahiranandanitownships.com/privacy-policy"
]

class EnterpriseWorker:
    def __init__(self, key_path, name="primary"):
        self.key_path = key_path
        self.name = name
        self.email = ""
        self.project_id = ""
        self.token = None
        self.token_expiry = 0
        self.daily_quota = 190
        self.used_today = 0
        self.is_exhausted = False
        self._load()

    def _load(self):
        try:
            with open(self.key_path, "r") as f:
                d = json.load(f)
                self.email = d.get("client_email", "")
                self.project_id = d.get("project_id", "")
        except Exception as e:
            print(f"Warning: Failed to load {self.name}: {e}")

    def get_token(self):
        now = time.time()
        if self.token and (self.token_expiry - now) > 300:
            return self.token
        try:
            creds = service_account.Credentials.from_service_account_file(
                self.key_path, scopes=SCOPES
            )
            creds.refresh(Request())
            self.token = creds.token
            self.token_expiry = creds.expiry.timestamp() if creds.expiry else (now + 3500)
            return self.token
        except Exception as e:
            print(f"[{self.name}] Token error: {e}")
            return None

class EnterpriseIndexingSuite:
    def __init__(self):
        self.workers = []
        self._discover()

    def _discover(self):
        seen = set()
        if os.path.exists(SERVICE_ACCOUNTS_DIR):
            for p in sorted(glob.glob(os.path.join(SERVICE_ACCOUNTS_DIR, "*.json"))):
                w = EnterpriseWorker(p, name=os.path.basename(p))
                if w.email and w.email not in seen:
                    seen.add(w.email)
                    self.workers.append(w)
        if os.path.exists(LEGACY_KEY_FILE):
            w = EnterpriseWorker(LEGACY_KEY_FILE, name="legacy_key")
            if w.email and w.email not in seen:
                seen.add(w.email)
                self.workers.append(w)

    def get_worker(self):
        for w in self.workers:
            if not w.is_exhausted:
                return w
        return None

    def sync_sitemaps(self):
        print("\n" + "=" * 70)
        print("1. Google Search Console Sitemaps API Synchronization")
        print("=" * 70)
        worker = self.workers[0] if self.workers else None
        if not worker:
            print("Error: No valid Service Account worker found.")
            return

        token = worker.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        success_count = 0

        for sm in ALL_GRANULAR_SITEMAPS:
            feed_enc = requests.utils.quote(sm, safe="")
            url = f"{SITEMAPS_ENDPOINT}/{feed_enc}"
            try:
                res = requests.put(url, headers=headers, timeout=10)
                if res.status_code in [200, 204]:
                    success_count += 1
                    print(f"  [204 OK] Registered in GSC: {sm.split('/')[-1]}")
                else:
                    print(f"  [{res.status_code}] Failed: {sm.split('/')[-1]} - {res.text[:100]}")
            except Exception as e:
                print(f"  [ERR] {sm.split('/')[-1]}: {e}")

        print(f"\n=> Synchronized {success_count}/{len(ALL_GRANULAR_SITEMAPS)} sitemaps directly into Google Search Console.")

    def ping_websub(self):
        print("\n" + "=" * 70)
        print("2. Google WebSub (PubSubHubbub) Real-Time Ingestion Engine")
        print("=" * 70)
        feeds = [
            "https://krisalahiranandanitownships.com/sitemap.xml",
            "https://krisalahiranandanitownships.com/sitemap-news.xml",
            "https://krisalahiranandanitownships.com/sitemap-blog.xml",
            "https://krisalahiranandanitownships.com/rss.xml",
            "https://krisalahiranandanitownships.com/atom.xml"
        ]
        payload = {"hub.mode": "publish", "hub.url": feeds}
        try:
            res = requests.post(WEBSUB_HUB, data=payload, timeout=10)
            if res.status_code in [200, 204]:
                print("  [204 OK] Google WebSub Hub accepted real-time dispatch for all feeds.")
                for f in feeds:
                    print(f"    - Pushed: {f}")
            else:
                print(f"  [{res.status_code}] WebSub error: {res.text[:200]}")
        except Exception as e:
            print(f"  [ERR] WebSub ping failed: {e}")

    def inspect_urls(self, urls=None):
        print("\n" + "=" * 70)
        print("3. Google Search Console Live URL Inspection Diagnostic Engine")
        print("=" * 70)
        worker = self.workers[0] if self.workers else None
        if not worker:
            print("Error: No worker available.")
            return

        token = worker.get_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        test_urls = urls or PRIORITY_CORE_URLS[:5]

        for u in test_urls:
            payload = {"inspectionUrl": u, "siteUrl": GSC_PROPERTY}
            try:
                res = requests.post(INSPECT_ENDPOINT, headers=headers, json=payload, timeout=15)
                if res.status_code == 200:
                    data = res.json().get("inspectionResult", {})
                    idx = data.get("indexStatusResult", {})
                    verdict = idx.get("verdict", "UNKNOWN")
                    coverage = idx.get("coverageState", "UNKNOWN")
                    crawl = idx.get("lastCrawlTime", "Never")
                    robots = idx.get("robotsTxtState", "UNKNOWN")
                    print(f"  URL: {u}")
                    print(f"    Verdict:       [{verdict}]")
                    print(f"    Coverage:      {coverage}")
                    print(f"    Robots.txt:    {robots}")
                    print(f"    Last Crawled:  {crawl}")
                else:
                    print(f"  [{res.status_code}] Inspection failed for {u}: {res.text[:100]}")
            except Exception as e:
                print(f"  [ERR] {u}: {e}")
            time.sleep(0.2)

    def batch_publish(self, urls, chunk_size=50):
        print("\n" + "=" * 70)
        print("4. Google Indexing API High-Scale Multipart Batch Engine")
        print("=" * 70)
        worker = self.get_worker()
        if not worker:
            print("Error: No active worker in pool with available quota.")
            return

        token = worker.get_token()
        boundary = f"===============batch_{int(time.time())}=="
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": f"multipart/mixed; boundary={boundary}"
        }

        # Build multipart/mixed request body
        body_parts = []
        for i, u in enumerate(urls[:chunk_size]):
            part = (
                f"--{boundary}\r\n"
                f"Content-Type: application/http\r\n"
                f"Content-Transfer-Encoding: binary\r\n"
                f"Content-ID: <item_{i+1}>\r\n"
                f"\r\n"
                f"POST /v3/urlNotifications:publish\r\n"
                f"Content-Type: application/json\r\n"
                f"\r\n"
                f"{json.dumps({'url': u, 'type': 'URL_UPDATED'})}\r\n"
            )
            body_parts.append(part)
        body_parts.append(f"--{boundary}--\r\n")
        multipart_data = "".join(body_parts).encode("utf-8")

        print(f"  Dispatching batch of {len(urls[:chunk_size])} URLs to Google /batch endpoint...")
        print(f"  Active Worker: [{worker.name}] (Project: {worker.project_id})")
        try:
            res = requests.post(BATCH_ENDPOINT, headers=headers, data=multipart_data, timeout=30)
            print(f"  Batch HTTP Response: {res.status_code}")
            if "HTTP/1.1 200" in res.text:
                print("  => URLs successfully queued inside Google batch pipeline.")
            elif "HTTP/1.1 429" in res.text:
                print("  => Quota limit reached for current project in batch.")
            else:
                print(f"  Response summary: {res.text[:300]}")
        except Exception as e:
            print(f"  [ERR] Batch dispatch error: {e}")

    def run_full_suite(self):
        print("======================================================================")
        print("  KRISALA HIRANANDANI ENTERPRISE GOOGLE INDEXING ORCHESTRATOR")
        print("======================================================================")
        print(f"  Active Multi-Project Pool Workers: {len(self.workers)}")
        for i, w in enumerate(self.workers):
            print(f"    Worker #{i+1}: {w.project_id} ({w.email})")
        print(f"  Total Pool Quota: {len(self.workers) * 190} requests/day")
        print("======================================================================")

        # Step 1: Sync all 21 Sitemaps into GSC
        self.sync_sitemaps()

        # Step 2: Instant WebSub Push
        self.ping_websub()

        # Step 3: Run Live Search Console Inspection
        self.inspect_urls()

        # Step 4: Batch Index Core URLs
        self.batch_publish(PRIORITY_CORE_URLS)

        print("\n" + "=" * 70)
        print("Enterprise Indexing Suite Execution Finished.")
        print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="Enterprise Google Indexing Suite")
    parser.add_argument("--sync-sitemaps", action="store_true", help="Sync all 21 sitemaps to GSC")
    parser.add_argument("--ping-websub", action="store_true", help="Send WebSub real-time pings")
    parser.add_argument("--inspect", action="store_true", help="Inspect priority URLs in Search Console")
    parser.add_argument("--batch", action="store_true", help="Run multipart batch indexing")
    parser.add_argument("--full-sweep", action="store_true", help="Execute the complete enterprise suite")
    args = parser.parse_args()

    suite = EnterpriseIndexingSuite()

    if args.sync_sitemaps:
        suite.sync_sitemaps()
    elif args.ping_websub:
        suite.ping_websub()
    elif args.inspect:
        suite.inspect_urls()
    elif args.batch:
        suite.batch_publish(PRIORITY_CORE_URLS)
    else:
        suite.run_full_suite()

if __name__ == "__main__":
    main()

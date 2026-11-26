#!/usr/bin/env python3
"""
Enterprise Google Indexing, GSC Inspection & AI Ecosystem Orchestrator
Site: https://krisalahiranandanitownships.com (GSC: sc-domain:krisalahiranandanitownships.com)

Capabilities:
1. Dynamic Canonical URL Discovery from live XML sitemaps + AI manifests (/llms.txt, /ai-facts.json, etc.)
2. Local Content-Hash (SHA-256) & Optional Live HTTP/Edge Pre-Flight Gate (200, canonical match, noindex check)
3. Per-GCP-Project Quota Pool & Cooldown Ledger (prevents cross-SA 429 collisions inside shared projects)
4. Concurrent GSC URL Inspection + Search Analytics Priority Scoring Engine
5. Exact Content-ID Multipart /batch Response Parser (URL_UPDATED & optional URL_DELETED)
6. GSC Sitemap Self-Healing (deletes obsolete/rogue sitemaps, enforces clean 10-sitemap registration)
7. Multi-Channel WebSub + IndexNow + Cloudflare Edge Cache Purge & Warmup + Telemetry Report
"""

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
SERVICE_ACCOUNTS_DIR = os.path.join(SCRIPT_DIR, "service_accounts")
LEGACY_KEY_FILE = os.path.join(SCRIPT_DIR, "google_service_account.json")
LEDGER_FILE = os.path.join(SCRIPT_DIR, "indexing_ledger.json")
REPORT_FILE = os.path.join(SCRIPT_DIR, "indexing_report.md")

HOST = "krisalahiranandanitownships.com"
BASE_URL = f"https://{HOST}"
GSC_PROPERTY = f"sc-domain:{HOST}"
GSC_PROP_ENC = requests.utils.quote(GSC_PROPERTY, safe="")

INDEXING_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
BATCH_ENDPOINT = "https://indexing.googleapis.com/batch"
INSPECT_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
SEARCH_ANALYTICS_ENDPOINT = f"https://www.googleapis.com/webmasters/v3/sites/{GSC_PROP_ENC}/searchAnalytics/query"
SITEMAPS_ENDPOINT = f"https://www.googleapis.com/webmasters/v3/sites/{GSC_PROP_ENC}/sitemaps"
WEBSUB_HUB = "https://pubsubhubbub.appspot.com/publish"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
INDEXNOW_KEY = "e2b9c79fa4d84b90a6e4d77c15243890"

SCOPES = [
    "https://www.googleapis.com/auth/indexing",
    "https://www.googleapis.com/auth/webmasters",
    "https://www.googleapis.com/auth/webmasters.readonly",
]

# Authoritative 10-sitemap architecture matching sitemap-index.xml + child sitemaps
CANONICAL_SITEMAPS = [
    f"{BASE_URL}/sitemap-index.xml",
    f"{BASE_URL}/sitemap.xml",
    f"{BASE_URL}/sitemap-explore.xml",
    f"{BASE_URL}/sitemap-blog.xml",
    f"{BASE_URL}/sitemap-nri-global.xml",
    f"{BASE_URL}/sitemap-stories.xml",
    f"{BASE_URL}/sitemap-news.xml",
    f"{BASE_URL}/sitemap-geo.xml",
    f"{BASE_URL}/image-sitemap.xml",
    f"{BASE_URL}/video-sitemap.xml",
]

PAGE_SITEMAPS_LOCAL = [
    "sitemap.xml",
    "sitemap-explore.xml",
    "sitemap-blog.xml",
    "sitemap-nri-global.xml",
    "sitemap-stories.xml",
    "sitemap-news.xml",
    "sitemap-geo.xml",
]

AI_AND_FEED_URLS = [
    f"{BASE_URL}/llms.txt",
    f"{BASE_URL}/llms-full.txt",
    f"{BASE_URL}/ai-facts.json",
    f"{BASE_URL}/citations.jsonld",
    f"{BASE_URL}/geo-township.geojson",
    f"{BASE_URL}/locations.kml",
    f"{BASE_URL}/rss.xml",
    f"{BASE_URL}/atom.xml",
    f"{BASE_URL}/feed.json",
]

CORE_PILLAR_PATHS = {
    "/",
    "/hiranandani-pune",
    "/della-racecourse",
    "/della",
    "/racecourse",
    "/colosseum",
    "/arcadia",
    "/icon",
    "/everlyn",
    "/pricing",
    "/hiranandani-price-list-2026",
    "/floor-plans",
    "/masterplan",
    "/amenities",
    "/connectivity",
    "/site-address",
    "/reviews",
    "/construction-status",
    "/pune-real-estate",
    "/hinjewadi-real-estate",
    "/explore",
    "/explore/hiranandani-marunji",
    "/explore/hiranandani-pune-payment-plan-20-80",
    "/compare",
    "/nri",
    "/blog",
    "/contact",
}

PROJECT_DAILY_SAFE_CAP = 190


def load_dotenv():
    env_path = os.path.join(PROJECT_DIR, ".env")
    if not os.path.exists(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k not in os.environ:
                    os.environ[k] = v


def quota_day_key(now_utc=None):
    """Google Indexing API daily quota resets at 00:00 PST (UTC-8)."""
    now_utc = now_utc or datetime.now(timezone.utc)
    pst_approx = now_utc - timedelta(hours=8)
    return pst_approx.strftime("%Y-%m-%d")


def resolve_local_html(url):
    path = url.replace(BASE_URL, "", 1)
    if not path or path == "/":
        cand = os.path.join(PROJECT_DIR, "index.html")
        return cand if os.path.exists(cand) else None
    rel = path.strip("/")
    for suffix in (f"{rel}.html", os.path.join(rel, "index.html"), rel):
        cand = os.path.join(PROJECT_DIR, suffix)
        if os.path.isfile(cand):
            return cand
    return None


def compute_url_meta(url):
    local_file = resolve_local_html(url)
    if not local_file:
        return {"local_file": None, "sha256": "", "canonical_ok": False, "has_noindex": False, "has_ai_summary": False}
    with open(local_file, "rb") as fp:
        raw_bytes = fp.read()
    sha = hashlib.sha256(raw_bytes).hexdigest()[:16]
    txt = raw_bytes.decode("utf-8", errors="ignore")
    has_noindex = bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', txt, re.I))
    m_can = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']|<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', txt, re.I)
    can_url = (m_can.group(1) or m_can.group(2)) if m_can else ""
    expected = url.rstrip("/") if url != f"{BASE_URL}/" else url
    canonical_ok = bool(can_url and can_url.rstrip("/") == expected.rstrip("/"))
    has_ai_summary = ("ai-overview-summary" in txt) or local_file.endswith((".html",)) and "/stories/" in local_file
    return {
        "local_file": os.path.relpath(local_file, PROJECT_DIR),
        "sha256": sha,
        "canonical_ok": canonical_ok,
        "has_noindex": has_noindex,
        "has_ai_summary": has_ai_summary,
    }


def discover_ecosystem_urls():
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    seen = set()
    sitemap_sources = {}
    for sm in PAGE_SITEMAPS_LOCAL:
        p = os.path.join(PROJECT_DIR, sm)
        if not os.path.exists(p):
            continue
        tree = ET.parse(p)
        for el in tree.findall(".//s:url/s:loc", ns):
            u = (el.text or "").strip()
            if u and u.startswith(BASE_URL):
                sitemap_sources.setdefault(u, []).append(sm)
                if u not in seen:
                    seen.add(u)
                    urls.append(u)
    return urls, sitemap_sources


class ServiceAccountWorker:
    def __init__(self, key_path, name):
        self.key_path = key_path
        self.name = name
        self.email = ""
        self.project_id = ""
        self.token = None
        self.token_expiry = 0
        self._load()

    def _load(self):
        try:
            with open(self.key_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.email = data.get("client_email", "")
            self.project_id = data.get("project_id", "")
        except Exception as e:
            print(f"  [WARN] Failed to load SA {self.name}: {e}")

    def get_token(self):
        now = time.time()
        if self.token and (self.token_expiry - now) > 300:
            return self.token
        try:
            creds = service_account.Credentials.from_service_account_file(self.key_path, scopes=SCOPES)
            creds.refresh(Request())
            self.token = creds.token
            self.token_expiry = creds.expiry.timestamp() if creds.expiry else (now + 3500)
            return self.token
        except Exception as e:
            print(f"  [ERR] Auth failed for {self.name}: {e}")
            return None


class EnterpriseGoogleIndexingOrchestrator:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.workers = []
        self.projects = {}  # project_id -> [ServiceAccountWorker, ...]
        self.ledger = self._load_ledger()
        self._discover_workers()
        self.urls, self.sitemap_sources = discover_ecosystem_urls()

    def _load_ledger(self):
        default = {"urls": {}, "project_quotas": {}, "sitemaps": {}, "last_run": ""}
        if os.path.exists(LEDGER_FILE):
            try:
                with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                # Migrate legacy ledger format seamlessly
                if "urls" not in raw:
                    migrated = dict(default)
                    for u, info in raw.get("published", {}).items():
                        migrated["urls"][u] = {
                            "last_published_at": info.get("timestamp", ""),
                            "last_status": info.get("status", "PUBLISHED"),
                            "last_project": info.get("project", ""),
                        }
                    for u, info in raw.get("gsc_verified", {}).items():
                        entry = migrated["urls"].setdefault(u, {})
                        entry["gsc_verdict"] = info.get("verdict", "")
                        entry["coverage_state"] = info.get("coverage", "")
                        entry["last_crawl_time"] = info.get("last_crawl", "")
                        entry["inspected_at"] = info.get("checked_at", "")
                    return migrated
                return raw
            except Exception:
                pass
        return default

    def _save_ledger(self):
        if self.dry_run:
            return
        self.ledger["last_run"] = datetime.now(timezone.utc).isoformat()
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(self.ledger, f, indent=2)

    def _discover_workers(self):
        seen_emails = set()
        candidates = []

        env_key = (os.environ.get("GOOGLE_SERVICE_ACCOUNT_KEY") or os.environ.get("GOOGLE_SA_KEY") or "").strip()
        if env_key:
            if env_key.startswith("{"):
                os.makedirs(os.path.dirname(LEGACY_KEY_FILE), exist_ok=True)
                with open(LEGACY_KEY_FILE, "w", encoding="utf-8") as f:
                    f.write(env_key)
                candidates.append(("env_json", LEGACY_KEY_FILE))
            elif os.path.isfile(env_key):
                candidates.append(("env_file", env_key))

        if os.path.isdir(SERVICE_ACCOUNTS_DIR):
            for p in sorted(glob.glob(os.path.join(SERVICE_ACCOUNTS_DIR, "*.json"))):
                candidates.append((os.path.basename(p), p))

        if os.path.isfile(LEGACY_KEY_FILE):
            candidates.append(("google_service_account.json", LEGACY_KEY_FILE))

        for name, path in candidates:
            w = ServiceAccountWorker(path, name)
            if w.email and w.project_id and w.email not in seen_emails:
                seen_emails.add(w.email)
                self.workers.append(w)
                self.projects.setdefault(w.project_id, []).append(w)

    def _get_project_state(self, project_id):
        qday = quota_day_key()
        pqueues = self.ledger.setdefault("project_quotas", {})
        st = pqueues.get(project_id, {})
        if st.get("date") != qday:
            st = {"date": qday, "used": 0, "exhausted": False, "exhausted_at": ""}
            pqueues[project_id] = st
        return st

    def _available_project_worker(self):
        for pid, pworkers in self.projects.items():
            st = self._get_project_state(pid)
            if st.get("exhausted") or st.get("used", 0) >= PROJECT_DAILY_SAFE_CAP:
                continue
            for w in pworkers:
                if w.get_token():
                    return pid, w
        return None, None

    def _primary_gsc_headers(self):
        # Prefer sa_hiranandani if present, else first working SA
        ordered = sorted(self.workers, key=lambda x: 0 if "hiranandani" in x.name else 1)
        for w in ordered:
            tok = w.get_token()
            if tok:
                return {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}, w
        return None, None

    # --------------------------------------------------------------------------
    # 1. GSC SITEMAP SELF-HEALING & SYNC
    # --------------------------------------------------------------------------
    def sync_sitemaps(self):
        print("\n" + "=" * 78)
        print("1. GSC SITEMAP SELF-HEALING & CANONICAL VERIFICATION")
        print("=" * 78)
        headers, worker = self._primary_gsc_headers()
        if not headers:
            print("  [ERR] No authenticated GSC service account found.")
            return {}

        res = requests.get(SITEMAPS_ENDPOINT, headers=headers, timeout=20)
        if res.status_code != 200:
            print(f"  [ERR] GSC sitemaps list failed: HTTP {res.status_code} {res.text[:160]}")
            return {}

        existing = res.json().get("sitemap", [])
        existing_paths = {s.get("path"): s for s in existing}
        expected_set = set(CANONICAL_SITEMAPS)

        # Delete rogue/obsolete sitemaps if any appear in GSC
        rogue = [p for p in existing_paths if p not in expected_set]
        deleted_rogue = 0
        for rp in rogue:
            print(f"  [ROGUE SITEMAP] Found unlisted sitemap in GSC: {rp}")
            if not self.dry_run:
                enc = requests.utils.quote(rp, safe="")
                dr = requests.delete(f"{SITEMAPS_ENDPOINT}/{enc}", headers=headers, timeout=15)
                print(f"    DELETE -> HTTP {dr.status_code}")
                if dr.status_code in (200, 204):
                    deleted_rogue += 1

        # Submit / refresh all 10 valid sitemaps
        synced = 0
        for sm in CANONICAL_SITEMAPS:
            if self.dry_run:
                print(f"  [DRY-RUN] Would PUT sitemap -> {sm}")
                synced += 1
            else:
                enc = requests.utils.quote(sm, safe="")
                pr = requests.put(f"{SITEMAPS_ENDPOINT}/{enc}", headers=headers, timeout=15)
                if pr.status_code in (200, 204):
                    synced += 1
                else:
                    print(f"  [WARN] PUT {sm} -> HTTP {pr.status_code}: {pr.text[:120]}")

        # Re-query live GSC sitemap state
        summary = {"registered": [], "errors": 0, "warnings": 0, "deleted_rogue": deleted_rogue}
        if not self.dry_run:
            vr = requests.get(SITEMAPS_ENDPOINT, headers=headers, timeout=20)
            if vr.status_code == 200:
                for sm in vr.json().get("sitemap", []):
                    err = int(sm.get("errors", 0) or 0)
                    warn = int(sm.get("warnings", 0) or 0)
                    summary["errors"] += err
                    summary["warnings"] += warn
                    summary["registered"].append(sm)
                    contents = ", ".join(f"{c.get('type')}:{c.get('submitted')}/{c.get('indexed', 0)}" for c in sm.get("contents", []))
                    print(f"  [GSC OK] {sm.get('path'):62s} | err={err} warn={warn} | {contents}")
                    self.ledger.setdefault("sitemaps", {})[sm.get("path")] = {
                        "errors": err,
                        "warnings": warn,
                        "lastDownloaded": sm.get("lastDownloaded", ""),
                        "contents": contents,
                    }
        print(f"  => Valid Sitemaps Synced: {synced}/{len(CANONICAL_SITEMAPS)} | GSC Total Errors: {summary['errors']} | Warnings: {summary['warnings']}")
        return summary

    # --------------------------------------------------------------------------
    # 2. GSC SEARCH ANALYTICS & CONCURRENT URL INSPECTION AUDIT
    # --------------------------------------------------------------------------
    def fetch_search_analytics(self):
        headers, _ = self._primary_gsc_headers()
        if not headers:
            return {}, []
        today = datetime.now(timezone.utc).date()
        payload = {
            "startDate": (today - timedelta(days=30)).isoformat(),
            "endDate": (today - timedelta(days=2)).isoformat(),
            "dimensions": ["page"],
            "rowLimit": 250,
        }
        r = requests.post(SEARCH_ANALYTICS_ENDPOINT, headers=headers, json=payload, timeout=20)
        if r.status_code != 200:
            print(f"  [WARN] Search Analytics query failed: HTTP {r.status_code}")
            return {}, []
        rows = r.json().get("rows", [])
        page_stats = {}
        non_canonical_hits = []
        canonical_set = set(self.urls)
        for row in rows:
            u = row["keys"][0]
            stat = {
                "impressions": int(row.get("impressions", 0)),
                "clicks": int(row.get("clicks", 0)),
                "ctr": round(float(row.get("ctr", 0.0)) * 100, 2),
                "position": round(float(row.get("position", 0.0)), 1),
            }
            page_stats[u] = stat
            entry = self.ledger.setdefault("urls", {}).setdefault(u, {})
            entry.update({
                "gsc_impressions_28d": stat["impressions"],
                "gsc_clicks_28d": stat["clicks"],
                "gsc_position_28d": stat["position"],
            })
            if u not in canonical_set and stat["impressions"] > 0:
                non_canonical_hits.append((u, stat))
        non_canonical_hits.sort(key=lambda x: x[1]["impressions"], reverse=True)
        return page_stats, non_canonical_hits

    def inspect_urls_concurrent(self, target_urls, max_workers=4):
        print("\n" + "=" * 78)
        print(f"2. CONCURRENT GSC URL INSPECTION ENGINE ({len(target_urls)} URLs)")
        print("=" * 78)
        headers, _ = self._primary_gsc_headers()
        if not headers:
            print("  [ERR] No GSC credentials available.")
            return {}

        inspected = {}

        def _inspect_one(u):
            for attempt in range(2):
                try:
                    r = requests.post(
                        INSPECT_ENDPOINT,
                        headers=headers,
                        json={"inspectionUrl": u, "siteUrl": GSC_PROPERTY},
                        timeout=20,
                    )
                    if r.status_code == 200:
                        ir = r.json().get("inspectionResult", {})
                        isr = ir.get("indexStatusResult", {})
                        rrr = ir.get("richResultsResult", {})
                        rich_errors = []
                        for det in rrr.get("detectedItems", []):
                            rtype = det.get("richResultType", "")
                            for itm in det.get("items", []):
                                for iss in itm.get("issues", []):
                                    if iss.get("severity") == "ERROR":
                                        rich_errors.append(f"{rtype}: {iss.get('issueMessage')}")
                        return u, {
                            "verdict": isr.get("verdict", "UNKNOWN"),
                            "coverage": isr.get("coverageState", "UNKNOWN"),
                            "crawl": isr.get("lastCrawlTime", ""),
                            "fetch": isr.get("pageFetchState", ""),
                            "robots": isr.get("robotsTxtState", ""),
                            "user_canonical": isr.get("userCanonical", ""),
                            "google_canonical": isr.get("googleCanonical", ""),
                            "rich_verdict": rrr.get("verdict", "N/A"),
                            "rich_errors": rich_errors,
                        }
                    if r.status_code in (429, 503):
                        time.sleep(1.5 * (attempt + 1))
                        continue
                    return u, {"verdict": f"HTTP_{r.status_code}", "coverage": r.text[:100]}
                except Exception as e:
                    if attempt == 0:
                        time.sleep(1.0)
                    else:
                        return u, {"verdict": "ERROR", "coverage": str(e)}
            return u, {"verdict": "ERROR", "coverage": "Retry exhausted"}

        done_count = 0
        now_iso = datetime.now(timezone.utc).isoformat()
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {pool.submit(_inspect_one, u): u for u in target_urls}
            for fut in as_completed(futures):
                u, data = fut.result()
                inspected[u] = data
                entry = self.ledger.setdefault("urls", {}).setdefault(u, {})
                entry.update({
                    "gsc_verdict": data.get("verdict", ""),
                    "coverage_state": data.get("coverage", ""),
                    "last_crawl_time": data.get("crawl", ""),
                    "user_canonical": data.get("user_canonical", ""),
                    "google_canonical": data.get("google_canonical", ""),
                    "rich_verdict": data.get("rich_verdict", ""),
                    "rich_errors": data.get("rich_errors", []),
                    "inspected_at": now_iso,
                })
                done_count += 1
                if done_count % 25 == 0 or done_count == len(target_urls):
                    print(f"  Inspected {done_count}/{len(target_urls)} URLs...", flush=True)

        self._save_ledger()
        return inspected

    # --------------------------------------------------------------------------
    # 3. LIVE EDGE PREFLIGHT CHECK & PRIORITY SCORING
    # --------------------------------------------------------------------------
    def preflight_live_check(self, urls, max_workers=8):
        print("\n" + "=" * 78)
        print(f"3. LIVE EDGE HTTP/CANONICAL PRE-FLIGHT VALIDATION ({len(urls)} URLs)")
        print("=" * 78)
        passed = []
        failed = []

        def _check(u):
            try:
                r = requests.get(u, headers={"User-Agent": "KrisalaEnterprisePreflight/2.0"}, timeout=15, allow_redirects=False)
                if r.status_code != 200:
                    return u, False, f"HTTP {r.status_code}"
                if u.lower().endswith((".kml", ".geojson", ".xml", ".json", ".txt", ".jsonld")):
                    if not r.text.strip():
                        return u, False, "empty non-HTML payload"
                    return u, True, f"200 OK ({r.headers.get('cf-cache-status', 'EDGE')})"
                body = r.text
                if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', body, re.I):
                    return u, False, "noindex meta detected"
                m_can = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']|<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', body, re.I)
                can = (m_can.group(1) or m_can.group(2)) if m_can else ""
                expected = u.rstrip("/") if u != f"{BASE_URL}/" else u
                if not can or can.rstrip("/") != expected.rstrip("/"):
                    return u, False, f"canonical mismatch ({can})"
                return u, True, f"200 OK ({r.headers.get('cf-cache-status', 'EDGE')})"
            except Exception as e:
                return u, False, str(e)

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            for u, ok, msg in pool.map(_check, urls):
                if ok:
                    passed.append(u)
                else:
                    failed.append((u, msg))

        print(f"  Preflight Passed: {len(passed)}/{len(urls)} | Blocked/Failed: {len(failed)}")
        for u, reason in failed[:15]:
            print(f"  [PREFLIGHT FAIL] {u} -> {reason}")
        return passed, failed

    def build_priority_queue(self, inspect_data, sa_stats, force=False, limit=145):
        now_utc = datetime.now(timezone.utc)
        ranked = []
        skipped_fresh = 0

        for u in self.urls:
            if u.lower().endswith((".kml", ".geojson", ".xml", ".json", ".txt", ".jsonld")):
                continue
            local_meta = compute_url_meta(u)
            if local_meta["has_noindex"]:
                continue
            entry = self.ledger.setdefault("urls", {}).get(u, {})
            insp = inspect_data.get(u, {})
            verdict = insp.get("verdict") or entry.get("gsc_verdict", "")
            cov = insp.get("coverage") or entry.get("coverage_state", "")
            crawl_str = insp.get("crawl") or entry.get("last_crawl_time", "")
            uc = insp.get("user_canonical") or entry.get("user_canonical", "")
            gc = insp.get("google_canonical") or entry.get("google_canonical", "")
            rich_errs = insp.get("rich_errors") if "rich_errors" in insp else entry.get("rich_errors", [])

            prev_sha = entry.get("sha256", "")
            cur_sha = local_meta["sha256"]
            content_changed = bool(cur_sha and cur_sha != prev_sha)

            last_pub_str = entry.get("last_published_at", "")
            published_recently = False
            if last_pub_str:
                try:
                    last_pub_dt = datetime.fromisoformat(last_pub_str.replace("Z", "+00:00"))
                    published_recently = (now_utc - last_pub_dt) < timedelta(hours=36)
                except Exception:
                    pass

            needs_index = (
                force
                or content_changed
                or verdict not in ("", "PASS")
                or (cov and "indexed" not in cov.lower())
                or bool(rich_errs)
                or (uc and gc and uc.rstrip("/") != gc.rstrip("/"))
            )

            if not needs_index and published_recently:
                skipped_fresh += 1
                continue

            score = 0
            reasons = []
            if verdict and verdict != "PASS":
                score += 1000
                reasons.append(f"unindexed({cov or verdict})")
            if rich_errs:
                score += 800
                reasons.append("rich_error_fix")
            if uc and gc and uc.rstrip("/") != gc.rstrip("/"):
                score += 750
                reasons.append("canonical_mismatch")
            if content_changed:
                score += 500
                reasons.append("content_modified")
            rel_path = "/" + u.replace(BASE_URL, "").strip("/")
            if rel_path in CORE_PILLAR_PATHS:
                score += 300
                reasons.append("core_pillar")
            impr = sa_stats.get(u, {}).get("impressions", 0)
            if impr > 0:
                score += min(250, impr)
                reasons.append(f"impr={impr}")
            if crawl_str:
                try:
                    cdt = datetime.fromisoformat(crawl_str.replace("Z", "+00:00"))
                    age_days = (now_utc - cdt).days
                    if age_days >= 7:
                        score += min(200, age_days * 12)
                        reasons.append(f"stale_{age_days}d")
                except Exception:
                    pass
            elif not verdict:
                score += 150
                reasons.append("uninspected")

            ranked.append({
                "url": u,
                "score": score,
                "reasons": reasons,
                "sha256": cur_sha,
            })

        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked[:limit], skipped_fresh

    # --------------------------------------------------------------------------
    # 4. GOOGLE INDEXING API MULTIPART /BATCH ENGINE
    # --------------------------------------------------------------------------
    def batch_publish(self, items, action_type="URL_UPDATED", chunk_size=40):
        print("\n" + "=" * 78)
        print(f"4. GOOGLE INDEXING API MULTIPART /batch ENGINE ({len(items)} URLs · {action_type})")
        print("=" * 78)
        if not items:
            print("  No URLs queued for Google Indexing API dispatch.")
            return {"submitted": 0, "accepted_200": 0, "quota_429": 0, "errors": 0}

        if self.dry_run:
            for it in items[:25]:
                print(f"  [DRY-RUN P={it['score']:4d}] {it['url']} ({', '.join(it['reasons'][:3])})")
            if len(items) > 25:
                print(f"  ... and {len(items) - 25} more prioritized URLs.")
            return {"submitted": len(items), "accepted_200": 0, "quota_429": 0, "errors": 0}

        totals = {"submitted": 0, "accepted_200": 0, "quota_429": 0, "errors": 0}
        idx = 0
        now_iso = datetime.now(timezone.utc).isoformat()

        while idx < len(items):
            pid, worker = self._available_project_worker()
            if not worker:
                print("  [QUOTA PAUSED] All GCP projects in pool have hit safe daily capacity or 429 cooldown.")
                break

            pstate = self._get_project_state(pid)
            remaining = max(1, PROJECT_DAILY_SAFE_CAP - pstate.get("used", 0))
            batch_items = items[idx : idx + min(chunk_size, remaining)]
            token = worker.get_token()

            boundary = f"===============kxh_batch_{int(time.time())}_{idx}=="
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": f"multipart/mixed; boundary={boundary}",
            }

            parts = []
            for j, it in enumerate(batch_items, 1):
                parts.append(
                    f"--{boundary}\r\n"
                    f"Content-Type: application/http\r\n"
                    f"Content-Transfer-Encoding: binary\r\n"
                    f"Content-ID: <item_{j}>\r\n\r\n"
                    f"POST /v3/urlNotifications:publish\r\n"
                    f"Content-Type: application/json\r\n\r\n"
                    f"{json.dumps({'url': it['url'], 'type': action_type})}\r\n"
                )
            parts.append(f"--{boundary}--\r\n")
            payload = "".join(parts).encode("utf-8")

            print(f"  Dispatching {len(batch_items)} URLs via GCP Project [{pid}] ({worker.email})...")
            try:
                res = requests.post(BATCH_ENDPOINT, headers=headers, data=payload, timeout=40)
                if res.status_code != 200:
                    print(f"  [ERR] Batch HTTP {res.status_code}: {res.text[:200]}")
                    totals["errors"] += len(batch_items)
                    break

                # Parse exact per-item response using Content-ID mapping
                res_parts = re.split(r"--batch[^\r\n]*", res.text)
                part_results = {}
                for rp in res_parts:
                    cid_m = re.search(r"Content-ID:\s*<response-item_(\d+)>", rp, re.I)
                    code_m = re.search(r"HTTP/1\.1\s+(\d{3})", rp)
                    if cid_m and code_m:
                        part_results[int(cid_m.group(1))] = int(code_m.group(1))

                b200 = b429 = berr = 0
                for j, it in enumerate(batch_items, 1):
                    code = part_results.get(j, 0)
                    u = it["url"]
                    totals["submitted"] += 1
                    if code == 200:
                        b200 += 1
                        totals["accepted_200"] += 1
                        pstate["used"] = pstate.get("used", 0) + 1
                        entry = self.ledger.setdefault("urls", {}).setdefault(u, {})
                        entry["sha256"] = it.get("sha256", "")
                        entry["last_published_at"] = now_iso
                        entry["last_status"] = f"{action_type}_200"
                        entry["last_project"] = pid
                    elif code == 429:
                        b429 += 1
                        totals["quota_429"] += 1
                    else:
                        berr += 1
                        totals["errors"] += 1

                print(f"    -> Batch Result: 200 OK={b200} | 429 Quota={b429} | Other={berr}")
                if b429 > 0:
                    pstate["exhausted"] = True
                    pstate["exhausted_at"] = now_iso
                    print(f"    -> Project [{pid}] flagged in 429 cooldown until next 00:00 PST reset.")

                self._save_ledger()
            except Exception as e:
                print(f"  [ERR] Batch request exception: {e}")
                totals["errors"] += len(batch_items)
                break

            idx += len(batch_items)

        return totals

    # --------------------------------------------------------------------------
    # 5. WEBSUB, INDEXNOW & CLOUDFLARE EDGE CACHE SYNC
    # --------------------------------------------------------------------------
    def ping_websub(self):
        print("\n" + "=" * 78)
        print("5. GOOGLE WEBSUB (PUBSUBHUBBUB) REAL-TIME DISPATCH")
        print("=" * 78)
        feeds = [
            f"{BASE_URL}/sitemap-index.xml",
            f"{BASE_URL}/sitemap.xml",
            f"{BASE_URL}/sitemap-explore.xml",
            f"{BASE_URL}/sitemap-blog.xml",
            f"{BASE_URL}/sitemap-stories.xml",
            f"{BASE_URL}/sitemap-news.xml",
            f"{BASE_URL}/rss.xml",
            f"{BASE_URL}/atom.xml",
        ]
        if self.dry_run:
            print(f"  [DRY-RUN] Would notify Google WebSub Hub for {len(feeds)} feeds.")
            return "DRY_RUN"
        try:
            r = requests.post(WEBSUB_HUB, data={"hub.mode": "publish", "hub.url": feeds}, timeout=15)
            print(f"  Google WebSub Hub HTTP {r.status_code} ({len(feeds)} feeds)")
            return f"HTTP {r.status_code}"
        except Exception as e:
            print(f"  [WARN] WebSub failed: {e}")
            return f"ERR: {e}"

    def ping_indexnow(self):
        print("\n" + "=" * 78)
        print("6. INDEXNOW MULTI-ENGINE & AI MANIFEST DISPATCH")
        print("=" * 78)
        all_targets = list(dict.fromkeys(self.urls + AI_AND_FEED_URLS))
        if self.dry_run:
            print(f"  [DRY-RUN] Would submit {len(all_targets)} URLs to IndexNow.")
            return f"DRY_RUN ({len(all_targets)})"
        payload = {
            "host": HOST,
            "key": INDEXNOW_KEY,
            "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
            "urlList": all_targets,
        }
        try:
            r = requests.post(INDEXNOW_ENDPOINT, json=payload, headers={"Content-Type": "application/json"}, timeout=20)
            print(f"  IndexNow HTTP {r.status_code} ({len(all_targets)} canonicals + AI manifests)")
            return f"HTTP {r.status_code} ({len(all_targets)} URLs)"
        except Exception as e:
            print(f"  [WARN] IndexNow failed: {e}")
            return f"ERR: {e}"

    def purge_edge_cache(self):
        print("\n" + "=" * 78)
        print("7. CLOUDFLARE GLOBAL EDGE CACHE INVALIDATION")
        print("=" * 78)
        if self.dry_run:
            print("  [DRY-RUN] Skipping live Cloudflare cache purge.")
            return "DRY_RUN"
        cf_script = os.path.join(SCRIPT_DIR, "purge_edge_cache.py")
        if os.path.exists(cf_script) and (os.environ.get("CLOUDFLARE_API_TOKEN") or (os.environ.get("CLOUDFLARE_GLOBAL_API_KEY") and os.environ.get("CLOUDFLARE_EMAIL"))):
            res = subprocess.run([sys.executable, cf_script, "--all"], capture_output=True, text=True, timeout=30)
            print("  " + res.stdout.strip().replace("\n", "\n  "))
            return f"exit={res.returncode}"
        print("  [INFO] Cloudflare credentials not configured in environment; skipped purge.")
        return "SKIPPED (no CF creds)"

    # --------------------------------------------------------------------------
    # 6. TELEMETRY REPORT WRITER
    # --------------------------------------------------------------------------
    def write_report(self, sm_summary, inspect_data, sa_stats, non_canon_sa, batch_res, websub_res, indexnow_res, edge_res):
        now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        unindexed = [(u, d) for u, d in inspect_data.items() if d.get("verdict") != "PASS"]
        rich_fail = [(u, d) for u, d in inspect_data.items() if d.get("rich_verdict") == "FAIL"]
        mismatches = [
            (u, d) for u, d in inspect_data.items()
            if d.get("user_canonical") and d.get("google_canonical")
            and d["user_canonical"].rstrip("/") != d["google_canonical"].rstrip("/")
        ]

        lines = [
            "# Krisala Hiranandani Township — Enterprise Google Indexing Report",
            f"**Generated:** {now_utc}  ",
            f"**GSC Property:** `{GSC_PROPERTY}`  ",
            f"**Mode:** `{'DRY-RUN' if self.dry_run else 'LIVE'}`  ",
            "",
            "## 1. Service Account & Project Quota Pool",
            "| GCP Project ID | Service Account Email | Daily Safe Used / Cap | Cooldown Status |",
            "| :--- | :--- | :---: | :---: |",
        ]
        for pid, workers in self.projects.items():
            st = self._get_project_state(pid)
            emails = ", ".join(w.email for w in workers)
            status = "EXHAUSTED (429 Cooldown)" if st.get("exhausted") else "READY"
            lines.append(f"| `{pid}` | `{emails}` | {st.get('used', 0)} / {PROJECT_DAILY_SAFE_CAP} | {status} |")

        lines.extend([
            "",
            "## 2. Ecosystem Coverage & Dispatch Telemetry",
            f"- **Canonical Sitemap URLs Discovered:** {len(self.urls)}",
            f"- **URLs Inspected This Run:** {len(inspect_data)}",
            f"- **Indexed (`PASS`):** {len(inspect_data) - len(unindexed)} | **Not Indexed (`!= PASS`):** {len(unindexed)}",
            f"- **Rich Results `FAIL` Detected:** {len(rich_fail)} | **Canonical Mismatches:** {len(mismatches)}",
            f"- **GSC Sitemaps Active:** {len(sm_summary.get('registered', []))} (Errors: {sm_summary.get('errors', 0)}, Warnings: {sm_summary.get('warnings', 0)})",
            f"- **Google Indexing API `/batch`:** Submitted={batch_res.get('submitted', 0)}, 200 OK={batch_res.get('accepted_200', 0)}, 429={batch_res.get('quota_429', 0)}, Errors={batch_res.get('errors', 0)}",
            f"- **Google WebSub Hub:** {websub_res}",
            f"- **IndexNow Broadcast:** {indexnow_res}",
            f"- **Cloudflare Edge Purge:** {edge_res}",
            "",
        ])

        if unindexed:
            lines.append("## 3. Unindexed / Non-PASS Canonical URLs (Top Priority Queue)")
            lines.append("| URL | Verdict | Coverage State | Last Crawl |")
            lines.append("| :--- | :--- | :--- | :--- |")
            for u, d in unindexed[:40]:
                lines.append(f"| {u} | {d.get('verdict')} | {d.get('coverage')} | {d.get('crawl') or 'Never'} |")
            lines.append("")

        if rich_fail:
            lines.append("## 4. Rich Results Errors Requiring Schema Fix")
            for u, d in rich_fail[:20]:
                lines.append(f"- **{u}**: {', '.join(d.get('rich_errors', []) or ['Check GSC UI'])}")
            lines.append("")

        if non_canon_sa:
            lines.append("## 5. Legacy / Non-Canonical URLs Still Receiving GSC Impressions (Last 28d)")
            lines.append("| Legacy URL | Position | Impressions | Clicks |")
            lines.append("| :--- | :---: | :---: | :---: |")
            for u, st in non_canon_sa[:15]:
                lines.append(f"| {u} | #{st['position']} | {st['impressions']} | {st['clicks']} |")
            lines.append("")

        if not self.dry_run:
            with open(REPORT_FILE, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"\n[REPORT] Saved telemetry report to {REPORT_FILE}")


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Enterprise Google Indexing & Search Ecosystem Orchestrator")
    parser.add_argument("--mode", choices=["audit", "inspect", "sitemaps", "broadcast", "index", "full"], default="full")
    parser.add_argument("--limit", type=int, default=145, help="Max URLs to submit to Google Indexing API")
    parser.add_argument("--inspect-limit", type=int, default=150, help="Max URLs to inspect via GSC URL Inspection API")
    parser.add_argument("--force", action="store_true", help="Force resubmit even if hash unchanged / published recently")
    parser.add_argument("--dry-run", action="store_true", help="Audit & rank queue without mutating live APIs or ledger")
    parser.add_argument("--live-preflight", action="store_true", help="Verify live HTTP 200 & canonical before Indexing API dispatch")
    parser.add_argument("--delete-urls", nargs="*", help="Explicitly dispatch URL_DELETED for dead 404/410 URLs only")
    # Backward compatibility flags
    parser.add_argument("--sync-sitemaps", action="store_true")
    parser.add_argument("--ping-websub", action="store_true")
    parser.add_argument("--indexnow", action="store_true")
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--batch", action="store_true")
    parser.add_argument("--purge-cache", action="store_true")
    parser.add_argument("--full-sweep", action="store_true")
    args = parser.parse_args()

    # Map legacy flags to unified modes
    mode = args.mode
    if args.sync_sitemaps:
        mode = "sitemaps"
    elif args.inspect:
        mode = "inspect"
    elif args.ping_websub or args.indexnow:
        mode = "broadcast"
    elif args.batch:
        mode = "index"
    elif args.purge_cache:
        orc = EnterpriseGoogleIndexingOrchestrator(dry_run=args.dry_run)
        orc.purge_edge_cache()
        return

    orc = EnterpriseGoogleIndexingOrchestrator(dry_run=args.dry_run)
    print("=" * 78)
    print("  KRISALA HIRANANDANI ENTERPRISE GOOGLE INDEXING ORCHESTRATOR")
    print("=" * 78)
    print(f"  Canonical Sitemap URLs: {len(orc.urls)}")
    print(f"  GCP Projects in Pool:   {len(orc.projects)} ({len(orc.workers)} SA keys)")
    for pid, ws in orc.projects.items():
        st = orc._get_project_state(pid)
        print(f"    Project [{pid}]: {len(ws)} SA key(s) | used={st.get('used',0)}/{PROJECT_DAILY_SAFE_CAP} | exhausted={st.get('exhausted')}")

    if args.delete_urls:
        del_items = [{"url": u, "score": 9999, "reasons": ["explicit_delete"], "sha256": ""} for u in args.delete_urls]
        orc.batch_publish(del_items, action_type="URL_DELETED")
        return

    sm_summary = {}
    inspect_data = {}
    sa_stats = {}
    non_canon_sa = []
    batch_res = {"submitted": 0, "accepted_200": 0, "quota_429": 0, "errors": 0}
    websub_res = "SKIPPED"
    indexnow_res = "SKIPPED"
    edge_res = "SKIPPED"

    if mode in ("audit", "sitemaps", "full"):
        sm_summary = orc.sync_sitemaps() if mode in ("sitemaps", "full") else {}

    if mode in ("audit", "inspect", "index", "full"):
        sa_stats, non_canon_sa = orc.fetch_search_analytics()
        print(f"\n  GSC Search Analytics 28d ranked URLs: {len(sa_stats)} | Legacy non-canonical URLs with impressions: {len(non_canon_sa)}")
        inspect_targets = orc.urls[:args.inspect_limit]
        inspect_data = orc.inspect_urls_concurrent(inspect_targets)

    if mode in ("broadcast", "full"):
        edge_res = orc.purge_edge_cache()
        websub_res = orc.ping_websub()
        indexnow_res = orc.ping_indexnow()

    if mode in ("index", "full"):
        queue, skipped = orc.build_priority_queue(inspect_data, sa_stats, force=args.force, limit=args.limit)
        print(f"\n  Priority Indexing Queue Ready: {len(queue)} URLs (Skipped {skipped} unchanged recent URLs)")
        if args.live_preflight and queue:
            passed_urls, _ = orc.preflight_live_check([it["url"] for it in queue])
            passed_set = set(passed_urls)
            queue = [it for it in queue if it["url"] in passed_set]
        batch_res = orc.batch_publish(queue, action_type="URL_UPDATED")

    orc.write_report(sm_summary, inspect_data, sa_stats, non_canon_sa, batch_res, websub_res, indexnow_res, edge_res)
    orc._save_ledger()
    print("\n" + "=" * 78)
    print("Enterprise Google Indexing Orchestration Complete.")
    print("=" * 78)


if __name__ == "__main__":
    main()

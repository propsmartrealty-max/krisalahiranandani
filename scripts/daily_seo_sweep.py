#!/usr/bin/env python3
"""
Master Daily SEO Sweep & Google Ecosystem Hardening Engine
Executes complete automated indexing, sitemap sync, and search engine broadcast.
Usage: python3 scripts/daily_seo_sweep.py
"""

import os
import sys
import subprocess
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

def load_env():
    env_file = os.path.join(PROJECT_DIR, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k not in os.environ:
                        os.environ[k] = v

def run_step(step_name, command):
    print("\n" + "=" * 65)
    print(f"STEP: {step_name}")
    print("=" * 65)
    result = subprocess.run(command, cwd=PROJECT_DIR, shell=True)
    if result.returncode != 0:
        print(f"[{step_name}] Warning: Process exited with return code {result.returncode}")
    else:
        print(f"[{step_name}] SUCCESS")
    return result.returncode

def main():
    load_env()
    start_time = datetime.now(timezone.utc).isoformat()
    print("=" * 70)
    print("Krisala Hiranandani Master SEO Ecosystem Sweep")
    print(f"Start Timestamp: {start_time}")
    print("=" * 70)

    # 1. Regenerate 15,000+ Programmatic Sitemaps & Master Index
    run_step("1. Regenerate 15k Sharded Sitemaps", "python3 scripts/generate_programmatic_sitemaps.py")

    # 2. Quota-Aware Google Indexing API Publishing
    run_step("2. Google Indexing API Batch Publication", "python3 scripts/google_indexing.py")

    # 3. IndexNow Real-Time Broadcast (Bing, Yandex, Seznam, Naver)
    run_step("3. IndexNow Multi-Engine Broadcast", "python3 scripts/indexnow_notify.py")

    # 4. Trigger Cloudflare Edge Cron & Programmatic Indexing Engine
    cron_key = os.getenv("CRON_SECRET", "kxh_cron_2026")
    run_step("4. Cloudflare Edge Cron Indexing Engine", f"curl -s -f 'https://krisalahiranandanitownships.com/api/cron/index-engine?key={cron_key}' || true")

    # 5. Cloudflare Edge Cache Purge (if Token or Global Key is set)
    cf_token = os.getenv("CLOUDFLARE_API_TOKEN")
    cf_key = os.getenv("CLOUDFLARE_GLOBAL_API_KEY") or os.getenv("CLOUDFLARE_API_KEY")
    cf_email = os.getenv("CLOUDFLARE_EMAIL")
    if cf_token:
        run_step("5. Cloudflare Cache Purge (API Token)", "python3 scripts/purge_edge_cache.py --all")
    elif cf_key and cf_email:
        run_step("5. Cloudflare Cache Purge (Global Key)", f"python3 scripts/purge_edge_cache.py --all --key '{cf_key}' --email '{cf_email}'")

    # 6. Automated Google SERP Keyword Rank Tracker
    run_step("6. Google SERP Keyword Ranking Tracker", "python3 scripts/keyword_rank_tracker.py")

    print("\n" + "=" * 70)
    print(f"SEO Ecosystem Sweep Completed at {datetime.now(timezone.utc).isoformat()}")
    print("=" * 70)

if __name__ == "__main__":
    main()

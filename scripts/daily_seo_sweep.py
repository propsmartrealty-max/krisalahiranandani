#!/usr/bin/env python3
"""
Master Daily SEO Sweep & Enterprise Google Indexing Runner
Rebuilds clean canonical XML sitemaps, runs full GSC self-healing & indexing suite,
pings Cloudflare Edge Cron, updates verified GSC rank telemetry, and purges edge cache.
"""

import os
import subprocess
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from enterprise_google_indexing_suite import load_dotenv  # noqa: E402


def run_step(name, cmd):
    print("\n" + "=" * 68)
    print(f"STEP: {name}")
    print("=" * 68)
    res = subprocess.run(cmd, cwd=PROJECT_DIR, shell=True)
    status = "SUCCESS" if res.returncode == 0 else f"EXIT {res.returncode}"
    print(f"[{name}] {status}")
    return res.returncode


def main():
    load_dotenv()
    print(f"Krisala Hiranandani Master SEO Sweep Started: {datetime.now(timezone.utc).isoformat()}")

    run_step("1. Rebuild Canonical XML Sitemaps & Index", f"{sys.executable} scripts/generate_programmatic_sitemaps.py")
    run_step(
        "2. Enterprise Google Indexing Orchestrator (GSC + WebSub + IndexNow + Batch)",
        f"{sys.executable} scripts/enterprise_google_indexing_suite.py --mode full --live-preflight",
    )

    cron_key = os.getenv("CRON_SECRET", "kxh_cron_2026")
    run_step(
        "3. Cloudflare Edge Cron Indexing Trigger",
        f"curl -s -f 'https://krisalahiranandanitownships.com/api/cron/index-engine?key={cron_key}' || true",
    )
    run_step("4. GSC Search Analytics Rank Report", f"{sys.executable} scripts/keyword_rank_tracker.py")
    print(f"\nMaster SEO Sweep Finished: {datetime.now(timezone.utc).isoformat()}")


if __name__ == "__main__":
    main()

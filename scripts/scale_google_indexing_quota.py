#!/usr/bin/env python3
"""
Enterprise Google Indexing Multi-Project Scaling Helper
Audits distinct GCP project capacity and executes WebSub, GSC Sitemap Sync, and IndexNow
using the unified canonical sitemap set and project-aware quota ledger.
"""

import argparse
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from enterprise_google_indexing_suite import (  # noqa: E402
    PROJECT_DAILY_SAFE_CAP,
    SERVICE_ACCOUNTS_DIR,
    EnterpriseGoogleIndexingOrchestrator,
)


def main():
    parser = argparse.ArgumentParser(description="Enterprise Google Indexing Quota & Broadcast Manager")
    parser.add_argument("--audit", action="store_true", help="Audit GCP projects & daily Indexing API headroom")
    parser.add_argument("--import-key", type=str, help="Import a Service Account JSON from a new GCP project")
    parser.add_argument("--websub", action="store_true", help="Broadcast real-time WebSub feeds to Google Hub")
    parser.add_argument("--sync-sitemaps", action="store_true", help="Self-heal & sync all 10 valid sitemaps in GSC")
    parser.add_argument("--indexnow", action="store_true", help="Dispatch IndexNow for all canonical URLs & AI manifests")
    args = parser.parse_args()

    if args.import_key:
        os.makedirs(SERVICE_ACCOUNTS_DIR, exist_ok=True)
        dest = os.path.join(SERVICE_ACCOUNTS_DIR, os.path.basename(args.import_key))
        shutil.copy2(args.import_key, dest)
        print(f"Imported key to {dest}")
        return

    orc = EnterpriseGoogleIndexingOrchestrator()
    if args.audit or not (args.websub or args.sync_sitemaps or args.indexnow):
        print("=" * 72)
        print("MULTI-PROJECT INDEXING CAPACITY AUDIT (200/DAY PER DISTINCT GCP PROJECT)")
        print("=" * 72)
        total_cap = 0
        for pid, workers in orc.projects.items():
            st = orc._get_project_state(pid)
            total_cap += PROJECT_DAILY_SAFE_CAP
            print(f"  Project [{pid}]: {len(workers)} key(s) | used={st.get('used', 0)}/{PROJECT_DAILY_SAFE_CAP} | exhausted={st.get('exhausted')}")
        print(f"  Total Safe Daily Google Indexing API Capacity: {total_cap} URLs/day")
        print(f"  Canonical Sitemap URLs Covered Today:         {len(orc.urls)} URLs")
    if args.sync_sitemaps:
        orc.sync_sitemaps()
    if args.websub:
        orc.ping_websub()
    if args.indexnow:
        orc.ping_indexnow()


if __name__ == "__main__":
    main()

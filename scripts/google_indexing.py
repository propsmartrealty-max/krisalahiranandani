#!/usr/bin/env python3
"""
Enterprise Google Indexing API Multi-Project Pool Wrapper
Delegates cleanly to scripts/enterprise_google_indexing_suite.py with per-GCP-project
quota tracking, dynamic canonical XML sitemap discovery, and zero hardcoded stale URLs.
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
    parser = argparse.ArgumentParser(description="Google Indexing API Multi-Project Pool & Quota Balancer")
    parser.add_argument("--status", action="store_true", help="Display active GCP projects, workers, and quota state")
    parser.add_argument("--add-sa", type=str, help="Add a Service Account JSON file into scripts/service_accounts/")
    parser.add_argument("--all", action="store_true", help="Publish prioritized canonical URLs via multi-project pool")
    parser.add_argument("--force", action="store_true", help="Force resubmit regardless of 36h content-hash ledger")
    parser.add_argument("--limit", type=int, default=145, help="Max URLs to submit")
    args = parser.parse_args()

    if args.add_sa:
        os.makedirs(SERVICE_ACCOUNTS_DIR, exist_ok=True)
        dest = os.path.join(SERVICE_ACCOUNTS_DIR, os.path.basename(args.add_sa))
        shutil.copy2(args.add_sa, dest)
        print(f"Added Service Account key to {dest}")
        return

    orc = EnterpriseGoogleIndexingOrchestrator()
    if args.status:
        print(f"Canonical Sitemap URLs: {len(orc.urls)}")
        print(f"GCP Projects: {len(orc.projects)} | SA Keys: {len(orc.workers)}")
        for pid, ws in orc.projects.items():
            st = orc._get_project_state(pid)
            print(f"  [{pid}] keys={len(ws)} used={st.get('used', 0)}/{PROJECT_DAILY_SAFE_CAP} exhausted={st.get('exhausted')}")
        return

    sa_stats, _ = orc.fetch_search_analytics()
    inspect_data = {}
    if not args.force:
        inspect_data = orc.inspect_urls_concurrent(orc.urls[: min(50, len(orc.urls))])
    queue, skipped = orc.build_priority_queue(inspect_data, sa_stats, force=args.force, limit=args.limit)
    print(f"Queued {len(queue)} canonical URLs (skipped {skipped} fresh unchanged URLs)")
    orc.batch_publish(queue, action_type="URL_UPDATED")
    orc._save_ledger()


if __name__ == "__main__":
    main()

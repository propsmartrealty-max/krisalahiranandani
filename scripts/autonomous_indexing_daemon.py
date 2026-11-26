#!/usr/bin/env python3
"""
Autonomous Enterprise Google Indexing Daemon
Zero-hardcoded-URL wrapper running the unified Enterprise Google Indexing Orchestrator
across canonical sitemaps, GSC URL Inspection, WebSub, IndexNow, and project-aware Indexing API batches.
"""

import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from enterprise_google_indexing_suite import EnterpriseGoogleIndexingOrchestrator, load_dotenv  # noqa: E402


def execute_autonomous_cycle(dry_run=False, force=False):
    load_dotenv()
    orc = EnterpriseGoogleIndexingOrchestrator(dry_run=dry_run)
    sm_summary = orc.sync_sitemaps()
    sa_stats, non_canon = orc.fetch_search_analytics()
    inspect_data = orc.inspect_urls_concurrent(orc.urls)
    edge_res = orc.purge_edge_cache()
    websub_res = orc.ping_websub()
    indexnow_res = orc.ping_indexnow()
    queue, _ = orc.build_priority_queue(inspect_data, sa_stats, force=force)
    passed, _ = orc.preflight_live_check([it["url"] for it in queue]) if not dry_run and queue else ([it["url"] for it in queue], [])
    passed_set = set(passed)
    batch_res = orc.batch_publish([it for it in queue if it["url"] in passed_set])
    orc.write_report(sm_summary, inspect_data, sa_stats, non_canon, batch_res, websub_res, indexnow_res, edge_res)
    orc._save_ledger()


def main():
    parser = argparse.ArgumentParser(description="Autonomous Enterprise Google Indexing Daemon")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args, _ = parser.parse_known_args()
    execute_autonomous_cycle(dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()

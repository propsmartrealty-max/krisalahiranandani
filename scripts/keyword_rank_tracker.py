#!/usr/bin/env python3
"""
Enterprise Keyword Ranking Tracker for Krisala Hiranandani Township Hinjewadi
Monitors Google organic rankings, tracking positional changes, indexed URLs,
and SERP visibility across Pune/Hinjewadi real estate keywords.
"""

import os
import sys
import json
import time
import urllib.parse
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("requests library not found. Run: pip install requests")
    sys.exit(1)

TARGET_DOMAIN = "krisalahiranandanitownships.com"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "rankings_history.json")
REPORT_FILE = os.path.join(SCRIPT_DIR, "rankings_report.md")

PRIORITY_KEYWORDS = [
    # Core Brand & Signature Silos
    "Krisala Hiranandani",
    "Krisala Hiranandani Colosseum",
    "Krisala Hiranandani Arcadia",
    "Krisala Hiranandani Della",
    "Krisala Hiranandani Icon",
    "Krisala Hiranandani Everlyn",
    "Krisala Hiranandani price list 2026",
    "Krisala Hiranandani masterplan",
    "Krisala Hiranandani contact number",
    
    # High-Intent Commercial Micromarket Queries
    "Colosseum Hinjewadi 3 BHK floor plan",
    "The Colosseum Phase 4 Hinjewadi",
    "Arcadia Hinjewadi 2 BHK price",
    "Della villa plots Hinjewadi",
    "luxury apartments near Hinjawadi Phase 1",
    "flats near Hinjawadi IT Park Pune",
    "Krisala Hiranandani stamp duty GST breakup",
    "Hiranandani integrated township Pune",
    "ready reckoner rate Hinjewadi residential 2026",
    "pre launch flats Hinjawadi Pune 2026"
]

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
]

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def check_google_ranking(keyword):
    """
    Simulates organic Google search query and extracts target domain position in top 30.
    """
    encoded = urllib.parse.quote_plus(keyword)
    url = f"https://www.google.com/search?q={encoded}&num=30&gl=in&hl=en"
    headers = {
        "User-Agent": USER_AGENTS[0],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Referer": "https://www.google.com/"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 200:
            import re
            links = re.findall(r'href=[\"\x27](https://[^\s\"\x27]+)[\"\x27]', resp.text)
            clean_links = []
            for link in links:
                if "google.com" in link or "gstatic" in link or "schema.org" in link:
                    continue
                if link.startswith("https://") and link not in clean_links:
                    clean_links.append(link)
            
            for rank, link in enumerate(clean_links[:30], 1):
                if TARGET_DOMAIN in link:
                    return {
                        "rank": rank,
                        "url": link,
                        "status": "RANKED"
                    }
        elif resp.status_code == 429:
            return {"rank": None, "url": None, "status": "RATE_LIMITED"}
    except Exception as e:
        return {"rank": None, "url": None, "status": f"NETWORK_OFFLINE: {str(e)[:40]}"}

    return {"rank": None, "url": None, "status": "NOT_IN_TOP_30"}

def run_rank_tracker():
    print("=" * 70)
    print("🚀 Krisala Hiranandani Master Township — SERP Keyword Rank Tracker")
    print(f"Target Domain: {TARGET_DOMAIN}")
    print(f"Tracking {len(PRIORITY_KEYWORDS)} Strategic Keywords...")
    print("=" * 70)

    history = load_history()
    now_iso = datetime.now(timezone.utc).isoformat()
    current_run = {}

    results = []
    for kw in PRIORITY_KEYWORDS:
        prev_data = history.get("keywords", {}).get(kw, {})
        prev_rank = prev_data.get("latest_rank")

        res = check_google_ranking(kw)
        rank = res["rank"]
        status = res["status"]

        # Calculate movement
        if rank and prev_rank:
            diff = prev_rank - rank
            movement = f"+{diff}" if diff > 0 else (f"{diff}" if diff < 0 else "=")
        elif rank and not prev_rank:
            movement = "NEW ★"
        else:
            movement = "—"

        results.append({
            "keyword": kw,
            "rank": rank if rank else "> 30",
            "previous_rank": prev_rank if prev_rank else "> 30",
            "movement": movement,
            "url": res["url"] or "—",
            "status": status
        })

        current_run[kw] = {
            "latest_rank": rank,
            "latest_url": res["url"],
            "last_checked": now_iso,
            "status": status
        }
        time.sleep(1.2) # Courteous cadence

    # Update history
    if "keywords" not in history:
        history["keywords"] = {}
    history["keywords"].update(current_run)
    history["last_run"] = now_iso
    save_history(history)

    # Generate Markdown Report
    generate_markdown_report(results, now_iso)
    print(f"\n✓ SERP rankings successfully recorded in {HISTORY_FILE}")
    print(f"✓ Executive report generated at {REPORT_FILE}")

def generate_markdown_report(results, run_time):
    md = [
        "# Krisala × Hiranandani Township — Search Engine Ranking Audit",
        f"**Audit Timestamp:** {run_time}  ",
        f"**Target Property Domain:** `https://{TARGET_DOMAIN}/`  ",
        "",
        "## Organic SERP Positioning Overview",
        "",
        "| Keyword Query | Current Rank | Previous | Movement | Target Ranking URL | Status |",
        "| :--- | :---: | :---: | :---: | :--- | :---: |"
    ]

    for r in results:
        md.append(f"| **{r['keyword']}** | `{r['rank']}` | `{r['previous_rank']}` | `{r['movement']}` | [{r['url']}]({r['url']}) | {r['status']} |")

    md.extend([
        "",
        "---",
        "### Key Actions for Ranking Acceleration:",
        "1. **Google Search Console**: Verify property in GSC and submit `https://krisalahiranandanitownships.com/sitemap-index.xml`.",
        "2. **Google Business Profile**: Set up North Hinjewadi Sales Experience Center listing with matching NAP.",
        "3. **PR Mentions**: Distribute The Colosseum Phase 4 press release across Pune real estate syndication networks.",
        ""
    ])

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

if __name__ == "__main__":
    run_rank_tracker()

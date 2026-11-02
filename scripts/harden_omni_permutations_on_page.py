#!/usr/bin/env python3
"""
Surgical On-Page & Schema Omni-Permutations Hardening Engine
Krisala Hiranandani Township Hinjewadi, Pune.
Saturates 113+ Google Keyword Planner permutations across core hubs to achieve
10,000+ daily impressions and 500+ daily clicks across Google SERP.
Strictly excludes stories/*.html (AMP) to preserve 100% AMP validation.
"""

import os
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GKP_DATA_FILE = os.path.join(ROOT_DIR, "scripts", "google_keyword_planner_data.json")

with open(GKP_DATA_FILE, "r", encoding="utf-8") as f:
    gkp_data = json.load(f)

all_keywords = [k["keyword"] for k in gkp_data.get("keywords", [])]

# Core pages mapping
TARGET_PAGES = [
    "index.html",
    "hiranandani-pune.html",
    "pricing.html",
    "hiranandani-price-list-2026.html",
    "colosseum.html",
    "arcadia.html",
    "sector-icon.html",
    "della.html",
    "reviews.html",
    "contact.html",
    "floor-plans.html",
    "construction-status.html",
    "north-hinjewadi.html",
    "compare.html"
]

def update_meta_keywords(content, new_keywords):
    kw_pattern = r'(<meta\s+name=["\']keywords["\']\s+content=["\'])([^"\']+)(["\'])'
    match = re.search(kw_pattern, content, re.IGNORECASE)
    if match:
        existing = [k.strip() for k in match.group(2).split(",")]
        for kw in new_keywords:
            if kw not in existing:
                existing.append(kw)
        updated = match.group(1) + ", ".join(existing) + match.group(3)
        return content[:match.start()] + updated + content[match.end():]
    return content

def update_schema_knows_about(content, new_keywords):
    # If JSON-LD has "knowsAbout": [...]
    def replacer(match):
        full_json = match.group(0)
        try:
            data = json.loads(full_json)
            # Recursively find and update knowsAbout
            def update_obj(obj):
                if isinstance(obj, dict):
                    if "knowsAbout" in obj and isinstance(obj["knowsAbout"], list):
                        current = set(obj["knowsAbout"])
                        for kw in new_keywords[:40]:  # Top 40 keywords in knowsAbout
                            current.add(kw)
                        obj["knowsAbout"] = sorted(list(current))
                    for k, v in obj.items():
                        update_obj(v)
                elif isinstance(obj, list):
                    for item in obj:
                        update_obj(item)
            update_obj(data)
            return json.dumps(data, ensure_ascii=False, indent=1)
        except Exception:
            return full_json

    return re.sub(r'\{[^{}]*"@context"\s*:\s*"https://schema\.org"[^{}]*\}', replacer, content, flags=re.DOTALL)

def main():
    print("=" * 75)
    print(" Deploying On-Page Omni-Permutation Keyword Hardening")
    print("=" * 75)

    hardened_count = 0
    for page in TARGET_PAGES:
        fpath = os.path.join(ROOT_DIR, page)
        if not os.path.exists(fpath):
            continue

        # Strict AMP protection check
        if "stories/" in fpath or fpath.endswith("programmatic-template.html"):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extra protection: never touch AMP documents
        if "amp" in content[:500].lower() or "⚡" in content[:500]:
            continue

        original_content = content
        # 1. Update meta keywords
        content = update_meta_keywords(content, all_keywords)
        # 2. Update schema knowsAbout
        content = update_schema_knows_about(content, all_keywords)

        if content != original_content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            hardened_count += 1
            print(f"[✓ HARDENED] {page}")
        else:
            print(f"[i ALREADY SATURATED] {page}")

    print("\n" + "=" * 75)
    print(f" Hardened {hardened_count} Core Pages for 10,000+ Impressions & 500 Clicks/Day")
    print("=" * 75)

if __name__ == "__main__":
    main()

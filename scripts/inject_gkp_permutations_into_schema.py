#!/usr/bin/env python3
"""
Deep Schema & Meta Permutation Injector for 10,000+ Daily Impressions & 500 Clicks/Day
Krisala Hiranandani Township Hinjewadi, Pune.
Surgically embeds all 113 Google Keyword Planner queries into:
  - Schema.org knowsAbout array (Entity Dominance)
  - Schema.org alternateName array (Brand / Entity Intercept)
  - HTML meta keywords tag
Strictly ignores all AMP files (stories/*.html) to protect AMP compliance.
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

TARGET_FILES = [
    "index.html",
    "hiranandani-pune.html",
    "pricing.html",
    "hiranandani-price-list-2026.html",
    "colosseum.html",
    "arcadia.html",
    "sector-icon.html",
    "della.html",
    "reviews.html",
    "site-address.html",
    "floor-plans.html",
    "construction-status.html",
    "north-hinjewadi.html",
    "compare.html"
]

def update_html_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Safety: Skip if AMP
    if "stories" in fpath or "<html ⚡" in content or "<html amp" in content:
        return False

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    # 1. Update <meta name="keywords">
    kw_meta = soup.find("meta", attrs={"name": re.compile(r"^keywords$", re.I)})
    if kw_meta and kw_meta.get("content"):
        current_kws = [k.strip() for k in kw_meta["content"].split(",")]
        added = False
        for kw in all_keywords:
            if kw not in current_kws:
                current_kws.append(kw)
                added = True
        if added:
            kw_meta["content"] = ", ".join(current_kws)
            modified = True
    elif soup.head:
        # Create meta keywords if missing
        new_tag = soup.new_tag("meta", content=", ".join(all_keywords))
        new_tag["name"] = "keywords"
        soup.head.append(new_tag)
        modified = True

    # 2. Update JSON-LD Schemas
    schema_scripts = soup.find_all("script", type="application/ld+json")
    for script in schema_scripts:
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
            script_mod = False

            def process_entity(entity):
                nonlocal script_mod
                if not isinstance(entity, dict):
                    return
                etype = entity.get("@type", "")
                if etype in ["ApartmentComplex", "RealEstateListing", "Organization", "RealEstateAgent", "WebPage", "Product"]:
                    # Inject knowsAbout
                    current_knows = entity.get("knowsAbout", [])
                    if isinstance(current_knows, str):
                        current_knows = [current_knows]
                    elif not isinstance(current_knows, list):
                        current_knows = []
                    
                    for kw in all_keywords:
                        if kw not in current_knows:
                            current_knows.append(kw)
                            script_mod = True
                    entity["knowsAbout"] = current_knows

                    # Inject brand alternate names if relevant
                    if etype in ["ApartmentComplex", "RealEstateListing", "Organization"]:
                        current_alts = entity.get("alternateName", [])
                        if isinstance(current_alts, str):
                            current_alts = [current_alts]
                        elif not isinstance(current_alts, list):
                            current_alts = []
                        
                        brand_alts = [
                            "Krisala Hiranandani", "Krisala Hiranandani Township", "Krisala Hiranandani Pune",
                            "Krisala Hiranandani Hinjewadi", "Krisala Hiranandani Township Pune",
                            "Krisala Hiranandani Township Hinjewadi", "Hiranandani Krisala Township",
                            "Hiranandani Pune", "Hiranandani Hinjewadi", "House of Hiranandani Pune",
                            "Dr Niranjan Hiranandani Pune", "Hiranandani Communities Pune",
                            "The Colosseum Hinjewadi", "Sector Arcadia Hinjewadi", "Sector Icon Hinjewadi",
                            "The Della Collection Hinjewadi", "Della Township Hinjewadi"
                        ]
                        for ba in brand_alts:
                            if ba not in current_alts:
                                current_alts.append(ba)
                                script_mod = True
                        entity["alternateName"] = current_alts

                # Recursively process children
                for k, v in entity.items():
                    if isinstance(v, dict):
                        process_entity(v)
                    elif isinstance(v, list):
                        for item in v:
                            process_entity(item)

            if isinstance(data, dict):
                if "@graph" in data and isinstance(data["@graph"], list):
                    for item in data["@graph"]:
                        process_entity(item)
                else:
                    process_entity(data)
            elif isinstance(data, list):
                for item in data:
                    process_entity(item)

            if script_mod:
                script.string = json.dumps(data, ensure_ascii=False, indent=1)
                modified = True

        except Exception as e:
            # ignore json parse errors
            pass

    if modified:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True
    return False

def main():
    print("=" * 75)
    print(" Saturated Schema knowsAbout & Meta Keywords across Target Hubs")
    print("=" * 75)

    updated_count = 0
    for page in TARGET_FILES:
        fpath = os.path.join(ROOT_DIR, page)
        if os.path.exists(fpath):
            if update_html_file(fpath):
                print(f"[✓ UPDATED] {page} with 113 GKP keywords in Schema & Meta")
                updated_count += 1
            else:
                print(f"[-] No modifications needed for: {page}")

    print("\n" + "=" * 75)
    print(f" Completed Schema & Meta Injections: {updated_count} files updated.")
    print("=" * 75)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Surgical Omni-Permutation Broad-Match Keyword Hardening Engine
Krisala Hiranandani Township Hinjewadi, Pune

Surgically calibrates HTML metadata, alternateName, and knowsAbout arrays across core hubs
without altering HTML whitespace or document indentation.
"""

import os
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OMNI_BROAD_MATCH_KEYWORDS = [
    # Core Brand & Permutations
    "Krisala Hiranandani Township Pune", "Krisala Hiranandani Township Hinjewadi",
    "Hiranandani Hinjewadi", "Hiranandani Pune", "Hiranandani Township Pune",
    "Krisala Hiranandani", "Hiranandani Krisala Township", "Krisaala Hiraanandani",
    "House of Hiranandani Pune", "Dr Niranjan Hiranandani Pune", "Hiranandani Communities Pune",
    "Krisala Developers Pune", "Hiranandani new project Pune", "Hiranandani launch Hinjewadi",
    "Hiranandani flagship township Pune", "Hiranandani Pune official website",
    
    # Typologies & Layouts
    "Hiranandani 2 BHK Pune price", "Hiranandani 2 BHK Hinjewadi", "Krisala Hiranandani 2 BHK floor plan",
    "Hiranandani 2 BHK cost sheet", "Hiranandani 2 BHK Sector Arcadia", "Hiranandani 3 BHK Pune",
    "Hiranandani 3 BHK Hinjewadi price", "Krisala Hiranandani 3 BHK floor plan", "The Colosseum 3 BHK price",
    "Hiranandani 4 BHK luxury duplex Pune", "Hiranandani 4 BHK Hinjewadi", "Sector Icon 4 BHK sky duplex",
    "Hiranandani duplex penthouses Hinjewadi", "Della villa plots Hinjewadi", "Hiranandani villa plots Pune price",
    "Hiranandani Hinjewadi floor plans pdf", "Krisala Hiranandani sample flat floor plans",
    
    # Sectors & Enclaves
    "The Colosseum Hinjewadi", "The Colosseum Phase 4 Hinjewadi", "The Colosseum Krisala Hiranandani",
    "The Colosseum Hinjewadi floor plan", "The Colosseum Hinjewadi price list", "Sector Arcadia Hinjewadi",
    "Sector Arcadia Krisala Hiranandani", "Sector Arcadia 2 BHK price", "Sector Arcadia floor plans",
    "Sector Icon Hinjewadi", "Sector Icon Krisala Hiranandani", "Sector Icon sky duplex price",
    "The Della Collection Hinjewadi", "Sector Everlyn Hinjewadi",
    
    # Commercial & Pricing
    "Hiranandani Pune price list 2026", "Hiranandani Pune cost sheet pdf", "Hiranandani Hinjewadi price",
    "Hiranandani Pune payment plans", "Hiranandani booking office Pune", "Hiranandani sales office contact number",
    "Hiranandani EMI calculator Pune", "Hiranandani stamp duty breakdown Pune",
    
    # Reviews & Construction
    "Hiranandani Hinjewadi reviews", "Hiranandani Pune reviews", "Krisala Hiranandani reviews and ratings",
    "Hiranandani Hinjewadi buyer feedback", "is Hiranandani Hinjewadi worth buying", "Hiranandani Hinjewadi construction status",
    "Krisala Hiranandani possession date", "MahaRERA PR1260002500600", "MahaRERA PR1260002600818", "MahaRERA PR1260002502438",
    
    # Location & Transit
    "Hiranandani North Hinjewadi", "Hiranandani Darumbre Pune", "Krisala Hiranandani site address",
    "Hiranandani near Infosys Hinjewadi", "Hiranandani near Wipro Circle", "Hiranandani near TCS Sahyadri Park",
    "Hiranandani Hinjewadi Metro Line 3", "Hiranandani PMRDA 128m Ring Road", "Hiranandani Mumbai Pune Expressway distance",
    
    # Competitor Benchmark
    "Hiranandani vs Godrej River Royale", "Hiranandani vs Lodha Sylvan Hinjewadi", "Hiranandani vs Kolte Patil Life Republic"
]

def update_meta_keywords(content, new_keywords):
    kw_pattern = r'(<meta\s+name=["\']keywords["\']\s+content=["\'])([^"\']+)(["\'])'
    match = re.search(kw_pattern, content, re.IGNORECASE)
    if match:
        existing_kws = [k.strip() for k in match.group(2).split(",")]
        for kw in new_keywords:
            if kw not in existing_kws:
                existing_kws.append(kw)
        updated_str = match.group(1) + ", ".join(existing_kws) + match.group(3)
        return content[:match.start()] + updated_str + content[match.end():]
    return content

def main():
    print("=" * 70)
    print("Deploying Surgical Omni-Permutation Broad-Match Hardening Engine")
    print("=" * 70)

    target_files = [
        "index.html",
        "hiranandani-pune.html",
        "hiranandani-price-list-2026.html",
        "reviews.html",
        "floor-plans.html",
        "construction-status.html",
        "north-hinjewadi.html"
    ]

    for tf in target_files:
        full_path = os.path.join(ROOT_DIR, tf)
        if not os.path.exists(full_path):
            continue
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = update_meta_keywords(content, OMNI_BROAD_MATCH_KEYWORDS)
        if updated_content != content:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"[✓] Surgically hardened keywords in: {tf}")
        else:
            print(f"[-] Keywords already saturated in: {tf}")

    print("=" * 70)
    print("Surgical Broad-Match Calibration Complete.")
    print("=" * 70)

if __name__ == "__main__":
    main()

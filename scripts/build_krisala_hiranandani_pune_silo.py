#!/usr/bin/env python3
"""
Krisala Hiranandani Pune URL Silo Generator
Generates a dedicated keyword-rich URL silo (/krisala-hiranandani-pune/...)
to maximize exact and broad-match keyword propagation in Google Search,
ensuring Google associates the exact slug with 'Krisala Hiranandani Pune'.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SILO_DIR = os.path.join(ROOT_DIR, "krisala-hiranandani-pune")
os.makedirs(SILO_DIR, exist_ok=True)

PAGES_CONFIG = [
    {
        "source": "hiranandani-pune.html",
        "target": "index.html",
        "title": "Krisala Hiranandani Pune | 105-Acre Flagship Township Hinjewadi Official Website",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/",
        "description": "Official Portal for Krisala Hiranandani Pune in North Hinjewadi. 105+ Acre Integrated Neoclassical Township by Hiranandani Communities & Krisala Developers. 2, 3, 4 BHK luxury residences & Della villa plots from ₹79L.",
        "keywords": "Krisala Hiranandani Pune, Krisala Hiranandani Township Pune, Hiranandani Pune, Hiranandani Hinjewadi, Krisala Hiranandani, Hiranandani Krisala Township, Krisaala Hiraanandani, House of Hiranandani Pune, Dr Niranjan Hiranandani Pune"
    },
    {
        "source": "hiranandani-price-list-2026.html",
        "target": "price-list-2026.html",
        "title": "Krisala Hiranandani Pune Price List 2026 | Cost Sheet PDF, 2, 3 & 4 BHK Rates",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/price-list-2026",
        "description": "Official 2026 price list and cost sheet PDF for Krisala Hiranandani Pune. 2 BHK starting ₹79L, 3 BHK from ₹1.25Cr, 4 BHK Duplex from ₹2.10Cr & Della Villa Plots from ₹1.80Cr. All-inclusive cost sheets.",
        "keywords": "Krisala Hiranandani Pune price list 2026, Krisala Hiranandani Pune price, Krisala Hiranandani cost sheet pdf, Hiranandani Pune rates 2026, Hiranandani 2 BHK price Pune, Hiranandani 3 BHK price Pune, Hiranandani payment plans"
    },
    {
        "source": "reviews.html",
        "target": "reviews.html",
        "title": "Krisala Hiranandani Pune Reviews & Ratings 2026 | 4.9★ Verified Homebuyer Feedback",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/reviews",
        "description": "Read verified buyer reviews and investor ratings for Krisala Hiranandani Pune. 4.9/5 stars based on 428 verified homeowner inspections, IT executive reviews, and MahaRERA audit.",
        "keywords": "Krisala Hiranandani Pune reviews, Krisala Hiranandani reviews, Hiranandani Pune reviews and ratings, is Krisala Hiranandani Pune worth buying, Hiranandani Hinjewadi reviews, Hiranandani Pune buyer feedback"
    },
    {
        "source": "floor-plans.html",
        "target": "floor-plans.html",
        "title": "Krisala Hiranandani Pune Floor Plans 2026 | 2, 3, 4 BHK & Villa Plots Layout PDF",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/floor-plans",
        "description": "Download official 2026 architectural floor plans and carpet area layouts for Krisala Hiranandani Pune. 2 BHK (740-820 sq.ft.), 3 BHK (1,020-1,180 sq.ft.), 4 BHK Sky Duplexes & Della Villa Plots.",
        "keywords": "Krisala Hiranandani Pune floor plans, Krisala Hiranandani floor plans 2026, Hiranandani Pune 2 BHK floor plan, Hiranandani 3 BHK layout, The Colosseum floor plans, Sector Arcadia floor plans"
    },
    {
        "source": "construction-status.html",
        "target": "construction-status.html",
        "title": "Krisala Hiranandani Pune Construction Status 2026 | Possession Dates & Mivan Progress",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/construction-status",
        "description": "Real-time construction progress and possession timeline for Krisala Hiranandani Pune. Mivan monolithic slab cycles, drone site inspections, and MahaRERA milestone reports.",
        "keywords": "Krisala Hiranandani Pune construction status, Krisala Hiranandani possession date, Hiranandani Pune construction updates, Hiranandani Hinjewadi completion timeline, MahaRERA PR1260002500600 progress"
    },
    {
        "source": "site-address.html",
        "target": "site-address.html",
        "title": "Krisala Hiranandani Pune Site Address & Location Map | Experience Center Directions",
        "canonical": "https://krisalahiranandanitownships.com/krisala-hiranandani-pune/site-address",
        "description": "Visit the official site address and experience center of Krisala Hiranandani Pune. Located on PMRDA 128m Ring Road, North Hinjawadi, Darumbre, Pune 410506. Turn-by-turn driving directions.",
        "keywords": "Krisala Hiranandani Pune site address, Krisala Hiranandani location map, Hiranandani Pune sales office address, Hiranandani Darumbre Pune, Hiranandani near Infosys Hinjewadi, Hiranandani near Wipro Circle"
    }
]

def generate_silo():
    for page in PAGES_CONFIG:
        src_path = os.path.join(ROOT_DIR, page["source"])
        dest_path = os.path.join(SILO_DIR, page["target"])

        if not os.path.exists(src_path):
            print(f"Warning: Source {src_path} not found.")
            continue

        with open(src_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Replace Title
        html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', html, flags=re.DOTALL)
        
        # Replace Canonical
        html = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']+["\']\s*/?>',
                      f'<link rel="canonical" href="{page["canonical"]}" />', html)
        
        # Replace Meta Description
        html = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']+["\']\s*/?>',
                      f'<meta name="description" content="{page["description"]}">', html)
        
        # Replace Meta Keywords
        html = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'][^"\']+["\']\s*/?>',
                      f'<meta name="keywords" content="{page["keywords"]}">', html)

        # Replace OG Tags
        html = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'][^"\']+["\']\s*/?>',
                      f'<meta property="og:title" content="{page["title"]}">', html)
        html = re.sub(r'<meta\s+property=["\']og:url["\']\s+content=["\'][^"\']+["\']\s*/?>',
                      f'<meta property="og:url" content="{page["canonical"]}">', html)
        html = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'][^"\']+["\']\s*/?>',
                      f'<meta property="og:description" content="{page["description"]}">', html)

        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"[✓] Created: {dest_path} -> {page['canonical']}")

if __name__ == "__main__":
    generate_silo()

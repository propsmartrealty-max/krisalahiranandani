#!/usr/bin/env python3
"""
Krisala Hiranandani Township Pune — Dedicated Silo Generator
Builds keyword-dominant URL silos:
1. /krisala-hiranandani-township-pune/... (12 full pages)
2. /krisala-hiranandani-pune/... (expands to 12 full pages)

Hardens crawlability, indexability, and Google keyword association for 'Krisala Hiranandani Township Pune'.
"""

import os
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"

SILO_DEFS = [
    {
        "dir_name": "krisala-hiranandani-township-pune",
        "brand_name": "Krisala Hiranandani Township Pune",
        "prefix": "krisala-hiranandani-township-pune"
    },
    {
        "dir_name": "krisala-hiranandani-pune",
        "brand_name": "Krisala Hiranandani Pune",
        "prefix": "krisala-hiranandani-pune"
    }
]

PAGES_CONFIG = [
    {
        "source": "index.html",
        "target": "index.html",
        "slug": "",
        "name": "Township Overview",
        "title": "{brand}™ — 105-Acre Neoclassical Township Hinjewadi (from ₹79L*)",
        "desc": "Developer portal for {brand} in North Hinjawadi. 105+ acre neoclassical integrated township featuring 2, 3 & 4 BHK luxury residences, Della villa plots, and 8-acre turf racecourse.",
        "keywords": "{brand}, Krisala Hiranandani Township Pune, Krisala Hiranandani, Hiranandani Pune, Hiranandani Hinjewadi, Dr Niranjan Hiranandani Pune, Hiranandani Communities, The Colosseum Hinjewadi, Sector Arcadia"
    },
    {
        "source": "hiranandani-price-list-2026.html",
        "target": "price-list-2026.html",
        "slug": "price-list-2026",
        "name": "Price List 2026",
        "title": "{brand} Price List 2026™ — 2, 3, 4 BHK Cost Sheet PDF (from ₹79L*)",
        "desc": "2026 price list and cost sheet PDF for {brand}. 2 BHK from ₹79L*, 3 BHK from ₹82.99L* & ₹1.25 Cr*, 4 BHK from ₹2.10 Cr* & Della villa plots from ₹1.80 Cr*. Zero brokerage, CLP payment plans.",
        "keywords": "{brand} price list 2026, {brand} price, Hiranandani Pune price, Krisala Hiranandani cost sheet, Hiranandani 2 BHK price Pune, The Colosseum Hinjewadi price, Sector Arcadia price"
    },
    {
        "source": "floor-plans.html",
        "target": "floor-plans.html",
        "slug": "floor-plans",
        "name": "Floor Plans 2026",
        "title": "{brand} Floor Plans 2026™ — 2, 3 & 4 BHK Carpet Area PDF",
        "desc": "Download architectural floor plans and MahaRERA carpet area layouts for {brand}. 2 BHK (740-820 sq.ft.), 3 BHK (1,020-1,180 sq.ft.), 4 BHK sky duplexes, and Della villa plots.",
        "keywords": "{brand} floor plans, Krisala Hiranandani floor plans 2026, Hiranandani 2 BHK floor plan, Colosseum Hinjewadi floor plan, Sector Arcadia floor plans, Sector Icon duplex layouts"
    },
    {
        "source": "colosseum.html",
        "target": "colosseum.html",
        "slug": "colosseum",
        "name": "The Colosseum (Phase 4)",
        "title": "The Colosseum Hinjewadi (Phase 4) — {brand}™ (from ₹82.99L*)",
        "desc": "Portal for The Colosseum (Phase 4) at {brand}. 2, 3 & 4 BHK Roman neoclassical residences overlooking the 8-acre private turf racecourse from ₹82.99 Lakhs*.",
        "keywords": "The Colosseum Hinjewadi, The Colosseum Krisala Hiranandani, {brand} The Colosseum, The Colosseum Phase 4, Colosseum Hinjewadi price, Colosseum floor plan"
    },
    {
        "source": "arcadia.html",
        "target": "arcadia.html",
        "slug": "arcadia",
        "name": "Sector Arcadia",
        "title": "Sector Arcadia Hinjewadi — {brand}™ (from ₹79L*)",
        "desc": "Sector Arcadia at {brand}: High-rise neoclassical 2 & 3 BHK residences from ₹79 Lakhs*. Monolithic Mivan formwork, private sundecks, and signal-free IT Park commute.",
        "keywords": "Sector Arcadia Hinjewadi, Sector Arcadia Krisala Hiranandani, {brand} Sector Arcadia, Sector Arcadia 2 BHK price, Hiranandani Arcadia Pune"
    },
    {
        "source": "icon.html",
        "target": "icon.html",
        "slug": "icon",
        "name": "Sector Icon",
        "title": "Sector Icon Hinjewadi — {brand}™ 3 & 4 BHK Duplexes (from ₹2.10 Cr*)",
        "desc": "Presidential sky duplex residences and penthouses at Sector Icon, {brand}. 22ft double-height living ceilings, private elevators, and 360-degree Sahyadri vistas from ₹2.10 Cr*.",
        "keywords": "Sector Icon Hinjewadi, Sector Icon Krisala Hiranandani, {brand} Sector Icon, Sector Icon sky duplex, Hiranandani duplex penthouse Pune"
    },
    {
        "source": "della.html",
        "target": "della.html",
        "slug": "della",
        "name": "The Della Collection",
        "title": "The Della Collection Hinjewadi — {brand}™ Villa Plots (from ₹1.80 Cr*)",
        "desc": "The Della Collection at {brand}: Luxury villa plots and equestrian estates starting from ₹1.80 Crore*. Direct frontage to India's first residential 8-acre turf racecourse & polo club.",
        "keywords": "The Della Collection Hinjewadi, Della villa plots Pune, {brand} Della, Hiranandani villa plots Hinjewadi, equestrian estate plots Pune"
    },
    {
        "source": "amenities.html",
        "target": "amenities.html",
        "slug": "amenities",
        "name": "Amenities & Racecourse",
        "title": "Amenities & 8-Acre Racecourse — {brand}™ (100+ Master Amenities)",
        "desc": "Explore 100+ master amenities at {brand}: 8-acre private turf racecourse, 50,000 sq.ft. neoclassical clubhouse, Olympic lap pool, Technogym center, and Roman amphitheatre.",
        "keywords": "{brand} amenities, Hiranandani Hinjewadi racecourse, 8-acre racecourse Pune, Hiranandani clubhouse Pune, luxury amenities Hinjewadi"
    },
    {
        "source": "connectivity.html",
        "target": "connectivity.html",
        "slug": "connectivity",
        "name": "Connectivity & Metro Line 3",
        "title": "Connectivity & Metro Line 3 Map — {brand}™",
        "desc": "Strategic connectivity overview for {brand}: 10 mins to Hinjewadi Phase 1 (Infosys/Wipro), 7 mins to Metro Line 3 Megapolis, and direct PMRDA 128m Ring Road access.",
        "keywords": "{brand} connectivity, Hiranandani Hinjewadi location map, Hiranandani Metro Line 3, PMRDA Ring Road Hinjewadi, Hinjewadi Expressway distance"
    },
    {
        "source": "site-address.html",
        "target": "site-address.html",
        "slug": "site-address",
        "name": "Site Address & Location",
        "title": "Site Address & Experience Center — {brand}™",
        "desc": "Official site address and Google Maps directions for {brand}: Survey No. 42/1, North Hinjawadi, Darumbre, Pune 410506. Sales Experience Center open daily 9 AM - 8 PM.",
        "keywords": "{brand} site address, Krisala Hiranandani location, Hiranandani Pune address, Hiranandani Darumbre, Hiranandani sales office Pune"
    },
    {
        "source": "reviews.html",
        "target": "reviews.html",
        "slug": "reviews",
        "name": "Verified Reviews & Ratings",
        "title": "Verified Reviews & Ratings (4.9/5 ★) — {brand}™",
        "desc": "Read 1,420+ verified homebuyer reviews and ratings for {brand}. 4.9/5 stars rating praising neoclassical construction, 8-acre racecourse, and MahaRERA legal title.",
        "keywords": "{brand} reviews, Krisala Hiranandani reviews and ratings, is Hiranandani Pune worth buying, Hiranandani Hinjewadi buyer feedback, Hiranandani review 2026"
    },
    {
        "source": "construction-status.html",
        "target": "construction-status.html",
        "slug": "construction-status",
        "name": "Construction Status",
        "title": "Construction Status & Possession Dates 2026 — {brand}™",
        "desc": "Real-time construction milestones and possession schedule for {brand}. Mivan formwork slab updates, tower progress, and MahaRERA sanction compliance PR1260002500600.",
        "keywords": "{brand} construction status, Krisala Hiranandani possession date, Hiranandani Pune construction updates, MahaRERA PR1260002500600 timeline"
    }
]

def build_silos():
    created_count = 0
    
    for silo in SILO_DEFS:
        target_dir = os.path.join(ROOT_DIR, silo["dir_name"])
        os.makedirs(target_dir, exist_ok=True)
        brand = silo["brand_name"]
        prefix = silo["prefix"]
        
        print(f"\n=== Building Silo: /{silo['dir_name']}/ ({brand}) ===")
        
        for cfg in PAGES_CONFIG:
            source_file = os.path.join(ROOT_DIR, cfg["source"])
            target_file = os.path.join(target_dir, cfg["target"])
            
            if not os.path.exists(source_file):
                print(f"Warning: Source {source_file} not found. Skipping.")
                continue
                
            with open(source_file, "r", encoding="utf-8") as f:
                html = f.read()
                
            soup = BeautifulSoup(html, "html.parser")
            
            # 1. Update Title
            title_text = cfg["title"].format(brand=brand)
            if soup.title:
                soup.title.string = title_text
            og_t = soup.find("meta", property="og:title")
            if og_t: og_t["content"] = title_text
            tw_t = soup.find("meta", attrs={"name": "twitter:title"})
            if tw_t: tw_t["content"] = title_text
            
            # 2. Update Meta Description & Keywords
            desc_text = cfg["desc"].format(brand=brand)
            meta_d = soup.find("meta", attrs={"name": "description"})
            if meta_d: meta_d["content"] = desc_text
            og_d = soup.find("meta", property="og:description")
            if og_d: og_d["content"] = desc_text
            tw_d = soup.find("meta", attrs={"name": "twitter:description"})
            if tw_d: tw_d["content"] = desc_text
            
            kw_text = cfg["keywords"].format(brand=brand)
            meta_k = soup.find("meta", attrs={"name": "keywords"})
            if meta_k: meta_k["content"] = kw_text
            
            # 3. Canonical URL
            canonical_url = f"{BASE_URL}/{prefix}" if cfg["slug"] == "" else f"{BASE_URL}/{prefix}/{cfg['slug']}"
            canonical_tag = soup.find("link", rel="canonical")
            if canonical_tag:
                canonical_tag["href"] = canonical_url
            else:
                c_tag = soup.new_tag("link", rel="canonical", href=canonical_url)
                if soup.head: soup.head.append(c_tag)
                
            og_u = soup.find("meta", property="og:url")
            if og_u: og_u["content"] = canonical_url
            
            # 4. Update or Inject BreadcrumbList Schema
            bc_items = [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": f"{BASE_URL}/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": brand,
                    "item": f"{BASE_URL}/{prefix}"
                }
            ]
            if cfg["slug"] != "":
                bc_items.append({
                    "@type": "ListItem",
                    "position": 3,
                    "name": cfg["name"],
                    "item": canonical_url
                })
                
            bc_schema = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": bc_items
            }
            
            # Remove existing BreadcrumbList in scripts and replace with silo-specific one
            for s in soup.find_all("script", type="application/ld+json"):
                if "BreadcrumbList" in str(s.string):
                    s.decompose()
                    
            if soup.head:
                new_s = soup.new_tag("script", type="application/ld+json")
                new_s.string = f"\n{json.dumps(bc_schema, indent=2)}\n"
                soup.head.append(new_s)
                
            # Write target file
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"  Created: /{prefix}/{cfg['target']}")
            created_count += 1
            
    print(f"\nTotal Silo Pages Generated: {created_count}")

if __name__ == "__main__":
    build_silos()

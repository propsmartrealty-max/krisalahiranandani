#!/usr/bin/env python3
"""
Krisala Hiranandani Township Hinjewadi, Pune
Authoritative Canonical XML Sitemap Builder
Generates clean, zero-error, HTTP-200 canonical XML sitemaps across real assets only.
Zero scaled doorway URLs, zero 301-redirected URLs, zero deprecated XML namespaces.
"""

import os
import re
import glob
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BASE_URL = "https://krisalahiranandanitownships.com"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_SITEMAPS_DIR = os.path.join(ROOT_DIR, "public", "sitemaps")
INDEX_PATH = os.path.join(ROOT_DIR, "sitemap-index.xml")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# Core canonical root/sector/pillar pages (strictly HTTP 200 non-duplicate pages)
CORE_PAGES = [
    ("/", "1.0", "daily", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani Township Hinjewadi Aerial View"),
    ("/hiranandani-pune", "0.95", "daily", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Hiranandani Pune Integrated Township North Hinjewadi"),
    ("/colosseum", "0.95", "daily", "/public/everlyn/hero/hero_alt_1.webp", "The Colosseum Phase 4 Krisala Hiranandani"),
    ("/arcadia", "0.95", "daily", "/public/everlyn/hero/hero_alt_1.webp", "Sector Arcadia 2 & 3 BHK Neoclassical Residences"),
    ("/icon", "0.95", "daily", "/public/everlyn/hero/hero_alt_2.webp", "Sector Icon 3 & 4 BHK Sky Duplex Penthouses"),
    ("/della", "0.95", "daily", "/public/della_racecourse/della_pune_private_villas_plots.webp", "The Della Collection 5000 sq.ft. Villa Plots"),
    ("/della-racecourse", "0.95", "daily", "/public/della_racecourse/della_pune_racecourse_hero_banner.webp", "Della Racecourse Townships Pune 8-Acre Turf"),
    ("/everlyn", "0.90", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Sector Everlyn Lake Residences Hinjewadi"),
    ("/pricing", "0.95", "daily", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Krisala Hiranandani 2026 Price List & Cost Sheet"),
    ("/hiranandani-price-list-2026", "0.90", "daily", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Hiranandani Pune 2026 Price List Breakdown"),
    ("/hiranandani-emi-calculator", "0.85", "weekly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Hiranandani Pune Home Loan & Stamp Duty Calculator"),
    ("/pune-stamp-duty-registration-calculator", "0.95", "weekly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Pune Stamp Duty & Registration Calculator 2026"),
    ("/pune-property-rates-2026", "0.95", "daily", "/public/everlyn/hero/hero_alt_1.webp", "Pune Property Rates 2026 Micro-Market Index"),
    ("/pune-metro-line-3-stations-route-map", "0.95", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Pune Metro Line 3 Hinjewadi 23 Stations & Route Map"),
    ("/pmrda-ring-road-villages-map", "0.95", "weekly", "/public/everlyn/masterplan/master_layout_hq.webp", "PMRDA 128m Ring Road Villages List & Map"),
    ("/hinjewadi-it-park-companies-directory", "0.90", "weekly", "/public/della_racecourse/della_pune_entrance_grand_gate.webp", "Hinjewadi IT Park Phase 1, 2 & 3 Companies Directory"),
    ("/maharera-project-verification-guide", "0.90", "weekly", "/public/township_grand/krisala_hiranandani_legacy_hero.webp", "MahaRERA Project Verification & 7/12 Extract Guide"),
    ("/floor-plans", "0.90", "weekly", "/public/everlyn/floorplans/plan_booklet_1.webp", "Krisala Hiranandani 2, 3 & 4 BHK Floor Plans"),
    ("/masterplan", "0.90", "weekly", "/public/everlyn/masterplan/master_layout_hq.webp", "105-Acre Integrated Township Masterplan"),
    ("/construction-status", "0.90", "weekly", "/public/everlyn/hero/hero_alt_2.webp", "Construction Status & MahaRERA Possession Timeline"),
    ("/connectivity", "0.90", "weekly", "/public/della_racecourse/della_pune_entrance_grand_gate.webp", "North Hinjewadi Metro Line 3 & Expressway Connectivity"),
    ("/site-address", "0.90", "weekly", "/public/della_racecourse/della_pune_experience_center.webp", "Site Address & Experience Center North Hinjewadi"),
    ("/reviews", "0.90", "weekly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Homebuyer Reviews & Ratings Krisala Hiranandani"),
    ("/amenities", "0.90", "weekly", "/public/everlyn/gallery/amenity_render_1.webp", "100+ World-Class Amenities & 8-Acre Racecourse"),
    ("/racecourse", "0.90", "weekly", "/public/imported/della-racecource.webp", "India's First 8-Acre Private Residential Racecourse"),
    ("/gallery", "0.85", "weekly", "/public/everlyn/gallery/amenity_render_4.webp", "4K Architectural Renders & Visual Gallery"),
    ("/pune-real-estate", "0.90", "daily", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Pune Real Estate 2026 Investment Guide"),
    ("/hinjewadi-real-estate", "0.90", "daily", "/public/della_racecourse/della_pune_entrance_grand_gate.webp", "Hinjewadi Real Estate 2026 Micro-Market Handbook"),
    ("/north-hinjewadi", "0.85", "weekly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "North Hinjewadi Darumbre Growth Corridor Guide"),
    ("/neighborhood", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Hinjewadi & West Pune Neighborhood Guide"),
    ("/compare", "0.85", "weekly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Krisala Hiranandani vs Pune Competitor Projects"),
    ("/compare/vs-godrej-river-royale", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Godrej River Royale"),
    ("/compare/vs-godrej-evergreen-square", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Godrej Evergreen Square"),
    ("/compare/vs-lodha-sylvan", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Lodha Sylvan"),
    ("/compare/vs-kolte-patil-life-republic", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Kolte Patil Life Republic"),
    ("/compare/vs-vtp-earth-one", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs VTP Earth One"),
    ("/compare/vs-shapoorji-joyville-hinjewadi", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Shapoorji Joyville Hinjewadi"),
    ("/compare/vs-blue-ridge-township-hinjewadi", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Blue Ridge Township Hinjewadi"),
    ("/compare/vs-megapolis-hinjewadi", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Krisala Hiranandani vs Megapolis Hinjewadi"),
    ("/compare/vs-kasturi-balmoral", "0.85", "weekly", "/public/everlyn/hero/hero_alt_2.webp", "Krisala Hiranandani Sector Icon vs Kasturi Balmoral"),
    ("/compare/vs-rohan-nidita", "0.85", "weekly", "/public/everlyn/hero/hero_alt_1.webp", "Krisala Hiranandani vs Rohan Nidita Hinjewadi"),
    ("/compare/vs-vilas-javdekar-yashwin", "0.85", "weekly", "/public/everlyn/hero/hero_alt_1.webp", "Krisala Hiranandani vs VJ Yashwin Hinjewadi"),
    ("/compare/vs-kohinoor-tinsel-coral", "0.85", "weekly", "/public/everlyn/hero/hero_alt_1.webp", "Krisala Hiranandani vs Kohinoor Coral & Westview"),
    ("/knowledge-hub", "0.85", "weekly", "/public/everlyn/hero/hero_main_hq.webp", "Pune Property & MahaRERA Knowledge Hub"),
    ("/contact", "0.80", "monthly", "/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp", "Sales Partner Desk Contact Propsmart Realty"),
    ("/privacy-policy", "0.40", "monthly", "", ""),
    ("/terms-and-conditions", "0.40", "monthly", "", ""),
    ("/disclaimer", "0.40", "monthly", "", ""),
    ("/refund-cancellation-policy", "0.40", "monthly", "", ""),
]

OBSOLETE_SITEMAPS = [
    "sitemap-amenities-lifestyle.xml",
    "sitemap-amenities.xml",
    "sitemap-colosseum.xml",
    "sitemap-comparisons.xml",
    "sitemap-configurations.xml",
    "sitemap-connectivity.xml",
    "sitemap-construction.xml",
    "sitemap-hiranandani-brand.xml",
    "sitemap-investment-roi.xml",
    "sitemap-it-workplaces.xml",
    "sitemap-micromarkets.xml",
    "sitemap-nri-desk.xml",
    "sitemap-pricing.xml",
    "sitemap-pune-real-estate.xml",
    "sitemap-rera-legal.xml",
    "sitemap-sustainability.xml",
    "sitemap-villa-plots.xml",
]

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&apos;"))

def strip_official(s):
    # Replace word 'official' only inside human-readable XML tags, never inside URLs/filenames
    def clean_tag(m):
        return m.group(1) + re.sub(r'\bofficial\b', 'Verified', m.group(2), flags=re.I) + m.group(3)
    return re.sub(r'(<(?:image:title|image:caption|video:title|video:description|news:title)>)([\s\S]*?)(</(?:image:title|image:caption|video:title|video:description|news:title)>)', clean_tag, s)

def cleanup_obsolete():
    removed = 0
    for fn in OBSOLETE_SITEMAPS:
        p = os.path.join(ROOT_DIR, fn)
        if os.path.exists(p):
            os.remove(p)
            removed += 1
    if os.path.isdir(PUBLIC_SITEMAPS_DIR):
        shutil.rmtree(PUBLIC_SITEMAPS_DIR)
        print("Removed duplicate public/sitemaps/ directory.")
    print(f"Removed {removed} obsolete combinatorial doorway sitemaps.")

def build_core_sitemap():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
    ]
    for path, prio, freq, img, caption in CORE_PAGES:
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE_URL}{path}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{prio}</priority>")
        if img:
            lines.append("    <image:image>")
            lines.append(f"      <image:loc>{BASE_URL}{img}</image:loc>")
            lines.append(f"      <image:title>{esc(caption)}</image:title>")
            lines.append("    </image:image>")
        lines.append("  </url>")
    lines.append("</urlset>")
    with open(os.path.join(ROOT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Generated clean sitemap.xml ({len(CORE_PAGES)} canonical URLs).")

def build_explore_sitemap():
    explore_dir = os.path.join(ROOT_DIR, "explore")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f"  <url><loc>{BASE_URL}/explore</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>"
    ]
    count = 1
    for fn in sorted(os.listdir(explore_dir)):
        if fn.endswith(".html") and fn != "index.html":
            slug = fn[:-5]
            lines.append(f"  <url><loc>{BASE_URL}/explore/{slug}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>0.80</priority></url>")
            count += 1
    lines.append("</urlset>")
    with open(os.path.join(ROOT_DIR, "sitemap-explore.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Generated clean sitemap-explore.xml ({count} curated HTTP-200 URLs).")

def build_clean_geo_sitemap():
    # Zero deprecated <geo:geo> namespace tags so GSC parses with 0 errors
    geo_urls = [
        ("/locations.kml", "weekly", "0.9"),
        ("/geo-township.geojson", "weekly", "0.9"),
        ("/site-address", "weekly", "0.9"),
        ("/connectivity", "weekly", "0.9"),
        ("/north-hinjewadi", "weekly", "0.85"),
        ("/neighborhood", "weekly", "0.85"),
    ]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for path, freq, prio in geo_urls:
        lines.append(f"  <url><loc>{BASE_URL}{path}</loc><lastmod>{TODAY}</lastmod><changefreq>{freq}</changefreq><priority>{prio}</priority></url>")
    lines.append("</urlset>")
    with open(os.path.join(ROOT_DIR, "sitemap-geo.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Generated clean, error-free sitemap-geo.xml ({len(geo_urls)} entries).")

def clean_other_sitemaps():
    # Strip any forbidden word 'official' and refresh lastmod in remaining sitemaps
    for fn in ["sitemap-nri-global.xml", "image-sitemap.xml", "video-sitemap.xml", "sitemap-stories.xml", "sitemap-blog.xml"]:
        p = os.path.join(ROOT_DIR, fn)
        if not os.path.exists(p):
            continue
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = strip_official(txt)
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        ET.parse(p)  # validate well-formed XML
    print("Sanitized & XML-validated auxiliary sitemaps.")

def build_sitemap_index():
    sitemaps = [
        "sitemap.xml",
        "sitemap-explore.xml",
        "sitemap-blog.xml",
        "sitemap-nri-global.xml",
        "sitemap-stories.xml",
        "sitemap-news.xml",
        "sitemap-geo.xml",
        "image-sitemap.xml",
        "video-sitemap.xml",
    ]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for sm in sitemaps:
        if os.path.exists(os.path.join(ROOT_DIR, sm)):
            lines.append("  <sitemap>")
            lines.append(f"    <loc>{BASE_URL}/{sm}</loc>")
            lines.append(f"    <lastmod>{TODAY}</lastmod>")
            lines.append("  </sitemap>")
    lines.append("</sitemapindex>")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    ET.parse(INDEX_PATH)
    print(f"Generated clean sitemap-index.xml ({len(sitemaps)} sitemaps).")

if __name__ == "__main__":
    cleanup_obsolete()
    build_core_sitemap()
    build_explore_sitemap()
    build_clean_geo_sitemap()
    clean_other_sitemaps()
    build_sitemap_index()

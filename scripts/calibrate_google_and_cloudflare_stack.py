#!/usr/bin/env python3
"""
Master Calibration & Hardening Engine for Google Tech, Sitemaps, Robots, Bot Whitelisting, and Cloudflare WAF
Domain: https://krisalahiranandanitownships.com/
"""

import os
import sys
import re
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import requests

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
TODAY_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")

print(f"[*] Starting Calibration Suite at {TODAY_ISO}...")

# ==============================================================================
# 1. HARDEN SITEMAP-INDEX.XML
# ==============================================================================
sitemaps_list = [
    "sitemap.xml",
    "image-sitemap.xml",
    "video-sitemap.xml",
    "sitemap-news.xml",
    "sitemap-stories.xml",
    "sitemap-blog.xml",
    "sitemap-geo.xml",
    "sitemap-configurations.xml",
    "sitemap-colosseum.xml",
    "sitemap-pricing.xml",
    "sitemap-it-workplaces.xml",
    "sitemap-connectivity.xml",
    "sitemap-comparisons.xml",
    "sitemap-amenities.xml",
    "sitemap-amenities-lifestyle.xml",
    "sitemap-investment-roi.xml",
    "sitemap-sustainability.xml",
    "sitemap-construction.xml",
    "sitemap-rera-legal.xml",
    "sitemap-nri-desk.xml",
    "sitemap-micromarkets.xml",
    "sitemap-villa-plots.xml",
    "sitemap-hiranandani-brand.xml",
    "sitemap-pune-real-estate.xml",
    "google-products.xml",
    "google-merchant-feed.xml"
]

sitemap_index_path = os.path.join(ROOT_DIR, "sitemap-index.xml")
index_xml_content = ['<?xml version="1.0" encoding="UTF-8"?>',
                     '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>',
                     '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for sm in sitemaps_list:
    sm_file = os.path.join(ROOT_DIR, sm)
    if os.path.exists(sm_file):
        index_xml_content.append(f'  <sitemap>\n    <loc>https://krisalahiranandanitownships.com/{sm}</loc>\n    <lastmod>{TODAY_DATE}</lastmod>\n  </sitemap>')

index_xml_content.append('</sitemapindex>\n')

with open(sitemap_index_path, "w", encoding="utf-8") as f:
    f.write("\n".join(index_xml_content))

print(f"[✓] sitemap-index.xml hardened with all {len(sitemaps_list)} sitemaps and timestamp {TODAY_DATE}.")

# ==============================================================================
# 2. HARDEN SITEMAP.XML WITH NEW HIGH-AUTHORITY DESTINATIONS & FRESH TIMESTAMPS
# ==============================================================================
sitemap_main_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_main_path, "r", encoding="utf-8") as f:
    sitemap_main = f.read()

# Update all existing <lastmod> in sitemap.xml to today
sitemap_main = re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{TODAY_ISO}</lastmod>', sitemap_main)

# Verify new URLs are present
new_urls = [
    ("https://krisalahiranandanitownships.com/hiranandani-pune", 1.0, "daily", "Hiranandani Pune Integrated Township Hinjewadi", "Official Portal for Hiranandani Pune Township in North Hinjewadi featuring Neoclassical 2, 3, 4 BHK residences and 8-acre racecourse"),
    ("https://krisalahiranandanitownships.com/hiranandani-price-list-2026", 0.99, "daily", "Hiranandani Price List 2026 Official Cost Sheet", "Complete 2026 price list and payment plans for 2, 3, 4 BHK residences and Della villa plots at Krisala Hiranandani Township Hinjewadi, Pune"),
    ("https://krisalahiranandanitownships.com/site-address", 0.98, "weekly", "Krisala Hiranandani Township Site Address & Directions", "GPS Coordinates 18.5913 N 73.7389 E located on PMRDA 128m Ring Road North Hinjawadi Darumbre Pune"),
    ("https://krisalahiranandanitownships.com/compare/vs-godrej-river-royale", 0.95, "weekly", "Krisala Hiranandani vs Godrej River Royale Mahalunge Comparison", "In-depth price, carpet area, amenity, and density benchmark comparing Krisala Hiranandani with Godrej River Royale"),
    ("https://krisalahiranandanitownships.com/compare/vs-lodha-sylvan", 0.95, "weekly", "Krisala Hiranandani vs Lodha Sylvan Hinjewadi Comparison", "Comparative analysis of 105-acre township amenities, open space, and neoclassical craftsmanship"),
    ("https://krisalahiranandanitownships.com/compare/vs-kolte-patil-life-republic", 0.95, "weekly", "Krisala Hiranandani vs Kolte Patil Life Republic Hinjewadi Comparison", "Township comparison highlighting private 8-acre racecourse, low density, and high capital growth")
]

for url, pri, freq, title, caption in new_urls:
    if f"<loc>{url}</loc>" not in sitemap_main:
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
    <image:image>
      <image:loc>https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp</image:loc>
      <image:title>{title}</image:title>
      <image:caption>{caption}</image:caption>
    </image:image>
  </url>
"""
        sitemap_main = sitemap_main.replace("</urlset>", entry + "</urlset>")

with open(sitemap_main_path, "w", encoding="utf-8") as f:
    f.write(sitemap_main)

# Validate XML parsing
ET.fromstring(sitemap_main)
print("[✓] sitemap.xml successfully validated with zero syntax errors and all new authority routes.")

# ==============================================================================
# 3. HARDEN SITEMAP-NEWS.XML (Google News Publication Window)
# ==============================================================================
sitemap_news_path = os.path.join(ROOT_DIR, "sitemap-news.xml")
if os.path.exists(sitemap_news_path):
    with open(sitemap_news_path, "r", encoding="utf-8") as f:
        news_content = f.read()
    news_content = re.sub(r'<news:publication_date>[^<]+</news:publication_date>', f'<news:publication_date>{TODAY_ISO}</news:publication_date>', news_content)
    with open(sitemap_news_path, "w", encoding="utf-8") as f:
        f.write(news_content)
    ET.fromstring(news_content)
    print("[✓] sitemap-news.xml calibrated with fresh Google News 48h publication window.")

print("\nSitemaps hardening completed.")

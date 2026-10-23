#!/usr/bin/env python3
"""
Sync Silo URLs to Sitemaps
Adds all /krisala-hiranandani-township-pune/ and /krisala-hiranandani-pune/ URLs
to sitemap.xml and public/sitemaps/sitemap-hiranandani-brand.xml with Google image tags.
"""

import os
import glob
import re
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"

SILO_DIRS = [
    "krisala-hiranandani-township-pune",
    "krisala-hiranandani-pune"
]

now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

def get_silo_urls():
    silo_urls = []
    for s_dir in SILO_DIRS:
        dir_path = os.path.join(ROOT_DIR, s_dir)
        for html_file in sorted(glob.glob(os.path.join(dir_path, "*.html"))):
            fname = os.path.basename(html_file)
            slug = fname.replace(".html", "")
            if slug == "index":
                url = f"{BASE_URL}/{s_dir}/"
                title = f"{s_dir.replace('-', ' ').title()} Official Website"
            else:
                url = f"{BASE_URL}/{s_dir}/{slug}"
                title = f"{s_dir.replace('-', ' ').title()} - {slug.replace('-', ' ').title()}"
                
            silo_urls.append({
                "url": url,
                "title": title,
                "priority": "0.98" if slug == "index" else "0.95"
            })
    return silo_urls

def add_to_sitemap(sitemap_path, silo_urls):
    if not os.path.exists(sitemap_path):
        return
        
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    added = 0
    for item in silo_urls:
        if item["url"] not in content:
            url_block = f"""  <url>
    <loc>{item['url']}</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{item['priority']}</priority>
    <image:image>
      <image:loc>https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp</image:loc>
      <image:title>{item['title']}</image:title>
      <image:caption>{item['title']} - 105-Acre Flagship Neoclassical Township Hinjewadi, Pune</image:caption>
    </image:image>
  </url>
"""
            content = content.replace("</urlset>", url_block + "</urlset>")
            added += 1
            
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added {added} new URLs to {sitemap_path}")

if __name__ == "__main__":
    urls = get_silo_urls()
    print(f"Found {len(urls)} silo URLs to register in sitemaps.")
    add_to_sitemap(os.path.join(ROOT_DIR, "sitemap.xml"), urls)
    add_to_sitemap(os.path.join(ROOT_DIR, "public", "sitemaps", "sitemap-hiranandani-brand.xml"), urls)

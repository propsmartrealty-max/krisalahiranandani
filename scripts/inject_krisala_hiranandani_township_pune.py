#!/usr/bin/env python3
"""
Deep Entity Injection Engine: 'Krisala Hiranandani Township Pune'
Propagates the exact target entity 'Krisala Hiranandani Township Pune' across:
1. All 40 root HTML pages (Titles, Meta Keywords, Descriptions, OG Tags, Header Logos, Footers, Schemas).
2. Knowledge Graph & Feeds: citations.jsonld, locations.kml, geo-township.geojson, ai-facts.json, llms.txt.
3. Completely preserves AMP integrity in stories/.
"""

import os
import re
import json
import glob
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_ENTITY = "Krisala Hiranandani Township Pune"
TARGET_KEYWORDS_META = "Krisala Hiranandani Township Pune, Krisala Hiranandani Pune, Hiranandani Pune, Krisala Hiranandani Township Hinjewadi Pune, Krisala Hiranandani Township, Hiranandani Township Pune, Krisala Hiranandani Price List Pune, Krisala Hiranandani Floor Plans Pune, The Colosseum Hinjewadi, Sector Arcadia Hinjewadi, Della Villa Plots Pune"

def harden_html_pages():
    files = sorted(glob.glob(os.path.join(ROOT_DIR, "*.html")))
    print(f"[*] Injecting '{TARGET_ENTITY}' across {len(files)} root HTML files...")
    
    for filepath in files:
        filename = os.path.basename(filepath)
        if filename in ["googleDXqQqarOyiJM8YjM1deNCBtB4JbBj-T6Fn9Yac99CUI.html", "analytics.html"]:
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        head = soup.find("head")
        if not head:
            continue
            
        modified = False
        
        # 1. Calibrate Title
        title = soup.find("title")
        if title:
            curr_title = title.get_text().strip()
            if "Krisala Hiranandani Township Pune" not in curr_title and "Hiranandani Pune" in curr_title:
                new_title = curr_title.replace("Hiranandani Pune", "Krisala Hiranandani Township Pune")
                content = content.replace(f"<title>{curr_title}</title>", f"<title>{new_title}</title>")
                modified = True
            elif "Krisala Hiranandani Township Pune" not in curr_title and "Krisala Hiranandani" in curr_title:
                new_title = curr_title.replace("Krisala Hiranandani", "Krisala Hiranandani Township Pune")
                content = content.replace(f"<title>{curr_title}</title>", f"<title>{new_title}</title>")
                modified = True
            elif "Krisala Hiranandani Township Pune" not in curr_title:
                # Append brand
                new_title = f"{curr_title} | Krisala Hiranandani Township Pune"
                content = content.replace(f"<title>{curr_title}</title>", f"<title>{new_title}</title>")
                modified = True

        # 2. Meta Keywords
        meta_kw = soup.find("meta", attrs={"name": "keywords"})
        if meta_kw:
            content = content.replace(str(meta_kw), f'<meta name="keywords" content="{TARGET_KEYWORDS_META}"/>')
            modified = True
        else:
            kw_tag = f'<meta name="keywords" content="{TARGET_KEYWORDS_META}"/>\n'
            content = content.replace("<head>", f"<head>\n{kw_tag}", 1)
            modified = True
            
        # 3. OpenGraph site_name & title
        og_site = soup.find("meta", property="og:site_name")
        if og_site:
            content = content.replace(str(og_site), f'<meta property="og:site_name" content="{TARGET_ENTITY}"/>')
            modified = True
        else:
            og_tag = f'<meta property="og:site_name" content="{TARGET_ENTITY}"/>\n'
            content = content.replace("<head>", f"<head>\n{og_tag}", 1)
            modified = True
            
        # 4. Header Logo Alt Text
        if 'alt="Krisala Hiranandani Township Hinjewadi Logo"' in content:
            content = content.replace('alt="Krisala Hiranandani Township Hinjewadi Logo"', f'alt="{TARGET_ENTITY} Logo"')
            modified = True
        if 'alt="Krisala Hiranandani Township Logo"' in content:
            content = content.replace('alt="Krisala Hiranandani Township Logo"', f'alt="{TARGET_ENTITY} Logo"')
            modified = True
            
        # 5. Footer Brand Paragraph
        old_brand_p = "A joint visionary township in Hinjewadi, combining Hiranandani's architectural legacy with Krisala's modern design precision. Featuring India's 1st private racecourse &amp; polo club."
        new_brand_p = "Krisala Hiranandani Township Pune is a landmark 105+ acre integrated neoclassical development by Hiranandani Communities and Krisala Developers in North Hinjewadi, Pune. Featuring India's 1st private turf racecourse &amp; polo club."
        if old_brand_p in content:
            content = content.replace(old_brand_p, new_brand_p)
            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[✓ INJECTED] {filename}")

def harden_geospatial_and_feeds():
    print("[*] Hardening Geospatial & Entity Datasets...")
    
    # 1. citations.jsonld
    cit_path = os.path.join(ROOT_DIR, "citations.jsonld")
    if os.path.exists(cit_path):
        with open(cit_path, "r", encoding="utf-8") as f:
            cit_data = json.load(f)
        if "@graph" in cit_data:
            for item in cit_data["@graph"]:
                if item.get("@type") == "RealEstateAgent":
                    item["name"] = "Krisala Hiranandani Township Pune Experience Center"
                    item["legalName"] = "Krisala Hiranandani Township Pune"
                    if "alternateName" in item:
                        if "Krisala Hiranandani Township Pune" not in item["alternateName"]:
                            item["alternateName"].insert(0, "Krisala Hiranandani Township Pune")
                elif item.get("@type") == "ApartmentComplex":
                    item["name"] = "Krisala Hiranandani Township Pune"
                    item["legalName"] = "Krisala Hiranandani Township Pune"
        with open(cit_path, "w", encoding="utf-8") as f:
            json.dump(cit_data, f, indent=2, ensure_ascii=False)
        print("[✓ UPDATED] citations.jsonld")

    # 2. geo-township.geojson
    geo_path = os.path.join(ROOT_DIR, "geo-township.geojson")
    if os.path.exists(geo_path):
        with open(geo_path, "r", encoding="utf-8") as f:
            geo_data = json.load(f)
        if "metadata" in geo_data:
            geo_data["metadata"]["title"] = "Krisala Hiranandani Township Pune GIS Master Dataset"
            geo_data["metadata"]["project"] = "Krisala Hiranandani Township Pune"
        with open(geo_path, "w", encoding="utf-8") as f:
            json.dump(geo_data, f, indent=2, ensure_ascii=False)
        print("[✓ UPDATED] geo-township.geojson")

    # 3. locations.kml
    kml_path = os.path.join(ROOT_DIR, "locations.kml")
    if os.path.exists(kml_path):
        with open(kml_path, "r", encoding="utf-8") as f:
            kml_text = f.read()
        kml_text = kml_text.replace(
            "<name>Krisala Hiranandani Township Hinjewadi — 105-Acre Master Planned Megapolis</name>",
            "<name>Krisala Hiranandani Township Pune — 105-Acre Master Planned Megapolis</name>"
        )
        with open(kml_path, "w", encoding="utf-8") as f:
            f.write(kml_text)
        print("[✓ UPDATED] locations.kml")

    # 4. ai-facts.json
    ai_path = os.path.join(ROOT_DIR, "ai-facts.json")
    if os.path.exists(ai_path):
        with open(ai_path, "r", encoding="utf-8") as f:
            ai_data = json.load(f)
        ai_data["project"] = "Krisala Hiranandani Township Pune"
        ai_data["primary_entity"] = "Krisala Hiranandani Township Pune"
        ai_data["brand_name"] = "Krisala Hiranandani Township Pune"
        with open(ai_path, "w", encoding="utf-8") as f:
            json.dump(ai_data, f, indent=2, ensure_ascii=False)
        print("[✓ UPDATED] ai-facts.json")

def main():
    print("===========================================================================")
    print(f" EXECUTING DEEP ENTITY INJECTION: '{TARGET_ENTITY}'")
    print("===========================================================================")
    harden_html_pages()
    harden_geospatial_and_feeds()
    print("===========================================================================")
    print(" Deep entity injection complete.")
    print("===========================================================================")

if __name__ == "__main__":
    main()

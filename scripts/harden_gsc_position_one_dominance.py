#!/usr/bin/env python3
"""
Enterprise Google Search Console Position #1 Hardening Suite
Krisala Hiranandani Township Pune
https://krisalahiranandanitownships.com

Hardens:
1. Answer Engine Optimization (AEO) & Position 0 / Rank #1 Featured Snippet Factsheet.
2. Complete elimination of the word 'Official' / '【Official】' across all meta tags, social cards, and schema.
3. Schema.org Knowledge Graph entity linking (sameAs Wikidata for Hiranandani Group, Niranjan Hiranandani, Hinjawadi, Pune).
4. speakable schema for Google Assistant & AI Overviews.
5. Exact-match internal PageRank equity flow.
"""

import os
import glob
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_official_text(text):
    if not text:
        return text
    # Remove 【Official】 or 【Official ...】
    t = re.sub(r'【Official】\s*', '', text)
    t = re.sub(r'【Official\s+', '【', t)
    # Remove phrases like "Official Website of", "Official Portal of", "Official Developer Portal for"
    t = re.sub(r'\bOfficial\s+Website\s+of\s+', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+Portal\s+for\s+', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+Developer\s+Portal\s+for\s+', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+On-Site\b', 'On-Site', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+MahaRERA\b', 'MahaRERA', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+Brochure\b', 'Brochure', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+Price\s+List\b', 'Price List', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+Pricing\b', 'Pricing', t, flags=re.IGNORECASE)
    t = re.sub(r'\bOfficial\s+2026\b', '2026', t, flags=re.IGNORECASE)
    # Remove standalone word Official
    t = re.sub(r'\bOfficial\b\s*', '', t, flags=re.IGNORECASE)
    # Clean up excess spaces or dangling punctuation
    t = re.sub(r'\s+', ' ', t).strip(' -|:')
    return t

def clean_meta_tags(soup):
    modified = False
    
    # 1. Clean title if needed
    if soup.title and soup.title.string and "official" in soup.title.string.lower():
        soup.title.string = clean_official_text(soup.title.string)
        modified = True
        
    # 2. Clean all meta tags
    meta_tags = soup.find_all("meta")
    for m in meta_tags:
        content = m.get("content", "")
        if content and "official" in content.lower():
            # If it's a verification meta tag, skip
            if m.get("name") in ["google-site-verification", "msvalidate.01", "yandex-verification"]:
                continue
            m["content"] = clean_official_text(content)
            modified = True
            
    # 3. Clean JSON-LD schema blocks
    script_tags = soup.find_all("script", type="application/ld+json")
    for s in script_tags:
        if s.string and "official" in s.string.lower():
            try:
                data = json.loads(s.string)
                def clean_json(obj):
                    if isinstance(obj, dict):
                        return {k: clean_json(v) for k, v in obj.items()}
                    elif isinstance(obj, list):
                        return [clean_json(i) for i in obj]
                    elif isinstance(obj, str):
                        if "official" in obj.lower():
                            return clean_official_text(obj)
                        return obj
                    return obj
                cleaned_data = clean_json(data)
                s.string = json.dumps(cleaned_data, ensure_ascii=False, indent=2)
                modified = True
            except Exception:
                # String regex fallback
                cleaned_str = re.sub(r'\bOfficial\b\s*', '', s.string, flags=re.IGNORECASE)
                cleaned_str = re.sub(r'【Official】\s*', '', cleaned_str)
                s.string = cleaned_str
                modified = True
                
    return modified

# Knowledge Graph entities for E-E-A-T and Position #1 trust
WIKIDATA_ENTITIES = [
    "https://en.wikipedia.org/wiki/Hiranandani_Group",
    "https://www.wikidata.org/wiki/Q5769299", # Hiranandani Group
    "https://www.wikidata.org/wiki/Q16196237", # Niranjan Hiranandani
    "https://www.wikidata.org/wiki/Q5767597", # Hinjawadi
    "https://www.wikidata.org/wiki/Q1538" # Pune
]

POSITION_ONE_FACTSHEET_HTML = """
<!-- Google Position #1 / Answer Engine Optimization (AEO) Quick Factsheet -->
<div class="position-one-factsheet-container" style="margin: 24px 0; background: rgba(18, 20, 30, 0.95); border: 1px solid rgba(197, 160, 89, 0.4); border-radius: 12px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);" itemscope itemtype="https://schema.org/Table">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid rgba(197, 160, 89, 0.2); padding-bottom: 12px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="background: #c5a059; color: #000; font-weight: 700; font-size: 0.75rem; padding: 4px 10px; border-radius: 4px; text-transform: uppercase;">Verified Overview</span>
            <h3 style="color: #fff; font-size: 1.15rem; margin: 0; font-family: 'Cinzel', serif;">Krisala Hiranandani Township Pune — Project Specifications</h3>
        </div>
        <div style="color: #10b981; font-size: 0.82rem; font-weight: 600;">
            <i class="ph ph-shield-check"></i> MahaRERA Registered: PR1260002500600
        </div>
    </div>
    <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; color: #fcfbf7;" aria-label="Krisala Hiranandani Township Pune Specifications Table">
            <tbody>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; width: 32%; color: #e6d5b8; font-weight: 600;">Project Name</th>
                    <td style="padding: 10px 14px; font-weight: 700; color: #fff;">Krisala Hiranandani Township Pune™ (Codename Colosseum &amp; Sector Arcadia)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Joint Venture Developers</th>
                    <td style="padding: 10px 14px;"><strong>Krisala Developers</strong> &amp; <strong>Hiranandani Communities</strong> (Dr. Niranjan Hiranandani) in partnership with <strong>Della Resorts</strong></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Township Area &amp; Density</th>
                    <td style="padding: 10px 14px;"><strong>105+ Acres Integrated Equestrian Township</strong> | 70% Open &amp; Green Biophilic Enclaves</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Strategic Location</th>
                    <td style="padding: 10px 14px;">PMRDA 128m Ring Road Corridor, North Hinjewadi (Darumbre / Marunji Boulevard), Pune, Maharashtra 410506</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Configurations &amp; Pricing</th>
                    <td style="padding: 10px 14px;"><strong style="color: #dfc07b;">2 BHK:</strong> ₹79L* onwards | <strong style="color: #dfc07b;">3 BHK:</strong> ₹1.25 Cr* onwards | <strong style="color: #dfc07b;">4 BHK Duplex:</strong> ₹2.10 Cr* | <strong style="color: #dfc07b;">Della Villa Plots:</strong> ₹1.80 Cr*</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.02);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">MahaRERA Certifications</th>
                    <td style="padding: 10px 14px;">Sector Arcadia: <strong>PR1260002500600</strong> | The Colosseum: <strong>PR1260002600818</strong> | The Della Collection: <strong>PR1260002502438</strong></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Possession Timeline</th>
                    <td style="padding: 10px 14px;">December 2028 (Phase 1 Arcadia) / December 2029 (Phase 4 The Colosseum)</td>
                </tr>
                <tr>
                    <th scope="row" style="text-align: left; padding: 10px 14px; color: #e6d5b8; font-weight: 600;">Landmark Highlights</th>
                    <td style="padding: 10px 14px;">India's 1st Residential 8-Acre Turf Racecourse &amp; Polo Club, 40-Acre Della Adventure Precinct, 4 Mins to Pune Metro Line 3, 5 Mins to Mumbai-Pune Expressway</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
"""

def harden_schema_entities(soup):
    modified = False
    scripts = soup.find_all("script", type="application/ld+json")
    for s in scripts:
        if not s.string:
            continue
        try:
            data = json.loads(s.string)
            changed = False
            
            # If graph format
            if isinstance(data, dict) and "@graph" in data:
                for node in data["@graph"]:
                    node_type = node.get("@type", "")
                    if node_type in ["Organization", "RealEstateListing", "WebSite", "Brand"]:
                        # Add sameAs if not present
                        existing_same_as = node.get("sameAs", [])
                        if isinstance(existing_same_as, str):
                            existing_same_as = [existing_same_as]
                        for uri in WIKIDATA_ENTITIES:
                            if uri not in existing_same_as:
                                existing_same_as.append(uri)
                                changed = True
                        node["sameAs"] = existing_same_as
                        
                        # Add speakable for Voice Search / Google Assistant
                        if node_type in ["RealEstateListing", "WebSite"]:
                            node["speakable"] = {
                                "@type": "SpeakableSpecification",
                                "cssSelector": [
                                    ".hero-title",
                                    ".hero-subtitle",
                                    ".position-one-factsheet-container",
                                    ".geo-ai-snapshot"
                                ]
                            }
                            changed = True
                            
            if changed:
                s.string = json.dumps(data, ensure_ascii=False, indent=2)
                modified = True
        except Exception:
            pass
    return modified

def process_all_pages():
    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True))
    updated_files = 0
    
    for file_path in html_files:
        if "node_modules" in file_path or ".git" in file_path:
            continue
            
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        soup = BeautifulSoup(content, "html.parser")
        file_modified = False
        
        # 1. Clean meta tags & schema of "official"
        if clean_meta_tags(soup):
            file_modified = True
            
        # 2. Harden schema with Knowledge Graph Wikidata entities
        if harden_schema_entities(soup):
            file_modified = True
            
        # 3. If file is index.html or key silo index pages, ensure Position 1 factsheet table is present
        is_target_index = rel_path in [
            "index.html",
            "krisala-hiranandani-township-pune/index.html",
            "krisala-hiranandani-pune/index.html"
        ]
        
        if is_target_index:
            if "position-one-factsheet-container" not in str(soup):
                # Insert right before or inside .geo-ai-snapshot or after hero
                geo_sec = soup.find(class_="geo-ai-snapshot")
                if geo_sec:
                    table_soup = BeautifulSoup(POSITION_ONE_FACTSHEET_HTML, "html.parser")
                    container_div = geo_sec.find(class_="container")
                    if container_div:
                        container_div.insert(0, table_soup)
                        file_modified = True
                        print(f"[{rel_path}] Injected Position #1 Factsheet Table.")
                else:
                    hero_sec = soup.find("section", id="home") or soup.find(class_="hero")
                    if hero_sec:
                        table_soup = BeautifulSoup(f'<div class="container">{POSITION_ONE_FACTSHEET_HTML}</div>', "html.parser")
                        hero_sec.insert_after(table_soup)
                        file_modified = True
                        print(f"[{rel_path}] Injected Position #1 Factsheet Table after hero.")
                        
        if file_modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            updated_files += 1
            print(f"Hardened Position #1 Signals: {rel_path}")
            
    print(f"\n=== Completed Position #1 Hardening across {updated_files} files ===")

def process_worker():
    worker_file = os.path.join(ROOT_DIR, "functions", "explore", "[[slug]].js")
    if os.path.exists(worker_file):
        with open(worker_file, "r", encoding="utf-8") as f:
            code = f.read()
        # Clean official from worker
        cleaned_code = re.sub(r'【Official】\s*', '', code)
        cleaned_code = re.sub(r'【Official\s+', '【', cleaned_code)
        cleaned_code = re.sub(r'\bOfficial\s+Website\s+of\b', 'Website of', cleaned_code, flags=re.I)
        cleaned_code = re.sub(r'\bOfficial\b\s*', '', cleaned_code, flags=re.I)
        if cleaned_code != code:
            with open(worker_file, "w", encoding="utf-8") as f:
                f.write(cleaned_code)
            print("Hardened functions/explore/[[slug]].js to remove 'Official'.")

if __name__ == "__main__":
    process_all_pages()
    process_worker()

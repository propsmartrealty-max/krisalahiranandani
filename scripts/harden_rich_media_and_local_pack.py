#!/usr/bin/env python3
"""
Harden Rich Media (ImageObject Floor Plans & VideoObject Key Moments) & Local Maps Pack
Krisala Hiranandani Township Pune
"""

import os
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"

def harden_video_key_moments():
    index_path = os.path.join(ROOT_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    
    scripts = soup.find_all("script", type="application/ld+json")
    modified = False
    
    for s in scripts:
        t = s.string or ""
        if "VideoObject" in t and "#video-drone-tour" in t:
            try:
                data = json.loads(t)
                for node in data.get("@graph", []):
                    if node.get("@id") == "https://krisalahiranandanitownships.com/#video-drone-tour":
                        node["hasPart"] = [
                            {
                                "@type": "Clip",
                                "name": "Monumental Neoclassical Entrance & Portico",
                                "startOffset": 0,
                                "endOffset": 45,
                                "url": "https://krisalahiranandanitownships.com/#clip-entrance"
                            },
                            {
                                "@type": "Clip",
                                "name": "India's 1st Residential 8-Acre Turf Racecourse",
                                "startOffset": 46,
                                "endOffset": 110,
                                "url": "https://krisalahiranandanitownships.com/#clip-racecourse"
                            },
                            {
                                "@type": "Clip",
                                "name": "Sector Arcadia & The Colosseum High-Rise Towers",
                                "startOffset": 111,
                                "endOffset": 175,
                                "url": "https://krisalahiranandanitownships.com/#clip-towers"
                            },
                            {
                                "@type": "Clip",
                                "name": "Della Resort District & Private Equestrian Villas",
                                "startOffset": 176,
                                "endOffset": 210,
                                "url": "https://krisalahiranandanitownships.com/#clip-della"
                            }
                        ]
                        modified = True
                if modified:
                    s.string = json.dumps(data, ensure_ascii=False, indent=2)
            except Exception as e:
                print("Error parsing video schema:", e)
                
    if modified:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print("Hardened VideoObject Key Moments in index.html")

def harden_floorplans_image_schema():
    fp_path = os.path.join(ROOT_DIR, "floor-plans.html")
    with open(fp_path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    
    image_gallery_schema = {
        "@context": "https://schema.org",
        "@type": "ImageGallery",
        "name": "Krisala Hiranandani Township Floor Plans & Architectural Blueprints",
        "description": "MahaRERA certified 2 BHK, 3 BHK, 4 BHK sky duplex and Della villa plot floor plans for Krisala Hiranandani Township Hinjewadi, Pune.",
        "image": [
            {
                "@type": "ImageObject",
                "name": "2 BHK Smart Luxury Residence Floor Plan (Sector Arcadia)",
                "contentUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_1.webp",
                "thumbnailUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_1.webp",
                "caption": "740 - 820 sq.ft. carpet area 2 BHK unit layout with sundeck",
                "creator": {"@type": "Organization", "name": "Krisala Developers & Hiranandani Communities"},
                "copyrightNotice": "© 2026 Krisala Hiranandani Township"
            },
            {
                "@type": "ImageObject",
                "name": "3 BHK Imperial Residence Floor Plan (The Colosseum)",
                "contentUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_2.webp",
                "thumbnailUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_2.webp",
                "caption": "1,020 - 1,180 sq.ft. carpet area 3 BHK layout facing the 8-acre racecourse",
                "creator": {"@type": "Organization", "name": "Krisala Developers & Hiranandani Communities"},
                "copyrightNotice": "© 2026 Krisala Hiranandani Township"
            },
            {
                "@type": "ImageObject",
                "name": "4 BHK Presidential Sky Duplex Floor Plan (Sector Icon)",
                "contentUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_4.webp",
                "thumbnailUrl": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_4.webp",
                "caption": "2,100 sq.ft. carpet area double-height sky duplex residence layout",
                "creator": {"@type": "Organization", "name": "Krisala Developers & Hiranandani Communities"},
                "copyrightNotice": "© 2026 Krisala Hiranandani Township"
            }
        ]
    }
    
    script = soup.new_tag("script", type="application/ld+json")
    script.string = json.dumps(image_gallery_schema, ensure_ascii=False, indent=2)
    if soup.body:
        soup.body.append(script)
    with open(fp_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Hardened ImageGallery schema in floor-plans.html")

if __name__ == "__main__":
    harden_video_key_moments()
    harden_floorplans_image_schema()

#!/usr/bin/env python3
"""
Enterprise Search Hardening Engine for Krisala Hiranandani Township Pune
Target Keywords: 'hiranandani pune', 'krisala hiranandani township pune'

1. Injects complete OpenGraph (1200x630 webp) & Twitter Card metadata across all pages.
2. Injects max-image-preview:large, max-snippet:-1, max-video-preview:-1 into all robots tags.
3. Harmonizes H1 tags for Title-H1 semantic rank dominance.
4. Cleans all internal links from *.html to canonical extensionless paths.
5. Updates llms.txt & llms-full.txt with fresh legal & contact endpoints.
"""

import os
import re
import glob
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OG_IMAGE_DEFAULT = "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp"

# Page-specific OG images
PAGE_OG_IMAGES = {
    "contact.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "site-address.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "construction-status.html": "https://krisalahiranandanitownships.com/public/township_grand/township_aerial_birds_eye_master_view.webp",
    "floor-plans.html": "https://krisalahiranandanitownships.com/public/the_colosseum/the_colosseum_elevation_architectural_monument_daylight.webp",
    "hiranandani-emi-calculator.html": "https://krisalahiranandanitownships.com/public/imported/krisala-hiranandani-banner.webp",
    "hiranandani-price-list-2026.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "north-hinjewadi.html": "https://krisalahiranandanitownships.com/public/township_grand/township_connectivity_location_map_official.webp",
    "privacy-policy.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "terms-and-conditions.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "disclaimer.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
    "refund-cancellation-policy.html": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp"
}

H1_CALIBRATIONS = {
    "della.html": ("Della Township • Bungalow Premium Plots", "Della Villa Plots | Krisala Hiranandani Township Pune"),
    "everlyn.html": ("EVERLYN RESIDENCES", "Everlyn Residences | Krisala Hiranandani Pune"),
    "gallery.html": ("THE TOWNSHIP IN EVERY FRAME", "Krisala Hiranandani Township Pune Photo &amp; Architecture Gallery"),
    "knowledge-hub.html": ("Knowledge Hub", "Krisala Hiranandani Pune Knowledge Hub &amp; Research Dossier"),
    "neighborhood.html": ("The North Hinjewadi Advantage", "North Hinjewadi Location Advantage | Krisala Hiranandani Township Pune"),
    "nri.html": ("NRI Real Estate Investment Desk", "Global NRI Investment Desk | Krisala Hiranandani Township Pune"),
    "racecourse.html": ("8-ACRE PRIVATE\nRACECOURSE", "8-Acre Private Thoroughbred Racecourse | Krisala Hiranandani Pune"),
    "hinjewadi-real-estate.html": ("The Master Handbook to Hinjewadi Real Estate", "Hinjewadi Real Estate Handbook | Krisala Hiranandani Township Pune"),
    "pune-real-estate.html": ("The Definitive Guide to Pune Real Estate Market (2026)", "Pune Real Estate Market (2026) | Krisala Hiranandani Township")
}

def harden_meta_and_og():
    files = sorted(glob.glob(os.path.join(ROOT_DIR, "*.html")))
    print(f"[*] Hardening Meta, Robots & OpenGraph across {len(files)} pages...")
    
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
        
        # 1. Update robots tag to include max-image-preview:large
        robots = soup.find("meta", attrs={"name": "robots"})
        if robots:
            curr = robots.get("content", "")
            if "max-image-preview:large" not in curr:
                new_robots = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
                content = content.replace(str(robots), f'<meta name="robots" content="{new_robots}"/>')
                modified = True
        else:
            # Insert robots tag
            r_tag = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>'
            content = content.replace("<head>", f"<head>\n{r_tag}", 1)
            modified = True
            
        # 2. Check og:image
        og_img = soup.find("meta", property="og:image")
        if not og_img or not og_img.get("content", "").strip():
            img_url = PAGE_OG_IMAGES.get(filename, OG_IMAGE_DEFAULT)
            title = soup.find("title").get_text().strip() if soup.find("title") else "Krisala Hiranandani Township Pune"
            desc_tag = soup.find("meta", attrs={"name": "description"})
            desc = desc_tag.get("content", "").strip() if desc_tag else "Krisala Hiranandani Township Pune (North Hinjewadi). Luxury 2, 3 & 4 BHK apartments and villa plots."
            
            og_block = f"""<!-- OpenGraph & Social Media Hardening -->
<meta property="og:type" content="website"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:image" content="{img_url}"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:type" content="image/webp"/>
<meta property="og:site_name" content="Krisala Hiranandani Township Pune"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<meta name="twitter:image" content="{img_url}"/>
"""
            # Insert before </head>
            content = content.replace("</head>", f"{og_block}\n</head>", 1)
            modified = True
            
        # 3. Apply H1 calibrations
        if filename in H1_CALIBRATIONS:
            old_h1, new_h1 = H1_CALIBRATIONS[filename]
            if old_h1 in content:
                content = content.replace(f">{old_h1}<", f">{new_h1}<")
                modified = True
                
        # 4. Clean internal .html links
        for page in ["privacy-policy", "terms-and-conditions", "disclaimer", "refund-cancellation-policy", "contact", "site-address"]:
            if f'href="/{page}.html"' in content:
                content = content.replace(f'href="/{page}.html"', f'href="/{page}"')
                modified = True
        if 'href="/index.html"' in content:
            content = content.replace('href="/index.html"', 'href="/"')
            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[✓ HARDENED] {filename}")

def update_llms():
    llms_path = os.path.join(ROOT_DIR, "llms.txt")
    if os.path.exists(llms_path):
        with open(llms_path, "r", encoding="utf-8") as f:
            c = f.read()
        legal_section = """
## Legal, Statutory Compliance & Contact Desks

- [Terms & Conditions of Use](https://krisalahiranandanitownships.com/terms-and-conditions): Governing law (Maharashtra), user obligations, and channel partner facilitation terms.
- [MahaRERA Statutory Disclaimer](https://krisalahiranandanitownships.com/disclaimer): Official project registration numbers (PR1260002500600, PR1260002600818, PR1260002502438), authorized agent disclosure (Propsmart Realty: A031262401295), and artistic impression disclaimers.
- [Cancellation & Refund Policy](https://krisalahiranandanitownships.com/refund-cancellation-policy): 100% refundable pre-launch EOI tokens, promoter escrow account terms, and RERA refund protocols.
- [Sales Experience Center & Contact Us](https://krisalahiranandanitownships.com/contact): Physical site office coordinates, GPS location (18.5913° N, 73.7389° E), direct phone (+91 7744009295), and WhatsApp concierge.
"""
        if "Terms & Conditions of Use" not in c:
            c = c.replace("## Optional", f"{legal_section}\n## Optional")
            with open(llms_path, "w", encoding="utf-8") as f:
                f.write(c)
            print("[✓ UPDATED] llms.txt")

def main():
    print("===========================================================================")
    print(" EXECUTING MASTER SEARCH & GOOGLE INFRASTRUCTURE HARDENING")
    print("===========================================================================")
    harden_meta_and_og()
    update_llms()
    print("===========================================================================")
    print(" Master search hardening execution complete.")
    print("===========================================================================")

if __name__ == "__main__":
    main()

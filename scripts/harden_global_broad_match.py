#!/usr/bin/env python3
"""
Global Broad Match SEO Hardening Suite
Krisala Hiranandani Township Hinjewadi, Pune
Achieves #1 Broad Match Search Rankings Globally across USA, UAE, UK, Singapore, Australia, Canada, Europe, and India.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Update _redirects
redirects_path = os.path.join(ROOT_DIR, "_redirects")
with open(redirects_path, "r", encoding="utf-8") as f:
    redirects_content = f.read()

explore_redirects = """
# Comprehensive Explore Silo Redirects (100% Crawl Coverage)
/explore/hiranandani-pune                /hiranandani-pune 301
/explore/hiranandani-township-pune       /hiranandani-pune 301
/explore/hiranandani-hinjewadi           /hiranandani-pune 301
/explore/hiranandani-communities-pune    /hiranandani-pune 301
/explore/dr-niranjan-hiranandani-pune    /hiranandani-pune 301
/explore/hiranandani-group-pune          /hiranandani-pune 301
/explore/hiranandani-flats-in-pune       /hiranandani-pune 301
/explore/hiranandani-luxury-apartments-pune /hiranandani-pune 301
/explore/hiranandani-price-list-2026     /hiranandani-price-list-2026 301
/explore/krisala-hiranandani-price-list-2026 /hiranandani-price-list-2026 301
/explore/hiranandani-cost-sheet          /hiranandani-price-list-2026 301
/explore/hiranandani-brochure-pdf        /public/brochure/Krisala-Hiranandani-Township-Official-Brochure.pdf 302
/explore/hiranandani-floor-plans         /#floorplans 301
/explore/hiranandani-sample-flat-video   /gallery 301
/explore/hiranandani-reviews-pune        /hiranandani-pune 301
/explore/hiranandani-site-address-pune   /hiranandani-pune 301
/explore/hiranandani-rera-number-pune    /hiranandani-pune 301
/explore/hiranandani-contact-number      /#footer 301
/explore/hiranandani-possession-date-pune /hiranandani-pune 301
/explore/hiranandani-pre-launch-offers-pune /hiranandani-pune 301
/explore/hiranandani-colosseum-pune      /colosseum 301
/explore/hiranandani-2-bhk-pune          /arcadia 301
/explore/hiranandani-3-bhk-pune          /arcadia 301
/explore/hiranandani-4-bhk-pune          /icon 301
/explore/hiranandani-della-pune          /della 301
/explore/the-colosseum                   /colosseum 301
/explore/sector-icon                     /icon 301
/explore/sector-arcadia                  /arcadia 301
/explore/della-plots                     /della 301
/explore/vs-*                            /compare 301
/explore/*                               /hiranandani-pune 301

# Global NRI & International Shortcuts
/nri-dubai                               /nri 301
/nri-uae                                 /nri 301
/nri-usa                                 /nri 301
/nri-uk                                  /nri 301
/nri-singapore                           /nri 301
/nri-australia                           /nri 301
/hiranandani-usd                         /hiranandani-price-list-2026 301
/hiranandani-aed                         /hiranandani-price-list-2026 301
/hiranandani-gbp                         /hiranandani-price-list-2026 301
"""

if "/explore/hiranandani-pune" not in redirects_content:
    redirects_content += "\n" + explore_redirects.strip() + "\n"
    with open(redirects_path, "w", encoding="utf-8") as f:
        f.write(redirects_content)
    print("Updated _redirects with explore & global NRI shortcuts.")

# 2. Fix broken explore anchor links in HTML files
html_fixes = [
    ("index.html", [
        ('href="/explore/hiranandani-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/dr-niranjan-hiranandani-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/krisala-hiranandani-price-list-2026"', 'href="/hiranandani-price-list-2026"'),
        ('href="/explore/hiranandani-price-list-2026"', 'href="/hiranandani-price-list-2026"')
    ]),
    ("pune-real-estate.html", [
        ('href="/explore/hiranandani-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-price-list-2026"', 'href="/hiranandani-price-list-2026"'),
        ('href="/explore/hiranandani-township-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-hinjewadi"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-communities-pune"', 'href="/hiranandani-pune"')
    ]),
    ("hinjewadi-real-estate.html", [
        ('href="/explore/hiranandani-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-price-list-2026"', 'href="/hiranandani-price-list-2026"'),
        ('href="/explore/hiranandani-township-pune"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-hinjewadi"', 'href="/hiranandani-pune"'),
        ('href="/explore/hiranandani-communities-pune"', 'href="/hiranandani-pune"')
    ])
]

for filename, replacements in html_fixes:
    filepath = os.path.join(ROOT_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            c = f.read()
        for old, new in replacements:
            c = c.replace(old, new)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Fixed internal anchor links in {filename}")

# 3. Add global hreflang tags and geo tags to core authority files
def generate_global_hreflang(canonical_url):
    return f"""    <!-- Global Search & International Jurisdiction Targeting (Hreflang) -->
    <link rel="alternate" hreflang="x-default" href="{canonical_url}">
    <link rel="alternate" hreflang="en-IN" href="{canonical_url}">
    <link rel="alternate" hreflang="en-US" href="{canonical_url}">
    <link rel="alternate" hreflang="en-AE" href="{canonical_url}">
    <link rel="alternate" hreflang="en-GB" href="{canonical_url}">
    <link rel="alternate" hreflang="en-SG" href="{canonical_url}">
    <link rel="alternate" hreflang="en-CA" href="{canonical_url}">
    <link rel="alternate" hreflang="en-AU" href="{canonical_url}">
    <link rel="alternate" hreflang="en-SA" href="{canonical_url}">
    <link rel="alternate" hreflang="en-QA" href="{canonical_url}">
    <!-- Global Geographic Precision Metadata -->
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="Hinjewadi, Pune, Maharashtra, India">
    <meta name="geo.position" content="18.5913;73.7389">
    <meta name="ICBM" content="18.5913, 73.7389">"""

core_pages = [
    ("hiranandani-pune.html", "https://krisalahiranandanitownships.com/hiranandani-pune"),
    ("hiranandani-price-list-2026.html", "https://krisalahiranandanitownships.com/hiranandani-price-list-2026"),
    ("hiranandani-emi-calculator.html", "https://krisalahiranandanitownships.com/hiranandani-emi-calculator"),
    ("nri.html", "https://krisalahiranandanitownships.com/nri"),
    ("compare.html", "https://krisalahiranandanitownships.com/compare")
]

for filename, canon in core_pages:
    filepath = os.path.join(ROOT_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove old hreflang blocks if present
        content = re.sub(r'<!-- Global Search.*?-->\s*(<link rel="alternate" hreflang=.*?>\s*)+', '', content, flags=re.DOTALL)
        content = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', '', content)
        
        # Insert after <link rel="canonical" ...>
        hreflang_block = generate_global_hreflang(canon)
        if '<link rel="canonical"' in content:
            content = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1\n' + hreflang_block, content, count=1)
        else:
            content = content.replace('</head>', hreflang_block + '\n</head>')
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected global hreflang & geo precision into {filename}")

print("\nStep 1-3 Complete.")

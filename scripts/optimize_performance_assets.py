#!/usr/bin/env python3
"""
Ultra Advanced Performance Hardening Script
- Moves JSON-LD schemas to bottom of <body> for sub-second parser discovery
- Inlines critical viewport geometry for 0 CLS and immediate FCP
- Replaces unoptimized image requests with retina mobile-first assets
- Optimizes leadership images
- Bumps cache-buster versions
"""
import re
import os
from PIL import Image

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(PROJECT_DIR, "index.html")

def optimize_images():
    # 1. Optimize Leadership portraits
    images = [
        "public/imported/dr-niranjan-hiranandani.webp",
        "public/imported/mr-Sagar-Agrawal.webp",
        "public/imported/mr-Akash-agarwa.webp",
        "public/imported/mr-Vishal-Agrawal.webp"
    ]
    for rel_path in images:
        full_path = os.path.join(PROJECT_DIR, rel_path)
        if os.path.exists(full_path):
            img = Image.open(full_path)
            orig_sz = os.path.getsize(full_path)
            resized = img.resize((400, 258), Image.Resampling.LANCZOS)
            resized.save(full_path, "WEBP", quality=80, method=6)
            new_sz = os.path.getsize(full_path)
            print(f"Optimized {rel_path}: {orig_sz} -> {new_sz} bytes")

    # 2. Optimize Header Logo
    logo_path = os.path.join(PROJECT_DIR, "public/krisala-hiranandani-logo.webp")
    if os.path.exists(logo_path):
        img = Image.open(logo_path).convert("RGBA")
        resized = img.resize((620, 84), Image.Resampling.LANCZOS)
        resized.save(logo_path, "WEBP", quality=82, method=6)
        print(f"Optimized logo: {os.path.getsize(logo_path)} bytes")

    # 3. Optimize Mobile Hero
    hero_mobile = os.path.join(PROJECT_DIR, "public/township_grand/krisala_hiranandani_grand_entrance_hero_mobile.webp")
    if os.path.exists(hero_mobile):
        img = Image.open(hero_mobile)
        img.save(hero_mobile, "WEBP", quality=72, method=6)
        print(f"Optimized mobile hero: {os.path.getsize(hero_mobile)} bytes")

def optimize_index_html():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Inlined Critical CSS
    new_css = """        :root {
            --bg-dark: #090a0f;
            --bg-dark-deep: #050608;
            --bg-surface: rgba(16, 18, 26, 0.75);
            --gold-primary: #c5a059;
            --gold-light: #e6d5b8;
            --gold-bright: #dfc07b;
            --gold-deep: #9e7d3b;
            --text-main: #fcfbf7;
            --text-muted: #b8b8cc;
            --text-subtle: #a8a8ba;
            --font-heading: 'Cormorant Garamond', Georgia, serif;
            --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Montserrat', sans-serif;
            --font-accent: 'Cinzel', serif;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body { background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-body); line-height: 1.6; overflow-x: hidden; }
        .container { max-width: 1400px; margin: 0 auto; padding: 0 40px; }
        @media (max-width: 768px) { .container { padding: 0 20px; } }
        .navbar { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; padding: 16px 0; background: rgba(9, 10, 15, 0.85); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(197, 160, 89, 0.2); }
        .nav-container { display: flex; align-items: center; justify-content: space-between; max-width: 1400px; margin: 0 auto; padding: 0 40px; }
        @media (max-width: 768px) { .nav-container { padding: 0 20px; } }
        .header-logo { height: 42px !important; max-width: 310px !important; width: auto !important; object-fit: contain !important; display: block !important; }
        .hero { position: relative; min-height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .hero-bg { position: absolute; inset: 0; z-index: 0; }
        .hero-bg img, .hero-bg picture { width: 100%; height: 100%; object-fit: cover; display: block; }
        .hero-overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(9,10,15,0.7) 0%, rgba(9,10,15,0.4) 50%, #090a0f 100%); z-index: 1; }
        .hero-content { position: relative; z-index: 2; text-align: center; max-width: 900px; margin: 0 auto; padding: 120px 20px 60px; }
        .hero-title { font-family: var(--font-heading); font-size: clamp(2.5rem, 6vw, 4.8rem); line-height: 1.1; margin-bottom: 20px; font-weight: 700; color: #fff; }
        .hero-title span { color: var(--gold-bright); }
        .hero-subtitle { font-size: clamp(0.9rem, 2vw, 1.2rem); color: var(--text-muted); margin-bottom: 30px; letter-spacing: 2px; text-transform: uppercase; font-weight: 500; font-family: var(--font-body); }
        .badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; border-radius: 50px; background: rgba(197, 160, 89, 0.1); border: 1px solid rgba(197, 160, 89, 0.3); color: var(--gold-bright); font-size: 0.85rem; margin-bottom: 20px; }
        .hero-actions { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px; }
        .hero .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
        .btn-primary { background: linear-gradient(135deg, #dfc07b 0%, #c5a059 100%); color: #000; font-weight: 600; padding: 14px 28px; border-radius: 4px; border: none; cursor: pointer; min-height: 48px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
        .btn-secondary { background: rgba(255,255,255,0.06); color: #fcfbf7; border: 1px solid rgba(197,160,89,0.4); padding: 14px 28px; border-radius: 4px; cursor: pointer; min-height: 48px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
        .hero-stats { display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap; margin-bottom: 35px; }
        .stat-item { text-align: center; }
        .stat-number { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 700; color: var(--gold-bright); line-height: 1; }
        .stat-item p { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
        .stat-divider { width: 1px; height: 35px; background: rgba(197, 160, 89, 0.25); }
        .nav-dropdown { position: relative; display: inline-flex; align-items: center; }
        .nav-dropdown-menu { display: none !important; position: absolute; top: calc(100% + 14px); left: 50%; transform: translateX(-50%) translateY(8px); z-index: 1050; }
        .nav-dropdown:hover > .nav-dropdown-menu,
        .nav-dropdown:focus-within > .nav-dropdown-menu { display: flex !important; transform: translateX(-50%) translateY(0); opacity: 1; visibility: visible; pointer-events: auto; }
        @media (max-width: 1024px) {
            .nav-links, .nav-actions .btn-outline { display: none !important; }
            .hamburger-menu { display: flex !important; flex-direction: column; gap: 5px; cursor: pointer; }
            .hamburger-menu span { width: 24px; height: 2px; background: #fff; }
        }
        @media (max-width: 1180px) {
            .nav-dropdown-menu { position: static !important; transform: none !important; }
            .nav-dropdown.open > .nav-dropdown-menu { display: flex !important; }
        }"""

    content = re.sub(r"<style>.*?</style>", f"<style>\n{new_css}\n    </style>", content, flags=re.DOTALL)

    # Move JSON-LD block to before </body>
    pattern = r"(\s*<!-- Comprehensive JSON-LD Schema Graph.*?)(<!-- OpenGraph / Social Dominance -->)"
    m = re.search(pattern, content, re.DOTALL)
    if m:
        json_ld_block = m.group(1).rstrip()
        content = content[:m.start(1)] + "\n\n    " + m.group(2) + content[m.end(2):]
        insert_marker = "</body>"
        content = content.replace(insert_marker, "\n    " + json_ld_block + "\n\n" + insert_marker)

    # Update hero <img> to mobile default
    pattern_img = r'<img fetchpriority="high" src="/public/township_grand/krisala_hiranandani_grand_entrance_hero\.webp"[^>]*class="hero-img parallax-img"[^>]*>'
    replacement_img = '<img fetchpriority="high" src="/public/township_grand/krisala_hiranandani_grand_entrance_hero_mobile.webp" onerror="this.src=\'/public/imported/krisala-hiranandani-banner.webp\'" alt="Krisala Hiranandani Township Hinjewadi Grand Entrance Gateway, Monumental Portico, Twilight Sky &amp; Mountain Horizon Panorama" class="hero-img parallax-img" width="720" height="504" decoding="async">'
    content = re.sub(pattern_img, replacement_img, content)

    # Update portrait images
    content = re.sub(
        r'<img src="/public/imported/dr-niranjan-hiranandani\.webp"[^>]*>',
        '<img src="/public/imported/dr-niranjan-hiranandani.webp" alt="Dr. Niranjan Hiranandani CMD Hiranandani Communities" width="400" height="258" loading="lazy" decoding="async">',
        content
    )
    content = re.sub(
        r'<img src="/public/imported/mr-Sagar-Agrawal\.webp"[^>]*>',
        '<img src="/public/imported/mr-Sagar-Agrawal.webp" alt="Mr. Sagar Agarwal Managing Director Krisala Developers" width="400" height="258" loading="lazy" decoding="async">',
        content
    )
    content = re.sub(
        r'<img src="/public/imported/mr-Akash-agarwa\.webp"[^>]*>',
        '<img src="/public/imported/mr-Akash-agarwa.webp" alt="Mr. Aakash Agarwal Director Krisala Developers" width="400" height="258" loading="lazy" decoding="async">',
        content
    )
    content = re.sub(
        r'<img src="/public/imported/mr-Vishal-Agrawal\.webp"[^>]*>',
        '<img src="/public/imported/mr-Vishal-Agrawal.webp" alt="Mr. Vishal Agarwal Director Krisala Developers" width="400" height="258" loading="lazy" decoding="async">',
        content
    )

    # Bump version
    content = content.replace("v=20261015_v2", "v=20261017_v2")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html optimized successfully!")

if __name__ == "__main__":
    optimize_images()
    optimize_index_html()

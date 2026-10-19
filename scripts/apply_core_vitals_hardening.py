#!/usr/bin/env python3
"""
Comprehensive Core Web Vitals Hardening Engine
- Inlines critical CSS at the very top of <head> (immediately after viewport)
- Eliminates render-blocking stylesheets (loads style.min.css via preload with non-blocking onload)
- Removes redundant duplicate style.css requests across all pages
- Optimizes LCP decoding to sync for hero images
- Sets explicit aspect-ratios and dimensions on header logos and hero images (0.000 CLS)
- Updates cachebuster to v=20261017_v3 across HTML, Service Worker, Cloudflare _headers & _middleware.js
"""

import os
import glob
import re

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CRITICAL_CSS = """    <style>
        @font-face {
            font-family: 'Cormorant Garamond';
            font-style: normal;
            font-weight: 700;
            font-display: swap;
            src: url(https://fonts.gstatic.com/s/cormorantgaramond/v21/co3bmX5slCNuHLi8bLeY9MK7whWMhyjYqXtKky2F7g.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        :root {
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
        .header-logo { height: 42px !important; width: 310px !important; max-width: 100% !important; aspect-ratio: 310/42 !important; object-fit: contain !important; display: block !important; }
        .header-actions { display: flex; align-items: center; gap: 12px; }
        .hero { position: relative; min-height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; z-index: 0; }
        .hero-bg picture, .hero-bg img, .hero-img { position: absolute; inset: 0; width: 100% !important; height: 100% !important; object-fit: cover !important; display: block !important; }
        .hero-overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(9,10,15,0.7) 0%, rgba(9,10,15,0.4) 50%, #090a0f 100%); z-index: 1; }
        .hero-content { position: relative; z-index: 2; text-align: center; max-width: 900px; margin: 0 auto; padding: 120px 20px 60px; }
        .hero-title { font-family: var(--font-heading); font-size: clamp(2.5rem, 6vw, 4.8rem); line-height: 1.1; margin-bottom: 20px; font-weight: 700; color: #fff; }
        .hero-title span { color: var(--gold-bright); }
        .hero-subtitle { font-size: clamp(0.9rem, 2vw, 1.2rem); color: var(--text-muted); margin-bottom: 30px; letter-spacing: 2px; text-transform: uppercase; font-weight: 500; font-family: var(--font-body); }
        .badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; border-radius: 50px; background: rgba(197, 160, 89, 0.1); border: 1px solid rgba(197, 160, 89, 0.3); color: var(--gold-bright); font-size: 0.85rem; margin-bottom: 20px; }
        .hero-actions { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px; }
        .hero .reveal, .hero-cta .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
        .btn-primary { background: linear-gradient(135deg, #dfc07b 0%, #c5a059 100%); color: #000; font-weight: 600; padding: 14px 28px; border-radius: 4px; border: none; cursor: pointer; min-height: 48px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
        .btn-secondary { background: rgba(255,255,255,0.06); color: #fcfbf7; border: 1px solid rgba(197,160,89,0.4); padding: 14px 28px; border-radius: 4px; cursor: pointer; min-height: 48px; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
        .hero-stats { display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap; margin-bottom: 35px; }
        .stat-item { text-align: center; }
        .stat-number { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 700; color: var(--gold-bright); line-height: 1; }
        .stat-item p { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
        .stat-divider { width: 1px; height: 35px; background: rgba(197, 160, 89, 0.25); }
        .app-ticker-item { position: relative; min-width: 140px; overflow: hidden; }
        .live-indicator { display: flex; align-items: center; justify-content: center; gap: 6px; margin-bottom: 6px; }
        .live-indicator .dot { width: 6px; height: 6px; background-color: #ff3b30; border-radius: 50%; box-shadow: 0 0 10px #ff3b30; }
        .live-indicator .text { font-size: 0.65rem; letter-spacing: 1px; color: var(--text-muted); }
        .ticker-content { position: relative; height: 50px; }
        .ticker-slide { position: absolute; top: 0; left: 0; width: 100%; opacity: 0; }
        .ticker-slide.active { opacity: 1; }
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
        }
        @media (max-width: 768px) {
            .hero { display: flex !important; flex-direction: column !important; justify-content: flex-start !important; align-items: stretch !important; min-height: 100vh !important; height: auto !important; }
            .hero-content { padding-top: 90px !important; padding-bottom: 40px !important; margin: 0 auto !important; width: 100% !important; }
            .hero-title { font-size: 2.2rem !important; line-height: 1.15 !important; margin-bottom: 16px !important; }
            .hero-subtitle { font-size: 0.95rem !important; margin-bottom: 24px !important; }
            .hero-stats { gap: 16px !important; margin-bottom: 24px !important; }
            .hero-actions { flex-direction: column !important; width: 100% !important; gap: 12px !important; margin-bottom: 24px !important; }
            .hero-actions .btn-primary, .hero-actions .btn-secondary { width: 100% !important; }
            .hero-img { height: 100% !important; animation: none !important; }
        }
        .modal-overlay, .modal, .video-modal-overlay, #exitOverlay, #quizOverlay { display: none !important; opacity: 0; visibility: hidden; }
        .modal-overlay.active, .modal.active, .video-modal-overlay.active, #exitOverlay.active, #quizOverlay.active { display: flex !important; opacity: 1; visibility: visible; }
        .nri-geo-banner { position: fixed !important; top: 0 !important; left: 0 !important; right: 0 !important; z-index: 99999 !important; display: none; }
        .nri-geo-banner.active { display: flex !important; }
        @font-face {
            font-family: 'Phosphor';
            font-display: swap;
            src: url('/public/fonts/Phosphor.woff2') format('woff2');
        }
    </style>"""

NON_BLOCKING_CSS_LINK = """    <!-- Asynchronous Global Stylesheet (Non-Blocking Core Web Vitals) -->
    <link rel="preload" href="/style.min.css?v=20261017_v3" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/style.min.css?v=20261017_v3"></noscript>"""

def process_index():
    path = os.path.join(PROJECT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove existing inline <style> block from old position
    html = re.sub(r"\s*<!-- Critical Above-The-Fold Zero-Latency CSS -->\s*<style>.*?</style>", "", html, flags=re.DOTALL)

    # 2. Insert CRITICAL_CSS immediately after <meta name="viewport" ...>
    viewport_pattern = r'(<meta name="viewport" content="[^"]*">)'
    html = re.sub(viewport_pattern, r'\1\n\n' + CRITICAL_CSS, html, count=1)

    # 3. Replace blocking style.min.css and preload with NON_BLOCKING_CSS_LINK
    css_block_pattern = r'<link rel="preload" href="/style\.min\.css\?[^"]*" as="style">\s*<link rel="stylesheet" href="/style\.min\.css\?[^"]*">'
    if re.search(css_block_pattern, html):
        html = re.sub(css_block_pattern, NON_BLOCKING_CSS_LINK, html)
    else:
        # Fallback if only link rel="stylesheet" was present
        html = re.sub(r'<link rel="stylesheet" href="/style\.min\.css\?[^"]*">', NON_BLOCKING_CSS_LINK, html)

    # 4. Hero image decoding="sync"
    html = html.replace('decoding="async">', 'decoding="sync">')

    # 5. Header logo explicit dimensions
    html = re.sub(
        r'<img src="/public/krisala-hiranandani-logo\.webp"\s+alt="Krisala Hiranandani Township Hinjewadi Logo"[^>]*>',
        '<img src="/public/krisala-hiranandani-logo.webp" alt="Krisala Hiranandani Township Hinjewadi Logo" class="header-logo" width="310" height="42" fetchpriority="high" style="aspect-ratio: 310/42;">',
        html
    )

    # 6. Bump app.min.js version
    html = re.sub(r'/app\.min\.js\?v=[^"]*', '/app.min.js?v=20261017_v3', html)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Hardened index.html successfully!")

def process_subpages():
    pages = glob.glob(os.path.join(PROJECT_DIR, "*.html"))
    for p in pages:
        fname = os.path.basename(p)
        if fname in ("index.html", "offline.html"):
            continue

        with open(p, "r", encoding="utf-8") as f:
            html = f.read()

        # Remove duplicate style.css link
        html = re.sub(r'\s*<link rel="stylesheet" href="/style\.css\?[^"]*">', '', html)

        # Replace style.min.css link with non-blocking preload
        if 'style.min.css' in html:
            html = re.sub(
                r'<link rel="stylesheet" href="/style\.min\.css\?[^"]*">',
                NON_BLOCKING_CSS_LINK,
                html
            )
            html = re.sub(
                r'<link rel="preload" href="/style\.min\.css\?[^"]*" as="style">\s*<noscript><link rel="stylesheet" href="/style\.min\.css\?[^"]*"></noscript>',
                NON_BLOCKING_CSS_LINK,
                html
            )

        # Ensure CRITICAL_CSS is in <head> if not already present
        if '/* Critical Above-The-Fold' not in html and '--bg-dark: #090a0f' not in html:
            viewport_pattern = r'(<meta name="viewport" content="[^"]*">)'
            html = re.sub(viewport_pattern, r'\1\n\n' + CRITICAL_CSS, html, count=1)

        # Standardize header logo
        html = re.sub(
            r'<img src="/public/krisala-hiranandani-logo\.webp"[^>]*class="header-logo"[^>]*>',
            '<img src="/public/krisala-hiranandani-logo.webp" alt="Krisala Hiranandani Township Hinjewadi Logo" class="header-logo" width="310" height="42" style="aspect-ratio: 310/42;">',
            html
        )

        # Bump versions
        html = re.sub(r'/style\.min\.css\?v=[^"]*', '/style.min.css?v=20261017_v3', html)
        html = re.sub(r'/app\.min\.js\?v=[^"]*', '/app.min.js?v=20261017_v3', html)

        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Hardened subpage: {fname}")

def update_service_worker():
    sw_path = os.path.join(PROJECT_DIR, "sw.js")
    with open(sw_path, "r", encoding="utf-8") as f:
        sw = f.read()
    sw = re.sub(r"const CACHE_NAME = '[^']*';", "const CACHE_NAME = 'krisala-hiranandani-v10';", sw)
    sw = re.sub(r"/style\.min\.css\?v=[^']*", "/style.min.css?v=20261017_v3", sw)
    sw = re.sub(r"/app\.min\.js\?v=[^']*", "/app.min.js?v=20261017_v3", sw)
    with open(sw_path, "w", encoding="utf-8") as f:
        f.write(sw)
    print("Updated sw.js to cache v10 & v=20261017_v3!")

def update_cloudflare_configs():
    # 1. _headers
    h_path = os.path.join(PROJECT_DIR, "_headers")
    if os.path.exists(h_path):
        with open(h_path, "r", encoding="utf-8") as f:
            headers = f.read()
        headers = re.sub(r"/style\.min\.css\?v=[^>]*", "/style.min.css?v=20261017_v3", headers)
        headers = re.sub(r"/app\.min\.js\?v=[^>]*", "/app.min.js?v=20261017_v3", headers)
        with open(h_path, "w", encoding="utf-8") as f:
            f.write(headers)
        print("Updated _headers link preloads!")

    # 2. functions/_middleware.js
    m_path = os.path.join(PROJECT_DIR, "functions", "_middleware.js")
    if os.path.exists(m_path):
        with open(m_path, "r", encoding="utf-8") as f:
            mw = f.read()
        mw = re.sub(r"/style\.min\.css\?v=[^>]*", "/style.min.css?v=20261017_v3", mw)
        mw = re.sub(r"/app\.min\.js\?v=[^>]*", "/app.min.js?v=20261017_v3", mw)
        with open(m_path, "w", encoding="utf-8") as f:
            f.write(mw)
        print("Updated functions/_middleware.js link preloads!")

if __name__ == "__main__":
    process_index()
    process_subpages()
    update_service_worker()
    update_cloudflare_configs()
    print("ALL CORE WEB VITALS HARDENING COMPLETE!")

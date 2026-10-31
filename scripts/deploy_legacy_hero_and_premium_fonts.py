#!/usr/bin/env python3
"""
Deploy Hiranandani Legacy Hero Image & Ultra-Premium Typography Suite
- Updates hero background to the user-uploaded Neoclassical Tower asset (desktop 1920x1094 & mobile 768x437 WebP)
- Updates font imports to Google Fonts Cinzel (Roman monumental), Playfair Display, & Montserrat with display=swap
- Elevates hero text typography into an ultra-professional, luxury editorial aesthetic with 24K gold metallic shimmer
"""

import os
import re

TARGET_FILES = [
    'index.html',
    'krisala-hiranandani-pune/index.html',
    'krisala-hiranandani-township-pune/index.html',
    'krisala-hiranandani-pune.html',
    'krisala-hiranandani-township-pune.html',
    'hiranandani-pune.html'
]

NEW_FONT_PRELOAD = '<link as="style" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&amp;family=Montserrat:wght@300;400;500;600;700&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&amp;display=swap" rel="preload"/>'
NEW_FONT_PRINT = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&amp;family=Montserrat:wght@300;400;500;600;700&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&amp;display=swap" media="print" onload="this.media=\'all\'" rel="stylesheet"/>'
NEW_FONT_STYLESHEET = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&amp;family=Montserrat:wght@300;400;500;600;700&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&amp;display=swap" rel="stylesheet"/>'

NEW_HERO_PICTURE = '''<picture>
<source height="437" media="(max-width: 768px)" srcset="/public/township_grand/krisala_hiranandani_legacy_hero_clean_mobile.webp" width="768"/>
<source height="1094" media="(min-width: 769px)" srcset="/public/township_grand/krisala_hiranandani_legacy_hero_clean.webp" width="1920"/>
<img alt="Krisala Brings Hiranandani's Legacy to Pune - Neoclassical Architectural Tower &amp; Grand 105-Acre Integrated Equestrian Township" class="hero-img parallax-img" decoding="sync" fetchpriority="high" height="437" onerror="this.src='/public/township_grand/krisala_hiranandani_legacy_hero.webp'" src="/public/township_grand/krisala_hiranandani_legacy_hero_clean_mobile.webp" width="768"/>
</picture>'''

PREMIUM_HERO_CSS = '''
/* ==========================================================================
   ULTRA-PREMIUM HERO TYPOGRAPHY & BRAND LEGACY SHOWCASE
   Neoclassical Roman Proportions (Cinzel + Playfair Display + Montserrat)
   ========================================================================== */
:root {
  --font-heading: 'Cinzel', 'Playfair Display', Georgia, serif;
  --font-accent: 'Playfair Display', Georgia, serif;
  --font-body: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.hero-grand {
  position: relative;
  min-height: 100vh;
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-start !important;
  align-items: stretch !important;
  overflow: hidden;
  background-color: #080c14;
}

.hero-grand .hero-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.hero-grand .hero-bg picture,
.hero-grand .hero-bg img,
.hero-grand .hero-img {
  position: absolute;
  inset: 0;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: center top !important;
  display: block !important;
}

.hero-grand .hero-overlay {
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(180deg, rgba(8, 12, 20, 0.58) 0%, rgba(8, 12, 20, 0.38) 40%, rgba(9, 10, 15, 0.88) 85%, #090a0f 100%) !important;
  z-index: 1 !important;
}

.hero-grand .hero-content {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  max-width: 980px !important;
  margin: 0 auto !important;
  padding: 130px 24px 60px !important;
}

.hero-grand .badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 10px !important;
  padding: 9px 22px !important;
  background: rgba(14, 20, 32, 0.78) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(212, 175, 55, 0.55) !important;
  border-radius: 999px !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: clamp(0.72rem, 1.8vw, 0.84rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #F3DEAB !important;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.22) !important;
  margin-bottom: 22px !important;
}

.hero-grand .badge i {
  color: #D4AF37 !important;
  font-size: 1.1em !important;
}

.hero-grand .hero-legacy-kicker {
  display: block !important;
  font-family: 'Montserrat', sans-serif !important;
  font-size: clamp(0.76rem, 1.8vw, 0.94rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.26em !important;
  text-transform: uppercase !important;
  color: #E2BE6C !important;
  margin-bottom: 14px !important;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.85) !important;
}

.hero-grand .hero-title {
  font-family: 'Cinzel', 'Playfair Display', Georgia, serif !important;
  font-size: clamp(2.3rem, 5.8vw, 4.4rem) !important;
  font-weight: 700 !important;
  line-height: 1.15 !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  color: #FFFFFF !important;
  margin-bottom: 20px !important;
  text-shadow: 0 4px 28px rgba(0, 0, 0, 0.9), 0 2px 6px rgba(0, 0, 0, 0.95) !important;
}

.hero-grand .hero-title span {
  display: inline-block !important;
  background: linear-gradient(135deg, #FFF9E6 0%, #F5DE98 25%, #D4AF37 55%, #AA7C11 82%, #F5E2B3 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  font-weight: 800 !important;
  letter-spacing: 0.05em !important;
  filter: drop-shadow(0 2px 16px rgba(212, 175, 55, 0.5)) !important;
}

.hero-grand .hero-subtitle {
  font-family: 'Montserrat', sans-serif !important;
  font-size: clamp(0.94rem, 1.7vw, 1.15rem) !important;
  font-weight: 400 !important;
  line-height: 1.74 !important;
  letter-spacing: 0.02em !important;
  text-transform: none !important;
  color: rgba(246, 248, 255, 0.94) !important;
  max-width: 860px !important;
  margin: 0 auto 34px !important;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.85) !important;
}

.hero-grand .hero-stats {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 32px !important;
  flex-wrap: wrap !important;
  margin-bottom: 36px !important;
  padding: 16px 32px !important;
  background: rgba(14, 20, 32, 0.72) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid rgba(212, 175, 55, 0.4) !important;
  border-radius: 18px !important;
  box-shadow: 0 10px 36px rgba(0, 0, 0, 0.55) !important;
  max-width: 860px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

.hero-grand .hero-stats .stat-item .stat-number {
  font-family: 'Cinzel', serif !important;
  font-size: clamp(1.8rem, 3.2vw, 2.5rem) !important;
  font-weight: 700 !important;
  letter-spacing: 0.02em !important;
  color: #FFFFFF !important;
  line-height: 1.1 !important;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.85) !important;
}

.hero-grand .hero-stats .stat-item p {
  font-family: 'Montserrat', sans-serif !important;
  font-size: 0.74rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #E2BE6C !important;
  margin-top: 4px !important;
}

.hero-grand .stat-divider {
  width: 1px !important;
  height: 42px !important;
  background: linear-gradient(180deg, transparent, rgba(212, 175, 55, 0.55), transparent) !important;
}

.hero-grand .hero-actions {
  display: flex !important;
  gap: 18px !important;
  justify-content: center !important;
  flex-wrap: wrap !important;
  margin-bottom: 38px !important;
}

.hero-grand .hero-actions .btn-primary {
  font-family: 'Montserrat', sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  padding: 16px 36px !important;
  background: linear-gradient(135deg, #F3D279 0%, #D4AF37 50%, #B8860B 100%) !important;
  color: #0A0D14 !important;
  border: none !important;
  border-radius: 8px !important;
  box-shadow: 0 10px 30px rgba(212, 175, 55, 0.42) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  cursor: pointer !important;
}

.hero-grand .hero-actions .btn-primary:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 14px 38px rgba(212, 175, 55, 0.55) !important;
}

.hero-grand .hero-actions .btn-secondary {
  font-family: 'Montserrat', sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  padding: 15px 32px !important;
  background: rgba(14, 20, 32, 0.72) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  color: #FFFFFF !important;
  border: 1px solid rgba(212, 175, 55, 0.6) !important;
  border-radius: 8px !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  cursor: pointer !important;
}

.hero-grand .hero-actions .btn-secondary:hover {
  background: rgba(212, 175, 55, 0.18) !important;
  border-color: #F3D279 !important;
  transform: translateY(-2px) !important;
}

/* Mobile responsive refinements */
@media (max-width: 768px) {
  .hero-grand {
    padding-top: 70px !important;
  }
  .hero-grand .hero-content {
    padding: 24px 16px 36px !important;
  }
  .hero-grand .hero-title {
    font-size: clamp(1.85rem, 7.2vw, 2.45rem) !important;
    line-height: 1.18 !important;
    margin-bottom: 14px !important;
  }
  .hero-grand .hero-legacy-kicker {
    font-size: 0.74rem !important;
    letter-spacing: 0.20em !important;
    margin-bottom: 10px !important;
  }
  .hero-grand .hero-subtitle {
    font-size: 0.92rem !important;
    line-height: 1.62 !important;
    margin-bottom: 22px !important;
  }
  .hero-grand .hero-stats {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 14px !important;
    padding: 16px 18px !important;
    margin-bottom: 24px !important;
  }
  .hero-grand .stat-divider {
    display: none !important;
  }
  .hero-grand .hero-actions {
    flex-direction: column !important;
    width: 100% !important;
    gap: 12px !important;
    margin-bottom: 24px !important;
  }
  .hero-grand .hero-actions .btn-primary,
  .hero-grand .hero-actions .btn-secondary {
    width: 100% !important;
    padding: 14px 20px !important;
  }
}
'''

def update_file(path):
    if not os.path.exists(path):
        print(f"Skipping {path} (not found)")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Google Fonts links
    font_pattern = r'<link[^>]*fonts\.googleapis\.com/css2\?[^>]*>'
    matches = list(re.finditer(font_pattern, content))
    if matches:
        for m in matches:
            tag = m.group(0)
            if 'as="style"' in tag:
                content = content.replace(tag, NEW_FONT_PRELOAD)
            elif 'onload=' in tag:
                content = content.replace(tag, NEW_FONT_PRINT)
            elif 'rel="stylesheet"' in tag:
                content = content.replace(tag, NEW_FONT_STYLESHEET)
        print(f"[✓ FONTS UPDATED] {path}")

    # 2. Update Hero Picture element
    picture_pattern = r'<picture>\s*<source[^>]*krisala_hiranandani_grand_entrance_hero_mobile\.webp[^>]*/>\s*<source[^>]*krisala_hiranandani_grand_entrance_hero\.webp[^>]*/>\s*<img[^>]*class="hero-img[^>]*>\s*</picture>'
    if re.search(picture_pattern, content, re.DOTALL):
        content = re.sub(picture_pattern, NEW_HERO_PICTURE, content, flags=re.DOTALL)
        print(f"[✓ HERO PICTURE REPLACED] {path}")
    else:
        # Fallback regex matching picture inside hero-bg
        picture_fallback = r'<div class="hero-bg">.*?<picture>.*?</picture>'
        if re.search(picture_fallback, content, re.DOTALL):
            content = re.sub(r'<picture>.*?</picture>', NEW_HERO_PICTURE, content, count=1, flags=re.DOTALL)
            print(f"[✓ HERO PICTURE REPLACED (Fallback)] {path}")

    # 3. Add kicker if not already present
    if 'hero-legacy-kicker' not in content:
        # insert right before <h1 class="hero-title">
        h1_match = re.search(r'(<h1 class="hero-title">)', content)
        if h1_match:
            kicker_html = '<div class="hero-legacy-kicker">Krisala Brings Hiranandani\'s Legacy to Pune</div>\n'
            content = content[:h1_match.start()] + kicker_html + content[h1_match.start():]
            print(f"[✓ HERO KICKER INSERTED] {path}")

    # 4. Inject Premium Hero CSS into <style>
    if 'ULTRA-PREMIUM HERO TYPOGRAPHY' not in content:
        if '</style>' in content:
            content = content.replace('</style>', f"{PREMIUM_HERO_CSS}\n</style>", 1)
            print(f"[✓ HERO CSS INJECTED] {path}")
        else:
            content = content.replace('</head>', f"<style>{PREMIUM_HERO_CSS}</style>\n</head>", 1)
            print(f"[✓ HERO CSS INJECTED (<head>)] {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[SUCCESS] Fully updated {path}\n")

def main():
    print("=" * 70)
    print("Deploying Hiranandani Legacy Hero Image & Ultra-Premium Typography")
    print("=" * 70)
    for p in TARGET_FILES:
        update_file(p)

if __name__ == '__main__':
    main()

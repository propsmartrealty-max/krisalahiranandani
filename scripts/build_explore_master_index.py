#!/usr/bin/env python3
"""
Master Explore Hub & Real Estate Directory Builder
Builds /explore/index.html linking all 101+ programmatic landing nodes.
Generates an internal crawl mesh that funnels Googlebot PageRank to convert
all 38,953 discovered URLs into active indexing impressions.
"""

import os
import glob
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPLORE_DIR = os.path.join(ROOT_DIR, "explore")

def get_explore_pages():
    pages = []
    for f in sorted(os.listdir(EXPLORE_DIR)):
        if f.endswith(".html") and f != "index.html":
            slug = f[:-5]
            fpath = os.path.join(EXPLORE_DIR, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                c = fp.read()
            soup = BeautifulSoup(c, "html.parser")
            title = soup.title.string if soup.title else slug.replace("-", " ").title()
            h1 = soup.find("h1").get_text(strip=True) if soup.find("h1") else title
            desc_tag = soup.find("meta", {"name": "description"})
            desc = desc_tag["content"] if desc_tag and "content" in desc_tag.attrs else ""
            
            # Categorize
            category = "General"
            if any(k in slug for k in ["2-bhk", "3-bhk", "4-bhk", "duplex", "penthouses"]):
                category = "Apartments & Typologies"
            elif any(k in slug for k in ["plot", "villa", "della", "equestrian", "bungalow"]):
                category = "Villa Plots & Land"
            elif any(k in slug for k in ["vs-", "comparison"]):
                category = "Township Comparisons"
            elif any(k in slug for k in ["under-", "price", "cost-sheet", "payment-plan"]):
                category = "Pricing & Budgets"
            elif any(k in slug for k in ["infosys", "wipro", "tcs", "techzone", "quadron", "embassy"]):
                category = "IT Park Proximity"
            elif any(k in slug for k in ["mahalunge", "wakad", "punawale", "baner", "balewadi", "tathawade", "ravet", "marunji", "expressway", "corridor"]):
                category = "Localities & Micro-Markets"
            else:
                category = "Buyer Guides & Due Diligence"

            pages.append({
                "slug": slug,
                "url": f"/explore/{slug}",
                "title": title.replace("™", "").strip(),
                "h1": h1,
                "desc": desc,
                "category": category
            })
    return pages

def build_explore_index():
    pages = get_explore_pages()
    
    # Group by category
    categories = [
        "Apartments & Typologies",
        "Villa Plots & Land",
        "Localities & Micro-Markets",
        "Pricing & Budgets",
        "IT Park Proximity",
        "Township Comparisons",
        "Buyer Guides & Due Diligence"
    ]
    
    sections_html = ""
    for cat in categories:
        cat_pages = [p for p in pages if p["category"] == cat]
        if not cat_pages:
            continue
            
        links_cards = ""
        for p in cat_pages:
            clean_title = p['title'].split("|")[0].split("—")[0].strip()
            links_cards += f"""
            <a href="{p['url']}" class="explore-card">
              <span class="explore-badge">{cat}</span>
              <h3 class="explore-card-title">{clean_title}</h3>
              <p class="explore-card-desc">{p['desc'][:130]}...</p>
              <span class="explore-link-arrow">Explore Guide &amp; Cost Sheet &rarr;</span>
            </a>
            """
            
        sections_html += f"""
        <div class="explore-category-group" style="margin-bottom: 50px;">
          <h2 class="explore-cat-heading" style="font-family: var(--font-heading); color: #fff; font-size: clamp(1.6rem, 2.8vw, 2.2rem); margin-bottom: 20px; border-bottom: 1px solid rgba(197,160,89,0.3); padding-bottom: 12px; display: flex; align-items: center; justify-content: space-between;">
            <span>{cat}</span>
            <span style="font-size: 0.9rem; color: var(--gold-bright); font-family: var(--font-body); font-weight: 600;">{len(cat_pages)} Dedicated Hubs</span>
          </h2>
          <div class="explore-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            {links_cards}
          </div>
        </div>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<style>
@font-face {{
  font-family: 'Cormorant Garamond';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/cormorantgaramond/v21/co3bmX5slCNuHLi8bLeY9MK7whWMhyjYqXtKky2F7g.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}}
:root {{
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
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{ background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-body); line-height: 1.6; overflow-x: hidden; }}
.container {{ max-width: 1400px; margin: 0 auto; padding: 0 40px; }}
@media (max-width: 768px) {{ .container {{ padding: 0 20px; }} }}
.navbar {{ position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; padding: 16px 0; background: rgba(9, 10, 15, 0.85); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(197, 160, 89, 0.2); }}
.nav-container {{ display: flex; align-items: center; justify-content: space-between; max-width: 1400px; margin: 0 auto; padding: 0 40px; }}
@media (max-width: 768px) {{ .nav-container {{ padding: 0 20px; }} }}
.header-logo {{ height: 42px !important; width: 310px !important; max-width: 100% !important; aspect-ratio: 310/42 !important; object-fit: contain !important; display: block !important; }}
.header-actions {{ display: flex; align-items: center; gap: 12px; }}
.hero-directory {{ padding: 140px 0 60px; text-align: center; background: radial-gradient(circle at 50% 20%, rgba(197,160,89,0.12) 0%, rgba(9,10,15,1) 80%); }}
.hero-title {{ font-family: var(--font-heading); font-size: clamp(2.4rem, 5vw, 4.2rem); color: #fff; line-height: 1.15; margin-bottom: 18px; }}
.hero-title span {{ color: var(--gold-bright); }}
.hero-subtitle {{ font-size: 1.15rem; color: var(--text-muted); max-width: 850px; margin: 0 auto 30px; line-height: 1.6; }}
.hero-badges {{ display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 30px; }}
.badge-item {{ background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.3); color: var(--gold-bright); padding: 6px 14px; border-radius: 50px; font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
.explore-card {{ background: rgba(16, 18, 26, 0.85); border: 1px solid rgba(197, 160, 89, 0.22); border-radius: 8px; padding: 22px; text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.3s ease; }}
.explore-card:hover {{ border-color: var(--gold-bright); transform: translateY(-4px); background: rgba(22, 25, 38, 0.95); box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
.explore-badge {{ display: inline-block; color: var(--gold-bright); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }}
.explore-card-title {{ font-family: var(--font-heading); font-size: 1.25rem; color: #fff; line-height: 1.3; margin-bottom: 8px; }}
.explore-card-desc {{ font-size: 0.86rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px; flex-grow: 1; }}
.explore-link-arrow {{ color: var(--gold-bright); font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }}
.btn-primary {{ background: linear-gradient(135deg, #dfc07b 0%, #c5a059 100%); color: #000; font-weight: 700; padding: 12px 24px; border-radius: 4px; border: none; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }}
.footer {{ background: #050608; border-top: 1px solid rgba(197, 160, 89, 0.2); padding: 60px 0 30px; font-size: 0.88rem; color: var(--text-muted); margin-top: 60px; }}
</style>
<title>Township Explorer &amp; Buyer Directory | Krisala Hiranandani Pune</title>
<meta name="description" content="Explore 68 curated residential &amp; investment guides for Krisala Hiranandani 105-acre township in North Hinjewadi, Pune: 2–4 BHK apartments, Della villa plots, pricing &amp; RERA sanctions."/>
<meta name="keywords" content="Krisala Hiranandani Township Pune, Hiranandani Pune guides, Hinjewadi flats directory, Della 5000 sq.ft. villa plots"/>
<meta content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" name="robots"/>
<link href="https://krisalahiranandanitownships.com/explore" id="seoCanonical" rel="canonical"/>
<link href="/favicon.png" rel="icon" sizes="32x32" type="image/png"/>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "CollectionPage",
      "@id": "https://krisalahiranandanitownships.com/explore#webpage",
      "url": "https://krisalahiranandanitownships.com/explore",
      "name": "Township Explorer & Buyer Directory | Krisala Hiranandani Pune",
      "description": "Curated real estate directory covering 68 buyer, transit, payment plan, and comparison guides for North Hinjewadi.",
      "dateModified": "2026-11-25",
      "speakable": {{
        "@type": "SpeakableSpecification",
        "cssSelector": ["#ai-overview-summary", "h1"]
      }},
      "breadcrumb": {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Township", "item": "https://krisalahiranandanitownships.com/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Explore Directory", "item": "https://krisalahiranandanitownships.com/explore" }}
        ]
      }}
    }},
    {{
      "@type": "RealEstateAgent",
      "@id": "https://krisalahiranandanitownships.com/explore#agent",
      "name": "Propsmart Realty — Authorised Channel Partner (Krisala Hiranandani Township)",
      "telephone": "+917744009295",
      "identifier": "MahaRERA Agent A031262401295",
      "url": "https://krisalahiranandanitownships.com/explore"
    }}
  ]
}}
</script>
</head>
<body>

<header class="navbar">
  <div class="nav-container">
    <a href="/" class="logo" aria-label="Krisala Hiranandani Home">
      <img src="/public/krisala-hiranandani-logo-310.webp" srcset="/public/krisala-hiranandani-logo-310.webp 1x, /public/krisala-hiranandani-logo.webp 2x" alt="Krisala Hiranandani Township Pune Logo" width="310" height="42" class="header-logo"/>
    </a>
    <div class="header-actions">
      <a href="/pricing" class="btn-primary" style="padding: 8px 16px; font-size: 0.85rem;">Price List 2026</a>
      <a href="https://wa.me/917744009295?text=Hello%2C+I+am+browsing+the+Krisala+Hiranandani+Township+Hinjewadi%2C+Pune+Explorer+and+would+like+the+brochure+and+cost+sheet." class="btn-primary" style="background: #25D366; color: #fff; padding: 8px 16px; font-size: 0.85rem;" target="_blank" rel="noopener noreferrer">WhatsApp</a>
    </div>
  </div>
</header>

<main>
  <section class="hero-directory">
    <div class="container">
      <div class="hero-badges">
        <span class="badge-item">105-Acre Master Township</span>
        <span class="badge-item">MahaRERA PR1260002500600</span>
        <span class="badge-item">MahaRERA Agent A031262401295</span>
      </div>
      <h1 class="hero-title">Township Explorer &amp; <span>68 Curated Buyer Guides</span></h1>
      <p class="hero-subtitle">Structured micro-market, configuration, payment schedule, and IT-corridor guides across the 105-acre estate in North Hinjewadi, Pune.</p>
      
      <div id="ai-overview-summary" style="max-width: 880px; margin: 0 auto 28px; background: rgba(16, 18, 26, 0.9); border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 10px; padding: 20px 24px; text-align: left;">
        <h2 style="font-family: var(--font-heading); color: var(--gold-bright); font-size: 1.3rem; margin-bottom: 8px;">What topics are covered in the Township Explorer Directory?</h2>
        <p style="color: #e2e8f0; font-size: 0.92rem; line-height: 1.65; margin: 0;">This curated index organizes 68 dedicated residential guides covering 2, 3, and 4 BHK apartments (from ₹79L*), 5,000 sq.ft. Della Villa Plots (from ₹3.75 Cr*), 20:80 payment schedules, IT park commute distances to Infosys and TCS, NRI FEMA norms, and Pune West project comparisons.</p>
      </div>

      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; margin-bottom: 25px;">
        <a href="/pricing" style="color: #dfc07b; background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.3); padding: 8px 16px; border-radius: 4px; text-decoration: none; font-size: 0.88rem; font-weight: 600;">Pricing Sheet (from ₹79L*)</a>
        <a href="/colosseum" style="color: #dfc07b; background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.3); padding: 8px 16px; border-radius: 4px; text-decoration: none; font-size: 0.88rem; font-weight: 600;">The Colosseum Phase 4</a>
        <a href="/arcadia" style="color: #dfc07b; background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.3); padding: 8px 16px; border-radius: 4px; text-decoration: none; font-size: 0.88rem; font-weight: 600;">Sector Arcadia</a>
        <a href="/della-racecourse" style="color: #dfc07b; background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.3); padding: 8px 16px; border-radius: 4px; text-decoration: none; font-size: 0.88rem; font-weight: 600;">Della 5,000 Sq.Ft. Villa Plots (₹3.75 Cr*)</a>
      </div>
    </div>
  </section>

  <section class="directory-content" style="padding: 40px 0 80px;">
    <div class="container">
      {sections_html}
      <div class="category-section" id="visual-web-stories">
        <div class="category-header">
          <div class="category-title-wrap">
            <h2>Interactive Visual Web Stories</h2>
          </div>
          <span class="category-count">14 Stories</span>
        </div>
        <div class="explore-grid">
          <a href="/stories/township-grand-living" class="explore-card"><span class="explore-badge">Visual Story • Township</span><h3 class="explore-card-title">105-Acre Township Grand Living</h3><p class="explore-card-desc">Visual walkthrough of Darumbre's 105-acre master plan, 70% open greens, and neoclassical civic architecture.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/della-equestrian-villa-plots" class="explore-card"><span class="explore-badge">Visual Story • Della District</span><h3 class="explore-card-title">Della Racecourse &amp; Villa Plots</h3><p class="explore-card-desc">Explore 98 Private Luxury Villas, 5,000 sq.ft. freehold villa plots (from ₹3.75 Cr*), and the 8-acre polo track.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/the-colosseum-phase-4" class="explore-card"><span class="explore-badge">Visual Story • Phase 4</span><h3 class="explore-card-title">The Colosseum Phase 4 Towers</h3><p class="explore-card-desc">Neoclassical Roman colonnades, amphitheatre podium, and 2–3 BHK homes starting ₹82.99 Lakhs*.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/sector-arcadia-luxury-living" class="explore-card"><span class="explore-badge">Visual Story • Phase 1 &amp; 2</span><h3 class="explore-card-title">Sector Arcadia Luxury Living</h3><p class="explore-card-desc">Inside Mivan 2 &amp; 3 BHK residences starting ₹79 Lakhs* near Infosys, Wipro, and TCS Hinjewadi.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/sector-icon-sky-residences" class="explore-card"><span class="explore-badge">Visual Story • Ultra-Luxury</span><h3 class="explore-card-title">Sector Icon 4 BHK Sky Villas</h3><p class="explore-card-desc">18ft double-height sky duplexes with racecourse sun decks from ₹2.10 Crore*.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/hinjewadi-it-investment-roi" class="explore-card"><span class="explore-badge">Visual Story • Investment</span><h3 class="explore-card-title">Hinjewadi IT Investment ROI</h3><p class="explore-card-desc">PMRDA 128m Ring Road, Metro Line 3 catalyst, and rental yield trajectory across North Hinjewadi.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/maharera-legal-sanctions-guide" class="explore-card"><span class="explore-badge">Visual Story • Compliance</span><h3 class="explore-card-title">MahaRERA Sanctions Guide</h3><p class="explore-card-desc">Verified registrations PR1260002500600, PR1260002600818, PR1260002502438, and escrow safeguards.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/nri-investment-desk-pune" class="explore-card"><span class="explore-badge">Visual Story • Global NRI</span><h3 class="explore-card-title">NRI Investment Desk Pune</h3><p class="explore-card-desc">FEMA repatriation, NRE/NRO escrow remittances, digital KYC, and USD/AED yield math.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/pune-metro-line-3-hinjewadi-stations" class="explore-card"><span class="explore-badge">Visual Story • Metro 3</span><h3 class="explore-card-title">23 Stations: Pune Metro Line 3</h3><p class="explore-card-desc">Station-by-station Hinjewadi to Civil Court rail guide and North Hinjewadi TOD appreciation.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/pmrda-128m-ring-road-impact" class="explore-card"><span class="explore-badge">Visual Story • Ring Road</span><h3 class="explore-card-title">PMRDA 128m Ring Road</h3><p class="explore-card-desc">Darumbre, Marunji &amp; Urse expressway link lifting West Pune capital velocity.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/pune-flat-rates-2026-comparison" class="explore-card"><span class="explore-badge">Visual Story • 2026 Rates</span><h3 class="explore-card-title">Hinjewadi vs Wakad vs Baner</h3><p class="explore-card-desc">Compare per-sq.ft. flat prices and 30% higher carpet value in North Hinjewadi.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/pune-stamp-duty-women-rebate-guide" class="explore-card"><span class="explore-badge">Visual Story • Tax Guide</span><h3 class="explore-card-title">Stamp Duty &amp; Women Rebate 2026</h3><p class="explore-card-desc">1% Women Grahlakshmi rebate and 0% GST plot savings explained.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/mivan-construction-vs-brick-guide" class="explore-card"><span class="explore-badge">Visual Story • Engineering</span><h3 class="explore-card-title">Mivan Formwork vs Brick</h3><p class="explore-card-desc">Monolithic shear-wall waterproofing, seismic durability, and acoustic insulation.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
          <a href="/stories/hiranandani-powai-vs-hinjewadi-wealth" class="explore-card"><span class="explore-badge">Visual Story • Legacy</span><h3 class="explore-card-title">Powai to Hinjewadi 55x Formula</h3><p class="explore-card-desc">How integrated neoclassical townships + Della Racecourse drive compounding wealth.</p><span class="explore-link-arrow">Open Web Story &rarr;</span></a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="container" style="text-align: center;">
    <p style="margin-bottom: 12px; color: #fff; font-size: 0.95rem;"><strong>Krisala Hiranandani Township Pune</strong> • PMRDA 128m Ring Road Corridor, North Hinjewadi, Darumbre, Pune 410506</p>
    <p style="margin-bottom: 14px; font-size: 0.82rem; line-height: 1.6;">Marketed by Authorised Real Estate Agent: Propsmart Realty (MahaRERA Reg: A031262401295). Project MahaRERA Registrations: Sector Arcadia (PR1260002500600), The Colosseum Phase 4 (PR1260002600818), Sector Everlyn / Della (PR1260002502438). Registered on maharera.maharashtra.gov.in.</p>
    <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.82rem; margin-top: 15px;">
      <a href="/" style="color: #dfc07b; text-decoration: none;">Township</a>
      <a href="/pricing" style="color: #dfc07b; text-decoration: none;">Price List 2026</a>
      <a href="/masterplan" style="color: #dfc07b; text-decoration: none;">Master Plan</a>
      <a href="/floor-plans" style="color: #dfc07b; text-decoration: none;">Floor Plans</a>
      <a href="/colosseum" style="color: #dfc07b; text-decoration: none;">The Colosseum</a>
      <a href="/arcadia" style="color: #dfc07b; text-decoration: none;">Sector Arcadia</a>
      <a href="/della-racecourse" style="color: #dfc07b; text-decoration: none;">Della Racecourse</a>
      <a href="/site-address" style="color: #dfc07b; text-decoration: none;">Site Address</a>
      <a href="/reviews" style="color: #dfc07b; text-decoration: none;">Reviews</a>
      <a href="/disclaimer" style="color: #888; text-decoration: none;">Disclaimer</a>
      <a href="/privacy-policy" style="color: #888; text-decoration: none;">Privacy Policy</a>
    </div>
    <p style="margin-top: 20px; font-size: 0.78rem; color: #666;">&copy; 2026 Krisala Hiranandani Township. All rights reserved. Prices subject to change without notice.</p>
  </div>
</footer>

</body>
</html>
"""

    out_file = os.path.join(EXPLORE_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as fp:
        fp.write(full_html)
    print(f"[✓ SUCCESS] Built explore/index.html with {len(pages)} categorized landing hubs!")

if __name__ == "__main__":
    build_explore_index()

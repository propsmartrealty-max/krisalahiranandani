#!/usr/bin/env python3
"""
Major SEO Content Expansion Engine
Builds 3 Strategic Authority Hubs:
1. floor-plans.html (/floor-plans)
2. construction-status.html (/construction-status)
3. north-hinjewadi.html (/north-hinjewadi)
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Shared CSS & Header Template
COMMON_STYLES = """
    <style>
        @font-face {
            font-family: 'Cormorant Garamond';
            font-style: normal;
            font-weight: 700;
            font-display: optional;
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
        .nav-links { display: flex; align-items: center; gap: 24px; }
        .nav-link { color: var(--text-muted); text-decoration: none; font-size: 0.88rem; font-weight: 500; transition: color 0.3s ease; }
        .nav-link:hover, .nav-link.active { color: var(--gold-bright); }
        .btn-primary { background: linear-gradient(135deg, #dfc07b 0%, #c5a059 100%); color: #000; font-weight: 600; padding: 12px 24px; border-radius: 4px; border: none; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.9rem; }
        .btn-secondary { background: rgba(255,255,255,0.06); color: #fcfbf7; border: 1px solid rgba(197,160,89,0.4); padding: 12px 24px; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.9rem; }
        .hero { position: relative; padding: 140px 0 60px; background: linear-gradient(180deg, rgba(9,10,15,0.85) 0%, var(--bg-dark) 100%); text-align: center; }
        .hero-title { font-family: var(--font-heading); font-size: clamp(2.3rem, 5vw, 4rem); line-height: 1.15; margin-bottom: 16px; color: #fff; font-weight: 700; }
        .hero-title span { color: var(--gold-bright); }
        .hero-subtitle { font-size: clamp(0.95rem, 1.8vw, 1.15rem); color: var(--text-muted); max-width: 850px; margin: 0 auto 30px; line-height: 1.6; }
        .badge { display: inline-flex; align-items: center; gap: 8px; padding: 6px 16px; border-radius: 50px; background: rgba(197, 160, 89, 0.1); border: 1px solid rgba(197, 160, 89, 0.3); color: var(--gold-bright); font-size: 0.82rem; margin-bottom: 20px; }
        .section-py { padding: 60px 0; }
        .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px; }
        .feature-card { background: rgba(16, 18, 26, 0.85); border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 12px; padding: 32px; transition: all 0.3s ease; }
        .feature-card:hover { border-color: var(--gold-primary); transform: translateY(-3px); }
        .footer { background: var(--bg-dark-deep); border-top: 1px solid rgba(197, 160, 89, 0.2); padding: 50px 0 30px; font-size: 0.88rem; color: var(--text-muted); text-align: center; }
        @media (max-width: 1024px) { .nav-links { display: none; } }
    </style>
"""

NAV_HTML = """
    <header class="navbar">
        <div class="container nav-container">
            <a href="/" class="logo">
                <img src="/public/krisala-hiranandani-logo.webp" alt="Krisala Hiranandani Township Hinjewadi Logo" class="header-logo" width="310" height="42">
            </a>
            <nav class="nav-links">
                <a href="/" class="nav-link">Township</a>
                <a href="/hiranandani-pune" class="nav-link">Hiranandani Pune</a>
                <a href="/floor-plans" class="nav-link">Floor Plans</a>
                <a href="/construction-status" class="nav-link">Construction</a>
                <a href="/north-hinjewadi" class="nav-link">North Hinjewadi</a>
                <a href="/hiranandani-price-list-2026" class="nav-link">Price List</a>
                <a href="/reviews" class="nav-link">Reviews</a>
            </nav>
            <div class="header-actions">
                <a href="https://wa.me/917744009295?text=Hello%20Sales%20Team%2C%20I%20am%20inquiring%20about%20Krisala%20Hiranandani%20Township%20Hinjewadi." class="btn-primary" target="_blank" rel="noopener">WhatsApp Direct</a>
            </div>
        </div>
    </header>
"""

# ==============================================================================
# 1. BUILD floor-plans.html
# ==============================================================================
floor_plans_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {COMMON_STYLES}
    <link rel="canonical" href="https://krisalahiranandanitownships.com/floor-plans">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/floor-plans">
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/floor-plans">
    
    <title>Hiranandani Hinjewadi Floor Plans 2026 | 2, 3 &amp; 4 BHK &amp; Villa Plots Layout</title>
    <meta name="description" content="Download official 2026 architectural floor plans and MahaRERA carpet area layouts for Krisala Hiranandani Township Hinjewadi, Pune. 2 BHK (740-820 sq.ft.), 3 BHK (1,020-1,180 sq.ft.), 4 BHK Sky Duplexes &amp; Della Villa Plots.">
    <meta name="keywords" content="Hiranandani Hinjewadi floor plans, Krisala Hiranandani floor plans, Colosseum Hinjewadi floor plan, Sector Arcadia floor plans, Sector Icon sky duplex floor plans, Della villa plots layout, Hiranandani 2 BHK floor plan, Hiranandani 3 BHK floor plan Hinjewadi, Hiranandani 4 BHK floor plan Pune">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ApartmentComplex",
      "name": "Krisala Hiranandani Township Master Floor Plans",
      "description": "Architectural floor plans for 2, 3, 4 BHK luxury residences and villa plots in North Hinjewadi, Pune.",
      "url": "https://krisalahiranandanitownships.com/floor-plans",
      "hasFloorPlan": [
        {{
          "@type": "FloorPlan",
          "name": "Sector Arcadia 2 BHK Smart Luxury",
          "numberOfBedrooms": 2,
          "numberOfBathroomsTotal": 2,
          "floorSize": {{
            "@type": "QuantitativeValue",
            "value": 740,
            "unitCode": "FTK"
          }}
        }},
        {{
          "@type": "FloorPlan",
          "name": "The Colosseum 3 BHK Royal Residence",
          "numberOfBedrooms": 3,
          "numberOfBathroomsTotal": 3,
          "floorSize": {{
            "@type": "QuantitativeValue",
            "value": 1080,
            "unitCode": "FTK"
          }}
        }},
        {{
          "@type": "FloorPlan",
          "name": "Sector Icon 4 BHK Sky Duplex",
          "numberOfBedrooms": 4,
          "numberOfBathroomsTotal": 4,
          "floorSize": {{
            "@type": "QuantitativeValue",
            "value": 2100,
            "unitCode": "FTK"
          }}
        }}
      ]
    }}
    </script>
</head>
<body>
    {NAV_HTML}
    <main>
        <section class="hero">
            <div class="container">
                <div class="badge">📐 ARCHITECTURAL SCHEMATICS &amp; MAHARERA CARPET</div>
                <h1 class="hero-title">Hiranandani Hinjewadi <span>Floor Plans 2026</span></h1>
                <p class="hero-subtitle">Meticulously engineered neoclassical floor plans featuring zero dead space, cross-ventilation, panoramic racecourse vistas, and Vastu-compliant layouts in North Hinjewadi, Pune.</p>
                <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                    <a href="https://wa.me/917744009295?text=Please%20send%20me%20the%20complete%20high-res%20floor%20plan%20dossier%20for%20Krisala%20Hiranandani%20Township." class="btn-primary" target="_blank" rel="noopener">Request High-Res PDF Plans</a>
                    <a href="/hiranandani-price-list-2026" class="btn-secondary">View 2026 Price List</a>
                </div>
            </div>
        </section>

        <section class="section-py">
            <div class="container">
                <div class="card-grid">
                    <!-- 2 BHK -->
                    <div class="feature-card">
                        <span class="badge">SECTOR ARCADIA</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">2 BHK Smart Luxury</h2>
                        <p style="color: var(--gold-bright); font-size: 1.25rem; font-weight: 700; margin-bottom: 14px;">Carpet Area: 740 – 820 Sq.Ft.</p>
                        <ul style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
                            <li>Generous 18ft wide living &amp; dining zone with deck</li>
                            <li>Monolithic Mivan acoustic separation between bedrooms</li>
                            <li>Modular kitchen niche with utility dry balcony</li>
                            <li>Master suite with timber laminate flooring</li>
                        </ul>
                        <a href="https://wa.me/917744009295?text=I%20would%20like%20to%20download%20the%20Sector%20Arcadia%202%20BHK%20floor%20plan" class="btn-primary" style="width: 100%; text-align: center;">Download 2 BHK Plan PDF</a>
                    </div>

                    <!-- 3 BHK -->
                    <div class="feature-card" style="border-color: var(--gold-primary);">
                        <span class="badge" style="background: rgba(197, 160, 89, 0.25);">THE COLOSSEUM PHASE 4</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">3 BHK Royal Residence</h2>
                        <p style="color: var(--gold-bright); font-size: 1.25rem; font-weight: 700; margin-bottom: 14px;">Carpet Area: 1,020 – 1,180 Sq.Ft.</p>
                        <ul style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
                            <li>Direct views over the 8-acre turf racecourse &amp; polo club</li>
                            <li>Expansive 26ft grand living corridor with Roman balcony</li>
                            <li>3 en-suite luxury bathrooms with Kohler / Grohe fittings</li>
                            <li>Walk-in wardrobe recess in master bedroom</li>
                        </ul>
                        <a href="https://wa.me/917744009295?text=I%20would%20like%20to%20download%20The%20Colosseum%203%20BHK%20floor%20plan" class="btn-primary" style="width: 100%; text-align: center;">Download 3 BHK Plan PDF</a>
                    </div>

                    <!-- 4 BHK -->
                    <div class="feature-card">
                        <span class="badge">SECTOR ICON</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">4 BHK Sky Duplex</h2>
                        <p style="color: var(--gold-bright); font-size: 1.25rem; font-weight: 700; margin-bottom: 14px;">Carpet Area: 1,850 – 2,400 Sq.Ft.</p>
                        <ul style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.8; margin-bottom: 24px; padding-left: 20px;">
                            <li>Double-height living pavilion with 22ft ceiling clearance</li>
                            <li>Private internal architectural staircase &amp; terrace lounge</li>
                            <li>Dual master suites with panoramic Sahyadri views</li>
                            <li>Dedicated staff accommodation &amp; service entrance</li>
                        </ul>
                        <a href="https://wa.me/917744009295?text=I%20would%20like%20to%20download%20the%20Sector%20Icon%204%20BHK%20duplex%20plan" class="btn-primary" style="width: 100%; text-align: center;">Download 4 BHK Plan PDF</a>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>© 2026 Krisala Hiranandani Township North Hinjewadi Pune. MahaRERA Sanction Nos: PR1260002500600 | PR1260002600818</p>
        </div>
    </footer>
</body>
</html>"""

with open(os.path.join(ROOT_DIR, "floor-plans.html"), "w", encoding="utf-8") as f:
    f.write(floor_plans_html)
print("[✓] Created floor-plans.html")

# ==============================================================================
# 2. BUILD construction-status.html
# ==============================================================================
construction_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {COMMON_STYLES}
    <link rel="canonical" href="https://krisalahiranandanitownships.com/construction-status">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/construction-status">
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/construction-status">
    
    <title>Hiranandani Hinjewadi Construction Status 2026 | Possession Dates &amp; Milestone Reports</title>
    <meta name="description" content="Official construction updates and possession timeline for Krisala Hiranandani Township Hinjewadi, Pune. Real-time engineering milestones, slab progression, drone footage, and MahaRERA compliance reports.">
    <meta name="keywords" content="Hiranandani Hinjewadi construction status, Krisala Hiranandani possession date, Hiranandani Pune construction updates, The Colosseum construction status, Sector Arcadia progress, MahaRERA PR1260002500600 compliance">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Project",
      "name": "Krisala Hiranandani Township Hinjewadi Construction Updates",
      "url": "https://krisalahiranandanitownships.com/construction-status",
      "description": "Quarterly engineering milestones and construction progression for the 105-acre integrated township in North Hinjewadi, Pune.",
      "location": {{
        "@type": "Place",
        "name": "Krisala Hiranandani Township",
        "address": "PMRDA 128m Ring Road, North Hinjawadi, Darumbre, Pune 410506"
      }}
    }}
    </script>
</head>
<body>
    {NAV_HTML}
    <main>
        <section class="hero">
            <div class="container">
                <div class="badge">🏗️ LIVE ENGINEERING PROGRESS &amp; MAHARERA AUDIT</div>
                <h1 class="hero-title">Hiranandani Hinjewadi <span>Construction Status</span></h1>
                <p class="hero-subtitle">Comprehensive civil engineering progress, milestone updates, and possession timeline for the 105-acre neoclassical master township in North Hinjewadi, Pune.</p>
                <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                    <a href="https://wa.me/917744009295?text=Hello%20Team%2C%20please%20send%20me%20the%20latest%20drone%20inspection%20video%20and%20slab%20milestone%20report%20for%20Krisala%20Hiranandani." class="btn-primary" target="_blank" rel="noopener">Request Drone Video Report</a>
                    <a href="/site-address" class="btn-secondary">Visit Site Experience Center</a>
                </div>
            </div>
        </section>

        <section class="section-py">
            <div class="container">
                <div class="card-grid">
                    <!-- Colosseum Status -->
                    <div class="feature-card">
                        <span class="badge" style="color: #10b981; border-color: #10b981;">ON SCHEDULE • RERA 2028</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">The Colosseum (Phase 4)</h2>
                        <p style="color: var(--gold-bright); font-size: 1.1rem; font-weight: 600; margin-bottom: 12px;">MahaRERA: PR1260002600818</p>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 20px;">
                            Foundational piling and double basement excavation 100% completed. Structural podium casting underway. Monolithic shear walls being poured with German aluminium formwork.
                        </p>
                        <div style="background: rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 6px; font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Target Handover:</strong> Q4 2028 (Phase 4 Early Bird Towers)
                        </div>
                    </div>

                    <!-- Sector Arcadia Status -->
                    <div class="feature-card">
                        <span class="badge" style="color: #10b981; border-color: #10b981;">ADVANCED RCC • RERA 2027</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">Sector Arcadia</h2>
                        <p style="color: var(--gold-bright); font-size: 1.1rem; font-weight: 600; margin-bottom: 12px;">MahaRERA: PR1260002500600</p>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 20px;">
                            Towers 1, 2, and 3 progressing at a rapid 12-day slab cycle. Mid-level civil structural completion reached. Plumbing and electrical conduit rough-ins actively underway.
                        </p>
                        <div style="background: rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 6px; font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Target Handover:</strong> Q4 2027 (Pre-launch Enclave)
                        </div>
                    </div>

                    <!-- Della Collection Status -->
                    <div class="feature-card">
                        <span class="badge" style="color: #10b981; border-color: #10b981;">INFRASTRUCTURE READY</span>
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin: 12px 0 8px;">Della Villa Plots &amp; Turf Racecourse</h2>
                        <p style="color: var(--gold-bright); font-size: 1.1rem; font-weight: 600; margin-bottom: 12px;">Sanctioned Estate Layout</p>
                        <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 20px;">
                            8-acre equestrian turf track grading complete. Sub-grade storm water drains, underground high-voltage electrical ducts, and internal 60ft arterial roads fully paved.
                        </p>
                        <div style="background: rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 6px; font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Plot Registration:</strong> Immediate Allotment &amp; Custom Design Signoff
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>© 2026 Krisala Hiranandani Township North Hinjewadi Pune. Official Engineering &amp; Regulatory Audit.</p>
        </div>
    </footer>
</body>
</html>"""

with open(os.path.join(ROOT_DIR, "construction-status.html"), "w", encoding="utf-8") as f:
    f.write(construction_html)
print("[✓] Created construction-status.html")

# ==============================================================================
# 3. BUILD north-hinjewadi.html
# ==============================================================================
north_hinjewadi_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {COMMON_STYLES}
    <link rel="canonical" href="https://krisalahiranandanitownships.com/north-hinjewadi">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/north-hinjewadi">
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/north-hinjewadi">
    
    <title>North Hinjewadi Pune Real Estate | Hiranandani Township Darumbre Growth Corridor</title>
    <meta name="description" content="Explore North Hinjewadi (Darumbre), Pune West's fastest-growing luxury corridor. 105-Acre Krisala Hiranandani Township on PMRDA 128m Ring Road, 7 mins from Hinjewadi Metro Line 3 Megapolis Station.">
    <meta name="keywords" content="North Hinjewadi, North Hinjewadi Pune, Hiranandani North Hinjewadi, Darumbre Hinjewadi, Hinjewadi Phase 4, PMRDA 128m Ring Road flats, Hinjewadi real estate future, flats in North Hinjewadi, luxury townships West Pune">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Place",
      "name": "North Hinjewadi Integrated Growth Corridor",
      "description": "High-growth residential and IT corridor along PMRDA 128m Ring Road in Pune West.",
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 18.5913,
        "longitude": 73.7389
      }}
    }}
    </script>
</head>
<body>
    {NAV_HTML}
    <main>
        <section class="hero">
            <div class="container">
                <div class="badge">🚀 PUNE WEST STRATEGIC MASTER PLAN</div>
                <h1 class="hero-title">North Hinjewadi <span>Growth Corridor</span></h1>
                <p class="hero-subtitle">Why West Pune's premier tech executives and NRI investors are migrating to North Hinjewadi (Darumbre) along the PMRDA 128m Ring Road for zero-traffic living and 105 acres of masterplanned luxury.</p>
                <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                    <a href="/site-address" class="btn-primary">View Location Map &amp; Directions</a>
                    <a href="/hiranandani-price-list-2026" class="btn-secondary">Check 2026 Price List</a>
                </div>
            </div>
        </section>

        <section class="section-py">
            <div class="container">
                <div class="card-grid">
                    <div class="feature-card">
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin-bottom: 12px;">Zero-Traffic Commute</h2>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8;">
                            Located outside the congested Phase 1 bottleneck, North Hinjewadi connects directly via the high-speed <strong>PMRDA 128m Ring Road</strong>. Reach Infosys Phase 1 in 12 minutes, Wipro Circle in 10 minutes, and TCS Sahyadri Park in 14 minutes without hitting internal IT park gridlock.
                        </p>
                    </div>

                    <div class="feature-card">
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin-bottom: 12px;">PMRDA 128m Ring Road</h2>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8;">
                            The 128-meter wide Ring Road serves as Western Pune's primary arterial spine, providing seamless multi-lane access between the Mumbai-Pune Expressway (Urse Toll, 10 mins), Hinjewadi Phase 3, Baner, and the upcoming Pune Ring Road economic clusters.
                        </p>
                    </div>

                    <div class="feature-card">
                        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: #fff; margin-bottom: 12px;">Metro Line 3 Connectivity</h2>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.8;">
                            Just 7 minutes from the Hinjewadi Metro Line 3 Megapolis terminus station, linking North Hinjewadi residents to Shivaji Nagar and central Pune in under 35 minutes via elevated rapid transit.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>© 2026 Krisala Hiranandani Township North Hinjewadi Pune. MahaRERA PR1260002500600.</p>
        </div>
    </footer>
</body>
</html>"""

with open(os.path.join(ROOT_DIR, "north-hinjewadi.html"), "w", encoding="utf-8") as f:
    f.write(north_hinjewadi_html)
print("[✓] Created north-hinjewadi.html")

print("\nMajor SEO content expansion pages generated successfully.")

#!/usr/bin/env python3
"""
Ecosystem Expansion Pages Generator
Generates:
1. amenities.html (100+ Master Amenities directory)
2. nri.html (NRI Investment & Repatriation Desk)
3. connectivity.html (North Hinjewadi & Transit Infrastructure)
"""

import os

HEADER_HTML = """    <!-- Navigation -->
    <header class="navbar" id="navbar">
        <div class="container nav-container">
            <a href="/" class="logo" style="text-decoration: none;" aria-label="Krisala Hiranandani Home">
                <img src="/public/krisala-hiranandani-logo.webp"
                    onerror="this.onerror=null; this.src='/public/krisala-hiranandani-logo.png';"
                    alt="Krisala Hiranandani Township Hinjewadi Logo" class="header-logo" width="280" height="38" fetchpriority="high">
            </a>
            <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
                <a href="/" class="nav-link">Township</a>
                <a href="/everlyn" class="nav-link">Everlyn</a>
                <a href="/arcadia" class="nav-link">Arcadia</a>
                <a href="/icon" class="nav-link">Icon</a>
                <a href="/della" class="nav-link">Della Plots</a>
                <a href="/racecourse" class="nav-link">Racecourse</a>
                <a href="/amenities" class="nav-link">Amenities</a>
                <a href="/pricing" class="nav-link">Pricing</a>
                <a href="/gallery" class="nav-link">Gallery</a>
                <a href="/masterplan" class="nav-link">Masterplan</a>
                <a href="/connectivity" class="nav-link">Connectivity</a>
                <a href="/nri" class="nav-link">NRI Desk</a>
                <a href="/compare" class="nav-link">Compare</a>
                <a href="/blog" class="nav-link">Blog</a>
            </nav>
            <div class="header-actions">
                <button class="btn-primary open-modal" aria-haspopup="dialog" data-magnet="brochure">Enquire Now</button>
                <div class="hamburger-menu" id="hamburgerMenu" aria-label="Toggle navigation" role="button" tabindex="0">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </header>"""

FOOTER_HTML = """    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div class="footer-grid">
                <div class="footer-col">
                    <img src="/public/krisala-hiranandani-logo.webp"
                        onerror="this.onerror=null; this.src='/public/krisala-hiranandani-logo.png';"
                        alt="Krisala Hiranandani Township Logo" class="footer-logo" width="260" height="35" loading="lazy">
                    <p style="margin-top: 15px; font-size: 0.9rem; line-height: 1.7; color: var(--text-muted);">
                        India's 1st Integrated Equestrian Township in North Hinjewadi, Pune. A landmark 105-acre joint venture between Krisala Developers and Hiranandani Communities with Della Resorts.
                    </p>
                    <div style="margin-top: 20px;">
                        <span class="badge badge-gold" style="font-size: 0.8rem; padding: 6px 12px;">MahaRERA: PR1260002502438 &amp; PR1260002600818</span>
                    </div>
                </div>

                <div class="footer-col">
                    <h4>Ecosystem Portals</h4>
                    <ul class="footer-links">
                        <li><a href="/arcadia">Sector Arcadia (2 &amp; 3 BHK)</a></li>
                        <li><a href="/icon">Sector Icon (Sky Villas)</a></li>
                        <li><a href="/della">The Della Collection (Plots)</a></li>
                        <li><a href="/racecourse">8-Acre Private Racecourse</a></li>
                        <li><a href="/amenities">100+ Master Amenities</a></li>
                        <li><a href="/pricing">2026 Price List &amp; Payment Plans</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4>Research &amp; Location</h4>
                    <ul class="footer-links">
                        <li><a href="/masterplan">105-Acre Masterplan Blueprint</a></li>
                        <li><a href="/connectivity">Connectivity &amp; Metro Line 3</a></li>
                        <li><a href="/neighborhood">North Hinjewadi Micro-Market</a></li>
                        <li><a href="/nri">NRI Investment Desk</a></li>
                        <li><a href="/compare">Competitor Benchmark</a></li>
                        <li><a href="/knowledge-hub">Investment ROI Whitepaper</a></li>
                        <li><a href="/blog">Real Estate Research Blog</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4>Sales Concierge Desk</h4>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 12px;">
                        Authorized Partner: Propsmart Realty (MahaRERA: A52100024102)
                    </p>
                    <p style="margin-bottom: 8px;">
                        <a href="tel:+917744009295" style="color: var(--gold-primary); font-weight: 600; font-size: 1.05rem;">
                            <i class="ph ph-phone"></i> +91 7744009295
                        </a>
                    </p>
                    <p style="margin-bottom: 15px; font-size: 0.85rem; color: var(--text-muted);">
                        Site: Sector Arcadia &amp; Della Precinct, Hinjewadi Phase 3, Pune 411057
                    </p>
                    <a href="/public/brochure/Krisala-Hiranandani-Township-Official-Brochure.pdf" download class="btn-outline" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 16px; font-size: 0.85rem;">
                        <i class="ph ph-file-pdf"></i> Download Official PDF Docket
                    </a>
                </div>
            </div>

            <div class="footer-bottom" style="margin-top: 40px; padding-top: 25px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 0.8rem; color: var(--text-muted);">
                <p>&copy; 2026 Krisala Hiranandani Township. All rights reserved. MahaRERA Phase 3: PR1260002502438 | Sector Icon: PR1260002600818 | CP RERA: A52100024102. <a href="/privacy-policy" style="color: var(--gold-light);">Privacy Policy</a></p>
            </div>
        </div>
    </footer>

    <!-- Lead Modal -->
    <div class="modal-overlay" id="leadModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
        <div class="modal-card glass-panel">
            <button class="modal-close" id="modalClose" aria-label="Close dialog">&times;</button>
            <div class="modal-header">
                <span class="badge badge-gold" id="modalBadge">Instant VIP Access</span>
                <h3 id="modalTitle" style="font-family: var(--font-heading); color: var(--text-main); margin-top: 10px;">Download Official Project Docket</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;" id="modalDesc">Enter your details to receive verified floor plans, 2026 price list &amp; CLP schedule.</p>
            </div>
            <form action="https://formsubmit.co/propsmartrealty@gmail.com" method="POST" class="modal-form" id="enquiryForm">
                <input type="hidden" name="_next" value="https://krisalahiranandanitownships.com/thank-you">
                <input type="hidden" name="_subject" value="New High-Intent Enquiry - Krisala Hiranandani Township">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="source_page" id="sourcePage" value="">
                
                <div class="form-group">
                    <label for="userName">Full Name *</label>
                    <input type="text" id="userName" name="name" required placeholder="e.g. Rahul Sharma" class="form-input">
                </div>
                <div class="form-group">
                    <label for="userPhone">Phone Number (WhatsApp) *</label>
                    <input type="tel" id="userPhone" name="phone" required placeholder="+91 98765 43210" pattern="[0-9+ ]{10,15}" class="form-input">
                </div>
                <div class="form-group">
                    <label for="userEmail">Email Address</label>
                    <input type="email" id="userEmail" name="email" placeholder="rahul@example.com" class="form-input">
                </div>
                <div class="form-group">
                    <label for="userConfig">Preferred Configuration</label>
                    <select id="userConfig" name="configuration" class="form-input">
                        <option value="2 BHK Arcadia (₹79L+)">2 BHK Arcadia (₹79 Lakhs* onwards)</option>
                        <option value="3 BHK Royale (₹1.18Cr+)">3 BHK Royale (₹1.18 Cr* onwards)</option>
                        <option value="4 BHK Sky Duplex (₹2.10Cr+)">4 BHK Sky Duplex (₹2.10 Cr* onwards)</option>
                        <option value="5 BHK Sky Mansion (₹3.20Cr+)">5 BHK Sky Mansion (₹3.20 Cr* onwards)</option>
                        <option value="Della Villa Plot (₹3.50Cr+)">The Della Collection Villa Plot</option>
                    </select>
                </div>
                <button type="submit" class="btn-primary" style="width: 100%; justify-content: center; padding: 14px;">
                    <i class="ph ph-lock-key"></i> Get Instant Access &amp; PDF Docket
                </button>
                <p style="font-size: 0.75rem; color: var(--text-muted); text-align: center; margin-top: 10px;">
                    🔒 100% Confidential. Zero spam. MahaRERA Authorized Concierge.
                </p>
            </form>
        </div>
    </div>

    <!-- Floating Concierge -->
    <div class="floating-actions">
        <a href="https://wa.me/917744009295?text=Hi%2C%20I%20am%20interested%20in%20Krisala%20Hiranandani%20Township.%20Please%20share%20details."
            class="float-btn float-whatsapp" target="_blank" aria-label="Chat on WhatsApp">
            <i class="ph ph-whatsapp-logo" aria-hidden="true"></i>
        </a>
        <a href="tel:+917744009295" class="float-btn float-call" aria-label="Call Assistance">
            <i class="ph ph-phone" aria-hidden="true"></i>
        </a>
    </div>

    <script src="/app.js" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const srcInput = document.getElementById('sourcePage');
            if (srcInput) srcInput.value = window.location.pathname;
        });
    </script>"""

def generate_amenities_page():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Canonical & Hreflang -->
    <link rel="canonical" href="https://krisalahiranandanitownships.com/amenities" />
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/amenities">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/amenities">

    <!-- Favicons -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" href="/favicon.ico">

    <!-- Title & SEO Meta -->
    <title>100+ Master Amenities | 8-Acre Racecourse &amp; 50,000 Sq.Ft. Clubhouse | Krisala Hiranandani Hinjewadi</title>
    <meta name="description" content="Discover 100+ curated lifestyle amenities at Krisala × Hiranandani Township, Hinjewadi: 8-acre private racecourse, 50,000 sq.ft. neoclassical clubhouse, Olympic lap pool, TERI 50-year hydrology &amp; sports arenas.">
    <meta name="keywords" content="Krisala Hiranandani amenities, 100 amenities Hinjewadi, private racecourse township Pune, equestrian polo club Pune, 50000 sqft clubhouse Hinjewadi, Olympic pool Hinjewadi, sports township Pune, Della amenities, TERI green township Pune">

    <!-- Robots & Geo -->
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="North Hinjawadi, Pune">
    <meta name="geo.position" content="18.5913;73.7389">
    <meta name="ICBM" content="18.5913, 73.7389">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://krisalahiranandanitownships.com/amenities">
    <meta property="og:title" content="100+ Master Amenities | Krisala Hiranandani Township Hinjewadi">
    <meta property="og:description" content="Explore India's 1st equestrian township amenities: 8-acre private racecourse, 50,000 sq.ft. neoclassical clubhouse, Olympic pools, tennis arenas &amp; TERI 50-year hydrology.">
    <meta property="og:image" content="https://krisalahiranandanitownships.com/public/everlyn/gallery/clubhouse_exterior.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="Krisala Hiranandani Township Pune">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:site" content="@KrisalaHiranandani">
    <meta property="twitter:title" content="100+ Master Amenities | Krisala Hiranandani Township Hinjewadi">
    <meta property="twitter:description" content="8-Acre racecourse, 50,000 sq.ft. clubhouse, Olympic pool &amp; sports courts in 105-acre mega township.">
    <meta property="twitter:image" content="https://krisalahiranandanitownships.com/public/everlyn/gallery/clubhouse_exterior.webp">

    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
    <script src="https://unpkg.com/@phosphor-icons/web" defer></script>
    <link rel="stylesheet" href="/style.css?v=2">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#08080a">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Place",
          "@id": "https://krisalahiranandanitownships.com/amenities#amenities",
          "name": "Krisala Hiranandani 100+ Master Amenities",
          "description": "Comprehensive lifestyle amenities ecosystem inside the 105-acre Krisala Hiranandani integrated township in North Hinjewadi, Pune. Featuring an 8-acre championship racecourse, 50,000 sq.ft. clubhouse, Olympic swimming pool, tennis and squash courts, co-working business lounges, and TERI 50-year circular hydrology reservoirs.",
          "url": "https://krisalahiranandanitownships.com/amenities",
          "photo": "https://krisalahiranandanitownships.com/public/everlyn/gallery/clubhouse_exterior.webp",
          "address": {{
            "@type": "PostalAddress",
            "streetAddress": "North Hinjawadi, Darumbre / Marunji",
            "addressLocality": "Pune",
            "addressRegion": "Maharashtra",
            "postalCode": "410506",
            "addressCountry": "IN"
          }}
        }},
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Township", "item": "https://krisalahiranandanitownships.com/" }},
            {{ "@type": "ListItem", "position": 2, "name": "Amenities", "item": "https://krisalahiranandanitownships.com/amenities" }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "How many total amenities are planned at Krisala Hiranandani Township?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "The township incorporates over 100+ curated lifestyle, equestrian, sports, wellness, and ecological amenities spread across 105 acres, anchored by an 8-acre private racecourse and a 50,000 sq.ft. multi-level neoclassical clubhouse."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Is the 8-acre racecourse open to all township residents?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Yes, residents of Sector Arcadia, Sector Icon, and The Della Collection have tiered privileges and access to the equestrian track, riding academy, polo club viewing pavilions, and stabling facilities."
              }}
            }},
            {{
              "@type": "Question",
              "name": "What is TERI 50-Year Hydrology and how does it benefit residents?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "TERI 50-Year Hydrology certification ensures circular, zero-discharge water self-sufficiency. Through rainwater harvesting reservoirs, biofiltration swales, and dual-plumbing recycling, the township reduces recurring municipal water dependence and maintenance bills by over 30%."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>

    <style>
        .amenities-hero {{
            padding: 160px 0 80px;
            background: radial-gradient(circle at 50% 20%, rgba(197, 160, 89, 0.12) 0%, rgba(8, 8, 10, 0.98) 80%);
            text-align: center;
        }}
        .filter-tabs {{
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin: 40px 0 30px;
        }}
        .tab-btn {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(197, 160, 89, 0.25);
            color: var(--text-muted);
            padding: 10px 20px;
            border-radius: 30px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.3s;
        }}
        .tab-btn.active, .tab-btn:hover {{
            background: var(--gold-primary);
            color: #000;
            border-color: var(--gold-primary);
            transform: translateY(-2px);
        }}
        .amenity-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(197, 160, 89, 0.18);
            border-radius: var(--border-radius);
            padding: 28px 24px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        .amenity-card:hover {{
            border-color: var(--gold-primary);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            background: rgba(255, 255, 255, 0.04);
        }}
        .amenity-icon {{
            font-size: 2.2rem;
            color: var(--gold-primary);
            margin-bottom: 16px;
        }}
        .amenity-card h3 {{
            font-family: var(--font-heading);
            font-size: 1.25rem;
            color: var(--text-main);
            margin-bottom: 10px;
        }}
        .amenity-card p {{
            color: var(--text-muted);
            font-size: 0.9rem;
            line-height: 1.6;
        }}
        .stats-banner {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 40px 0;
            text-align: center;
        }}
        .stat-item {{
            padding: 25px;
            border-radius: 8px;
            background: rgba(197, 160, 89, 0.05);
            border: 1px solid rgba(197, 160, 89, 0.2);
        }}
        .stat-num {{
            font-family: var(--font-heading);
            font-size: 2.2rem;
            color: var(--gold-light);
            font-weight: 700;
        }}
        .stat-lbl {{
            color: var(--text-muted);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 5px;
        }}
    </style>
</head>

<body>
{HEADER_HTML}

    <!-- Hero -->
    <section class="amenities-hero">
        <div class="container">
            <span class="badge badge-gold"><i class="ph ph-crown"></i> 105-Acre Master Township Infrastructure</span>
            <h1 style="font-family: var(--font-heading); font-size: clamp(2.2rem, 4vw, 3.8rem); color: var(--text-main); margin: 20px 0 15px;">
                100+ World-Class Master Amenities
            </h1>
            <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 820px; margin: 0 auto 30px; line-height: 1.8;">
                From India's first residential 8-acre championship racecourse to a 50,000 sq.ft. palatial neoclassical clubhouse, experience a benchmark in curated sports, wellness, and family leisure.
            </p>

            <div class="stats-banner">
                <div class="stat-item">
                    <div class="stat-num">100+</div>
                    <div class="stat-lbl">Curated Features</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">8 ACRES</div>
                    <div class="stat-lbl">Private Racecourse</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">50,000 SQ.FT.</div>
                    <div class="stat-lbl">Grand Clubhouse</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">70%</div>
                    <div class="stat-lbl">Open Green Podiums</div>
                </div>
                <div class="stat-item">
                    <div class="stat-num">TERI 50-YR</div>
                    <div class="stat-lbl">Certified Hydrology</div>
                </div>
            </div>

            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <button class="btn-primary open-modal" data-magnet="brochure">
                    <i class="ph ph-download-simple"></i> Download Amenities Brochure (PDF)
                </button>
                <a href="https://wa.me/917744009295?text=Hi%2C%20I%20would%20like%20to%20schedule%20a%20site%20visit%20to%20experience%20Krisala%20Hiranandani%20amenities." target="_blank" class="btn-outline">
                    <i class="ph ph-whatsapp-logo"></i> Book Experience Tour
                </a>
            </div>
        </div>
    </section>

    <!-- Filter Tabs & Directory Grid -->
    <section class="section" style="padding: 40px 0 90px;">
        <div class="container">
            <div class="filter-tabs" id="filterTabs">
                <button class="tab-btn active" data-filter="all">All Amenities (100+)</button>
                <button class="tab-btn" data-filter="equestrian">Equestrian &amp; Derby</button>
                <button class="tab-btn" data-filter="clubhouse">Clubhouse &amp; Wellness</button>
                <button class="tab-btn" data-filter="sports">Sports &amp; Fitness</button>
                <button class="tab-btn" data-filter="hydrology">Eco-Hydrology &amp; Greens</button>
                <button class="tab-btn" data-filter="family">Family &amp; Leisure</button>
                <button class="tab-btn" data-filter="business">Work &amp; Smart Living</button>
            </div>

            <div class="grid grid-3" id="amenitiesGrid">
                <!-- 1. Equestrian -->
                <div class="amenity-card" data-category="equestrian">
                    <div class="amenity-icon"><i class="ph ph-horse"></i></div>
                    <h3>8-Acre Private Racecourse</h3>
                    <p>Championship-grade 6-furlong oval turf galloping track designed to international equestrian racing specifications inside the Della precinct.</p>
                </div>
                <div class="amenity-card" data-category="equestrian">
                    <div class="amenity-icon"><i class="ph ph-trophy"></i></div>
                    <h3>International Polo Pavilion</h3>
                    <p>Members-only polo viewing lounge, private spectator boxes, and champagne viewing terrace overlooking the central turf arena.</p>
                </div>
                <div class="amenity-card" data-category="equestrian">
                    <div class="amenity-icon"><i class="ph ph-shield-star"></i></div>
                    <h3>Horse Riding Academy</h3>
                    <p>Professional training academy with certified equestrian coaches offering dressage, show-jumping, and leisure riding for residents.</p>
                </div>
                <div class="amenity-card" data-category="equestrian">
                    <div class="amenity-icon"><i class="ph ph-barn"></i></div>
                    <h3>Air-Cooled Horse Stables</h3>
                    <p>Private equine boarding stalls equipped with veterinary care on-call, daily grooming, and dedicated paddock turnout rings.</p>
                </div>

                <!-- 2. Clubhouse & Wellness -->
                <div class="amenity-card" data-category="clubhouse">
                    <div class="amenity-icon"><i class="ph ph-buildings"></i></div>
                    <h3>50,000 Sq.Ft. Neoclassical Clubhouse</h3>
                    <p>Multi-level architectural masterpiece with Greco-Roman colonnades, double-height grand lobby, and 5-star concierge reception desk.</p>
                </div>
                <div class="amenity-card" data-category="clubhouse">
                    <div class="amenity-icon"><i class="ph ph-waves"></i></div>
                    <h3>Olympic-Length Heated Lap Pool</h3>
                    <p>50-meter temperature-controlled infinity swimming pool with sunken sunbeds, poolside cabanas, and integrated water massage jets.</p>
                </div>
                <div class="amenity-card" data-category="clubhouse">
                    <div class="amenity-icon"><i class="ph ph-heartbeat"></i></div>
                    <h3>Ayurvedic Spa &amp; Turkish Hammam</h3>
                    <p>Dedicated therapeutic wellness center featuring separate men's and women's steam, sauna, Jacuzzi plunge tubs, and massage treatment rooms.</p>
                </div>
                <div class="amenity-card" data-category="clubhouse">
                    <div class="amenity-icon"><i class="ph ph-barbell"></i></div>
                    <h3>High-Tech Technogym Fitness Suite</h3>
                    <p>Fully equipped 5,000 sq.ft. gymnasium with biometric cardio consoles, free-weight rigs, TRX functional training zone, and personal trainers.</p>
                </div>

                <!-- 3. Sports & Fitness -->
                <div class="amenity-card" data-category="sports">
                    <div class="amenity-icon"><i class="ph ph-tennis-ball"></i></div>
                    <h3>Pro-Turf Tennis &amp; Pickleball Arena</h3>
                    <p>Three floodlit international standard acrylic cushioned tennis courts and two tournament-grade pickleball courts with stadium seating.</p>
                </div>
                <div class="amenity-card" data-category="sports">
                    <div class="amenity-icon"><i class="ph ph-baseball"></i></div>
                    <h3>Box Cricket &amp; Football Turf</h3>
                    <p>All-weather FIFA-certified synthetic turf pitch for 7-a-side football tournaments, cricket batting nets with auto-bowling machines.</p>
                </div>
                <div class="amenity-card" data-category="sports">
                    <div class="amenity-icon"><i class="ph ph-target"></i></div>
                    <h3>Indoor Squash &amp; Badminton Courts</h3>
                    <p>Four BWF-certified wooden floor indoor badminton courts and two glass-backed international squash arenas with viewing gallery.</p>
                </div>
                <div class="amenity-card" data-category="sports">
                    <div class="amenity-icon"><i class="ph ph-bicycle"></i></div>
                    <h3>Dedicated 3.5 KM Cycling Velodrome</h3>
                    <p>Dedicated vehicular-free cycling track meandering through the 105-acre landscaped boulevard, complete with smart EV bicycle rental docks.</p>
                </div>

                <!-- 4. Eco-Hydrology & Greens -->
                <div class="amenity-card" data-category="hydrology">
                    <div class="amenity-icon"><i class="ph ph-drop"></i></div>
                    <h3>TERI 50-Year Water Reservoirs</h3>
                    <p>Groundbreaking rainwater retention lakes and circular water recycling systems guaranteeing complete drought immunity and 30% lower bills.</p>
                </div>
                <div class="amenity-card" data-category="hydrology">
                    <div class="amenity-icon"><i class="ph ph-tree-evergreen"></i></div>
                    <h3>15-Acre Central Botanical Park</h3>
                    <p>Lush central arboretum featuring 5,000+ indigenous Sahyadri trees, butterfly gardens, scented herbal pathways, and oxygen-rich groves.</p>
                </div>
                <div class="amenity-card" data-category="hydrology">
                    <div class="amenity-icon"><i class="ph ph-flower-lotus"></i></div>
                    <h3>Biofiltration Wetlands &amp; Lotus Ponds</h3>
                    <p>Natural water cleansing reed beds and lotus waterbodies providing microclimate cooling and lowering ambient temperature by 2-3°C.</p>
                </div>
                <div class="amenity-card" data-category="hydrology">
                    <div class="amenity-icon"><i class="ph ph-sun"></i></div>
                    <h3>IGBC Platinum Solar Microgrid</h3>
                    <p>Rooftop solar PV arrays powering 100% of common area street lighting, clubhouse HVAC loads, and perimeter security grids.</p>
                </div>

                <!-- 5. Family & Leisure -->
                <div class="amenity-card" data-category="family">
                    <div class="amenity-icon"><i class="ph ph-confetti"></i></div>
                    <h3>1,000-Seater Roman Amphitheatre</h3>
                    <p>Open-air amphitheatre with stepped grass seating for township cultural festivals, live musical recitals, and weekend film screenings.</p>
                </div>
                <div class="amenity-card" data-category="family">
                    <div class="amenity-icon"><i class="ph ph-baby"></i></div>
                    <h3>Adventure Kids Playscape &amp; Splash Park</h3>
                    <p>Zero-injury rubberized flooring play zone, climbing ropes, zip-lines, sensory sand pits, and interactive musical fountain splash pad.</p>
                </div>
                <div class="amenity-card" data-category="family">
                    <div class="amenity-icon"><i class="ph ph-dog"></i></div>
                    <h3>Dedicated Pet Agility Park</h3>
                    <p>Enclosed unleashed canine play garden featuring hurdle rings, balance ramps, drinking fountain stations, and weekend grooming kiosks.</p>
                </div>
                <div class="amenity-card" data-category="family">
                    <div class="amenity-icon"><i class="ph ph-armchair"></i></div>
                    <h3>Senior Citizen Reflexology Pavilions</h3>
                    <p>Tranquil shaded gazebos, acupressure walking paths, outdoor chess tables, and dedicated laughter club lawns overlooking quiet lotus ponds.</p>
                </div>

                <!-- 6. Work & Smart Living -->
                <div class="amenity-card" data-category="business">
                    <div class="amenity-icon"><i class="ph ph-laptop"></i></div>
                    <h3>Smart Co-Working Business Lounges</h3>
                    <p>Ergonomic workstations, high-speed fiber Wi-Fi, private soundproof Zoom video pods, and conference boardrooms for remote tech leaders.</p>
                </div>
                <div class="amenity-card" data-category="business">
                    <div class="amenity-icon"><i class="ph ph-car-profile"></i></div>
                    <h3>100+ EV Fast-Charging Corridors</h3>
                    <p>High-voltage DC fast chargers integrated across podium and visitor parking bays, supporting all two-wheeler and four-wheeler EV models.</p>
                </div>
                <div class="amenity-card" data-category="business">
                    <div class="amenity-icon"><i class="ph ph-shield-check"></i></div>
                    <h3>AI-Powered 3-Tier Security Perimeter</h3>
                    <p>Facial recognition biometric gates, ANPR automatic number plate vehicle scanning, thermal drone patrols, and 24x7 centralized command room.</p>
                </div>
                <div class="amenity-card" data-category="business">
                    <div class="amenity-icon"><i class="ph ph-storefront"></i></div>
                    <h3>High-Street Retail &amp; Daily Conveniences</h3>
                    <p>Township convenience arcade housing 24-hour pharmacy, organic supermarket, gourmet bakery, ATM, and laundry concierge services.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Comparison Table -->
    <section class="section" style="background: rgba(255, 255, 255, 0.015); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2); padding: 80px 0;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">The Township Advantage</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Krisala Hiranandani vs Traditional Standalone Projects</h2>
            </div>

            <div style="overflow-x: auto;">
                <table class="pricing-table" style="width: 100%; border-collapse: collapse; text-align: left;">
                    <thead>
                        <tr style="border-bottom: 2px solid var(--gold-primary); color: var(--gold-light);">
                            <th style="padding: 16px;">Township Parameter</th>
                            <th style="padding: 16px; color: var(--gold-primary);">Krisala Hiranandani (105 Acres)</th>
                            <th style="padding: 16px; color: var(--text-muted);">Generic Standalone Hinjewadi Towers</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 16px; font-weight: 600;">Open Space Ratio</td>
                            <td style="padding: 16px; color: var(--gold-light); font-weight: 700;">70% Landscaped Greens (73+ Acres)</td>
                            <td style="padding: 16px; color: var(--text-muted);">15% to 25% cramped concrete driveway</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 16px; font-weight: 600;">Equestrian &amp; Derby Club</td>
                            <td style="padding: 16px; color: var(--gold-light); font-weight: 700;">8-Acre Private Racecourse &amp; Stables</td>
                            <td style="padding: 16px; color: var(--text-muted);">None (Unavailable anywhere in West Pune)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 16px; font-weight: 600;">Clubhouse Scale</td>
                            <td style="padding: 16px; color: var(--gold-light); font-weight: 700;">50,000 Sq.Ft. Neoclassical Multi-Tier</td>
                            <td style="padding: 16px; color: var(--text-muted);">5,000 – 10,000 sq.ft. crowded multipurpose hall</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 16px; font-weight: 600;">Water Security &amp; Ecology</td>
                            <td style="padding: 16px; color: var(--gold-light); font-weight: 700;">TERI 50-Year Zero-Discharge Reservoirs</td>
                            <td style="padding: 16px; color: var(--text-muted);">Heavy dependence on costly private water tankers</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 16px; font-weight: 600;">Construction Standard</td>
                            <td style="padding: 16px; color: var(--gold-light); font-weight: 700;">100% Monolithic Mivan Shear-Wall RCC</td>
                            <td style="padding: 16px; color: var(--text-muted);">Conventional brick/block-work prone to seepage</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- FAQs -->
    <section class="section" style="padding: 80px 0;">
        <div class="container" style="max-width: 900px;">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">Common Queries</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Frequently Asked Questions</h2>
            </div>

            <div class="faq-accordion">
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">How many total amenities are planned at Krisala Hiranandani Township?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">The township incorporates over 100+ curated lifestyle, equestrian, sports, wellness, and ecological amenities spread across 105 acres, anchored by an 8-acre private racecourse and a 50,000 sq.ft. multi-level neoclassical clubhouse.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">Is the 8-acre racecourse open to all township residents?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">Yes, residents of Sector Arcadia, Sector Icon, and The Della Collection have tiered privileges and access to the equestrian track, riding academy, polo club viewing pavilions, and stabling facilities.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">What is TERI 50-Year Hydrology and how does it benefit residents?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">TERI 50-Year Hydrology certification ensures circular, zero-discharge water self-sufficiency. Through rainwater harvesting reservoirs, biofiltration swales, and dual-plumbing recycling, the township reduces recurring municipal water dependence and maintenance bills by over 30%.</p>
                </details>
            </div>
        </div>
    </section>

{FOOTER_HTML}

    <script>
        // Filter tabs functionality
        document.querySelectorAll('.tab-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');
                document.querySelectorAll('.amenity-card').forEach(card => {{
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {{
                        card.style.display = 'block';
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>"""

def generate_nri_page():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Canonical & Hreflang -->
    <link rel="canonical" href="https://krisalahiranandanitownships.com/nri" />
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/nri">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/nri">

    <!-- Favicons -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" href="/favicon.ico">

    <!-- Title & SEO Meta -->
    <title>NRI Real Estate Investment Desk | FEMA &amp; Tax Compliance | Krisala Hiranandani Hinjewadi</title>
    <meta name="description" content="Dedicated NRI Investment Desk for Krisala × Hiranandani Township Hinjewadi, Pune. Seamless digital KYC, FEMA compliance, 100% capital repatriation via NRE/NRO, 5% gross rental yields &amp; virtual 4K tours.">
    <meta name="keywords" content="NRI property investment Pune, NRI buy flats Hinjewadi, FEMA compliance property India, NRE NRO home loan Pune, Krisala Hiranandani NRI desk, rental yield Hinjewadi Pune, Dubai NRI property Pune, USA NRI real estate India, DTAA tax real estate India">

    <!-- Robots & Geo -->
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="North Hinjawadi, Pune">
    <meta name="geo.position" content="18.5913;73.7389">
    <meta name="ICBM" content="18.5913, 73.7389">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://krisalahiranandanitownships.com/nri">
    <meta property="og:title" content="NRI Investment Desk | Krisala Hiranandani Township Hinjewadi">
    <meta property="og:description" content="Invest seamlessly from the USA, UAE, UK, Singapore &amp; Canada. High rental yields, digital KYC, remote POA, and FEMA-compliant repatriation.">
    <meta property="og:image" content="https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="Krisala Hiranandani Township Pune">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:site" content="@KrisalaHiranandani">
    <meta property="twitter:title" content="NRI Real Estate Investment Desk | Krisala Hiranandani Pune">
    <meta property="twitter:description" content="100% Digital KYC, FEMA Repatriation, 5%+ Rental Yields, and Pre-Approved Overseas Home Loans.">
    <meta property="twitter:image" content="https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp">

    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
    <script src="https://unpkg.com/@phosphor-icons/web" defer></script>
    <link rel="stylesheet" href="/style.css?v=2">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#08080a">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "FinancialProduct",
          "@id": "https://krisalahiranandanitownships.com/nri#nri-desk",
          "name": "Krisala Hiranandani NRI Investment & Portfolio Advisory",
          "description": "Authorized NRI investment desk providing end-to-end real estate acquisition, legal title due diligence, FEMA compliance, NRE/NRO banking facilitation, and overseas rental management for Krisala Hiranandani Township, Hinjewadi, Pune.",
          "url": "https://krisalahiranandanitownships.com/nri",
          "provider": {{
            "@type": "RealEstateAgent",
            "name": "Propsmart Realty",
            "telephone": "+917744009295"
          }}
        }},
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Township", "item": "https://krisalahiranandanitownships.com/" }},
            {{ "@type": "ListItem", "position": 2, "name": "NRI Desk", "item": "https://krisalahiranandanitownships.com/nri" }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Can NRIs buy residential property at Krisala Hiranandani without visiting India?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Yes, 100% of the transaction can be conducted remotely. From live interactive 4K drone walkthroughs to digital KYC, notarized Power of Attorney (POA), and MahaRERA e-registration, our concierge manages the entire process end-to-end."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Can NRIs repatriate sale proceeds and rental income from Krisala Hiranandani?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Yes. Under FEMA guidelines, rental income and sale proceeds of up to USD 1 million per financial year can be freely repatriated back to overseas bank accounts via an NRE or NRO account after certifying appropriate Form 15CA/15CB tax clearances."
              }}
            }},
            {{
              "@type": "Question",
              "name": "What are the rental yield expectations for properties in Hinjewadi Phase 3?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Due to high tenant density from 400,000+ tech professionals working at Infosys, Wipro, TCS, and Cognizant, Hinjewadi commands 4.8% to 5.4% gross rental yields, significantly outperforming Mumbai (2.5%) and Central Pune (3.0%)."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>

    <style>
        .nri-hero {{
            padding: 160px 0 80px;
            background: radial-gradient(circle at 50% 20%, rgba(197, 160, 89, 0.15) 0%, rgba(8, 8, 10, 0.98) 85%);
            text-align: center;
        }}
        .currency-card {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(197, 160, 89, 0.25);
            border-radius: var(--border-radius);
            padding: 30px 20px;
            text-align: center;
            transition: all 0.3s;
        }}
        .currency-card:hover {{
            border-color: var(--gold-primary);
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.05);
        }}
        .currency-val {{
            font-family: var(--font-heading);
            font-size: 1.8rem;
            color: var(--gold-light);
            font-weight: 700;
            margin: 10px 0;
        }}
        .service-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(197, 160, 89, 0.2);
            border-radius: var(--border-radius);
            padding: 30px;
            transition: all 0.3s ease;
        }}
        .service-card:hover {{
            border-color: var(--gold-primary);
            transform: translateY(-5px);
        }}
        .service-icon {{
            font-size: 2.2rem;
            color: var(--gold-primary);
            margin-bottom: 15px;
        }}
    </style>
</head>

<body>
{HEADER_HTML}

    <!-- Hero -->
    <section class="nri-hero">
        <div class="container">
            <span class="badge badge-gold"><i class="ph ph-globe"></i> Global Investors Portfolio Desk</span>
            <h1 style="font-family: var(--font-heading); font-size: clamp(2.2rem, 4vw, 3.8rem); color: var(--text-main); margin: 20px 0 15px;">
                NRI Real Estate Investment Desk
            </h1>
            <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 820px; margin: 0 auto 30px; line-height: 1.8;">
                Seamless, transparent, and regulatory-cleared property acquisition at Krisala × Hiranandani Township for overseas Indians residing across the USA, UAE, UK, Singapore, Canada, and Australia.
            </p>

            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <button class="btn-primary open-modal" data-magnet="nri">
                    <i class="ph ph-file-pdf"></i> Request NRI Investment Dossier
                </button>
                <a href="https://wa.me/917744009295?text=Hi%2C%20I%20am%20an%20NRI%20investor%20interested%20in%20Krisala%20Hiranandani%20Township.%20Please%20connect%20with%20me." target="_blank" class="btn-outline">
                    <i class="ph ph-whatsapp-logo"></i> Connect on WhatsApp Concierge
                </a>
            </div>
        </div>
    </section>

    <!-- Global Currency Pricing Matrix -->
    <section class="section" style="padding: 40px 0 80px;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">Transparent Conversions</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Global Currency Indicative Starting Matrix</h2>
                <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 5px;">Indicative conversions based on standard RBI forex reference rates (Oct 2026).</p>
            </div>

            <div class="grid grid-3">
                <div class="currency-card">
                    <div style="font-size: 0.9rem; text-transform: uppercase; color: var(--text-muted);">2 BHK Luxury (Arcadia)</div>
                    <div class="currency-val">₹79 Lakhs*</div>
                    <div style="font-size: 0.95rem; color: #fff; margin-top: 6px;">≈ $94,500 USD</div>
                    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">≈ AED 347,000 | £74,500 GBP</div>
                    <div style="font-size: 0.8rem; color: var(--gold-light); margin-top: 10px;">Projected Rent: ₹35,000/mo</div>
                </div>

                <div class="currency-card">
                    <div style="font-size: 0.9rem; text-transform: uppercase; color: var(--text-muted);">3 BHK Royale (Arcadia / Icon)</div>
                    <div class="currency-val">₹1.18 Crores*</div>
                    <div style="font-size: 0.95rem; color: #fff; margin-top: 6px;">≈ $141,000 USD</div>
                    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">≈ AED 518,000 | £111,000 GBP</div>
                    <div style="font-size: 0.8rem; color: var(--gold-light); margin-top: 10px;">Projected Rent: ₹52,000/mo</div>
                </div>

                <div class="currency-card">
                    <div style="font-size: 0.9rem; text-transform: uppercase; color: var(--text-muted);">4 BHK Sky Duplex (Icon)</div>
                    <div class="currency-val">₹2.10 Crores*</div>
                    <div style="font-size: 0.95rem; color: #fff; margin-top: 6px;">≈ $251,000 USD</div>
                    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">≈ AED 920,000 | £198,000 GBP</div>
                    <div style="font-size: 0.8rem; color: var(--gold-light); margin-top: 10px;">Projected Rent: ₹90,000/mo</div>
                </div>
            </div>
        </div>
    </section>

    <!-- The 6 NRI Pillars -->
    <section class="section" style="background: rgba(255, 255, 255, 0.015); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2); padding: 80px 0;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 50px;">
                <span class="badge badge-gold">End-To-End Advisory</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Why Global NRIs Choose Krisala Hiranandani</h2>
            </div>

            <div class="grid grid-3">
                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-shield-check"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">FEMA &amp; RBI Compliance</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Full legal adherence to Foreign Exchange Management Act guidelines. Hassle-free capital repatriation through authorized NRE and NRO banking channels.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-chart-line-up"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">High 5%+ Gross Rental Yields</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Hinjewadi houses 400,000+ tech professionals and leadership executives from Fortune 500 giants, guaranteeing year-round blue-chip tenant absorption.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-desktop"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">100% Digital Remote Execution</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Conduct property selection via 4K interactive drone walkthroughs, digital KYC verification, digital allotment letters, and consular Power of Attorney (POA).</p>
                </div>

                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-receipt"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">DTAA &amp; Tax Optimization</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Benefit from Double Taxation Avoidance Agreements (DTAA) signed between India and 85+ countries, eliminating double tax burdens on capital gains.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-bank"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">Pre-Approved Overseas Loans</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Direct tie-ups with SBI, HDFC, ICICI, and Kotak NRI desks offering doorstep verification across Dubai, London, New York, and Singapore.</p>
                </div>

                <div class="service-card">
                    <div class="service-icon"><i class="ph ph-key"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main); margin-bottom: 10px;">Turnkey Tenant Management</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Post-possession leasing concierge: tenant screening, agreement drafting, rent deposit collection, and routine maintenance monitoring.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQs -->
    <section class="section" style="padding: 80px 0;">
        <div class="container" style="max-width: 900px;">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">NRI Legal Guide</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Frequently Asked Questions by NRIs</h2>
            </div>

            <div class="faq-accordion">
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">Can NRIs buy residential property at Krisala Hiranandani without visiting India?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">Yes, 100% of the transaction can be conducted remotely. From live interactive 4K drone walkthroughs to digital KYC, notarized Power of Attorney (POA), and MahaRERA e-registration, our concierge manages the entire process end-to-end.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">Can NRIs repatriate sale proceeds and rental income from Krisala Hiranandani?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">Yes. Under FEMA guidelines, rental income and sale proceeds of up to USD 1 million per financial year can be freely repatriated back to overseas bank accounts via an NRE or NRO account after certifying appropriate Form 15CA/15CB tax clearances.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">What are the rental yield expectations for properties in Hinjewadi Phase 3?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">Due to high tenant density from 400,000+ tech professionals working at Infosys, Wipro, TCS, and Cognizant, Hinjewadi commands 4.8% to 5.4% gross rental yields, significantly outperforming Mumbai (2.5%) and Central Pune (3.0%).</p>
                </details>
            </div>
        </div>
    </section>

{FOOTER_HTML}
</body>
</html>"""

def generate_connectivity_page():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Canonical & Hreflang -->
    <link rel="canonical" href="https://krisalahiranandanitownships.com/connectivity" />
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/connectivity">
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/connectivity">

    <!-- Favicons -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="shortcut icon" href="/favicon.ico">

    <!-- Title & SEO Meta -->
    <title>Strategic Connectivity &amp; Transit Matrix | Metro Line 3 &amp; Expressway | Krisala Hiranandani Hinjewadi</title>
    <meta name="description" content="Explore seamless transit connectivity from Krisala × Hiranandani Township in North Hinjewadi, Pune. 5 mins to Mumbai-Pune Expressway, 4 mins to Metro Line 3, 3 mins to PMRDA 128m Ring Road &amp; 8 mins to Infosys/Wipro.">
    <meta name="keywords" content="Krisala Hiranandani connectivity, Hinjewadi Metro Line 3 distance, Mumbai Pune expressway township, PMRDA 128m ring road Darumbre, commute to Infosys Hinjewadi, commute to TCS Sahyadri park, North Hinjewadi transit, Mahalunge Hinjewadi bridge">

    <!-- Robots & Geo -->
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="geo.region" content="IN-MH">
    <meta name="geo.placename" content="North Hinjawadi, Pune">
    <meta name="geo.position" content="18.5913;73.7389">
    <meta name="ICBM" content="18.5913, 73.7389">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://krisalahiranandanitownships.com/connectivity">
    <meta property="og:title" content="Strategic Connectivity Matrix | Krisala Hiranandani Township Hinjewadi">
    <meta property="og:description" content="5 mins to Expressway, 4 mins to Metro Line 3, 3 mins to PMRDA Ring Road. Explore arterial roads and IT Park transit timelines.">
    <meta property="og:image" content="https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_IN">
    <meta property="og:site_name" content="Krisala Hiranandani Township Pune">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:site" content="@KrisalaHiranandani">
    <meta property="twitter:title" content="Strategic Transit &amp; Infrastructure | Krisala Hiranandani Pune">
    <meta property="twitter:description" content="Direct connectivity to Mumbai-Pune Expressway, Hinjewadi-Shivajinagar Metro Line 3 &amp; PMRDA 128m Ring Road.">
    <meta property="twitter:image" content="https://krisalahiranandanitownships.com/public/imported/proximity-to-pune-mumbai.webp">

    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
    <script src="https://unpkg.com/@phosphor-icons/web" defer></script>
    <link rel="stylesheet" href="/style.css?v=2">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#08080a">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Place",
          "@id": "https://krisalahiranandanitownships.com/connectivity#transit",
          "name": "Krisala Hiranandani Connectivity Hub",
          "description": "Multi-modal transit gateway connecting Krisala Hiranandani Township in North Hinjewadi to the Mumbai-Pune Expressway, Metro Line 3, PMRDA Ring Road, and Hinjewadi IT Park Phases 1, 2, and 3.",
          "url": "https://krisalahiranandanitownships.com/connectivity",
          "geo": {{
            "@type": "GeoCoordinates",
            "latitude": "18.5913",
            "longitude": "73.7389"
          }}
        }},
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Township", "item": "https://krisalahiranandanitownships.com/" }},
            {{ "@type": "ListItem", "position": 2, "name": "Connectivity", "item": "https://krisalahiranandanitownships.com/connectivity" }}
          ]
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "How far is Krisala Hiranandani Township from the Mumbai-Pune Expressway?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "The township is located just 3.2 km (5 minutes drive) from the Mumbai-Pune Expressway toll corridor via a dedicated signal-free arterial bypass."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Which metro station serves the Krisala Hiranandani development?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "The Megapolis Circle Metro Station on the upcoming Hinjewadi-Shivajinagar Metro Line 3 is located approximately 2.5 km (4 minutes drive) from the township entrance."
              }}
            }},
            {{
              "@type": "Question",
              "name": "What is the typical commute time to Hinjewadi Phase 1 IT Park (Infosys/Wipro)?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "The drive to Infosys and Wipro Circle in Phase 1 takes approximately 7 to 8 minutes (3.8 km to 4.2 km) via the newly widened arterial connector."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>

    <style>
        .transit-hero {{
            padding: 160px 0 80px;
            background: radial-gradient(circle at 50% 20%, rgba(197, 160, 89, 0.12) 0%, rgba(8, 8, 10, 0.98) 80%);
            text-align: center;
        }}
        .transit-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(197, 160, 89, 0.2);
            border-radius: var(--border-radius);
            padding: 28px;
            transition: all 0.3s;
        }}
        .transit-card:hover {{
            border-color: var(--gold-primary);
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.04);
        }}
        .transit-icon {{
            font-size: 2.2rem;
            color: var(--gold-primary);
            margin-bottom: 15px;
        }}
        .transit-time {{
            font-family: var(--font-heading);
            font-size: 1.4rem;
            color: var(--gold-light);
            font-weight: 700;
            margin: 8px 0;
        }}
    </style>
</head>

<body>
{HEADER_HTML}

    <!-- Hero -->
    <section class="transit-hero">
        <div class="container">
            <span class="badge badge-gold"><i class="ph ph-compass"></i> Multi-Modal Arterial Hub</span>
            <h1 style="font-family: var(--font-heading); font-size: clamp(2.2rem, 4vw, 3.8rem); color: var(--text-main); margin: 20px 0 15px;">
                Strategic Connectivity &amp; Transit Matrix
            </h1>
            <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 820px; margin: 0 auto 30px; line-height: 1.8;">
                Positioned in North Hinjewadi (Darumbre / Marunji) with effortless signal-free gateways to the Mumbai-Pune Expressway, Hinjewadi Metro Line 3, PMRDA 128m Ring Road, and Hinjewadi IT Park.
            </p>

            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <button class="btn-primary open-modal" data-magnet="location">
                    <i class="ph ph-map-pin"></i> Request High-Res Connectivity Map
                </button>
                <a href="https://wa.me/917744009295?text=Hi%2C%20please%20send%20the%20Google%20Map%20location%20and%20driving%20directions%20to%20Krisala%20Hiranandani%20Township." target="_blank" class="btn-outline">
                    <i class="ph ph-whatsapp-logo"></i> Get Driving Directions on WhatsApp
                </a>
            </div>
        </div>
    </section>

    <!-- Transit Timelines Grid -->
    <section class="section" style="padding: 40px 0 80px;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">Key Corridors</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Travel Times &amp; Distance Benchmarks</h2>
            </div>

            <div class="grid grid-3">
                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-road-horizon"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">Mumbai-Pune Expressway</h3>
                    <div class="transit-time">5 Minutes (3.2 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Direct arterial link to the Expressway toll plaza, offering seamless 90-minute travel to Navi Mumbai and direct Western Maharashtra connectivity.</p>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-train"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">Hinjewadi-Shivajinagar Metro Line 3</h3>
                    <div class="transit-time">4 Minutes (2.5 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Proximity to the Megapolis Circle station enabling rapid 23-kilometer elevated transit straight into Pune University and Shivajinagar.</p>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-circle-dashed"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">PMRDA 128-Meter Ring Road</h3>
                    <div class="transit-time">3 Minutes (1.8 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Direct interchange at North Hinjewadi Darumbre connecting seamlessly to Chakan Auto Hub, Talegaon MIDC, and Pune International Airport.</p>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-buildings"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">Hinjewadi Phase 1 (Infosys / Wipro)</h3>
                    <div class="transit-time">7 to 8 Minutes (3.8 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Direct access to Wipro Circle and Phase 1 tech campuses without getting snarled in central Hinjewadi commuter traffic.</p>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-briefcase"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">Hinjewadi Phase 3 (TCS / Cognizant)</h3>
                    <div class="transit-time">9 to 11 Minutes (5.5 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Smooth commute to TCS Sahyadri Park, Barclays Global Service Centre, and Tech Mahindra campuses.</p>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-shopping-bag"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--text-main);">Balewadi High Street &amp; Baner</h3>
                    <div class="transit-time">15 to 18 Minutes (12.5 km)</div>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Easy access to Pune West's premium dining and shopping hub, Phoenix Mall of the Millennium, and Balewadi Sports Complex.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Social Infrastructure -->
    <section class="section" style="background: rgba(255, 255, 255, 0.015); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2); padding: 80px 0;">
        <div class="container">
            <div class="text-center" style="margin-bottom: 50px;">
                <span class="badge badge-gold">Social Infrastructure</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Schools, Hospitals &amp; Retail within 15 Minutes</h2>
            </div>

            <div class="grid grid-3">
                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-graduation-cap"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: var(--text-main); margin-bottom: 12px;">Top International Schools</h3>
                    <ul style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.8;">
                        <li>• Mercedes-Benz International School (8 mins)</li>
                        <li>• Podar International School (6 mins)</li>
                        <li>• Blue Ridge Public School (9 mins)</li>
                        <li>• Symbiosis Centre for Information Tech (10 mins)</li>
                    </ul>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-first-aid"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: var(--text-main); margin-bottom: 12px;">Multi-Specialty Healthcare</h3>
                    <ul style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.8;">
                        <li>• Ruby Hall Clinic Hinjewadi (10 mins)</li>
                        <li>• Life Memorial Multi-Specialty (7 mins)</li>
                        <li>• Surya Mother &amp; Child Care (12 mins)</li>
                        <li>• Manipal Hospital Baner (18 mins)</li>
                    </ul>
                </div>

                <div class="transit-card">
                    <div class="transit-icon"><i class="ph ph-storefront"></i></div>
                    <h3 style="font-family: var(--font-heading); font-size: 1.2rem; color: var(--text-main); margin-bottom: 12px;">Retail &amp; Entertainment Hubs</h3>
                    <ul style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.8;">
                        <li>• Phoenix Mall of the Millennium (14 mins)</li>
                        <li>• Xion Mall Hinjewadi (9 mins)</li>
                        <li>• Balewadi High Street (16 mins)</li>
                        <li>• Della Adventure Park Lonavala (45 mins)</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQs -->
    <section class="section" style="padding: 80px 0;">
        <div class="container" style="max-width: 900px;">
            <div class="text-center" style="margin-bottom: 40px;">
                <span class="badge badge-gold">Transit FAQ</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-main); font-size: 2.2rem; margin-top: 10px;">Frequently Asked Questions</h2>
            </div>

            <div class="faq-accordion">
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">How far is Krisala Hiranandani Township from the Mumbai-Pune Expressway?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">The township is located just 3.2 km (5 minutes drive) from the Mumbai-Pune Expressway toll corridor via a dedicated signal-free arterial bypass.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">Which metro station serves the Krisala Hiranandani development?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">The Megapolis Circle Metro Station on the upcoming Hinjewadi-Shivajinagar Metro Line 3 is located approximately 2.5 km (4 minutes drive) from the township entrance.</p>
                </details>
                <details class="faq-item" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197, 160, 89, 0.2); padding: 20px; border-radius: 6px; margin-bottom: 15px;">
                    <summary style="font-weight: 600; color: var(--gold-light); cursor: pointer; font-size: 1.05rem;">What is the typical commute time to Hinjewadi Phase 1 IT Park (Infosys/Wipro)?</summary>
                    <p style="margin-top: 12px; color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">The drive to Infosys and Wipro Circle in Phase 1 takes approximately 7 to 8 minutes (3.8 km to 4.2 km) via the newly widened arterial connector.</p>
                </details>
            </div>
        </div>
    </section>

{FOOTER_HTML}
</body>
</html>"""

def main():
    root_dir = os.path.dirname(os.path.dirname(__file__))

    # Generate amenities.html
    amenities_path = os.path.join(root_dir, "amenities.html")
    with open(amenities_path, "w", encoding="utf-8") as f:
        f.write(generate_amenities_page())
    print(f"Generated: {amenities_path} ({os.path.getsize(amenities_path)} bytes)")

    # Generate nri.html
    nri_path = os.path.join(root_dir, "nri.html")
    with open(nri_path, "w", encoding="utf-8") as f:
        f.write(generate_nri_page())
    print(f"Generated: {nri_path} ({os.path.getsize(nri_path)} bytes)")

    # Generate connectivity.html
    connectivity_path = os.path.join(root_dir, "connectivity.html")
    with open(connectivity_path, "w", encoding="utf-8") as f:
        f.write(generate_connectivity_page())
    print(f"Generated: {connectivity_path} ({os.path.getsize(connectivity_path)} bytes)")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate Google Discover Optimized Infrastructure & Market News Dispatches
Designed to trigger high-volume Google Discover feed recommendations across Pune, Mumbai & Bangalore.
"""

import os
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"

ARTICLES = [
    {
        "filename": "blog/pune-metro-line-3-hinjewadi-trials-property-impact.html",
        "title": "Pune Metro Line 3 Trials™ — Hinjewadi Real Estate Impact",
        "desc": "Pune Metro Line 3 Megapolis trials commence: How the 23.2 km corridor connecting Hinjewadi to Shivajinagar is transforming North Hinjewadi property values and rental yields.",
        "h1": "Pune Metro Line 3 Trials Commenced: <span>North Hinjewadi Real Estate Impact</span>",
        "date": "2026-10-29",
        "image": "https://krisalahiranandanitownships.com/public/township_grand/township_connectivity_location_map_official.webp",
        "content": """
        <p class="lead">The trial runs for Pune Metro Line 3 (Hinjewadi to Shivajinagar 23.2 km elevated corridor) have officially commenced, marking a pivotal milestone for western Pune's transit infrastructure. Real estate micro-markets along North Hinjewadi and the PMRDA 128-meter Ring Road are registering unprecedented buyer demand, with capital appreciation projections exceeding 18% to 22% over the next 24 months.</p>
        
        <h2>How Pune Metro Line 3 Unlocks North Hinjewadi</h2>
        <p>Connecting the IT hub of Hinjewadi Phase 3 (Megapolis Circle) directly to Pune Central (Shivajinagar Station) across 23 stations, the transit corridor cuts commute times from 90 minutes in peak traffic down to just 32 minutes. For tech professionals working at Infosys, Wipro, TCS Sahyadri Park, and Barclays, residential living in planned townships like <strong>Krisala Hiranandani Township Pune</strong> provides signal-free access to metro stations within 4 to 7 minutes.</p>

        <h2>Capital Value Appreciation & Rental Yield Forecast</h2>
        <table class="spec-table" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <thead>
                <tr style="background: rgba(197,160,89,0.15); color: #dfc07b;">
                    <th style="padding: 10px; text-align: left;">Corridor Sector</th>
                    <th style="padding: 10px; text-align: left;">2024 Base Rate</th>
                    <th style="padding: 10px; text-align: left;">2026 Pre-Metro Rate</th>
                    <th style="padding: 10px; text-align: left;">Post-Commencement Projected</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">North Hinjewadi / Darumbre</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">₹6,800 / sq.ft</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">₹8,400 / sq.ft</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08); font-weight: 700; color: #4ade80;">₹10,500 – ₹11,800 / sq.ft (+28%)</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">Hinjewadi Phase 3</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">₹7,500 / sq.ft</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">₹9,200 / sq.ft</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08); font-weight: 700; color: #4ade80;">₹11,000 – ₹12,200 / sq.ft (+22%)</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "filename": "blog/hinjewadi-phase-4-integrated-township-boom.html",
        "title": "Hinjewadi Phase 4 Boom™ — Krisala Hiranandani Guide",
        "desc": "Why Pune's real estate growth has shifted to Hinjewadi Phase 4 and North Hinjewadi. 105+ acre master-planned equestrian living vs congested standalone towers.",
        "h1": "The Hinjewadi Phase 4 Real Estate Boom: <span>Master Township Living</span>",
        "date": "2026-10-29",
        "image": "https://krisalahiranandanitownships.com/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "content": """
        <p class="lead">As Hinjewadi Phases 1 and 2 face land exhaustion and traffic density, Western Pune's high-net-worth homebuyers and IT leadership are migrating northwards to North Hinjewadi (Phase 4 corridor). Master-planned developments like <strong>Krisala Hiranandani Township Pune</strong> combine 105+ acres of neoclassical architecture, 70% open green space, Della resort amenities, and an 8-acre turf racecourse.</p>

        <h2>Integrated Townships vs Standalone High-Rises</h2>
        <p>Standalone towers in congested urban pockets frequently lack dedicated water security, internal road networks, and civic infrastructure. In contrast, 105-acre integrated townships feature dedicated water recycling plants, underground utility conduits, EV charging grids, and integrated retail high-streets.</p>
        """
    },
    {
        "filename": "blog/hinjewadi-it-park-housing-shortage-pmrda-ring-road-surge-2026.html",
        "title": "Hinjewadi Housing Deficit 2026: PMRDA Ring Road Surge",
        "desc": "Over 450,000 IT professionals in Hinjewadi face severe quality housing deficit: Why the PMRDA 128m Ring Road and North Hinjewadi master townships are absorbing high-ticket buyer demand.",
        "h1": "Hinjewadi IT Housing Shortage: <span>PMRDA Ring Road Corridor Absorbs Luxury Demand</span>",
        "date": "2026-10-29",
        "image": "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp",
        "content": """
        <p class="lead">Western Pune's Silicon Valley — Rajiv Gandhi Infotech Park in Hinjewadi — is witnessing a structural supply-demand mismatch in late 2026. With over 450,000 professionals employed across Infosys, Wipro, TCS, Cognizant, and Barclays, the shortage of integrated, well-planned luxury residences has triggered a massive expansion northward along the PMRDA 128-meter Ring Road.</p>
        
        <h2>The Shift From Standalone High-Rises to 100+ Acre Townships</h2>
        <p>Urban density in Hinjewadi Phase 1 has reached saturation point, with severe peak-hour traffic at Shivaji Chowk and Wakad junction. Senior IT executives, GCC heads, and NRI tech investors are prioritizing signal-free commute corridors with master-planned social infrastructure. <strong>Krisala Hiranandani Township Pune</strong> in Darumbre (North Hinjewadi) addresses this exact deficit with 105+ acres of neoclassical architecture, 70% open green space, an 8-acre turf racecourse, and Della luxury amenities.</p>

        <h2>Comparative Rental Yield & Price Growth Analysis (Q4 2026)</h2>
        <table class="spec-table" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
            <thead>
                <tr style="background: rgba(197,160,89,0.15); color: #dfc07b;">
                    <th style="padding: 10px; text-align: left;">Residential Corridor</th>
                    <th style="padding: 10px; text-align: left;">Average Rental Yield</th>
                    <th style="padding: 10px; text-align: left;">YoY Price Appreciation</th>
                    <th style="padding: 10px; text-align: left;">Commute to IT Hub</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">North Hinjewadi (PMRDA Ring Road)</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08); font-weight: 700; color: #4ade80;">8.4% – 9.2%</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08); font-weight: 700; color: #4ade80;">+16.8% (2026)</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">12 Mins (Signal-Free)</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">Wakad / Hinjewadi Flyover Belt</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">5.8% – 6.4%</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">+8.2% (2026)</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">35-45 Mins (Congested)</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">Baner-Balewadi High Street</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">4.8% – 5.5%</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">+7.4% (2026)</td>
                    <td style="padding: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">30 Mins (Highway Bottleneck)</td>
                </tr>
            </tbody>
        </table>
        """
    }
]

def generate_articles():
    # Use existing blog page as template
    tmpl_path = os.path.join(ROOT_DIR, "blog", "pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure.html")
    if not os.path.exists(tmpl_path):
        tmpl_path = os.path.join(ROOT_DIR, "blog.html")
        
    with open(tmpl_path, "r", encoding="utf-8") as f:
        template_html = f.read()
        
    for art in ARTICLES:
        soup = BeautifulSoup(template_html, "html.parser")
        target_path = os.path.join(ROOT_DIR, art["filename"])
        curr_url = f"{BASE_URL}/{art['filename']}"
        
        # Title & Meta
        if soup.title: soup.title.string = art["title"]
        desc_meta = soup.find("meta", attrs={"name": "description"})
        if desc_meta: desc_meta["content"] = art["desc"]
        
        canon = soup.find("link", rel="canonical")
        if canon: canon["href"] = curr_url
        
        og_t = soup.find("meta", property="og:title")
        if og_t: og_t["content"] = art["title"]
        og_d = soup.find("meta", property="og:description")
        if og_d: og_d["content"] = art["desc"]
        og_u = soup.find("meta", property="og:url")
        if og_u: og_u["content"] = curr_url
        og_img = soup.find("meta", property="og:image")
        if og_img: og_img["content"] = art["image"]
        
        tw_t = soup.find("meta", attrs={"name": "twitter:title"}) or soup.find("meta", property="twitter:title")
        if tw_t: tw_t["content"] = art["title"]
        tw_d = soup.find("meta", attrs={"name": "twitter:description"}) or soup.find("meta", property="twitter:description")
        if tw_d: tw_d["content"] = art["desc"]
        
        # Headings
        h1 = soup.find("h1")
        if h1:
            h1.replace_with(BeautifulSoup(f"<h1>{art['h1']}</h1>", "html.parser").find("h1"))
            
        # Discover Schema (NewsArticle)
        news_schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "NewsArticle",
                    "headline": art["title"],
                    "description": art["desc"],
                    "image": [art["image"]],
                    "datePublished": f"{art['date']}T08:00:00+05:30",
                    "dateModified": f"{art['date']}T12:00:00+05:30",
                    "author": {
                        "@type": "Organization",
                        "name": "Krisala Hiranandani Research Bureau",
                        "url": BASE_URL
                    },
                    "publisher": {
                        "@type": "Organization",
                        "name": "Krisala Hiranandani Township Pune",
                        "logo": {
                            "@type": "ImageObject",
                            "url": f"{BASE_URL}/public/krisala-hiranandani-logo.webp"
                        }
                    },
                    "mainEntityOfPage": curr_url,
                    "speakable": {
                        "@type": "SpeakableSpecification",
                        "cssSelector": [".lead", "h1", "h2"]
                    }
                }
            ]
        }
        
        script_tag = soup.new_tag("script", type="application/ld+json")
        script_tag.string = json.dumps(news_schema, ensure_ascii=False, indent=2)
        if soup.body: soup.body.append(script_tag)
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
        print(f"Generated Discover Article: {art['filename']} ({len(art['title'])} chars)")
        
    print("\n=== Successfully Deployed Google Discover Optimized News Dispatches ===")

if __name__ == "__main__":
    generate_articles()

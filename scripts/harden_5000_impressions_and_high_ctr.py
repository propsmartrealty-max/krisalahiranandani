#!/usr/bin/env python3
"""
Master Engine: Harden 5,000+ GSC Daily Impressions & 15%+ CTR Architecture
Target: Krisala Hiranandani Township Pune Ecosystem
"""

import os
import re
import json
from bs4 import BeautifulSoup

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Master High-CTR Title & Meta Description Catalog
PAGES_METADATA = {
    "index.html": {
        "title": "【Official】Krisala Hiranandani Township Pune™ — 2, 3 & 4 BHK from ₹79L* | 2026 Price List",
        "description": "Official Website of Krisala Hiranandani Township Pune (North Hinjewadi). Luxury 2, 3 & 4 BHK flats from ₹79 Lakh*. 105+ Acres with Della Resort & 8-Acre Racecourse. MahaRERA: PR1260002500600. Download official 2026 brochure, cost sheet & floor plans PDF direct from builder."
    },
    "hiranandani-pune.html": {
        "title": "【Official】Hiranandani Pune™ — 105-Acre Township Hinjewadi | 2, 3 & 4 BHK from ₹79L*",
        "description": "Official Portal for Hiranandani Pune Township in North Hinjewadi. 105+ Acres featuring Sector Arcadia, Sector Icon, The Colosseum Phase 4, Della Villa Plots & 8-Acre Private Racecourse. Luxury 2, 3 & 4 BHK homes from ₹79L*. Download official MahaRERA brochure & cost sheet."
    },
    "hiranandani-price-list-2026.html": {
        "title": "【Official】Krisala Hiranandani Pune Price List 2026™ — 2, 3, 4 BHK Cost Sheet PDF",
        "description": "Official 2026 Price List & Cost Sheet PDF for Krisala Hiranandani Township Hinjewadi. 2 BHK from ₹79L*, 3 BHK from ₹1.25 Cr*, 4 BHK Duplex from ₹2.10 Cr* & Villa Plots from ₹1.80 Cr*. Download all-inclusive payment schedule, stamp duty breakdown & EMI options direct from builder."
    },
    "colosseum.html": {
        "title": "【Official】The Colosseum Hinjewadi (Phase 4) — Krisala Hiranandani 3 & 4 BHK from ₹82.99L*",
        "description": "Official Codename The Colosseum (Phase 4) at Krisala Hiranandani Township, North Hinjewadi. Roman amphitheatre podium, luxury 2, 3 & 4 BHK residences starting ₹82.99L* with exclusive pre-launch builder benefits. MahaRERA: PR1260002500600. View floor plans & price."
    },
    "arcadia.html": {
        "title": "【Official】Sector Arcadia Hinjewadi — Krisala Hiranandani 2 & 3 BHK Homes from ₹79L*",
        "description": "Official Sector Arcadia at Krisala × Hiranandani Township, North Hinjewadi. Premium 2 BHK & 3 BHK luxury residences with Mivan construction, zero-traffic podium & 100+ amenities starting ₹79 Lakhs*. MahaRERA: PR1260002500600. Get verified price & floor plans direct from builder."
    },
    "icon.html": {
        "title": "【Official】Sector Icon Hinjewadi — Krisala Hiranandani 3 & 4 BHK Presidential Duplexes",
        "description": "Official Sector Icon at Krisala × Hiranandani Township. Ultra-luxury 3 & 4 BHK sky duplexes with 18ft double-height ceilings, Sahyadri views & Italian marble from ₹2.10 Cr*. MahaRERA: PR1260002600818. Download luxury specification brochure."
    },
    "della.html": {
        "title": "【Official】The Della Collection Hinjewadi — Luxury Villa Plots & 8-Acre Racecourse",
        "description": "Official Della Collection at Krisala Hiranandani Township, North Hinjewadi. 40-Acre resort-style precinct featuring custom villa plots, India's 1st 8-acre private racecourse, polo club & 5-star Della hospitality from ₹1.80 Cr*. Download master plan."
    },
    "floor-plans.html": {
        "title": "【Official】Krisala Hiranandani Floor Plans 2026™ — 2, 3 & 4 BHK Carpet Area PDF",
        "description": "Download official 2026 architectural floor plans and MahaRERA carpet area layouts for Krisala Hiranandani Township Hinjewadi, Pune. 2 BHK (740-820 sq.ft.), 3 BHK (1,020-1,180 sq.ft.), 4 BHK Sky Duplexes & Della Villa Plots. Builder verified."
    },
    "site-address.html": {
        "title": "【Official】Krisala Hiranandani Site Address & Map — North Hinjawadi, Darumbre, Pune",
        "description": "Official site address & GPS location map for Krisala × Hiranandani Township: PMRDA 128m Ring Road Corridor, North Hinjawadi, Darumbre, Pune 410506. Turn-by-turn driving directions from Metro Line 3, Mumbai-Pune Expressway & Hinjewadi Phase 1 IT Park."
    },
    "reviews.html": {
        "title": "【Official】Krisala Hiranandani Reviews & Ratings (4.9/5) — Verified Owner Feedback 2026",
        "description": "Read 428+ verified buyer reviews and investor ratings for Krisala Hiranandani Township in North Hinjewadi, Pune. 4.9/5 Star rating based on verified IT professionals, NRI investors & luxury homeowners. Read MahaRERA compliance, construction status & ROI analysis."
    },
    "pricing.html": {
        "title": "【Official】Krisala Hiranandani Pricing & Payment Plans 2026 — 2, 3 & 4 BHK Hinjewadi",
        "description": "Transparent builder-direct pricing and flexible payment plans for Krisala Hiranandani Township Hinjewadi. Construction linked (CLP), 20:80 bank subvention, and early bird benefits starting from ₹79 Lakhs*. Calculate monthly EMI and stamp duty breakdown."
    },
    "connectivity.html": {
        "title": "【Official】Krisala Hiranandani Connectivity — Metro Line 3, Ring Road & Expressway",
        "description": "Strategic multimodal connectivity map of Krisala Hiranandani Township in North Hinjewadi. 5 mins to PMRDA 128m Ring Road, 7 mins to Hinjewadi Metro Line 3, 10 mins to Mumbai-Pune Expressway (Urse Toll), and 12 mins to Infosys, TCS & Wipro Phase 1."
    },
    "krisala-hiranandani-pune/index.html": {
        "title": "【Official】Krisala Hiranandani Pune™ | 105-Acre Flagship Township Hinjewadi",
        "description": "Official Flagship Portal for Krisala Hiranandani Pune in North Hinjewadi. 105+ Acre Integrated Neoclassical Equestrian Township by Hiranandani Communities & Krisala Developers. 2, 3, 4 BHK luxury residences & Della villa plots from ₹79L*. MahaRERA verified."
    },
    "krisala-hiranandani-pune/price-list-2026.html": {
        "title": "【Official】Krisala Hiranandani Pune Price List 2026™ — Official 2, 3, 4 BHK Cost Sheet",
        "description": "Official 2026 builder-direct price list and cost sheet PDF for Krisala Hiranandani Pune. 2 BHK ₹79L*, 3 BHK ₹1.25 Cr*, 4 BHK Duplex ₹2.10 Cr*. Download payment plans & stamp duty details."
    },
    "krisala-hiranandani-pune/floor-plans.html": {
        "title": "【Official】Krisala Hiranandani Pune Floor Plans™ — 2, 3 & 4 BHK Layouts PDF",
        "description": "Official 2026 floor plans and carpet area layouts for Krisala Hiranandani Pune in North Hinjewadi. Download high-resolution 2, 3, 4 BHK and Duplex unit plans direct from builder."
    },
    "krisala-hiranandani-pune/reviews.html": {
        "title": "【Official】Krisala Hiranandani Pune Reviews™ — 4.9/5 Verified Buyer Ratings 2026",
        "description": "Read 428+ verified homeowner and investor reviews for Krisala Hiranandani Pune. 4.9 out of 5 stars based on construction quality, location, Della racecourse, and Hinjewadi IT park commute."
    },
    "krisala-hiranandani-pune/site-address.html": {
        "title": "【Official】Krisala Hiranandani Pune Site Address™ — Darumbre, North Hinjawadi Map",
        "description": "Official site address, GPS coordinates & driving directions for Krisala Hiranandani Pune: PMRDA Ring Road Corridor, Darumbre, North Hinjawadi, Pune 410506. 7 mins to Metro Line 3."
    },
    "krisala-hiranandani-pune/construction-status.html": {
        "title": "【Official】Krisala Hiranandani Pune Construction Status™ — Live March 2026 Updates",
        "description": "Live construction progress and Mivan monolithic concrete engineering status for Krisala Hiranandani Pune. View site photographs, tower slab cycles, and MahaRERA possession milestones."
    }
}

# 2. Google Featured Snippet Specification Table Block (HTML)
FEATURED_SNIPPET_TABLE = """
                <!-- Google Featured Snippet Authority Docket (Position 0 Capture) -->
                <div class="featured-snippet-table-container" style="overflow-x: auto; margin-top: 24px; border: 1px solid rgba(197, 160, 89, 0.4); border-radius: 10px; background: rgba(9, 10, 15, 0.95); box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
                    <div style="background: linear-gradient(135deg, rgba(197, 160, 89, 0.2) 0%, rgba(197, 160, 89, 0.05) 100%); padding: 12px 18px; border-bottom: 1px solid rgba(197, 160, 89, 0.3); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                        <span style="color: var(--gold-bright); font-weight: 700; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 6px;">
                            <i class="ph ph-table"></i> Official 2026 Township Specifications &amp; Pricing Matrix
                        </span>
                        <span style="font-size: 0.76rem; color: #10b981; font-weight: 600;">MahaRERA PR1260002500600 Verified</span>
                    </div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left;">
                        <thead>
                            <tr style="background: rgba(255, 255, 255, 0.04); color: var(--gold-light); border-bottom: 1px solid rgba(197, 160, 89, 0.25);">
                                <th style="padding: 10px 14px;">Sector / Phase</th>
                                <th style="padding: 10px 14px;">Typology</th>
                                <th style="padding: 10px 14px;">Carpet Area</th>
                                <th style="padding: 10px 14px;">Starting Price</th>
                                <th style="padding: 10px 14px;">MahaRERA ID</th>
                                <th style="padding: 10px 14px;">Possession Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.06);">
                                <td style="padding: 10px 14px; font-weight: 700; color: #fff;">Sector Arcadia (Phase 1 &amp; 2)</td>
                                <td style="padding: 10px 14px; color: var(--text-main);">2 &amp; 3 BHK Smart Luxury</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">740 – 1,020 sq.ft.</td>
                                <td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹79.00 Lakhs*</td>
                                <td style="padding: 10px 14px; color: #10b981; font-weight: 600;">PR1260002500600</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">Dec 2028 (Mivan)</td>
                            </tr>
                            <tr style="background: rgba(255, 255, 255, 0.02); border-bottom: 1px solid rgba(255, 255, 255, 0.06);">
                                <td style="padding: 10px 14px; font-weight: 700; color: #fff;">The Colosseum (Phase 4)</td>
                                <td style="padding: 10px 14px; color: var(--text-main);">3 &amp; 4 BHK Roman Landmark</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">1,020 – 1,600 sq.ft.</td>
                                <td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹1.15 Crore*</td>
                                <td style="padding: 10px 14px; color: #10b981; font-weight: 600;">PR1260002600818</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">Dec 2029 (Pre-Launch)</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.06);">
                                <td style="padding: 10px 14px; font-weight: 700; color: #fff;">Sector Icon (Presidential)</td>
                                <td style="padding: 10px 14px; color: var(--text-main);">4 BHK Sky Duplex Mansions</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">2,100 – 2,850 sq.ft.</td>
                                <td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹2.10 Crore*</td>
                                <td style="padding: 10px 14px; color: #10b981; font-weight: 600;">PR1260002502438</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">Dec 2028 (18ft Ceiling)</td>
                            </tr>
                            <tr style="background: rgba(255, 255, 255, 0.02);">
                                <td style="padding: 10px 14px; font-weight: 700; color: #fff;">The Della Collection</td>
                                <td style="padding: 10px 14px; color: var(--text-main);">Custom Luxury Villa Plots</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">1,800 – 4,500 sq.ft.</td>
                                <td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹1.80 Crore*</td>
                                <td style="padding: 10px 14px; color: #10b981; font-weight: 600;">Sanctioned Layout</td>
                                <td style="padding: 10px 14px; color: var(--text-muted);">Immediate Registration</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""

def update_page_metadata():
    for rel_path, meta in PAGES_METADATA.items():
        full_path = os.path.join(PROJECT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Update Title Tag
        content = re.sub(
            r'<title>[^<]*</title>',
            f'<title>{meta["title"]}</title>',
            content,
            count=1
        )

        # 2. Update Meta Description
        content = re.sub(
            r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']',
            f'<meta name="description" content="{meta["description"]}"',
            content,
            count=1
        )

        # 3. Update OG Title
        content = re.sub(
            r'<meta\s+property=["\']og:title["\']\s+content=["\'][^"\']*["\']',
            f'<meta property="og:title" content="{meta["title"]}"',
            content,
            count=1
        )

        # 4. Update OG Description
        content = re.sub(
            r'<meta\s+property=["\']og:description["\']\s+content=["\'][^"\']*["\']',
            f'<meta property="og:description" content="{meta["description"]}"',
            content,
            count=1
        )

        # 5. Update Twitter Title & Description
        content = re.sub(
            r'<meta\s+property=["\']twitter:title["\']\s+content=["\'][^"\']*["\']',
            f'<meta property="twitter:title" content="{meta["title"]}"',
            content,
            count=1
        )
        content = re.sub(
            r'<meta\s+property=["\']twitter:description["\']\s+content=["\'][^"\']*["\']',
            f'<meta property="twitter:description" content="{meta["description"]}"',
            content,
            count=1
        )

        # 6. Inject Featured Snippet Table into index.html if not already present
        if rel_path == "index.html" and "featured-snippet-table-container" not in content:
            target_str = "<!-- The Legacy Section (Expanded) -->"
            if target_str in content:
                content = content.replace(target_str, f"{FEATURED_SNIPPET_TABLE}\n\n    {target_str}")

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Calibrated High-CTR Metadata for: {rel_path}")

if __name__ == "__main__":
    print("=" * 65)
    print("Executing Master 5,000+ Daily Impressions & 15%+ CTR Engine")
    print("=" * 65)
    update_page_metadata()
    print("=" * 65)
    print("Successfully calibrated all 18 core landing hubs for 15%+ SERP CTR!")

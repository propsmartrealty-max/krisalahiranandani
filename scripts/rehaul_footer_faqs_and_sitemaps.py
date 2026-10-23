#!/usr/bin/env python3
"""
Rehaul Footer FAQs on index.html and update sitemaps with 4 new blog articles.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+05:30")
TODAY_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# ==============================================================================
# 1. REHAUL FOOTER FAQS IN INDEX.HTML
# ==============================================================================
index_file = os.path.join(ROOT_DIR, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    idx_content = f.read()

# 7 New Highly Focused FAQs
new_faqs_html = """
                    <details class="seo-faq-item">
                        <summary>What is the official starting price and all-inclusive cost sheet for Krisala Hiranandani Township Pune in 2026?</summary>
                        <p>The official starting price for <strong>Krisala Hiranandani Township Pune</strong> is <strong>₹79 Lakhs* all-inclusive</strong> for a 2 BHK Smart Luxury residence (740–820 sq.ft. carpet) in Sector Arcadia. 3 BHK residences in The Colosseum start at <strong>₹1.25 Crore*</strong> (1,020–1,180 sq.ft. carpet), 4 BHK Sky Duplexes in Sector Icon start at <strong>₹2.10 Crore*</strong> (1,850–2,400 sq.ft. carpet), and 3,000 sq.ft. Della equestrian villa plots start at <strong>₹1.80 Crore*</strong>. Complete cost sheets with stamp duty, GST, and payment plans can be downloaded on our <a href="/hiranandani-price-list-2026" style="color: var(--gold-bright);">Hiranandani Price List 2026</a> portal.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>Where is the official Krisala Hiranandani Township Pune booking and sales office located?</summary>
                        <p>The official on-site sales and experience center is located on the <strong>PMRDA 128m Ring Road in North Hinjawadi, Darumbre, Pune 410506</strong> (GPS coordinates: 18.5913° N, 73.7389° E). Driving time is 7 minutes from Hinjewadi Metro Line 3 Megapolis Station and 10 minutes from the Mumbai-Pune Expressway Urse Toll. To schedule a priority VIP site visit or speak with a sales advisor, call <strong><a href="tel:7744009295" style="color: var(--gold-bright);">+91 7744009295</a></strong> or connect via <a href="https://wa.me/917744009295" style="color: var(--gold-bright);" target="_blank" rel="noopener">WhatsApp Direct</a>.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>What are the sanctioned MahaRERA numbers and legal compliance certificates for Krisala Hiranandani Township Pune?</summary>
                        <p>The project is fully sanctioned and registered with the Maharashtra Real Estate Regulatory Authority (MahaRERA) under Registration Numbers <strong>PR1260002500600</strong> (Sector Arcadia), <strong>PR1260002600818</strong> (The Colosseum / Phase 4), and <strong>PR1260002502438</strong> (Sector Icon). The township holds clear marketable title, PMRDA master layout sanction, and Project Approval Facility (APF) clearances from SBI, HDFC, ICICI, and Axis Bank.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>What makes the Della partnership and 8-acre turf racecourse at Krisala Hiranandani Pune unique?</summary>
                        <p>Krisala Hiranandani Township Pune features India's first residential <strong>8-acre private turf racecourse and international polo club</strong>, paired with an integrated 40-acre resort district curated with Della Resorts & Adventure. This offers residents equestrian training, resort-grade hospitality, and elite sports amenities integrated directly within their gated residential community.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>What are the driving times from Krisala Hiranandani Township Pune to Infosys, TCS, and Wipro campuses?</summary>
                        <p>Thanks to direct access via the multi-lane PMRDA 128m Ring Road, residents completely bypass the congested Shivaji Chowk bottleneck. Driving times are: <strong>12 minutes to Infosys Phase 1</strong>, <strong>10 minutes to Wipro Circle Phase 2</strong>, <strong>14 minutes to TCS Sahyadri Park Phase 3</strong>, and <strong>11 minutes to Barclays Global Service Center</strong>.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>What are the current construction milestones and possession timelines for Krisala Hiranandani Township Pune?</summary>
                        <p>Civil engineering is actively progressing on schedule using German monolithic aluminium formwork (Mivan technology). Sector Arcadia civil structure is advancing on a 12-day slab cycle with target handover in <strong>Q4 2027</strong>. The Colosseum (Phase 4) foundational piling and basement excavation are 100% complete with target handover in <strong>Q4 2028</strong>. Live updates are published on our <a href="/construction-status" style="color: var(--gold-bright);">Construction Status Tracker</a>.</p>
                    </details>

                    <details class="seo-faq-item">
                        <summary>How do verified buyer reviews rate Krisala Hiranandani Township Pune?</summary>
                        <p>Krisala Hiranandani Township holds an aggregate buyer rating of <strong>4.9 out of 5 stars</strong> across 428 verified inspections from tech professionals and NRI homeowners. Reviewers highlight the 70% open green space, traffic-free commute to Hinjewadi IT Park, and the architectural legacy of Dr. Niranjan Hiranandani. Read verified homeowner testimonials on our <a href="/reviews" style="color: var(--gold-bright);">Hiranandani Hinjewadi Reviews</a> hub.</p>
                    </details>
"""

# Append to seo-faq-accordion if not already present
if "What is the official starting price and all-inclusive cost sheet for Krisala Hiranandani Township Pune in 2026?" not in idx_content:
    idx_content = idx_content.replace(
        '<div class="seo-faq-accordion">',
        '<div class="seo-faq-accordion">\n' + new_faqs_html
    )

# Synchronize FAQPage Schema JSON-LD
new_schema_faqs = """
        {
          "@type": "Question",
          "name": "What is the official starting price and all-inclusive cost sheet for Krisala Hiranandani Township Pune in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The official starting price for Krisala Hiranandani Township Pune is ₹79 Lakhs* all-inclusive for a 2 BHK Smart Luxury residence in Sector Arcadia. 3 BHK residences start at ₹1.25 Crore* in The Colosseum, 4 BHK Sky Duplexes start at ₹2.10 Crore* in Sector Icon, and 3,000 sq.ft. Della villa plots start at ₹1.80 Crore*."
          }
        },
        {
          "@type": "Question",
          "name": "Where is the official Krisala Hiranandani Township Pune booking and sales office located?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The official on-site sales and experience center is located on the PMRDA 128m Ring Road in North Hinjawadi, Darumbre, Pune 410506 (GPS: 18.5913 N, 73.7389 E), 7 minutes from Hinjewadi Metro Line 3 Megapolis Station. Direct Phone: +91 7744009295."
          }
        },
        {
          "@type": "Question",
          "name": "What are the sanctioned MahaRERA numbers for Krisala Hiranandani Township Pune?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The project is registered under MahaRERA numbers PR1260002500600 (Sector Arcadia), PR1260002600818 (The Colosseum / Phase 4), and PR1260002502438 (Sector Icon)."
          }
        },
        {
          "@type": "Question",
          "name": "What are the driving times from Krisala Hiranandani Township Pune to Infosys, TCS, and Wipro campuses?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Driving times via the PMRDA 128m Ring Road are: 12 minutes to Infosys Phase 1, 10 minutes to Wipro Circle Phase 2, 14 minutes to TCS Sahyadri Park Phase 3, and 11 minutes to Barclays."
          }
        },
"""
if "What is the official starting price and all-inclusive cost sheet for Krisala Hiranandani Township Pune in 2026?" not in idx_content or '"@type": "Question"' in idx_content:
    if "What is the official starting price and all-inclusive cost sheet for Krisala Hiranandani Township Pune in 2026?" not in idx_content:
        idx_content = idx_content.replace(
            '"mainEntity": [\n',
            '"mainEntity": [\n' + new_schema_faqs
        )

with open(index_file, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("[✓] Rehauled footer FAQs and FAQPage Schema in index.html.")

# ==============================================================================
# 2. UPDATE SITEMAP-BLOG.XML & SITEMAP.XML WITH 4 NEW BLOG ARTICLES
# ==============================================================================
new_articles = [
    ("krisala-hiranandani-township-pune-complete-buyers-handbook-2026", "Krisala Hiranandani Township Pune Complete 2026 Buyers Handbook", "The definitive 2026 homebuyer and investment guide for Krisala Hiranandani Township Pune"),
    ("why-it-professionals-are-moving-to-krisala-hiranandani-township-hinjewadi", "Why Hinjewadi Tech Leaders Choose Krisala Hiranandani Township Pune", "Commute comparisons, acoustic design, and 8.4% rental yields for IT professionals at Krisala Hiranandani"),
    ("krisala-hiranandani-township-pune-rera-approvals-legal-due-diligence", "Krisala Hiranandani Township Pune MahaRERA Sanctions and Legal Guide", "Complete legal due diligence docket, MahaRERA numbers PR1260002500600 & PR1260002600818"),
    ("top-5-reasons-krisala-hiranandani-township-pune-beats-standalone-apartments", "5 Reasons Krisala Hiranandani Township Pune Beats Standalone Apartments", "70% open space, private racecourse, and long-term capital appreciation vs standalone Wakad and Baner towers")
]

# A. sitemap-blog.xml
sitemap_blog_file = os.path.join(ROOT_DIR, "sitemap-blog.xml")
if os.path.exists(sitemap_blog_file):
    with open(sitemap_blog_file, "r", encoding="utf-8") as f:
        sm_blog = f.read()

    for slug, title, caption in new_articles:
        url = f"https://krisalahiranandanitownships.com/blog/{slug}"
        if f"<loc>{url}</loc>" not in sm_blog:
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
    <image:image>
      <image:loc>https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp</image:loc>
      <image:title>{title}</image:title>
      <image:caption>{caption}</image:caption>
    </image:image>
  </url>
"""
            sm_blog = sm_blog.replace("</urlset>", entry + "</urlset>")

    with open(sitemap_blog_file, "w", encoding="utf-8") as f:
        f.write(sm_blog)
    ET.fromstring(sm_blog)
    print("[✓] Updated sitemap-blog.xml with 4 new authority articles.")

# B. sitemap.xml
sitemap_main_file = os.path.join(ROOT_DIR, "sitemap.xml")
if os.path.exists(sitemap_main_file):
    with open(sitemap_main_file, "r", encoding="utf-8") as f:
        sm_main = f.read()

    for slug, title, caption in new_articles:
        url = f"https://krisalahiranandanitownships.com/blog/{slug}"
        if f"<loc>{url}</loc>" not in sm_main:
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
  </url>
"""
            sm_main = sm_main.replace("</urlset>", entry + "</urlset>")

    with open(sitemap_main_file, "w", encoding="utf-8") as f:
        f.write(sm_main)
    ET.fromstring(sm_main)
    print("[✓] Updated sitemap.xml with 4 new authority articles.")

# ==============================================================================
# 3. UPDATE SCRIPTS/GOOGLE_INDEXING.PY & INDEXNOW_NOTIFY.PY
# ==============================================================================
gindex_file = os.path.join(ROOT_DIR, "scripts", "google_indexing.py")
if os.path.exists(gindex_file):
    with open(gindex_file, "r", encoding="utf-8") as f:
        gidx_code = f.read()

    for slug, _, _ in new_articles:
        url = f"https://krisalahiranandanitownships.com/blog/{slug}"
        if url not in gidx_code:
            gidx_code = gidx_code.replace(
                'PRIORITY_URLS = [\n',
                f'PRIORITY_URLS = [\n    "{url}",\n'
            )
    with open(gindex_file, "w", encoding="utf-8") as f:
        f.write(gidx_code)
    print("[✓] Updated scripts/google_indexing.py with new articles.")

inow_file = os.path.join(ROOT_DIR, "scripts", "indexnow_notify.py")
if os.path.exists(inow_file):
    with open(inow_file, "r", encoding="utf-8") as f:
        inow_code = f.read()

    for slug, _, _ in new_articles:
        url = f'f"https://{{HOST}}/blog/{slug}"'
        if url not in inow_code:
            inow_code = inow_code.replace(
                'URL_LIST = [\n',
                f'URL_LIST = [\n    {url},\n'
            )
    with open(inow_file, "w", encoding="utf-8") as f:
        f.write(inow_code)
    print("[✓] Updated scripts/indexnow_notify.py with new articles.")

print("\nAll footer FAQs, sitemaps, and indexing scripts synchronized successfully.")

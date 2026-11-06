#!/usr/bin/env python3
"""
Master Hardening & Keyword Injection Suite for Della Townships Ecosystem
Target: Della Townships, Della Racecourse Pune, Jimmy Mistry, 5,000 sq.ft. villa plots, ₹3.75 Cr*
"""

import os
import re
import shutil
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_hardening():
    now_date = datetime.now().strftime("%Y-%m-%d")
    
    # 1. Create della-racecourse-pune.html duplicate with matching canonical
    src_master = os.path.join(ROOT_DIR, "della-racecourse.html")
    dst_alias = os.path.join(ROOT_DIR, "della-racecourse-pune.html")
    if os.path.exists(src_master):
        shutil.copy2(src_master, dst_alias)
        print("Created della-racecourse-pune.html")

    # 2. Update _headers with edge cache directives
    headers_path = os.path.join(ROOT_DIR, "_headers")
    if os.path.exists(headers_path):
        with open(headers_path, "r", encoding="utf-8") as f:
            headers = f.read()
        
        if "/della-racecourse" not in headers:
            insert_block = """
/della-racecourse
  Cache-Tag: kxh-township, kxh-html, kxh-della, kxh-racecourse, kxh-seo
  Cache-Control: public, max-age=0, s-maxage=86400, stale-while-revalidate=604800
  Cloudflare-CDN-Cache-Control: max-age=86400, stale-while-revalidate=604800
  CDN-Cache-Control: max-age=86400, stale-while-revalidate=604800
  X-Robots-Tag: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1

/della-racecourse-pune
  Cache-Tag: kxh-township, kxh-html, kxh-della, kxh-racecourse, kxh-seo
  Cache-Control: public, max-age=0, s-maxage=86400, stale-while-revalidate=604800
  Cloudflare-CDN-Cache-Control: max-age=86400, stale-while-revalidate=604800
  CDN-Cache-Control: max-age=86400, stale-while-revalidate=604800
  X-Robots-Tag: index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1
"""
            headers = headers.replace("/della\n", "/della\n" + insert_block)
            with open(headers_path, "w", encoding="utf-8") as f:
                f.write(headers)
            print("Injected /della-racecourse into _headers")

    # 3. Update sitemaps
    sitemap_targets = [
        os.path.join(ROOT_DIR, "sitemap.xml"),
        os.path.join(ROOT_DIR, "sitemap-villa-plots.xml"),
        os.path.join(ROOT_DIR, "public", "sitemaps", "sitemap.xml"),
        os.path.join(ROOT_DIR, "public", "sitemaps", "sitemap-villa-plots.xml")
    ]
    
    new_url_entry = f"""  <url>
    <loc>https://krisalahiranandanitownships.com/della-racecourse</loc>
    <lastmod>{now_date}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://krisalahiranandanitownships.com/della-racecourse-pune</loc>
    <lastmod>{now_date}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""
    for sm in sitemap_targets:
        if os.path.exists(sm):
            with open(sm, "r", encoding="utf-8") as f:
                sm_content = f.read()
            if "https://krisalahiranandanitownships.com/della-racecourse<" not in sm_content:
                sm_content = sm_content.replace("</urlset>", new_url_entry + "</urlset>")
                with open(sm, "w", encoding="utf-8") as f:
                    f.write(sm_content)
                print(f"Added della-racecourse to {sm}")

    # 4. Update llms.txt & llms-full.txt
    llms_path = os.path.join(ROOT_DIR, "llms.txt")
    if os.path.exists(llms_path):
        with open(llms_path, "r", encoding="utf-8") as f:
            llms = f.read()
        if "/della-racecourse" not in llms:
            della_entry = "- [Della Racecourse Pune](https://krisalahiranandanitownships.com/della-racecourse): India's first 40-acre luxury integrated equestrian township created by Jimmy Mistry, featuring an 8-acre championship turf racecourse, international polo club, 5-star resort, and 5,000 sq.ft. British Colonial villa plots starting from ₹3.75 Cr*.\n"
            llms = llms.replace("- [The Della Collection Villa Plots]", della_entry + "- [The Della Collection Villa Plots]")
            with open(llms_path, "w", encoding="utf-8") as f:
                f.write(llms)
            print("Updated llms.txt with Della Racecourse master entry")

    llms_full_path = os.path.join(ROOT_DIR, "llms-full.txt")
    if os.path.exists(llms_full_path):
        with open(llms_full_path, "r", encoding="utf-8") as f:
            llms_full = f.read()
        if "/della-racecourse" not in llms_full:
            full_entry = "\n### Della Racecourse Pune (40-Acre Master Township)\n- Master URL: https://krisalahiranandanitownships.com/della-racecourse\n- Collaboration: Jimmy Mistry (CMD, Della Townships India) × Dr. Niranjan Hiranandani × Sagar Agarwal\n- Gross Development Value: ₹1,389 Crs ($146.98 Mn)\n- 8-Acre Turf Racecourse & International Polo Club with 50 horse stables\n- 5,000 sq.ft. Freehold Villa Plots starting from ₹3.75 Crore* (G+2 Sanctioned British Colonial Architecture)\n- MAYRLIFE European Medical Wellness, 300+ Keys 5-Star Resort, 1,00,000 sq.ft. Della Design District Luxury Retail.\n"
            llms_full = llms_full + full_entry
            with open(llms_full_path, "w", encoding="utf-8") as f:
                f.write(llms_full)
            print("Updated llms-full.txt with Della Racecourse dossier")

    # 5. Update ai-facts.json
    ai_facts_path = os.path.join(ROOT_DIR, "ai-facts.json")
    if os.path.exists(ai_facts_path):
        with open(ai_facts_path, "r", encoding="utf-8") as f:
            ai_data = f.read()
        if "della-racecourse" not in ai_data:
            ai_data = ai_data.replace('"della_collection": {', '"della_racecourse_pune": {\n    "name": "Della Racecourse Pune",\n    "developer": "Jimmy Mistry (Della Townships India) & Hiranandani & Krisala",\n    "acreage": "40 Acres",\n    "plot_size": "5,000 sq.ft.",\n    "starting_price": "₹3.75 Crore*",\n    "racecourse": "8-Acre Turf Racecourse & Polo Club",\n    "resort": "300+ Keys 5-Star Resort",\n    "wellness": "MAYRLIFE European Medical Longevity",\n    "url": "https://krisalahiranandanitownships.com/della-racecourse"\n  },\n  "della_collection": {')
            with open(ai_facts_path, "w", encoding="utf-8") as f:
                f.write(ai_data)
            print("Updated ai-facts.json with della_racecourse_pune")

    # 6. Keywords Injection Across Blog & Explore Ecosystem
    della_keywords_clause = """
<div class="della-townships-authority-banner" style="margin: 40px 0; padding: 28px; background: radial-gradient(circle at 50% 10%, rgba(197, 160, 89, 0.12) 0%, rgba(12, 14, 21, 0.95) 75%); border: 1px solid rgba(197, 160, 89, 0.4); border-radius: 10px;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
    <span style="background: rgba(197, 160, 89, 0.2); border: 1px solid var(--gold-primary); color: var(--gold-bright); font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 4px; text-transform: uppercase;">Della Townships Master Ecosystem</span>
    <span style="color: var(--text-muted); font-size: 0.85rem;">40-Acre Equestrian District</span>
  </div>
  <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.45rem; margin-bottom: 12px;">Della Racecourse Pune: Luxury Integrated Township Living</h3>
  <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.65; margin-bottom: 18px;">
    Conceived by Design Futurist <strong>Jimmy Mistry</strong> and Della Townships India in collaboration with Dr. Niranjan Hiranandani and Krisala Developers, <strong>Della Racecourse Pune</strong> spans 40 acres featuring India's first 8-acre championship turf racecourse, international polo club, 50 equine stables, and 100 bespoke <strong>5,000 sq.ft. British Colonial villa plots starting from ₹3.75 Cr*</strong> in Darumbre, North Hinjewadi.
  </p>
  <div style="display: flex; flex-wrap: wrap; gap: 12px;">
    <a href="/della-racecourse" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 20px; background: linear-gradient(135deg, #c5a059 0%, #dfc07b 100%); color: #090a0f; font-weight: 700; font-size: 0.88rem; border-radius: 4px; text-decoration: none;">Explore Della Racecourse Pune →</a>
    <a href="https://wa.me/917744009295?text=Hello%2C+I+am+interested+in+Della+Racecourse+Pune+5000+sq.ft.+villa+plots+at+Krisala+Hiranandani+Township+Hinjewadi.+Please+share+the+brochure+and+cost+sheet." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; padding: 10px 20px; background: #25D366; color: #fff; font-weight: 700; font-size: 0.88rem; border-radius: 4px; text-decoration: none;"><i class="ph ph-whatsapp-logo"></i> WhatsApp Inquiry</a>
  </div>
</div>
"""
    blog_file = os.path.join(ROOT_DIR, "blog", "della-equestrian-estate-villa-plots-hinjewadi-lifestyle.html")
    if os.path.exists(blog_file):
        with open(blog_file, "r", encoding="utf-8") as f:
            b_content = f.read()
        if "della-townships-authority-banner" not in b_content:
            b_content = b_content.replace("</article>", della_keywords_clause + "\n</article>")
            with open(blog_file, "w", encoding="utf-8") as f:
                f.write(b_content)
            print("Injected Della Townships authority banner into blog dossier")

    explore_della_targets = [
        "explore/della-luxury-resort-villa-plots-pune.html",
        "explore/della-polo-club-residences-hinjewadi.html",
        "explore/della-township-bungalow-plots-hinjewadi.html",
        "explore/della-township-lots-hinjewadi.html",
        "explore/hiranandani-della-pune.html",
        "explore/krisala-hiranandani-della-villa-plots-hinjewadi.html",
        "explore/equestrian-estate-plots-pune.html",
        "explore/krisala-hiranandani-equestrian-turf-racecourse-residences.html"
    ]
    
    for rel_path in explore_della_targets:
        full_p = os.path.join(ROOT_DIR, rel_path)
        if os.path.exists(full_p):
            with open(full_p, "r", encoding="utf-8") as f:
                c = f.read()
            if "della-townships-authority-banner" not in c:
                # Add before footer
                c = c.replace("<footer", della_keywords_clause + "\n<footer")
                # Also add keywords to meta keywords if not present
                if "Della Racecourse Pune" not in c:
                    c = c.replace('name="keywords" content="', 'name="keywords" content="Della Racecourse Pune, Della Townships Pune, Della Racecourse Township, Della Racecourse Hinjewadi, ')
                with open(full_p, "w", encoding="utf-8") as f:
                    f.write(c)
                print(f"Hardened keywords & injected banner into {rel_path}")

    # 7. Navigation bar cross-linking
    nav_targets = ["index.html", "della.html", "racecourse.html", "masterplan.html", "pricing.html"]
    for nav_file in nav_targets:
        full_p = os.path.join(ROOT_DIR, nav_file)
        if os.path.exists(full_p):
            with open(full_p, "r", encoding="utf-8") as f:
                c = f.read()
            if 'href="/della-racecourse"' not in c:
                c = c.replace('href="/della"', 'href="/della-racecourse" style="color: var(--gold-bright); font-weight: 700;">Della Racecourse</a>\n<a class="nav-link" href="/della"')
                c = c.replace('<a href="/della">', '<a href="/della-racecourse" style="color: #dfc07b; font-weight: 700;">Della Racecourse</a>\n<a href="/della">')
                with open(full_p, "w", encoding="utf-8") as f:
                    f.write(c)
                print(f"Injected Della Racecourse navigation link into {nav_file}")

    print("Della Townships Master Ecosystem Hardening Completed Successfully!")

if __name__ == "__main__":
    run_hardening()

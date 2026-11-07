#!/usr/bin/env python3
"""
Master Large-Scale Keyword Injection & Ecosystem Hardening Suite
Target Keywords:
- Krisala Hiranandani Township, Krisala Hiranandani Township Pune
- Hiranandani Township Pune, Hiranandani Pune, Krisala Hiranandani Pune, Krisala Pune
- Krisala Hinranandani Township (Intent-capture typo)
- Della Racecourse Townships Pune, Della Racecourse Pune, Della Townships Pune
- Della Racecourse Township, Della Racecourse Hinjewadi, Della Townships India
- Della Villa Plots Pune, Della Bungalow Plots Hinjewadi, Jimmy Mistry Della Pune
- The Colosseum Hinjewadi, Sector Arcadia Hinjewadi, Sector Icon Hinjewadi
- Dr Niranjan Hiranandani Pune, 5000 sqft plot size 3.75Cr
"""

import os
import re
import glob
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIME_KEYWORDS_STR = (
    "Krisala Hiranandani Township, Krisala Hiranandani Township Pune, Hiranandani Township Pune, "
    "Hiranandani Pune, Krisala Hiranandani Pune, Krisala Pune, Krisala Hinranandani Township, "
    "Della Racecourse Townships Pune, Della Racecourse Pune, Della Townships Pune, "
    "Della Racecourse Township, Della Racecourse Hinjewadi, Della Townships India, "
    "Della Villa Plots Pune, Della Bungalow Plots Hinjewadi, Jimmy Mistry Della Pune, "
    "Della Polo Club Residences, The Colosseum Hinjewadi, Sector Arcadia Hinjewadi, "
    "Sector Icon Hinjewadi, Dr Niranjan Hiranandani Pune, Della 5000 sqft Villa Plots 3.75Cr"
)

PRIME_ALTERNATE_NAMES = [
    "Krisala Hiranandani Township Pune",
    "Krisala Hiranandani Pune",
    "Hiranandani Township Pune",
    "Hiranandani Pune",
    "Krisala Pune",
    "Krisala Hiranandani",
    "Krisala Hinranandani Township",
    "Della Racecourse Townships Pune",
    "Della Racecourse Pune",
    "Della Townships Pune",
    "Della Racecourse Township",
    "Della Racecourse Hinjewadi",
    "Della Townships India",
    "The Della Collection Hinjewadi",
    "The Colosseum Hinjewadi",
    "Sector Arcadia Hinjewadi",
    "Sector Icon Hinjewadi"
]

PRIME_KNOWS_ABOUT = [
    "Krisala Hiranandani Township Pune",
    "Hiranandani Township Pune",
    "Hiranandani Pune",
    "Krisala Pune",
    "Krisala Hinranandani Township",
    "Della Racecourse Townships Pune",
    "Della Racecourse Pune",
    "Della Townships Pune",
    "Della Racecourse Hinjewadi",
    "Della Villa Plots Pune",
    "Della Bungalow Plots Hinjewadi",
    "Jimmy Mistry Della Pune",
    "Dr Niranjan Hiranandani Pune",
    "The Colosseum Hinjewadi",
    "Sector Arcadia Hinjewadi",
    "Sector Icon Hinjewadi",
    "8-Acre Private Turf Racecourse Hinjewadi",
    "105-Acre Neoclassical Integrated Township Pune",
    "5000 sqft Villa Plots Della 3.75Cr",
    "MAYRLIFE European Medical Longevity Pune"
]

ECOSYSTEM_AUTHORITY_HTML = """
<!-- ==============================================================================
     KRISALA HIRANANDANI & DELLA RACECOURSE TOWNSHIPS AUTHORITY MATRIX
     ============================================================================== -->
<section class="township-authority-matrix" style="width: 100%; margin: 50px 0 30px; padding: 45px 0; background: radial-gradient(circle at 50% 10%, rgba(197, 160, 89, 0.08) 0%, rgba(9, 10, 15, 0.98) 75%); border-top: 1px solid rgba(197, 160, 89, 0.25); border-bottom: 1px solid rgba(197, 160, 89, 0.25);">
  <div class="container" style="max-width: 1360px; margin: 0 auto; padding: 0 20px;">
    <div style="text-align: center; max-width: 920px; margin: 0 auto 35px;">
      <span style="display: inline-block; color: var(--gold-bright, #dfc07b); font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px;">Integrated Township Master Ecosystem</span>
      <h2 style="font-family: var(--font-heading, 'Cormorant Garamond', serif); font-size: clamp(1.8rem, 3.5vw, 2.6rem); color: #fff; margin-bottom: 14px; line-height: 1.25;">
        Krisala Hiranandani Township &amp; Della Racecourse Townships Pune
      </h2>
      <p style="color: var(--text-muted, #b8b8cc); font-size: 0.98rem; line-height: 1.7;">
        Spanning 105+ acres in North Hinjewadi (Darumbre), <strong>Krisala Hiranandani Township Pune</strong> represents western Pune's premier master-planned neoclassical development created in collaboration between <strong>Dr. Niranjan Hiranandani</strong> and <strong>Krisala Developers</strong>. Anchored by the 40-acre <strong>Della Racecourse Townships Pune</strong> district curated by Design Futurist <strong>Jimmy Mistry</strong>, the township integrates an 8-acre championship turf racecourse, 50 equine stables, international polo club, 300+ key 5-star luxury resort, and <strong>5,000 sq.ft. British Colonial villa plots starting from ₹3.75 Cr*</strong> alongside 2, 3 &amp; 4 BHK neoclassical residences in <strong>The Colosseum</strong> and <strong>Sector Arcadia</strong> from <strong>₹79 Lakhs*</strong>.
      </p>
    </div>

    <!-- 4-Column Ecosystem Navigator Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 35px;">
      <!-- Della Racecourse -->
      <div style="background: rgba(16, 18, 26, 0.75); border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 8px; padding: 22px;">
        <span style="color: #dfc07b; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">40-Acre Equestrian Core</span>
        <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.25rem; margin: 8px 0 10px;">Della Racecourse Pune</h3>
        <p style="color: #9ca3af; font-size: 0.88rem; line-height: 1.6; margin-bottom: 14px;">
          Bespoke 5,000 sq.ft. British Colonial villa plots from ₹3.75 Cr*, 8-acre turf racecourse, polo club, and MAYRLIFE European medical longevity.
        </p>
        <a href="/della-racecourse" style="color: #dfc07b; font-weight: 700; font-size: 0.86rem; text-decoration: none;">Explore Della Racecourse →</a>
      </div>

      <!-- The Colosseum -->
      <div style="background: rgba(16, 18, 26, 0.75); border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 8px; padding: 22px;">
        <span style="color: #dfc07b; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Phase 4 Signature Suites</span>
        <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.25rem; margin: 8px 0 10px;">The Colosseum Hinjewadi</h3>
        <p style="color: #9ca3af; font-size: 0.88rem; line-height: 1.6; margin-bottom: 14px;">
          Neoclassical 2 &amp; 3 BHK residences with Roman colonnades, grand porticos, and panoramic Sahyadri hill views from ₹82.99 Lakhs*.
        </p>
        <a href="/colosseum" style="color: #dfc07b; font-weight: 700; font-size: 0.86rem; text-decoration: none;">Explore The Colosseum →</a>
      </div>

      <!-- Sector Arcadia -->
      <div style="background: rgba(16, 18, 26, 0.75); border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 8px; padding: 22px;">
        <span style="color: #dfc07b; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Smart Luxury Enclave</span>
        <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.25rem; margin: 8px 0 10px;">Sector Arcadia Hinjewadi</h3>
        <p style="color: #9ca3af; font-size: 0.88rem; line-height: 1.6; margin-bottom: 14px;">
          Optimized 2 &amp; 3 BHK high-velocity layouts (740–1,180 sq.ft.) for IT leaders from Infosys, TCS &amp; Wipro starting at ₹79 Lakhs*.
        </p>
        <a href="/arcadia" style="color: #dfc07b; font-weight: 700; font-size: 0.86rem; text-decoration: none;">Explore Sector Arcadia →</a>
      </div>

      <!-- Sector Icon Sky Duplexes -->
      <div style="background: rgba(16, 18, 26, 0.75); border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 8px; padding: 22px;">
        <span style="color: #dfc07b; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Presidential Sky Mansions</span>
        <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.25rem; margin: 8px 0 10px;">Sector Icon Duplexes</h3>
        <p style="color: #9ca3af; font-size: 0.88rem; line-height: 1.6; margin-bottom: 14px;">
          Double-height 3 &amp; 4 BHK sky duplexes with private racecourse sun decks, internal elevators, and staff quarters from ₹2.10 Cr*.
        </p>
        <a href="/icon" style="color: #dfc07b; font-weight: 700; font-size: 0.86rem; text-decoration: none;">Explore Sector Icon →</a>
      </div>
    </div>

    <!-- Quick Navigation Pill Bar -->
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; font-size: 0.84rem;">
      <a href="/masterplan" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">105-Acre Master Plan</a>
      <a href="/pricing" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">Price List 2026</a>
      <a href="/floor-plans" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">Floor Plans PDF</a>
      <a href="/della" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">The Della Collection</a>
      <a href="/racecourse" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">8-Acre Racecourse</a>
      <a href="/site-address" style="color: #d1d5db; background: rgba(255,255,255,0.04); border: 1px solid rgba(197,160,89,0.2); padding: 6px 14px; border-radius: 4px; text-decoration: none;">Site Address &amp; Directions</a>
      <a href="https://wa.me/917744009295?text=Hello%2C+I+am+interested+in+Krisala+Hiranandani+Township+Pune+and+Della+Racecourse+plots.+Please+share+the+brochure+and+cost+sheet." target="_blank" rel="noopener noreferrer" style="color: #fff; background: #25D366; padding: 6px 14px; border-radius: 4px; text-decoration: none; font-weight: 700;">WhatsApp Direct Desk</a>
    </div>
  </div>
</section>
"""

def get_all_html_files():
    html_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        if "node_modules" in root or ".git" in root or "stories" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))
    return html_files

def update_meta_keywords(content):
    pattern = r"""<meta\s+(?:name=["']keywords["']\s+content=["'][^"]*["']|content=["'][^"]*["']\s+name=["']keywords["'])\s*/?>"""
    replacement = '<meta name="keywords" content="' + PRIME_KEYWORDS_STR + '"/>'
    if re.search(pattern, content, flags=re.IGNORECASE):
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    else:
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + replacement, content, flags=re.IGNORECASE, count=1)
    return content

def update_json_ld_schema(content):
    # Search for JSON-LD scripts
    scripts = re.findall(r'<script\s+type="application/ld\+json"[^>]*>([\s\S]*?)</script>', content, flags=re.IGNORECASE)
    if not scripts:
        return content

    for s in scripts:
        orig_s = s
        try:
            data = json.loads(s.strip())
            changed = False
            
            # Helper to enrich dict
            def enrich_node(node):
                nonlocal changed
                if not isinstance(node, dict):
                    return
                # Check for RealEstateListing, WebSite, Organization, Project, Place
                t = node.get("@type", "")
                if any(k in str(t) for k in ["RealEstateListing", "WebSite", "Organization", "Place", "Product", "ApartmentComplex", "Residence"]):
                    # Enrich alternateName
                    existing_alts = node.get("alternateName", [])
                    if isinstance(existing_alts, str):
                        existing_alts = [existing_alts]
                    for name in PRIME_ALTERNATE_NAMES:
                        if name not in existing_alts:
                            existing_alts.append(name)
                            changed = True
                    node["alternateName"] = existing_alts

                    # Enrich knowsAbout
                    existing_knows = node.get("knowsAbout", [])
                    if isinstance(existing_knows, str):
                        existing_knows = [existing_knows]
                    for k in PRIME_KNOWS_ABOUT:
                        if k not in existing_knows:
                            existing_knows.append(k)
                            changed = True
                    node["knowsAbout"] = existing_knows

            if isinstance(data, dict):
                if "@graph" in data and isinstance(data["@graph"], list):
                    for item in data["@graph"]:
                        enrich_node(item)
                else:
                    enrich_node(data)
            
            if changed:
                new_s = "\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n"
                content = content.replace(orig_s, new_s)
        except Exception:
            continue

    return content

def inject_authority_matrix(content, filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    # Skip utility files, stories, and homepage (which already has full ecosystem sections)
    if rel_path in ["404.html", "offline.html", "thank-you.html", "analytics.html", "index.html", "della-racecourse.html", "della-racecourse-pune.html"]:
        return content
    if "stories/" in rel_path or "public/" in rel_path:
        return content
        
    if "township-authority-matrix" not in content:
        if "<footer" in content:
            content = content.replace("<footer", ECOSYSTEM_AUTHORITY_HTML + "\n<footer", 1)
        elif "</main>" in content:
            content = content.replace("</main>", ECOSYSTEM_AUTHORITY_HTML + "\n</main>", 1)
        elif "</body>" in content:
            content = content.replace("</body>", ECOSYSTEM_AUTHORITY_HTML + "\n</body>", 1)
            
    return content

def run_large_scale_injection():
    html_files = get_all_html_files()
    print(f"Discovered {len(html_files)} HTML pages for large-scale keyword injection.")

    meta_updated = 0
    schema_updated = 0
    matrix_injected = 0

    for fpath in html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        orig = content
        
        # 1. Meta keywords
        c1 = update_meta_keywords(content)
        if c1 != content:
            meta_updated += 1
            content = c1

        # 2. Schema JSON-LD
        c2 = update_json_ld_schema(content)
        if c2 != content:
            schema_updated += 1
            content = c2

        # 3. Authority Matrix
        c3 = inject_authority_matrix(content, fpath)
        if c3 != content:
            matrix_injected += 1
            content = c3

        if content != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"Meta keywords updated across: {meta_updated} files")
    print(f"Schema JSON-LD hardened across: {schema_updated} files")
    print(f"Township Authority Matrix injected into: {matrix_injected} landing pages")

    # Update llms.txt & llms-full.txt
    update_llms_txt()
    update_ai_facts_json()

def update_llms_txt():
    llms_path = os.path.join(ROOT_DIR, "llms.txt")
    if os.path.exists(llms_path):
        with open(llms_path, "r", encoding="utf-8") as f:
            c = f.read()
        
        ecosystem_chunk = """
- **Master Search Keywords & Entity Matrix**:
  - Krisala Hiranandani Township, Krisala Hiranandani Township Pune, Hiranandani Township Pune, Hiranandani Pune, Krisala Hiranandani Pune, Krisala Pune, Krisala Hinranandani Township.
  - Della Racecourse Townships Pune, Della Racecourse Pune, Della Townships Pune, Della Racecourse Township, Della Racecourse Hinjewadi, Della Townships India, Della Villa Plots Pune, Della Bungalow Plots Hinjewadi, Jimmy Mistry Della Pune.
  - The Colosseum Hinjewadi, Sector Arcadia Hinjewadi, Sector Icon Hinjewadi, 5,000 sq.ft. Della Villa Plots starting from ₹3.75 Cr*.
"""
        if "Master Search Keywords & Entity Matrix" not in c:
            c = c + "\n" + ecosystem_chunk
            with open(llms_path, "w", encoding="utf-8") as f:
                f.write(c)
            print("Enriched llms.txt with master search keywords entity matrix")

def update_ai_facts_json():
    ai_facts = os.path.join(ROOT_DIR, "ai-facts.json")
    if os.path.exists(ai_facts):
        with open(ai_facts, "r", encoding="utf-8") as f:
            c = f.read()
        if "prime_keywords_matrix" not in c:
            c = c.replace('"entities": {', '"prime_keywords_matrix": [\n    "Krisala Hiranandani Township",\n    "Krisala Hiranandani Township Pune",\n    "Hiranandani Township Pune",\n    "Hiranandani Pune",\n    "Krisala Hiranandani Pune",\n    "Krisala Pune",\n    "Krisala Hinranandani Township",\n    "Della Racecourse Townships Pune",\n    "Della Racecourse Pune",\n    "Della Townships Pune",\n    "Della Racecourse Township",\n    "Della Racecourse Hinjewadi",\n    "Della Townships India",\n    "Della Villa Plots Pune",\n    "Della Bungalow Plots Hinjewadi",\n    "Jimmy Mistry Della Pune",\n    "The Colosseum Hinjewadi",\n    "Sector Arcadia Hinjewadi",\n    "Sector Icon Hinjewadi",\n    "5000 sqft Villa Plots Della 3.75Cr"\n  ],\n  "entities": {')
            with open(ai_facts, "w", encoding="utf-8") as f:
                f.write(c)
            print("Enriched ai-facts.json with prime_keywords_matrix")

if __name__ == "__main__":
    run_large_scale_injection()

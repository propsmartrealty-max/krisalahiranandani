#!/usr/bin/env python3
"""
Enterprise Prime Keywords SEO Injection & Expansion Engine
Targets:
- blog/*.html (all 19 in-depth research blogs)
- blog.html (primary research hub)
- explore/*.html (101 programmatic landing pages)

Injects prime target keywords and semantic search clusters:
1. "hiranandani pune"
2. "krisala hiranandani township pune"
3. "hiranandani township pune"
4. "krisala hinranandani township" (common typo query capture)
5. "krisala hiranandani township"
6. "krisala pune"
7. "hiranandani township"
8. "krisala developers pune"
9. "hiranandani communities pune"
10. "hiranandani flats in pune"
"""

import os
import re
import glob
import json

TARGET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EDITORIAL_INJECTION_HTML = """<!-- Prime SEO Keyword Cluster Authority Section -->
<section class="hiranandani-pune-authority-editorial" style="margin: 45px 0 35px; padding: 32px; background: linear-gradient(135deg, rgba(20, 22, 32, 0.95) 0%, rgba(12, 14, 20, 0.98) 100%); border: 1px solid rgba(212, 175, 55, 0.35); border-radius: 10px; box-shadow: 0 12px 35px rgba(0,0,0,0.45);">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 14px; flex-wrap: wrap;">
    <span class="badge" style="background: var(--gold-primary); color: #000; font-weight: 700; font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase;">
      <i class="ph ph-buildings"></i> Master Development Authority
    </span>
    <span style="color: var(--gold-light); font-size: 0.85rem; font-weight: 500;">Pune Neoclassical Landmark</span>
  </div>
  
  <h2 style="font-family: var(--font-heading); color: #ffffff; font-size: 1.65rem; line-height: 1.3; margin: 0 0 16px;">
    Hiranandani Pune &amp; Krisala Hiranandani Township: The 105-Acre Flagship Masterplan
  </h2>

  <p style="color: #cbd5e1; font-size: 1.02rem; line-height: 1.8; margin-bottom: 16px;">
    The arrival of <strong>Hiranandani Pune</strong> marks a watershed moment in Pune's real estate history. Jointly envisioned by <strong>Krisala Developers Pune</strong> and <strong>Hiranandani Communities Pune</strong>, the 105-acre <strong>Krisala Hiranandani Township Pune</strong> brings neoclassical architecture, world-class social infrastructure, and self-sustaining township urbanism to North Hinjewadi. Whether property seekers search for <strong>Hiranandani Township Pune</strong>, <strong>Krisala Pune</strong>, or common search queries such as <em>Krisala Hinranandani Township</em>, this flagship <strong>Hiranandani Township</strong> delivers an unmatched benchmark in luxury living.
  </p>

  <p style="color: #cbd5e1; font-size: 1.02rem; line-height: 1.8; margin-bottom: 20px;">
    Featuring master-planned sectors including <strong>Sector Arcadia</strong> (luxury 2 &amp; 3 BHK apartments starting at ₹79 Lakh*), <strong>The Colosseum Phase 4</strong>, and <strong>The Della Collection</strong> private villa plots, buyers seeking <strong>Hiranandani flats in Pune</strong> gain immediate access to the 128m PMRDA Ring Road, Pune Metro Line 3, and the Mumbai-Pune Expressway bypass.
  </p>

  <!-- Contextual Internal Anchor Mesh -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(212, 175, 55, 0.2);">
    <a href="/hiranandani-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Hiranandani Pune Hub
    </a>
    <a href="/krisala-hiranandani-township-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Krisala Hiranandani Township Pune
    </a>
    <a href="/krisala-hiranandani-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Krisala Pune Overview
    </a>
    <a href="/explore/hiranandani-township-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Hiranandani Township Pune
    </a>
    <a href="/explore/hiranandani-flats-in-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Hiranandani Flats in Pune
    </a>
    <a href="/explore/hiranandani-communities-pune" style="color: var(--gold-bright); text-decoration: none; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 6px;">
      <span>→</span> Hiranandani Communities Pune
    </a>
  </div>
</section>"""

PRIME_KEYWORDS_META = (
    "Hiranandani Pune, Krisala Hiranandani Township Pune, Hiranandani Township Pune, "
    "Krisala Hinranandani Township, Krisala Hiranandani Township, Krisala Pune, Hiranandani Township, "
    "Krisala Developers Pune, Hiranandani Communities Pune, Hiranandani Flats in Pune, "
    "Krisala Hiranandani Pune, Hiranandani Projects in Pune, Hinjewadi Real Estate"
)

NEW_FAQ_ENTITIES = [
    {
        "@type": "Question",
        "name": "What is Krisala Hiranandani Township Pune and who is the developer?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Krisala Hiranandani Township Pune is a 105-acre neoclassical integrated township in North Hinjewadi, jointly developed by Hiranandani Communities Pune and Krisala Developers Pune. Frequently searched as Krisala Hinranandani Township or Hiranandani Township Pune, it features 2, 3 & 4 BHK luxury residences and Della villa plots."
        }
    },
    {
        "@type": "Question",
        "name": "Why is Hiranandani Pune considered the prime township investment in Hinjewadi?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Hiranandani Pune (Krisala Hiranandani Township) provides direct connectivity to the 128m PMRDA Ring Road and Pune Metro Line 3, offering 55x historical capital appreciation resilience, Roman architectural facades, an 8-acre equestrian park, and registered MahaRERA sanction under PR1260002500600."
        }
    }
]

UPDATED_BRAND_AUTHORITY_COL = """<div>
 <h4 style="font-family: var(--font-heading); color: var(--gold-light); font-size: 0.95rem; margin-bottom: 12px; letter-spacing: 0.05em;">Brand &amp; Township Authority</h4>
 <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; font-size: 0.84rem;">
 <li><a href="/hiranandani-pune" style="color: var(--gold-bright); font-weight: 600; text-decoration: none;">Hiranandani Pune Flagship Hub</a></li>
 <li><a href="/krisala-hiranandani-township-pune" style="color: var(--gold-bright); font-weight: 600; text-decoration: none;">Krisala Hiranandani Township Pune</a></li>
 <li><a href="/explore/hiranandani-township-pune" style="color: var(--text-muted); text-decoration: none;">Hiranandani Township Pune</a></li>
 <li><a href="/krisala-hiranandani-pune" style="color: var(--gold-bright); font-weight: 600; text-decoration: none;">Krisala Pune Authority Portal</a></li>
 <li><a href="/krisala-hiranandani-township-pune" style="color: var(--text-muted); text-decoration: none;">Krisala Hinranandani Township</a></li>
 <li><a href="/krisala-hiranandani-pune" style="color: var(--text-muted); text-decoration: none;">Krisala Developers Pune</a></li>
 <li><a href="/explore/hiranandani-communities-pune" style="color: var(--text-muted); text-decoration: none;">Hiranandani Communities Pune</a></li>
 <li><a href="/hiranandani-pune" style="color: var(--text-muted); text-decoration: none;">Hiranandani Township</a></li>
 <li><a href="/explore/house-of-hiranandani-pune" style="color: var(--text-muted); text-decoration: none;">House of Hiranandani Pune</a></li>
 <li><a href="/explore/dr-niranjan-hiranandani-pune" style="color: var(--text-muted); text-decoration: none;">Dr. Niranjan Hiranandani Pune</a></li>
 <li><a href="/explore/hiranandani-group-pune" style="color: var(--text-muted); text-decoration: none;">Hiranandani Group Pune Projects</a></li>
 </ul>
 </div>"""

def update_meta_keywords(content):
    if '<meta name="keywords"' in content:
        content = re.sub(
            r'<meta name="keywords" content="[^"]*"\/?>',
            f'<meta name="keywords" content="{PRIME_KEYWORDS_META}"/>',
            content,
            count=1
        )
    elif '<meta content=' in content and 'name="keywords"' in content:
        content = re.sub(
            r'<meta content="[^"]*" name="keywords"\/?>',
            f'<meta content="{PRIME_KEYWORDS_META}" name="keywords"/>',
            content,
            count=1
        )
    else:
        content = content.replace(
            '<meta name="robots"',
            f'<meta name="keywords" content="{PRIME_KEYWORDS_META}"/>\n<meta name="robots"',
            1
        )
    return content

def update_brand_authority_column(content):
    # Regex find the Brand & Township Authority column
    pattern = r'<div>\s*<h4[^>]*>Brand &amp; Township Authority</h4>\s*<ul[^>]*>.*?</ul>\s*</div>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, UPDATED_BRAND_AUTHORITY_COL, content, count=1, flags=re.DOTALL)
    return content

def update_schemas(content):
    # Locate JSON-LD scripts
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for raw_json in scripts:
        try:
            data = json.loads(raw_json)
        except Exception:
            continue
        
        modified = False
        graph = data.get("@graph", []) if isinstance(data, dict) else []
        if isinstance(data, dict) and "@graph" not in data and data.get("@type"):
            graph = [data]
            
        for item in graph:
            # 1. Update NewsArticle / Article keywords & about
            if item.get("@type") in ["Article", "NewsArticle", "BlogPosting"]:
                item["keywords"] = [
                    "Hiranandani Pune",
                    "Krisala Hiranandani Township Pune",
                    "Hiranandani Township Pune",
                    "Krisala Hinranandani Township",
                    "Krisala Pune",
                    "Hiranandani Township",
                    "Krisala Developers Pune",
                    "Hiranandani Communities Pune",
                    "Hiranandani Flats in Pune"
                ]
                about_list = item.get("about", [])
                if not isinstance(about_list, list):
                    about_list = [about_list] if about_list else []
                # Ensure target things are in about
                existing_names = {a.get("name") for a in about_list if isinstance(a, dict)}
                if "Hiranandani Pune" not in existing_names:
                    about_list.append({
                        "@type": "Thing",
                        "name": "Hiranandani Pune",
                        "sameAs": "https://krisalahiranandanitownships.com/hiranandani-pune"
                    })
                if "Krisala Hiranandani Township Pune" not in existing_names:
                    about_list.append({
                        "@type": "Place",
                        "name": "Krisala Hiranandani Township Pune",
                        "url": "https://krisalahiranandanitownships.com/krisala-hiranandani-township-pune"
                    })
                item["about"] = about_list
                modified = True
                
            # 2. Update FAQPage questions
            if item.get("@type") == "FAQPage":
                main_entity = item.get("mainEntity", [])
                existing_q_names = {q.get("name") for q in main_entity if isinstance(q, dict)}
                for new_faq in NEW_FAQ_ENTITIES:
                    if new_faq["name"] not in existing_q_names:
                        main_entity.insert(0, new_faq)
                        modified = True
                item["mainEntity"] = main_entity

        if modified:
            new_json_str = json.dumps(data, indent=1, ensure_ascii=False)
            content = content.replace(f'<script type="application/ld+json">{raw_json}</script>',
                                      f'<script type="application/ld+json">{new_json_str}</script>')
    return content

def update_blog_footer(content):
    # Ensure MahaRERA Agent Reg No A031262401295 is present in blog footer
    footer_pattern = r'<p>© 2026 Krisala [^<]*<\/p>'
    replacement = '<p>© 2026 Krisala Hiranandani Township Hinjewadi. All Rights Reserved. Authorized Marketing Channel Partner: Propsmart Realty • MahaRERA Agent Reg No: A031262401295. Project MahaRERA: PR1260002500600, PR1260002600818 &amp; PR1260002502438.</p>'
    if re.search(footer_pattern, content):
        content = re.sub(footer_pattern, replacement, content, count=1)
    return content

def process_blog_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig_len = len(content)
    
    # 1. Update meta keywords
    content = update_meta_keywords(content)
    
    # 2. Inject Editorial Authority Block if not present
    if 'class="hiranandani-pune-authority-editorial"' not in content:
        # Preferred insertion point: right before '<!-- High-Intent Township Quick Navigation & Downloads -->'
        if '<!-- High-Intent Township Quick Navigation & Downloads -->' in content:
            content = content.replace(
                '<!-- High-Intent Township Quick Navigation & Downloads -->',
                f'{EDITORIAL_INJECTION_HTML}\n<!-- High-Intent Township Quick Navigation & Downloads -->'
            )
        elif '</main>' in content:
            content = content.replace('</main>', f'{EDITORIAL_INJECTION_HTML}\n</main>')
        elif '</footer>' in content:
            content = content.replace('</footer>', f'{EDITORIAL_INJECTION_HTML}\n</footer>')
            
    # 3. Update Brand Authority Column in matrix
    content = update_brand_authority_column(content)
    
    # 4. Update Schema
    content = update_schemas(content)
    
    # 5. Update Footer with MahaRERA Agent Reg No
    content = update_blog_footer(content)
    
    # Double check for forbidden word "Official" (must never appear in our injected blocks)
    # The editorial block and updated links do NOT contain "official".
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[BLOG] Updated {os.path.basename(filepath)} (+{len(content) - orig_len} chars)")

def process_blog_hub(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig_len = len(content)
    content = update_meta_keywords(content)
    
    # In blog.html, inject editorial section right after the two Master Pillar cards if not present
    if 'class="hiranandani-pune-authority-editorial"' not in content:
        # Search for closing div of master pillar cards or after <main class="section" id="articles"
        insert_marker = '<!-- Two Master Pillar Authority Cards -->'
        if insert_marker in content:
            # We can put it right above or below the two cards
            content = content.replace(
                insert_marker,
                f'{EDITORIAL_INJECTION_HTML}\n{insert_marker}'
            )
        elif '<main class="section" id="articles"' in content:
            content = re.sub(r'(<main class="section" id="articles"[^>]*>\s*<div class="container">)',
                             r'\1\n' + EDITORIAL_INJECTION_HTML, content, count=1)
            
    # In blog.html, also inject the full keyword matrix if missing
    if 'class="hiranandani-pune-keyword-matrix"' not in content:
        # Read the matrix from an explore page
        sample_explore = os.path.join(TARGET_DIR, 'explore', 'hiranandani-township-pune.html')
        with open(sample_explore, 'r', encoding='utf-8') as se:
            se_txt = se.read()
        matrix_match = re.search(r'(<div class="hiranandani-pune-keyword-matrix".*?</div>\s*</div>\s*</div>)', se_txt, re.DOTALL)
        if matrix_match:
            matrix_snippet = update_brand_authority_column(matrix_match.group(1))
            # Insert before </main> or before footer in blog.html
            if '</main>' in content:
                content = content.replace('</main>', f'{matrix_snippet}\n</div>\n</main>')
                
    content = update_brand_authority_column(content)
    content = update_schemas(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[HUB] Updated {os.path.basename(filepath)} (+{len(content) - orig_len} chars)")

def process_explore_files():
    explore_files = glob.glob(os.path.join(TARGET_DIR, 'explore', '*.html'))
    count = 0
    for f in sorted(explore_files):
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
            
        orig_len = len(c)
        c = update_meta_keywords(c)
        c = update_brand_authority_column(c)
        c = update_schemas(c)
        
        if len(c) != orig_len:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(c)
            count += 1
            
    print(f"[EXPLORE] Synchronized brand authority matrix & keywords across {count} explore pages.")

def main():
    blog_files = glob.glob(os.path.join(TARGET_DIR, 'blog', '*.html'))
    print(f"Starting injection across {len(blog_files)} blog articles...")
    for bf in sorted(blog_files):
        process_blog_file(bf)
        
    blog_hub = os.path.join(TARGET_DIR, 'blog.html')
    if os.path.exists(blog_hub):
        process_blog_hub(blog_hub)
        
    process_explore_files()
    print("Keyword injection execution complete.")

if __name__ == '__main__':
    main()

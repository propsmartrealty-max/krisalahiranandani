#!/usr/bin/env python3
"""
Master Della Racecourse Pricing & Plot Size Calibration Script
Target:
- Della Racecourse Villa Plots pricing starts at ₹3.75 Cr* (₹3.75 Crore*)
- Plot size: 5,000 sq.ft. (5,000 sqft plot size)
"""

import os
import re
import glob

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def update_file(filepath, replacements):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    for pattern, repl in replacements:
        if isinstance(pattern, str):
            content = content.replace(pattern, repl)
        else:
            content = pattern.sub(repl, content)
            
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

def run_updates():
    updated_files = 0
    
    # 1. Update della.html
    della_path = os.path.join(PROJECT_DIR, "della.html")
    if os.path.exists(della_path):
        with open(della_path, 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Titles & Meta
        c = re.sub(r'<title>Della Township Plots \| Krisala Hiranandani Township Pune [^<]+</title>',
                   '<title>Della Township Plots | Krisala Hiranandani Township Pune ₹3.75Cr*</title>', c)
        c = re.sub(r'<meta content="Della Township at Krisala Hiranandani Hinjewadi\. Freehold bungalow plots &amp; Della lots around 8-acre racecourse from [^"]+" name="description"/>',
                   '<meta content="Della Township at Krisala Hiranandani Hinjewadi. Freehold 5,000 sq.ft. equestrian bungalow plots around 8-acre racecourse starting from ₹3.75 Cr*. MahaRERA PR1260002500600." name="description"/>', c)
        c = re.sub(r'property="og:title" content="Della Township Plots \| Krisala Hiranandani [^"]+"',
                   'property="og:title" content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*"', c)
        c = re.sub(r'name="twitter:title" content="Della Township Plots \| Krisala Hiranandani [^"]+"',
                   'name="twitter:title" content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*"', c)
        c = c.replace('property="og:title" content="Della Township Plots | Krisala Hiranandani ₹1.8Cr*"', 'property="og:title" content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*"')
        c = c.replace('name="twitter:title" content="Della Township Plots | Krisala Hiranandani ₹1.8Cr*"', 'name="twitter:title" content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*"')
        c = c.replace('content="Della Township Plots | Krisala Hiranandani ₹1.8Cr*" property="og:title"', 'content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*" property="og:title"')
        c = c.replace('content="Della Township Plots | Krisala Hiranandani ₹1.8Cr*" name="twitter:title"', 'content="Della Township Plots | Krisala Hiranandani ₹3.75Cr*" name="twitter:title"')
        
        # FAQ schema
        c = c.replace('Villa plots start from ₹1.80 Cr* onwards, subject to plot dimensions, location frontage, and racecourse proximity.',
                      'Della racecourse villa plots start at ₹3.75 Cr* with 5,000 sq.ft. plot size, subject to plot dimensions, location frontage, and racecourse proximity.')
        
        # Plot Cards
        c = c.replace('<li><i class="ph ph-check gold-icon"></i> <strong>Plot Size</strong>: 1,800 – 2,400 sq.ft.</li>\n<li><i class="ph ph-check gold-icon"></i> <strong>Permissible FSI</strong>: Sanctioned for G+2 Bungalow / Villa</li>\n<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹1.80 Cr* onwards</li>',
                      '<li><i class="ph ph-check gold-icon"></i> <strong>Plot Size</strong>: 5,000 sq.ft. (Equestrian Plot)</li>\n<li><i class="ph ph-check gold-icon"></i> <strong>Permissible FSI</strong>: Sanctioned for G+2 Bungalow / Villa</li>\n<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹3.75 Cr* onwards</li>')
        c = c.replace('<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹1.80 Cr* onwards</li>',
                      '<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹3.75 Cr* onwards</li>')
        
        # Table
        c = c.replace('<td style="padding: 14px 16px; color: #fcfbf7;">1,800 – 2,400 Sq.Ft.</td>\n<td style="padding: 14px 16px; color: #c5a059;">G+2 Luxury Villa (FSI 1.5)</td>\n<td style="padding: 14px 16px; color: #b8b8cc;">Polo Arena Frontage</td>\n<td style="padding: 14px 16px; color: #dfc07b; font-weight: 700;">₹1.80 Crore*</td>',
                      '<td style="padding: 14px 16px; color: #fcfbf7;">5,000 Sq.Ft.</td>\n<td style="padding: 14px 16px; color: #c5a059;">G+2 Luxury Villa (FSI 1.5)</td>\n<td style="padding: 14px 16px; color: #b8b8cc;">Racecourse & Polo Frontage</td>\n<td style="padding: 14px 16px; color: #dfc07b; font-weight: 700;">₹3.75 Crore*</td>')
        c = c.replace('₹1.80 Crore*', '₹3.75 Crore*')
        c = c.replace('₹1.80 Cr*', '₹3.75 Cr*')
        
        with open(della_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated della.html")

    # 2. Update racecourse.html
    racecourse_path = os.path.join(PROJECT_DIR, "racecourse.html")
    if os.path.exists(racecourse_path):
        with open(racecourse_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('<p class="price-hint">Plot from 2,000–5,000 sq ft* — Build Your Own Mansion</p>',
                      '<p class="price-hint">Starting from ₹3.75 Cr* with 5,000 sq.ft. plot size — Build Your Own Mansion</p>')
        with open(racecourse_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated racecourse.html")

    # 3. Update masterplan.html
    mp_path = os.path.join(PROJECT_DIR, "masterplan.html")
    if os.path.exists(mp_path):
        with open(mp_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('<span class="price-badge">From ₹1.80 Cr*</span>', '<span class="price-badge">From ₹3.75 Cr*</span>')
        c = c.replace('<span style="color:#ffd88a;">₹1.80 Cr* onwards</span>', '<span style="color:#ffd88a;">₹3.75 Cr* onwards</span>')
        c = c.replace("carpet: '2,000 – 5,000 sq.ft.',\n price: '₹1.80 Cr* onwards',",
                      "carpet: '5,000 sq.ft. Plots',\n price: '₹3.75 Cr* onwards',")
        c = c.replace("and ₹1.80 Crore* for Della villa plots.", "and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.")
        with open(mp_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated masterplan.html")

    # 4. Update hiranandani-price-list-2026.html
    pl_path = os.path.join(PROJECT_DIR, "hiranandani-price-list-2026.html")
    if os.path.exists(pl_path):
        with open(pl_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('Plots ₹1.80Cr*', 'Plots ₹3.75Cr*')
        c = c.replace('Plots ₹1.80 Cr*', 'Plots ₹3.75 Cr*')
        c = c.replace('and ₹1.80 Crore* for Della villa plots.', 'and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.')
        c = c.replace('<div class="stat-number">₹1.80 Cr*</div>', '<div class="stat-number">₹3.75 Cr*</div>')
        c = c.replace('<td style="padding: 16px 20px; color: var(--gold-light);">2,000 - 5,500 sq.ft.</td>\n<td style="padding: 16px 20px; color: var(--gold-bright); font-weight: 700;">₹1.68 Crore</td>\n<td style="padding: 16px 20px; color: #fff; font-weight: 700;">₹1.80 Crore*</td>',
                      '<td style="padding: 16px 20px; color: var(--gold-light);">5,000 sq.ft.</td>\n<td style="padding: 16px 20px; color: var(--gold-bright); font-weight: 700;">₹3.50 Crore</td>\n<td style="padding: 16px 20px; color: #fff; font-weight: 700;">₹3.75 Crore*</td>')
        c = c.replace('<td style="padding: 12px 16px; font-weight: 700; color: #fff;">Della Villa Plots (1,500 - 3,500 sq.ft.)</td>\n<td style="padding: 12px 16px; color: var(--gold-light);">₹1.80 Crore</td>',
                      '<td style="padding: 12px 16px; font-weight: 700; color: #fff;">Della Racecourse Villa Plots (5,000 sq.ft.)</td>\n<td style="padding: 12px 16px; color: var(--gold-light);">₹3.75 Crore*</td>')
        c = c.replace("stats[3].textContent = '₹1.80 Cr*';", "stats[3].textContent = '₹3.75 Cr*';")
        c = c.replace("Custom Della Villa plots start at ₹1.80 Cr*.", "Custom Della Racecourse Villa plots start at ₹3.75 Cr* with 5,000 sq.ft. plot size.")
        with open(pl_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated hiranandani-price-list-2026.html")

    # 5. Update pricing.html
    pr_path = os.path.join(PROJECT_DIR, "pricing.html")
    if os.path.exists(pr_path):
        with open(pr_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('<td>Della Villa Plot — Type A</td>\n<td><span class="sector-tag sector-della">Della</span></td>\n<td>1,800 – 2,400</td>\n<td><span class="price-badge-tag">₹1.80 Cr*</span></td>',
                      '<td>Della Racecourse Villa Plot</td>\n<td><span class="sector-tag sector-della">Della</span></td>\n<td>5,000</td>\n<td><span class="price-badge-tag">₹3.75 Cr*</span></td>')
        c = c.replace('data-name="Della Bespoke Equestrian Villa Plot" data-price="15000000"',
                      'data-name="Della Bespoke Equestrian Villa Plot" data-price="37500000"')
        c = c.replace('<span>Equestrian Estate • ₹1.50 Cr*</span>',
                      '<span>Equestrian Estate • ₹3.75 Cr*</span>')
        with open(pr_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated pricing.html")

    # 6. Update index.html
    idx_path = os.path.join(PROJECT_DIR, "index.html")
    if os.path.exists(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('Plots ₹1.80Cr*', 'Plots ₹3.75Cr*')
        c = c.replace('Plots ₹1.80 Cr*', 'Plots ₹3.75 Cr*')
        c = c.replace('<strong style="color: #dfc07b;">Della Villa Plots:</strong> ₹1.80 Cr*',
                      '<strong style="color: #dfc07b;">Della Villa Plots:</strong> ₹3.75 Cr*')
        c = c.replace('<td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹1.80 Crore*</td>',
                      '<td style="padding: 10px 14px; color: var(--gold-bright); font-weight: 700;">₹3.75 Crore*</td>')
        c = c.replace('<td>1,800 – 2,400 sq. ft.</td>\n<td>G+2 Villa / Mansion</td>\n<td>Della Adventure, Stables, Clubhouse</td>\n<td>₹1.80 Cr* Onwards</td>',
                      '<td>5,000 sq. ft.</td>\n<td>G+2 Villa / Mansion</td>\n<td>Della Adventure, Stables, Clubhouse</td>\n<td>₹3.75 Cr* Onwards</td>')
        c = c.replace('and 3,000 sq.ft. Della equestrian villa plots start at <strong>₹1.80 Crore*</strong>.',
                      'and 5,000 sq.ft. Della racecourse villa plots start at <strong>₹3.75 Crore*</strong>.')
        c = c.replace('<span>Della District • From ₹1.50 Cr*</span>', '<span>Della District • From ₹3.75 Cr* (5,000 sq.ft.)</span>')
        c = c.replace('Custom Della Villa plots start at ₹1.80 Cr*.', 'Custom Della Racecourse Villa plots start at ₹3.75 Cr* with 5,000 sq.ft. plot size.')
        c = c.replace('and ₹1.80 Crore* for Della villa plots.', 'and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.')
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated index.html")

    # 7. Update stories/della-equestrian-villa-plots.html
    story_path = os.path.join(PROJECT_DIR, "stories/della-equestrian-villa-plots.html")
    if os.path.exists(story_path):
        with open(story_path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('<div class="spec-num">₹1.50 Cr*</div>', '<div class="spec-num">₹3.75 Cr*</div>')
        c = c.replace('and ₹1.80 Crore* for Della villa plots.', 'and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.')
        with open(story_path, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print("Updated stories/della-equestrian-villa-plots.html")

    # 8. Update llms.txt, llms-full.txt, ai-facts.json
    for ai_file in ["llms.txt", "llms-full.txt", "ai-facts.json"]:
        p = os.path.join(PROJECT_DIR, ai_file)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                c = f.read()
            c = c.replace('Della Villa Plots from ₹1.80 Crore*', 'Della Racecourse Villa Plots from ₹3.75 Crore* (5,000 sq.ft. plot size)')
            c = c.replace('Villa Plots from ₹1.80 Cr (Della Collection)', 'Villa Plots from ₹3.75 Cr for 5,000 sq.ft. (Della Collection)')
            c = c.replace('Della Villa Plots from ₹1.80Cr*', 'Della Racecourse Villa Plots from ₹3.75Cr* (5,000 sq.ft.)')
            c = c.replace('1,800 sq.ft. plot | ₹1.70 Crore | **₹1.80 Crore\\***', '5,000 sq.ft. plot | ₹3.50 Crore | **₹3.75 Crore\\***')
            c = c.replace('Della Luxury Villa Plots (1,500 - 3,500 sq.ft.): ₹1.80 Crore', 'Della Racecourse Villa Plots (5,000 sq.ft.): ₹3.75 Crore')
            c = c.replace('Della Luxury Villa Plots (1,500 - 3,500 sq.ft.): Starting at ₹1.80 Crore*', 'Della Racecourse Villa Plots (5,000 sq.ft.): Starting at ₹3.75 Crore*')
            c = c.replace('The Della Collection from ₹1.80 Crore', 'The Della Collection from ₹3.75 Crore for 5,000 sq.ft. plots')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            updated_files += 1
            print(f"Updated {ai_file}")

    # 9. Update syndication feeds: rss.xml, atom.xml, google-products.xml, google-merchant-feed.xml, township-press-feed.json
    feed_files = ["rss.xml", "atom.xml", "google-products.xml", "google-merchant-feed.xml", "township-press-feed.json",
                  "public/google-merchant-feed.xml", "public/google-products.xml"]
    for ff in feed_files:
        p = os.path.join(PROJECT_DIR, ff)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                c = f.read()
            c = c.replace('Villa Plots from ₹1.80Cr', 'Villa Plots from ₹3.75Cr (5,000 sq.ft.)')
            c = c.replace('Villa Plots from ₹1.80 Crore', 'Villa Plots from ₹3.75 Crore (5,000 sq.ft.)')
            c = c.replace('Della villa plots from ₹1.80Cr', 'Della racecourse villa plots from ₹3.75Cr (5,000 sq.ft.)')
            c = c.replace('2,000 to 5,000 sq.ft.', '5,000 sq.ft.')
            c = c.replace('1,800 - 5,000 sq.ft.', '5,000 sq.ft.')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            updated_files += 1
            print(f"Updated {ff}")

    # 10. Update all HTML files in explore/, blog/, krisala-hiranandani-township-pune/, krisala-hiranandani-pune/
    patterns = [
        os.path.join(PROJECT_DIR, "explore", "*.html"),
        os.path.join(PROJECT_DIR, "blog", "*.html"),
        os.path.join(PROJECT_DIR, "krisala-hiranandani-township-pune", "*.html"),
        os.path.join(PROJECT_DIR, "krisala-hiranandani-pune", "*.html"),
        os.path.join(PROJECT_DIR, "compare", "*.html"),
        os.path.join(PROJECT_DIR, "*.html")
    ]
    
    html_files = []
    for pat in patterns:
        html_files.extend(glob.glob(pat))
        
    for hf in set(html_files):
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        # Targeted replacements
        content = content.replace("Della Villa Plots | Krisala Hiranandani ₹1.80Cr*", "Della Villa Plots | Krisala Hiranandani ₹3.75Cr*")
        content = content.replace("Della Villa Plots | Krisala Hiranandani ₹1.8Cr*", "Della Villa Plots | Krisala Hiranandani ₹3.75Cr*")
        content = content.replace("Della Resort Plots | Krisala Hiranandani ₹1.8Cr*", "Della Resort Plots | Krisala Hiranandani ₹3.75Cr*")
        content = content.replace("Della Polo Club | Krisala Hiranandani ₹1.8Cr*", "Della Polo Club | Krisala Hiranandani ₹3.75Cr*")
        content = content.replace("Plots ₹1.80Cr*", "Plots ₹3.75Cr*")
        content = content.replace("Plots ₹1.80 Cr*", "Plots ₹3.75 Cr*")
        content = content.replace("and ₹1.80 Crore* for Della villa plots.", "and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.")
        content = content.replace("Custom Della Villa plots start at ₹1.80 Cr*.", "Custom Della Racecourse Villa plots start at ₹3.75 Cr* with 5,000 sq.ft. plot size.")
        content = content.replace("from ₹1.80 Crore*", "from ₹3.75 Crore* (5,000 sq.ft. plot size)")
        content = content.replace("from ₹1.80Cr*", "from ₹3.75Cr* (5,000 sq.ft. plot size)")
        content = content.replace("starting ₹1.80 Crore*", "starting ₹3.75 Crore* (5,000 sq.ft. plot size)")
        content = content.replace("from ₹1.80 Cr*", "from ₹3.75 Cr* (5,000 sq.ft. plot size)")
        
        # When describing Della plots area
        content = content.replace("1,800 to 5,000 sq.ft. plots with views", "5,000 sq.ft. plots with views")
        content = content.replace("1,800-5,000 sq.ft. from ₹1.80Cr*", "5,000 sq.ft. from ₹3.75Cr*")
        content = content.replace("1,800 to 5,000 sq.ft. from ₹1.80Cr*", "5,000 sq.ft. from ₹3.75Cr*")
        content = content.replace("1,800-5,000 sq.ft. at", "5,000 sq.ft. at")
        content = content.replace("1,500-3,500 sq.ft.", "5,000 sq.ft.")
        content = content.replace("1,500, 2,200, and 3,500 sq.ft.", "5,000 sq.ft.")
        
        if content != orig:
            with open(hf, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files += 1

    print(f"Total files updated: {updated_files}")

if __name__ == "__main__":
    run_updates()

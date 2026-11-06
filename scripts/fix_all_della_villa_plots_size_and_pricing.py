#!/usr/bin/env python3
"""
Comprehensive Fix for Della Villa Plots Size and Pricing Across All Files
Target:
- Plot Size: 5,000 sq. ft. (or 5,000 sq.ft.)
- Price: ₹3.75 Cr* Onwards (or ₹3.75 Crore* / ₹3.75 Cr*)
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fix_all():
    updated = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if "node_modules" in root or ".git" in root:
            continue
        for fname in files:
            if not (fname.endswith(".html") or fname.endswith(".json") or fname.endswith(".js") or fname.endswith(".txt") or fname.endswith(".xml")):
                continue
                
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            orig = content
            
            # 1. Exact table row from user screenshot
            content = content.replace("<td>2,000 – 4,500 sq. ft.</td>", "<td>5,000 sq. ft.</td>")
            content = content.replace("<td>1,800 – 4,500 sq.ft.</td>", "<td>5,000 sq.ft.</td>")
            content = content.replace("<td>2,000 – 4,500 sq.ft.</td>", "<td>5,000 sq.ft.</td>")
            content = content.replace("<td>2,000 - 4,500 sq. ft.</td>", "<td>5,000 sq. ft.</td>")
            
            # 2. Indicative starting price
            content = content.replace("<td>₹1.80 Cr* Onwards</td>", "<td>₹3.75 Cr* Onwards</td>")
            content = content.replace("<td>₹1.80 Cr* onwards</td>", "<td>₹3.75 Cr* onwards</td>")
            content = content.replace("<td>₹1.80 Crore*</td>", "<td>₹3.75 Crore*</td>")
            content = content.replace("<td>₹1.80 Crore</td>", "<td>₹3.75 Crore*</td>")
            content = content.replace("<span class=\"price-badge-tag\">₹1.80 Cr*</span>", "<span class=\"price-badge-tag\">₹3.75 Cr*</span>")
            content = content.replace("<span class=\"price-badge-tag\">₹1.80 Crore*</span>", "<span class=\"price-badge-tag\">₹3.75 Crore*</span>")
            content = content.replace("<td style=\"padding: 16px 20px; font-weight: 700; color: var(--gold-bright);\">₹1.80 Cr*</td>",
                                      "<td style=\"padding: 16px 20px; font-weight: 700; color: var(--gold-bright);\">₹3.75 Cr*</td>")
            content = content.replace("<td style=\"padding: 14px 16px; color: #dfc07b; font-weight: 700;\">₹1.80 Crore*</td>",
                                      "<td style=\"padding: 14px 16px; color: #dfc07b; font-weight: 700;\">₹3.75 Crore*</td>")
            content = content.replace("<td style=\"padding: 12px; border: 1px solid rgba(197, 160, 89, 0.2); color: #dfc07b; font-weight: 700;\">₹1.80 Crore*</td>",
                                      "<td style=\"padding: 12px; border: 1px solid rgba(197, 160, 89, 0.2); color: #dfc07b; font-weight: 700;\">₹3.75 Crore*</td>")
            content = content.replace("<td style=\"padding: 10px 14px; color: var(--gold-bright); font-weight: 700;\">₹1.80 Crore*</td>",
                                      "<td style=\"padding: 10px 14px; color: var(--gold-bright); font-weight: 700;\">₹3.75 Crore*</td>")

            # 3. Quick strip / header highlights
            content = content.replace("<strong style=\"color: #dfc07b;\">Della Villa Plots:</strong> ₹1.80 Cr*",
                                      "<strong style=\"color: #dfc07b;\">Della Villa Plots:</strong> ₹3.75 Cr*")
            content = content.replace("Della Villa Plots: ₹1.80 Cr*", "Della Villa Plots: ₹3.75 Cr*")

            # 4. Paragraphs and FAQ answers
            content = content.replace("and ₹1.80 Crore* for Della villa plots.",
                                      "and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots.")
            content = content.replace("and ₹1.80 Crore* for Della villa plots",
                                      "and ₹3.75 Crore* for 5,000 sq.ft. Della racecourse villa plots")
            content = content.replace("and 3,000 sq.ft. Della equestrian villa plots start at <strong>₹1.80 Crore*</strong>.",
                                      "and 5,000 sq.ft. Della racecourse villa plots start at <strong>₹3.75 Crore*</strong>.")
            content = content.replace("and 3,000 sq.ft. Della equestrian villa plots start at ₹1.80 Crore*.",
                                      "and 5,000 sq.ft. Della racecourse villa plots start at ₹3.75 Crore*.")
            content = content.replace("Della villa plots Hinjewadi:</strong> 100 bespoke equestrian resort estates (5,000 sq.ft.) from ₹1.80 Crore",
                                      "Della villa plots Hinjewadi:</strong> 100 bespoke equestrian resort estates (5,000 sq.ft.) from ₹3.75 Crore*")

            # 5. Form options & presets
            content = content.replace('<option value="della-plots">The Della Collection - Villa Plots (₹1.80 Cr*)</option>',
                                      '<option value="della-plots">The Della Collection - 5,000 sq.ft. Villa Plots (₹3.75 Cr*)</option>')
            content = content.replace('<option value="Villa Plot (The Della Collection)">Equestrian Villa Plot (₹1.80 Cr* onwards)</option>',
                                      '<option value="Villa Plot (The Della Collection)">Della Racecourse Villa Plot (₹3.75 Cr* onwards, 5,000 sq.ft.)</option>')
            content = content.replace('setPreset(18000000, this)" type="button">Villa Plot (₹1.80Cr)</button>',
                                      'setPreset(37500000, this)" type="button">Della Villa Plot (₹3.75Cr)</button>')
            content = content.replace('<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹1.80 Cr* onwards</li>',
                                      '<li><i class="ph ph-check gold-icon"></i> <strong>Price Guidance</strong>: ₹3.75 Cr* onwards</li>')

            # 6. NRI tables
            content = content.replace('<tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px; color: var(--gold-light);">1,800 - 3,500 sq.ft.</td><td style="padding: 12px; font-weight: 700; color: #fff;">₹1.80 Crore*</td>',
                                      '<tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px; color: var(--gold-light);">5,000 sq.ft.</td><td style="padding: 12px; font-weight: 700; color: #fff;">₹3.75 Crore*</td>')

            # 7. Functions / Cloudflare workers
            content = content.replace('price: "₹1.80 Cr – ₹3.50 Cr*"', 'price: "₹3.75 Cr* Onwards (5,000 sq.ft.)"')
            content = content.replace('"della-plots": "₹1.80 Cr – ₹3.50 Cr* (~$215,000 – $418,000 USD)"',
                                      '"della-plots": "₹3.75 Cr* Onwards (~$425,000 USD, 5,000 sq.ft.)"')
            content = content.replace("metaTitle = buildCleanTitle(formattedSubject, '₹1.80Cr*');",
                                      "metaTitle = buildCleanTitle(formattedSubject, '₹3.75Cr*');")
            content = content.replace("2,000–5,000 sq.ft. plots with 8-acre", "5,000 sq.ft. plots with 8-acre")

            # 8. Disclaimer
            content = content.replace("₹1.80 Cr*", "₹3.75 Cr*")

            # 9. JSON feeds
            content = content.replace('"price_inr": "₹1.80 Crore*"', '"price_inr": "₹3.75 Crore*"')
            content = content.replace('from ₹1.80 Crore*', 'from ₹3.75 Crore*')
            content = content.replace('from ₹1.80Cr*', 'from ₹3.75Cr*')

            if content != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                updated += 1
                print(f"Updated {fpath}")

    print(f"Successfully updated Della villa plots size & pricing in {updated} files.")

if __name__ == "__main__":
    fix_all()

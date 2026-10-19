#!/usr/bin/env python3
"""
Deploy Global Broad Match Engine
Krisala Hiranandani Township Hinjewadi, Pune
Hardens site for #1 broad match rankings across Google US, UK, UAE, Singapore, Australia, Canada, Europe, and India.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================================================================
# 1. HARDEN hiranandani-pune.html WITH GLOBAL NRI & INTERNATIONAL INVESTOR HUB
# ==============================================================================
hiranandani_pune_file = os.path.join(ROOT_DIR, "hiranandani-pune.html")
with open(hiranandani_pune_file, "r", encoding="utf-8") as f:
    hp_html = f.read()

global_hub_section = """
        <!-- Global NRI & International Investors Corridor (Worldwide Broad Match Target) -->
        <section class="section-py" id="global-nri" style="background: linear-gradient(180deg, var(--bg-dark) 0%, rgba(16,18,26,0.95) 100%); border-top: 1px solid rgba(197, 160, 89, 0.25);">
            <div class="container">
                <div class="section-header center scroll-reveal">
                    <span class="badge-gold">GLOBAL NRI DESK &bull; WORLDWIDE BROAD MATCH CORRIDOR</span>
                    <h2 class="section-title">Hiranandani Pune: Global Real Estate Investment Gateway</h2>
                    <p class="section-subtitle">Dedicated cross-border facilitation for Indian diaspora and global investors across the UAE (Dubai, Abu Dhabi), United States, United Kingdom, Singapore, Australia, and Canada.</p>
                </div>

                <!-- Global Corridors Grid -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 24px; margin-top: 36px;">
                    <!-- Dubai & UAE Corridor -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 24px;" class="scroll-reveal">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                            <span style="font-size: 1.5rem;">🇦🇪</span>
                            <span style="font-size: 0.75rem; background: rgba(197,160,89,0.15); color: var(--gold-bright); padding: 4px 10px; border-radius: 4px; font-weight: 700;">UAE &amp; GCC HUB</span>
                        </div>
                        <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">Dubai &amp; Abu Dhabi NRIs</h3>
                        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">Direct dirham equivalent valuation (AED 328K to 1.1M AED). Dedicated Relationship Manager in Gulf Standard Time (GST), FEMA compliance assistance &amp; zero capital gains repatriation via NRE accounts.</p>
                        <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Starting From:</strong> ~328,000 AED*
                        </div>
                    </div>

                    <!-- USA & Canada Silicon Valley Corridor -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 24px;" class="scroll-reveal">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                            <span style="font-size: 1.5rem;">🇺🇸 🇨🇦</span>
                            <span style="font-size: 0.75rem; background: rgba(197,160,89,0.15); color: var(--gold-bright); padding: 4px 10px; border-radius: 4px; font-weight: 700;">NORTH AMERICA TECH</span>
                        </div>
                        <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">USA &amp; Canada Tech Diaspora</h3>
                        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">Silicon Valley, Seattle, Texas, New York &amp; Toronto NRI corridor. Seamless USD wire transfers, digital KYC, remote Power of Attorney (PoA) execution &amp; virtual 4K architectural walkthroughs.</p>
                        <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Starting From:</strong> ~$89,500 USD*
                        </div>
                    </div>

                    <!-- UK & Europe Corridor -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 24px;" class="scroll-reveal">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                            <span style="font-size: 1.5rem;">🇬🇧 🇪🇺</span>
                            <span style="font-size: 0.75rem; background: rgba(197,160,89,0.15); color: var(--gold-bright); padding: 4px 10px; border-radius: 4px; font-weight: 700;">EUROPE &amp; UK DESK</span>
                        </div>
                        <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">London, UK &amp; Europe Investors</h3>
                        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">DTAA tax credit protection between India &amp; UK/Europe. High 5.2% gross rental yields driven by 400+ Fortune 500 tech multinationals in Hinjewadi Rajiv Gandhi Infotech Park.</p>
                        <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Starting From:</strong> ~£68,500 GBP*
                        </div>
                    </div>

                    <!-- Singapore & Australia Corridor -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 24px;" class="scroll-reveal">
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                            <span style="font-size: 1.5rem;">🇸🇬 🇦🇺</span>
                            <span style="font-size: 0.75rem; background: rgba(197,160,89,0.15); color: var(--gold-bright); padding: 4px 10px; border-radius: 4px; font-weight: 700;">ASIA-PACIFIC CHANNEL</span>
                        </div>
                        <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">Singapore &amp; Australia Channel</h3>
                        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">Dedicated real estate wealth desk for Singapore (SGD) and Sydney/Melbourne (AUD). End-to-end leasing management, rental yield collection &amp; full exit capital repatriation.</p>
                        <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.85rem; color: var(--gold-light);">
                            <strong>Starting From:</strong> ~S$116,000 SGD* / ~A$138,000 AUD*
                        </div>
                    </div>
                </div>

                <!-- Global Investor Benefits Banner -->
                <div style="margin-top: 36px; background: rgba(16,18,26,0.9); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px;">
                    <div>
                        <h4 style="color: var(--gold-bright); margin-bottom: 6px; font-size: 1.1rem;">Ready to Invest from Overseas?</h4>
                        <p style="color: var(--text-muted); font-size: 0.88rem; margin: 0;">Connect directly with our Senior NRI Portfolio Manager on WhatsApp for digital brochures, live video walkthroughs, and customized NRE/NRO payment schedules.</p>
                    </div>
                    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                        <a href="https://wa.me/917744009295?text=Hello%20NRI%20Desk%2C%20I%20am%20inquiring%20about%20Krisala%20Hiranandani%20Township%20from%20overseas." target="_blank" rel="noopener" class="btn-primary" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 22px; text-decoration: none;"><i class="ph ph-whatsapp-logo" style="color: #25D366; font-size: 1.2rem;"></i> WhatsApp Global NRI Desk</a>
                        <a href="/nri" class="btn-secondary" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 22px; text-decoration: none;">Visit Complete NRI Portal</a>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert section if not present
if 'id="global-nri"' not in hp_html:
    hp_html = hp_html.replace('<!-- Chapter 6: Frequently Asked Questions', global_hub_section + '\n        <!-- Chapter 6: Frequently Asked Questions')
    with open(hiranandani_pune_file, "w", encoding="utf-8") as f:
        f.write(hp_html)
    print("Injected Global NRI & International Investor section into hiranandani-pune.html")


# ==============================================================================
# 2. HARDEN hiranandani-price-list-2026.html WITH MULTI-CURRENCY CONVERTER
# ==============================================================================
price_list_file = os.path.join(ROOT_DIR, "hiranandani-price-list-2026.html")
with open(price_list_file, "r", encoding="utf-8") as f:
    pl_html = f.read()

currency_switcher_html = """
                <!-- Global Multi-Currency Conversion Controls -->
                <div style="margin-top: 28px; background: rgba(16,18,26,0.85); border: 1px solid rgba(197,160,89,0.3); border-radius: 10px; padding: 18px 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px;">
                    <div>
                        <span style="color: var(--gold-bright); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: block;">International NRI Currency Switcher</span>
                        <p style="color: var(--text-muted); font-size: 0.82rem; margin: 4px 0 0 0;">View real-time indicative prices in Indian Rupee, US Dollar, UAE Dirham, British Pound, Euro, or Singapore Dollar.</p>
                    </div>
                    <div id="currencySelector" style="display: flex; flex-wrap: wrap; gap: 8px;">
                        <button type="button" class="curr-btn active" data-curr="INR" style="background: var(--gold-primary); color: #000; border: none; padding: 7px 14px; border-radius: 4px; font-weight: 700; font-size: 0.82rem; cursor: pointer;">INR (₹)</button>
                        <button type="button" class="curr-btn" data-curr="USD" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 7px 14px; border-radius: 4px; font-weight: 600; font-size: 0.82rem; cursor: pointer;">USD ($)</button>
                        <button type="button" class="curr-btn" data-curr="AED" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 7px 14px; border-radius: 4px; font-weight: 600; font-size: 0.82rem; cursor: pointer;">AED (د.إ)</button>
                        <button type="button" class="curr-btn" data-curr="GBP" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 7px 14px; border-radius: 4px; font-weight: 600; font-size: 0.82rem; cursor: pointer;">GBP (£)</button>
                        <button type="button" class="curr-btn" data-curr="EUR" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 7px 14px; border-radius: 4px; font-weight: 600; font-size: 0.82rem; cursor: pointer;">EUR (€)</button>
                        <button type="button" class="curr-btn" data-curr="SGD" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 7px 14px; border-radius: 4px; font-weight: 600; font-size: 0.82rem; cursor: pointer;">SGD (S$)</button>
                    </div>
                </div>
"""

# Multi-currency static reference table for international bots & search engines
currency_static_table = """
                <!-- Static Global Broad Match Price Table (Indexed by Search Engines Worldwide) -->
                <div style="margin-top: 36px; background: rgba(255,255,255,0.02); border: 1px solid rgba(197,160,89,0.25); border-radius: 10px; padding: 24px;">
                    <h3 style="color: var(--gold-bright); font-size: 1.15rem; margin-bottom: 12px;">Global NRI Price Benchmark (USD, AED, GBP, EUR, SGD)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; margin-bottom: 20px;">For international Indian homebuyers and overseas property investors, here is the official all-inclusive starting price conversion table across key foreign currencies:</p>
                    <div style="overflow-x: auto;">
                        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.88rem;">
                            <thead>
                                <tr style="background: rgba(197,160,89,0.1); border-bottom: 1px solid var(--gold-primary);">
                                    <th style="padding: 12px 16px; color: var(--gold-bright);">Configuration</th>
                                    <th style="padding: 12px 16px; color: #fff;">INR Price</th>
                                    <th style="padding: 12px 16px; color: #fff;">USD ($) Approx.</th>
                                    <th style="padding: 12px 16px; color: #fff;">UAE Dirham (AED)</th>
                                    <th style="padding: 12px 16px; color: #fff;">UK Pound (£)</th>
                                    <th style="padding: 12px 16px; color: #fff;">Singapore (SGD)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">2 BHK Smart Luxury (740 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹79.00 Lakhs</td>
                                    <td style="padding: 12px 16px; color: #fff;">$89,500 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">328,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£68,500 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$116,000 SGD</td>
                                </tr>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">2 BHK Grande (820 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹88.00 Lakhs</td>
                                    <td style="padding: 12px 16px; color: #fff;">$99,500 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">365,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£76,500 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$129,500 SGD</td>
                                </tr>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">3 BHK Imperial (1,020 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹1.25 Crore</td>
                                    <td style="padding: 12px 16px; color: #fff;">$141,500 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">518,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£108,500 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$183,500 SGD</td>
                                </tr>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">3 BHK Racecourse View (1,180 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹1.45 Crore</td>
                                    <td style="padding: 12px 16px; color: #fff;">$164,000 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">601,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£126,000 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$213,000 SGD</td>
                                </tr>
                                <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">4 BHK Sky Duplex (1,850 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹2.10 Crore</td>
                                    <td style="padding: 12px 16px; color: #fff;">$237,500 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">871,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£182,500 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$308,000 SGD</td>
                                </tr>
                                <tr>
                                    <td style="padding: 12px 16px; font-weight: 700; color: #fff;">Della Villa Plots (1,500 - 3,500 sq.ft.)</td>
                                    <td style="padding: 12px 16px; color: var(--gold-light);">₹1.80 Crore</td>
                                    <td style="padding: 12px 16px; color: #fff;">$203,500 USD</td>
                                    <td style="padding: 12px 16px; color: #fff;">746,000 AED</td>
                                    <td style="padding: 12px 16px; color: #fff;">£156,500 GBP</td>
                                    <td style="padding: 12px 16px; color: #fff;">S$264,500 SGD</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
"""

# Multi-currency client-side switcher JS
currency_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var rates = {
        'INR': { symbol: '₹', rate: 1, suffix: ' Lakhs', crSuffix: ' Cr' },
        'USD': { symbol: '$', rate: 0.00113, suffix: 'K', crSuffix: 'K' },
        'AED': { symbol: 'AED ', rate: 0.00415, suffix: 'K', crSuffix: 'K' },
        'GBP': { symbol: '£', rate: 0.00087, suffix: 'K', crSuffix: 'K' },
        'EUR': { symbol: '€', rate: 0.00104, suffix: 'K', crSuffix: 'K' },
        'SGD': { symbol: 'S$', rate: 0.00147, suffix: 'K', crSuffix: 'K' }
    };
    var currBtns = document.querySelectorAll('#currencySelector .curr-btn');
    currBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            currBtns.forEach(function(b) {
                b.classList.remove('active');
                b.style.background = 'rgba(255,255,255,0.08)';
                b.style.color = '#fff';
            });
            this.classList.add('active');
            this.style.background = 'var(--gold-primary)';
            this.style.color = '#000';
            var selected = this.getAttribute('data-curr');
            // update stats
            var stats = document.querySelectorAll('.hero-stats .stat-number');
            if (stats.length >= 4) {
                if (selected === 'INR') {
                    stats[0].textContent = '₹79 L*';
                    stats[1].textContent = '₹1.25 Cr*';
                    stats[2].textContent = '₹2.10 Cr*';
                    stats[3].textContent = '₹1.80 Cr*';
                } else if (selected === 'USD') {
                    stats[0].textContent = '$89.5K*';
                    stats[1].textContent = '$141.5K*';
                    stats[2].textContent = '$237.5K*';
                    stats[3].textContent = '$203.5K*';
                } else if (selected === 'AED') {
                    stats[0].textContent = '328K AED*';
                    stats[1].textContent = '518K AED*';
                    stats[2].textContent = '871K AED*';
                    stats[3].textContent = '746K AED*';
                } else if (selected === 'GBP') {
                    stats[0].textContent = '£68.5K*';
                    stats[1].textContent = '£108.5K*';
                    stats[2].textContent = '£182.5K*';
                    stats[3].textContent = '£156.5K*';
                } else if (selected === 'EUR') {
                    stats[0].textContent = '€82.0K*';
                    stats[1].textContent = '€130.0K*';
                    stats[2].textContent = '€218.0K*';
                    stats[3].textContent = '€187.0K*';
                } else if (selected === 'SGD') {
                    stats[0].textContent = 'S$116K*';
                    stats[1].textContent = 'S$183.5K*';
                    stats[2].textContent = 'S$308K*';
                    stats[3].textContent = 'S$264.5K*';
                }
            }
        });
    });
});
</script>
"""

if 'id="currencySelector"' not in pl_html:
    pl_html = pl_html.replace('<div style="overflow-x: auto; margin-top: 36px;', currency_switcher_html + '\n                <div style="overflow-x: auto; margin-top: 36px;')
    pl_html = pl_html.replace('</table>\n                </div>', '</table>\n                </div>\n' + currency_static_table)
    pl_html = pl_html.replace('</body>', currency_js + '\n</body>')
    with open(price_list_file, "w", encoding="utf-8") as f:
        f.write(pl_html)
    print("Injected Multi-Currency Switcher and Static International Matrix into hiranandani-price-list-2026.html")


# ==============================================================================
# 3. ENRICH llms.txt & llms-full.txt WITH GLOBAL BROAD MATCH KNOWLEDGE GRAPH
# ==============================================================================
llms_file = os.path.join(ROOT_DIR, "llms.txt")
with open(llms_file, "r", encoding="utf-8") as f:
    llms_content = f.read()

global_llm_section = """
## Global Broad Match & International NRI Real Estate Knowledge Graph
- Target International Jurisdictions: United Arab Emirates (Dubai, Abu Dhabi, Sharjah), United States (California / Bay Area, Texas, New York, Seattle), United Kingdom (London, Midlands), Singapore, Australia (Sydney, Melbourne), Canada (Toronto, Vancouver), and Europe.
- Currency Valuation Matrix:
  - 2 BHK Smart Luxury (740 sq.ft.): ₹79 Lakhs | ~$89,500 USD | ~328,000 AED | ~£68,500 GBP | ~S$116,000 SGD
  - 2 BHK Grande (820 sq.ft.): ₹88 Lakhs | ~$99,500 USD | ~365,000 AED | ~£76,500 GBP | ~S$129,500 SGD
  - 3 BHK Imperial (1,020 sq.ft.): ₹1.25 Crore | ~$141,500 USD | ~518,000 AED | ~£108,500 GBP | ~S$183,500 SGD
  - 3 BHK Colosseum Racecourse View (1,180 sq.ft.): ₹1.45 Crore | ~$164,000 USD | ~601,000 AED | ~£126,000 GBP | ~S$213,000 SGD
  - 4 BHK Sky Duplex / Penthouse (1,850 sq.ft.): ₹2.10 Crore | ~$237,500 USD | ~871,000 AED | ~£182,500 GBP | ~S$308,000 SGD
  - Della Luxury Villa Plots (1,500 - 3,500 sq.ft.): ₹1.80 Crore | ~$203,500 USD | ~746,000 AED | ~£156,500 GBP | ~S$264,500 SGD
- Repatriation & Legal Compliance: 100% principal & capital appreciation repatriation permissible under RBI/FEMA regulations via designated NRE / NRO bank accounts. Zero capital gains taxation under reciprocal DTAA treaties.
- Developer Entity Authority: Joint venture between Hiranandani Communities (championed by Dr. Niranjan Hiranandani) and Krisala Developers.
- Canonical International Desk: https://krisalahiranandanitownships.com/nri
"""

if "Global Broad Match" not in llms_content:
    llms_content += "\n" + global_llm_section.strip() + "\n"
    with open(llms_file, "w", encoding="utf-8") as f:
        f.write(llms_content)
    print("Enriched llms.txt with Global Broad Match Knowledge Graph.")

llms_full_file = os.path.join(ROOT_DIR, "llms-full.txt")
if os.path.exists(llms_full_file):
    with open(llms_full_file, "r", encoding="utf-8") as f:
        llms_full_content = f.read()
    if "Global Broad Match" not in llms_full_content:
        llms_full_content += "\n" + global_llm_section.strip() + "\n"
        with open(llms_full_file, "w", encoding="utf-8") as f:
            f.write(llms_full_content)
        print("Enriched llms-full.txt with Global Broad Match Knowledge Graph.")

print("\nDeployment of Global Broad Match Engine Completed Successfully.")

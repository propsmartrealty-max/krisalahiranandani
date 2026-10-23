#!/usr/bin/env python3
"""
Global NRI Hubs Programmatic Generator
Krisala Hiranandani Township Hinjewadi, Pune

Generates 6 physical, high-authority regional NRI landing hubs in /nri/:
1. /nri/dubai-uae (UAE / Dubai / Abu Dhabi)
2. /nri/usa-silicon-valley (USA / Silicon Valley / Texas / Seattle / NY)
3. /nri/uk-london (UK / London / Manchester)
4. /nri/singapore (Singapore / Asia-Pacific)
5. /nri/australia-sydney (Australia / Sydney / Melbourne)
6. /nri/canada-toronto (Canada / Toronto / Vancouver)

Hardened with reciprocal international hreflang links, multi-currency pricing,
FEMA/DTAA regulatory guidance, and Schema.org JSON-LD graphs.
"""

import os
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NRI_DIR = os.path.join(ROOT_DIR, "nri")
os.makedirs(NRI_DIR, exist_ok=True)

TEMPLATE_PATH = os.path.join(ROOT_DIR, "programmatic-template.html")
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    TEMPLATE_CONTENT = f.read()

HREFLANG_BLOCK = """
    <!-- Reciprocal International Hreflang Network -->
    <link rel="alternate" hreflang="x-default" href="https://krisalahiranandanitownships.com/nri" />
    <link rel="alternate" hreflang="en-IN" href="https://krisalahiranandanitownships.com/nri" />
    <link rel="alternate" hreflang="en-AE" href="https://krisalahiranandanitownships.com/nri/dubai-uae" />
    <link rel="alternate" hreflang="ar-AE" href="https://krisalahiranandanitownships.com/nri/dubai-uae" />
    <link rel="alternate" hreflang="en-US" href="https://krisalahiranandanitownships.com/nri/usa-silicon-valley" />
    <link rel="alternate" hreflang="en-GB" href="https://krisalahiranandanitownships.com/nri/uk-london" />
    <link rel="alternate" hreflang="en-SG" href="https://krisalahiranandanitownships.com/nri/singapore" />
    <link rel="alternate" hreflang="en-AU" href="https://krisalahiranandanitownships.com/nri/australia-sydney" />
    <link rel="alternate" hreflang="en-CA" href="https://krisalahiranandanitownships.com/nri/canada-toronto" />
"""

GLOBAL_NRI_HUBS = [
    {
        "slug": "dubai-uae",
        "title": "Buy Property in Pune from Dubai UAE | Krisala Hiranandani NRI Desk (AED)",
        "description": "Official UAE & Dubai NRI Desk for Krisala Hiranandani Township Hinjewadi, Pune. Seamless AED investments from د.إ 348,000*, 8.4% rental yields, zero tax in UAE, FEMA compliance & remote POA.",
        "keywords": "buy property in pune from dubai, krisala hiranandani nri investment dubai, uae nri property investment pune, hiranandani flats pune aed price, nri real estate desk uae",
        "h1": "Invest in Pune's Flagship Neoclassical Township from Dubai & UAE",
        "subtitle": "Tax-free AED wealth allocation into 105+ acres in North Hinjewadi with 8.4% gross rental yields and direct Pune-Dubai flight connectivity starting from AED 348,000*.",
        "badge": "OFFICIAL UAE & DUBAI NRI DESK • CURRENCY: AED (د.إ)",
        "breadcrumb": "Dubai UAE NRI Desk",
        "currency_code": "AED",
        "low_price": "348000",
        "high_price": "1800000",
        "editorial": """
            <p>For Non-Resident Indians across <strong>Dubai, Abu Dhabi, Sharjah, and the GCC</strong>, investing in Indian real estate is an essential hedge against inflation and a foundational pillar of generational wealth. <strong>Krisala Hiranandani Township in North Hinjewadi, Pune</strong> represents the premier institutional-grade investment destination.</p>
            <p>Benefiting from the stability of the UAE Dirham (pegged to the USD), UAE investors achieve an immediate purchasing power advantage. With direct flights connecting <strong>Dubai International (DXB) to Pune International Airport (PNQ)</strong> in just 3 hours and 15 minutes, overseeing your asset is as effortless as a weekend trip.</p>
            <h3>Strategic Investment Privileges for UAE Buyers</h3>
            <ul>
                <li><strong>Tax-Free Returns:</strong> Zero income tax on rental yields or capital gains in the UAE, fortified by the Indo-UAE Double Tax Avoidance Agreement (DTAA)</li>
                <li><strong>High Rental Yields:</strong> Strong 8.4% projected gross rental yield fueled by multinational tech executives from Infosys, TCS, and Wipro</li>
                <li><strong>Remote Digital Execution:</strong> End-to-end digital KYC, video site walkthroughs, and consular Power of Attorney (POA) assistance in Dubai and Abu Dhabi</li>
                <li><strong>100% Repatriation:</strong> Complete FEMA compliance with transparent capital and rental repatriation through NRE/NRO bank accounts</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in AED (د.إ)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">AED 348,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">AED 550,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">AED 925,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">AED 792,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">3h 15m</div><div style="font-size: 0.85rem; color: #fff;">DXB to Pune Flight</div><div style="font-size: 0.75rem; color: var(--text-muted);">Direct Non-Stop Route</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Gross Rental Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">Hinjewadi Tech Corridor</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">100%</div><div style="font-size: 0.85rem; color: #fff;">FEMA Repatriation</div><div style="font-size: 0.75rem; color: var(--text-muted);">NRE Banking Approved</div></div>
            </div>
        """,
        "faqs": [
            ("Can UAE residents and NRIs purchase residential property in Krisala Hiranandani without RBI permission?", "Yes, under general permission granted by the Reserve Bank of India (RBI), NRIs and OCIs residing in the UAE can acquire unlimited residential properties without needing special approvals."),
            ("How does capital gains taxation work between India and the UAE?", "Under the India-UAE Double Tax Avoidance Agreement (DTAA), capital gains on immovable property situated in India are taxable in India, while remaining entirely tax-free in the UAE. Tax treaty relief ensures no double taxation."),
            ("How do I execute property booking and registration from Dubai?", "Our dedicated UAE NRI desk facilitates digital booking, virtual walkthroughs, remote agreement review, and legal Power of Attorney (POA) registration attested through the Indian Consulate in Dubai or VFS Global.")
        ]
    },
    {
        "slug": "usa-silicon-valley",
        "title": "Buy Property in Pune from USA | Krisala Hiranandani NRI Desk (USD)",
        "description": "Official US NRI Investment Desk for Krisala Hiranandani Township Hinjewadi. USD rates starting $95,000*, favorable USD/INR exchange rate, 8.4% rental yields, FEMA & IRS Form 8938 compliance.",
        "keywords": "buy flat in pune from usa, us tech nri property investment pune, krisala hiranandani usd price, bay area nri property pune, fema compliant property pune",
        "h1": "High-Yield Real Estate Investment in Pune for US Tech Professionals",
        "subtitle": "Leverage historical USD/INR exchange arbitrage into 105+ acres in North Hinjewadi. 8.4% tech executive rental yields & 100% NRE capital repatriation starting at $95,000*.",
        "badge": "OFFICIAL USA NRI DESK • CURRENCY: USD ($)",
        "breadcrumb": "USA Silicon Valley Desk",
        "currency_code": "USD",
        "low_price": "95000",
        "high_price": "450000",
        "editorial": """
            <p>For Indian technology professionals and executives residing across <strong>Silicon Valley (San Francisco/San Jose), Seattle, Texas (Dallas/Austin), and New Jersey</strong>, Pune's Hinjewadi is recognized as India's premier counterpart to US tech corridors. <strong>Krisala Hiranandani Township</strong> offers an ideal institutional-grade residential asset combining iconic neoclassical architecture with world-class amenities.</p>
            <p>With the USD trading at favorable levels against the INR ($1 = ~₹83-84), US buyers benefit from an immediate <strong>18-22% valuation arbitrage</strong>. Senior technology managers at Google, Apple, Microsoft, Amazon, and Meta are allocating equity into West Pune to secure both inflation-beating capital growth and strong passive rental streams.</p>
            <h3>US Investor Advantages & Tax Governance</h3>
            <ul>
                <li><strong>Exchange Rate Arbitrage:</strong> Maximize dollar purchasing power with pre-launch pricing on 2, 3, and 4 BHK residences starting at $95,000*</li>
                <li><strong>FBAR &amp; FATCA Transparency:</strong> Seamless documentation compliant with US IRS Form 8938 and foreign bank account reporting (FBAR)</li>
                <li><strong>Pre-Approved US Dollar Remittances:</strong> Direct wire transfers via SWIFT into project-specific MahaRERA escrow accounts</li>
                <li><strong>Dedicated Property Management:</strong> Full lifecycle tenant management, lease renewals, and direct rental credit into NRE accounts</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in USD ($)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">$95,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">$150,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">$252,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">$216,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">$95K</div><div style="font-size: 0.85rem; color: #fff;">Entry Level 2 BHK</div><div style="font-size: 0.75rem; color: var(--text-muted);">Sector Arcadia Luxury</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Rental Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">Tech Executive Tenancy</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">100%</div><div style="font-size: 0.85rem; color: #fff;">NRE Repatriation</div><div style="font-size: 0.75rem; color: var(--text-muted);">FBAR & FATCA Ready</div></div>
            </div>
        """,
        "faqs": [
            ("Can US citizens and Green Card holders legally purchase property in Krisala Hiranandani?", "Yes, US citizens of Indian origin holding OCI cards as well as Indian passport holders (NRIs) have unrestricted statutory rights under the Foreign Exchange Management Act (FEMA) to acquire residential property in India."),
            ("How is rental income treated for US tax reporting (IRS Form 1040)?", "Rental income earned from Indian property is reported on Schedule E of your US Form 1040. Under the US-India Tax Treaty, taxes paid in India can be claimed as a Foreign Tax Credit (FTC) via IRS Form 1116, preventing double taxation."),
            ("Can US buyers avail of home loans from Indian banks?", "Yes, premier Indian financial institutions including State Bank of India (SBI) and HDFC Bank offer NRI home loans up to 80% loan-to-value with tenure up to 20 years, serviceable directly via US dollar remittances.")
        ]
    },
    {
        "slug": "uk-london",
        "title": "Buy Property in Pune from UK London | Krisala Hiranandani NRI Desk (GBP)",
        "description": "Official UK & London NRI Investment Desk for Krisala Hiranandani Hinjewadi, Pune. Starting from £75,000*, DTAA tax safeguards, 8.4% rental yields, and bespoke neoclassical architecture.",
        "keywords": "buy property in pune from uk, london nri property investment pune, krisala hiranandani gbp price, uk nri buy flats hinjewadi, dtaa india uk property tax",
        "h1": "Neoclassical Integrated Living in Pune for UK & London NRI Investors",
        "subtitle": "Institutional-grade capital allocation starting £75,000*. High rental yields and full legal repatriation under Indo-UK Double Taxation Treaty.",
        "badge": "OFFICIAL UK & LONDON NRI DESK • CURRENCY: GBP (£)",
        "breadcrumb": "UK London Desk",
        "currency_code": "GBP",
        "low_price": "75000",
        "high_price": "360000",
        "editorial": """
            <p>For British Indians and NRI professionals residing in <strong>London, Manchester, Birmingham, and across the United Kingdom</strong>, <strong>Krisala Hiranandani Township</strong> offers an exquisite blend of British-European neoclassical architectural heritage and modern high-tech convenience in Pune.</p>
            <p>Designed under the master vision of Dr. Niranjan Hiranandani, the 105+ acre township features grand Greco-Roman colonnades, Corinthian capitals, manicured classical gardens, and India's first 8-acre turf racecourse. Starting at just <strong>£75,000*</strong>, it offers unmatched value compared to prohibitive prime London real estate.</p>
            <h3>Advantages for UK-Based Investors</h3>
            <ul>
                <li><strong>Indo-UK Double Taxation Treaty:</strong> Seamless tax credits ensure that taxes paid in India are fully offset against UK HMRC obligations</li>
                <li><strong>Superior Yield Profile:</strong> 8.4% gross rental yield in Hinjewadi vs 2.8-3.2% in central London residential property</li>
                <li><strong>Hassle-Free Consular POA:</strong> Execute binding legal deeds through the High Commission of India in London or Consulates in Birmingham and Edinburgh</li>
                <li><strong>MahaRERA Consumer Protection:</strong> 70% mandatory escrow safeguards guarantee timely delivery and structural warranties</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in GBP (£)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">£75,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">£118,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">£199,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">£170,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">£75K</div><div style="font-size: 0.85rem; color: #fff;">Entry Level Price</div><div style="font-size: 0.75rem; color: var(--text-muted);">Sector Arcadia 2 BHK</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Gross Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">3x Central London Yield</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">DTAA</div><div style="font-size: 0.85rem; color: #fff;">Tax Protected</div><div style="font-size: 0.75rem; color: var(--text-muted);">HMRC Offset Compliant</div></div>
            </div>
        """,
        "faqs": [
            ("Can British passport holders with OCI cards buy apartments in Krisala Hiranandani?", "Yes, Overseas Citizens of India (OCI) holding British citizenship enjoy identical property ownership rights as Indian citizens under FEMA regulations."),
            ("How does HMRC tax rental income received from property in Pune?", "Under the UK-India Double Taxation Convention, Indian withholding tax (TDS) paid on rental income is credited against UK income tax liability via Foreign Tax Credit Relief in your Self-Assessment tax return."),
            ("How can UK buyers repatriate sale proceeds back to their UK bank accounts?", "Sale proceeds can be repatriated up to $1 million USD per financial year through authorized dealer banks under FEMA Form 15CA and 15CB certification.")
        ]
    },
    {
        "slug": "singapore",
        "title": "Buy Property in Pune from Singapore | Krisala Hiranandani NRI Desk (SGD)",
        "description": "Singapore NRI Investment Desk for Krisala Hiranandani Township Hinjewadi, Pune. SGD rates from S$125,000*, 8.4% gross rental yields, 5-hour direct flight corridor, and full FEMA compliance.",
        "keywords": "buy property in pune from singapore, singapore nri property investment pune, krisala hiranandani sgd price, buy flats in hinjewadi from singapore, nri property desk singapore",
        "h1": "Premier Pune Property Investment for Singapore NRIs & OCIs",
        "subtitle": "Smart diversification into Pune's fastest growing tech corridor starting S$125,000*. High-yield neoclassical master township with 8-acre racecourse.",
        "badge": "OFFICIAL SINGAPORE NRI DESK • CURRENCY: SGD (S$)",
        "breadcrumb": "Singapore NRI Desk",
        "currency_code": "SGD",
        "low_price": "125000",
        "high_price": "600000",
        "editorial": """
            <p>For Indian finance and tech executives based in <strong>Singapore (Marina Bay, Changi, Jurong, One-North)</strong>, investing in high-yield Indian real estate provides an essential diversification strategy away from Singapore's restrictive property cooling measures and high Additional Buyer's Stamp Duty (ABSD).</p>
            <p>Located on the PMRDA 128m Ring Road in North Hinjewadi, <strong>Krisala Hiranandani Township</strong> offers a self-contained 105+ acre integrated neoclassical ecosystem. With convenient direct flight corridors between <strong>Singapore Changi (SIN) and Pune International (PNQ)</strong>, maintaining a premier real estate foothold in Western India has never been simpler.</p>
            <h3>Key Benefits for Singapore-Based Investors</h3>
            <ul>
                <li><strong>No ABSD Penalties:</strong> Allocate capital freely into Indian real estate without punitive Singapore buyer stamp duty surcharges</li>
                <li><strong>Compounded Appreciation:</strong> West Pune's IT infrastructure expansion delivers projected 12-15% annual capital appreciation</li>
                <li><strong>Streamlined Digital Conveyancing:</strong> Digital reservation, electronic documentation, and remote Power of Attorney attestation via High Commission of India in Singapore</li>
                <li><strong>Full Currency Repatriation:</strong> 100% legal capital and dividend repatriation under RBI &amp; FEMA guidelines directly into Singapore bank accounts</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in SGD (S$)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">S$ 125,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">S$ 198,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">S$ 333,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">S$ 285,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">5 Hours</div><div style="font-size: 0.85rem; color: #fff;">Singapore to Pune</div><div style="font-size: 0.75rem; color: var(--text-muted);">Direct Flight Corridor</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">0% ABSD</div><div style="font-size: 0.85rem; color: #fff;">No Singapore Surcharges</div><div style="font-size: 0.75rem; color: var(--text-muted);">Full Indian Property Rights</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Gross Rental Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">Premium Hinjewadi Demand</div></div>
            </div>
        """,
        "faqs": [
            ("Can Singapore permanent residents and OCIs invest in Della villa plots?", "Yes, OCIs and NRIs are fully permitted to buy demarcated Non-Agricultural (NA) residential plots and apartments in India under FEMA guidelines."),
            ("How does the Singapore-India Double Taxation Avoidance Agreement work?", "Under the Singapore-India DTAA, taxes paid in India on capital gains and rental income can be claimed as a tax credit against Inland Revenue Authority of Singapore (IRAS) tax assessments."),
            ("What payment schedules are available for Singapore buyers?", "We offer flexible 20:80 bank-approved payment plans as well as customized milestone schedules linked to Mivan monolithic construction progress.")
        ]
    },
    {
        "slug": "australia-sydney",
        "title": "Buy Property in Pune from Australia | Krisala Hiranandani NRI Desk (AUD)",
        "description": "Official Australia & Sydney NRI Desk for Krisala Hiranandani Hinjewadi, Pune. Starting A$145,000*, high 8.4% rental yields, Indo-Aus DTAA benefits, and 105-acre equestrian master township.",
        "keywords": "buy property in pune from australia, sydney melbourne nri property investment pune, krisala hiranandani aud price, buy flat in hinjewadi from australia, australian nri real estate pune",
        "h1": "Invest in Pune's Master Neoclassical Township from Australia",
        "subtitle": "Bespoke residential assets in North Hinjewadi starting A$145,000*. High rental yield, zero stamp duty surcharges, and direct NRE repatriation.",
        "badge": "OFFICIAL AUSTRALIA & SYDNEY NRI DESK • CURRENCY: AUD (A$)",
        "breadcrumb": "Australia Sydney Desk",
        "currency_code": "AUD",
        "low_price": "145000",
        "high_price": "700000",
        "editorial": """
            <p>For Australian NRIs and OCIs residing in <strong>Sydney, Melbourne, Brisbane, and Perth</strong>, high residential entry prices and strict mortgage stress tests in Australia make Pune real estate an exceptionally attractive diversification avenue.</p>
            <p><strong>Krisala Hiranandani Township</strong> provides Australian buyers with institutional security, MahaRERA compliance, and an equestrian master lifestyle modeled on the world's most prestigious gated townships. Starting from <strong>A$ 145,000*</strong>, it offers steady 8.4% gross rental yields from Hinjewadi tech corridor executives.</p>
            <h3>Australia Investor Highlights</h3>
            <ul>
                <li><strong>Indo-Australia DTAA Protection:</strong> Avoid double taxation with foreign income tax offsets recognized by the Australian Taxation Office (ATO)</li>
                <li><strong>No FIRB Surcharges:</strong> Australian foreign investment fees do not apply to your property acquisitions in India</li>
                <li><strong>VFS / Consular Attestation:</strong> Simple remote Power of Attorney attestation via Indian Consulates in Sydney, Melbourne, and Perth</li>
                <li><strong>Institutional Bank Approvals:</strong> Backed by State Bank of India (Sydney branch) and HDFC Bank with attractive interest rates</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in AUD (A$)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">A$ 145,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">A$ 230,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">A$ 386,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">A$ 331,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">A$ 145K</div><div style="font-size: 0.85rem; color: #fff;">Entry Level Price</div><div style="font-size: 0.75rem; color: var(--text-muted);">Sector Arcadia 2 BHK</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Gross Rental Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">High Tech Tenancy</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">ATO Offset</div><div style="font-size: 0.85rem; color: #fff;">DTAA Protection</div><div style="font-size: 0.75rem; color: var(--text-muted);">Indo-Australian Treaty</div></div>
            </div>
        """,
        "faqs": [
            ("Can Australian citizens of Indian origin (OCIs) acquire property in Krisala Hiranandani?", "Yes, Australian citizens holding OCI status have unrestricted rights to purchase residential real estate and plots in India under FEMA guidelines."),
            ("How does the Australian Taxation Office (ATO) treat foreign rental income?", "Foreign rental income must be declared on your Australian tax return, but you can claim a Foreign Income Tax Offset (FITO) for taxes paid in India under the Indo-Australian DTAA, avoiding double taxation."),
            ("How do I repatriate the sale proceeds back to Australia?", "Funds can be repatriated to your Australian bank account through your Indian NRE bank account under RBI Form 15CA and 15CB certification up to $1 million USD per year.")
        ]
    },
    {
        "slug": "canada-toronto",
        "title": "Buy Property in Pune from Canada | Krisala Hiranandani NRI Desk (CAD)",
        "description": "Official Canada & Toronto NRI Investment Desk for Krisala Hiranandani Hinjewadi, Pune. Starting from C$130,000*, high rental yields (8.4%), CRA reporting compliance & remote POA.",
        "keywords": "buy property in pune from canada, toronto vancouver nri property investment pune, krisala hiranandani cad price, canadian nri buy flat hinjewadi, cra foreign property reporting india",
        "h1": "Institutional Real Estate Wealth in Pune for Canadian NRIs",
        "subtitle": "Invest in Pune's 105-acre equestrian neoclassical township from Toronto & Vancouver starting C$130,000*. CRA-compliant, high rental yields.",
        "badge": "OFFICIAL CANADA & TORONTO NRI DESK • CURRENCY: CAD (C$)",
        "breadcrumb": "Canada Toronto Desk",
        "currency_code": "CAD",
        "low_price": "130000",
        "high_price": "620000",
        "editorial": """
            <p>For Indo-Canadians residing in the <strong>Greater Toronto Area (GTA), Vancouver, Calgary, and Ottawa</strong>, rapid home price escalation and stringent stress tests in Canada highlight the enormous upside of investing back home in Pune's fastest growing tech corridor.</p>
            <p><strong>Krisala Hiranandani Township</strong> offers Canadian investors institutional transparency, MahaRERA escrow protections, and timeless neoclassical architecture. Starting at <strong>C$ 130,000*</strong>, residences command robust 8.4% gross rental yields from senior engineers at Infosys, Wipro, and TCS.</p>
            <h3>Canadian NRI Investor Benefits</h3>
            <ul>
                <li><strong>Canada-India Tax Convention:</strong> Full Foreign Tax Credit (FTC) recognition by the Canada Revenue Agency (CRA)</li>
                <li><strong>CRA Form T1135 Compliance:</strong> Clear, auditable documentation making annual foreign reporting seamless</li>
                <li><strong>Remote Consular Attestation:</strong> Power of Attorney authenticated via High Commission of India in Ottawa or Consulates in Toronto and Vancouver</li>
                <li><strong>Strong Currency Leverage:</strong> Favorable Canadian Dollar to Indian Rupee exchange rates maximize real estate square footage</li>
            </ul>
        """,
        "spec_table": """
            <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; color: #fff;">
                <tr style="border-bottom: 1px solid rgba(197,160,89,0.3); background: rgba(197,160,89,0.1);"><th style="padding: 12px; text-align: left;">Typology</th><th style="padding: 12px; text-align: left;">Carpet Area</th><th style="padding: 12px; text-align: left;">Price in CAD (C$)*</th><th style="padding: 12px; text-align: left;">Price in INR (₹)*</th><th style="padding: 12px; text-align: left;">Projected Annual Yield</th></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">2 BHK Smart Luxury (Arcadia)</td><td style="padding: 12px;">740 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">C$ 130,000*</td><td style="padding: 12px;">₹79 Lakhs*</td><td style="padding: 12px;">8.4% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">3 BHK Royale (The Colosseum)</td><td style="padding: 12px;">1,020 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">C$ 206,000*</td><td style="padding: 12px;">₹1.25 Crore*</td><td style="padding: 12px;">8.2% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">4 BHK Sky Duplex (Sector Icon)</td><td style="padding: 12px;">1,850 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">C$ 346,000*</td><td style="padding: 12px;">₹2.10 Crore*</td><td style="padding: 12px;">7.8% p.a.</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 12px;">Della Equestrian Villa Plot</td><td style="padding: 12px;">2,000 Sq.Ft.</td><td style="padding: 12px; color: var(--gold-bright); font-weight: 700;">C$ 297,000*</td><td style="padding: 12px;">₹1.80 Crore*</td><td style="padding: 12px;">High Capital Growth</td></tr>
            </table>
        """,
        "commute": """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">C$ 130K</div><div style="font-size: 0.85rem; color: #fff;">Entry Level Price</div><div style="font-size: 0.75rem; color: var(--text-muted);">Sector Arcadia 2 BHK</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">8.4%</div><div style="font-size: 0.85rem; color: #fff;">Gross Rental Yield</div><div style="font-size: 0.75rem; color: var(--text-muted);">Hinjewadi IT Demand</div></div>
                <div style="background: rgba(255,255,255,0.03); padding: 18px; border-radius: 8px; border: 1px solid rgba(197,160,89,0.2);"><div style="color: var(--gold-bright); font-size: 1.4rem; font-weight: 700;">CRA Ready</div><div style="font-size: 0.85rem; color: #fff;">Form T1135 Compliant</div><div style="font-size: 0.75rem; color: var(--text-muted);">Canada-India Tax Treaty</div></div>
            </div>
        """,
        "faqs": [
            ("Can Canadian citizens and permanent residents buy property in Krisala Hiranandani?", "Yes, Canadian passport holders with OCI registration as well as Indian passport holders (NRIs) can legally acquire residential apartments and plots in India."),
            ("How does the CRA tax rental income earned in India?", "Under the Canada-India Income Tax Convention, Canadian tax residents must report global rental income on their T1 return, but can claim a Foreign Tax Credit (FTC) on Form T2209 for taxes paid to Indian tax authorities."),
            ("Can Canadian NRIs secure home loans from Indian banks?", "Yes, SBI, HDFC, and ICICI Bank offer pre-approved home loan facilities for Canadian NRIs with up to 80% financing and tenure up to 20 years.")
        ]
    }
]

def render_hub(config):
    html = TEMPLATE_CONTENT
    canonical_url = f"https://krisalahiranandanitownships.com/nri/{config['slug']}"

    # Replace Metadata
    html = html.replace('<title id="seoTitle">Krisala Hiranandani Township Hinjewadi | Official Guide</title>',
                        f'<title>{config["title"]}</title>')
    html = re.sub(r'<meta\s+name=["\']description["\']\s+id=["\']seoDesc["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta name="description" id="seoDesc" content="{config["description"]}">', html)
    html = re.sub(r'<meta\s+name=["\']keywords["\']\s+id=["\']seoKeywords["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta name="keywords" id="seoKeywords" content="{config["keywords"]}">', html)
    html = re.sub(r'<link\s+rel=["\']canonical["\']\s+id=["\']seoCanonical["\']\s+href=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<link rel="canonical" id="seoCanonical" href="{canonical_url}" />\n{HREFLANG_BLOCK}', html)

    # Replace OG & Twitter Tags
    html = re.sub(r'<meta\s+property=["\']og:title["\']\s+id=["\']ogTitle["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta property="og:title" id="ogTitle" content="{config["title"]}">', html)
    html = re.sub(r'<meta\s+property=["\']og:url["\']\s+id=["\']ogUrl["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta property="og:url" id="ogUrl" content="{canonical_url}">', html)
    html = re.sub(r'<meta\s+property=["\']og:description["\']\s+id=["\']ogDesc["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta property="og:description" id="ogDesc" content="{config["description"]}">', html)

    html = re.sub(r'<meta\s+name=["\']twitter:title["\']\s+id=["\']twTitle["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta name="twitter:title" id="twTitle" content="{config["title"]}">', html)
    html = re.sub(r'<meta\s+name=["\']twitter:description["\']\s+id=["\']twDesc["\']\s+content=["\'][^"\']+["\']\s*/?>',
                  lambda m: f'<meta name="twitter:description" id="twDesc" content="{config["description"]}">', html)

    # Replace Hero & Content
    html = re.sub(r'<span class="badge" id="seoBadge".*?</span>',
                  lambda m: f'<span class="badge" id="seoBadge" style="margin-bottom: 16px;"><i class="ph ph-globe-hemisphere-east"></i> {config["badge"]}</span>', html, flags=re.DOTALL)
    html = re.sub(r'<h1 id="seoH1".*?</h1>',
                  lambda m: f'<h1 id="seoH1" style="font-size: clamp(2rem, 4vw, 3.2rem); font-family: var(--font-heading); color: #fff; line-height: 1.2; margin-bottom: 15px;">{config["h1"]}</h1>', html, flags=re.DOTALL)
    html = re.sub(r'<p id="seoSubtitle".*?</p>',
                  lambda m: f'<p id="seoSubtitle" style="font-size: 1.15rem; color: var(--text-muted); max-width: 800px; margin: 0 auto 25px; line-height: 1.6;">{config["subtitle"]}</p>', html, flags=re.DOTALL)
    
    html = re.sub(r'<div id="seoBreadcrumbs".*?</div>',
                  lambda m: f'<div id="seoBreadcrumbs" style="font-size: 0.85rem; color: var(--gold-light); margin-bottom: 12px; letter-spacing: 0.5px;"><a href="/" style="color:var(--text-muted); text-decoration:none;">Home</a> &bull; <a href="/nri" style="color:var(--text-muted); text-decoration:none;">NRI Desk</a> &bull; <span>{config["breadcrumb"]}</span></div>', html, flags=re.DOTALL)

    html = re.sub(r'<div id="seoEditorialBody".*?</div>',
                  lambda m: f'<div id="seoEditorialBody" style="font-size: 1.05rem; line-height: 1.8; color: #e6e6f0;">{config["editorial"]}</div>', html, flags=re.DOTALL)
    
    html = re.sub(r'<div id="seoSpecTable".*?</div>',
                  lambda m: f'<div id="seoSpecTable" style="overflow-x: auto; margin: 30px 0;">{config["spec_table"]}</div>', html, flags=re.DOTALL)

    html = re.sub(r'<div id="seoCommuteMatrix".*?</div>',
                  lambda m: f'<div id="seoCommuteMatrix" style="margin: 30px 0;">{config["commute"]}</div>', html, flags=re.DOTALL)

    # Render FAQs
    faq_html = '<div class="faq-container">'
    for q, a in config["faqs"]:
        faq_html += f"""
        <div class="faq-item" style="background: rgba(16,18,26,0.8); border: 1px solid rgba(197,160,89,0.25); border-radius: 8px; margin-bottom: 14px; padding: 20px;">
            <h3 style="font-family: var(--font-heading); color: #fff; font-size: 1.15rem; margin-bottom: 8px;">{q}</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">{a}</p>
        </div>
        """
    faq_html += '</div>'
    html = re.sub(r'<div id="seoFaqAccordion".*?</div>',
                  lambda m: f'<div id="seoFaqAccordion">{faq_html}</div>', html, flags=re.DOTALL)

    # Schema JSON-LD
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{canonical_url}#webpage",
                "url": canonical_url,
                "name": config["title"],
                "description": config["description"],
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://krisalahiranandanitownships.com/"},
                        {"@type": "ListItem", "position": 2, "name": "NRI Desk", "item": "https://krisalahiranandanitownships.com/nri"},
                        {"@type": "ListItem", "position": 3, "name": config["breadcrumb"], "item": canonical_url}
                    ]
                }
            },
            {
                "@type": "FinancialProduct",
                "name": f"Krisala Hiranandani NRI Investment Desk ({config['currency_code']})",
                "description": config["description"],
                "url": canonical_url,
                "feesAndCommissionsSpecification": "Zero Developer Brokerage, Direct Channel Partner Mandate",
                "annualPercentageRate": "8.4"
            },
            {
                "@type": "RealEstateListing",
                "name": config["h1"],
                "description": config["description"],
                "url": canonical_url,
                "offers": {
                    "@type": "AggregateOffer",
                    "priceCurrency": config["currency_code"],
                    "lowPrice": config["low_price"],
                    "highPrice": config["high_price"]
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}
                    } for q, a in config["faqs"]
                ]
            }
        ]
    }
    schema_json_str = f'<script type="application/ld+json" id="seoSchemaJson">\n{json.dumps(schema_data, indent=2)}\n</script>'
    html = re.sub(r'<script type="application/ld\+json" id="seoSchemaJson">.*?</script>',
                  lambda m: schema_json_str, html, flags=re.DOTALL)

    return html

def main():
    print("=" * 70)
    print("Generating Global NRI Regional Hubs")
    print(f"Target Count: {len(GLOBAL_NRI_HUBS)} Regional Portals")
    print("=" * 70)

    for hub in GLOBAL_NRI_HUBS:
        dest_file = os.path.join(NRI_DIR, f"{hub['slug']}.html")
        rendered = render_hub(hub)
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"[✓] Generated: /nri/{hub['slug']}")

    print("=" * 70)
    print("Global NRI Generation Complete.")
    print("=" * 70)

if __name__ == "__main__":
    main()

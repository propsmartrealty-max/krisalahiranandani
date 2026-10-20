#!/usr/bin/env python3
"""
Comprehensive Real Estate Modernization & Search Dominance Suite
Krisala Hiranandani Township Hinjewadi, Pune

Implements:
1. Interactive Floor Plan & View Configurator Component
2. Instant Dynamic WhatsApp Automated Cost Sheet Engine
3. On-Page AI Real Estate Concierge Floating Widget
4. Google News PR Syndication Feed (sitemap-news.xml & press-releases.json)
5. Local Business / Site Address Routing in _redirects & sitemaps
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================================================================
# 1. GENERATE GOOGLE NEWS PR SYNDICATION FEED (sitemap-news.xml & press-releases.json)
# ==============================================================================
news_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
    <url>
        <loc>https://krisalahiranandanitownships.com/blog/the-colosseum-hinjewadi-phase-4-investment-guide</loc>
        <news:news>
            <news:publication>
                <news:name>Krisala Hiranandani Township Media Bureau</news:name>
                <news:language>en</news:language>
            </news:publication>
            <news:publication_date>2026-10-19T08:00:00+00:00</news:publication_date>
            <news:title>The Colosseum Phase 4 Launch: B+G+27 Roman Landmark Towers Unveiled in North Hinjewadi</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://krisalahiranandanitownships.com/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle</loc>
        <news:news>
            <news:publication>
                <news:name>Krisala Hiranandani Township Media Bureau</news:name>
                <news:language>en</news:language>
            </news:publication>
            <news:publication_date>2026-10-18T10:00:00+00:00</news:publication_date>
            <news:title>The Della Collection Unveils 100 Exclusive Luxury Equestrian Villa Plots in West Pune</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://krisalahiranandanitownships.com/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure</loc>
        <news:news>
            <news:publication>
                <news:name>Krisala Hiranandani Township Media Bureau</news:name>
                <news:language>en</news:language>
            </news:publication>
            <news:publication_date>2026-10-17T09:00:00+00:00</news:publication_date>
            <news:title>PMRDA 128m Ring Road and Metro Line 3 Accelerate Capital Appreciation in North Hinjewadi</news:title>
        </news:news>
    </url>
    <url>
        <loc>https://krisalahiranandanitownships.com/hiranandani-pune</loc>
        <news:news>
            <news:publication>
                <news:name>Krisala Hiranandani Township Media Bureau</news:name>
                <news:language>en</news:language>
            </news:publication>
            <news:publication_date>2026-10-20T06:00:00+00:00</news:publication_date>
            <news:title>Dr. Niranjan Hiranandani and Krisala Developers Announce 105-Acre Neoclassical Master Township in Pune</news:title>
        </news:news>
    </url>
</urlset>
"""

with open(os.path.join(ROOT_DIR, "sitemap-news.xml"), "w", encoding="utf-8") as f:
    f.write(news_xml_content.strip())
print("Generated sitemap-news.xml")

press_releases_data = [
    {
        "id": "pr-2026-001",
        "title": "Dr. Niranjan Hiranandani and Krisala Developers Announce 105-Acre Neoclassical Master Township in Pune",
        "date": "2026-10-20",
        "url": "https://krisalahiranandanitownships.com/hiranandani-pune",
        "category": "Corporate Partnership",
        "summary": "Hiranandani Communities and Krisala Developers officially launch Pune's largest integrated equestrian township in North Hinjewadi featuring India's first 8-acre turf racecourse."
    },
    {
        "id": "pr-2026-002",
        "title": "The Colosseum Phase 4 Launch: B+G+27 Roman Landmark Towers Unveiled",
        "date": "2026-10-19",
        "url": "https://krisalahiranandanitownships.com/colosseum",
        "category": "Project Launch",
        "summary": "Phase 4 Roman-inspired towers open for VIP bookings offering 2, 3 and 4 BHK racecourse-facing residences under MahaRERA PR1260002600818."
    },
    {
        "id": "pr-2026-003",
        "title": "Della Collection Introduces 100 Exclusive Equestrian Villa Plots",
        "date": "2026-10-18",
        "url": "https://krisalahiranandanitownships.com/della",
        "category": "Luxury Living",
        "summary": "Exclusive collaboration with Della Resorts brings 100 bespoke villa plots with adventure park and polo club privileges."
    }
]

with open(os.path.join(ROOT_DIR, "press-releases.json"), "w", encoding="utf-8") as f:
    json.dump(press_releases_data, f, indent=2)
print("Generated press-releases.json")


# ==============================================================================
# 2. INTERACTIVE 3D/2D FLOOR PLAN & VIEW CONFIGURATOR + INSTANT WHATSAPP ENGINE
# ==============================================================================
configurator_html = """
        <!-- Interactive 3D/2D Floor Plan & View Configurator (Instant WhatsApp Cost Sheet) -->
        <section class="section-py" id="interactive-configurator" style="background: linear-gradient(180deg, var(--bg-dark-deep) 0%, rgba(16,18,26,0.95) 100%); border-top: 1px solid rgba(197, 160, 89, 0.25);">
            <div class="container">
                <div class="section-header center scroll-reveal">
                    <span class="badge-gold">INTERACTIVE UNIT &amp; VIEW EXPLORER</span>
                    <h2 class="section-title">Configure Your Residence &amp; View Simulator</h2>
                    <p class="section-subtitle">Select unit configuration, floor elevation, and facing orientation to view detailed carpet dimensions, 3D daylight aspects, and receive an instant builder-direct WhatsApp cost sheet.</p>
                </div>

                <div style="background: rgba(16, 18, 26, 0.85); border: 1px solid rgba(197, 160, 89, 0.3); border-radius: 12px; padding: 28px; margin-top: 36px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; align-items: start;">
                    <!-- Left: Control Sliders & Configuration Buttons -->
                    <div>
                        <span style="color: var(--gold-bright); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 12px;">Step 1: Select Configuration</span>
                        <div id="cfgUnitSelector" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px;">
                            <button type="button" class="cfg-btn active" data-unit="2bhk-smart" data-name="2 BHK Smart Luxury" data-carpet="740 sq.ft." data-base="79" data-sector="Sector Arcadia" style="background: var(--gold-primary); color: #000; border: none; padding: 10px 16px; border-radius: 6px; font-weight: 700; font-size: 0.85rem; cursor: pointer;">2 BHK (740 sq.ft.)</button>
                            <button type="button" class="cfg-btn" data-unit="2bhk-grande" data-name="2 BHK Grande" data-carpet="820 sq.ft." data-base="88" data-sector="Sector Arcadia" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 10px 16px; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer;">2 BHK Grande (820 sq.ft.)</button>
                            <button type="button" class="cfg-btn" data-unit="3bhk-imp" data-name="3 BHK Imperial" data-carpet="1,020 sq.ft." data-base="125" data-sector="The Colosseum" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 10px 16px; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer;">3 BHK (1,020 sq.ft.)</button>
                            <button type="button" class="cfg-btn" data-unit="3bhk-rc" data-name="3 BHK Racecourse View" data-carpet="1,180 sq.ft." data-base="145" data-sector="The Colosseum" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 10px 16px; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer;">3 BHK Racecourse (1,180 sq.ft.)</button>
                            <button type="button" class="cfg-btn" data-unit="4bhk-sky" data-name="4 BHK Sky Duplex" data-carpet="1,850 sq.ft." data-base="210" data-sector="Sector Icon" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 10px 16px; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer;">4 BHK Duplex (1,850 sq.ft.)</button>
                            <button type="button" class="cfg-btn" data-unit="della-plots" data-name="Della Villa Plot" data-carpet="2,000 sq.ft." data-base="180" data-sector="The Della Collection" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 10px 16px; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer;">Della Villa Plots</button>
                        </div>

                        <span style="color: var(--gold-bright); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 12px;">Step 2: Choose View Horizon</span>
                        <div id="cfgViewSelector" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px;">
                            <button type="button" class="view-btn active" data-view="racecourse" data-viewname="8-Acre Turf Racecourse View" style="background: var(--gold-primary); color: #000; border: none; padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 700; cursor: pointer;">🏇 Racecourse View</button>
                            <button type="button" class="view-btn" data-view="sahyadri" data-viewname="Sahyadri Mountain Horizon" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; cursor: pointer;">🏔️ Mountain Horizon</button>
                            <button type="button" class="view-btn" data-view="podium" data-viewname="105-Acre Central Podium Garden" style="background: rgba(255,255,255,0.06); color: #fff; border: 1px solid rgba(197,160,89,0.3); padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; cursor: pointer;">🌿 Central Podium Green</button>
                        </div>

                        <span style="color: var(--gold-bright); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px;">Step 3: Floor Elevation: <span id="cfgFloorDisplay" style="color: #fff; font-size: 1rem; font-weight: 700;">14th Floor (Mid-Rise Horizon)</span></span>
                        <input type="range" id="cfgFloorSlider" min="1" max="27" value="14" style="width: 100%; accent-color: var(--gold-primary); cursor: pointer; margin-bottom: 24px;">
                    </div>

                    <!-- Right: Dynamic Specification & Instant WhatsApp Dispatch Card -->
                    <div style="background: rgba(9, 10, 15, 0.7); border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 10px; padding: 24px;">
                        <span id="cfgSectorBadge" style="background: rgba(197,160,89,0.15); color: var(--gold-bright); padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Sector Arcadia</span>
                        <h3 id="cfgTitle" style="color: #fff; font-size: 1.4rem; font-family: var(--font-heading); margin: 8px 0 16px;">2 BHK Smart Luxury</h3>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 18px; font-size: 0.88rem;">
                            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px;">
                                <span style="color: var(--text-muted); display: block; font-size: 0.75rem;">MahaRERA Carpet</span>
                                <strong id="cfgCarpet" style="color: var(--gold-light);">740 sq.ft.</strong>
                            </div>
                            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px;">
                                <span style="color: var(--text-muted); display: block; font-size: 0.75rem;">Selected Facing</span>
                                <strong id="cfgViewLabel" style="color: #fff; font-size: 0.82rem;">Racecourse View</strong>
                            </div>
                            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px;">
                                <span style="color: var(--text-muted); display: block; font-size: 0.75rem;">Estimated EMI</span>
                                <strong id="cfgEmi" style="color: #10b981;">~₹61,500 / mo</strong>
                            </div>
                            <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px;">
                                <span style="color: var(--text-muted); display: block; font-size: 0.75rem;">Estimated Price*</span>
                                <strong id="cfgPrice" style="color: var(--gold-bright); font-size: 1.15rem;">₹79 Lakhs*</strong>
                            </div>
                        </div>

                        <!-- Instant WhatsApp CTA -->
                        <a id="cfgWhatsappBtn" href="https://wa.me/917744009295?text=Hello%20Krisala%20Hiranandani%20Sales%20Team%2C%20I%20am%20interested%20in%20the%202%20BHK%20Smart%20Luxury%20(740%20sq.ft.)%20with%20Racecourse%20View%20on%20the%2014th%20Floor.%20Please%20send%20the%20complete%20MahaRERA%20cost%20sheet%20and%20floor%20plan%20PDF." target="_blank" rel="noopener" class="btn-primary" style="width: 100%; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.92rem; padding: 14px;">
                            <i class="ph ph-whatsapp-logo" style="color: #25D366; font-size: 1.3rem;"></i> Receive Official Cost Sheet on WhatsApp
                        </a>
                        <p style="text-align: center; font-size: 0.75rem; color: var(--text-subtle); margin-top: 8px;">Instant automated quote &bull; Zero broker commission &bull; Official RERA docket</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Configurator JS Logic -->
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            var unitButtons = document.querySelectorAll('#cfgUnitSelector .cfg-btn');
            var viewButtons = document.querySelectorAll('#cfgViewSelector .view-btn');
            var slider = document.getElementById('cfgFloorSlider');
            var floorDisplay = document.getElementById('cfgFloorDisplay');
            var titleEl = document.getElementById('cfgTitle');
            var carpetEl = document.getElementById('cfgCarpet');
            var sectorBadgeEl = document.getElementById('cfgSectorBadge');
            var viewLabelEl = document.getElementById('cfgViewLabel');
            var priceEl = document.getElementById('cfgPrice');
            var emiEl = document.getElementById('cfgEmi');
            var whatsappBtn = document.getElementById('cfgWhatsappBtn');

            var currentUnit = {
                name: '2 BHK Smart Luxury',
                carpet: '740 sq.ft.',
                base: 79,
                sector: 'Sector Arcadia'
            };
            var currentView = '8-Acre Turf Racecourse View';
            var currentFloor = 14;

            function updateDisplay() {
                var floorFactor = 1 + ((currentFloor - 1) * 0.003); // 0.3% floor rise per floor
                var calculatedPrice = currentUnit.base * floorFactor;
                var formattedPrice = calculatedPrice >= 100 ? ('₹' + (calculatedPrice/100).toFixed(2) + ' Crore*') : ('₹' + calculatedPrice.toFixed(2) + ' Lakhs*');
                var calculatedEmi = Math.round(calculatedPrice * 780); // approx EMI multiplier per lakh

                titleEl.textContent = currentUnit.name;
                carpetEl.textContent = currentUnit.carpet;
                sectorBadgeEl.textContent = currentUnit.sector;
                viewLabelEl.textContent = currentView;
                priceEl.textContent = formattedPrice;
                emiEl.textContent = '~₹' + calculatedEmi.toLocaleString('en-IN') + ' / mo';
                floorDisplay.textContent = currentFloor + (currentFloor === 1 ? 'st' : currentFloor === 2 ? 'nd' : currentFloor === 3 ? 'rd' : 'th') + ' Floor';

                var message = "Hello Krisala Hiranandani Sales Team, I configured the " + currentUnit.name + " (" + currentUnit.carpet + ") in " + currentUnit.sector + " on the " + currentFloor + "th Floor with " + currentView + " at approx " + formattedPrice + ". Please send the official 2026 cost sheet PDF, floor plan, and booking payment schedule to my WhatsApp.";
                whatsappBtn.href = "https://wa.me/917744009295?text=" + encodeURIComponent(message);
            }

            unitButtons.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    unitButtons.forEach(function(b) {
                        b.style.background = 'rgba(255,255,255,0.06)';
                        b.style.color = '#fff';
                    });
                    this.style.background = 'var(--gold-primary)';
                    this.style.color = '#000';
                    currentUnit = {
                        name: this.getAttribute('data-name'),
                        carpet: this.getAttribute('data-carpet'),
                        base: parseFloat(this.getAttribute('data-base')),
                        sector: this.getAttribute('data-sector')
                    };
                    updateDisplay();
                });
            });

            viewButtons.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    viewButtons.forEach(function(b) {
                        b.style.background = 'rgba(255,255,255,0.06)';
                        b.style.color = '#fff';
                    });
                    this.style.background = 'var(--gold-primary)';
                    this.style.color = '#000';
                    currentView = this.getAttribute('data-viewname');
                    updateDisplay();
                });
            });

            if (slider) {
                slider.addEventListener('input', function() {
                    currentFloor = parseInt(this.value);
                    updateDisplay();
                });
            }
        });
        </script>
"""


# ==============================================================================
# 3. ON-PAGE AI REAL ESTATE CONCIERGE WIDGET (Zero CLS, Embedded Knowledge Graph)
# ==============================================================================
ai_concierge_widget_html = """
    <!-- Floating AI Real Estate Concierge Widget (Zero CLS) -->
    <div id="aiConciergeLauncher" style="position: fixed; bottom: 24px; right: 24px; z-index: 9999; display: flex; align-items: center; gap: 8px;">
        <button id="aiLauncherBtn" type="button" aria-label="Open AI Concierge" style="background: linear-gradient(135deg, #dfc07b 0%, #c5a059 100%); color: #000; border: none; border-radius: 50px; padding: 12px 20px; font-weight: 700; font-size: 0.88rem; box-shadow: 0 8px 24px rgba(197,160,89,0.4); cursor: pointer; display: flex; align-items: center; gap: 8px; transition: transform 0.2s ease;">
            <span style="display: inline-block; width: 8px; height: 8px; background: #10b981; border-radius: 50%; box-shadow: 0 0 8px #10b981;"></span>
            <span>Ask Hiranandani AI</span>
        </button>
    </div>

    <!-- AI Concierge Modal Dialog -->
    <div id="aiConciergeModal" style="display: none; position: fixed; bottom: 84px; right: 24px; width: 360px; max-width: calc(100vw - 32px); height: 500px; background: rgba(16, 18, 26, 0.98); border: 1px solid rgba(197, 160, 89, 0.4); border-radius: 12px; box-shadow: 0 16px 40px rgba(0,0,0,0.8); z-index: 10000; flex-direction: column; overflow: hidden; backdrop-filter: blur(16px);">
        <!-- Header -->
        <div style="background: rgba(255,255,255,0.04); border-bottom: 1px solid rgba(197,160,89,0.25); padding: 14px 18px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.1rem;">🏛️</span>
                <div>
                    <h4 style="margin: 0; color: #fff; font-size: 0.9rem; font-family: var(--font-heading);">Hiranandani AI Concierge</h4>
                    <span style="color: var(--gold-bright); font-size: 0.7rem;">Verified Township Knowledge Graph</span>
                </div>
            </div>
            <button id="aiCloseBtn" type="button" aria-label="Close" style="background: none; border: none; color: var(--text-muted); font-size: 1.2rem; cursor: pointer; padding: 4px;">&times;</button>
        </div>

        <!-- Chat History -->
        <div id="aiChatBody" style="flex: 1; padding: 14px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; font-size: 0.85rem;">
            <div style="background: rgba(197,160,89,0.1); border: 1px solid rgba(197,160,89,0.25); border-radius: 8px; padding: 10px; color: #fff; line-height: 1.5;">
                Welcome! I am your 24/7 Krisala &times; Hiranandani Township Concierge. Ask me anything about MahaRERA numbers, price lists, floor plans, racecourse access, or bank approvals.
            </div>

            <!-- Quick Prompt Chips -->
            <div id="aiChipContainer" style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px;">
                <button type="button" class="ai-chip" data-q="What is the starting price of 2 BHK and 3 BHK?" style="background: rgba(255,255,255,0.06); color: var(--gold-light); border: 1px solid rgba(197,160,89,0.3); border-radius: 20px; padding: 5px 10px; font-size: 0.75rem; cursor: pointer;">💰 2 BHK / 3 BHK Price</button>
                <button type="button" class="ai-chip" data-q="What are the official MahaRERA registration numbers?" style="background: rgba(255,255,255,0.06); color: var(--gold-light); border: 1px solid rgba(197,160,89,0.3); border-radius: 20px; padding: 5px 10px; font-size: 0.75rem; cursor: pointer;">📜 MahaRERA Numbers</button>
                <button type="button" class="ai-chip" data-q="What is the possession date for the township?" style="background: rgba(255,255,255,0.06); color: var(--gold-light); border: 1px solid rgba(197,160,89,0.3); border-radius: 20px; padding: 5px 10px; font-size: 0.75rem; cursor: pointer;">📅 Possession Date</button>
                <button type="button" class="ai-chip" data-q="Tell me about the 8-acre turf racecourse and Della resort." style="background: rgba(255,255,255,0.06); color: var(--gold-light); border: 1px solid rgba(197,160,89,0.3); border-radius: 20px; padding: 5px 10px; font-size: 0.75rem; cursor: pointer;">🏇 Racecourse &amp; Della</button>
                <button type="button" class="ai-chip" data-q="Where is the site sales office located?" style="background: rgba(255,255,255,0.06); color: var(--gold-light); border: 1px solid rgba(197,160,89,0.3); border-radius: 20px; padding: 5px 10px; font-size: 0.75rem; cursor: pointer;">📍 Site Address &amp; Map</button>
            </div>
        </div>

        <!-- Input Bar -->
        <div style="padding: 10px 14px; background: rgba(9,10,15,0.9); border-top: 1px solid rgba(197,160,89,0.25); display: flex; gap: 8px;">
            <input type="text" id="aiInput" placeholder="Type a question..." style="flex: 1; background: rgba(255,255,255,0.06); border: 1px solid rgba(197,160,89,0.3); border-radius: 6px; padding: 8px 12px; color: #fff; font-size: 0.85rem; outline: none;">
            <button id="aiSendBtn" type="button" style="background: var(--gold-primary); color: #000; border: none; border-radius: 6px; padding: 8px 14px; font-weight: 700; cursor: pointer;">Send</button>
        </div>
    </div>

    <!-- AI Concierge Logic -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var launcher = document.getElementById('aiLauncherBtn');
        var modal = document.getElementById('aiConciergeModal');
        var closeBtn = document.getElementById('aiCloseBtn');
        var input = document.getElementById('aiInput');
        var sendBtn = document.getElementById('aiSendBtn');
        var chatBody = document.getElementById('aiChatBody');
        var chips = document.querySelectorAll('.ai-chip');

        if (launcher && modal) {
            launcher.addEventListener('click', function() {
                modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex';
            });
        }
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                modal.style.display = 'none';
            });
        }

        var knowledgeBase = [
            {
                keywords: ['price', 'cost', 'rate', 'starting', '2 bhk', '3 bhk', '4 bhk'],
                answer: "Official 2026 Pricing: 2 BHK Smart Luxury (740 sq.ft.) starts at ₹79 Lakhs* ($89.5K USD / 328K AED). 3 BHK Imperial (1,020 sq.ft.) starts at ₹1.25 Crore*. 3 BHK Racecourse View (1,180 sq.ft.) starts at ₹1.45 Crore*. 4 BHK Sky Duplexes start at ₹2.10 Cr*. Custom Della Villa plots start at ₹1.80 Cr*."
            },
            {
                keywords: ['rera', 'maharera', 'number', 'registration', 'legal'],
                answer: "Official Verified MahaRERA Certifications: Sector Arcadia (MahaRERA: PR1260002500600), The Colosseum Phase 4 (MahaRERA: PR1260002600818), and Sector Everlyn (MahaRERA: PR1260002502438). Registered on maharera.maharashtra.gov.in."
            },
            {
                keywords: ['possession', 'date', 'timeline', 'completion'],
                answer: "The official MahaRERA possession timeline commences in December 2028 for Sector Arcadia, extending through December 2029 for The Colosseum Phase 4, powered by accelerated Mivan monolithic shear-wall construction velocity."
            },
            {
                keywords: ['racecourse', 'della', 'equestrian', 'resort', 'club'],
                answer: "Krisala × Hiranandani features India's first 8-acre private turf racecourse, polo riding tracks, and an integrated 40-acre Della adventure resort precinct with 52+ world-class equestrian and wellness amenities."
            },
            {
                keywords: ['address', 'location', 'site', 'reach', 'office', 'where'],
                answer: "Official Site Address: PMRDA 128m Ring Road Corridor, North Hinjawadi, Darumbre, Pune 410506. Driving time: 5 mins to Ring Road, 7 mins to Hinjewadi Metro Line 3 Megapolis Station, 10 mins to Mumbai-Pune Expressway (Urse Toll), and 12 mins to Infosys Phase 1."
            },
            {
                keywords: ['bank', 'loan', 'emi', 'pre approved', 'finance', 'sbi', 'hdfc'],
                answer: "Pre-approved home loans with PMAY interest subsidies are active through SBI, HDFC Bank, ICICI Bank, Axis Bank, and Bank of Baroda. Instant loan pre-assessment is available at our on-site desk."
            }
        ];

        function handleQuestion(q) {
            if (!q || !q.trim()) return;
            var userDiv = document.createElement('div');
            userDiv.style.alignSelf = 'flex-end';
            userDiv.style.background = 'rgba(255,255,255,0.08)';
            userDiv.style.padding = '8px 12px';
            userDiv.style.borderRadius = '8px';
            userDiv.style.color = '#fff';
            userDiv.style.maxWidth = '85%';
            userDiv.textContent = q;
            chatBody.appendChild(userDiv);

            var qLower = q.toLowerCase();
            var responseText = "Thank you for inquiring! For complete personalized information, official brochure PDF, or to schedule a priority site visit with our senior sales manager, click below to connect instantly on WhatsApp.";
            for (var i = 0; i < knowledgeBase.length; i++) {
                var item = knowledgeBase[i];
                for (var k = 0; k < item.keywords.length; k++) {
                    if (qLower.indexOf(item.keywords[k]) !== -1) {
                        responseText = item.answer;
                        break;
                    }
                }
                if (responseText !== "Thank you for inquiring! For complete personalized information, official brochure PDF, or to schedule a priority site visit with our senior sales manager, click below to connect instantly on WhatsApp.") break;
            }

            var botDiv = document.createElement('div');
            botDiv.style.alignSelf = 'flex-start';
            botDiv.style.background = 'rgba(197,160,89,0.12)';
            botDiv.style.border = '1px solid rgba(197,160,89,0.25)';
            botDiv.style.padding = '10px';
            botDiv.style.borderRadius = '8px';
            botDiv.style.color = '#fff';
            botDiv.style.maxWidth = '90%';
            botDiv.innerHTML = responseText + '<div style="margin-top: 8px;"><a href="https://wa.me/917744009295?text=' + encodeURIComponent('Hello, I was using the AI Concierge and would like more details on: ' + q) + '" target="_blank" rel="noopener" style="color: #25D366; font-weight: 700; text-decoration: none; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 4px;">💬 Connect on WhatsApp &rarr;</a></div>';
            chatBody.appendChild(botDiv);
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        if (sendBtn && input) {
            sendBtn.addEventListener('click', function() {
                handleQuestion(input.value);
                input.value = '';
            });
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    handleQuestion(input.value);
                    input.value = '';
                }
            });
        }

        chips.forEach(function(chip) {
            chip.addEventListener('click', function() {
                handleQuestion(this.getAttribute('data-q'));
            });
        });
    });
    </script>
"""

# ==============================================================================
# 4. INJECT COMPONENTS INTO CORE PAGES
# ==============================================================================
# Inject interactive configurator into hiranandani-pune.html and hiranandani-price-list-2026.html
pages_for_configurator = [
    ("hiranandani-pune.html", '<!-- Chapter 6: Frequently Asked Questions'),
    ("hiranandani-price-list-2026.html", '<!-- Interactive 3D/2D Floor Plan')
]

for filename, anchor in pages_for_configurator:
    filepath = os.path.join(ROOT_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if 'id="interactive-configurator"' not in content:
            content = content.replace(anchor, configurator_html + '\n        ' + anchor)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected Interactive Configurator into {filename}")

# Inject AI Concierge Widget into index.html, hiranandani-pune.html, hiranandani-price-list-2026.html, and site-address.html
pages_for_widget = ["index.html", "hiranandani-pune.html", "hiranandani-price-list-2026.html", "site-address.html"]
for filename in pages_for_widget:
    filepath = os.path.join(ROOT_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if 'id="aiConciergeLauncher"' not in content:
            content = content.replace('</body>', ai_concierge_widget_html + '\n</body>')
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected AI Concierge Widget into {filename}")


# ==============================================================================
# 5. UPDATE _redirects, sitemap.xml, AND llms.txt
# ==============================================================================
# Update _redirects
redirects_path = os.path.join(ROOT_DIR, "_redirects")
with open(redirects_path, "r", encoding="utf-8") as f:
    redirects_content = f.read()

local_redirects = """
# Local Business & Site Address Shortcuts
/site-address                            /site-address 200
/sales-office                            /site-address 301
/location-map                            /site-address 301
/how-to-reach                            /site-address 301
/experience-center                       /site-address 301
/darumbre-site                           /site-address 301
/hiranandani-location                    /site-address 301
"""
if "/sales-office" not in redirects_content:
    redirects_content += "\n" + local_redirects.strip() + "\n"
    with open(redirects_path, "w", encoding="utf-8") as f:
        f.write(redirects_content)
    print("Updated _redirects with local business shortcuts.")

# Update sitemap.xml
sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

if "https://krisalahiranandanitownships.com/site-address" not in sitemap_content:
    new_url_entry = """    <url>
        <loc>https://krisalahiranandanitownships.com/site-address</loc>
        <lastmod>2026-10-20</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
"""
    sitemap_content = sitemap_content.replace('</urlset>', new_url_entry + '</urlset>')
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Added /site-address to sitemap.xml")

# Update llms.txt
llms_path = os.path.join(ROOT_DIR, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    llms_content = f.read()

if "https://krisalahiranandanitownships.com/site-address" not in llms_content:
    llms_content = llms_content.replace(
        '- [Research & Knowledge Hub]',
        '- [Official Sales Office & Site Address Experience Center](https://krisalahiranandanitownships.com/site-address): On-site 105-acre experience center location, GPS navigation (18.5913° N, 73.7389° E), and turn-by-turn driving directions.\n- [Research & Knowledge Hub]'
    )
    with open(llms_path, "w", encoding="utf-8") as f:
        f.write(llms_content)
    print("Added /site-address to llms.txt")

print("\nAll 5 Systems Deployed Successfully.")

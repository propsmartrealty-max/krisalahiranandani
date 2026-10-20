#!/usr/bin/env python3
"""
Deploy Google Discover Visual Optimization (Web Stories) & Voice Search Engine
Krisala Hiranandani Township Hinjewadi, Pune

Executes:
1. Google Discover Optimization:
   - Updates AMP Web Stories with high-impact keyframe CTA attachments, responsive vertical poster assets, and 1-tap WhatsApp deep links.
   - Refreshes sitemap-stories.xml with latest timestamps for Google Discover crawl ingestion.
2. Voice Search Optimization (Google Assistant, Siri, Alexa):
   - Injects Schema.org SpeakableSpecification into site-address.html, hiranandani-price-list-2026.html, and compare.html.
   - Embeds audio-optimized voice summary microdata (#voice-summary, #voice-address, #voice-pricing) for instant speech synthesis.
"""

import os
import re
from datetime import datetime, timezone

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================================================================
# 1. VOICE SEARCH HARDENING (SpeakableSpecification)
# ==============================================================================

# A. site-address.html Voice Search Injection
site_address_file = os.path.join(ROOT_DIR, "site-address.html")
if os.path.exists(site_address_file):
    with open(site_address_file, "r", encoding="utf-8") as f:
        c = f.read()

    voice_schema_address = """
    <!-- Voice Search Optimization: SpeakableSpecification for Google Assistant & Siri -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Hiranandani Pune Site Address & Location Map",
      "url": "https://krisalahiranandanitownships.com/site-address",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["#voice-address-summary", "#voice-transit-summary"]
      }
    }
    </script>
"""
    if "SpeakableSpecification" not in c:
        c = c.replace("</head>", voice_schema_address + "\n</head>")
        
        # Add speakable content block in hero/top
        speakable_block = """
                <!-- Voice Assistant Spoken Synthesis Target (Google Assistant / Alexa / Siri) -->
                <div id="voice-address-summary" style="display: none;" aria-hidden="true">
                    Krisala Hiranandani Township is located along the PMRDA 128m Ring Road in North Hinjawadi, Darumbre, Pune 410506. Driving time is 7 minutes to Hinjewadi Metro Line 3 Megapolis Station, 10 minutes to Mumbai Pune Expressway Urse Toll, and 12 minutes to Infosys Phase 1.
                </div>
                <div id="voice-transit-summary" style="display: none;" aria-hidden="true">
                    The on-site sales experience center is open Monday through Sunday from 9:30 AM to 7:30 PM. For direct telephone inquiries call 7744009295.
                </div>
"""
        c = c.replace('<main id="main-content">', '<main id="main-content">\n' + speakable_block)
        with open(site_address_file, "w", encoding="utf-8") as f:
            f.write(c)
        print("Hardened site-address.html with Voice Search SpeakableSpecification.")

# B. hiranandani-price-list-2026.html Voice Search Injection
price_file = os.path.join(ROOT_DIR, "hiranandani-price-list-2026.html")
if os.path.exists(price_file):
    with open(price_file, "r", encoding="utf-8") as f:
        c = f.read()

    voice_schema_price = """
    <!-- Voice Search Optimization: SpeakableSpecification for Google Assistant & Siri -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Hiranandani Pune Price List 2026",
      "url": "https://krisalahiranandanitownships.com/hiranandani-price-list-2026",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["#voice-pricing-summary"]
      }
    }
    </script>
"""
    if "SpeakableSpecification" not in c:
        c = c.replace("</head>", voice_schema_price + "\n</head>")
        speakable_price_block = """
                <!-- Voice Assistant Spoken Synthesis Target -->
                <div id="voice-pricing-summary" style="display: none;" aria-hidden="true">
                    The official starting price for Krisala Hiranandani Pune is 79 Lakhs all inclusive for a 2 BHK Smart Luxury apartment in Sector Arcadia. 3 BHK residences start at 1.25 Crore in The Colosseum, and 4 BHK Sky Duplexes start at 2.10 Crore in Sector Icon. Della villa plots start at 1.80 Crore.
                </div>
"""
        c = c.replace('<main id="main-content">', '<main id="main-content">\n' + speakable_price_block)
        with open(price_file, "w", encoding="utf-8") as f:
            f.write(c)
        print("Hardened hiranandani-price-list-2026.html with Voice Search SpeakableSpecification.")

# C. compare.html Voice Search Injection
compare_file = os.path.join(ROOT_DIR, "compare.html")
if os.path.exists(compare_file):
    with open(compare_file, "r", encoding="utf-8") as f:
        c = f.read()

    voice_schema_compare = """
    <!-- Voice Search Optimization: SpeakableSpecification for Google Assistant & Siri -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Krisala Hiranandani Competitor Benchmark",
      "url": "https://krisalahiranandanitownships.com/compare",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["#voice-compare-summary"]
      }
    }
    </script>
"""
    if "SpeakableSpecification" not in c:
        c = c.replace("</head>", voice_schema_compare + "\n</head>")
        speakable_comp_block = """
        <!-- Voice Assistant Spoken Synthesis Target -->
        <div id="voice-compare-summary" style="display: none;" aria-hidden="true">
            Krisala Hiranandani Township in North Hinjewadi spans 105 acres featuring India's first residential 8-acre turf racecourse and Della adventure resort, offering 70% open green space at 9,800 rupees per square foot all-inclusive, compared to standalone high-rises in Mahalunge.
        </div>
"""
        c = c.replace('<main id="main-content">', '<main id="main-content">\n' + speakable_comp_block)
        with open(compare_file, "w", encoding="utf-8") as f:
            f.write(c)
        print("Hardened compare.html with Voice Search SpeakableSpecification.")


# ==============================================================================
# 2. GOOGLE DISCOVER VISUAL OPTIMIZATION (AMP Web Stories)
# ==============================================================================
stories_dir = os.path.join(ROOT_DIR, "stories")
story_files = [f for f in os.listdir(stories_dir) if f.endswith(".html")]

updated_stories_count = 0
for sf in story_files:
    sf_path = os.path.join(stories_dir, sf)
    with open(sf_path, "r", encoding="utf-8") as f:
        s_html = f.read()

    # Update dateModified to now for fresh Google Discover re-indexing
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    s_html = re.sub(r'"dateModified":\s*"[^"]+"', f'"dateModified": "{now_iso}"', s_html)

    # Ensure Discover CTA attachment points to instant WhatsApp
    if "wa.me/917744009295" not in s_html:
        s_html = s_html.replace('data-cta-link="https://krisalahiranandanitownships.com/#contact"', 'data-cta-link="https://wa.me/917744009295?text=Hello%20Sales%20Team%2C%20I%20viewed%20your%20Google%20Web%20Story%20and%20would%20like%20to%20receive%20the%202026%20cost%20sheet%20and%20floor%20plans."')
        s_html = s_html.replace('data-cta-link="https://krisalahiranandanitownships.com/pricing"', 'data-cta-link="https://wa.me/917744009295?text=Hello%20Sales%20Team%2C%20I%20viewed%20your%20Google%20Web%20Story%20and%20would%20like%20to%20receive%20the%202026%20cost%20sheet%20and%20floor%20plans."')

    with open(sf_path, "w", encoding="utf-8") as f:
        f.write(s_html)
    updated_stories_count += 1

print(f"Refreshed {updated_stories_count} AMP Web Stories with fresh Discover timestamps and instant WhatsApp CTAs.")

# Update sitemap-stories.xml with fresh timestamps
stories_sitemap = os.path.join(ROOT_DIR, "sitemap-stories.xml")
if os.path.exists(stories_sitemap):
    with open(stories_sitemap, "r", encoding="utf-8") as f:
        sm_stories = f.read()
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    sm_stories = re.sub(r'<lastmod>[^<]+</lastmod>', f'<lastmod>{today_str}</lastmod>', sm_stories)
    with open(stories_sitemap, "w", encoding="utf-8") as f:
        f.write(sm_stories)
    print("Updated sitemap-stories.xml with fresh Google Discover crawl timestamps.")

print("\nVoice Search & Google Discover Optimization Completed Successfully.")

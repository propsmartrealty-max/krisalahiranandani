#!/usr/bin/env python3
"""
Krisala Hiranandani Township Hinjewadi
Enterprise Google Merchant Center & Google Shopping XML Feed Generator
Generates standards-compliant Google Product RSS 2.0 Feeds with namespace xmlns:g="http://base.google.com/ns/1.0"
Enables Google Shopping, Merchant Center, and SERP Price Snippets indexing.
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BASE_URL = "https://krisalahiranandanitownships.com"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")

INVENTORY = [
    {
        "id": "KXH-PUNE-MASTER",
        "title": "Hiranandani Pune 105-Acre Flagship Integrated Equestrian Township (Hinjewadi)",
        "description": "Official Master Township Portal for Krisala Hiranandani Pune in North Hinjewadi. 105+ Acres featuring Neoclassical Greco-Roman architecture, 2, 3, 4 BHK residences, Della luxury villa plots, and India's first 8-acre private racecourse. MahaRERA: PR1260002500600, PR1260002600818, PR1260002502438.",
        "link": f"{BASE_URL}/hiranandani-pune",
        "image_link": f"{BASE_URL}/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "price": "7900000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Integrated Townships > Flagship Master Development",
        "mpn": "PR1260002500600-TOWNSHIP"
    },
    {
        "id": "KXH-PRICE-2026",
        "title": "Hiranandani Pune 2026 Official Price List, Cost Sheet & Payment Schedules",
        "description": "Official 2026 price list and cost sheets for Krisala Hiranandani Township Hinjewadi, Pune. 2 BHK from ₹79L, 3 BHK from ₹1.25Cr, 4 BHK Duplex from ₹2.10Cr, and Della Villa Plots from ₹1.80Cr. All-inclusive cost sheets with stamp duty and RERA milestones.",
        "link": f"{BASE_URL}/hiranandani-price-list-2026",
        "image_link": f"{BASE_URL}/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "price": "7900000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Pricing & Cost Sheets > 2026 Price List",
        "mpn": "PR1260002500600-PRICELIST2026"
    },
    {
        "id": "KXH-ARC-2BHK",
        "title": "Krisala Hiranandani 2 BHK Luxury Neoclassical Apartment (Sector Arcadia)",
        "description": "Official MahaRERA PR1260002502438 verified 2 BHK residence in Sector Arcadia, Krisala Hiranandani Township Hinjewadi, Pune. 740-840 sq.ft. carpet area, Mivan aluminium formwork, private sundeck, 8-acre racecourse access, and signal-free connectivity to Hinjewadi IT Park.",
        "link": f"{BASE_URL}/arcadia",
        "image_link": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_1.webp",
        "price": "7900000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > 2 BHK Apartments",
        "mpn": "PR1260002502438-ARC2BHK"
    },
    {
        "id": "KXH-ARC-3BHK",
        "title": "Krisala Hiranandani 3 BHK Royale Neoclassical Residence (Sector Arcadia)",
        "description": "Grand 3 BHK luxury residences in Sector Arcadia, Krisala Hiranandani Township. 1,050-1,280 sq.ft. usable carpet area, double balconies, Italian marble living room, 10.5 ft ceilings, and panoramic views of the 8-acre private equestrian racecourse. MahaRERA PR1260002502438.",
        "link": f"{BASE_URL}/arcadia",
        "image_link": f"{BASE_URL}/public/everlyn/floorplans/plan_booklet_2.webp",
        "price": "12500000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > 3 BHK Apartments",
        "mpn": "PR1260002502438-ARC3BHK"
    },
    {
        "id": "KXH-COL-2BHK",
        "title": "The Colosseum 2 BHK Grande Roman Amphitheater Tower Residence (Phase 4)",
        "description": "Codename The Colosseum Phase 4 pre-launch opportunity: 765 sq.ft. Grande 2 BHK with Roman amphitheater podium, Diwali pricing benefits of ₹5L-₹9L, and 270-degree horizons across Sahyadri foothills. MahaRERA PR1260002500600.",
        "link": f"{BASE_URL}/colosseum",
        "image_link": f"{BASE_URL}/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "price": "8299000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > The Colosseum Phase 4",
        "mpn": "PR1260002500600-COL2BHK"
    },
    {
        "id": "KXH-COL-3BHK",
        "title": "The Colosseum 3 BHK Royale Amphitheater Tower Residence (Phase 4)",
        "description": "Premium 3 BHK Royale (1,085 sq.ft.) and 3 BHK Regalia (1,215 sq.ft.) in The Colosseum Phase 4 towers. B+G+27 storeys, Roman colonnade architecture, Olympic lap pool, and IGBC Platinum design in North Hinjewadi. MahaRERA PR1260002500600.",
        "link": f"{BASE_URL}/colosseum",
        "image_link": f"{BASE_URL}/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "price": "13500000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > The Colosseum Phase 4",
        "mpn": "PR1260002500600-COL3BHK"
    },
    {
        "id": "KXH-COL-4BHK",
        "title": "The Colosseum 4 BHK Palatial Roman Penthouse Suite (Phase 4)",
        "description": "Monumental 4 BHK Palatial residences (1,600 sq.ft.) commanding 270-degree panoramic views of the private racecourse and expressway corridor. Private foyer, luxury finishings, and exclusive Diwali window token access.",
        "link": f"{BASE_URL}/colosseum",
        "image_link": f"{BASE_URL}/public/township_grand/krisala_hiranandani_grand_entrance_hero.webp",
        "price": "21000000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > The Colosseum Phase 4",
        "mpn": "PR1260002500600-COL4BHK"
    },
    {
        "id": "KXH-ICN-3BHK",
        "title": "Sector Icon 3 BHK Luxury Flagship Residence (Tower A, B & C Triad)",
        "description": "Ultra-luxury 3 BHK flagship residences in Sector Icon Towers A, B & C. 1,250-1,450 sq.ft. carpet area, 52 numbered flagship amenities, Lookout Pod Aether Deck, floating clubhouse, and acoustic glazing. MahaRERA PR1260002600818.",
        "link": f"{BASE_URL}/icon",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "18500000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Ultra Luxury > Sector Icon",
        "mpn": "PR1260002600818-ICN3BHK"
    },
    {
        "id": "KXH-ICN-4BHK",
        "title": "Sector Icon 4 BHK Palatial Presidential Suite (Sector Icon Flagship)",
        "description": "Palatial 4 BHK presidential suites commanding 1,850-2,300 sq.ft. carpet area with private high-speed elevators, servant quarters, and 360-degree vistas across the Della resort and equestrian derby track. MahaRERA PR1260002600818.",
        "link": f"{BASE_URL}/icon",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "21000000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Ultra Luxury > Sector Icon",
        "mpn": "PR1260002600818-ICN4BHK"
    },
    {
        "id": "KXH-ICN-DUPLEX",
        "title": "Sector Icon 3 & 4 BHK Sky Duplex Penthouse with Private Terrace Sky Garden",
        "description": "Signature 22-foot double-height sky duplex penthouses spanning 2,600-3,400 sq.ft. Designed for CXOs and business leaders seeking a private villa in the sky with home automation and equestrian views.",
        "link": f"{BASE_URL}/icon",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "26500000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Ultra Luxury > Sky Duplexes",
        "mpn": "PR1260002600818-DUPLEX"
    },
    {
        "id": "KXH-ICN-5BHK",
        "title": "Sector Icon 5 BHK Imperial Sky Mansion with Private Lap Pool",
        "description": "The pinnacle of luxury in Western Pune: 2,800-3,800 sq.ft. imperial sky mansions with 24-foot double-height living room, private lap pool, dedicated butler room, and panoramic Sahyadri mountain views.",
        "link": f"{BASE_URL}/icon",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "32000000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Ultra Luxury > Sky Mansions",
        "mpn": "PR1260002600818-5BHK"
    },
    {
        "id": "KXH-DEL-VILLA-2000",
        "title": "The Della Collection 2,000 sq.ft. Equestrian Villa Plot",
        "description": "Bespoke resort villa plot in the 40-acre Della hospitality district with 8-acre championship polo oval and private racecourse. G+2 independent villa permissions with Della Resorts 5-star concierge membership.",
        "link": f"{BASE_URL}/della",
        "image_link": f"{BASE_URL}/public/imported/krisala-hiranandani-banner.webp",
        "price": "18000000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Land & Plots > Equestrian Villa Plots",
        "mpn": "DELLA-RESORT-PLOT2000"
    },
    {
        "id": "KXH-DEL-VILLA-3000",
        "title": "The Della Collection 3,000 sq.ft. Equestrian Estate Plot",
        "description": "Expansive 3,000 sq.ft. equestrian estate parcel fronting the private polo track. Clear demarcated title, PMRDA sanctioned layouts, and exclusive access to the Della Adventure & Concierge Club.",
        "link": f"{BASE_URL}/della",
        "image_link": f"{BASE_URL}/public/imported/krisala-hiranandani-banner.webp",
        "price": "26500000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Land & Plots > Equestrian Villa Plots",
        "mpn": "DELLA-RESORT-PLOT3000"
    },
    {
        "id": "KXH-DEL-VILLA-5000",
        "title": "The Della Collection 5,000 sq.ft. Presidential Polo Estate Parcel",
        "description": "Ultra-exclusive 5,000 sq.ft. presidential polo parcel with direct racecourse frontage, air-cooled equine stables, and resort lifestyle privileges curated in collaboration with Jimmy Mistry (Della Resorts).",
        "link": f"{BASE_URL}/della",
        "image_link": f"{BASE_URL}/public/imported/krisala-hiranandani-banner.webp",
        "price": "35000000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Land & Plots > Equestrian Villa Plots",
        "mpn": "DELLA-RESORT-PLOT5000"
    },
    {
        "id": "KXH-EVR-2BHK",
        "title": "Sector Everlyn 2 BHK Lakefront & Butterfly Sanctuary Apartment",
        "description": "Family-first residential sector nestled along the northwest green ribbon: 740 sq.ft. 2 BHK apartments featuring direct access to the central lake, butterfly sanctuary, and nature walking trails. MahaRERA PR1260002500600.",
        "link": f"{BASE_URL}/everlyn",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "7650000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > Sector Everlyn",
        "mpn": "PR1260002500600-EVR2BHK"
    },
    {
        "id": "KXH-EVR-3BHK",
        "title": "Sector Everlyn 3 BHK Lakefront & Botanical Park Residence",
        "description": "Spacious 1,150-1,320 sq.ft. 3 BHK lakefront residences in Sector Everlyn. Monolithic Mivan RCC construction, zero beam intrusion, high-speed elevators, and TERI circular water ecology.",
        "link": f"{BASE_URL}/everlyn",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "12200000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > Sector Everlyn",
        "mpn": "PR1260002500600-EVR3BHK"
    },
    {
        "id": "KXH-SMP-EXEC",
        "title": "Simplex Executive Single-Level Luxury Suite (Sector Arcadia)",
        "description": "Tailored single-level executive homes (920-1,150 sq.ft.) in Sector Arcadia designed for modern tech leaders seeking streamlined maintenance with elite Hiranandani craftsmanship and expressway connectivity.",
        "link": f"{BASE_URL}/arcadia",
        "image_link": f"{BASE_URL}/public/everlyn/hero/hero_main_hq.webp",
        "price": "9800000.00 INR",
        "availability": "in stock",
        "brand": "Krisala x Hiranandani",
        "product_type": "Real Estate > Residential Properties > Simplex Suites",
        "mpn": "PR1260002502438-SIMPLEX"
    }
]

def generate_feed():
    rss = ET.Element("rss", {
        "version": "2.0",
        "xmlns:g": "http://base.google.com/ns/1.0"
    })
    channel = ET.SubElement(rss, "channel")

    title = ET.SubElement(channel, "title")
    title.text = "Krisala Hiranandani Township Hinjewadi — Official Google Product Inventory Feed"

    link = ET.SubElement(channel, "link")
    link.text = BASE_URL

    desc = ET.SubElement(channel, "description")
    desc.text = "Verified Google Merchant & Google Shopping Product Feed for Krisala Hiranandani Township Hinjewadi, Pune. Featuring 2, 3, 4 BHK apartments, Sky Duplexes, and Della Villa plots."

    last_build = ET.SubElement(channel, "lastBuildDate")
    last_build.text = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

    for item_data in INVENTORY:
        item = ET.SubElement(channel, "item")

        i_id = ET.SubElement(item, "g:id")
        i_id.text = item_data["id"]

        i_title = ET.SubElement(item, "g:title")
        i_title.text = item_data["title"]

        i_desc = ET.SubElement(item, "g:description")
        i_desc.text = item_data["description"]

        i_link = ET.SubElement(item, "g:link")
        i_link.text = item_data["link"]

        i_img = ET.SubElement(item, "g:image_link")
        i_img.text = item_data["image_link"]

        i_avail = ET.SubElement(item, "g:availability")
        i_avail.text = item_data["availability"]

        i_price = ET.SubElement(item, "g:price")
        i_price.text = item_data["price"]

        i_brand = ET.SubElement(item, "g:brand")
        i_brand.text = item_data["brand"]

        i_condition = ET.SubElement(item, "g:condition")
        i_condition.text = "new"

        i_cat = ET.SubElement(item, "g:google_product_category")
        i_cat.text = "Real Estate > Residential Properties"

        i_type = ET.SubElement(item, "g:product_type")
        i_type.text = item_data["product_type"]

        i_mpn = ET.SubElement(item, "g:mpn")
        i_mpn.text = item_data["mpn"]

    xml_bytes = ET.tostring(rss, encoding="utf-8", xml_declaration=True)

    dest_files = [
        os.path.join(PUBLIC_DIR, "google-merchant-feed.xml"),
        os.path.join(PUBLIC_DIR, "google-products.xml"),
        os.path.join(ROOT_DIR, "google-products.xml")
    ]

    for dest in dest_files:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(xml_bytes)
        print(f"  [✓] Feed generated: {dest} ({len(INVENTORY)} products)")

if __name__ == "__main__":
    print("=================================================================")
    print("Generating Google Merchant Center & Shopping Product Feeds...")
    print("=================================================================")
    generate_feed()
    print("=================================================================")

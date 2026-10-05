#!/usr/bin/env python3
"""
Generate high-fidelity, luxury neoclassical PDF brochure and price list for Krisala Hiranandani Township.
Uses PyMuPDF (fitz) and Pillow (PIL).
"""

import io
import os
import fitz  # PyMuPDF
from PIL import Image

def img_to_bytes(img_path, format="PNG"):
    """Load image from disk and return bytes in given format."""
    with Image.open(img_path) as im:
        buf = io.BytesIO()
        # Convert RGBA to RGB with dark background if JPEG
        if format == "JPEG" and im.mode in ("RGBA", "P"):
            bg = Image.new("RGB", im.size, (11, 11, 15))
            if im.mode == "RGBA":
                bg.paste(im, mask=im.split()[3])
            else:
                bg.paste(im)
            bg.save(buf, format="JPEG", quality=90)
        else:
            im.save(buf, format=format)
        return buf.getvalue()

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))

GOLD = hex_to_rgb("#C5A059")
GOLD_LIGHT = hex_to_rgb("#DFBE7F")
DARK_BG = hex_to_rgb("#0B0B0F")
CARD_BG = hex_to_rgb("#141419")
TEXT_LIGHT = hex_to_rgb("#FFFFFF")
TEXT_MUTED = hex_to_rgb("#A0A0A0")
BORDER_GOLD = hex_to_rgb("#4A3B22")

def add_header_footer(page, page_num, total_pages=7):
    """Adds uniform luxury header and footer across internal pages."""
    # Top rule
    page.draw_line(fitz.Point(36, 40), fitz.Point(559, 40), color=BORDER_GOLD, width=0.75)
    page.insert_text((36, 32), "KRISALA HIRANANDANI TOWNSHIP", fontsize=8, color=GOLD, fontname="helv")
    page.insert_text((390, 32), "HINJEWADI, PUNE • MAHARERA VERIFIED", fontsize=7.5, color=TEXT_MUTED, fontname="helv")

    # Bottom rule
    page.draw_line(fitz.Point(36, 800), fitz.Point(559, 800), color=BORDER_GOLD, width=0.75)
    page.insert_text((36, 814), "Authorized Partner Desk: Propsmart Realty • Direct Concierge: +91 7744009295", fontsize=7.5, color=TEXT_MUTED, fontname="helv")
    page.insert_text((515, 814), f"Page {page_num} of {total_pages}", fontsize=7.5, color=GOLD, fontname="helv")

def build_official_brochure():
    doc = fitz.open()

    # ==========================================
    # PAGE 1: COVER
    # ==========================================
    p1 = doc.new_page(width=595, height=842) # A4
    # Background fill
    p1.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    
    # Border
    p1.draw_rect(fitz.Rect(20, 20, 575, 822), color=BORDER_GOLD, width=1.5)
    p1.draw_rect(fitz.Rect(24, 24, 571, 818), color=BORDER_GOLD, width=0.5)

    # Logo
    if os.path.exists("public/krisala-hiranandani-logo.png"):
        logo_bytes = img_to_bytes("public/krisala-hiranandani-logo.png", "PNG")
        p1.insert_image(fitz.Rect(140, 50, 455, 95), stream=logo_bytes)

    # Title
    p1.insert_text((70, 130), "KRISALA × HIRANANDANI", fontsize=24, color=GOLD_LIGHT, fontname="times-bold")
    p1.insert_text((150, 152), "T O W N S H I P", fontsize=14, color=GOLD, fontname="times-roman")
    p1.insert_text((135, 175), "HINJEWADI • PUNE WEST", fontsize=10, color=TEXT_MUTED, fontname="helv")

    # Hero Image
    if os.path.exists("public/everlyn/hero/hero_main_hq.webp"):
        hero_bytes = img_to_bytes("public/everlyn/hero/hero_main_hq.webp", "JPEG")
        p1.insert_image(fitz.Rect(45, 195, 550, 470), stream=hero_bytes)
        p1.draw_rect(fitz.Rect(45, 195, 550, 470), color=GOLD, width=0.8)

    # Sub-box
    p1.draw_rect(fitz.Rect(45, 485, 550, 580), color=BORDER_GOLD, fill=CARD_BG, width=0.8)
    p1.insert_text((65, 510), "INDIA'S FIRST RESIDENTIAL EQUESTRIAN TOWNSHIP", fontsize=12, color=GOLD, fontname="helv")
    p1.insert_text((65, 532), "105-Acre Master Development featuring Sector Arcadia (2 & 3 BHK),", fontsize=10, color=TEXT_LIGHT, fontname="helv")
    p1.insert_text((65, 548), "Sector Icon (3, 4 & 5 BHK Sky Duplexes), and 8-Acre Private Racecourse.", fontsize=10, color=TEXT_LIGHT, fontname="helv")
    p1.insert_text((65, 566), "Curated by Dr. Niranjan Hiranandani & Krisala Developers.", fontsize=9.5, color=GOLD_LIGHT, fontname="times-italic")

    # Metrics Grid
    p1.draw_rect(fitz.Rect(45, 595, 165, 665), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p1.insert_text((65, 625), "105 ACRES", fontsize=13, color=GOLD_LIGHT, fontname="helv")
    p1.insert_text((65, 645), "Master Township", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    p1.draw_rect(fitz.Rect(175, 595, 295, 665), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p1.insert_text((195, 625), "8-ACRE RACECOURSE", fontsize=11, color=GOLD_LIGHT, fontname="helv")
    p1.insert_text((195, 645), "Polo & Equestrian Track", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    p1.draw_rect(fitz.Rect(305, 595, 425, 665), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p1.insert_text((325, 625), "70% GREENS", fontsize=13, color=GOLD_LIGHT, fontname="helv")
    p1.insert_text((325, 645), "Low Density Zoning", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    p1.draw_rect(fitz.Rect(435, 595, 550, 665), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p1.insert_text((455, 625), "₹79 LAKHS*", fontsize=13, color=GOLD_LIGHT, fontname="helv")
    p1.insert_text((455, 645), "Starting Price", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    # MahaRERA Footer on Cover
    p1.insert_text((65, 715), "OFFICIAL MAHARERA REGISTRATIONS:", fontsize=9, color=GOLD, fontname="helv")
    p1.insert_text((65, 735), "• Phase 3 (Sector Arcadia): MahaRERA PR1260002502438", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p1.insert_text((65, 752), "• Sector Icon (Sky Villas): MahaRERA PR1260002600818", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p1.insert_text((65, 770), "• Authorized Channel Partner: Propsmart Realty (MahaRERA: A52100024102)", fontsize=9, color=TEXT_MUTED, fontname="helv")

    # ==========================================
    # PAGE 2: VISION & 105-ACRE MASTERPLAN
    # ==========================================
    p2 = doc.new_page(width=595, height=842)
    p2.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p2, 2)

    p2.insert_text((36, 70), "MASTERPLAN & URBAN DESIGN", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p2.insert_text((36, 90), "A 105-Acre Self-Sustained Neoclassical Township in North Hinjewadi", fontsize=10, color=TEXT_MUTED, fontname="helv")

    if os.path.exists("public/everlyn/masterplan/master_layout_hq.webp"):
        mp_bytes = img_to_bytes("public/everlyn/masterplan/master_layout_hq.webp", "JPEG")
        p2.insert_image(fitz.Rect(36, 110, 559, 390), stream=mp_bytes)
        p2.draw_rect(fitz.Rect(36, 110, 559, 390), color=BORDER_GOLD, width=0.8)

    # Zoning Breakdown
    sectors = [
        ("SECTOR ARCADIA (PHASE 3)", "High-speed Mivan monolithic towers offering spacious 2 & 3 BHK residences with double-ventilation balconies and zero hallway wastage. Starting ₹79 Lakhs* onwards."),
        ("SECTOR ICON (SKY VILLAS)", "Ultra-luxury high-rise tower cluster featuring 18-foot double-height sky duplexes and 360-degree racecourse views. Starting ₹1.18 Cr* onwards."),
        ("THE DELLA COLLECTION", "Limited 100 private equestrian villa plots (2,000 to 5,000 sq.ft.) curated with Della Resorts, boasting VIP polo privileges. Starting ₹3.50 Cr* onwards."),
        ("8-ACRE PRIVATE RACECOURSE", "India's first private residential championship turf track, complete with equestrian riding academy, stables, and member club lounges.")
    ]

    y_pos = 415
    for title, desc in sectors:
        p2.draw_rect(fitz.Rect(36, y_pos, 559, y_pos + 75), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
        p2.insert_text((50, y_pos + 22), title, fontsize=11, color=GOLD, fontname="helv")
        # Multi-line wrap
        p2.insert_textbox(fitz.Rect(50, y_pos + 30, 545, y_pos + 70), desc, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_pos += 85

    # Hydrology note
    p2.insert_text((36, 780), "✦ TERI 50-Year Hydrology Resilience: Zero-discharge water neutrality & circular rainwater reservoirs.", fontsize=8.5, color=GOLD_LIGHT, fontname="times-italic")

    # ==========================================
    # PAGE 3: SECTOR ARCADIA (2 & 3 BHK)
    # ==========================================
    p3 = doc.new_page(width=595, height=842)
    p3.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p3, 3)

    p3.insert_text((36, 70), "SECTOR ARCADIA — 2 & 3 BHK HOMES", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p3.insert_text((36, 90), "Mivan Monolithic Engineering • 780 – 1,180 Sq.Ft. Carpet • MahaRERA PR1260002502438", fontsize=9.5, color=TEXT_MUTED, fontname="helv")

    # Floor plan preview
    if os.path.exists("public/everlyn/floorplans/plan_booklet_1.webp"):
        fp_bytes = img_to_bytes("public/everlyn/floorplans/plan_booklet_1.webp", "JPEG")
        p3.insert_image(fitz.Rect(36, 110, 559, 380), stream=fp_bytes)
        p3.draw_rect(fitz.Rect(36, 110, 559, 380), color=BORDER_GOLD, width=0.8)

    # Specs table
    p3.draw_rect(fitz.Rect(36, 400, 559, 560), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p3.insert_text((50, 425), "ARCHITECTURAL SPECIFICATIONS & HIGHLIGHTS", fontsize=11, color=GOLD, fontname="helv")

    specs = [
        ("Monolithic Mivan Structure", "Engineered with 100% monolithic shear-wall RCC for superior seismic resistance and smooth finishes."),
        ("Zero Corridor Wastage", "Efficient spatial design ensuring maximum carpet efficiency with 82%+ usable space."),
        ("10.5 Ft Ceiling Heights", "Extended vertical clearance delivering enhanced natural light, cross-breeze, and luxury grandeur."),
        ("Acoustic German Windows", "Double-glazed powder-coated aluminum sliding windows for acoustic sound isolation."),
        ("Smart Home Automation", "Digital door lock with biometric fingerprint, video door phone, and sensor controls.")
    ]
    y_spec = 445
    for k, v in specs:
        p3.insert_text((50, y_spec), f"• {k}:", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p3.insert_textbox(fitz.Rect(200, y_spec - 10, 545, y_spec + 15), v, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_spec += 22

    # Typologies
    p3.draw_rect(fitz.Rect(36, 580, 290, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p3.insert_text((50, 605), "2 BHK LUXURY RESIDENCE", fontsize=12, color=GOLD, fontname="helv")
    p3.insert_text((50, 625), "• Carpet Area: 780 – 840 Sq.Ft.", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((50, 645), "• 2 Bed | 2 Bath | 1 Private Sundeck", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((50, 665), "• Living-Dining Layout with Modular Kitchen", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((50, 685), "• Starting Price: ₹79 Lakhs* onwards", fontsize=10, color=GOLD_LIGHT, fontname="helv")
    p3.insert_text((50, 715), "• Possession: December 2029", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    p3.draw_rect(fitz.Rect(305, 580, 559, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p3.insert_text((320, 605), "3 BHK ROYALE RESIDENCE", fontsize=12, color=GOLD, fontname="helv")
    p3.insert_text((320, 625), "• Carpet Area: 1,050 – 1,180 Sq.Ft.", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((320, 645), "• 3 Bed | 3 Bath | 2 Wrap-Around Decks", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((320, 665), "• Walk-in Wardrobe Niche in Master Suite", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p3.insert_text((320, 685), "• Starting Price: ₹1.18 Cr* onwards", fontsize=10, color=GOLD_LIGHT, fontname="helv")
    p3.insert_text((320, 715), "• Possession: December 2029", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    # ==========================================
    # PAGE 4: SECTOR ICON (SKY VILLAS & DUPLEXES)
    # ==========================================
    p4 = doc.new_page(width=595, height=842)
    p4.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p4, 4)

    p4.insert_text((36, 70), "SECTOR ICON — ULTRA-LUXURY SKY VILLAS", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p4.insert_text((36, 90), "18-Ft Double Height Duplexes • Racecourse Panorama • MahaRERA PR1260002600818", fontsize=9.5, color=TEXT_MUTED, fontname="helv")

    if os.path.exists("public/everlyn/floorplans/unit_plan_2.webp"):
        duplex_bytes = img_to_bytes("public/everlyn/floorplans/unit_plan_2.webp", "JPEG")
        p4.insert_image(fitz.Rect(36, 110, 559, 380), stream=duplex_bytes)
        p4.draw_rect(fitz.Rect(36, 110, 559, 380), color=BORDER_GOLD, width=0.8)

    # Duplex features
    p4.draw_rect(fitz.Rect(36, 400, 559, 560), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p4.insert_text((50, 425), "SIGNATURE SKY DUPLEX & MANSION HIGHLIGHTS", fontsize=11, color=GOLD, fontname="helv")

    icon_specs = [
        ("18-Ft Double-Height Living Atrium", "Cathedral-like vertical scale offering unmatched spatial grandeur and dramatic views."),
        ("Direct Elevator Foyer Access", "Key-controlled high-speed elevators landing in your private private residential vestibule."),
        ("Panoramic Racecourse Sundecks", "Private wrap-around terraces looking directly onto the 8-acre championship turf."),
        ("Italian Botticino Marble Flooring", "Imported mirror-finish stone flooring laid across living, dining, and master corridors."),
        ("Smart Automated Climate & Lighting", "Centralized iPad control console integrating VRV HVAC, mood lights, and motorized drapes.")
    ]
    y_ispec = 445
    for k, v in icon_specs:
        p4.insert_text((50, y_ispec), f"• {k}:", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p4.insert_textbox(fitz.Rect(210, y_ispec - 10, 545, y_ispec + 15), v, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_ispec += 22

    # Duplex Configurations
    p4.draw_rect(fitz.Rect(36, 580, 290, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p4.insert_text((50, 605), "4 BHK GRAND DUPLEX SKY VILLA", fontsize=11, color=GOLD, fontname="helv")
    p4.insert_text((50, 625), "• Carpet Area: 1,650 – 1,850 Sq.Ft.", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((50, 645), "• 4 Bed | 4 Bath | Powder Room | Sundeck", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((50, 665), "• 18-Ft Living Room with Mezzanine Lounge", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((50, 685), "• Starting Price: ₹2.10 Cr* onwards", fontsize=10, color=GOLD_LIGHT, fontname="helv")
    p4.insert_text((50, 715), "• Possession: December 2029", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    p4.draw_rect(fitz.Rect(305, 580, 559, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p4.insert_text((320, 605), "5 BHK IMPERIAL SKY MANSION", fontsize=11, color=GOLD, fontname="helv")
    p4.insert_text((320, 625), "• Carpet Area: 2,800 – 3,500 Sq.Ft.", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((320, 645), "• 5 Bed | 6 Bath | Private Plunge Pool Terrace", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((320, 665), "• Dual Master Suites with En-Suite Walk-ins", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    p4.insert_text((320, 685), "• Starting Price: ₹3.20 Cr* onwards", fontsize=10, color=GOLD_LIGHT, fontname="helv")
    p4.insert_text((320, 715), "• Possession: December 2029", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    # ==========================================
    # PAGE 5: 8-ACRE RACECOURSE & DELLA EQUESTRIAN
    # ==========================================
    p5 = doc.new_page(width=595, height=842)
    p5.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p5, 5)

    p5.insert_text((36, 70), "8-ACRE RACECOURSE & THE DELLA COLLECTION", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p5.insert_text((36, 90), "India's First Private Equestrian Circuit Curated in Association with Della Resorts", fontsize=9.5, color=TEXT_MUTED, fontname="helv")

    if os.path.exists("public/imported/della-racecource.webp"):
        race_bytes = img_to_bytes("public/imported/della-racecource.webp", "JPEG")
        p5.insert_image(fitz.Rect(36, 110, 559, 380), stream=race_bytes)
        p5.draw_rect(fitz.Rect(36, 110, 559, 380), color=BORDER_GOLD, width=0.8)

    # Equestrian Details
    p5.draw_rect(fitz.Rect(36, 400, 559, 560), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p5.insert_text((50, 425), "EQUESTRIAN & POLO CLUB HIGHLIGHTS", fontsize=11, color=GOLD, fontname="helv")

    equestrian_points = [
        ("6-Furlong Turf Track", "Championship-standard manicured galloping turf built to global FEI equestrian standards."),
        ("Horse Riding Academy", "Certified trainers and instructors for children, beginners, and competitive show-jumpers."),
        ("Stables & Livery Service", "Air-cooled boarding stalls with on-demand veterinarian care and equine nutritional experts."),
        ("Della Resort Privileges", "Members-only lounge, viewing pavilions, private cigar room, and gourmet dining."),
        ("Dressage & Polo Arena", "Dedicated jumping arenas, sand school tracks, and weekend polo match tournaments.")
    ]
    y_epoint = 445
    for k, v in equestrian_points:
        p5.insert_text((50, y_epoint), f"• {k}:", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p5.insert_textbox(fitz.Rect(190, y_epoint - 10, 545, y_epoint + 15), v, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_epoint += 22

    # Villa plots card
    p5.draw_rect(fitz.Rect(36, 580, 559, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p5.insert_text((50, 605), "THE DELLA COLLECTION — ULTRA-EXCLUSIVE VILLA PLOTS", fontsize=12, color=GOLD, fontname="helv")
    p5.insert_text((50, 630), "• Limited Collection of Only 100 Gated Villa Plots (2,000 to 5,000 Sq.Ft.)", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    p5.insert_text((50, 650), "• Bespoke Villa Architectural Designs by Leading International Architects", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    p5.insert_text((50, 670), "• Direct Equestrian Circuit Access with Frontage onto the Polo Pavilion", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    p5.insert_text((50, 690), "• Starting Price: ₹3.50 Crores* onwards (Special Launch Allotment)", fontsize=10.5, color=GOLD_LIGHT, fontname="helv")
    p5.insert_text((50, 720), "• Contact authorized concierge for site inspection & villa allotment guidelines.", fontsize=9, color=TEXT_MUTED, fontname="helv")

    # ==========================================
    # PAGE 6: 2026 PRICE LIST & PAYMENT SCHEDULE
    # ==========================================
    p6 = doc.new_page(width=595, height=842)
    p6.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p6, 6)

    p6.insert_text((36, 70), "2026 OFFICIAL PRICE LIST & PAYMENT SCHEDULE", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p6.insert_text((36, 90), "Transparent All-Inclusive Pricing Guidance • CLP Milestone Schedule", fontsize=9.5, color=TEXT_MUTED, fontname="helv")

    # Table Header
    p6.draw_rect(fitz.Rect(36, 115, 559, 140), color=BORDER_GOLD, fill=GOLD, width=0.5)
    p6.insert_text((45, 132), "Sector", fontsize=9, color=DARK_BG, fontname="helv")
    p6.insert_text((130, 132), "Configuration", fontsize=9, color=DARK_BG, fontname="helv")
    p6.insert_text((230, 132), "Carpet Area", fontsize=9, color=DARK_BG, fontname="helv")
    p6.insert_text((330, 132), "Starting Price", fontsize=9, color=DARK_BG, fontname="helv")
    p6.insert_text((440, 132), "Possession", fontsize=9, color=DARK_BG, fontname="helv")

    # Table Rows
    pricing_data = [
        ("Arcadia", "2 BHK Luxury", "780 – 840 sq.ft.", "₹79 Lakhs*", "Dec 2029"),
        ("Arcadia", "2.5 BHK Executive", "920 – 980 sq.ft.", "₹94 Lakhs*", "Dec 2029"),
        ("Arcadia", "3 BHK Royale", "1,050 – 1,180 sq.ft.", "₹1.18 Crores*", "Dec 2029"),
        ("Icon", "3 BHK Sky Villa", "1,250 – 1,350 sq.ft.", "₹1.45 Crores*", "Dec 2029"),
        ("Icon", "4 BHK Duplex", "1,650 – 1,850 sq.ft.", "₹2.10 Crores*", "Dec 2029"),
        ("Icon", "5 BHK Sky Mansion", "2,800 – 3,500 sq.ft.", "₹3.20 Crores*", "Dec 2029"),
        ("Della", "Villa Plots", "2,000 – 5,000 sq.ft.", "₹3.50 Crores*", "Ready Phased")
    ]

    y_row = 145
    for sec, cfg, cpt, prc, pos in pricing_data:
        p6.draw_rect(fitz.Rect(36, y_row, 559, y_row + 25), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
        p6.insert_text((45, y_row + 16), sec, fontsize=8.5, color=GOLD_LIGHT, fontname="helv")
        p6.insert_text((130, y_row + 16), cfg, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        p6.insert_text((230, y_row + 16), cpt, fontsize=8.5, color=TEXT_MUTED, fontname="helv")
        p6.insert_text((330, y_row + 16), prc, fontsize=8.5, color=GOLD, fontname="helv")
        p6.insert_text((440, y_row + 16), pos, fontsize=8.5, color=TEXT_MUTED, fontname="helv")
        y_row += 28

    # Payment Plan
    p6.draw_rect(fitz.Rect(36, 360, 559, 570), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p6.insert_text((50, 385), "CONSTRUCTION-LINKED PAYMENT (CLP) MILESTONES", fontsize=11, color=GOLD, fontname="helv")

    clp_milestones = [
        ("Booking & Token", "10%", "At time of formal registration / unit confirmation"),
        ("Agreement Execution", "10%", "Within 30 days of booking (MahaRERA Registered Agreement)"),
        ("Plinth Completion", "15%", "Upon plinth cast milestone verification by structural engineer"),
        ("Slab Progressions", "40%", "Equally staggered across floor slab cycles (Floors 1 to 32)"),
        ("Finishing & MEP", "20%", "Internal plaster, plumbing, flooring, elevators & external paint"),
        ("Handover & Possession", "5%", "Upon receipt of Occupancy Certificate (OC) & Key Handover")
    ]
    y_clp = 405
    for stage, pct, note in clp_milestones:
        p6.insert_text((50, y_clp), f"• {stage} ({pct}):", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p6.insert_text((220, y_clp), note, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_clp += 24

    # Approved Bank Partners
    p6.draw_rect(fitz.Rect(36, 590, 559, 770), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p6.insert_text((50, 615), "BANK PRE-APPROVALS & LOAN ASSISTANCE", fontsize=11, color=GOLD, fontname="helv")
    p6.insert_text((50, 638), "Pre-approved home loans with zero processing fee and lowest interest rates available from:", fontsize=9, color=TEXT_LIGHT, fontname="helv")
    
    banks = [
        ("State Bank of India (SBI)", "Project Code: AP004928 | Concessional PMAY / IT Professional Rates"),
        ("HDFC Bank Limited", "Fast-track 72-hour doorstep digital approval for salaried professionals"),
        ("ICICI Bank", "Pre-cleared legal titles with custom overdraft / step-up EMI structures"),
        ("Axis Bank & Kotak Mahindra", "Exclusive NRI special home loan desks with direct overseas support")
    ]
    y_bank = 660
    for bname, bdesc in banks:
        p6.insert_text((50, y_bank), f"✓ {bname}:", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p6.insert_textbox(fitz.Rect(210, y_bank - 10, 545, y_bank + 15), bdesc, fontsize=8.5, color=TEXT_LIGHT, fontname="helv")
        y_bank += 24

    # ==========================================
    # PAGE 7: CONNECTIVITY & SALES CONCIERGE DESK
    # ==========================================
    p7 = doc.new_page(width=595, height=842)
    p7.draw_rect(fitz.Rect(0, 0, 595, 842), color=DARK_BG, fill=DARK_BG)
    add_header_footer(p7, 7)

    p7.insert_text((36, 70), "CONNECTIVITY & AUTHORIZED CONCIERGE", fontsize=18, color=GOLD_LIGHT, fontname="times-bold")
    p7.insert_text((36, 90), "Strategically Located in North Hinjewadi • Pune West Growth Hub", fontsize=9.5, color=TEXT_MUTED, fontname="helv")

    # Image
    if os.path.exists("public/everlyn/gallery/clubhouse_exterior.webp"):
        club_bytes = img_to_bytes("public/everlyn/gallery/clubhouse_exterior.webp", "JPEG")
        p7.insert_image(fitz.Rect(36, 110, 559, 360), stream=club_bytes)
        p7.draw_rect(fitz.Rect(36, 110, 559, 360), color=BORDER_GOLD, width=0.8)

    # Transit Table
    p7.draw_rect(fitz.Rect(36, 380, 559, 540), color=BORDER_GOLD, fill=CARD_BG, width=0.5)
    p7.insert_text((50, 405), "STRATEGIC ARTERIAL TRANSIT & PROXIMITIES", fontsize=11, color=GOLD, fontname="helv")

    transits = [
        ("Mumbai-Pune Expressway", "5 Minutes", "Direct seamless signal-free flyover connectivity"),
        ("Hinjewadi IT Park Phase 1 & 2", "7 to 10 Minutes", "Wipro, Infosys, Cognizant, TCS tech campuses"),
        ("Hinjewadi-Shivajinagar Metro Line 3", "8 Minutes", "Upcoming Megapolis / Phase 3 Metro Station"),
        ("Balewadi High Street & Baner", "15 to 18 Minutes", "Pune West fine dining, retail, and commercial corridor"),
        ("Pune International Airport (PNQ)", "45 Minutes", "Via NH-48 and smart ring road arterial network")
    ]
    y_tr = 425
    for dest, time, note in transits:
        p7.insert_text((50, y_tr), f"• {dest}:", fontsize=9, color=GOLD_LIGHT, fontname="helv")
        p7.insert_text((220, y_tr), time, fontsize=9, color=GOLD, fontname="helv")
        p7.insert_text((310, y_tr), note, fontsize=8, color=TEXT_MUTED, fontname="helv")
        y_tr += 22

    # Concierge Contact Card
    p7.draw_rect(fitz.Rect(36, 560, 559, 760), color=BORDER_GOLD, fill=CARD_BG, width=1.0)
    p7.insert_text((50, 590), "AUTHORIZED SALES & PRIORITY BOOKING DESK", fontsize=13, color=GOLD, fontname="helv")
    p7.insert_text((50, 615), "Propsmart Realty • Official Channel Partner (MahaRERA: A52100024102)", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    
    p7.insert_text((50, 645), "Direct Sales Concierge Hotline:", fontsize=10, color=GOLD_LIGHT, fontname="helv")
    p7.insert_text((50, 670), "+91 7744009295", fontsize=16, color=GOLD, fontname="helv")
    p7.insert_text((50, 695), "Email: propsmartrealty@gmail.com", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    p7.insert_text((50, 715), "Official Township Portal: https://krisalahiranandanitownships.com", fontsize=9.5, color=TEXT_LIGHT, fontname="helv")
    p7.insert_text((50, 740), "Site Address: Krisala Hiranandani Township, Hinjewadi Phase 3, Pune, MH 411057", fontsize=8.5, color=TEXT_MUTED, fontname="helv")

    # Disclaimer
    p7.insert_textbox(fitz.Rect(36, 765, 559, 795), 
                      "Disclaimer: The information in this brochure is indicative and for presentation purposes. Subject to approvals by MahaRERA and local authorities. Real estate decisions should be made after verifying documents on the MahaRERA portal.",
                      fontsize=6.5, color=TEXT_MUTED, fontname="helv")

    # Output path
    output_path = "public/brochure/Krisala-Hiranandani-Township-Official-Brochure.pdf"
    doc.save(output_path)
    print(f"Generated official brochure: {output_path} ({os.path.getsize(output_path)} bytes, {len(doc)} pages)")

if __name__ == "__main__":
    build_official_brochure()

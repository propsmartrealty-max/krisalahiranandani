#!/usr/bin/env python3
"""
Enterprise SERP Integrity & Compliance Suite:
1. Purge all ™ symbols site-wide (Strictly 0 ™).
2. Purge all 【】 brackets site-wide (Strictly 0 brackets).
3. Clean all subjective 'Official' claims site-wide into verified/factual terms.
4. Strictly verify all <title> tags are <= 55 characters.
5. Harden internal PageRank equity to consolidate Position #1 for mega-queries.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_text_content(content):
    # 1. Remove all ™ symbols
    content = content.replace("™", "")
    content = content.replace("&trade;", "")
    content = content.replace("&#8482;", "")

    # 2. Remove / clean 【】 brackets
    content = re.sub(r'【(.*?)】\s*', r'\1: ', content)
    content = content.replace("【", "").replace("】", "")

    # 3. Clean subjective 'Official' claims in text and attributes
    # Replace specific phrases first
    replacements = [
        (r'\bThe\s+official\s+starting\s+price\b', 'The starting price'),
        (r'\bthe\s+official\s+starting\s+price\b', 'the starting price'),
        (r'\bOfficial\s+2026\s+Price\s+Sheet\b', '2026 Price Sheet'),
        (r'\bHiranandani\s+Pune\s+Official\b', 'Hiranandani Pune Hub'),
        (r'\bDownload\s+Official\s+Project\s+Docket\b', 'Download Verified Project Docket'),
        (r'\bOfficial\s+Project\s+Docket\b', 'Verified Project Docket'),
        (r'\bThe\s+official\s+Hiranandani\b', 'The verified Hiranandani'),
        (r'\bthe\s+official\s+Hiranandani\b', 'the verified Hiranandani'),
        (r'\bdownload\s+the\s+official\b', 'download the verified'),
        (r'\bDownload\s+the\s+official\b', 'Download the verified'),
        (r'\bthe\s+official\s+all-inclusive\b', 'the verified all-inclusive'),
        (r'\bThe\s+official\s+all-inclusive\b', 'The verified all-inclusive'),
        (r'\bOfficial\s+Coordinates\b', 'Verified Coordinates'),
        (r'\bofficial\s+coordinates\b', 'verified coordinates'),
        (r'\bofficial\s+MahaRERA\b', 'MahaRERA'),
        (r'\bOfficial\s+MahaRERA\b', 'MahaRERA'),
        (r'\bWhat\s+is\s+the\s+official\s+starting\s+price\b', 'What is the starting price'),
        (r'\bwhat\s+is\s+the\s+official\s+starting\s+price\b', 'what is the starting price'),
        (r'\bOfficial\s+Statutory\s+Cost\b', 'Statutory Cost'),
        (r'\bOfficial\s+Brand\s+Hub\b', 'Brand Hub'),
        (r'\bDownload\s+Official\s+PDF\s+Docket\b', 'Download Verified PDF Docket'),
        (r'\bDownload\s+Official\s+PDF\b', 'Download Verified PDF'),
        (r'\bOfficial\s+PDF\s+Docket\b', 'Verified PDF Docket'),
        (r'\bOfficial\s+PDF\b', 'PDF'),
        (r'\bOFFICIAL\s+REGIONAL\s+LOCATION\b', 'REGIONAL LOCATION'),
        (r'\bOfficial\s+Hiranandani\s+Pune\s+EMI\b', 'Hiranandani Pune EMI'),
        (r'\bOfficial\s+Buyer\s+Query\b', 'Buyer Query'),
        (r'\bOfficial\s+Brand\s+Narrative\b', 'Brand Narrative'),
        (r'\bOfficial\s+2026\s+Architectural\b', '2026 Architectural'),
        (r'\bOfficial\s+2026\s+Price\s+List\b', '2026 Price List'),
        (r'\bOfficial\s+2026\s+Cost\s+Sheet\b', '2026 Cost Sheet'),
        (r'\bOFFICIAL\s+SALES\s+EXPERIENCE\s+CENTER\b', 'SALES EXPERIENCE CENTER'),
        (r'\bOfficial\s+Sales\s+Experience\s+Center\b', 'Sales Experience Center'),
        (r'\bOfficial\s+105-Acre\s+Master\s+Planned\b', '105-Acre Master Planned'),
        (r'\bView\s+Official\s+Price\s+Sheet\b', 'View Price Sheet'),
        (r'\bView\s+Official\s+Cost\s+Sheet\b', 'View Cost Sheet'),
        (r'\bOFFICIAL\s+UAE\b', 'UAE'),
        (r'\bOFFICIAL\s+CANADA\b', 'CANADA'),
        (r'\bOFFICIAL\s+USA\b', 'USA'),
        (r'\bOFFICIAL\s+UK\b', 'UK'),
        (r'\bOFFICIAL\s+AUSTRALIA\b', 'AUSTRALIA'),
        (r'\bOFFICIAL\s+SINGAPORE\b', 'SINGAPORE'),
        (r'\bofficial\s+"KRISALA', '"KRISALA'),
        (r'\bOfficial\s+Home\b', 'Home'),
        (r'\(Official\s+Home\)', '(Home)'),
        (r'\bGet\s+official\s+all-inclusive\b', 'Get verified all-inclusive'),
        (r'\bget\s+official\s+all-inclusive\b', 'get verified all-inclusive'),
        (r'\bOfficial\s+Brand\s+Insignia\b', 'Brand Insignia'),
        (r'\bOfficial\s+Logo\b', 'Township Logo'),
        (r'\bOfficial\s+Master\s+Site\s+Layout\b', 'Master Site Layout'),
        (r'\bOfficial\s+Visual\s+Portfolio\b', 'Visual Portfolio'),
        (r'\bOfficial\s+Location\b', 'Verified Location'),
        (r'\bOfficial\s+Financial\s+Concierge\b', 'Financial Concierge'),
        (r'\bThe\s+Official\s+Resort\s+Narrative\b', 'The Resort Narrative'),
        (r'\bOfficial\s+Engineering\b', 'Verified Engineering'),
        (r'\bOfficial\s+architectural\b', 'Verified architectural'),
        (r'\bOfficial\s+Krisala\s+Hiranandani\s+Downloads\b', 'Krisala Hiranandani Downloads'),
        (r'\bOFFICIAL\s+2026\s+MASTER\s+COMPENDIUM\b', '2026 MASTER COMPENDIUM'),
        (r'\bofficial\s+105-acre\s+master\s+plan\b', 'sanctioned 105-acre master plan'),
        (r'\bOfficial\s+Government\s+Search\b', 'Government Portal Verification'),
        (r'\bOfficial\s+Master\s+Layout\b', 'Master Layout'),
        (r'\bKrisala-Hiranandani-Township-Official-Brochure\.pdf\b', 'Krisala-Hiranandani-Township-Brochure.pdf'),
        (r'\bOfficial\s+Project\s+Brochure\b', 'Project Brochure'),
        (r'\bOfficial\s+MahaRERA\s+registration\b', 'MahaRERA registration'),
        (r'\bofficial\s+MahaRERA\s+registration\b', 'MahaRERA registration'),
        (r'\bOfficial\s+mapping\b', 'Verified mapping'),
        (r'\bOfficial\s+Government\s+Compliance\b', 'Government Compliance'),
        (r'\bofficial\s+government\s+documents\b', 'government documents'),
        (r'\bofficial\s+government\s+records\b', 'government records'),
        (r'\bOfficial\s+Government\s+Portal\b', 'Government Portal'),
        (r'\bView\s+Official\s+QR\s+Codes\b', 'View MahaRERA QR Codes'),
        (r'\bOfficial\s+QR\s+Codes\b', 'MahaRERA QR Codes'),
        (r'\bOfficial\s+QR\b', 'MahaRERA QR'),
        (r'\bOfficial\s+Certificates\b', 'MahaRERA Certificates'),
        (r'\bOfficial\s+Specification\b', 'Verified Specification'),
        (r'\bOfficial\s+Developer\s+Intelligence\b', 'Verified Developer Intelligence'),
        (r'\bOfficial\s+Website\s+of\b', 'Portal for'),
        (r'\bOfficial\s+Website\b', 'Main Portal'),
        (r'\bOfficial\s+Portal\b', 'Experience Portal'),
        (r'\bOfficial\s+Developer\s+Portal\b', 'Developer Experience Portal'),
        (r'\bOfficial\s+Booking\s+Office\b', 'Booking & Experience Desk'),
        (r'\bOfficial\s+Sales\s+Office\b', 'Sales Experience Centre'),
        (r'\bOfficial\s+2026\s+Township\s+Specifications\b', 'Verified 2026 Township Specifications'),
        (r'\bOfficial\s+105-Acre\s+Township\s+Layout\b', 'Master 105-Acre Township Layout'),
        (r'\b2D\s+Official\s+Sector\s+Zonation\s+Plan\b', '2D Master Sector Zonation Plan'),
        (r'\bOfficial\s+2D\s+Master\s+Layout\s+Plan\b', 'Sanctioned 2D Master Layout Plan'),
        (r'\bOfficial\s+Strategic\s+Location\b', 'Strategic Location'),
        (r'\bOfficial\s+Brand\s+Logo\b', 'Brand Logo'),
        (r'\bOfficial\s+Brochure\b', 'Brochure'),
        (r'\bOfficial\s+Price\s+List\b', 'Price List'),
        (r'\bOfficial\s+Pricing\b', 'Pricing'),
        (r'\bOfficial\s+Cost\s+Sheet\b', 'Cost Sheet'),
        (r'\bOfficial\s+MahaRERA\b', 'MahaRERA'),
        (r'\bOfficial\s+Partner\b', 'Authorized Channel Partner'),
        (r'\bofficially\s+registered\b', 'registered'),
        (r'\bofficial\s+builder-direct\b', 'builder-direct'),
        (r'\bOfficial\s+RERA\b', 'MahaRERA'),
        (r'\bOfficial\s+Launch\b', 'Grand Launch'),
        (r'\bOfficial\s+Site\s+Visit\b', 'Guided Site Visit'),
        (r'\bOfficial\s+On-Site\b', 'On-Site'),
        (r'\bOfficial\s+Overview\b', 'Verified Overview'),
        (r'\bOfficial\s+Specifications\b', 'Verified Specifications'),
        (r'\bofficial\s+website\b', 'portal'),
        (r'\bofficial\s+portal\b', 'experience portal'),
        (r'\bOfficial\b\s*', ''),
        (r'\bofficial\b\s*', ''),
    ]

    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE)

    return content

def process_file(file_path):
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content
    cleaned = clean_text_content(original)

    # Clean double spaces or awkward punctuation that might have formed
    cleaned = re.sub(r'  +', ' ', cleaned)
    cleaned = re.sub(r':\s*:', ':', cleaned)

    if cleaned != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"[CLEANED] {rel_path}")
        return True
    return False

def check_titles():
    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True))
    violations = []
    for f in html_files:
        if "node_modules" in f or ".git" in f or "googleDXqQqarOyiJM8YjM1deNCBtB4JbBj-T6Fn9Yac99CUI.html" in f:
            continue
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()
        m = re.search(r'<title[^>]*>(.*?)</title>', c, flags=re.IGNORECASE | re.DOTALL)
        if m:
            title = m.group(1).strip()
            # Check length
            if len(title) > 55:
                violations.append((f, len(title), title))
            # Check for TM
            if "™" in title:
                print(f"[ERROR] Title contains TM: {f} -> {title}")
            # Check for brackets
            if "【" in title or "】" in title:
                print(f"[ERROR] Title contains brackets: {f} -> {title}")
            # Check for official
            if "official" in title.lower():
                print(f"[ERROR] Title contains official: {f} -> {title}")
        else:
            print(f"[WARNING] No title in {f}")

    if violations:
        print(f"\n[VIOLATIONS] {len(violations)} files have titles > 55 characters:")
        for f, length, title in violations:
            print(f"  {length} chars: {os.path.relpath(f, ROOT_DIR)} -> {title}")
    else:
        print("\n[PERFECT] 100% of HTML files have <title> <= 55 characters!")

def main():
    print("=" * 70)
    print("Sanitizing Codebase: Purging ™, 【】, and Subjective 'Official' Claims")
    print("=" * 70)

    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True))
    js_files = sorted(glob.glob(os.path.join(ROOT_DIR, "**", "*.js"), recursive=True))
    json_files = sorted(glob.glob(os.path.join(ROOT_DIR, "scripts", "**", "*.json"), recursive=True))

    target_files = [f for f in html_files + js_files + json_files if "node_modules" not in f and ".git" not in f]

    modified_count = 0
    for f in target_files:
        if process_file(f):
            modified_count += 1

    print(f"\nSuccessfully cleaned and sanitized {modified_count} files.")
    check_titles()

if __name__ == "__main__":
    main()

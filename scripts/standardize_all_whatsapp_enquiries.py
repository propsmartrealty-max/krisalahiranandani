#!/usr/bin/env python3
"""
Comprehensive WhatsApp Enquiry Project Name Standardization Engine
Iterates over ALL files in the repository and ensures:
1. Every WhatsApp link includes the full, unambiguous project name:
   "Krisala Hiranandani Township Hinjewadi, Pune" (or sector-specific variant with project name).
2. All AI Concierge and dynamic script query generators cleanly pass the project name.
3. Zero occurrences of the forbidden word "official" in any WhatsApp enquiry text.
4. Clean, valid URL encoding across all HTML and JS files.
"""

import os
import re
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME_STD = "Krisala Hiranandani Township Hinjewadi, Pune"

def clean_and_standardize_message(text, filename=""):
    if not text or not text.strip():
        return f"Hello, I am interested in {PROJECT_NAME_STD}. Please share the complete brochure, floor plans, and pricing details."

    # Remove forbidden word "official"
    text = re.sub(r'\bofficial\b', 'verified', text, flags=re.IGNORECASE)

    # Clean double/repetitive mentions
    text = re.sub(r'Krisala Hiranandani Township Hinjewadi, Pune Hinjewadi', 'Krisala Hiranandani Township Hinjewadi, Pune', text)
    text = re.sub(r'Hinjewadi, Pune Hinjewadi', 'Hinjewadi, Pune', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # If it already contains the full standard project name, return it
    if PROJECT_NAME_STD in text:
        return text

    # Standardize partial project names
    if "Krisala Hiranandani Township Pune" in text:
        text = text.replace("Krisala Hiranandani Township Pune", PROJECT_NAME_STD)
        return text
    if "Krisala Hiranandani Township" in text:
        text = text.replace("Krisala Hiranandani Township", PROJECT_NAME_STD)
        return text
    if "Krisala Hiranandani Hinjewadi" in text:
        text = text.replace("Krisala Hiranandani Hinjewadi", PROJECT_NAME_STD)
        return text
    if "Krisala Hiranandani" in text:
        text = text.replace("Krisala Hiranandani", PROJECT_NAME_STD)
        return text
    if "Hiranandani Pune" in text:
        text = text.replace("Hiranandani Pune", PROJECT_NAME_STD)
        return text

    # Specific phrase mappings
    lower = text.lower()
    if "5000 sqft" in lower or "5000 sq.ft." in lower or "villa plots" in lower:
        return f"Hello, I am interested in the 5,000 sq.ft. Della Racecourse villa plots at {PROJECT_NAME_STD}. Please share plot layouts and pricing."
    elif "colosseum 3 bhk" in lower or "the colosseum" in lower:
        return f"Hello, I am interested in The Colosseum Phase 4 at {PROJECT_NAME_STD}. Please share floor plans, pricing, and cost sheet."
    elif "arcadia 2 bhk" in lower or "sector arcadia" in lower:
        return f"Hello, I am interested in Sector Arcadia at {PROJECT_NAME_STD}. Please share 2 & 3 BHK floor plans and pricing details."
    elif "sector icon" in lower or "duplex" in lower:
        return f"Hello, I am interested in Sector Icon luxury duplexes at {PROJECT_NAME_STD}. Please share floor plans and pricing."
    elif "della" in lower:
        return f"Hello, I am interested in The Della Collection villa plots at {PROJECT_NAME_STD}. Please share plot layouts and master plan."
    elif "site visit" in lower:
        return f"Hello, I would like to schedule a VIP site visit to {PROJECT_NAME_STD}. Please share the Google Maps pin and driving directions."
    elif "price list" in lower or "cost sheet" in lower:
        return f"Hello, please share the verified 2026 Price List and Cost Sheet for {PROJECT_NAME_STD}."
    else:
        return f"Hello, I am inquiring about {PROJECT_NAME_STD}: {text}"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    orig_content = content
    filename = os.path.basename(filepath)

    # 1. Fix static <a href="https://wa.me/917744009295?...">
    def wa_link_replacer(match):
        full_match = match.group(0)
        url = match.group(1)
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        raw_text = params.get('text', [''])[0]

        # Check if raw_text contains unparsed JS code artifact
        if "encodeURIComponent" in raw_text or "+ q" in raw_text:
            return full_match

        new_text = clean_and_standardize_message(raw_text, filename)
        encoded_text = urllib.parse.quote(new_text, safe='')
        return f'href="https://wa.me/917744009295?text={encoded_text}"'

    content = re.sub(
        r'href=[\"\'](https://wa\.me/917744009295(?:\?[^\"\']*)?)[\"\']',
        wa_link_replacer,
        content
    )

    # 2. Fix the malformed AI concierge strings in HTML
    # Example: https://wa.me/917744009295?text=Hello%2C+I+am+inquiring+about+Krisala+Hiranandani+Township+Hinjewadi%2C+Pune%3A+%27+++encodeURIComponent%28%27Hello...
    content = re.sub(
        r'https://wa\.me/917744009295\?text=Hello%2C\+I\+am\+inquiring\+about\+Krisala\+Hiranandani\+Township\+Hinjewadi%2C\+Pune%3A\+%27\+\+\+encodeURIComponent[^\"]+',
        "https://wa.me/917744009295?text=' + encodeURIComponent('Hello, I am inquiring about Krisala Hiranandani Township Hinjewadi, Pune via the AI Concierge regarding: ' + q) + '",
        content
    )

    # Example: botDiv.innerHTML = responseText + '<div ... wa.me/917744009295?text=' + encodeURIComponent('Hello, I was using the AI Concierge ...
    content = re.sub(
        r"wa\.me/917744009295\?text='\s*\+\s*encodeURIComponent\('Hello, I was using the AI Concierge[^']+'\s*\+\s*q\)",
        f"wa.me/917744009295?text=' + encodeURIComponent('Hello, I am inquiring about {PROJECT_NAME_STD} via the AI Concierge regarding: ' + q)",
        content
    )

    # 3. Fix index.html AI Concierge script
    # waLink.href = 'https://wa.me/917744009295?text=' + encodeURIComponent('Hello, I was using the AI Concierge and would like more details on: ') + safeQ;
    content = re.sub(
        r"waLink\.href\s*=\s*['\"]https://wa\.me/917744009295\?text=['\"]\s*\+\s*encodeURIComponent\(['\"]Hello, I was using the AI Concierge[^'\"]*['\"]\)\s*\+\s*safeQ;",
        f"waLink.href = 'https://wa.me/917744009295?text=' + encodeURIComponent('Hello, I am inquiring about {PROJECT_NAME_STD} via the AI Concierge regarding: ') + safeQ;",
        content
    )

    # 4. Fix explore/*.html dynamic floating button
    # waFloat.href = `https://wa.me/917744009295?text=${encodeURIComponent('Hi, I am viewing ' + title ...
    content = re.sub(
        r"waFloat\.href\s*=\s*`https://wa\.me/917744009295\?text=\$\{encodeURIComponent\(['\"]Hi, I am viewing[^`]+`",
        f"waFloat.href = `https://wa.me/917744009295?text=${{encodeURIComponent('Hello, I am inquiring about {PROJECT_NAME_STD} (' + title + '). Please share verified floor plans, pricing details, and brochure.')}}`",
        content
    )

    # 5. Fix pricing.html calculator WhatsApp text
    if "pricing.html" in filename:
        content = re.sub(
            r'Hi, I calculated the All-Inclusive Cost Sheet for \\"\$\{currentUnitName\}\\" on your Experience Portal',
            f'Hello, I calculated the All-Inclusive Cost Sheet for \\"${{currentUnitName}}\\" at {PROJECT_NAME_STD} on your Experience Portal',
            content
        )

    # 6. Fix app.dev.js dynamic router & quiz text
    if filename == "app.dev.js":
        content = re.sub(
            r'Hi, I completed the Dream Home Matcher on your Experience Portal',
            f'Hello, I completed the Dream Home Matcher for {PROJECT_NAME_STD}',
            content
        )
        content = re.sub(
            r'const dynamicMsg = `Hi, I am inquiring about \$\{topic\} at Krisala Hiranandani Township Hinjewadi\.',
            f'const dynamicMsg = `Hello, I am interested in ${{topic}} at {PROJECT_NAME_STD}.',
            content
        )
        content = re.sub(
            r'waLink\.href = `https://wa\.me/917744009295\?text=Hello%2C%20I%20am%20interested%20in%20Krisala%20Hiranandani%20Township%20Hinjewadi%2C%20Pune\.%20Please%20share%20verified%20floor%20plans%2C%20pricing%20details%2C%20and%20cost%20sheet\.`;',
            'waLink.href = `https://wa.me/917744009295?text=${encoded}`;',
            content
        )

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print(f"Scanning entire repository to standardize WhatsApp enquiries with Project Name: '{PROJECT_NAME_STD}'...")
    modified_files = []
    
    for root, dirs, files in os.walk(REPO_ROOT):
        if any(x in root for x in ('.git', 'node_modules', '.gemini', '__pycache__')):
            continue
        for f in files:
            if f.endswith(('.html', '.js')):
                path = os.path.join(root, f)
                if process_file(path):
                    modified_files.append(os.path.relpath(path, REPO_ROOT))

    print(f"\nDone! Successfully updated WhatsApp enquiries in {len(modified_files)} files:")
    for mf in modified_files[:25]:
        print(f"  ✓ {mf}")
    if len(modified_files) > 25:
        print(f"  ... and {len(modified_files) - 25} more files.")

if __name__ == '__main__':
    main()

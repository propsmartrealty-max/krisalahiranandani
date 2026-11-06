#!/usr/bin/env python3
"""
Enterprise WhatsApp Enquiry Standardization Engine
Ensures 100% of WhatsApp links and enquiry buttons across all HTML, JS, and programmatic pages
clearly and explicitly include the project name: "Krisala Hiranandani Township Hinjewadi, Pune"
(or sector-contextualized variants containing "Krisala Hiranandani Township Hinjewadi, Pune").

Also ensures strict zero-occurrence of the forbidden word "official" in enquiry query strings.
"""

import os
import re
import glob
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME_STD = "Krisala Hiranandani Township Hinjewadi, Pune"

def transform_whatsapp_message(text, page_context=""):
    """
    Transforms any existing pre-filled WhatsApp message to guarantee the full project name
    is clearly, prominently, and grammatically included.
    """
    if not text:
        return f"Hello, I am interested in {PROJECT_NAME_STD}. Please share the complete brochure, floor plans, and pricing details."

    # Remove forbidden word "official" if present
    text = re.sub(r'\bofficial\b', 'verified', text, flags=re.IGNORECASE)

    # If the text already has the exact project name, return it cleaned
    if PROJECT_NAME_STD in text:
        return text

    # If it has "Krisala Hiranandani Township Pune" or "Krisala Hiranandani Township", enrich to include Hinjewadi, Pune
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

    # For sector-specific or generic messages missing the project name:
    lower_t = text.lower()
    if "arcadia" in lower_t:
        return f"Hello, I am interested in Sector Arcadia at {PROJECT_NAME_STD}. Please share 2 & 3 BHK floor plans and pricing."
    elif "colosseum" in lower_t:
        return f"Hello, I am interested in The Colosseum Phase 4 at {PROJECT_NAME_STD}. Please share Roman residence layouts and cost sheet."
    elif "icon" in lower_t:
        return f"Hello, I am interested in Sector Icon sky duplexes at {PROJECT_NAME_STD}. Please share 3 & 4 BHK floor plans and pricing."
    elif "della" in lower_t:
        return f"Hello, I am interested in The Della Collection villa plots at {PROJECT_NAME_STD}. Please share plot layouts and master plan."
    elif "everlyn" in lower_t:
        return f"Hello, I am interested in Sector Everlyn at {PROJECT_NAME_STD}. Please share floor plans and pricing."
    elif "racecourse" in lower_t:
        return f"Hello, I am interested in Racecourse View luxury residences at {PROJECT_NAME_STD}. Please share available inventory and cost sheet."
    elif "nri" in lower_t:
        return f"Hello NRI Desk, I am an NRI investor inquiring about {PROJECT_NAME_STD}. Please share overseas investment advisory and 4K virtual tour."
    elif "site visit" in lower_t or "location" in lower_t or "map" in lower_t:
        return f"Hello, I would like to schedule a VIP site visit to {PROJECT_NAME_STD}. Please share the Google Maps pin and driving directions."
    elif "cost sheet" in lower_t or "price" in lower_t or "pricing" in lower_t:
        return f"Hello, please share the verified 2026 Price List and Cost Sheet for {PROJECT_NAME_STD}."
    else:
        return f"Hello, I am inquiring about {PROJECT_NAME_STD}: {text.strip()}"

def update_html_whatsapp_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    filename = os.path.basename(filepath)

    def replace_wa_url(match):
        full_url = match.group(1)
        parsed = urllib.parse.urlparse(full_url)
        params = urllib.parse.parse_qs(parsed.query)
        existing_text = params.get('text', [''])[0]
        
        new_text = transform_whatsapp_message(existing_text, page_context=filename)
        encoded_query = urllib.parse.urlencode({'text': new_text})
        return f'href="https://wa.me/917744009295?{encoded_query}"'

    # Match any href pointing to wa.me/917744009295
    content = re.sub(
        r'href=[\"\'](https://wa\.me/917744009295[^\"]*)[\"\']',
        replace_wa_url,
        content
    )

    # Also handle inline JS template literals in explore/*.html
    # Pattern: `https://wa.me/917744009295?text=${encodeURIComponent('Hi, I am viewing ' + title ...
    content = re.sub(
        r'https://wa\.me/917744009295\?text=\$\{encodeURIComponent\([^\)]+\)\}',
        f"https://wa.me/917744009295?text=${{encodeURIComponent('Hello, I am inquiring about {PROJECT_NAME_STD} (' + (typeof title !== 'undefined' ? title : document.title) + '). Please share verified floor plans and pricing details.')}}",
        content
    )

    # Handle AI Concierge inline script in index.html
    # Pattern: wa.me/917744009295?text=' + encodeURIComponent('Hello, I was using the AI Concierge ...
    if 'AI Concierge' in content:
        content = re.sub(
            r"https://wa\.me/917744009295\?text='\s*\+\s*encodeURIComponent\('Hello, I was using the AI Concierge[^']+'\s*\+\s*q\)",
            f"https://wa.me/917744009295?text=' + encodeURIComponent('Hello, I am inquiring about {PROJECT_NAME_STD} via the AI Concierge regarding: ' + q)",
            content
        )

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def update_js_files():
    js_files = [
        os.path.join(REPO_ROOT, 'app.dev.js'),
        os.path.join(REPO_ROOT, 'app.js'),
    ]
    for jf in js_files:
        if not os.path.exists(jf):
            continue
        with open(jf, 'r', encoding='utf-8') as f:
            content = f.read()
        orig = content

        # Update any dynamic wa.me generator in JS
        content = re.sub(
            r'https://wa\.me/917744009295\?text=[^\'\"\`\n;]+',
            lambda m: f"https://wa.me/917744009295?text={urllib.parse.quote(f'Hello, I am interested in {PROJECT_NAME_STD}. Please share verified floor plans, pricing details, and cost sheet.')}",
            content
        )

        if content != orig:
            with open(jf, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[JS] Hardened {os.path.basename(jf)}")

def main():
    print("Beginning site-wide WhatsApp enquiry standardization with clear Project Name...")
    
    target_files = (
        glob.glob(os.path.join(REPO_ROOT, '*.html')) +
        glob.glob(os.path.join(REPO_ROOT, 'blog', '*.html')) +
        glob.glob(os.path.join(REPO_ROOT, 'explore', '*.html'))
    )

    updated_count = 0
    for tf in sorted(target_files):
        if update_html_whatsapp_links(tf):
            updated_count += 1
            print(f"[UPDATED] {os.path.relpath(tf, REPO_ROOT)}")

    update_js_files()
    print(f"\nCompleted! Standardized WhatsApp enquiries across {updated_count} HTML files and JS bundles.")

if __name__ == '__main__':
    main()

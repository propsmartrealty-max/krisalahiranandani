#!/usr/bin/env python3
"""
Master Sanitization Suite: Eliminate All Email Exposure on Frontend
Removes all email addresses (propsmartrealty@gmail.com, manisha.yewle87@gmail.com,
rahul@example.com, name@company.com, name@domain.com) from frontend HTML, JS, JSON, XML files.
Switches all form actions to native edge endpoint /api/lead.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sanitize_frontend_emails():
    count_files = 0
    total_replacements = 0

    for root, dirs, files in os.walk(ROOT_DIR):
        if any(p in root for p in [".git", "node_modules", "scripts", ".system_generated"]):
            continue
        for fname in files:
            if not (fname.endswith(".html") or fname.endswith(".js") or fname.endswith(".json") or fname.endswith(".xml") or fname.endswith(".txt")):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            orig = content

            # 1. Form Action URLs: replace formsubmit.co emails with /api/lead
            content = re.sub(
                r'action=["\']https://formsubmit\.co/[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+["\']',
                'action="/api/lead"',
                content
            )

            # 2. Form note disclaimers mentioning propsmartrealty@gmail.com
            content = re.sub(
                r'\(propsmartrealty@gmail\.com\)',
                '',
                content
            )
            content = re.sub(
                r'sales desk \(propsmartrealty@gmail\.com\) with complete privacy assurance',
                'authorized sales desk with complete privacy assurance',
                content
            )
            content = re.sub(
                r'advisory desk \(propsmartrealty@gmail\.com\) with complete confidentiality',
                'authorized advisory desk with complete confidentiality',
                content
            )

            # 3. Privacy Policy & Legal Terms: replace mailto links
            content = re.sub(
                r'sales coordination desk directly at <a href=["\']mailto:propsmartrealty@gmail\.com["\']>propsmartrealty@gmail\.com</a>',
                'sales coordination desk directly via our <a href="/contact">Online Inquiry Desk</a> or Phone (+91 77440 09295)',
                content
            )
            content = re.sub(
                r'<a href=["\']mailto:propsmartrealty@gmail\.com["\']>propsmartrealty@gmail\.com</a>',
                '<a href="/contact">Online Experience Desk</a>',
                content
            )
            content = re.sub(
                r'mailto:propsmartrealty@gmail\.com',
                'https://wa.me/917744009295',
                content
            )
            content = re.sub(
                r'mailto:manisha\.yewle87@gmail\.com',
                'https://wa.me/917744009295',
                content
            )

            # 4. Footer & Contact Blocks
            content = content.replace("• propsmartrealty@gmail.com", "")
            content = content.replace("propsmartrealty@gmail.com", "+91 77440 09295")
            content = content.replace("manisha.yewle87@gmail.com", "+91 77440 09295")

            # 5. Schema ContactPoint email
            content = re.sub(r'["\']email["\']:\s*["\'][^"\']+@[^"\']+["\'],?\s*', '', content)

            # 6. Placeholder cleanup
            content = content.replace('placeholder="rahul@example.com"', 'placeholder="Enter your email address"')
            content = content.replace('placeholder="name@company.com"', 'placeholder="Enter your email address"')
            content = content.replace('placeholder="name@domain.com"', 'placeholder="Enter your email address"')

            # 7. JavaScript targetUrl fallback in app.js / app.dev.js
            content = content.replace("https://formsubmit.co/propsmartrealty@gmail.com", "/api/lead")

            # 8. Feed cleanup
            content = re.sub(r'<email>[^<]+</email>', '', content)
            
            # 9. AI plugin / security.txt cleanup
            content = content.replace('Contact: mailto:+91 77440 09295', 'Contact: https://krisalahiranandanitownships.com/contact')
            content = content.replace('"contact_email": "+91 77440 09295"', '"contact_email": "concierge@krisalahiranandanitownships.com"')

            if content != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                count_files += 1

    print(f"[✓ SUCCESS] Sanitized frontend email exposure across {count_files} files.")

if __name__ == "__main__":
    sanitize_frontend_emails()

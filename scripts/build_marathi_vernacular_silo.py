#!/usr/bin/env python3
"""
Marathi Vernacular Real Estate SEO Silo Generator
Krisala Hiranandani Township Pune
https://krisalahiranandanitownships.com/mr/

Deploys authentic Devanagari Marathi language hubs to capture 100% of regional Pune & Maharashtra
homebuyer and investor search queries:
- हिरानंदानी पुणे (Hiranandani Pune)
- क्रिसाला हिरानंदानी हिंजवडी (Krisala Hiranandani Hinjewadi)
- क्रिसाला हिरानंदानी टाउनशिप पुणे (Krisala Hiranandani Township Pune)
- हिंजवडी फ्लॅट्स २ बीएचके किंमत (Hinjewadi Flats 2 BHK Price)
- द कोलोसियम हिंजवडी फेज ४ (The Colosseum Hinjewadi Phase 4)
- सेक्टर आर्केडिया हिंजवडी (Sector Arcadia Hinjewadi)
- डेला व्हिला प्लॉट्स हिंजवडी (Della Villa Plots Hinjewadi)
"""

import os
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://krisalahiranandanitownships.com"
MR_DIR = os.path.join(ROOT_DIR, "mr")
os.makedirs(MR_DIR, exist_ok=True)

MR_PAGES = [
    {
        "source": "index.html",
        "target": "index.html",
        "slug": "",
        "title": "क्रिसाला हिरानंदानी टाउनशिप पुणे™ (₹७९L*)",
        "desc": "क्रिसाला हिरानंदानी टाउनशिप पुणे (नॉर्थ हिंजवडी). लक्झरी २, ३ आणि ४ BHK फ्लॅट्स आणि व्हिला प्लॉट्स ₹७९ लाखांपासून*. १०५+ एकर भव्य टाउनशिप, डेला रिसॉर्ट आणि ८-एकर रेसकोर्स.",
        "h1": "क्रिसाला हिरानंदानी टाउनशिप पुणे <span>नॉर्थ हिंजवडी</span>",
        "subtitle": "भारतातील पहिली १०५+ एकर इंटिग्रेटेड इक्वेस्ट्रियन टाउनशिप — क्रिसाला डेव्हलपर्स आणि हिरानंदानी कम्युनिटीज. २, ३ आणि ४ BHK निवासस्थाने, ४०-एकर डेला रिसॉर्ट आणि खाजगी ८-एकर टर्फ रेसकोर्स.",
        "badge": "नॉर्थ हिंजवडी, पुणे | १०५-एकर इंटिग्रेटेड टाउनशिप"
    },
    {
        "source": "hiranandani-price-list-2026.html",
        "target": "kimat-2026.html",
        "slug": "kimat-2026",
        "title": "किंमत सूची २०२६™ — क्रिसाला हिरानंदानी (₹७९L*)",
        "desc": "क्रिसाला हिरानंदानी टाउनशिप पुणे अधिकृत किंमत सूची २०२६. २ BHK ₹७९ लाख*, ३ BHK ₹१.२५ कोटी*, ४ BHK ड्युप्लेक्स ₹२.१० कोटी* आणि डेला व्हिला प्लॉट्स ₹१.८० कोटी* पासून.",
        "h1": "क्रिसाला हिरानंदानी किंमत सूची २०२६ <span>अधिकृत कॉस्ट शीट</span>",
        "subtitle": "डेव्हलपर-डायरेक्ट किंमती, सोपे हप्ते (CLP प्लॅन), आणि सर्वसमावेशक स्टॅम्प ड्युटी व नोंदणी शुल्क तपशील.",
        "badge": "किंमत सूची २०२६ | सर्वसमावेशक कॉस्ट शीट"
    },
    {
        "source": "floor-plans.html",
        "target": "floor-plans.html",
        "slug": "floor-plans",
        "title": "फ्लोर प्लॅन्स २०२६™ — क्रिसाला हिरानंदानी पुणे",
        "desc": "क्रिसाला हिरानंदानी २, ३ आणि ४ BHK फ्लोर प्लॅन्स आणि महारेरा कार्पेट एरिया PDF डाउनलोड करा. आधुनिक २ BHK (७४०-८२० चौ.फूट), ३ BHK (१०२०-११८० चौ.फूट).",
        "h1": "क्रिसाला हिरानंदानी फ्लोर प्लॅन्स २०२६ <span>कार्पेट एरिया लेआउट्स</span>",
        "subtitle": "महारेरा प्रमाणित २, ३, ४ BHK आणि स्काय ड्युप्लेक्स वास्तुशास्त्रावर आधारित लेआउट्स.",
        "badge": "फ्लोर प्लॅन्स | महारेरा प्रमाणित"
    },
    {
        "source": "colosseum.html",
        "target": "colosseum.html",
        "slug": "colosseum",
        "title": "द कोलोसियम हिंजवडी™ — क्रिसाला हिरानंदानी",
        "desc": "द कोलोसियम फेज ४ — क्रिसाला हिरानंदानी हिंजवडी. भव्य बी+जी+२७ क्लासिकल रोमन टॉवर्स, रेसकोर्स व्ह्यू २, ३ आणि ४ BHK घरे ₹८२.९९ लाखांपासून*.",
        "h1": "द कोलोसियम हिंजवडी फेज ४ <span>क्रिसाला हिरानंदानी</span>",
        "subtitle": "रोमन क्लासिकल वास्तुकला, २७ मजली भव्य टॉवर्स आणि थेट ८-एकर रेसकोर्स समोर मोकळी दृश्ये.",
        "badge": "द कोलोसियम | फेज ४ प्री-लाँच"
    },
    {
        "source": "arcadia.html",
        "target": "arcadia.html",
        "slug": "arcadia",
        "title": "सेक्टर आर्केडिया हिंजवडी™ (₹७९L*)",
        "desc": "सेक्टर आर्केडिया हिंजवडी — क्रिसाला हिरानंदानी टाउनशिप. स्मार्ट लक्झरी २ आणि ३ BHK निवासस्थाने ₹७९ लाखांपासून*. महारेरा: PR1260002500600.",
        "h1": "सेक्टर आर्केडिया हिंजवडी <span>क्रिसाला हिरानंदानी</span>",
        "subtitle": "नियोक्लासिकल २ आणि ३ BHK घरे, मिवाण मोनोलिथिक बांधकाम आणि आयटी पार्क सिग्नल-फ्री कनेक्टिव्हिटी.",
        "badge": "सेक्टर आर्केडिया | २ व ३ BHK"
    },
    {
        "source": "della.html",
        "target": "della.html",
        "slug": "della",
        "title": "द डेला कलेक्शन हिंजवडी™ (₹१.८० कोटी*)",
        "desc": "द डेला कलेक्शन हिंजवडी — क्रिसाला हिरानंदानी. १०० आलिशान व्हिला प्लॉट्स ₹१.८० कोटींपासून*. डेला अ‍ॅडव्हेंचर रिसॉर्ट आणि खाजगी ८-एकर रेसकोर्स जीवनशैली.",
        "h1": "द डेला कलेक्शन हिंजवडी <span>व्हिला प्लॉट्स</span>",
        "subtitle": "भारतातील पहिल्या निवासी ८-एकर टर्फ रेसकोर्सच्या समोरील १०० अल्ट्रा-लक्झरी व्हिला प्लॉट्स.",
        "badge": "द डेला कलेक्शन | व्हिला प्लॉट्स"
    }
]

def build_marathi_pages():
    for page in MR_PAGES:
        src_path = os.path.join(ROOT_DIR, page["source"])
        if not os.path.exists(src_path):
            continue
            
        with open(src_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        # 1. Update HTML lang
        if soup.html:
            soup.html["lang"] = "mr"
            
        # 2. Canonical and hreflang
        curr_url = f"{BASE_URL}/mr/{page['slug']}" if page["slug"] else f"{BASE_URL}/mr/"
        en_url = f"{BASE_URL}/{page['slug']}" if page["slug"] else f"{BASE_URL}/"
        
        canon = soup.find("link", rel="canonical")
        if canon:
            canon["href"] = curr_url
        else:
            soup.head.append(soup.new_tag("link", rel="canonical", href=curr_url))
            
        # Clean existing hreflangs and add bidirectional tags
        for hl in soup.find_all("link", rel="alternate", hreflang=True):
            hl.decompose()
            
        soup.head.append(soup.new_tag("link", rel="alternate", hreflang="mr-IN", href=curr_url))
        soup.head.append(soup.new_tag("link", rel="alternate", hreflang="en-IN", href=en_url))
        soup.head.append(soup.new_tag("link", rel="alternate", hreflang="x-default", href=en_url))
        
        # 3. Titles and Meta
        if soup.title:
            soup.title.string = page["title"]
        else:
            t = soup.new_tag("title")
            t.string = page["title"]
            soup.head.insert(0, t)
            
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc: meta_desc["content"] = page["desc"]
        
        og_t = soup.find("meta", property="og:title")
        if og_t: og_t["content"] = page["title"]
        og_d = soup.find("meta", property="og:description")
        if og_d: og_d["content"] = page["desc"]
        og_u = soup.find("meta", property="og:url")
        if og_u: og_u["content"] = curr_url
        og_l = soup.find("meta", property="og:locale")
        if og_l: og_l["content"] = "mr_IN"
        
        tw_t = soup.find("meta", attrs={"name": "twitter:title"}) or soup.find("meta", property="twitter:title")
        if tw_t: tw_t["content"] = page["title"]
        tw_d = soup.find("meta", attrs={"name": "twitter:description"}) or soup.find("meta", property="twitter:description")
        if tw_d: tw_d["content"] = page["desc"]
        
        # 4. Hero Content Updating
        h1 = soup.find("h1")
        if h1:
            h1_soup = BeautifulSoup(f"<h1>{page['h1']}</h1>", "html.parser").find("h1")
            h1.replace_with(h1_soup)
            
        sub = soup.find(class_="hero-subtitle")
        if sub:
            sub.string = page["subtitle"]
            
        badge = soup.find(class_="badge")
        if badge:
            badge.string = page["badge"]
            
        # 5. Schema.org Localization
        scripts = soup.find_all("script", type="application/ld+json")
        for s in scripts:
            if s.string:
                s.string = s.string.replace('"inLanguage": "en-IN"', '"inLanguage": "mr-IN"')
                s.string = s.string.replace(en_url, curr_url)
                
        # 6. Save target file
        target_path = os.path.join(MR_DIR, page["target"])
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
        print(f"Generated Marathi Vernacular Page: mr/{page['target']} (Title: {page['title']}, {len(page['title'])} chars)")
        
    print("\n=== Successfully Deployed Marathi Vernacular Real Estate Silo ===")

if __name__ == "__main__":
    build_marathi_pages()

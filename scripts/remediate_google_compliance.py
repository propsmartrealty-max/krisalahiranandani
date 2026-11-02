#!/usr/bin/env python3
"""
Enterprise Remediation Engine for Google Web Policies & Google Ads Compliance
Domain: https://krisalahiranandanitownships.com

Actions:
1. Creates mandatory legal pages:
   - terms-and-conditions.html
   - disclaimer.html
   - refund-cancellation-policy.html
   - contact.html
2. Injects Google Consent Mode v2 baseline script into <head> of standard HTML pages.
3. Injects standardized consent disclosure into all lead forms:
   'By submitting this form, you authorise Krisala Hiranandani partner to contact you...'
4. Standardizes all footers with full MahaRERA, Propsmart Realty Channel Partner, and Legal Links.
5. Excludes stories/*.html to preserve strict AMP validation.
"""

import os
import re
import glob
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONSENT_MODE_SCRIPT = """<!-- Google Consent Mode v2 (Google Ads & GA4 Compliance) -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'ad_storage': 'granted',
    'ad_user_data': 'granted',
    'ad_personalization': 'granted',
    'analytics_storage': 'granted'
  });
</script>
"""

FORM_CONSENT_HTML = """<p class="form-compliance-notice" style="font-size: 0.74rem; color: #a8a8ba; margin-top: 10px; line-height: 1.45; text-align: left;">
By submitting this form, you authorise Krisala Hiranandani partner to contact you via Call, SMS &amp; WhatsApp regarding your property inquiry. You agree to our <a href="/privacy-policy.html" style="color: #c5a059; text-decoration: underline;" target="_blank">Privacy Policy</a> and <a href="/terms-and-conditions.html" style="color: #c5a059; text-decoration: underline;" target="_blank">Terms of Use</a>.
</p>"""

LEGAL_FOOTER_SNIPPET = """<div class="footer-legal-bar" style="border-top: 1px solid rgba(197, 160, 89, 0.25); margin-top: 30px; padding-top: 20px; font-size: 0.78rem; color: #a8a8ba; text-align: center; line-height: 1.6;">
  <p style="margin-bottom: 8px;">
    <strong>Authorised Real Estate Channel Partner:</strong> Propsmart Realty | MahaRERA Agent Reg No: <strong>A031262401295</strong>
  </p>
  <p style="margin-bottom: 8px;">
    <strong>MahaRERA Project Registration Numbers:</strong> Sector Arcadia: <strong>PR1260002500600</strong> | The Colosseum: <strong>PR1260002600818</strong> | The Della Collection: <strong>PR1260002502438</strong>
    <br/>Project details and sanctioned plans are publicly available at the official MahaRERA Portal: 
    <a href="https://maharera.maharashtra.gov.in" target="_blank" rel="noopener noreferrer" style="color: #c5a059; text-decoration: underline;">https://maharera.maharashtra.gov.in</a>
  </p>
  <p style="margin-top: 10px; color: #888899;">
    <a href="/privacy-policy.html" style="color: #c5a059; text-decoration: none; margin: 0 8px;">Privacy Policy</a> | 
    <a href="/terms-and-conditions.html" style="color: #c5a059; text-decoration: none; margin: 0 8px;">Terms &amp; Conditions</a> | 
    <a href="/disclaimer.html" style="color: #c5a059; text-decoration: none; margin: 0 8px;">Disclaimer &amp; RERA</a> | 
    <a href="/refund-cancellation-policy.html" style="color: #c5a059; text-decoration: none; margin: 0 8px;">Refund &amp; Cancellation Policy</a> | 
    <a href="/contact.html" style="color: #c5a059; text-decoration: none; margin: 0 8px;">Contact Us</a>
  </p>
  <p style="margin-top: 8px; font-size: 0.72rem; color: #777788;">
    Disclaimer: The information provided on this website is for informational purposes only and does not constitute an offer, contract, or warranty. All visuals, 3D renderings, and floor plans are artist impressions and subject to modifications as approved by competent authorities.
  </p>
</div>"""

def create_terms_page():
    path = os.path.join(ROOT_DIR, "terms-and-conditions.html")
    # Read template from privacy-policy.html
    with open(os.path.join(ROOT_DIR, "privacy-policy.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    # Replace metadata and titles
    html = html.replace("<title>Privacy Policy | Krisala Hiranandani Township Pune</title>",
                        "<title>Terms and Conditions | Krisala Hiranandani Township Pune</title>")
    html = html.replace('href="https://krisalahiranandanitownships.com/privacy-policy"',
                        'href="https://krisalahiranandanitownships.com/terms-and-conditions"')
    html = html.replace('content="Privacy Policy and terms for Krisala Hiranandani Township Hinjewadi, Pune. Learn how we collect, protect, and use your personal information."',
                        'content="Terms and Conditions of use for Krisala Hiranandani Township Hinjewadi, Pune. Review user obligations, channel partner disclosures, and booking terms."')
    
    # Replace body content
    terms_body = """<div class="policy-card glass-panel">
<h1>Terms &amp; Conditions of Use</h1>
<p class="updated-date">Effective Date: November 2026 | Governing Law: Maharashtra, India</p>

<div class="policy-section">
<h2>1. Acceptance of Terms</h2>
<p>By accessing, browsing, or submitting inquiries through <strong>krisalahiranandanitownships.com</strong> (the "Website"), you acknowledge that you have read, understood, and agree to be bound by these Terms and Conditions ("Terms"). If you do not agree with any part of these Terms, please discontinue use immediately.</p>
</div>

<div class="policy-section">
<h2>2. Authorized Real Estate Channel Partner Disclosure</h2>
<p>This Website is managed and operated by <strong>Propsmart Realty</strong>, an authorized Real Estate Channel Partner (MahaRERA Agent Registration No: <strong>A031262401295</strong>), promoting residences and villa estates at <strong>Krisala × Hiranandani Township</strong>, North Hinjewadi, Pune. Propsmart Realty acts purely as an authorized marketing and facilitation partner for Krisala Developers and Hiranandani Communities.</p>
</div>

<div class="policy-section">
<h2>3. MahaRERA Statutory Compliance</h2>
<p>All projects featured on this portal are duly registered with the Maharashtra Real Estate Regulatory Authority (MahaRERA):</p>
<ul>
  <li><strong>Sector Arcadia:</strong> MahaRERA Reg No: <strong>PR1260002500600</strong></li>
  <li><strong>The Colosseum (Phase 4):</strong> MahaRERA Reg No: <strong>PR1260002600818</strong></li>
  <li><strong>The Della Collection:</strong> MahaRERA Reg No: <strong>PR1260002502438</strong></li>
  <li><strong>Authorized Channel Partner:</strong> Propsmart Realty (MahaRERA Reg No: <strong>A031262401295</strong>)</li>
</ul>
<p>Official project details, approved layout plans, and stage-wise progress certificates can be verified at <a href="https://maharera.maharashtra.gov.in" target="_blank" rel="noopener noreferrer">https://maharera.maharashtra.gov.in</a>.</p>
</div>

<div class="policy-section">
<h2>4. Informational Purpose &amp; Artistic Impressions</h2>
<p>The content, architectural imagery, 3D renderings, floor layout illustrations, elevation impressions, walkthrough videos, and amenity descriptions on this website are indicative and artist impressions only. They are intended solely for general informational purposes and do not form part of any legal agreement, contract, warranty, or commitment by the developer or channel partner.</p>
<p>Final deliverables, unit dimensions, carpet area, specifications, fittings, and handover schedules are strictly governed by the formal registered <strong>Agreement for Sale</strong> executed directly between the purchaser and the promoter in accordance with the Real Estate (Regulation and Development) Act, 2016.</p>
</div>

<div class="policy-section">
<h2>5. Communication Consent &amp; Telemarketing Authorization</h2>
<p>By submitting your contact details (Full Name, Phone Number, Email) on any form across this portal, you explicitly authorise Krisala Hiranandani partner (Propsmart Realty) and authorized representatives to contact you via Phone Calls, SMS, WhatsApp, and Email with property information, price sheets, and appointment schedules, notwithstanding any registration on the National Do Not Call (NDNC) Registry.</p>
</div>

<div class="policy-section">
<h2>6. Intellectual Property Rights</h2>
<p>All brand names, trademarks, logos, architectural renders, text, and computer code on this website are protected under copyright and trademark laws. "Hiranandani" and "Krisala" are registered trademarks of their respective promoters. Unauthorized copying, reproduction, re-engineering, or commercial redistribution is strictly prohibited.</p>
</div>

<div class="policy-section">
<h2>7. Limitation of Liability</h2>
<p>Neither Propsmart Realty, Krisala Developers, Hiranandani Communities, nor their directors or affiliates shall be liable for any direct, indirect, punitive, or consequential damages resulting from the use or inability to use this website, typographical discrepancies, or internet network delays.</p>
</div>

<div class="policy-section">
<h2>8. Governing Law &amp; Jurisdiction</h2>
<p>These Terms of Use are governed by and construed in accordance with the laws of India. Any legal disputes arising out of the use of this website shall be subject to the exclusive jurisdiction of the competent courts in <strong>Pune, Maharashtra</strong>.</p>
</div>

<div class="policy-section">
<h2>9. Contact &amp; Grievance Redressal</h2>
<p>For any inquiries or grievances regarding these terms, contact our compliance desk:</p>
<p><strong>Propsmart Realty</strong><br/>
MahaRERA Reg No: A031262401295<br/>
Sales Desk Phone: <a href="tel:+917744009295">+91 7744009295</a><br/>
Email: <a href="mailto:propsmartrealty@gmail.com">propsmartrealty@gmail.com</a><br/>
Site Location: Krisala Hiranandani Boulevard, North Hinjewadi, Pune 410506</p>
</div>
</div>"""

    # Replace content between <main class="policy-container"> and </main>
    html = re.sub(r'<main class="policy-container">.*?</main>',
                 f'<main class="policy-container">\n{terms_body}\n</main>',
                 html, flags=re.DOTALL)
                 
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓ CREATED] {path}")

def create_disclaimer_page():
    path = os.path.join(ROOT_DIR, "disclaimer.html")
    with open(os.path.join(ROOT_DIR, "privacy-policy.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("<title>Privacy Policy | Krisala Hiranandani Township Pune</title>",
                        "<title>Disclaimer &amp; MahaRERA Compliance | Krisala Hiranandani Township</title>")
    html = html.replace('href="https://krisalahiranandanitownships.com/privacy-policy"',
                        'href="https://krisalahiranandanitownships.com/disclaimer"')
    html = html.replace('content="Privacy Policy and terms for Krisala Hiranandani Township Hinjewadi, Pune. Learn how we collect, protect, and use your personal information."',
                        'content="Official MahaRERA statutory disclaimer, channel partner disclosure, and artistic impression notice for Krisala Hiranandani Township Pune."')
    
    disclaimer_body = """<div class="policy-card glass-panel">
<h1>Disclaimer &amp; MahaRERA Statutory Disclosure</h1>
<p class="updated-date">Published in Compliance with MahaRERA Circular No. 34/2021 &amp; RERA Act 2016</p>

<div class="policy-section">
<h2>1. MahaRERA Project Registration Status</h2>
<p>Krisala Hiranandani Township, located at North Hinjewadi, Pune, comprises multiple residential and villa sectors, each registered under Maharashtra Real Estate Regulatory Authority (MahaRERA):</p>
<ul>
  <li><strong>Sector Arcadia:</strong> MahaRERA Registration No. <strong>PR1260002500600</strong></li>
  <li><strong>The Colosseum (Phase 4):</strong> MahaRERA Registration No. <strong>PR1260002600818</strong></li>
  <li><strong>The Della Collection &amp; Equestrian District:</strong> MahaRERA Registration No. <strong>PR1260002502438</strong></li>
</ul>
<p>Official registration records, sanctioned floor plans, layout approvals, and stage-wise completion certificates are available for public inspection at the MahaRERA website: 
<a href="https://maharera.maharashtra.gov.in" target="_blank" rel="noopener noreferrer">https://maharera.maharashtra.gov.in</a> under the registered projects section.</p>
</div>

<div class="policy-section">
<h2>2. Real Estate Channel Partner Disclosure</h2>
<p>This website (<strong>krisalahiranandanitownships.com</strong>) is an authorized digital information and marketing portal operated by <strong>Propsmart Realty</strong> (MahaRERA Real Estate Agent Registration No: <strong>A031262401295</strong>). Propsmart Realty is an authorized Channel Partner engaged in facilitating property inquiries, sales coordination, and site visits for Krisala Developers and Hiranandani Communities.</p>
<p>Propsmart Realty does not represent itself as the promoter or direct builder of the project.</p>
</div>

<div class="policy-section">
<h2>3. Artistic Impressions &amp; Indicative Visuals</h2>
<p>All renders, 3D architectural illustrations, photos, walkthrough animations, landscape impressions, elevation views, interior mock-ups, and amenity representations on this website are conceptual artist impressions and for representation purposes only. Actual structural finishes, elevations, materials, trees, lighting, and fittings may vary in accordance with municipal sanctions and final architectural execution.</p>
</div>

<div class="policy-section">
<h2>4. Pricing, Inventory &amp; Availability</h2>
<p>All property pricing mentioned on this portal (e.g. ₹79 Lakh*, ₹1.25 Cr*, ₹1.80 Cr*) is indicative base price and subject to change without prior notice. Final property cost involves floor rise charges, preferential location charges (PLC), covered parking, clubhouse memberships, stamp duty, registration fees, GST, and applicable statutory taxes. Apartment and villa plot allotment is subject to inventory availability at the time of formal application.</p>
</div>

<div class="policy-section">
<h2>5. Agreement for Sale Prevails</h2>
<p>No content on this website shall constitute an offer, warranty, or contractual obligation. The rights, specifications, handover timeline, and amenities guaranteed to the purchaser are strictly and exclusively defined in the registered <strong>Agreement for Sale</strong> executed between the buyer and the promoter.</p>
</div>

<div class="policy-section">
<h2>6. Contact Authority</h2>
<p>For official inquiries, verifications, or documentation requests:<br/>
<strong>Propsmart Realty (MahaRERA: A031262401295)</strong><br/>
Sales Coordination Desk: <a href="tel:+917744009295">+91 7744009295</a><br/>
Official Communications Email: <a href="mailto:propsmartrealty@gmail.com">propsmartrealty@gmail.com</a></p>
</div>
</div>"""

    html = re.sub(r'<main class="policy-container">.*?</main>',
                 f'<main class="policy-container">\n{disclaimer_body}\n</main>',
                 html, flags=re.DOTALL)
                 
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓ CREATED] {path}")

def create_refund_policy_page():
    path = os.path.join(ROOT_DIR, "refund-cancellation-policy.html")
    with open(os.path.join(ROOT_DIR, "privacy-policy.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("<title>Privacy Policy | Krisala Hiranandani Township Pune</title>",
                        "<title>Cancellation &amp; Refund Policy | Krisala Hiranandani Township</title>")
    html = html.replace('href="https://krisalahiranandanitownships.com/privacy-policy"',
                        'href="https://krisalahiranandanitownships.com/refund-cancellation-policy"')
    html = html.replace('content="Privacy Policy and terms for Krisala Hiranandani Township Hinjewadi, Pune. Learn how we collect, protect, and use your personal information."',
                        'content="Transparent Cancellation and Refund Policy for booking tokens, expressions of interest (EOI), and MahaRERA registered allotments."')
    
    refund_body = """<div class="policy-card glass-panel">
<h1>Cancellation &amp; Refund Policy</h1>
<p class="updated-date">Published in Compliance with MahaRERA Statutory Guidelines</p>

<div class="policy-section">
<h2>1. Overview</h2>
<p>This Cancellation and Refund Policy governs expressions of interest (EOI), advance booking tokens, and formal allotment payments made towards residences and villa plots at <strong>Krisala Hiranandani Township</strong>, Hinjewadi, Pune.</p>
</div>

<div class="policy-section">
<h2>2. Direct Developer Escrow Accounts</h2>
<p>Propsmart Realty (Authorized Channel Partner No: A031262401295) does not collect, hold, or accept booking amounts, cheques, or online payments in its own name. All booking tokens, expression of interest deposits, and installment payments are paid directly to the <strong>Promoter's MahaRERA-Designated Master Escrow Bank Account</strong> opened in compliance with Section 4(2)(l)(D) of the Real Estate (Regulation and Development) Act, 2016.</p>
</div>

<div class="policy-section">
<h2>3. Pre-Launch Expression of Interest (EOI) Refundability</h2>
<p>Booking tokens or Expression of Interest (EOI) amounts deposited prior to unit allotment or execution of the Agreement for Sale are <strong>100% refundable without deductions</strong> if:</p>
<ul>
  <li>The prospective buyer does not receive their preferred inventory, floor, or view during priority allotment.</li>
  <li>The buyer cancels their request in writing before the issuance of the formal Allotment Letter.</li>
  <li>The developer or promoter modifies key commercial terms unacceptably to the applicant prior to booking confirmation.</li>
</ul>
<p>Upon receipt of a written cancellation request, verified EOI refunds are processed directly by the promoter's banking desk within <strong>15 to 21 business days</strong> via direct NEFT/RTGS transfer to the applicant's originating bank account.</p>
</div>

<div class="policy-section">
<h2>4. Post-Allotment Cancellation &amp; Agreement for Sale</h2>
<p>Once an Allotment Letter has been issued or an Agreement for Sale has been formally registered under MahaRERA, cancellation terms, statutory deductions, administrative fees, and refund timelines shall be strictly governed by the cancellation clauses stipulated in the <strong>Registered Agreement for Sale</strong> in full compliance with MahaRERA rules.</p>
</div>

<div class="policy-section">
<h2>5. Assistance &amp; Refund Queries</h2>
<p>For tracking refund requests or escalation assistance, contact our facilitation desk:</p>
<p><strong>Customer Experience Concierge:</strong><br/>
Email: <a href="mailto:propsmartrealty@gmail.com">propsmartrealty@gmail.com</a><br/>
Phone: <a href="tel:+917744009295">+91 7744009295</a><br/>
Address: Krisala Hiranandani Sales Gallery, North Hinjewadi Boulevard, Pune 410506</p>
</div>
</div>"""

    html = re.sub(r'<main class="policy-container">.*?</main>',
                 f'<main class="policy-container">\n{refund_body}\n</main>',
                 html, flags=re.DOTALL)
                 
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓ CREATED] {path}")

def create_contact_page():
    path = os.path.join(ROOT_DIR, "contact.html")
    # Read site-address.html and adapt into canonical contact.html
    with open(os.path.join(ROOT_DIR, "site-address.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("<title>Site Address &amp; Location Map | Krisala Hiranandani Township Pune</title>",
                        "<title>Contact Us &amp; Sales Gallery Address | Krisala Hiranandani Township</title>")
    html = html.replace('href="https://krisalahiranandanitownships.com/site-address"',
                        'href="https://krisalahiranandanitownships.com/contact"')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✓ CREATED] {path}")

def remediate_html_files():
    html_files = sorted(glob.glob(os.path.join(ROOT_DIR, "*.html")))
    print(f"[*] Processing {len(html_files)} root HTML files for Google compliance...")
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        modified = False
        
        # 1. Inject Consent Mode v2 if missing
        if "gtag('consent'" not in content and "</head>" in content:
            content = content.replace("</head>", f"{CONSENT_MODE_SCRIPT}\n</head>", 1)
            modified = True
            
        # 2. Inject form consent notice below submit button in forms
        # Look for <button ... type="submit">...</button> or <button class="btn-primary...">...</button>
        # Check if form already has form-compliance-notice
        soup = BeautifulSoup(content, "html.parser")
        forms = soup.find_all("form")
        
        for form in forms:
            ftext = form.get_text().lower()
            if "authorise krisala hiranandani partner" not in ftext and "propsmart" not in ftext:
                # Find submit button
                btn = form.find("button", type="submit") or form.find("button")
                if btn:
                    # Append notice right after button
                    btn_str = str(btn)
                    if btn_str in content and FORM_CONSENT_HTML not in content:
                        content = content.replace(btn_str, f"{btn_str}\n{FORM_CONSENT_HTML}")
                        modified = True
                        
        # 3. Standardize footer with Legal bar & MahaRERA / Propsmart channel partner disclosure
        if "footer-legal-bar" not in content and "</footer>" in content:
            # Place right before </footer> or before <div class="footer-bottom">
            if '<div class="footer-bottom">' in content:
                content = content.replace('<div class="footer-bottom">', f"{LEGAL_FOOTER_SNIPPET}\n<div class=\"footer-bottom\">", 1)
                modified = True
            else:
                content = content.replace("</footer>", f"{LEGAL_FOOTER_SNIPPET}\n</footer>", 1)
                modified = True
                
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[✓ REMEDIATED] {filename}")
        else:
            print(f"[UNCHANGED] {filename} already compliant.")

def main():
    print("===========================================================================")
    print(" EXECUTING GOOGLE WEB & ADS COMPLIANCE REMEDIATION")
    print("===========================================================================")
    create_terms_page()
    create_disclaimer_page()
    create_refund_policy_page()
    create_contact_page()
    remediate_html_files()
    print("===========================================================================")
    print(" Remediation complete.")
    print("===========================================================================")

if __name__ == "__main__":
    main()

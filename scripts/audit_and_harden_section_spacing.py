#!/usr/bin/env python3
"""
Master Section Spacing Audit & Hardening Suite
Resolves:
1. Missing .section and .section-dark CSS definitions causing 0-padding section collapses.
2. Massive --section-gap (140px) dead space on desktop and mobile.
3. Fixes boxed <section> max-width in della-racecourse.html by introducing full-width sections + responsive inner containers.
4. Wraps della-townships-authority-banner inside container padding in explore & blog pages.
5. Calibrates mobile padding on .glass-panel (reducing 40px horizontal margin/padding to 16px on small screens).
6. Harmonizes vertical spacing in della.html, racecourse.html, pricing.html, index.html.
"""

import os
import re
import glob

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def harden_style_css():
    style_dev = os.path.join(ROOT_DIR, "style.dev.css")
    if not os.path.exists(style_dev):
        return
    with open(style_dev, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Calibrate --section-gap from 140px to balanced 85px desktop, 60px tablet, 45px mobile
    css = re.sub(r'--section-gap:\s*140px;', '--section-gap: 85px;', css)
    css = re.sub(r'--section-gap:\s*80px;', '--section-gap: 60px;', css)
    css = re.sub(r'--section-gap:\s*60px;', '--section-gap: 45px;', css)

    # 2. Add master .section and .section-dark architecture if missing
    section_rules = """
/* ==============================================================================
   STANDARDIZED MASTER SECTION ARCHITECTURE & RESPONSIVE SPACING
   ============================================================================== */
.section {
    width: 100%;
    padding: var(--section-gap, 85px) 0;
    position: relative;
    overflow: hidden;
}

.section-dark {
    background-color: var(--bg-dark-deep, #050608);
    border-top: 1px solid rgba(197, 160, 89, 0.18);
    border-bottom: 1px solid rgba(197, 160, 89, 0.18);
}

.section-light {
    background-color: rgba(16, 18, 26, 0.45);
}

.section-alt {
    background: radial-gradient(circle at 50% 10%, rgba(197, 160, 89, 0.05) 0%, rgba(9, 10, 15, 0.98) 75%);
    border-top: 1px solid rgba(197, 160, 89, 0.2);
    border-bottom: 1px solid rgba(197, 160, 89, 0.2);
}

@media (max-width: 992px) {
    .section {
        padding: 65px 0;
    }
}

@media (max-width: 768px) {
    .section {
        padding: 48px 0;
    }
    .section-header {
        margin-bottom: 45px !important;
    }
    .glass-panel {
        padding: 24px 16px !important;
        margin-bottom: 24px !important;
    }
}
"""
    if "STANDARDIZED MASTER SECTION ARCHITECTURE" not in css:
        css = section_rules + "\n" + css

    with open(style_dev, "w", encoding="utf-8") as f:
        f.write(css)
    print("Hardened style.dev.css section spacing architecture")


def harden_della_racecourse_pages():
    for filename in ["della-racecourse.html", "della-racecourse-pune.html"]:
        filepath = os.path.join(ROOT_DIR, filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        # Update CSS styling for full-width sections and contained inner grids
        old_css_part = """.section-pad {
  padding: 100px 20px;
  max-width: 1360px;
  margin: 0 auto;
}"""
        new_css_part = """.della-rc-section {
  width: 100%;
  padding: 85px 0;
  position: relative;
  overflow: hidden;
}

.della-rc-section .container {
  max-width: 1360px;
  margin: 0 auto;
  padding: 0 24px;
}

@media (max-width: 992px) {
  .della-rc-section { padding: 65px 0; }
  .della-rc-section .container { padding: 0 20px; }
}

@media (max-width: 768px) {
  .della-rc-section { padding: 48px 0; }
  .della-rc-section .container { padding: 0 16px; }
  .sec-head { margin-bottom: 35px; }
  .della-rc-hero { padding: 100px 16px 50px; min-height: auto; }
  .gdv-badge-strip { gap: 10px; margin-bottom: 25px; }
  .gdv-chip { padding: 10px 16px; width: 100%; }
  .form-card { padding: 28px 18px; }
  nav { overflow-x: auto; max-width: 100%; -webkit-overflow-scrolling: touch; }
}"""
        if old_css_part in html:
            html = html.replace(old_css_part, new_css_part)

        # Replace section structure from <section class="section-pad"> to <section class="della-rc-section"><div class="container">
        # 1. Visionary section
        html = html.replace('<section class="section-pad" style="background: rgba(16, 18, 26, 0.4);">\n  <div class="sec-head">',
                            '<section class="della-rc-section" style="background: rgba(16, 18, 26, 0.45); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2);">\n  <div class="container">\n  <div class="sec-head">')
        html = html.replace('  </div>\n</section>\n\n<!-- Section 2:', '  </div>\n  </div>\n</section>\n\n<!-- Section 2:')

        # 2. 12 Pillars section
        html = html.replace('<section class="section-pad">\n  <div class="sec-head">',
                            '<section class="della-rc-section">\n  <div class="container">\n  <div class="sec-head">')
        html = html.replace('  </div>\n</section>\n\n<!-- Section 3:', '  </div>\n  </div>\n</section>\n\n<!-- Section 3:')

        # 3. Spec Table section
        html = html.replace('<section class="section-pad" style="background: rgba(16, 18, 26, 0.45);">\n  <div class="sec-head">',
                            '<section class="della-rc-section" style="background: rgba(16, 18, 26, 0.45); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2);">\n  <div class="container">\n  <div class="sec-head">')
        html = html.replace('  </div>\n</section>\n\n<!-- Section 4:', '  </div>\n  </div>\n</section>\n\n<!-- Section 4:')

        # 4. Form section
        html = html.replace('<section id="enquire" class="section-pad">\n  <div class="sec-head">',
                            '<section id="enquire" class="della-rc-section">\n  <div class="container">\n  <div class="sec-head">')
        html = html.replace('  </div>\n</section>\n\n<!-- Section 5:', '  </div>\n  </div>\n</section>\n\n<!-- Section 5:')

        # 5. FAQ section
        html = html.replace('<section class="section-pad" style="background: rgba(16, 18, 26, 0.4);">\n  <div class="sec-head">',
                            '<section class="della-rc-section" style="background: rgba(16, 18, 26, 0.45); border-top: 1px solid rgba(197, 160, 89, 0.2); border-bottom: 1px solid rgba(197, 160, 89, 0.2);">\n  <div class="container">\n  <div class="sec-head">')
        html = html.replace('  </div>\n</section>\n\n<!-- Footer -->', '  </div>\n  </div>\n</section>\n\n<!-- Footer -->')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Hardened layout & container spacing in {filename}")


def harden_della_html():
    filepath = os.path.join(ROOT_DIR, "della.html")
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject .section & .section-dark CSS into della.html's <style> block
    section_css = """
.section {
 width: 100%;
 padding: 85px 0;
 position: relative;
 overflow: hidden;
}
.section-dark {
 background-color: var(--bg-dark-deep, #050608);
 border-top: 1px solid rgba(197, 160, 89, 0.18);
 border-bottom: 1px solid rgba(197, 160, 89, 0.18);
}
@media (max-width: 992px) {
 .section { padding: 65px 0; }
}
@media (max-width: 768px) {
 .section { padding: 48px 0; }
 .section-header { margin-bottom: 40px !important; }
}
"""
    if ".section {" not in html:
        html = html.replace("</style>", section_css + "\n</style>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Hardened .section & .section-dark in della.html")


def harden_racecourse_html():
    filepath = os.path.join(ROOT_DIR, "racecourse.html")
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Calibrate .section-equestrian and .section-equestrian-alt for mobile
    equestrian_mobile_css = """
@media (max-width: 768px) {
 .section-equestrian, .section-equestrian-alt {
   padding: 48px 0 !important;
 }
 .experience-section {
   padding: 48px 0 !important;
 }
}
"""
    if "padding: 48px 0 !important;" not in html:
        html = html.replace("</style>", equestrian_mobile_css + "\n</style>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Hardened responsive section spacing in racecourse.html")


def harden_pricing_html():
    filepath = os.path.join(ROOT_DIR, "pricing.html")
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    section_css = """
<style>
.section {
 width: 100%;
 padding: 80px 0;
 position: relative;
 overflow: hidden;
}
.section-dark {
 background-color: #050608;
 border-top: 1px solid rgba(197, 160, 89, 0.18);
 border-bottom: 1px solid rgba(197, 160, 89, 0.18);
}
@media (max-width: 768px) {
 .section { padding: 48px 0; }
}
</style>
"""
    if ".section {" not in html:
        html = html.replace("</head>", section_css + "\n</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Hardened .section in pricing.html")


def harden_authority_banner_containment():
    # In explore/*.html and blog pages, wrap the della authority banner in a container if it's placed outside
    explore_files = glob.glob(os.path.join(ROOT_DIR, "explore", "*.html"))
    blog_files = glob.glob(os.path.join(ROOT_DIR, "blog", "*.html"))
    
    count = 0
    for hf in explore_files + blog_files:
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()

        if '<div class="della-townships-authority-banner"' in content:
            # Check if it is already wrapped in a container
            if '<div class="container">\n<div class="della-townships-authority-banner"' not in content and '<div class="container">\n  <div class="della-townships-authority-banner"' not in content:
                # Wrap it with container
                content = content.replace(
                    '<div class="della-townships-authority-banner"',
                    '<div class="container" style="max-width: 1360px; margin: 0 auto; padding: 0 20px;">\n<div class="della-townships-authority-banner"'
                )
                content = content.replace(
                    'WhatsApp Inquiry</a>\n  </div>\n</div>',
                    'WhatsApp Inquiry</a>\n  </div>\n</div>\n</div>'
                )
                with open(hf, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1

    print(f"Contained Della authority banner inside container grids across {count} pages")


if __name__ == "__main__":
    harden_style_css()
    harden_della_racecourse_pages()
    harden_della_html()
    harden_racecourse_html()
    harden_pricing_html()
    harden_authority_banner_containment()

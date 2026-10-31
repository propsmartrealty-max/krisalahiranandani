#!/usr/bin/env python3
"""
Incorporate Official Della Racecourse Pune (40-Acre District) Exclusive Showcase
Referenced & Imported from https://www.dellatownships.com/pune/della-racecourse
"""

import os
import re
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DELLA_HTML = os.path.join(ROOT_DIR, "della.html")
SILO_DELLA_1 = os.path.join(ROOT_DIR, "krisala-hiranandani-pune", "della.html")
SILO_DELLA_2 = os.path.join(ROOT_DIR, "krisala-hiranandani-township-pune", "della.html")

EXCLUSIVE_SECTION_CSS = """
/* ==============================================================================
   EXCLUSIVE SHOWCASE: DELLA RACECOURSE PUNE (40 ACRES)
   Imported & referenced from https://www.dellatownships.com/pune/della-racecourse
   ============================================================================== */
.della-racecourse-exclusive-showcase {
  padding: 90px 0;
  background: radial-gradient(circle at 50% 10%, rgba(197, 160, 89, 0.08) 0%, rgba(9, 10, 15, 0.98) 70%);
  border-top: 1px solid rgba(197, 160, 89, 0.35);
  border-bottom: 1px solid rgba(197, 160, 89, 0.35);
  position: relative;
  overflow: hidden;
}
.della-rc-header {
  text-align: center;
  max-width: 960px;
  margin: 0 auto 55px;
}
.della-rc-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(197, 160, 89, 0.12);
  border: 1px solid rgba(197, 160, 89, 0.4);
  color: var(--gold-bright);
  font-size: 0.85rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 8px 20px;
  border-radius: 50px;
  margin-bottom: 18px;
  font-weight: 600;
}
.della-rc-title {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 4.2vw, 3.6rem);
  color: var(--gold-light);
  line-height: 1.15;
  margin-bottom: 18px;
}
.della-rc-subtitle {
  color: var(--text-muted);
  font-size: clamp(1rem, 1.8vw, 1.2rem);
  line-height: 1.7;
}

/* Featured Hero Banner */
.della-rc-hero-card {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(197, 160, 89, 0.35);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
  margin-bottom: 60px;
}
.della-rc-hero-card img {
  width: 100%;
  height: clamp(340px, 50vw, 560px);
  object-fit: cover;
  display: block;
}
.della-rc-hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(9, 10, 15, 0.2) 0%, rgba(9, 10, 15, 0.85) 90%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: clamp(24px, 4vw, 48px);
}
.della-rc-hero-stats {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
  margin-top: 15px;
}
.della-rc-hero-stat-item {
  border-left: 2px solid var(--gold-bright);
  padding-left: 14px;
}
.della-rc-hero-stat-val {
  color: var(--gold-bright);
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 700;
  line-height: 1;
}
.della-rc-hero-stat-lbl {
  color: #fff;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 4px;
}

/* Feature Grid & Cards */
.della-rc-module {
  margin-bottom: 60px;
}
.della-rc-module-title {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 3vw, 2.4rem);
  color: var(--gold-bright);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.della-rc-module-desc {
  color: var(--text-muted);
  font-size: 1.02rem;
  line-height: 1.8;
  max-width: 900px;
  margin-bottom: 30px;
}
.della-rc-grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
}
.della-rc-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
}
.della-rc-grid-4 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
}
.della-rc-card {
  background: rgba(16, 18, 26, 0.7);
  border: 1px solid rgba(197, 160, 89, 0.22);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
  flex-direction: column;
}
.della-rc-card:hover {
  border-color: var(--gold-bright);
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(197, 160, 89, 0.15);
}
.della-rc-card-img {
  position: relative;
  overflow: hidden;
  aspect-ratio: 16/10;
  background: #050608;
}
.della-rc-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}
.della-rc-card:hover .della-rc-card-img img {
  transform: scale(1.05);
}
.della-rc-card-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(9, 10, 15, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(197, 160, 89, 0.4);
  color: var(--gold-bright);
  font-size: 0.72rem;
  letter-spacing: 1px;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 4px;
  font-weight: 600;
}
.della-rc-card-body {
  padding: 24px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.della-rc-card-title {
  font-family: var(--font-heading);
  font-size: 1.4rem;
  color: var(--gold-light);
  margin-bottom: 10px;
  line-height: 1.25;
}
.della-rc-card-text {
  color: var(--text-muted);
  font-size: 0.92rem;
  line-height: 1.65;
  margin-bottom: 16px;
  flex-grow: 1;
}
.della-rc-card-specs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 14px;
}
.della-rc-pill {
  font-size: 0.75rem;
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(197, 160, 89, 0.2);
  padding: 3px 8px;
  border-radius: 4px;
}

/* Strategic Partnership Showcase */
.della-rc-partnership-box {
  background: linear-gradient(135deg, rgba(197, 160, 89, 0.12) 0%, rgba(10, 12, 16, 0.95) 100%);
  border: 1px solid rgba(197, 160, 89, 0.4);
  border-radius: 16px;
  padding: clamp(28px, 4vw, 48px);
  margin-bottom: 60px;
}
.della-rc-titans-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
  margin-top: 30px;
}
.della-rc-titan-card {
  background: rgba(9, 10, 15, 0.6);
  border: 1px solid rgba(197, 160, 89, 0.25);
  border-radius: 10px;
  padding: 22px;
  text-align: center;
}
.della-rc-titan-name {
  color: var(--gold-bright);
  font-family: var(--font-heading);
  font-size: 1.35rem;
  margin-bottom: 4px;
}
.della-rc-titan-role {
  color: var(--text-muted);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Salutogenic 4-Pillars */
.della-rc-salutogenic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 25px;
}
.della-rc-saluto-item {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(197, 160, 89, 0.2);
  border-radius: 8px;
  padding: 20px;
}
.della-rc-saluto-title {
  color: var(--gold-bright);
  font-weight: 600;
  font-size: 1.05rem;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.della-rc-saluto-desc {
  color: var(--text-muted);
  font-size: 0.86rem;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .della-racecourse-exclusive-showcase { padding: 60px 0; }
  .della-rc-hero-stats { gap: 16px; }
  .della-rc-grid-2, .della-rc-grid-3, .della-rc-grid-4 { grid-template-columns: 1fr; }
}
"""

EXCLUSIVE_SECTION_HTML = """
<!-- ============================================================================== -->
<!-- EXCLUSIVE SHOWCASE: DELLA RACECOURSE PUNE • 40 ACRES                           -->
<!-- Referenced & Imported from https://www.dellatownships.com/pune/della-racecourse -->
<!-- ============================================================================== -->
<section class="section section-dark della-racecourse-exclusive-showcase" id="della-racecourse-exclusive">
  <div class="container">
    
    <!-- Header -->
    <div class="della-rc-header scroll-reveal">
      <div class="della-rc-badge">
        <i class="ph ph-crown"></i> Exclusive Destination Showcase
      </div>
      <h2 class="della-rc-title">Della Racecourse Pune • 40 Acres</h2>
      <p class="della-rc-subtitle">
        International Polo Club, 5-Star Resort &amp; Private Residences • Darumbre, North Hinjewadi, Pune.<br/>
        India’s first-ever residential racecourse and international polo club within a luxury integrated salutogenic township.
      </p>
    </div>

    <!-- Featured Master Hero Banner -->
    <div class="della-rc-hero-card scroll-reveal">
      <img src="/public/della_racecourse/della_pune_racecourse_hero_banner.webp" 
           alt="Della Racecourse Pune 40 Acres International Polo Club and Resort Darumbre Hinjewadi" 
           width="1440" height="600" loading="lazy" decoding="async"/>
      <div class="della-rc-hero-overlay">
        <span class="della-rc-badge" style="align-self: flex-start; margin-bottom: 8px;">
          <i class="ph ph-horse"></i> The 8-Acre Derby Arena
        </span>
        <h3 style="font-family: var(--font-heading); font-size: clamp(1.8rem, 3.5vw, 2.8rem); color: #fff; margin-bottom: 6px;">
          India's 1st Residential Equestrian Haven
        </h3>
        <p style="color: var(--text-light); max-width: 800px; font-size: 0.98rem; line-height: 1.6;">
          An 8-acre professionally graded private turf track, steeplechase schooling rings, international polo field, and luxury air-conditioned stables in North Hinjewadi (Darumbre).
        </p>
        <div class="della-rc-hero-stats">
          <div class="della-rc-hero-stat-item">
            <div class="della-rc-hero-stat-val">40 Acres</div>
            <div class="della-rc-hero-stat-lbl">Della Enclave</div>
          </div>
          <div class="della-rc-hero-stat-item">
            <div class="della-rc-hero-stat-val">8 Acres</div>
            <div class="della-rc-hero-stat-lbl">Turf Racecourse</div>
          </div>
          <div class="della-rc-hero-stat-item">
            <div class="della-rc-hero-stat-val">300+ Keys</div>
            <div class="della-rc-hero-stat-lbl">5-Star Resort</div>
          </div>
          <div class="della-rc-hero-stat-item">
            <div class="della-rc-hero-stat-val">1,00,000 Sq.Ft.</div>
            <div class="della-rc-hero-stat-lbl">Luxury Retail</div>
          </div>
          <div class="della-rc-hero-stat-item">
            <div class="della-rc-hero-stat-val">MAYRLIFE</div>
            <div class="della-rc-hero-stat-lbl">Medical Wellness</div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 1: The Visionary Strategic Partnership -->
    <div class="della-rc-partnership-box scroll-reveal">
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
        <span class="della-rc-badge"><i class="ph ph-handshake"></i> Strategic Tripartite Alliance</span>
      </div>
      <h3 style="font-family: var(--font-heading); font-size: clamp(1.8rem, 2.8vw, 2.3rem); color: var(--gold-light); margin-bottom: 16px;">
        The Visionary Collaboration: Mistry × Hiranandani × Krisala
      </h3>
      <p style="color: var(--text-light); line-height: 1.85; font-size: 1.05rem;">
        <strong>Della Townships</strong>, <strong>Hiranandani Communities</strong>, and <strong>Krisala Developers</strong> have entered a landmark strategic partnership to develop the 40-acre <strong>Della Racecourse Pune</strong> district at Darumbre, North Hinjewadi. Conceived by Design Futurist <strong>Jimmy Mistry</strong>, township patriarch <strong>Dr. Niranjan Hiranandani</strong>, and real estate developer <strong>Sagar Agarwal</strong>, this partnership unites neoclassical architectural grandeur with 5-star international resort hospitality, equestrian sport, and salutogenic longevity living.
      </p>

      <div class="della-rc-titans-grid">
        <div class="della-rc-titan-card">
          <div class="della-rc-titan-name">Jimmy Mistry</div>
          <div class="della-rc-titan-role">Design Futurist &amp; Creator of Future-Fit Cities<br/>CMD, Della Townships India</div>
        </div>
        <div class="della-rc-titan-card">
          <div class="della-rc-titan-name">Dr. Niranjan Hiranandani</div>
          <div class="della-rc-titan-role">Chairman - NAREDCO<br/>CMD, Hiranandani Group</div>
        </div>
        <div class="della-rc-titan-card">
          <div class="della-rc-titan-name">Sagar Agarwal</div>
          <div class="della-rc-titan-role">Managing Director<br/>Krisala Developers</div>
        </div>
      </div>

      <!-- Bhumi Poojan Milestone -->
      <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; align-items: center; border-top: 1px solid rgba(197,160,89,0.25); padding-top: 24px;">
        <div style="border-radius: 10px; overflow: hidden; border: 1px solid rgba(197, 160, 89, 0.3);">
          <img src="/public/della_racecourse/della_pune_bhumi_poojan_site.webp" 
               alt="Della Racecourse Pune Bhumi Poojan Ceremony at Darumbre North Hinjewadi" 
               width="600" height="380" loading="lazy" decoding="async" style="width: 100%; height: auto; display: block;"/>
        </div>
        <div>
          <h4 style="font-family: var(--font-heading); color: var(--gold-bright); font-size: 1.35rem; margin-bottom: 10px;">
            Groundbreaking Ceremony • Darumbre Site
          </h4>
          <p style="color: var(--text-muted); font-size: 0.94rem; line-height: 1.7; margin-bottom: 14px;">
            The official Bhumi Poojan and foundation stone laying ceremony for the 40-acre Della Racecourse was consecrated on-site in Darumbre, North Hinjewadi, initiating fast-track grading of the 8-acre turf racecourse and foundation milestones for the international polo grounds.
          </p>
          <span class="della-rc-pill" style="border-color: var(--gold-bright); color: var(--gold-bright);">
            <i class="ph ph-check-circle"></i> On-Site Civil Infrastructure Underway
          </span>
        </div>
      </div>
    </div>

    <!-- MODULE 2: Racecourse, Polo Club & Luxury Stables -->
    <div class="della-rc-module scroll-reveal">
      <div class="della-rc-module-title">
        <i class="ph ph-horse"></i> 1. The 8-Acre Racecourse &amp; International Polo Club
      </div>
      <p class="della-rc-module-desc">
        At the heart of the township lies a private 8-acre turf racecourse—a rare privilege reserved for residents. Home to the International Polo Club, professional training chukkers, derby showcases, and air-conditioned equestrian stables.
      </p>

      <div class="della-rc-grid-3">
        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_polo_club_main.webp" 
                 alt="International Polo Club Main Pavilion Della Racecourse Pune" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Polo Club</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">International Polo Pavilion</h4>
            <p class="della-rc-card-text">
              Championship polo pavilion with VIP members' grandstand, hospitality lounges, and viewing terraces overlooking the central turf arena.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Championship Field</span>
              <span class="della-rc-pill">VIP Grandstand</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_racecourse_track_action.webp" 
                 alt="Turf Track Action and Steeplechase Oval Della Racecourse" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Derby Oval</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">8-Acre Turf Derby Oval</h4>
            <p class="della-rc-card-text">
              Professionally engineered Bermuda grass track with banked curves, steeplechase schooling rings, and automated irrigation for thoroughbred training.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Bermuda Turf</span>
              <span class="della-rc-pill">Steeplechase Rings</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_equine_stables.webp" 
                 alt="World-Class Equine Boarding Stables Della Townships Pune" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Equine Boarding</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Air-Conditioned Stables</h4>
            <p class="della-rc-card-text">
              Veterinary-assisted luxury stables, private horse paddocks, equine spa, hydrotherapy equine pools, and professional groom quarters.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">AC Horse Suites</span>
              <span class="della-rc-pill">On-Call Vet Care</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 3: 40-Acre Masterplan, Monumental Gate & Experience Center -->
    <div class="della-rc-module scroll-reveal">
      <div class="della-rc-module-title">
        <i class="ph ph-map-pin"></i> 2. 40-Acre Masterplan, Gateway &amp; Experience Center
      </div>
      <p class="della-rc-module-desc">
        A self-contained equestrian sanctuary entered via a monumental triumphal gate, featuring the state-of-the-art Della Experience Center for VIP buyers.
      </p>

      <div class="della-rc-grid-3">
        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_masterplan_40acres.webp" 
                 alt="Della Racecourse Pune 40-Acre Masterplan Blueprint" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Masterplan</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">40-Acre Master Ecosystem</h4>
            <p class="della-rc-card-text">
              Zoned master planning incorporating the racecourse at the core, bordered by 100 private villa plots, branded high-rise towers, 5-star resort, and retail promenade.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">40 Sanctioned Acres</span>
              <span class="della-rc-pill">12m Paved Avenues</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_entrance_grand_gate.webp" 
                 alt="Della Racecourse Pune Grand Monumental Entrance Gate" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Monumental Entry</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Triumphal Arch Entrance</h4>
            <p class="della-rc-card-text">
              Classical Roman triumphal entrance portal with biometric security, license-plate recognition cameras, water cascades, and private palm-lined carriage drives.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">24/7 Biometric Access</span>
              <span class="della-rc-pill">Grand Boulevard</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_experience_center.webp" 
                 alt="Della Townships Pune Experience Center and Sales Lounge" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Sales Experience</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Della Experience Center</h4>
            <p class="della-rc-card-text">
              A bespoke luxury preview pavilion featuring full architectural mockups, VR immersion walk-throughs, material libraries, and relationship concierge.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">VR 3D Walkthroughs</span>
              <span class="della-rc-pill">VIP Private Lounge</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 4: Private Luxury Villas (4 British Colonial Styles) -->
    <div class="della-rc-module scroll-reveal">
      <div class="della-rc-module-title">
        <i class="ph ph-buildings"></i> 3. Private Luxury Villas in British Colonial Architecture
      </div>
      <p class="della-rc-module-desc">
        Drawing inspiration from the stately charm of British Colonial architecture, the township blends timeless grandeur with tropical verandas across 4 curated architectural styles on G+2 sanctioned freehold plots (1,800 to 5,000+ sq.ft.).
      </p>

      <div class="della-rc-grid-4">
        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_british_colonial_villa_style2.webp" 
                 alt="British Colonial Architecture Style 1 Imperial Georgian Manor Della Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Style 1 • Georgian</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">The Georgian Manor</h4>
            <p class="della-rc-card-text">
              Symmetrical facades, classical porticos with Doric columns, double-hung sash windows, and grand carriage porch.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Symmetrical Facade</span>
              <span class="della-rc-pill">Doric Portico</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_british_colonial_villa_style3.webp" 
                 alt="British Colonial Architecture Style 2 Anglo-Palladian Villa Della Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Style 2 • Palladian</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Anglo-Palladian Villa</h4>
            <p class="della-rc-card-text">
              Grand triangular pediments, wrap-around tropical verandas, tall French doors, and deep shaded eaves.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Wrap Veranda</span>
              <span class="della-rc-pill">French Casements</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_british_colonial_villa_style4.webp" 
                 alt="British Colonial Architecture Style 3 Regency Equestrian Estate Della Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Style 3 • Regency</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Regency Equestrian</h4>
            <p class="della-rc-card-text">
              Soaring 14-foot ceilings, wrought-iron balustrades, private plunge pool terraces overlooking the racecourse.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">14ft Ceilings</span>
              <span class="della-rc-pill">Plunge Pool Deck</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_private_villas_plots.webp" 
                 alt="British Colonial Style 4 Colonial Plantation Residence Della Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Style 4 • Plantation</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Plantation Residence</h4>
            <p class="della-rc-card-text">
              Deep louvered wooden shutters, central courtyard water bodies, and sprawling private rear gardens.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Courtyard Oasis</span>
              <span class="della-rc-pill">Private Lawn</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 5: Branded Residences, 5-Star Resort, Dining & Retail -->
    <div class="della-rc-module scroll-reveal">
      <div class="della-rc-module-title">
        <i class="ph ph-sparkle"></i> 4. Branded Sky Villas, 5-Star Resort &amp; Gastronomy
      </div>
      <p class="della-rc-module-desc">
        A seamless blend of branded high-rise residences, 300+ keys luxury resort rooms, glamping retreats, and celebrity chef dining venues.
      </p>

      <div class="della-rc-grid-3">
        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_branded_residences_skyvillas.webp" 
                 alt="Della Branded Residences and Sky Villas Della Racecourse Pune" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Sky Duplexes</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Della Branded Sky Villas</h4>
            <p class="della-rc-card-text">
              Biophilic residential towers featuring double-height presidential sky duplexes with Italian marble, acoustic glazing, and private elevator vestibules.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Double-Height Ceilings</span>
              <span class="della-rc-pill">Private Elevators</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_glamping_bedroom.webp" 
                 alt="Della Luxury Glamping Resort Bedroom View Pune" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">300+ Key Resort</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">5-Star Glamping &amp; Suites</h4>
            <p class="della-rc-card-text">
              300+ luxury resort rooms and experiential glamping tents with private outdoor Jacuzzis, 24/7 concierge, in-villa dining, and valet service.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Private Jacuzzi</span>
              <span class="della-rc-pill">24/7 Concierge</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_celebrity_chef_dining.webp" 
                 alt="Celebrity Chef Fine Dining Restaurants Della Racecourse Pune" 
                 width="400" height="250" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Gastronomy</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Destination Dining &amp; Bars</h4>
            <p class="della-rc-card-text">
              Signature culinary venues led by celebrity chefs, 24x7 gourmet coffee shop, sports bar, cigar lounge, and open-air polo turf terrace dining.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Celebrity Chefs</span>
              <span class="della-rc-pill">Polo Turf Lounge</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 6: Weddings, Design District, Adventure & Longevity -->
    <div class="della-rc-module scroll-reveal">
      <div class="della-rc-module-title">
        <i class="ph ph-heart"></i> 5. Weddings, Design District, Adventure Park &amp; Longevity
      </div>
      <p class="della-rc-module-desc">
        Everything needed for celebration, extreme sport, retail indulgence, and holistic European medical wellness.
      </p>

      <div class="della-rc-grid-4">
        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_destination_wedding_venue.webp" 
                 alt="Della Destination Weddings and MICE Venues Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Weddings &amp; MICE</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Destination Weddings</h4>
            <p class="della-rc-card-text">
              Polo-facing royal lawns, grand banquet ballrooms, amphitheatre, and 12 executive MICE boardrooms.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Grand Ballrooms</span>
              <span class="della-rc-pill">12 MICE Venues</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_design_district_retail.webp" 
                 alt="Della Design District 100,000 Sq.Ft. Luxury Retail Promenade" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">1,00,000 Sq.Ft. Retail</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Della Design District</h4>
            <p class="della-rc-card-text">
              1,00,000 sq.ft. luxury retail boulevard: Luxury Interiors &amp; Design, Bridal Maison, Fine Jewellery, and Couture.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Luxury Fashion</span>
              <span class="della-rc-pill">Jewellery Maison</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_extreme_adventure_park.webp" 
                 alt="Della Extreme Adventure Park Within Residential Township Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Extreme Adventure</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Extreme Adventure Park</h4>
            <p class="della-rc-card-text">
              India's 1st extreme adventure park inside a residential township: flying fox, swoop swing, sky cycling, and motocross.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">Sky Cycling</span>
              <span class="della-rc-pill">Motocross Dirt</span>
            </div>
          </div>
        </div>

        <div class="della-rc-card">
          <div class="della-rc-card-img">
            <img src="/public/della_racecourse/della_pune_senior_living_longevity.webp" 
                 alt="Senior Living and Longevity Community Della Racecourse Pune" 
                 width="300" height="200" loading="lazy" decoding="async"/>
            <span class="della-rc-card-tag">Longevity Living</span>
          </div>
          <div class="della-rc-card-body">
            <h4 class="della-rc-card-title">Longevity &amp; Senior Living</h4>
            <p class="della-rc-card-text">
              Active vibrant senior community, 24/7 on-call geriatric healthcare, assisted living suites, and reflexology trails.
            </p>
            <div class="della-rc-card-specs">
              <span class="della-rc-pill">24/7 Health Desk</span>
              <span class="della-rc-pill">Assisted Living</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULE 7: European Medical Wellness (MAYRLIFE Collaboration) & Salutogenic 4-Pillars -->
    <div class="della-rc-module scroll-reveal" style="background: rgba(16, 18, 26, 0.6); border: 1px solid rgba(197, 160, 89, 0.3); border-radius: 16px; padding: clamp(24px, 4vw, 44px); margin-bottom: 30px;">
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">
        <div>
          <span class="della-rc-badge"><i class="ph ph-heartbeat"></i> MAYRLIFE Collaboration</span>
          <h3 style="font-family: var(--font-heading); font-size: clamp(1.8rem, 3vw, 2.3rem); color: var(--gold-bright); margin-top: 8px;">
            European Medical Wellness, Longevity Science &amp; Salutogenic Living
          </h3>
        </div>
        <button class="btn-primary open-modal" data-magnet="wellness_docket">Request Longevity Docket</button>
      </div>

      <p style="color: var(--text-light); line-height: 1.85; font-size: 1.02rem; margin-bottom: 25px;">
        In strategic collaboration with <strong>MAYRLIFE</strong>—the world's foremost pioneer in Mayr-based medical longevity—every resident gains access to advanced preventative health diagnostics: <strong>Whole-Body Cryotherapy (-110°C)</strong>, <strong>PEMF (Pulsed Electromagnetic Field Therapy)</strong>, <strong>Hyperbaric Oxygen Chambers (HBOT)</strong>, <strong>IV Micronutrient Drips</strong>, and <strong>Gut Microbiome Optimization</strong>.
      </p>

      <h4 style="color: var(--gold-light); font-size: 1.15rem; margin-bottom: 12px; font-weight: 600;">
        The 4 Operating System Pillars of Salutogenic Living:
      </h4>
      <div class="della-rc-salutogenic-grid">
        <div class="della-rc-saluto-item">
          <div class="della-rc-saluto-title"><i class="ph ph-plant"></i> Biophilic Design</div>
          <div class="della-rc-saluto-desc">Living tactile materials, indoor vertical gardens, and natural Sahyadri stone lowering cortisol and elevating cognitive focus.</div>
        </div>
        <div class="della-rc-saluto-item">
          <div class="della-rc-saluto-title"><i class="ph ph-sun"></i> Natural Light</div>
          <div class="della-rc-saluto-desc">Architectural circadian daylight planning with passive solar orientation and automated shading tuning melatonin and deep REM sleep cycles.</div>
        </div>
        <div class="della-rc-saluto-item">
          <div class="della-rc-saluto-title"><i class="ph ph-drop"></i> Water Perfection</div>
          <div class="della-rc-saluto-desc">Structured micro-clustered drinking water and mineral-optimized pH across plunge pools, lap baths, and hydrotherapy suites.</div>
        </div>
        <div class="della-rc-saluto-item">
          <div class="della-rc-saluto-title"><i class="ph ph-wind"></i> Air Purity</div>
          <div class="della-rc-saluto-desc">High-efficiency MERV-15 mechanical filtration, negative-ion charging, and low-VOC construction materials ensuring clinical indoor air purity.</div>
        </div>
      </div>
    </div>

    <!-- Exclusive Section Call to Action -->
    <div style="text-align: center; margin-top: 50px;">
      <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px;">
        Experience India's first equestrian township destination by personal invitation only.
      </p>
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <button class="btn-primary open-modal" data-magnet="della_racecourse_vip">
          <i class="ph ph-calendar-check"></i> Book Della Racecourse VIP Tour
        </button>
        <button class="btn-secondary open-modal" data-magnet="della_racecourse_docket">
          <i class="ph ph-download-simple"></i> Download 40-Page Della Brochure
        </button>
      </div>
    </div>

  </div>
</section>
"""

def update_della_page(file_path):
    if not os.path.exists(file_path):
        print(f"[SKIP] File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject CSS if not already present
    if ".della-racecourse-exclusive-showcase" not in content:
        content = content.replace("</style>", EXCLUSIVE_SECTION_CSS + "\n</style>", 1)
        print(f"[✓ CSS INJECTED] {file_path}")

    # 2. Replace or inject EXCLUSIVE_SECTION_HTML
    # If #racecourse section exists, replace it with #della-racecourse-exclusive
    racecourse_pattern = r"<!-- Racecourse Highlight -->\s*<section class=\"racecourse-highlight\" id=\"racecourse\">.*?</section>"
    if re.search(racecourse_pattern, content, re.DOTALL):
        content = re.sub(racecourse_pattern, EXCLUSIVE_SECTION_HTML, content, flags=re.DOTALL)
        print(f"[✓ EXCLUSIVE SECTION REPLACED #racecourse] {file_path}")
    elif '<section class="section section-dark della-racecourse-exclusive-showcase"' in content:
        # Update existing
        exclusive_pattern = r"<!-- ============================================================================== -->\s*<!-- EXCLUSIVE SHOWCASE: DELLA RACECOURSE PUNE.*?<!-- End of Exclusive Showcase / CTA -->|</section>\s*(?=<!-- Villa Plot Options -->)"
        # Simple string replacement if present
        start_marker = '<!-- ============================================================================== -->'
        end_marker = '<!-- Villa Plot Options -->'
        if start_marker in content and end_marker in content:
            idx1 = content.find(start_marker)
            idx2 = content.find(end_marker)
            content = content[:idx1] + EXCLUSIVE_SECTION_HTML + "\n" + content[idx2:]
            print(f"[✓ EXCLUSIVE SECTION UPDATED] {file_path}")
    else:
        # Insert before <!-- Villa Plot Options -->
        target = "<!-- Villa Plot Options -->"
        if target in content:
            content = content.replace(target, EXCLUSIVE_SECTION_HTML + "\n" + target, 1)
            print(f"[✓ EXCLUSIVE SECTION INSERTED BEFORE #villa-plots] {file_path}")

    # 3. Add link in sub-navigation if not present
    if "#della-racecourse-exclusive" not in content:
        content = content.replace('href="#racecourse"', 'href="#della-racecourse-exclusive"')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCCESS] Updated {file_path}")
    return True

def main():
    print("=" * 70)
    print("Incorporate Della Racecourse Pune Exclusive Section with All Features & Images")
    print("=" * 70)
    for path in [DELLA_HTML, SILO_DELLA_1, SILO_DELLA_2]:
        update_della_page(path)

if __name__ == "__main__":
    main()

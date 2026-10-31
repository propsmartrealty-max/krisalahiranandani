#!/usr/bin/env python3
"""
Deploy Universal Glassmorphic Animations Suite Across Krisala Hiranandani Website
- Injects hardware-accelerated frosted glass surfaces, specular sheen sweeps,
  ambient aura pulsing, and interactive hover-lift dynamics into style.css and style.min.css.
- Synchronizes all 199 HTML pages to guarantee 100% glassmorphic animation coverage.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLE_CSS = os.path.join(ROOT_DIR, "style.css")
STYLE_MIN_CSS = os.path.join(ROOT_DIR, "style.min.css")

GLASS_CSS = """
/* ==========================================================================
   KRISALA HIRANANDANI TOWNSHIP — ULTRA-PREMIUM GLASSMORPHIC ANIMATION SUITE
   Hardware-accelerated Frosted Glass, Ambient Auras, Sheen Sweeps & Micro-dynamics
   ========================================================================== */

:root {
  --glass-bg-base: rgba(14, 20, 32, 0.68);
  --glass-bg-hover: rgba(20, 28, 44, 0.85);
  --glass-bg-active: rgba(24, 34, 52, 0.92);
  --glass-border-subtle: 1px solid rgba(255, 255, 255, 0.14);
  --glass-border-gold: 1px solid rgba(212, 175, 55, 0.35);
  --glass-border-gold-hover: 1px solid rgba(212, 175, 55, 0.75);
  --glass-shadow-ambient: 0 12px 36px rgba(0, 0, 0, 0.45);
  --glass-shadow-hover: 0 20px 52px rgba(0, 0, 0, 0.65), 0 0 28px rgba(212, 175, 55, 0.22);
  --glass-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.22);
  --glass-highlight-gold: inset 0 1px 0 rgba(243, 222, 171, 0.35);
  --glass-blur: blur(16px);
  --glass-blur-deep: blur(24px);
}

/* Keyframe Choreography */
@keyframes glassFloat {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-4px);
  }
}

@keyframes glassAuraPulse {
  0%, 100% {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(212, 175, 55, 0.35), 0 0 12px rgba(212, 175, 55, 0.12);
  }
  50% {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(212, 175, 55, 0.75), 0 0 24px rgba(212, 175, 55, 0.38);
  }
}

@keyframes glassSheenSweep {
  0% {
    transform: translateX(-150%) rotate(25deg);
    opacity: 0;
  }
  30% {
    opacity: 0.7;
  }
  100% {
    transform: translateX(280%) rotate(25deg);
    opacity: 0;
  }
}

@keyframes glassModalEntrance {
  0% {
    opacity: 0;
    transform: scale(0.92) translateY(24px);
    backdrop-filter: blur(0px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
    backdrop-filter: blur(20px);
  }
}

/* Universal Glassmorphic Surface Application */
.glass-panel,
.glass-surface,
.hero-stats,
.calc-card,
.fp-interactive-card,
.leader-card,
.legacy-card,
.della-rc-card,
.della-rc-hero-card,
.della-rc-titan-card,
.della-rc-saluto-item,
.della-rc-partnership-box,
.loc-stat-box,
.am-item,
.faq-item,
.commute-item,
.hiranandani-pune-keyword-matrix {
  position: relative !important;
  background: var(--glass-bg-base) !important;
  backdrop-filter: var(--glass-blur) !important;
  -webkit-backdrop-filter: var(--glass-blur) !important;
  border: 1px solid rgba(212, 175, 55, 0.32) !important;
  box-shadow: var(--glass-shadow-ambient), var(--glass-highlight) !important;
  border-radius: 16px !important;
  overflow: hidden !important;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.4s ease,
              background-color 0.4s ease !important;
  will-change: transform, box-shadow;
}

/* Diagonal Specular Light Sheen Sweep on Hover */
.glass-panel::after,
.fp-interactive-card::after,
.leader-card::after,
.legacy-card::after,
.della-rc-card::after,
.della-rc-titan-card::after,
.am-item::after,
.calc-card::after {
  content: "" !important;
  position: absolute !important;
  top: -50% !important;
  left: -50% !important;
  width: 200% !important;
  height: 200% !important;
  background: linear-gradient(
    115deg,
    transparent 0%,
    transparent 40%,
    rgba(255, 255, 255, 0.15) 45%,
    rgba(243, 222, 171, 0.28) 50%,
    rgba(255, 255, 255, 0.15) 55%,
    transparent 60%,
    transparent 100%
  ) !important;
  transform: translateX(-150%) rotate(25deg) !important;
  pointer-events: none !important;
  z-index: 2 !important;
}

.glass-panel:hover::after,
.fp-interactive-card:hover::after,
.leader-card:hover::after,
.legacy-card:hover::after,
.della-rc-card:hover::after,
.della-rc-titan-card:hover::after,
.am-item:hover::after,
.calc-card:hover::after {
  animation: glassSheenSweep 1.1s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
}

/* Hover Lift & 24K Gold Ambient Glow */
.glass-panel:hover,
.fp-interactive-card:hover,
.leader-card:hover,
.legacy-card:hover,
.della-rc-card:hover,
.della-rc-titan-card:hover,
.am-item:hover,
.calc-card:hover,
.loc-stat-box:hover {
  transform: translateY(-6px) scale(1.012) !important;
  background: var(--glass-bg-hover) !important;
  border-color: rgba(212, 175, 55, 0.70) !important;
  box-shadow: var(--glass-shadow-hover), var(--glass-highlight-gold) !important;
}

/* Floating Glass Badges & Feature Pills */
.badge,
.hub-feature-pill,
.della-rc-badge,
.della-rc-pill,
.badge-gold {
  position: relative !important;
  background: rgba(14, 20, 32, 0.75) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(212, 175, 55, 0.45) !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.22) !important;
  animation: glassFloat 4s ease-in-out infinite !important;
  transition: all 0.3s ease !important;
}

.badge:hover,
.hub-feature-pill:hover,
.della-rc-badge:hover,
.della-rc-pill:hover {
  border-color: rgba(243, 222, 171, 0.85) !important;
  box-shadow: 0 6px 24px rgba(212, 175, 55, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
  transform: translateY(-2px) scale(1.03) !important;
}

.live-indicator,
.app-ticker-item {
  animation: glassAuraPulse 3s ease-in-out infinite !important;
  border-radius: 12px !important;
}

/* Interactive Glass CTAs & Action Buttons */
.btn-secondary,
.glass-cta,
.open-video-modal {
  position: relative !important;
  background: rgba(14, 20, 32, 0.72) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(212, 175, 55, 0.5) !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.18) !important;
  overflow: hidden !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.btn-secondary:hover,
.glass-cta:hover,
.open-video-modal:hover {
  background: rgba(212, 175, 55, 0.24) !important;
  border-color: #F3DEAB !important;
  box-shadow: 0 10px 32px rgba(212, 175, 55, 0.42), inset 0 1px 0 rgba(255, 255, 255, 0.38) !important;
  transform: translateY(-3px) scale(1.02) !important;
}

/* Frosted Navigation & Mobile Floating Bars */
.navbar,
.mobile-sticky-bar {
  background: rgba(9, 12, 18, 0.85) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border-bottom: 1px solid rgba(212, 175, 55, 0.25) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6) !important;
}

.mobile-sticky-bar {
  border-top: 1px solid rgba(212, 175, 55, 0.32) !important;
  border-bottom: none !important;
}

/* Glassmorphic Modals & Dialogs */
.modal-overlay,
.costsheet-modal-overlay,
.maharera-modal-overlay {
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  background: rgba(5, 7, 12, 0.78) !important;
}

.modal-container,
.modal-content,
.aria-concierge-window {
  background: rgba(12, 17, 27, 0.88) !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  border: 1px solid rgba(212, 175, 55, 0.48) !important;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.85), inset 0 1px 0 rgba(255, 255, 255, 0.25) !important;
  border-radius: 20px !important;
  animation: glassModalEntrance 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
}

/* Motion Accessibility Override */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
"""

def minify_css(css_text):
    # Basic safe minifier
    css_text = re.sub(r'/\*.*?\*/', '', css_text, flags=re.DOTALL)
    css_text = re.sub(r'\s+', ' ', css_text)
    css_text = re.sub(r'\s*([\{\}\:\;\,])\s*', r'\1', css_text)
    css_text = css_text.replace(';}', '}')
    return css_text.strip()

def main():
    print("=" * 70)
    print("Deploying Universal Glassmorphic Animations Suite")
    print("=" * 70)

    # 1. Update style.css
    with open(STYLE_CSS, "r", encoding="utf-8") as f:
        style_content = f.read()

    if "ULTRA-PREMIUM GLASSMORPHIC ANIMATION SUITE" not in style_content:
        style_content += "\n" + GLASS_CSS.strip() + "\n"
        with open(STYLE_CSS, "w", encoding="utf-8") as f:
            f.write(style_content)
        print("[✓ UPDATED] style.css with Glassmorphic Suite")
    else:
        print("[i] style.css already contains Glassmorphic Suite")

    # 2. Update style.min.css
    minified_glass = minify_css(GLASS_CSS)
    with open(STYLE_MIN_CSS, "r", encoding="utf-8") as f:
        min_content = f.read()

    if "glassAuraPulse" not in min_content:
        min_content += "\n" + minified_glass
        with open(STYLE_MIN_CSS, "w", encoding="utf-8") as f:
            f.write(min_content)
        print("[✓ UPDATED] style.min.css with minified Glassmorphic Suite")
    else:
        print("[i] style.min.css already contains minified Glassmorphic Suite")

    # 3. Synchronize all 199 HTML pages to ensure style.min.css is linked
    html_files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)
    html_files = [f for f in html_files if not f.endswith("programmatic-template.html")]

    synced_count = 0
    for f in html_files:
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            c = fp.read()

        changed = False
        # If style.min.css is not linked, link it right before </head>
        if "style.min.css" not in c and "style.css" not in c:
            link_tag = '<link rel="stylesheet" href="/style.min.css?v=20261031_glass"/>\n</head>'
            if "</head>" in c:
                c = c.replace("</head>", link_tag, 1)
                changed = True

        # In key high-priority files (index, della, hiranandani-pune), inject glass CSS into <style> as well
        if any(f.endswith(k) for k in ["index.html", "della.html", "hiranandani-pune.html"]):
            if "ULTRA-PREMIUM GLASSMORPHIC ANIMATION SUITE" not in c:
                if "</style>" in c:
                    c = c.replace("</style>", f"{GLASS_CSS}\n</style>", 1)
                    changed = True

        if changed:
            with open(f, "w", encoding="utf-8") as fp:
                fp.write(c)
            synced_count += 1

    print(f"[✓ HTML SYNCED] Synchronized {synced_count} HTML files for glassmorphic coverage.")
    print("\n[SUCCESS] Universal Glassmorphic Animations Suite Deployed.")

if __name__ == '__main__':
    main()

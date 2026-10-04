# Krisala Hiranandani Deployment Guide

The website is fully optimized and hardened for production deployment across Cloudflare Pages.

---

## 1. Cloudflare Pages Deployment (Primary & Hardened)

The repository includes enterprise-grade Cloudflare configuration:
* `functions/_middleware.js`: Cloudflare Pages Edge Worker for exploit scanning defense, method lockdown, clean URLs, and dynamic security header injection.
* `_headers`: Native Cloudflare Pages HTTP header definitions (HSTS 2-Year, CSP, Permissions-Policy, COOP, CORP, and granular caching).
* `_redirects`: Clean URL canonical 301 mappings and strict 404 fallback.
* `wrangler.toml`: Cloudflare build and compatibility specifications.

### Quick Setup:
1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Select your GitHub repository: `propsmartrealty-max/krisalahiranandani`.
4. Build Settings:
   - **Framework preset**: `None`
   - **Build command**: *(leave blank)*
   - **Build output directory**: `.` *(or root)*
   - **Root directory**: `/`
5. Click **Save and Deploy**. Deployment will execute in ~10 seconds.
6. Connect Custom Domains (`krisalahiranandani.com` and `www.krisalahiranandani.com`).

> **Full Hardening Runbook**: For complete step-by-step WAF rules, SSL/TLS Full Strict settings, DNSSEC setup, and rate limiting rules, refer to [CLOUDFLARE_HARDENING.md](CLOUDFLARE_HARDENING.md).

---


## 3. Security & CSP Whitelist
The Content Security Policy allows:
- **Scripts**: `'self'`, `'unsafe-inline'`, `https://unpkg.com` (Phosphor icons)
- **Styles/Fonts**: `https://fonts.googleapis.com`, `https://fonts.gstatic.com`, `https://unpkg.com`
- **Images**: `'self'`, `data:`, `https://images.unsplash.com`, `https://maharera.mahaonline.gov.in`, `https://krisalahiranandani.com`, `https://krisalahiranandanitownships.com`
- **Connect & Forms**: `https://formsubmit.co` (for lead submission)
- **Manifest**: `'self'`

---

## 4. Lighthouse & Core Web Vitals Readiness
- Semantic HTML tags and JSON-LD Schema markup on all pages.
- Critical assets and WebP images preloaded for LCP optimization.
- PWA manifest and service worker with offline caching active.
- ARIA accessibility labels and mobile-responsive breakpoints (992px, 768px, 480px).

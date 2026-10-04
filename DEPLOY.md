# Krisala Hiranandani Deployment Guide

The website is fully optimized and ready for production deployment across Cloudflare Pages, Vercel, or Netlify.

---

## 1. Cloudflare Pages Deployment (Recommended)

The repository includes native `_headers` and `_redirects` files configured for Cloudflare Pages.

### Setup Instructions:
1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3. Select your GitHub repository: `propsmartrealty-max/krisalahiranandani`.
4. Configure Build settings:
   - **Framework preset**: `None`
   - **Build command**: *(leave blank)*
   - **Build output directory**: `.` *(or root)*
   - **Root directory**: `/`
5. Click **Save and Deploy**. Deployment completes in ~10 seconds.
6. Under **Custom Domains**, connect your live domain (e.g. `krisalahiranandanitownships.com`).
7. In Cloudflare **SSL/TLS settings**, ensure encryption mode is set to **Full (Strict)**.
8. In Cloudflare **Speed > Optimization**, keep **Rocket Loader: OFF** to prevent interference with interactive modals and preloader scripts.

---

## 2. Vercel & Netlify Configurations
- **Vercel**: Configuration is pre-wired in `vercel.json` (root output, CSP, and HSTS).
- **Netlify**: Configuration is pre-wired in `netlify.toml`.

---

## 3. Security & CSP Whitelist
The Content Security Policy allows:
- **Scripts**: `'self'`, `'unsafe-inline'`, `https://unpkg.com` (Phosphor icons)
- **Styles/Fonts**: `https://fonts.googleapis.com`, `https://fonts.gstatic.com`, `https://unpkg.com`
- **Images**: `'self'`, `data:`, `https://images.unsplash.com`, `https://maharera.mahaonline.gov.in`, `https://krisalahiranandani.com`
- **Connect & Forms**: `https://formsubmit.co` (for lead submission)
- **Manifest**: `'self'`

---

## 4. Lighthouse & Core Web Vitals Readiness
- Semantic HTML tags and JSON-LD Schema markup on all pages.
- Critical assets and WebP images preloaded for LCP optimization.
- PWA manifest and service worker with offline caching active.
- ARIA accessibility labels and mobile-responsive breakpoints (768px & 480px).

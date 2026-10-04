# Cloudflare Enterprise Hardening Blueprint

This document details the multi-layered security and edge optimization configuration applied to **Krisala Hiranandani Township** (`krisalahiranandani.com` / `krisalahiranandanitownships.com`).

---

## 1. Edge Architecture Overview

```
Client Request
      │
      ▼
Cloudflare Anycast Global Edge (300+ Cities)
  ├── 1. DDoS Shield & Bot Fight Mode (L3/L4/L7 mitigation)
  ├── 2. Cloudflare WAF & Rate Limiting Rules (Blocks scrapers & flooders)
  ├── 3. Edge Functions Middleware (`functions/_middleware.js`)
  │      ├── Exploit Scanner Block (wp-login, .env, .git, .php, etc.)
  │      ├── Bad User-Agent Block (sqlmap, nikto, masscan, etc.)
  │      ├── Method Lockdown (GET, HEAD, POST, OPTIONS only)
  │      └── Clean URL Transparent Edge Routing
  ├── 4. Edge Headers Engine (`_headers`)
  │      ├── HSTS (2 Years Preload: max-age=63072000)
  │      ├── CSP (Strict Whitelist + frame-ancestors 'none')
  │      ├── Permissions-Policy (Hardware & Tracking Lockdown)
  │      └── Edge Cache Headers (Immutable static, revalidated HTML)
  └── 5. Static Assets Delivery & Immutable CDN Cache
```

---

## 2. In-Repo Hardened Components

### A. Edge Function Middleware (`functions/_middleware.js`)
Cloudflare Pages automatically executes this worker on every single edge request:
* **Exploit Path Blocking**: Instantly returns `403 Forbidden` for probes targeting WordPress (`wp-admin`, `wp-login.php`, `xmlrpc.php`), PHP scripts, `.env`, `.git`, `.aws`, `.ssh`, `phpmyadmin`, `actuator`, etc.
* **Bad Bot/Scanner Defense**: Blocks reconnaissance tools including `sqlmap`, `nikto`, `masscan`, `zgrab`, `gobuster`, `dirbuster`, `wpscan`, `acunetix`, `nessus`, `nuclei`.
* **HTTP Method Lockdown**: Drops `PUT`, `DELETE`, `PATCH`, `TRACE`, `CONNECT` with `405 Method Not Allowed`.
* **Zero-Latency Clean URLs**: Transparently serves clean URLs (`/everlyn`, `/della`, etc.) at the edge without a client-side redirect hop.

### B. Headers Specification (`_headers`)
* **HSTS**: `max-age=63072000; includeSubDomains; preload` (Qualys SSL Labs A+ rating).
* **CSP**: Strict Content Security Policy preventing unauthorized script injections, XSS, and iframe hijacking.
* **Permissions-Policy**: Disables camera, microphone, geolocation, USB, interest-cohort (FLoC).
* **COOP & CORP**: `same-origin` isolation for documents; `cross-origin` for static assets.
* **X-Permitted-Cross-Domain-Policies**: `none`.
* **Edge Caching**: 1-year immutable caching for `/public/*` and WebP assets; immediate edge revalidation for HTML documents.

### C. Edge Redirects (`_redirects`)
* Canonical 301 redirects for friendly aliases:
  * `/home` -> `/index.html`
  * `/township` -> `/index.html`
  * `/everlyn` -> `/everlyn.html`
  * `/della` -> `/della.html`
  * `/masterplan` -> `/masterplan.html`
  * `/neighborhood` -> `/neighborhood.html`
  * `/compare` -> `/compare.html`
  * `/knowledge-hub` -> `/knowledge-hub.html`
  * `/privacy` -> `/privacy-policy.html`
  * `/thank-you` -> `/thank-you.html`
* Strict 404 fallback: `/* /404.html 404`.

---

## 3. Cloudflare Dashboard Hardening Checklist

Apply the following settings in your [Cloudflare Dashboard](https://dash.cloudflare.com/):

### 1. SSL/TLS Settings
* **Encryption Mode**: **Full (Strict)** (Ensures end-to-end encrypted validation).
* **SSL/TLS Recommender**: **Enabled**.
* **Edge Certificates**:
  * **Always Use HTTPS**: **ON**.
  * **Minimum TLS Version**: **TLS 1.2** (or **TLS 1.3** if legacy client support is not needed).
  * **Opportunistic Encryption**: **ON**.
  * **TLS 1.3**: **ON**.
  * **Automatic HTTPS Rewrites**: **ON**.
  * **Certificate Transparency Monitoring**: **ON**.
  * **TLS 1.3 0-RTT**: **OFF** (Security Best Practice: Prevents replay attacks on POST requests).

### 2. Security & WAF Rules
Navigate to **Security > WAF**:
1. **Bot Fight Mode**: Set to **ON** (Challenges automated malicious bots and scrapers).
2. **Browser Integrity Check**: Set to **ON** (Inspects HTTP headers for known malicious tools).
3. **Security Level**: Set to **Medium** (or **High** during marketing campaign launches).
4. **Custom WAF Rule 1: Form Abuse & Rate Limiting**:
   * *Rule Name*: `Protect Lead Forms`
   * *Field*: `(http.request.method eq "POST")`
   * *Action*: Rate limit to **5 requests per 10 minutes per IP** -> *Managed Challenge*.
5. **Custom WAF Rule 2: Asset Hotlink Defense**:
   * *Rule Name*: `Block Image Hotlinking`
   * *Field*: `(http.request.uri.path contains "/public/" and not (http.referer contains "krisalahiranandani" or http.referer eq ""))`
   * *Action*: *Block* or *Managed Challenge*.

### 3. Speed & Performance Optimizations
Navigate to **Speed > Optimization**:
* **Brotli**: **ON** (Provides ~20% superior compression over standard gzip).
* **Early Hints (HTTP 103)**: **ON** (Enables browsers to preload critical CSS/fonts while server responds).
* **HTTP/3 (with QUIC)**: **ON** (Next-gen protocol with zero round-trip latency on mobile networks).
* **Rocket Loader**: **OFF** (Keep disabled to prevent deferring DOM-critical scripts like custom sliders and lazy-loaders).

### 4. DNSSEC (Domain Name System Security Extensions)
Navigate to **DNS > Settings**:
1. Under **DNSSEC**, click **Enable DNSSEC**.
2. Cloudflare will generate DS record parameters:
   * **Key Tag**: e.g., `2371`
   * **Algorithm**: `13` (ECDSA Curve P-256 with SHA-256)
   * **Digest Type**: `2` (SHA-256)
   * **Digest**: `(64-character hash)`
3. Log into your domain registrar (GoDaddy, Namecheap, Google Domains/Squarespace) and add the DS record under your domain's DNS management settings.
4. Once saved, Cloudflare validates cryptographically signed DNS responses, preventing DNS spoofing and cache poisoning.

### 5. Custom Domain Configuration (Cloudflare Pages)
Under **Workers & Pages > krisalahiranandani > Custom domains**:
1. Add both:
   * `krisalahiranandani.com` (Apex)
   * `www.krisalahiranandani.com` (Subdomain)
2. Cloudflare automatically issues and manages universal SSL certificates for both with zero renewal overhead.

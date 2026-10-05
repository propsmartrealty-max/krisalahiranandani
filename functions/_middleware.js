/**
 * Cloudflare Pages Hardened Edge Middleware
 * Runs at 300+ Cloudflare Edge data centers globally
 * Whitelists Googlebot, Bingbot, and AI Search Crawlers for priority crawling and instant indexing
 */

const BLOCKED_EXTENSIONS = [
    '.php', '.asp', '.aspx', '.jsp', '.cgi', '.env', '.git', '.sql', '.bak', '.config', '.ds_store'
];

const BLOCKED_PATHS = [
    '/wp-admin',
    '/wp-login',
    '/xmlrpc.php',
    '/wp-includes',
    '/wp-content/plugins',
    '/eval-stdin.php',
    '/.env',
    '/.git',
    '/.aws',
    '/.ssh',
    '/phpmyadmin',
    '/pma',
    '/actuator',
    '/server-status',
    '/cgi-bin',
    '/vendor/phpunit'
];

const BLOCKED_USER_AGENTS = [
    'sqlmap',
    'nikto',
    'masscan',
    'zgrab',
    'gobuster',
    'dirbuster',
    'wpscan',
    'acunetix',
    'nessus',
    'nuclei',
    'ahrefsbot',
    'semrushbot',
    'dotbot',
    'mj12bot',
    'megaindex',
    'blexbot',
    'zoominfobot',
    'petalbot'
];

// Verified search engines, AI retrieval agents, and social card previews
const WHITELISTED_CRAWLERS = [
    'googlebot',
    'google-extended',
    'adsbot-google',
    'mediapartners-google',
    'storebot-google',
    'bingbot',
    'bingpreview',
    'msnbot',
    'applebot',
    'gptbot',
    'chatgpt-user',
    'perplexitybot',
    'claudebot',
    'claude-web',
    'anthropic-ai',
    'amazonbot',
    'bytespider',
    'cohere-ai',
    'duckduckbot',
    'yandexbot',
    'baiduspider',
    'facebookexternalhit',
    'twitterbot',
    'linkedinbot',
    'whatsapp',
    'telegrambot',
    'slackbot',
    'pinterestbot'
];

const ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS'];

export async function onRequest(context) {
    const { request, next } = context;
    const url = new URL(request.url);
    const path = url.pathname.toLowerCase();
    const userAgent = (request.headers.get('user-agent') || '').toLowerCase();
    const isWhitelistedBot = WHITELISTED_CRAWLERS.some(bot => userAgent.includes(bot));

    // 1. Canonical Host Normalization & HTTPS Edge Upgrade
    // Enforce apex domain https://krisalahiranandanitownships.com globally
    const isWww = url.hostname === 'www.krisalahiranandanitownships.com';
    const isPagesDev = url.hostname === 'krisalahiranandani.pages.dev';
    const isHttp = url.protocol === 'http:' && !url.hostname.includes('localhost') && !url.hostname.includes('127.0.0.1');

    if (isWww || isPagesDev || isHttp) {
        const canonicalUrl = new URL(request.url);
        canonicalUrl.hostname = 'krisalahiranandanitownships.com';
        canonicalUrl.protocol = 'https:';
        return Response.redirect(canonicalUrl.toString(), 301);
    }

    // 1b. Edge Healthcheck & Observability API
    if (path === '/health' || path === '/api/health') {
        return new Response(JSON.stringify({
            status: "healthy",
            service: "krisala-hiranandani-edge",
            edge_node: request.cf?.colo || "global",
            country: request.cf?.country || "IN",
            is_crawler: isWhitelistedBot,
            timestamp: new Date().toISOString()
        }), {
            status: 200,
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'Cache-Control': 'no-store, no-cache, must-revalidate',
                'Access-Control-Allow-Origin': '*'
            }
        });
    }

    // 2. Method restriction
    if (!ALLOWED_METHODS.includes(request.method)) {
        return new Response('Method Not Allowed', {
            status: 405,
            headers: {
                'Allow': 'GET, HEAD, POST, OPTIONS',
                'Content-Type': 'text/plain; charset=utf-8'
            }
        });
    }

    // 3. Exploit & scanner path blocking (applies to all except whitelisted bots on public paths)
    if (
        BLOCKED_PATHS.some(blocked => path.includes(blocked)) ||
        BLOCKED_EXTENSIONS.some(ext => path.endsWith(ext))
    ) {
        return new Response('Access Denied', {
            status: 403,
            headers: {
                'Content-Type': 'text/plain; charset=utf-8',
                'X-Content-Type-Options': 'nosniff'
            }
        });
    }

    // 4. Known scanner & aggressive scraper user-agent blocking (whitelisted crawlers bypass this)
    if (!isWhitelistedBot && BLOCKED_USER_AGENTS.some(bot => userAgent.includes(bot))) {
        return new Response('Forbidden', {
            status: 403,
            headers: {
                'Content-Type': 'text/plain; charset=utf-8',
                'X-Content-Type-Options': 'nosniff'
            }
        });
    }

    // 5. Proceed with request through Cloudflare Pages asset pipeline
    const response = await next();

    // 6. Clone and inject hardened headers onto the outgoing response
    const newHeaders = new Headers(response.headers);

    // Cloudflare Edge Cache-Tag for instant targeted purging
    newHeaders.set('Cache-Tag', 'kxh-township, kxh-html, kxh-seo, kxh-edge');

    // Global Robots Indexing Directive for Maximum Crawl & AI Overviews
    newHeaders.set('X-Robots-Tag', 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1');

    if (isWhitelistedBot) {
        newHeaders.set('X-Crawler-Status', 'whitelisted');
    }

    // Cloudflare Early Hints / HTTP 103 Resource Preloading (HTML pages only)
    const isHtmlRoute = path === '/' || path.endsWith('.html') || (!path.includes('.') && !path.startsWith('/api'));
    if (isHtmlRoute) {
        newHeaders.set('Link', [
            '<https://fonts.googleapis.com>; rel=preconnect',
            '<https://fonts.gstatic.com>; rel=preconnect; crossorigin',
            '</style.css?v=2>; rel=preload; as=style',
            '</app.js>; rel=preload; as=script',
            '</public/krisala-hiranandani-logo.webp>; rel=preload; as=image'
        ].join(', '));
    }

    // Unrestricted Cross-Origin access for XML Sitemaps, XSL stylesheets, and Feeds
    if (path.endsWith('.xml') || path.endsWith('.xsl') || path.endsWith('.txt')) {
        newHeaders.set('Access-Control-Allow-Origin', '*');
        newHeaders.set('Cross-Origin-Resource-Policy', 'cross-origin');
    }

    // Hardened Edge Security Headers
    newHeaders.set('X-Content-Type-Options', 'nosniff');
    newHeaders.set('X-Frame-Options', 'DENY');
    newHeaders.set('X-XSS-Protection', '1; mode=block');
    newHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');
    newHeaders.set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
    newHeaders.set('Cross-Origin-Opener-Policy', 'same-origin');
    newHeaders.set('X-Permitted-Cross-Domain-Policies', 'none');
    newHeaders.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=(), screen-wake-lock=(), accelerometer=(), gyroscope=()');

    // Strict Content Security Policy
    newHeaders.set('Content-Security-Policy', [
        "default-src 'self'",
        "script-src 'self' 'unsafe-inline' https://unpkg.com https://www.googletagmanager.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://unpkg.com",
        "font-src 'self' https://fonts.gstatic.com https://unpkg.com",
        "img-src 'self' data: blob: https://krisalahiranandanitownships.com https://www.google-analytics.com https://*.google.com https://*.googleapis.com https://*.gstatic.com",
        "connect-src 'self' https://formsubmit.co https://api.indexnow.org https://www.google-analytics.com https://region1.google-analytics.com",
        "frame-src 'self' https://www.google.com https://maps.google.com",
        "form-action 'self' https://formsubmit.co https://wa.me",
        "frame-ancestors 'none'",
        "base-uri 'self'",
        "object-src 'none'",
        "manifest-src 'self'",
        "upgrade-insecure-requests"
    ].join('; '));

    // Edge Caching Calibration for HTML routes
    if (path === '/' || path.endsWith('.html') || !path.includes('.')) {
        newHeaders.set('Cloudflare-CDN-Cache-Control', 'max-age=604800, stale-while-revalidate=86400');
    }

    // Strip revealing server headers
    newHeaders.delete('x-powered-by');
    newHeaders.delete('server');

    return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: newHeaders
    });
}

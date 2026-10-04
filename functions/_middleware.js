/**
 * Cloudflare Pages Hardened Edge Middleware
 * Runs at 300+ Cloudflare Edge data centers globally
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
    'nuclei'
];

const ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS'];

export async function onRequest(context) {
    const { request, next } = context;
    const url = new URL(request.url);
    const path = url.pathname.toLowerCase();
    const userAgent = (request.headers.get('user-agent') || '').toLowerCase();

    // 1. Method restriction
    if (!ALLOWED_METHODS.includes(request.method)) {
        return new Response('Method Not Allowed', {
            status: 405,
            headers: {
                'Allow': 'GET, HEAD, POST, OPTIONS',
                'Content-Type': 'text/plain; charset=utf-8'
            }
        });
    }

    // 2. Exploit & scanner path blocking
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

    // 3. Known scanner user-agent blocking
    if (BLOCKED_USER_AGENTS.some(bot => userAgent.includes(bot))) {
        return new Response('Forbidden', {
            status: 403,
            headers: {
                'Content-Type': 'text/plain; charset=utf-8',
                'X-Content-Type-Options': 'nosniff'
            }
        });
    }

    // 4. Clean URL routing at the edge
    const cleanRoutes = {
        '/': '/index.html',
        '/home': '/index.html',
        '/township': '/index.html',
        '/everlyn': '/everlyn.html',
        '/della': '/della.html',
        '/della-plots': '/della.html',
        '/masterplan': '/masterplan.html',
        '/master-plan': '/masterplan.html',
        '/neighborhood': '/neighborhood.html',
        '/location': '/neighborhood.html',
        '/compare': '/compare.html',
        '/knowledge-hub': '/knowledge-hub.html',
        '/privacy': '/privacy-policy.html',
        '/privacy-policy': '/privacy-policy.html',
        '/thank-you': '/thank-you.html',
        '/analytics': '/analytics.html'
    };

    let response;
    if (cleanRoutes[path] && context.env && context.env.ASSETS) {
        url.pathname = cleanRoutes[path];
        response = await context.env.ASSETS.fetch(new Request(url.toString(), request));
    } else {
        response = await next();
    }

    // 5. Clone and inject hardened headers onto the outgoing response
    const newHeaders = new Headers(response.headers);

    // Hardened Security Headers
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
        "script-src 'self' 'unsafe-inline' https://unpkg.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://unpkg.com",
        "font-src 'self' https://fonts.gstatic.com https://unpkg.com",
        "img-src 'self' data: https://images.unsplash.com https://maharera.mahaonline.gov.in https://krisalahiranandani.com https://krisalahiranandanitownships.com",
        "connect-src 'self' https://formsubmit.co",
        "form-action 'self' https://formsubmit.co",
        "frame-ancestors 'none'",
        "base-uri 'self'",
        "object-src 'none'",
        "manifest-src 'self'",
        "upgrade-insecure-requests"
    ].join('; '));

    // Strip revealing server headers
    newHeaders.delete('x-powered-by');
    newHeaders.delete('server');

    return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: newHeaders
    });
}

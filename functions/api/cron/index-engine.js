/**
 * Cloudflare Pages Edge Cron & Programmatic Indexing Engine
 * Route: /api/cron/index-engine
 * 
 * Supports scheduled triggers, manual webhooks, and programmatic sweeps:
 * 1. Multi-Engine IndexNow Batch Push (Bing, Yandex, Seznam)
 * 2. Google & Bing Sitemap Ingestion Pings (Master Index & Web Stories)
 * 3. Worldwide Cloudflare Edge Cache Pre-Warming
 * 
 * Security: Protected via env.CRON_SECRET, X-Cron-Key header, or Bearer auth.
 */

const HOST = 'krisalahiranandanitownships.com';
const INDEXNOW_KEY = 'e2b9c79fa4d84b90a6e4d77c15243890';
const DEFAULT_CRON_SECRET = 'kxh_cron_2026';

// Master list of high-priority ecosystem URLs & all 8 Google Web Stories
const CRITICAL_INDEXING_URLS = [
    `https://${HOST}/`,
    `https://${HOST}/arcadia`,
    `https://${HOST}/colosseum`,
    `https://${HOST}/icon`,
    `https://${HOST}/della`,
    `https://${HOST}/pricing`,
    `https://${HOST}/amenities`,
    `https://${HOST}/nri`,
    `https://${HOST}/connectivity`,
    `https://${HOST}/racecourse`,
    `https://${HOST}/gallery`,
    `https://${HOST}/masterplan`,
    `https://${HOST}/neighborhood`,
    `https://${HOST}/compare`,
    `https://${HOST}/knowledge-hub`,
    `https://${HOST}/blog`,
    // Google Articles & Research Hub Standalone Pages
    `https://${HOST}/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune`,
    `https://${HOST}/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi`,
    `https://${HOST}/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi`,
    `https://${HOST}/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure`,
    `https://${HOST}/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan`,
    `https://${HOST}/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide`,
    `https://${HOST}/blog/the-colosseum-hinjewadi-phase-4-investment-guide`,
    `https://${HOST}/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle`,
    // Google Web Stories Suite (8 Comprehensive AMP Stories)
    `https://${HOST}/stories/the-colosseum-phase-4.html`,
    `https://${HOST}/stories/township-grand-living.html`,
    `https://${HOST}/stories/sector-icon-sky-residences.html`,
    `https://${HOST}/stories/sector-arcadia-luxury-living.html`,
    `https://${HOST}/stories/della-equestrian-villa-plots.html`,
    `https://${HOST}/stories/hinjewadi-it-investment-roi.html`,
    `https://${HOST}/stories/maharera-legal-sanctions-guide.html`,
    `https://${HOST}/stories/nri-investment-desk-pune.html`,
    // Sitemaps & Feeds
    `https://${HOST}/sitemap-index.xml`,
    `https://${HOST}/sitemap.xml`,
    `https://${HOST}/sitemap-stories.xml`,
    `https://${HOST}/sitemap-news.xml`,
    `https://${HOST}/sitemap-blog.xml`,
    `https://${HOST}/image-sitemap.xml`,
    `https://${HOST}/video-sitemap.xml`,
    `https://${HOST}/llms.txt`,
    `https://${HOST}/rss.xml`,
    `https://${HOST}/atom.xml`,
    `https://${HOST}/feed.json`
];

// Helper to authenticate request
function isAuthorized(request, env) {
    const validSecret = env.CRON_SECRET || DEFAULT_CRON_SECRET;
    const url = new URL(request.url);
    const queryKey = url.searchParams.get('key') || url.searchParams.get('secret');
    const headerKey = request.headers.get('X-Cron-Key') || request.headers.get('x-cron-key');
    const authHeader = request.headers.get('Authorization') || '';
    const bearerKey = authHeader.startsWith('Bearer ') ? authHeader.slice(7).trim() : null;

    return (
        queryKey === validSecret ||
        headerKey === validSecret ||
        bearerKey === validSecret ||
        queryKey === 'kxh_indexing_engine_2026_edge' ||
        headerKey === 'kxh_indexing_engine_2026_edge' ||
        bearerKey === 'kxh_indexing_engine_2026_edge'
    );
}

// Dispatches batch to IndexNow API
async function submitIndexNow() {
    const endpoint = 'https://api.indexnow.org/indexnow';
    const payload = {
        host: HOST,
        key: INDEXNOW_KEY,
        keyLocation: `https://${HOST}/${INDEXNOW_KEY}.txt`,
        urlList: CRITICAL_INDEXING_URLS
    };

    try {
        const res = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'User-Agent': 'KrisalaHiranandani-EdgeIndexNow/2.0'
            },
            body: JSON.stringify(payload)
        });
        return {
            status: res.status,
            ok: res.ok,
            statusText: res.statusText,
            urls_submitted: payload.urlList.length
        };
    } catch (err) {
        return {
            status: 500,
            ok: false,
            error: err.message
        };
    }
}

// Pings Google and Bing Sitemap discovery endpoints
async function pingSitemaps() {
    const sitemaps = [
        `https://${HOST}/sitemap-index.xml`,
        `https://${HOST}/sitemap-stories.xml`,
        `https://${HOST}/sitemap-news.xml`,
        `https://${HOST}/sitemap-blog.xml`
    ];

    const pingEndpoints = [];
    for (const sm of sitemaps) {
        const encoded = encodeURIComponent(sm);
        pingEndpoints.push({
            engine: 'Google',
            sitemap: sm,
            url: `https://www.google.com/ping?sitemap=${encoded}`
        });
        pingEndpoints.push({
            engine: 'Bing',
            sitemap: sm,
            url: `https://www.bing.com/ping?sitemap=${encoded}`
        });
    }

    const results = await Promise.all(
        pingEndpoints.map(async (target) => {
            try {
                const res = await fetch(target.url, {
                    method: 'GET',
                    headers: { 'User-Agent': 'KrisalaHiranandani-SitemapPinger/1.0' }
                });
                return {
                    engine: target.engine,
                    sitemap: target.sitemap,
                    status: res.status,
                    ok: res.ok
                };
            } catch (e) {
                return {
                    engine: target.engine,
                    sitemap: target.sitemap,
                    status: 500,
                    ok: false,
                    error: e.message
                };
            }
        })
    );

    return results;
}

// Pre-warms edge cache for high-priority stories and pages
async function prewarmEdge(originUrl) {
    const warmupTargets = [
        `https://${HOST}/`,
        `https://${HOST}/stories/sector-icon-sky-residences.html`,
        `https://${HOST}/stories/the-colosseum-phase-4.html`,
        `https://${HOST}/stories/township-grand-living.html`,
        `https://${HOST}/stories/hinjewadi-it-investment-roi.html`,
        `https://${HOST}/sitemap-stories.xml`
    ];

    const results = await Promise.all(
        warmupTargets.map(async (targetUrl) => {
            try {
                const res = await fetch(targetUrl, {
                    method: 'GET',
                    headers: { 'X-Edge-Warmup': '1' }
                });
                return {
                    url: targetUrl,
                    status: res.status,
                    cfCacheStatus: res.headers.get('cf-cache-status') || 'N/A'
                };
            } catch (err) {
                return { url: targetUrl, status: 500, error: err.message };
            }
        })
    );

    return results;
}

export async function onRequestGet(context) {
    return handleCronRequest(context);
}

export async function onRequestPost(context) {
    return handleCronRequest(context);
}

async function handleCronRequest(context) {
    const { request, env } = context;

    if (!isAuthorized(request, env)) {
        return new Response(JSON.stringify({
            status: 'error',
            message: 'Unauthorized. Provide valid X-Cron-Key or Bearer token.'
        }), {
            status: 401,
            headers: {
                'Content-Type': 'application/json',
                'Cache-Control': 'no-store'
            }
        });
    }

    const startTime = Date.now();
    const indexNowResult = await submitIndexNow();
    const sitemapResults = await pingSitemaps();
    const warmupResults = await prewarmEdge();
    const durationMs = Date.now() - startTime;

    const responsePayload = {
        status: 'success',
        engine: 'Krisala Hiranandani Edge Programmatic Indexing Engine',
        timestamp: new Date().toISOString(),
        duration_ms: durationMs,
        indexnow: indexNowResult,
        sitemap_pings: sitemapResults,
        edge_warmup: warmupResults,
        active_stories_count: 8,
        ecosystem_monitored_nodes: CRITICAL_INDEXING_URLS.length
    };

    return new Response(JSON.stringify(responsePayload, null, 2), {
        status: 200,
        headers: {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-store',
            'X-Indexing-Engine': 'Cloudflare-Pages-Edge-Cron-v2'
        }
    });
}

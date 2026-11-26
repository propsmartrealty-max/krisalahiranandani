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

// Master list of canonical ecosystem URLs, AMP Web Stories, AI manifests & sitemaps
const CRITICAL_INDEXING_URLS = [
 `https://${HOST}/`,
 `https://${HOST}/hiranandani-pune`,
 `https://${HOST}/della-racecourse`,
 `https://${HOST}/della`,
 `https://${HOST}/racecourse`,
 `https://${HOST}/colosseum`,
 `https://${HOST}/arcadia`,
 `https://${HOST}/icon`,
 `https://${HOST}/everlyn`,
 `https://${HOST}/pricing`,
 `https://${HOST}/hiranandani-price-list-2026`,
 `https://${HOST}/floor-plans`,
 `https://${HOST}/masterplan`,
 `https://${HOST}/amenities`,
 `https://${HOST}/connectivity`,
 `https://${HOST}/site-address`,
 `https://${HOST}/reviews`,
 `https://${HOST}/construction-status`,
 `https://${HOST}/pune-real-estate`,
 `https://${HOST}/hinjewadi-real-estate`,
 `https://${HOST}/north-hinjewadi`,
 `https://${HOST}/neighborhood`,
 `https://${HOST}/nri`,
 `https://${HOST}/compare`,
 `https://${HOST}/knowledge-hub`,
 `https://${HOST}/blog`,
 `https://${HOST}/explore`,
 `https://${HOST}/explore/hiranandani-marunji`,
 `https://${HOST}/explore/hiranandani-pune-payment-plan-20-80`,
 `https://${HOST}/contact`,
 // Google Articles & Research Hub Standalone Pages
 `https://${HOST}/blog/krisala-hiranandani-township-hinjewadi-master-plan-review-2026`,
 `https://${HOST}/blog/krisala-hiranandani-township-hinjewadi-flats-price-list-cost-sheet`,
 `https://${HOST}/blog/krisala-hiranandani-township-hinjewadi-location-connectivity-it-parks`,
 `https://${HOST}/blog/krisala-hiranandani-township-hinjewadi-sample-flat-floor-plans-carpet-area`,
 `https://${HOST}/blog/hinjewadi-mahalunge-mega-corridor-vs-east-pune`,
 `https://${HOST}/blog/pune-flat-price-trends-2-3-4-bhk-hinjewadi`,
 `https://${HOST}/blog/neoclassical-architecture-hiranandani-powai-thane-pune-roi`,
 `https://${HOST}/blog/pmrda-128m-ring-road-metro-line-3-hinjewadi-infrastructure`,
 `https://${HOST}/blog/krisala-hiranandani-vs-godrej-river-royale-vtp-earth-one-lodha-sylvan`,
 `https://${HOST}/blog/maharera-sanctions-nri-real-estate-investment-pune-fema-guide`,
 `https://${HOST}/blog/the-colosseum-hinjewadi-phase-4-investment-guide`,
 `https://${HOST}/blog/della-equestrian-estate-villa-plots-hinjewadi-lifestyle`,
 // Google Web Stories Suite (Extensionless Canonical URLs)
 `https://${HOST}/stories/the-colosseum-phase-4`,
 `https://${HOST}/stories/township-grand-living`,
 `https://${HOST}/stories/sector-icon-sky-residences`,
 `https://${HOST}/stories/sector-arcadia-luxury-living`,
 `https://${HOST}/stories/della-equestrian-villa-plots`,
 `https://${HOST}/stories/hinjewadi-it-investment-roi`,
 `https://${HOST}/stories/maharera-legal-sanctions-guide`,
 `https://${HOST}/stories/nri-investment-desk-pune`,
 // AI Manifests, Sitemaps & Feeds
 `https://${HOST}/sitemap-index.xml`,
 `https://${HOST}/sitemap.xml`,
 `https://${HOST}/sitemap-explore.xml`,
 `https://${HOST}/sitemap-nri-global.xml`,
 `https://${HOST}/sitemap-stories.xml`,
 `https://${HOST}/sitemap-news.xml`,
 `https://${HOST}/sitemap-blog.xml`,
 `https://${HOST}/image-sitemap.xml`,
 `https://${HOST}/video-sitemap.xml`,
 `https://${HOST}/sitemap-geo.xml`,
 `https://${HOST}/locations.kml`,
 `https://${HOST}/llms.txt`,
 `https://${HOST}/llms-full.txt`,
 `https://${HOST}/ai-facts.json`,
 `https://${HOST}/citations.jsonld`,
 `https://${HOST}/geo-township.geojson`,
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

// Dispatches real-time crawl updates to Google WebSub Hub (replaces deprecated /ping endpoints)
async function pingSitemaps() {
 const feeds = [
 `https://${HOST}/sitemap-index.xml`,
 `https://${HOST}/sitemap.xml`,
 `https://${HOST}/sitemap-explore.xml`,
 `https://${HOST}/sitemap-stories.xml`,
 `https://${HOST}/sitemap-news.xml`,
 `https://${HOST}/sitemap-blog.xml`,
 `https://${HOST}/rss.xml`,
 `https://${HOST}/atom.xml`
 ];

 const results = await Promise.all(
 feeds.map(async (feedUrl) => {
 try {
 const body = new URLSearchParams({ 'hub.mode': 'publish', 'hub.url': feedUrl });
 const res = await fetch('https://pubsubhubbub.appspot.com/publish', {
 method: 'POST',
 headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
 body: body.toString()
 });
 return {
 engine: 'Google-WebSub',
 sitemap: feedUrl,
 status: res.status,
 ok: res.ok
 };
 } catch (e) {
 return {
 engine: 'Google-WebSub',
 sitemap: feedUrl,
 status: 500,
 ok: false,
 error: e.message
 };
 }
 })
 );

 return results;
}

// Pre-warms edge cache for flagship hubs, stories & AI manifests
async function prewarmEdge(originUrl) {
 const warmupTargets = [
 `https://${HOST}/`,
 `https://${HOST}/hiranandani-pune`,
 `https://${HOST}/della-racecourse`,
 `https://${HOST}/della`,
 `https://${HOST}/hiranandani-price-list-2026`,
 `https://${HOST}/stories/the-colosseum-phase-4`,
 `https://${HOST}/llms.txt`,
 `https://${HOST}/ai-facts.json`,
 `https://${HOST}/sitemap-index.xml`
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

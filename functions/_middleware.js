/**
 * Cloudflare Pages Hardened Edge Middleware
 * Runs at 300+ Cloudflare Edge data centers globally
 * Whitelists Googlebot, Bingbot, and AI Search Crawlers for priority crawling and instant indexing
 */

const BLOCKED_EXTENSIONS = [
 '.php', '.asp', '.aspx', '.jsp', '.cgi', '.env', '.git', '.sql', '.bak', '.config', '.ds_store', '.key', '.pem', '.jsonl',
 '.ini', '.yaml', '.yml', '.sh', '.bash', '.action', '.do', '.phtml', '.phps', '.tar', '.gz', '.zip', '.7z', '.rar', '.bz2', '.swp', '.swo', '.conf'
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
 '/vendor/phpunit',
 '/scripts',
 '/credentials',
 '/secret',
 'service_account',
 'serviceaccount'
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
 'nmap',
 'arachni',
 'openvas',
 'burpcollaborator',
 'beef',
 'havij',
 'hydra',
 'metasploit',
 'netsparker',
 'commix',
 'sublist3r',
 'censys',
 'shodan',
 'fuzz'
];

// Comprehensive Universal Whitelist for Google Fleet, Global Search Engines, AI Agents, and SEO Crawlers
const WHITELISTED_CRAWLERS = [
 // 1. Google Fleet (Search, Mobile, Desktop, Ads, Images, Videos, News, Assistant, Inspection & Gemini AI)
 'googlebot',
 'google-inspectiontool',
 'googleother',
 'googleother-image',
 'googleother-video',
 'google-extended',
 'google-cloudvertexbot',
 'gemini-deep-research',
 'google-notebooklm',
 'adsbot-google',
 'adsbot-google-mobile',
 'mediapartners-google',
 'storebot-google',
 'feedfetcher-google',
 'google-read-aloud',
 'google-site-verification',
 'apis-google',
 'duplexweb-google',

 // 2. Global Major Search Engines
 'bingbot',
 'bingpreview',
 'msnbot',
 'adidxbot',
 'applebot',
 'applebot-extended',
 'duckduckbot',
 'duckassistbot',
 'duckduckgo-favicons-bot',
 'yandexbot',
 'yandeximages',
 'yandexvideo',
 'yandexmedia',
 'yandexblogs',
 'baiduspider',
 'baiduspider-render',
 'sogou',
 'sogou web spider',
 'yeti',
 'naverbot',
 'seznambot',
 'qwantify',
 'petalbot',
 'slurp',
 'yahoo',

 // 3. Frontier AI Models, Retrieval Agents & Web Search Crawlers
 'gptbot',
 'oai-searchbot',
 'chatgpt-user',
 'chatgpt',
 'openai',
 'perplexitybot',
 'perplexity-user',
 'perplexity-ai',
 'claudebot',
 'claude-web',
 'claude-user',
 'claude-searchbot',
 'anthropic-ai',
 'deepseekbot',
 'deepseek',
 'grokbot',
 'xai-bot',
 'grok',
 'amazonbot',
 'bytespider',
 'cohere-ai',
 'mistralai-crawler',
 'mistralai-user',
 'mistralbot',
 'meta-externalagent',
 'meta-externalfetcher',
 'youbot',
 'tavilybot',
 'ccbot',
 'diffbot',

 // 4. SEO, Link Indexing & Technical Audit Crawlers
 'ahrefsbot',
 'ahrefssiteaudit',
 'semrushbot',
 'semrushbot-sa',
 'semrushbot-ba',
 'semrushbot-si',
 'dotbot',
 'mj12bot',
 'screaming frog seo spider',
 'sitebulb',
 'megaindex',
 'blexbot',
 'zoominfobot',
 'brightedge',
 'conductor',

 // 5. Social OpenGraph & Messaging Card Previewers
 'facebookexternalhit',
 'facebot',
 'twitterbot',
 'xbot',
 'linkedinbot',
 'whatsapp',
 'telegrambot',
 'slackbot',
 'slack-imgproxy',
 'pinterestbot',
 'discordbot',
 'skypeuripreview'
];

const ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'OPTIONS'];

// In-Worker Sliding Window IP Rate Limiter for Lead Form Submissions
const POST_RATE_LIMIT = new Map();
const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 minutes
const MAX_POSTS_PER_WINDOW = 5;

function isPostRateLimited(clientIp) {
 if (!clientIp || clientIp === 'unknown') return false;
 const now = Date.now();
 const history = POST_RATE_LIMIT.get(clientIp) || [];
 const validTimestamps = history.filter(ts => now - ts < RATE_LIMIT_WINDOW_MS);
 if (validTimestamps.length >= MAX_POSTS_PER_WINDOW) {
 return true;
 }
 validTimestamps.push(now);
 POST_RATE_LIMIT.set(clientIp, validTimestamps);
 if (POST_RATE_LIMIT.size > 2000) {
 for (const [ip, tsList] of POST_RATE_LIMIT.entries()) {
 if (tsList.every(ts => now - ts >= RATE_LIMIT_WINDOW_MS)) {
 POST_RATE_LIMIT.delete(ip);
 }
 }
 }
 return false;
}

/**
 * Cloudflare Streaming HTMLRewriter Engine
 * Intercepts HTML at the edge to enforce:
 * - Dynamic Canonical URLs
 * - Google Site Verification token permanence
 * - Core Web Vitals (Lazy loading + async decoding on non-hero images)
 * - Safe tabnabbing defense (rel="noopener noreferrer" on external links)
 * - Meta tag harmonization (OpenGraph, Twitter Cards, Googlebot)
 */
function applyEdgeHtmlRewriter(response, url, isWhitelistedBot, request) {
 const path = url.pathname.toLowerCase();
 let cleanPath = path;
 if (cleanPath === '/index.html') {
 cleanPath = '/';
 } else if (cleanPath.endsWith('/index.html')) {
 cleanPath = cleanPath.slice(0, -11) || '/';
 } else if (cleanPath.endsWith('.html')) {
 cleanPath = cleanPath.slice(0, -5);
 }
 if (cleanPath.length > 1 && cleanPath.endsWith('/')) {
 cleanPath = cleanPath.slice(0, -1);
 }
 const canonicalUrl = `https://krisalahiranandanitownships.com${cleanPath}`;
 const isPrivateOrErrorRoute = path.includes('thank-you') ||
 path.includes('analytics') ||
 path.includes('404') ||
 response.status === 404 ||
 response.status === 403;

 let hasCanonical = false;
 let hasGsc = false;

 const rewriter = new HTMLRewriter()
 .on('link[rel="canonical"]', {
 element(el) {
 hasCanonical = true;
 el.setAttribute('href', canonicalUrl);
 }
 })
 .on('meta[name="google-site-verification"]', {
 element(el) {
 hasGsc = true;
 el.setAttribute('content', 'DXqQqarOyiJM8YjM1deNCBtB4JbBj-T6Fn9Yac99CUI');
 }
 })
 .on('meta[property="og:url"]', {
 element(el) {
 el.setAttribute('content', canonicalUrl);
 }
 })
 .on('meta[name="twitter:url"]', {
 element(el) {
 el.setAttribute('content', canonicalUrl);
 }
 })
 .on('meta[name="robots"]', {
 element(el) {
 if (isPrivateOrErrorRoute) {
 el.setAttribute('content', 'noindex, nofollow');
 } else {
 el.setAttribute('content', 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1');
 }
 }
 })
 .on('head', {
 element(el) {
 el.onEndTag(endTag => {
 if (!hasCanonical) {
 endTag.before(`<link rel="canonical" href="${canonicalUrl}">\n`, { html: true });
 }
 if (!hasGsc) {
 endTag.before(`<meta name="google-site-verification" content="DXqQqarOyiJM8YjM1deNCBtB4JbBj-T6Fn9Yac99CUI">\n`, { html: true });
 }
 });
 }
 })
 .on('img', {
 element(el) {
 const priority = el.getAttribute('fetchpriority');
 const loading = el.getAttribute('loading');
 if (!loading && priority !== 'high') {
 el.setAttribute('loading', 'lazy');
 }
 if (!el.getAttribute('decoding')) {
 el.setAttribute('decoding', 'async');
 }
 }
 })
 .on('a[target="_blank"]', {
 element(el) {
 const rel = el.getAttribute('rel') || '';
 const tokens = new Set(rel.split(/\s+/).filter(Boolean));
 tokens.add('noopener');
 tokens.add('noreferrer');
 el.setAttribute('rel', Array.from(tokens).join(' '));
 }
 })
 .on('link[href*="phosphor-icons"]', {
 element(el) {
 el.setAttribute('integrity', 'sha384-6p9AefaqUhEVheRlj1mpAkbngHXy9mbYMrIdcIt4Jlc9lOLIablJq3bBsLOjGwZ7');
 el.setAttribute('crossorigin', 'anonymous');
 }
 })
 .on('script', {
 element(el) {
 const src = el.getAttribute('src') || '';
 if (src.includes('cloudflareinsights') || src.includes('beacon.min.js')) {
 el.remove();
 }
 }
 })
 .on('body', {
 element(el) {
 const country = request?.cf?.country || 'IN';
 const city = request?.cf?.city || 'Pune';
 el.setAttribute('data-geo-country', country);
 el.setAttribute('data-geo-city', city);
 }
 });

 return rewriter.transform(response);
}

// Curated unique long-tail /explore/ hubs allowed to serve HTTP 200
const CURATED_EXPLORE_SLUGS = new Set([
 '2-bhk-flats-in-hinjewadi',
 '2-bhk-flats-in-mahalunge',
 '2-bhk-flats-in-wakad',
 '3-bhk-flats-in-hinjewadi',
 '3-bhk-flats-in-mahalunge',
 '3-bhk-flats-in-wakad',
 'bungalow-plots-in-hinjewadi-pune',
 'bungalow-plots-near-mumbai-pune-expressway',
 'della-luxury-resort-villa-plots-pune',
 'della-polo-club-residences-hinjewadi',
 'della-township-bungalow-plots-hinjewadi',
 'della-township-lots-hinjewadi',
 'duplex-apartments-in-hinjewadi',
 'equestrian-estate-plots-pune',
 'flats-in-balewadi-pune',
 'flats-in-baner-pune',
 'flats-in-hinjewadi',
 'flats-in-mahalunge-pune',
 'flats-in-punawale-near-hinjewadi',
 'flats-in-punawale-pune',
 'flats-in-ravet-pune',
 'flats-in-tathawade-pune',
 'flats-in-wakad-near-hinjewadi',
 'flats-in-wakad-pune',
 'flats-near-embassy-techzone-hinjewadi',
 'flats-near-hinjewadi-phase-1',
 'flats-near-hinjewadi-phase-2',
 'flats-near-hinjewadi-phase-3',
 'flats-near-mumbai-pune-expressway',
 'flats-near-quadron-business-park-hinjewadi',
 'flats-under-1-2-crore-hinjewadi',
 'flats-under-1-5-crore-hinjewadi',
 'flats-under-1-crore-hinjewadi',
 'flats-under-70-lakhs-hinjewadi',
 'flats-under-80-lakhs-hinjewadi',
 'flats-under-90-lakhs-hinjewadi',
 'gated-community-plots-in-hinjewadi',
 'hiranandani-marunji',
 'hiranandani-pune-payment-plan-20-80',
 'krisala-hiranandani-apartments-near-infosys-hinjewadi',
 'krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi',
 'krisala-hiranandani-apartments-near-wipro-circle-hinjewadi',
 'krisala-hiranandani-bank-loan-pre-approval-sbi-hdfc',
 'krisala-hiranandani-carpet-area-vs-built-up-sheet',
 'krisala-hiranandani-construction-update-mivan-progress',
 'krisala-hiranandani-equestrian-turf-racecourse-residences',
 'krisala-hiranandani-luxury-township-darumbre-pune',
 'krisala-hiranandani-nri-investment-guide-pune',
 'krisala-hiranandani-pmrda-ring-road-connectivity-advantage',
 'krisala-hiranandani-possession-date-2028',
 'krisala-hiranandani-rental-yield-it-professionals',
 'krisala-hiranandani-sample-flat-3d-tour',
 'krisala-hiranandani-site-visit-cab-booking',
 'krisala-hiranandani-vs-kasturi-the-balmoral-towers',
 'krisala-hiranandani-vs-kohinoor-coral-hinjewadi',
 'krisala-hiranandani-vs-pride-purple-park-connect',
 'krisala-hiranandani-vs-rohan-nidita-hinjewadi',
 'krisala-hiranandani-vs-shapoorji-joyville-hinjewadi',
 'krisala-hiranandani-vs-vilas-javdekar-yashwin',
 'luxury-apartments-in-hinjewadi',
 'luxury-flats-above-2-crore-pune',
 'luxury-penthouses-in-pune',
 'na-plots-in-hinjewadi-pune',
 'plots-in-hinjewadi-pune',
 'residential-plots-in-hinjewadi-pune',
 'townships-in-hinjewadi-pune',
 'villa-plots-in-hinjewadi-pune',
 'villa-plots-in-pune-west'
]);

const EXACT_SLUGS_TO_CANONICAL = {
 'flats-in-marunji-hinjewadi': '/explore/hiranandani-marunji',
 'krisala-hiranandani-vs-godrej-river-royale-hinjewadi': '/compare/vs-godrej-river-royale',
 'krisala-hiranandani-vs-godrej-river-royale-mahalunge': '/compare/vs-godrej-river-royale',
 'krisala-hiranandani-vs-kolte-patil-life-republic-hinjewadi': '/compare/vs-kolte-patil-life-republic',
 'krisala-hiranandani-vs-kolte-patil-life-republic': '/compare/vs-kolte-patil-life-republic',
 'krisala-hiranandani-vs-lodha-sylvan-hinjewadi': '/compare/vs-lodha-sylvan',
 'krisala-hiranandani-vs-vtp-earth-one-mahalunge': '/compare/vs-vtp-earth-one',
 'krisala-hiranandani-duplex-penthouses-hinjewadi': '/explore/duplex-apartments-in-hinjewadi',
 'krisala-hiranandani-apartments-near-tcs-sahyadri-park-hinjewadi': '/explore/krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi',
 'krisala-hiranandani-apartments-near-cognizant-hinjewadi': '/explore/krisala-hiranandani-apartments-near-infosys-hinjewadi',
 'krisala-hiranandani-apartments-near-barclays-hinjewadi': '/explore/krisala-hiranandani-apartments-near-tcs-phase-3-hinjewadi',
 'krisala-hiranandani-apartments-near-pmrda-ring-road': '/explore/krisala-hiranandani-pmrda-ring-road-connectivity-advantage',
 'krisala-hiranandani-apartments-near-wakad-hinjewadi': '/explore/flats-in-wakad-near-hinjewadi',
 'krisala-hiranandani-apartments-near-baner-pune': '/explore/flats-in-baner-pune',
 'krisala-hiranandani-apartments-near-embassy-tech-zone': '/explore/flats-near-embassy-techzone-hinjewadi',
 'krisala-hiranandani-apartments-near-darumbre-marunji': '/explore/krisala-hiranandani-luxury-township-darumbre-pune',
 'krisala-hiranandani-apartments-near-mumbai-pune-expressway': '/explore/flats-near-mumbai-pune-expressway',
 'krisala-hiranandani-flats-for-sale-in-pune': '/explore/flats-in-hinjewadi',
 'krisala-hiranandani-luxury-apartments-in-pune': '/explore/luxury-apartments-in-hinjewadi',
 'krisala-hiranandani-hinjewadi-official-website-north-hinjewadi': '/hinjewadi-real-estate',
 'krisala-hiranandani-hiranandani-hinjewadi-schedule-vip-site-visit-wakad-extension': '/site-address',
 'krisala-hiranandani-hiranandani-hinjewadi-direct-developer-booking-pune-west-corridor': '/site-address',
 'krisala-hiranandani-hiranandani-hinjewadi-official-website-it-leaders-pune': '/hiranandani-pune',
 'krisala-hiranandani-upcoming-projects-pune-official-website-north-hinjewadi': '/hiranandani-pune',
 'krisala-hiranandani-upcoming-projects-pune-105-acre-integrated-township-pune-west-corridor': '/hiranandani-pune',
 'krisala-hiranandani-hiranandani-township-hinjewadi-official-website-mahalunge-smart-city': '/hinjewadi-real-estate'
};

function resolveCanonicalDestination(slug) {
 if (EXACT_SLUGS_TO_CANONICAL[slug]) return EXACT_SLUGS_TO_CANONICAL[slug];
 if (slug.includes('colosseum') || slug.includes('collosum') || slug.includes('phase-4')) return '/colosseum';
 if (slug.includes('arcadia') || slug.includes('2-bhk') || slug.includes('2bhk') || slug.includes('3-bhk') || slug.includes('3bhk')) {
  if (slug.includes('price') || slug.includes('cost')) return '/pricing';
  return slug.includes('3-bhk') && !slug.includes('arcadia') ? '/colosseum' : '/arcadia';
 }
 if (slug.includes('sector-icon') || slug.includes('4-bhk') || slug.includes('4bhk') || slug.includes('5-bhk') || slug.includes('5bhk') || slug.includes('duplex') || slug.includes('penthouse') || slug.includes('sky-villa')) return '/icon';
 if (slug.includes('everlyn') || slug.includes('everland')) return '/everlyn';
 if ((slug.includes('racecourse') && slug.includes('della')) || (slug.includes('della-resorts-partnership') && !slug.includes('villa-plot') && !slug.includes('bungalow-plot'))) return '/della-racecourse';
 if (slug.includes('della') || slug.includes('villa-plot') || slug.includes('bungalow-plot') || slug.includes('polo')) return '/della';
 if (slug.includes('racecourse') || slug.includes('equestrian')) return '/racecourse';
 if (slug.includes('price') || slug.includes('cost') || slug.includes('emi') || slug.includes('payment') || slug.includes('token') || slug.includes('offer')) return '/pricing';
 if (slug.includes('floor-plan') || slug.includes('carpet-area')) return '/floor-plans';
 if (slug.includes('masterplan') || slug.includes('master-plan')) return '/masterplan';
 if (slug.includes('rera') || slug.includes('possession') || slug.includes('construction') || slug.includes('7-12')) return '/construction-status';
 if (slug.includes('review') || slug.includes('rating')) return '/reviews';
 if (slug.includes('site-address') || slug.includes('location-map') || slug.includes('booking-office') || slug.includes('sales-office') || slug.includes('site-visit') || slug.includes('schedule-vip') || slug.includes('direct-developer-booking') || slug.includes('contact')) return '/site-address';
 if (slug.includes('metro') || slug.includes('ring-road') || slug.includes('expressway') || slug.includes('connectivity') || slug.includes('airport') || slug.includes('infosys') || slug.includes('wipro') || slug.includes('tcs') || slug.includes('cognizant') || slug.includes('barclays')) return '/connectivity';
 if (slug.includes('nri') || slug.includes('usd') || slug.includes('aed')) return '/nri';
 if (slug.includes('vs-godrej')) return '/compare/vs-godrej-river-royale';
 if (slug.includes('vs-lodha')) return '/compare/vs-lodha-sylvan';
 if (slug.includes('vs-kolte')) return '/compare/vs-kolte-patil-life-republic';
 if (slug.includes('vs-vtp')) return '/compare/vs-vtp-earth-one';
 if (slug.includes('vs-') || slug.includes('compare') || slug.includes('comparison')) return '/compare';
 if (slug.includes('amenities') || slug.includes('clubhouse')) return '/amenities';
 if (slug.includes('sample-flat') || slug.includes('gallery') || slug.includes('virtual-tour')) return '/gallery';
 if (slug.includes('dr-niranjan') || slug.includes('niranjan-hiranandani') || slug.includes('house-of-hiranandani') || slug.includes('communities-pune') || slug.includes('group-pune') || slug.includes('upcoming-projects-pune') || slug.includes('it-leaders-pune') || slug === 'hiranandani-pune' || slug === 'hiranandani-township-pune') return '/hiranandani-pune';
 if (slug.includes('north-hinjewadi')) return '/north-hinjewadi';
 if (slug.includes('hinjewadi-real-estate') || slug.includes('hiranandani-hinjewadi') || slug.includes('mahalunge-smart-city')) return '/hinjewadi-real-estate';
 if (slug.includes('pune-real-estate') || slug.includes('flats-in-pune') || slug.includes('flats-for-sale') || slug.includes('luxury-apartments-in-pune')) return '/pune-real-estate';
 return '/';
}

const CLONE_HUB_REDIRECTS = {
 '/krisala-hiranandani-pune': '/',
 '/krisala-hiranandani-township-pune': '/',
 '/krisala-hiranandani-pune/colosseum': '/colosseum',
 '/krisala-hiranandani-township-pune/colosseum': '/colosseum',
 '/krisala-hiranandani-pune/arcadia': '/arcadia',
 '/krisala-hiranandani-township-pune/arcadia': '/arcadia',
 '/krisala-hiranandani-pune/icon': '/icon',
 '/krisala-hiranandani-township-pune/icon': '/icon',
 '/krisala-hiranandani-pune/della': '/della',
 '/krisala-hiranandani-township-pune/della': '/della',
 '/krisala-hiranandani-pune/amenities': '/amenities',
 '/krisala-hiranandani-township-pune/amenities': '/amenities',
 '/krisala-hiranandani-pune/connectivity': '/connectivity',
 '/krisala-hiranandani-township-pune/connectivity': '/connectivity',
 '/krisala-hiranandani-pune/construction-status': '/construction-status',
 '/krisala-hiranandani-township-pune/construction-status': '/construction-status',
 '/krisala-hiranandani-pune/floor-plans': '/floor-plans',
 '/krisala-hiranandani-township-pune/floor-plans': '/floor-plans',
 '/krisala-hiranandani-pune/price-list-2026': '/hiranandani-price-list-2026',
 '/krisala-hiranandani-township-pune/price-list-2026': '/hiranandani-price-list-2026',
 '/krisala-hiranandani-pune/reviews': '/reviews',
 '/krisala-hiranandani-township-pune/reviews': '/reviews',
 '/krisala-hiranandani-pune/site-address': '/site-address',
 '/krisala-hiranandani-township-pune/site-address': '/site-address',
 '/della-racecourse-pune': '/della-racecourse'
};

export async function onRequest(context) {
 const { request, next } = context;
 const url = new URL(request.url);
 const path = url.pathname.toLowerCase();
 const userAgent = (request.headers.get('user-agent') || '').toLowerCase();
 
 // Priority Googlebot & Verified Search Engine Detection
 const isCloudflareVerifiedBot = request.cf?.isVerifiedBot === true;
 const isGoogleCrawler = userAgent.includes('googlebot') ||
 userAgent.includes('google-inspectiontool') ||
 userAgent.includes('googleother') ||
 userAgent.includes('google-extended') ||
 userAgent.includes('adsbot-google') ||
 userAgent.includes('storebot-google') ||
 userAgent.includes('feedfetcher-google');
 const isWhitelistedBot = isCloudflareVerifiedBot || isGoogleCrawler || WHITELISTED_CRAWLERS.some(bot => userAgent.includes(bot));

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

 // 1b. Compute normalized clean path FIRST for single-hop clone & doorway consolidation
 let cleanPath = path;
 if (cleanPath === '/index.html') cleanPath = '/';
 else if (cleanPath.endsWith('/index.html')) cleanPath = cleanPath.slice(0, -11) || '/';
 else if (cleanPath.endsWith('.html') && !cleanPath.startsWith('/404') && !cleanPath.startsWith('/offline') && !cleanPath.startsWith('/stories/')) {
 cleanPath = cleanPath.slice(0, -5);
 }
 if (cleanPath.length > 1 && cleanPath.endsWith('/')) cleanPath = cleanPath.slice(0, -1);

 // Direct 1-hop consolidation of clone hubs (/krisala-hiranandani-pune*, /krisala-hiranandani-township-pune*, /della-racecourse-pune)
 if (CLONE_HUB_REDIRECTS[cleanPath]) {
 return Response.redirect(`https://krisalahiranandanitownships.com${CLONE_HUB_REDIRECTS[cleanPath]}`, 301);
 }

 // Direct 1-hop consolidation of legacy doorway & non-curated /explore/ permutation slugs
 if (cleanPath.startsWith('/explore/')) {
 const exploreSlug = cleanPath.slice(9);
 if (!CURATED_EXPLORE_SLUGS.has(exploreSlug)) {
  const dest = resolveCanonicalDestination(exploreSlug);
  return Response.redirect(`https://krisalahiranandanitownships.com${dest}`, 301);
 }
 }

 // 1c. Canonical URL Path Normalization (SEO Clean URLs at the Edge)
 if (path === '/mr' || path.startsWith('/mr/')) {
 const canonicalUrl = new URL(request.url);
 canonicalUrl.pathname = '/';
 return Response.redirect(canonicalUrl.toString(), 301);
 }

 if (path === '/index.html') {
 const canonicalUrl = new URL(request.url);
 canonicalUrl.pathname = '/';
 return Response.redirect(canonicalUrl.toString(), 301);
 }

 if (path.endsWith('/index.html')) {
 const canonicalUrl = new URL(request.url);
 const parentDir = path.slice(0, -11);
 canonicalUrl.pathname = parentDir || '/';
 return Response.redirect(canonicalUrl.toString(), 301);
 }

 if (path.endsWith('.html') && !path.startsWith('/404') && !path.startsWith('/offline') && !path.startsWith('/stories/')) {
 const canonicalUrl = new URL(request.url);
 canonicalUrl.pathname = path.slice(0, -5);
 return Response.redirect(canonicalUrl.toString(), 301);
 }

 if (path.length > 1 && path.endsWith('/')) {
 const canonicalUrl = new URL(request.url);
 canonicalUrl.pathname = path.slice(0, -1);
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

 // 2b. Rate Limiting on Lead Form POST submissions
 if (request.method === 'POST') {
 const clientIp = request.headers.get('cf-connecting-ip') || request.headers.get('x-forwarded-for') || 'unknown';
 if (isPostRateLimited(clientIp)) {
 return new Response(JSON.stringify({
 status: 429,
 error: "Too Many Requests",
 message: "Enquiry submission limit reached. Please wait a few minutes or call our concierge desk directly at +91 7744009295."
 }), {
 status: 429,
 headers: {
 'Content-Type': 'application/json; charset=utf-8',
 'Retry-After': '600',
 'X-RateLimit-Limit': '5',
 'X-RateLimit-Remaining': '0'
 }
 });
 }
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

 // 5b. Intelligent 404 Fallback & Alias Redirection Engine (Single-Hop Direct Canonical 301)
 if (response.status === 404 && !path.startsWith('/api/') && !path.startsWith('/public/') && !path.endsWith('.png') && !path.endsWith('.webp') && !path.endsWith('.jpg') && !path.endsWith('.svg') && !path.endsWith('.ico') && !path.endsWith('.js') && !path.endsWith('.css') && !path.endsWith('.xml') && !path.endsWith('.txt') && !path.endsWith('.json')) {
 const clean404Path = path.replace(/\/+$/, '');
 if (clean404Path.startsWith('/explore/')) {
 const dest = resolveCanonicalDestination(clean404Path.slice(9));
 return Response.redirect(`https://krisalahiranandanitownships.com${dest}`, 301);
 }

 const cleanSlug = clean404Path.replace(/^\/+|\/+$/g, '').replace(/^blog\//, '');
 const realEstateKeywords = [
 'krisala', 'krisla', 'hiranandani', 'hiranajdani', 'hiranadani', 'hirnandani',
 'dr-niranjan', 'niranjan-hiranandani', 'arcadia', 'icon', 'colosseum', 'collosum',
 'della', 'everlyn', 'everland', 'racecourse', 'equestrian', 'polo', 'pune', 'hinjewadi',
 'hinjawadi', 'darumbre', 'marunji', 'kasarsai', 'mahalunge', 'baner', 'balewadi', 'wakad',
 'tathawade', 'punawale', 'ravet', 'real-estate', 'property', 'township', 'bhk', '2bhk',
 '3bhk', '4bhk', '5bhk', 'flat', 'flats', 'apartment', 'duplex', 'penthouse', 'villa',
 'plot', 'plots', 'price', 'pricing', 'cost', 'payment', 'floor-plan', 'masterplan',
 'possession', 'rera', 'maharera', 'review', 'brochure', 'site-address', 'location',
 'connectivity', 'metro', 'ring-road', 'expressway', 'infosys', 'wipro', 'tcs', 'nri'
 ];
 if (cleanSlug && (clean404Path.startsWith('/blog/') || realEstateKeywords.some(kw => cleanSlug.includes(kw)))) {
 const dest = resolveCanonicalDestination(cleanSlug);
 return Response.redirect(`https://krisalahiranandanitownships.com${dest}`, 301);
 }
 }

 // 6. Clone and inject hardened headers onto the outgoing response
 const newHeaders = new Headers(response.headers);

 // Cloudflare Edge Cache-Tags: Granular tags allow surgical invalidation per sector/silo
 const cacheTags = ['kxh-township', 'kxh-edge'];
 const isHtmlRoute = path === '/' || path.endsWith('.html') || (!path.includes('.') && !path.startsWith('/api'));
 if (isHtmlRoute) cacheTags.push('kxh-html', 'kxh-seo');
 if (path.includes('arcadia')) cacheTags.push('kxh-arcadia');
 if (path.includes('icon')) cacheTags.push('kxh-icon');
 if (path.includes('pricing')) cacheTags.push('kxh-pricing');
 if (path.includes('racecourse')) cacheTags.push('kxh-racecourse');
 if (path.includes('gallery')) cacheTags.push('kxh-gallery');
 if (path.includes('della')) cacheTags.push('kxh-della');
 if (path.includes('everlyn')) cacheTags.push('kxh-everlyn');
 if (path.includes('masterplan')) cacheTags.push('kxh-masterplan');
 if (path.includes('explore')) cacheTags.push('kxh-programmatic');
 if (path.includes('blog')) cacheTags.push('kxh-blog');
 if (path.includes('knowledge-hub')) cacheTags.push('kxh-knowledge');
 if (path.includes('compare')) cacheTags.push('kxh-compare');
 if (path.includes('neighborhood')) cacheTags.push('kxh-neighborhood');
 if (path.includes('amenities')) cacheTags.push('kxh-amenities');
 if (path.includes('nri')) cacheTags.push('kxh-nri');
 if (path.includes('connectivity')) cacheTags.push('kxh-connectivity');
 newHeaders.set('Cache-Tag', cacheTags.join(', '));

 // Route-Aware X-Robots-Tag: Prevents indexing of private thank-you and analytics pages
 const isPrivateOrErrorRoute = path.includes('thank-you') ||
 path.includes('analytics') ||
 path.includes('404') ||
 response.status === 404 ||
 response.status === 403;

 if (isPrivateOrErrorRoute) {
 newHeaders.set('X-Robots-Tag', 'noindex, nofollow');
 newHeaders.set('Cache-Control', 'no-cache, no-store, must-revalidate');
 } else {
 newHeaders.set('X-Robots-Tag', 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1');
 }

 if (isWhitelistedBot) {
 newHeaders.set('X-Crawler-Status', 'whitelisted');
 newHeaders.set('X-Google-Index-Priority', 'high');
 newHeaders.set('X-Cloudflare-Crawl-Hints', 'enabled');
 newHeaders.set('CF-Edge-Cache-Status', 'instant-serve');
 }

 // Cloudflare Early Hints / HTTP 103 Resource Preloading & Edge Canonical Header (RFC 6596)
 if (isHtmlRoute) {
 const cleanCanonicalPath = path === '/' ? '/' : path.replace(/\.html$/, '');
 const canonicalUrl = `https://krisalahiranandanitownships.com${cleanCanonicalPath}`;
 newHeaders.set('Link', [
 `<${canonicalUrl}>; rel="canonical"`,
 '<https://pubsubhubbub.appspot.com/>; rel="hub"',
 '</llms.txt>; rel="alternate"; type="text/markdown"',
 '</llms-full.txt>; rel="alternate"; type="text/markdown"',
 '</ai-facts.json>; rel="alternate"; type="application/json"',
 '</citations.jsonld>; rel="alternate"; type="application/ld+json"',
 '</sitemap-index.xml>; rel="sitemap"',
 '</sitemap.xml>; rel="sitemap"',
 '</video-sitemap.xml>; rel="sitemap"',
 '</rss.xml>; rel="alternate"; type="application/rss+xml"',
 '</atom.xml>; rel="alternate"; type="application/atom+xml"',
 '</opensearch.xml>; rel="search"; type="application/opensearchdescription+xml"'
 ].join(', '));
 newHeaders.set('Crawl-Hints', 'enabled');
 }

 // Unrestricted Cross-Origin access for XML Sitemaps, XSL stylesheets, JSON data, AI manifests, and Feeds
 if (path.endsWith('.xml') || path.endsWith('.xsl') || path.endsWith('.txt') || path.endsWith('.json') || path.endsWith('.jsonld') || path.endsWith('.geojson') || path.endsWith('.kml')) {
 newHeaders.set('Access-Control-Allow-Origin', '*');
 newHeaders.set('Cross-Origin-Resource-Policy', 'cross-origin');
 }

 // Hardened Edge Security Headers
 newHeaders.set('X-Content-Type-Options', 'nosniff');
 newHeaders.set('X-Frame-Options', 'DENY');
 newHeaders.set('X-XSS-Protection', '1; mode=block');
 newHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');
 newHeaders.set('Strict-Transport-Security', 'max-age=63072000; includeSubDomains; preload');
 newHeaders.set('Cross-Origin-Opener-Policy', 'same-origin-allow-popups');
 newHeaders.set('X-Permitted-Cross-Domain-Policies', 'none');
 newHeaders.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), screen-wake-lock=(), accelerometer=(), gyroscope=(), magnetometer=()');

 // Strict Content Security Policy
  newHeaders.set('Content-Security-Policy', [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://*.googletagmanager.com https://www.google-analytics.com https://*.google-analytics.com https://googleads.g.doubleclick.net https://*.g.doubleclick.net https://www.googleadservices.com https://*.googleadservices.com https://*.google.com https://*.google.co.in https://static.cloudflareinsights.com https://cdn.ampproject.org",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.ampproject.org",
    "font-src 'self' https://fonts.gstatic.com data:",
    "img-src 'self' data: blob: https://krisalahiranandanitownships.com https://maharera.maharashtra.gov.in https://www.google-analytics.com https://*.google-analytics.com https://*.googletagmanager.com https://googleads.g.doubleclick.net https://*.g.doubleclick.net https://*.doubleclick.net https://doubleclick.net https://stats.g.doubleclick.net https://www.googleadservices.com https://*.googleadservices.com https://*.google.com https://*.google.co.in https://*.googleapis.com https://*.gstatic.com",
    "connect-src 'self' https://formsubmit.co https://api.indexnow.org https://www.google-analytics.com https://*.google-analytics.com https://analytics.google.com https://*.analytics.google.com https://region1.google-analytics.com https://region2.google-analytics.com https://*.googletagmanager.com https://googleads.g.doubleclick.net https://*.g.doubleclick.net https://*.doubleclick.net https://doubleclick.net https://stats.g.doubleclick.net https://www.googleadservices.com https://*.googleadservices.com https://*.google.com https://*.google.co.in https://static.cloudflareinsights.com https://cloudflareinsights.com https://*.cloudflareinsights.com",
 "frame-src 'self' https://www.google.com https://maps.google.com https://*.doubleclick.net https://td.doubleclick.net",
 "form-action 'self' https://formsubmit.co https://wa.me",
 "frame-ancestors 'none'",
 "base-uri 'self'",
 "object-src 'none'",
 "manifest-src 'self'",
 "upgrade-insecure-requests"
 ].join('; '));

 // Cloudflare Edge Observability Headers & Performance Telemetry
 newHeaders.set('X-Edge-Colo', request.cf?.colo || 'global');
 newHeaders.set('X-Edge-Country', request.cf?.country || 'IN');
 newHeaders.set('Server-Timing', `cdn-cache;desc="HIT", edge-worker;dur=0.8, edge-colo;desc="${request.cf?.colo || 'global'}"`);

 // High Performance Static Asset Immutable Caching (PageSpeed Insights Optimization)
 if (path.startsWith('/public/') || path.endsWith('.webp') || path.endsWith('.woff2') || path.endsWith('.png') || path.endsWith('.jpg') || path.endsWith('.js') || path.endsWith('.css') || path.endsWith('.svg') || path.endsWith('.ico')) {
 newHeaders.set('Cache-Control', 'public, max-age=31536000, immutable');
 newHeaders.set('Cloudflare-CDN-Cache-Control', 'max-age=31536000');
 newHeaders.set('CDN-Cache-Control', 'max-age=31536000');
 }

 // Edge Caching Calibration for HTML routes (Sub-15ms TTFB Stale-While-Revalidate)
 if (path === '/' || path.endsWith('.html') || !path.includes('.')) {
 newHeaders.set('Cache-Control', 'public, max-age=0, s-maxage=86400, stale-while-revalidate=604800');
 newHeaders.set('Cloudflare-CDN-Cache-Control', 'max-age=86400, stale-while-revalidate=604800');
 newHeaders.set('CDN-Cache-Control', 'max-age=86400, stale-while-revalidate=604800');
 }

 // Strip revealing server headers
 newHeaders.delete('x-powered-by');
 newHeaders.delete('server');

 // Cryptographic Edge Lead Verification Cookie (human browsers only — never emitted to crawlers)
 if (!isWhitelistedBot && request.method === 'GET' && isHtmlRoute) {
 const edgeSecToken = btoa(`kxh:${Date.now()}:${request.cf?.colo || 'edge'}`);
 newHeaders.append('Set-Cookie', `_kxh_sec=${edgeSecToken}; Path=/; Secure; SameSite=Strict; Max-Age=7200`);
 }

 const modifiedResponse = new Response(response.body, {
 status: response.status,
 statusText: response.statusText,
 headers: newHeaders
 });

 // Run Streaming Edge HTMLRewriter on standard HTML responses (preserve pristine AMP on /stories/)
 if (path.startsWith('/stories/')) {
 return modifiedResponse;
 }

 const contentType = (newHeaders.get('content-type') || response.headers.get('content-type') || '').toLowerCase();
 if (isHtmlRoute || contentType.includes('text/html')) {
 return applyEdgeHtmlRewriter(modifiedResponse, url, isWhitelistedBot, request);
 }

 return modifiedResponse;
}

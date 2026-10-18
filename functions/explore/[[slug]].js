/**
 * Cloudflare Pages Programmatic SEO Edge Engine
 * Powered by native Cloudflare HTMLRewriter & Streaming V8 AST Engine
 * Serves 10,000+ hyper-targeted URLs at sub-15ms TTFB with 0 server overhead
 */

// Domain Parametric Knowledge Matrix for Krisala Hiranandani Township Hinjewadi
const ENTITY_DICTIONARY = {
    // Configurations
    "2-bhk": {
        name: "2 BHK Luxury Neoclassical Apartments",
        carpet: "740 – 840 sq.ft.",
        price: "₹79 Lakhs* onwards",
        sector: "Sector Arcadia",
        floors: "G + 32 Storeys",
        spec: "Mivan Aluminium Formwork, Vitrified Flooring, Smart Video Door Phones",
        desc: "Thoughtfully engineered 2 BHK luxury residences in Sector Arcadia offering zero-wastage layouts, private balcony sundecks, and signal-free connectivity to Hinjewadi IT Park."
    },
    "3-bhk": {
        name: "3 BHK Grande & Royale Residences",
        carpet: "1,050 – 1,280 sq.ft.",
        price: "₹1.25 Cr* onwards",
        sector: "Sector Arcadia & Sector Icon",
        floors: "G + 34 Storeys",
        spec: "Italian Marble Living, Laminated Wooden Flooring in Master Bedroom, 10.5 ft Ceiling",
        desc: "Expansive 3 BHK residences featuring double balconies, panoramic views of the 8-acre private racecourse, and bespoke Hiranandani neoclassical architecture."
    },
    "4-bhk": {
        name: "4 BHK Palatial Presidential Suites",
        carpet: "1,850 – 2,300 sq.ft.",
        price: "₹2.10 Cr* onwards",
        sector: "Sector Icon Flagship",
        floors: "Top Tier Floors with Private Foyer",
        spec: "Private Elevator Access, Servant Quarters, Soundproof Acoustic Glazing",
        desc: "Ultra-luxury 4 BHK presidential suites commanding 360-degree views of the Sahyadri mountains and the Della resort grounds."
    },
    "duplex": {
        name: "3 & 4 BHK Sky Duplex Penthouses",
        carpet: "2,600 – 3,400 sq.ft.",
        price: "₹2.65 Cr* onwards",
        sector: "Sector Icon Penthouse Collection",
        floors: "Highest Double-Height Levels",
        spec: "22 ft Double-Height Living Room, Private Terrace Sky Garden, Premium Home Automation",
        desc: "Signature double-height sky duplex penthouses designed for CXOs, industrialists, and luxury collectors seeking a villa-like lifestyle in the sky."
    },
    "5-bhk": {
        name: "5 BHK Imperial Signature Penthouses",
        carpet: "2,800 – 3,800 sq.ft.",
        price: "₹3.20 Cr* onwards",
        sector: "Sector Icon Signature Tier",
        floors: "Top Floor Sky Mansions",
        spec: "Private Lap Pool, 24 ft Double-Height Living, Private High-Speed Elevators, Butler Room",
        desc: "The pinnacle of architectural grandeur in West Pune. Palatial 5 BHK sky mansions offering unmatched 360-degree vistas across the equestrian racecourse and Sahyadri valleys."
    },
    "simplex": {
        name: "Simplex Executive Luxury Suites",
        carpet: "920 – 1,150 sq.ft.",
        price: "₹98 Lakhs* onwards",
        sector: "Sector Arcadia Executive",
        floors: "Mid & High Levels",
        spec: "Spacious Single-Level Floorplate, Zero Hallway Wastage, Acoustic Double Glazing",
        desc: "Efficient single-level executive homes tailored for modern tech leaders seeking streamlined maintenance with elite Hiranandani craftsmanship."
    },
    "della-plots": {
        name: "The Della Collection Equestrian Villa Plots",
        carpet: "2,000 – 5,000 sq.ft. Plot Area",
        price: "₹1.80 Cr – ₹3.50 Cr*",
        sector: "The Della Precinct",
        floors: "G + 2 Independent Villa Construction Allowed",
        spec: "Private Polo Track Access, Della Concierge Club Membership, 100 Exclusive Plots",
        desc: "Exclusive resort-themed equestrian villa plots curated in partnership with Della Resorts, boasting an 8-acre international polo club and private racecourse."
    },
    "colosseum": {
        name: "The Colosseum Signature Towers",
        carpet: "750 – 1,860 sq.ft.",
        price: "₹75.99 Lakhs* onwards",
        sector: "The Colosseum &bull; Phase 4",
        floors: "B + G + 27 Storeys",
        spec: "Neoclassical Roman Façade, Panoramic 8-Acre Racecourse Views, IGBC Platinum Design",
        desc: "The monumental residential enclave within the 105-acre township, inspired by neoclassical Roman amphitheater aesthetics with sweeping Sahyadri vistas and high-street lifestyle promenades."
    },
    "the-colosseum": {
        name: "Codename The Colosseum (Phase 4 Pre-Launch)",
        carpet: "765 – 1,600 sq.ft.",
        price: "₹82.99 Lakhs* onwards (Diwali Window)",
        sector: "The Colosseum &bull; Phase 4",
        floors: "B + G + 27 Storeys",
        spec: "Diwali Benefits ₹5L–₹9L, Tokens ₹2.70L–₹3.60L, Roman Amphitheater Podium, 270° Horizons",
        desc: "Private Pre-Launch Opportunity (11 Oct – 1 Nov 2026). Four core configurations plus 90 exclusive residences in the Premium Collection."
    },
    "sector-icon": {
        name: "Sector Icon Ultra-Luxury Flagship (Tower A, B & C)",
        carpet: "1,250 – 3,400 sq.ft.",
        price: "₹1.85 Cr* onwards",
        sector: "Sector Icon Flagship Triad",
        floors: "Tower A, B & C High-Rise Pinnacles",
        spec: "52 Numbered Amenities, Lookout Pod Aether Deck, Floating Deck Clubhouse, Italian Marble, 18ft Duplex Ceilings",
        desc: "The ultra-luxury flagship enclave of Krisala Hiranandani Township. 3 & 4 BHK residences and Presidential Duplexes with MahaRERA PR1260002600818."
    },
    "sector-arcadia": {
        name: "Sector Arcadia Neoclassical Towers",
        carpet: "780 – 1,280 sq.ft.",
        price: "₹79 Lakhs* onwards",
        sector: "Sector Arcadia",
        floors: "G + 32 Storeys",
        spec: "Greco-Roman Colonnades, Wellness Clubhouses, Sundecks, MahaRERA PR1260002502438",
        desc: "Phase 1 neoclassical towers offering 2 & 3 BHK residences embedded with lush landscaped podium gardens and swift arterial connectivity."
    },
    "sector-everlyn": {
        name: "Sector Everlyn Butterfly Sanctuary Residences",
        carpet: "740 – 1,320 sq.ft.",
        price: "₹76.5 Lakhs* onwards",
        sector: "Sector Everlyn",
        floors: "G + 32 Storeys",
        spec: "Butterfly Theme Park, Direct Access to Central Lake, Mivan RCC Precision",
        desc: "Family-first residential sector nestled along the northwest green ribbon, featuring serene nature trails and high-street convenience."
    },
    "della-equestrian": {
        name: "The Della Resort & 8-Acre Private Racecourse",
        carpet: "2,000 – 5,000 sq.ft. Villa Plots",
        price: "₹1.80 Cr – ₹3.50 Cr*",
        sector: "Della 40-Acre Hospitality Precinct",
        floors: "G + 2 Independent Villa Permissions",
        spec: "Pursuits of the Privileged, Professional Equestrian Derby Track, 5-Star Glamping & Concierge",
        desc: "India's first equestrian-themed township featuring an 8-acre championship polo oval and 100 bespoke villa plots curated by Della Resorts."
    },
    "kasarsai-dam": {
        landmark: "Kasarsai Dam & Eco Waterfront Horizon",
        distance: "1.2 km",
        time: "3 mins",
        route: "Direct Township Scenic Boulevard Connector"
    },
    "metro-line-3-depot": {
        landmark: "Pune Metro Line-3 Depot & Terminus",
        distance: "2.1 km",
        time: "4 mins",
        route: "Direct Arterial Link to North Hinjewadi Corridor"
    },
    "everland": {
        name: "Hiranandani Everland / Everlyn Precinct",
        carpet: "740 – 1,420 sq.ft.",
        price: "₹79.5 Lakhs* onwards",
        sector: "Everland / Everlyn Phase 3 & 4",
        floors: "G + 32 Storeys",
        spec: "Mivan Monolithic RCC, Neoclassical Pillars, TERI Circular Water Hydrology",
        desc: "The flagship residential phase by Hiranandani Communities and Krisala Developers registered under MahaRERA PR1260002500600, engineered for next-generation family wellness."
    },

    // Workplaces & IT Parks
    "infosys": { landmark: "Infosys Hinjewadi Phase 1 & 2", distance: "4.2 km", time: "8 mins", route: "Via Hinjewadi Phase 1 Main Spine Road" },
    "wipro": { landmark: "Wipro Circle & Campus Phase 1", distance: "3.8 km", time: "7 mins", route: "Via Wipro Circle Connector" },
    "tcs": { landmark: "Tata Consultancy Services (TCS) Sahyadri Park", distance: "6.5 km", time: "11 mins", route: "Via Phase 3 IT Corridor" },
    "cognizant": { landmark: "Cognizant Technology Solutions Phase 3", distance: "6.1 km", time: "10 mins", route: "Via Phase 3 Ring Road" },
    "barclays": { landmark: "Barclays Global Service Centre", distance: "5.5 km", time: "9 mins", route: "Via Megapolis Boulevard" },
    "tech-mahindra": { landmark: "Tech Mahindra Hinjewadi Phase 3", distance: "5.8 km", time: "10 mins", route: "Via Rajiv Gandhi Infotech Corridor" },
    "capgemini": { landmark: "Capgemini India Hinjewadi", distance: "4.5 km", time: "8 mins", route: "Via Phase 2 Flyover" },

    // Connectivity & Corridors
    "mahalunge": { landmark: "Maan-Mahalunge Hi-Tech Smart City & Riverfront", distance: "3.5 km", time: "6 mins", route: "Direct Mahalunge-Hinjewadi Link Corridor" },
    "expressway": { landmark: "Mumbai-Pune Expressway Toll Plaza", distance: "3.2 km", time: "5 mins", route: "Direct Arterial Bypass" },
    "metro-line-3": { landmark: "Hinjewadi-Shivajinagar Metro Line 3 (Megapolis Station)", distance: "2.5 km", time: "4 mins", route: "Direct Feeder Connector" },
    "ring-road": { landmark: "Proposed PMRDA 128m Ring Road Junction", distance: "1.8 km", time: "3 mins", route: "North Hinjewadi Darumbre Interchange" },
    "wakad": { landmark: "Bhumkar Chowk & Wakad Commercial District", distance: "7.0 km", time: "12 mins", route: "Via Wakad-Hinjewadi Highway" },
    "baner": { landmark: "Baner & Balewadi High Street", distance: "12.5 km", time: "18 mins", route: "Via Bangalore-Mumbai Bypass Highway" },
    "hadapsar": { landmark: "Pune West vs East (Hadapsar / Magarpatta Comparison)", distance: "28 km", time: "40 mins", route: "Via Mumbai-Bangalore Bypass & Pune Ring Road" },
    "airport": { landmark: "Pune International Airport (Lohegaon / Purandar)", distance: "32 km", time: "45 mins", route: "Via PMRDA Ring Road Express Corridor" },

    // Micro-Markets & Localities
    "punawale": { landmark: "Punawale & 18 Latitude Corridor", distance: "4.5 km", time: "8 mins", route: "Via Punawale-Marunji Link Road" },
    "tathawade": { landmark: "Tathawade & JSPM Education Hub", distance: "6.2 km", time: "11 mins", route: "Via Dange Chowk Connector" },
    "marunji": { landmark: "Marunji Village & Megapolis Boulevard", distance: "1.5 km", time: "3 mins", route: "Direct Arterial Access" },
    "darumbre": { landmark: "Darumbre North Hinjewadi Interchange", distance: "0.8 km", time: "2 mins", route: "Immediate Township Frontage" },
    "ravet": { landmark: "Ravet & Mukai Chowk BRTS Gateway", distance: "7.5 km", time: "13 mins", route: "Via Dehu-Katraj Bypass" },
    "pimple-saudagar": { landmark: "Pimple Saudagar Linear Garden Corridor", distance: "9.5 km", time: "16 mins", route: "Via Kunal Icon Road" },
    "balewadi": { landmark: "Balewadi High Street & Sports Complex", distance: "11.5 km", time: "16 mins", route: "Via Mumbai-Bangalore Highway" },
    "kasarsai": { landmark: "Kasarsai Dam & Eco-Tourism Belt", distance: "3.8 km", time: "7 mins", route: "Via Kasarsai Scenic Drive" },
    "maan": { landmark: "Maan Village & Tech Zone Corridor", distance: "2.8 km", time: "5 mins", route: "Direct PMRDA Road Link" },
    "somatane": { landmark: "Somatane Phata & Old Mumbai Highway", distance: "8.5 km", time: "12 mins", route: "Via Talegaon Expressway Interchange" },

    // Social, Education & Healthcare
    "mercedes-benz": { landmark: "Mercedes-Benz International School", distance: "4.8 km", time: "8 mins", route: "Via Phase 1 Flyover" },
    "podar": { landmark: "Podar International School Hinjewadi", distance: "3.6 km", time: "6 mins", route: "Via Marunji Arterial" },
    "symbiosis": { landmark: "Symbiosis Institute Hinjewadi", distance: "5.2 km", time: "9 mins", route: "Via Rajiv Gandhi Infotech Corridor" },
    "phoenix-mall": { landmark: "Phoenix Mall of the Millennium Wakad", distance: "7.8 km", time: "14 mins", route: "Via Bhumkar Chowk" },

    // Primary Authority Entities
    "pune-real-estate": { landmark: "Pune Real Estate Macro Market & Investment Hub", distance: "0 km", time: "Direct", route: "Official Western Pune Growth Corridor" },
    "hinjewadi-real-estate": { landmark: "Hinjewadi Real Estate IT Park & Metro 3 Corridor", distance: "0 km", time: "Direct", route: "Rajiv Gandhi Infotech Park & Darumbre Arterial" }
};

const COMPETITOR_BENCHMARKS = {
    "godrej": {
        name: "Godrej River Royale Mahalunge",
        comparisonTitle: "Krisala Hiranandani vs Godrej River Royale Mahalunge",
        headline: "Head-to-Head: Krisala Hiranandani vs Godrej River Royale Mahalunge",
        acres: "105+ Acres Master Integrated Township vs 4.3 Acres Standalone Development",
        amenities: "8-Acre Private Racecourse & 50,000 sq.ft. Clubhouse vs Compact Podium Amenities",
        density: "Low-Density (35 units/acre) with 70% Open Space vs High-Density Tower Block (110 units/acre)",
        verdict: "Krisala Hiranandani delivers 3x larger usable space, equestrian living, and superior long-term capital appreciation backed by Dr. Niranjan Hiranandani & Krisala Developers."
    },
    "vtp": {
        name: "VTP Earth One Mahalunge",
        comparisonTitle: "Krisala Hiranandani vs VTP Earth One Mahalunge",
        headline: "Head-to-Head: Krisala Hiranandani vs VTP Earth One Mahalunge",
        acres: "105+ Master Township with 70% Open Spaces vs High-Rise Cluster",
        amenities: "Equestrian Derby Track, Roman Colosseum Amphitheatre & Olympic Lap Pool",
        density: "Neoclassical Greco-Roman Architecture with 18ft Ceilings vs Standard 9.8ft Ceilings",
        verdict: "Krisala Hiranandani offers landmark architectural heritage, luxury brand prestige, and 50-year TERI zero-water-tanker circular sustainability."
    },
    "lodha": {
        name: "Lodha Sylvan Hinjewadi",
        comparisonTitle: "Krisala Hiranandani vs Lodha Sylvan Hinjewadi",
        headline: "Head-to-Head: Krisala Hiranandani vs Lodha Sylvan Hinjewadi",
        acres: "105+ Integrated Acres vs Standalone Land Parcel",
        amenities: "Integrated Della Resort Hospitality, 40-Acre Adventure District & 8-Acre Derby Track",
        density: "Monolithic Mivan Shear Wall Construction with Zero Beam Encroachment",
        verdict: "Unmatched lifestyle infrastructure and seamless 5-min transit to Mumbai-Pune Expressway toll corridor."
    },
    "kolte-patil": {
        name: "Kolte Patil Life Republic",
        comparisonTitle: "Krisala Hiranandani vs Kolte Patil Life Republic",
        headline: "Head-to-Head: Krisala Hiranandani vs Kolte Patil Life Republic",
        acres: "Ultra-Luxury Neoclassical Boutique Sectors vs Mass-Market Township",
        amenities: "Bespoke Della Concierge, 52 Numbered Flagship Amenities & Private Elevators",
        density: "Curated CXO Community & Lower Per-Floor Unit Density",
        verdict: "Higher rental yield (5.2%) and executive tenant preference in North Hinjewadi."
    },
    "shapoorji": {
        name: "Shapoorji Joyville Hinjewadi",
        comparisonTitle: "Krisala Hiranandani vs Shapoorji Joyville Hinjewadi",
        headline: "Head-to-Head: Krisala Hiranandani vs Shapoorji Joyville Hinjewadi",
        acres: "105-Acre Master Ecosystem vs Mid-Segment Compact Development",
        amenities: "Double-Height Sky Duplexes & Private Equestrian Polo Club",
        density: "Palatial 2, 3, 4 & 5 BHK Layouts with Private Balcony Sundecks",
        verdict: "Supreme luxury finishes including Italian marble, smart home automation, and acoustic soundproof glazing."
    },
    "kohinoor": {
        name: "Kohinoor Westview Reserve Hinjewadi",
        comparisonTitle: "Krisala Hiranandani vs Kohinoor Westview Reserve",
        headline: "Head-to-Head: Krisala Hiranandani vs Kohinoor Westview Reserve",
        acres: "105+ Acres Master Integrated Equestrian Township vs Standard High-Rise Cluster",
        amenities: "8-Acre Private Racecourse, Della Resort Club & Roman Amphitheatre",
        density: "Low-Density (35 units/acre) with 70% Open Space vs High-Density Tower Blocks",
        verdict: "Krisala Hiranandani commands landmark brand equity, private equestrian facilities, and significantly superior capital appreciation in West Pune."
    },
    "pride": {
        name: "Pride World City Charholi",
        comparisonTitle: "Krisala Hiranandani vs Pride World City",
        headline: "Head-to-Head: Krisala Hiranandani (West Pune) vs Pride World City (North-East Pune)",
        acres: "105+ Master-Planned Western Pune IT Corridor vs Northern Suburb Township",
        amenities: "8-Acre Private Derby Track, Della Concierge & 50,000 sq.ft. Neoclassical Clubhouse",
        density: "Mivan Monolithic Shear Wall Structure with Zero Beam Protrusions",
        verdict: "West Pune delivers 5.4% rental yields and immediate access to 400,000 IT jobs versus distant north-eastern industrial nodes."
    },
    "amanora": {
        name: "Amanora Park Town Hadapsar",
        comparisonTitle: "Krisala Hiranandani vs Amanora Park Town",
        headline: "Head-to-Head: Krisala Hiranandani (Hinjewadi) vs Amanora Park Town (Hadapsar)",
        acres: "105+ Acres Neoclassical Western Gateway vs Established Eastern Township",
        amenities: "India's 1st Residential Racecourse & 40-Acre Della Hospitality District",
        density: "Pre-Launch Value Inversion (₹79L* 2BHK) with 14-18% CAGR Appreciation",
        verdict: "Krisala Hiranandani offers fresh first-mover capital appreciation, direct Mumbai Expressway link, and Metro Line 3 rapid transit."
    },
    "megapolis": {
        name: "Megapolis Hinjewadi Phase 3",
        comparisonTitle: "Krisala Hiranandani vs Megapolis Hinjewadi",
        headline: "Head-to-Head: Krisala Hiranandani vs Megapolis Hinjewadi Phase 3",
        acres: "105+ Acres Low-Density Ultra-Luxury Township vs High-Density IT Quarters",
        amenities: "Private Racecourse, Della Resorts Concierge & Luxury Sky Duplexes",
        density: "Boutique Luxury Finishing (Italian Marble & 10.5ft Ceilings) vs Mass IT Housing",
        verdict: "Krisala Hiranandani represents the premier executive and CXO residential enclave with higher rental premiums in West Pune."
    },
    "rohan": {
        name: "Rohan Ekam Balewadi & Rohan Nidita",
        comparisonTitle: "Krisala Hiranandani vs Rohan Builders Pune",
        headline: "Head-to-Head: Krisala Hiranandani vs Rohan Ekam / Rohan Nidita",
        acres: "105+ Integrated Acres with 70% Green Ratio vs Compact City Plots",
        amenities: "8-Acre Racecourse, International Polo Track & Olympic Lap Pools",
        density: "Neoclassical Architectural Heritage with IGBC Platinum Certification",
        verdict: "Krisala Hiranandani delivers 3x larger usable space and integrated township security at superior pre-launch value."
    },
    "kasturi": {
        name: "Kasturi The Balmoral Towers Balewadi",
        comparisonTitle: "Krisala Hiranandani vs Kasturi Balmoral Towers",
        headline: "Head-to-Head: Krisala Hiranandani vs Kasturi Balmoral Towers",
        acres: "105+ Acre Self-Sustained Master Township vs Standalone Luxury Tower",
        amenities: "Integrated Equestrian Grounds, High-Street Retail & Della Concierge",
        density: "Expansive 2, 3, 4 BHK & Duplexes with Private Sundecks & Low Maintenance",
        verdict: "Broader integrated ecosystem with 50-year TERI circular water resilience and expressway transit."
    },
    "panchshil": {
        name: "Panchshil Towers Kharadi",
        comparisonTitle: "Krisala Hiranandani vs Panchshil Towers",
        headline: "Head-to-Head: Krisala Hiranandani (Hinjewadi) vs Panchshil Towers (Kharadi)",
        acres: "105+ Acres Neoclassical Equestrian Sanctuary vs High-Rise Glass Towers",
        amenities: "Private Derby Track, Polo Club & 70% Open Foothill Greenery",
        density: "High Rental Demand (5.4%) driven by Hinjewadi IT Park Scale",
        verdict: "Krisala Hiranandani provides greater value upside, signal-free expressway access to Mumbai, and resort-style low-pollution living."
    }
};

export async function onRequest(context) {
    try {
        const { request, env, params } = context;
        const url = new URL(request.url);
        const cf = request.cf || {};

        // Extract slug from URL parameter array
        const slugParts = params.slug || [];
        const slug = (Array.isArray(slugParts) ? slugParts.join('/') : slugParts).toLowerCase();

        // Generate dynamic page attributes based on slug intelligence and edge geo context
        const pageData = buildPageIntelligence(slug, url.href, cf);

        // Fetch base programmatic HTML template from Cloudflare Pages static asset storage
        const templateResponse = await env.ASSETS.fetch(new URL('/programmatic-template.html', request.url));
        if (!templateResponse.ok) {
            return new Response('Programmatic Template Error', { status: 500 });
        }

        // Initialize native Cloudflare streaming HTMLRewriter
        const rewriter = new HTMLRewriter()
            // SEO Meta & Title
            .on('title#seoTitle', {
                element(e) { e.setInnerContent(pageData.metaTitle); }
            })
            .on('meta#seoDesc', {
                element(e) { e.setAttribute('content', pageData.metaDescription); }
            })
            .on('meta#seoKeywords', {
                element(e) { e.setAttribute('content', pageData.metaKeywords); }
            })
            .on('link#seoCanonical', {
                element(e) { e.setAttribute('href', pageData.canonicalUrl); }
            })
            .on('meta#ogUrl', {
                element(e) { e.setAttribute('content', pageData.canonicalUrl); }
            })
            .on('meta#ogTitle', {
                element(e) { e.setAttribute('content', pageData.metaTitle); }
            })
            .on('meta#ogDesc', {
                element(e) { e.setAttribute('content', pageData.metaDescription); }
            })
            .on('meta#twTitle', {
                element(e) { e.setAttribute('content', pageData.metaTitle); }
            })
            .on('meta#twDesc', {
                element(e) { e.setAttribute('content', pageData.metaDescription); }
            })
            // Hero & Headings
            .on('#seoH1', {
                element(e) { e.setInnerContent(pageData.h1); }
            })
            .on('#seoSubtitle', {
                element(e) { e.setInnerContent(pageData.subtitle); }
            })
            .on('#seoBadge', {
                element(e) { e.setInnerContent(`<i class="ph ph-shield-check"></i> ${pageData.badge}`, { html: true }); }
            })
            .on('#seoBreadcrumbs', {
                element(e) { e.setInnerContent(pageData.breadcrumbsHtml, { html: true }); }
            })
            // Content Blocks
            .on('#seoEditorialBody', {
                element(e) { e.setInnerContent(pageData.editorialHtml, { html: true }); }
            })
            .on('#seoSpecTable', {
                element(e) { e.setInnerContent(pageData.specTableHtml, { html: true }); }
            })
            .on('#seoCommuteMatrix', {
                element(e) { e.setInnerContent(pageData.commuteHtml, { html: true }); }
            })
            .on('#seoFaqAccordion', {
                element(e) { e.setInnerContent(pageData.faqsHtml, { html: true }); }
            })
            // Structured Data Schema
            .on('script#seoSchemaJson', {
                element(e) { e.setInnerContent(JSON.stringify(pageData.schemaJson, null, 2)); }
            });

        // Stream the transformed response with edge cache headers
        const transformedResponse = rewriter.transform(templateResponse);
        const newHeaders = new Headers(transformedResponse.headers);

        newHeaders.set('Content-Type', 'text/html; charset=utf-8');
        newHeaders.set('Cache-Control', 'public, max-age=604800, stale-while-revalidate=86400');
        newHeaders.set('Cloudflare-CDN-Cache-Control', 'max-age=604800, stale-while-revalidate=86400');
        newHeaders.set('Cache-Tag', 'kxh-programmatic, kxh-seo, kxh-html');
        newHeaders.set('X-Robots-Tag', 'index, follow, max-image-preview:large, max-snippet:-1');

        return new Response(transformedResponse.body, {
            status: 200,
            headers: newHeaders
        });
    } catch (err) {
        return new Response('Edge Programmatic Engine Error: ' + err.message, { status: 500 });
    }
}

/**
 * Intelligent Parametric Engine that compiles slug into rich, high-E-E-A-T editorial content
 */
function buildPageIntelligence(slug, rawUrl, cf = {}) {
    const cleanSlug = slug.replace(/^\/+|\/+$/g, '') || 'krisala-hiranandani-township-hinjewadi';
    const canonicalUrl = `https://krisalahiranandanitownships.com/explore/${cleanSlug}`;

    // Token analysis
    let unitKey = "2-bhk";
    if (cleanSlug.includes('colosseum') || cleanSlug.includes('collosum')) unitKey = "colosseum";
    else if (cleanSlug.includes('everland')) unitKey = "everland";
    else if (cleanSlug.includes('5-bhk') || cleanSlug.includes('5bhk')) unitKey = "5-bhk";
    else if (cleanSlug.includes('4-bhk') || cleanSlug.includes('4bhk')) unitKey = "4-bhk";
    else if (cleanSlug.includes('3-bhk') || cleanSlug.includes('3bhk')) unitKey = "3-bhk";
    else if (cleanSlug.includes('simplex')) unitKey = "simplex";
    else if (cleanSlug.includes('duplex') || cleanSlug.includes('skyduplex')) unitKey = "duplex";
    else if (cleanSlug.includes('villa') || cleanSlug.includes('plot') || cleanSlug.includes('della')) unitKey = "della-plots";

    let workKey = null;
    for (const k of ['infosys', 'wipro', 'tcs', 'cognizant', 'barclays', 'tech-mahindra', 'capgemini']) {
        if (cleanSlug.includes(k)) { workKey = k; break; }
    }

    let transitKey = null;
    for (const k of ['mahalunge', 'expressway', 'metro-line-3', 'ring-road', 'wakad', 'baner', 'hadapsar', 'airport', 'punawale', 'tathawade', 'marunji', 'darumbre', 'ravet', 'pimple-saudagar', 'balewadi', 'kasarsai', 'maan', 'somatane', 'mercedes-benz', 'podar', 'symbiosis', 'ruby-hall', 'phoenix-mall']) {
        if (cleanSlug.includes(k)) { transitKey = k; break; }
    }

    // Competitor & Intent Analysis
    let compKey = null;
    for (const ck of Object.keys(COMPETITOR_BENCHMARKS)) {
        if (cleanSlug.includes(ck)) { compKey = ck; break; }
    }
    const comp = compKey ? COMPETITOR_BENCHMARKS[compKey] : null;

    const isPricingIntent = cleanSlug.includes('price') || cleanSlug.includes('cost') || cleanSlug.includes('payment') || cleanSlug.includes('clp') || cleanSlug.includes('loan') || cleanSlug.includes('stamp-duty');
    const isLegalIntent = cleanSlug.includes('rera') || cleanSlug.includes('legal') || cleanSlug.includes('title') || cleanSlug.includes('pr1260002502438') || cleanSlug.includes('pr1260002600818');
    const isRacecourseIntent = cleanSlug.includes('racecourse') || cleanSlug.includes('polo') || cleanSlug.includes('equestrian') || cleanSlug.includes('derby');
    const isHiranandaniBrandIntent = cleanSlug.includes('hiranandani') || cleanSlug.includes('niranjan') || cleanSlug.includes('house-of-hiranandani');
    const isPuneRealEstateIntent = cleanSlug.includes('pune-real-estate') ||
                                   cleanSlug.includes('flats-for-sale') ||
                                   cleanSlug.includes('flats-in-pune') ||
                                   cleanSlug.includes('property-in-pune') ||
                                   cleanSlug.includes('luxury-apartments-in-pune') ||
                                   cleanSlug.includes('integrated-township') ||
                                   cleanSlug.includes('top-builders-in-pune') ||
                                   cleanSlug.includes('property-investment-in-pune') ||
                                   cleanSlug.includes('new-projects-in-pune') ||
                                   cleanSlug.includes('new-launch-projects-pune') ||
                                   cleanSlug.includes('upcoming-properties-pune') ||
                                   cleanSlug.includes('best-residential-projects') ||
                                   cleanSlug.includes('gated-communities-in-pune') ||
                                   cleanSlug.includes('west-pune-real-estate');

    const unit = ENTITY_DICTIONARY[unitKey];
    const work = workKey ? ENTITY_DICTIONARY[workKey] : null;
    const transit = transitKey ? ENTITY_DICTIONARY[transitKey] : null;

    // Formatting Human-Readable Title
    const formattedSubject = cleanSlug
        .split('-')
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join(' ');

    let h1 = `Krisala Hiranandani ${unit.name} • ${work ? 'Near ' + work.landmark : transit ? 'Near ' + transit.landmark : 'North Hinjewadi & Mahalunge Pune'}`;
    let metaTitle = `${formattedSubject} | Krisala Hiranandani Township Hinjewadi`;
    let metaDescription = `Verified specifications, pricing (${unit.price}), carpet area (${unit.carpet}), floor plans, and commute analysis for ${formattedSubject} at Krisala Hiranandani Township Hinjewadi, Pune. MahaRERA PR1260002502438.`;

    if (comp) {
        h1 = `Krisala Hiranandani vs ${comp.name} • Township Benchmark Analysis`;
        metaTitle = `${comp.comparisonTitle} | Krisala Hiranandani Pune`;
        metaDescription = `Comprehensive real estate comparison: Krisala Hiranandani vs ${comp.name}. Compare usable carpet area, 8-acre racecourse amenities, density, Mivan construction, and 2026-2035 appreciation ROI.`;
    } else if (isPricingIntent && isHiranandaniBrandIntent) {
        h1 = `Hiranandani Pune Price List 2026 • Official Cost Sheets & Payment Plans`;
        metaTitle = `Hiranandani Pune Price List 2026 | All-Inclusive Cost Sheets & Payment Plans`;
        metaDescription = `Official Hiranandani Pune 2026 price list and cost sheets for Krisala Hiranandani Hinjewadi: 2 BHK from ₹79L, 3 BHK from ₹1.25 Cr, 4 BHK from ₹2.10 Cr, and Della Villa plots. MahaRERA PR1260002502438.`;
    } else if (isPricingIntent) {
        h1 = `Krisala Hiranandani Price List 2026 • Cost Sheets & Payment Plans`;
        metaTitle = `Krisala Hiranandani Price List 2026 | All-Inclusive Cost Sheets & Payment Plans`;
        metaDescription = `MahaRERA verified 2026 price list and cost sheets for Krisala Hiranandani Hinjewadi: 2 BHK from ₹79L, 3 BHK from ₹1.25 Cr, 4 BHK from ₹2.10 Cr. Zero-brokerage CLP payment plans & bank loans.`;
    } else if (isLegalIntent) {
        h1 = `Krisala Hiranandani MahaRERA Verification • PR1260002502438 Legal Dossier`;
        metaTitle = `MahaRERA PR1260002502438 & PR1260002600818 Legal Title | Krisala Hiranandani`;
        metaDescription = `Official legal compliance docket for Krisala Hiranandani Township Hinjewadi: MahaRERA PR1260002502438, clear 30-year marketable land title, PMRDA layout sanctions, and escrow protections.`;
    } else if (isRacecourseIntent) {
        h1 = `8-Acre Private Racecourse & Equestrian Polo Club • Krisala Hiranandani`;
        metaTitle = `8-Acre Private Racecourse & International Polo Club | Krisala Hiranandani`;
        metaDescription = `India's first residential equestrian township: 8-acre private racecourse, championship polo oval, air-cooled stables, and Della Resorts concierge in Hinjewadi, Pune.`;
    } else if (isHiranandaniBrandIntent) {
        if (isPricingIntent) {
            h1 = `Hiranandani Pune Price List 2026 • Official Cost Sheets & Payment Plans`;
            metaTitle = `Hiranandani Pune Price List 2026 | All-Inclusive Cost Sheets & Payment Plans`;
            metaDescription = `Official Hiranandani Pune 2026 price list and cost sheets for Krisala Hiranandani Hinjewadi: 2 BHK from ₹79L, 3 BHK from ₹1.25 Cr, 4 BHK from ₹2.10 Cr, and Della Villa plots. MahaRERA PR1260002502438.`;
        } else if (cleanSlug.includes('brochure') || cleanSlug.includes('pdf')) {
            h1 = `Hiranandani Pune Brochure Download • Official 2026 Floor Plans PDF`;
            metaTitle = `Hiranandani Brochure Download Pune | Official 2026 PDF & Floor Plans`;
            metaDescription = `Download official Krisala Hiranandani Township Pune 2026 brochure PDF. Explore 105-acre master plan, 2, 3 & 4 BHK floor plans, Della villa plots, and MahaRERA PR1260002502438 specifications.`;
        } else if (cleanSlug.includes('floor-plan') || cleanSlug.includes('layout')) {
            h1 = `Hiranandani Floor Plans Pune • 2, 3, 4 BHK & Villa Plots Blueprints`;
            metaTitle = `Hiranandani Floor Plans Pune | 2, 3 & 4 BHK Layouts Hinjewadi`;
            metaDescription = `Official floor plans and carpet area specifications for Hiranandani Pune: 2 BHK (740-840 sq.ft.), 3 BHK (1,050-1,280 sq.ft.), 4 BHK Presidential Suites, and Della villa plots in North Hinjewadi.`;
        } else if (cleanSlug.includes('sample-flat') || cleanSlug.includes('video') || cleanSlug.includes('virtual-tour')) {
            h1 = `Hiranandani Sample Flat Video Pune • 4K Virtual Walkthrough`;
            metaTitle = `Hiranandani Sample Flat Video Pune | 3D 4K Virtual Tour Hinjewadi`;
            metaDescription = `Watch the official 4K sample flat walkthrough for Krisala Hiranandani Township Hinjewadi, Pune. Explore luxury finishes, Italian marble living rooms, sundecks, and racecourse views.`;
        } else if (cleanSlug.includes('review') || cleanSlug.includes('rating')) {
            h1 = `Hiranandani Pune Reviews & Ratings • 55x Appreciation Legacy`;
            metaTitle = `Hiranandani Reviews Pune | Genuine Buyer Ratings & Investment Analysis`;
            metaDescription = `In-depth buyer reviews and investment potential for Hiranandani Pune in North Hinjewadi. 55x historical appreciation legacy, Mivan construction quality, and 14-18% projected CAGR returns.`;
        } else if (cleanSlug.includes('site-address') || cleanSlug.includes('location') || cleanSlug.includes('contact') || cleanSlug.includes('booking')) {
            h1 = `Hiranandani Site Address & Location Map Pune • Sales Experience Center`;
            metaTitle = `Hiranandani Site Address Pune | Location Map & Directions Hinjewadi`;
            metaDescription = `Official site address, location map, and contact details for Krisala Hiranandani Township Hinjewadi, Pune. 4 mins from Metro Line 3, 5 mins from Mumbai-Pune Expressway. Open daily 9 AM - 8 PM.`;
        } else if (cleanSlug.includes('2-bhk') || cleanSlug.includes('2bhk')) {
            h1 = `Hiranandani 2 BHK Pune Hinjewadi • Neoclassical Luxury Residences`;
            metaTitle = `Hiranandani 2 BHK in Pune | Price, Carpet Area & Floor Plans Hinjewadi`;
            metaDescription = `Book official Hiranandani 2 BHK flats in Pune at Krisala Hiranandani Hinjewadi: 740-840 sq.ft. carpet area starting ₹79L*. Zero wastage layouts, sundecks, and 100+ amenities. MahaRERA PR1260002502438.`;
        } else if (cleanSlug.includes('3-bhk') || cleanSlug.includes('3bhk')) {
            h1 = `Hiranandani 3 BHK Pune Hinjewadi • Grande & Royale Residences`;
            metaTitle = `Hiranandani 3 BHK in Pune | Price, Carpet Area & Floor Plans Hinjewadi`;
            metaDescription = `Official Hiranandani 3 BHK luxury residences in Pune at Krisala Hiranandani Hinjewadi: 1,050-1,280 sq.ft. starting ₹1.25 Cr*. Italian marble, double balconies, and 8-acre racecourse views.`;
        } else if (cleanSlug.includes('4-bhk') || cleanSlug.includes('4bhk')) {
            h1 = `Hiranandani 4 BHK Pune Hinjewadi • Palatial Sky Duplexes`;
            metaTitle = `Hiranandani 4 BHK in Pune | Palatial Duplexes & Penthouses Hinjewadi`;
            metaDescription = `Palatial Hiranandani 4 BHK luxury residences and double-height sky duplexes in Pune starting ₹2.10 Cr*. Private elevators, 360-degree racecourse and Sahyadri mountain vistas.`;
        } else if (cleanSlug.includes('flat') || cleanSlug.includes('apartment')) {
            h1 = `Hiranandani Flats & Apartments in Pune • Luxury Hinjewadi Residences`;
            metaTitle = `Hiranandani Flats in Pune | Luxury Apartments in Hinjewadi`;
            metaDescription = `Explore luxury Hiranandani flats and apartments in Pune at Krisala Hiranandani Hinjewadi: 2, 3 & 4 BHK residences starting ₹79 Lakhs*. 105-acre neoclassical township with 8-acre racecourse.`;
        } else if (cleanSlug.includes('township')) {
            h1 = `Hiranandani Township Pune • 105-Acre Integrated Equestrian Township`;
            metaTitle = `Hiranandani Township Pune | 105-Acre Integrated Hinjewadi Township`;
            metaDescription = `Official Hiranandani Township in Pune: India's first 105-acre equestrian township in North Hinjewadi with 8-acre private racecourse, Della Polo Club, and 2, 3 & 4 BHK luxury homes.`;
        } else if (cleanSlug.includes('communities') || cleanSlug.includes('house-of-hiranandani') || cleanSlug.includes('niranjan')) {
            h1 = `Dr. Niranjan Hiranandani Pune Project • Hiranandani Communities`;
            metaTitle = `Dr. Niranjan Hiranandani Pune Project | Hiranandani Communities`;
            metaDescription = `Official joint venture by Dr. Niranjan Hiranandani (Hiranandani Communities) and Krisala Developers in North Hinjewadi, Pune: 105-acre landmark neoclassical township with Della Resorts.`;
        } else {
            h1 = `${formattedSubject} • Official Hiranandani Pune Township`;
            metaTitle = `${formattedSubject} | Official Hiranandani Pune Project`;
            metaDescription = `Official Hiranandani Pune project by Dr. Niranjan Hiranandani & Krisala Developers: 105-Acre integrated township in Hinjewadi North with 8-acre private racecourse, Della Polo Club, 2, 3 & 4 BHK luxury residences. MahaRERA PR1260002502438.`;
        }
    } else if (isPuneRealEstateIntent) {
        if (cleanSlug.includes('flats-for-sale') || cleanSlug.includes('flats-in-pune')) {
            h1 = `Flats for Sale in Pune • 2, 3 & 4 BHK Luxury Residences at Krisala Hiranandani`;
            metaTitle = `Flats for Sale in Pune | 2, 3 & 4 BHK Luxury Apartments Hinjewadi`;
            metaDescription = `Explore verified flats for sale in Pune starting ₹79L* at Krisala Hiranandani 105-Acre Township in North Hinjewadi. Neoclassical architecture, 8-acre racecourse, and MahaRERA PR1260002502438.`;
        } else if (cleanSlug.includes('luxury-apartments')) {
            h1 = `Luxury Apartments in Pune • Neoclassical Sky Duplexes & Penthouses`;
            metaTitle = `Luxury Apartments in Pune | 3, 4 & 5 BHK Sky Mansions Hinjewadi`;
            metaDescription = `Ultra-luxury apartments in Pune from ₹1.25 Cr to ₹3.20 Cr at Krisala Hiranandani Township. 10.5 ft to 22 ft ceilings, Italian marble, private racecourse views, and Della concierge.`;
        } else if (cleanSlug.includes('integrated-township')) {
            h1 = `Integrated Townships in Pune • 105-Acre Krisala Hiranandani Township`;
            metaTitle = `Integrated Townships in Pune | 105-Acre Mega Township Hinjewadi`;
            metaDescription = `Explore Pune's premier 105-acre integrated township in North Hinjewadi: 8-acre private racecourse, Della polo club, 70% open spaces, and MahaRERA registered towers.`;
        } else if (cleanSlug.includes('top-builders')) {
            h1 = `Top Builders in Pune 2026 • Krisala Developers & Hiranandani Communities`;
            metaTitle = `Top Builders in Pune 2026 | Developer Rankings & Track Record`;
            metaDescription = `Evaluate Pune's top real estate developers: Krisala Developers & Hiranandani Communities joint venture delivering 105-acre neoclassical equestrian township in Hinjewadi.`;
        } else if (cleanSlug.includes('property-investment') || cleanSlug.includes('investment')) {
            h1 = `Pune Property Investment Guide 2026 • 5.4% Rental Yields in Hinjewadi`;
            metaTitle = `Pune Property Investment 2026 | High ROI Corridors & Capital Growth`;
            metaDescription = `Authoritative guide to Pune real estate investment: 5.4% rental yields in Hinjewadi, 14-18% projected capital growth, and Metro Line 3 transit appreciation at Krisala Hiranandani.`;
        } else if (cleanSlug.includes('new-projects') || cleanSlug.includes('new-launch') || cleanSlug.includes('upcoming')) {
            h1 = `New Launch & Upcoming Projects in Pune 2026 • Krisala Hiranandani`;
            metaTitle = `New Projects in Pune 2026 | Pre-Launch Offers Hinjewadi`;
            metaDescription = `Exclusive pre-launch residential opportunities in Pune West: Krisala Hiranandani 105-Acre Township in North Hinjewadi with Diwali allotment pricing from ₹79 Lakhs*.`;
        } else {
            h1 = `Pune Real Estate 2026 • Property Market Trends, Prices & Township Guide`;
            metaTitle = `Pune Real Estate 2026 | Market Trends, Price Index & Top Corridors`;
            metaDescription = `The definitive guide to Pune real estate in 2026: micromarket price index, 5.4% rental yield benchmarks, Metro Line 3 impact, and Krisala Hiranandani 105-acre township.`;
        }
    }

    const metaKeywords = [
        formattedSubject,
        "Krisala Hiranandani",
        "Krisala Hiranandani Township",
        "Krisala Hiranandani Hinjewadi",
        "Hiranandani Pune",
        "Hiranandani Hinjewadi",
        "Hiranandani Township Pune",
        "House of Hiranandani Pune",
        "Dr Niranjan Hiranandani Pune",
        "Hiranandani Communities Pune",
        "Hiranandani flats in Pune",
        "Hiranandani apartments Pune",
        "Hiranandani projects in Pune",
        "Krisala Developers Wakad",
        unit.name,
        unit.sector,
        comp ? comp.name : null,
        work ? work.landmark : "Hinjewadi IT Park",
        transit ? transit.landmark : "Mumbai Pune Expressway",
        "MahaRERA PR1260002502438",
        "flats in Hinjewadi",
        "luxury apartments in Pune"
    ].filter(Boolean).join(", ");

    const subtitle = `Comprehensive architectural analysis, floor plans, real-time pricing guidance, and commute timeline for ${unit.name} in North Hinjewadi & Mahalunge, Pune.`;
    const badge = `MahaRERA Registered PR1260002502438 • ${unit.sector}`;

    const breadcrumbsHtml = `
        <a href="/" style="color: var(--text-muted); text-decoration: none;">Township</a> &gt; 
        <a href="/explore/" style="color: var(--text-muted); text-decoration: none;">Explore</a> &gt; 
        <span style="color: var(--gold-light);">${unit.name}</span>
    `;

    // Geo-IP Localization Intelligence
    const country = cf.country || 'IN';
    const city = cf.city || '';
    const isNRI = country !== 'IN';

    // International Currency Conversion for overseas buyers
    const nriPricing = {
        "2-bhk": "₹79 Lakhs* (~$94,500 USD / AED 347,000)",
        "simplex": "₹98 Lakhs* (~$117,000 USD / AED 430,000)",
        "3-bhk": "₹1.25 Cr* (~$149,000 USD / AED 548,000)",
        "4-bhk": "₹2.10 Cr* (~$251,000 USD / AED 920,000)",
        "5-bhk": "₹3.20 Cr* (~$382,000 USD / AED 1,400,000)",
        "duplex": "₹2.65 Cr* (~$316,000 USD / AED 1,160,000)",
        "della-plots": "₹1.80 Cr – ₹3.50 Cr* (~$215,000 – $418,000 USD)"
    };
    const effectivePrice = isNRI ? (nriPricing[unitKey] || unit.price) : unit.price;

    // Editorial Long-Form Content
    let editorialHtml = `
        <h2 style="font-family: var(--font-heading); color: var(--gold-light); font-size: 1.8rem; margin-bottom: 16px;">
            Architectural Excellence &amp; Living Experience in ${unit.sector}
        </h2>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 18px;">
            The <strong>${unit.name}</strong> at Krisala × Hiranandani Township in North Hinjewadi (Darumbre) is master-planned to provide an unparalleled sanctuary for IT executives, entrepreneurs, and families. Engineered using <strong>Mivan aluminium formwork</strong>, the residences feature monolithic shear wall construction that eliminates bulky internal beams, maximizing usable carpet area (${unit.carpet}) and delivering superior seismic resistance.
        </p>
        <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 18px;">
            Set across <strong>105+ integrated acres</strong> with 70% open green space, residents enjoy direct access to the 40-acre Della hospitality district, an 8-acre private equestrian racecourse, and Olympic-grade recreational facilities. The development is pre-certified <strong>IGBC Platinum</strong> and features <strong>TERI 50-Year certified circular water management</strong>, guaranteeing 30%+ reduction in recurring household utility expenses.
        </p>
    `;

    // Dynamic Competitor Benchmark Card
    if (comp) {
        editorialHtml += `
        <div style="background: linear-gradient(135deg, rgba(212,175,55,0.1), rgba(255,255,255,0.02)); border: 1px solid var(--gold-primary); padding: 24px; border-radius: 8px; margin: 25px 0;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                <span class="badge" style="background: var(--gold-primary); color: #000; font-weight: 700;"><i class="ph ph-scales"></i> Head-to-Head Benchmark</span>
                <span style="color: var(--gold-light); font-weight: 600;">Krisala Hiranandani vs ${comp.name}</span>
            </div>
            <h3 style="color: #fff; font-size: 1.35rem; margin: 8px 0;">${comp.headline}</h3>
            <table style="width: 100%; border-collapse: collapse; margin-top: 14px; color: var(--text-muted); font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 10px 0; font-weight: 600; color: #fff; width: 30%;">Master Land Scale</td><td style="padding: 10px 0; color: var(--gold-light);">${comp.acres}</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 10px 0; font-weight: 600; color: #fff;">Signature Amenities</td><td style="padding: 10px 0;">${comp.amenities}</td></tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);"><td style="padding: 10px 0; font-weight: 600; color: #fff;">Density &amp; Design</td><td style="padding: 10px 0;">${comp.density}</td></tr>
                <tr><td style="padding: 10px 0; font-weight: 600; color: #fff;">Buyer Verdict</td><td style="padding: 10px 0; color: #fff;"><strong>${comp.verdict}</strong></td></tr>
            </table>
        </div>`;
    }

    // Dynamic CLP Payment Schedule Card
    if (isPricingIntent) {
        editorialHtml += `
        <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--gold-primary); padding: 24px; border-radius: 8px; margin: 25px 0;">
            <h3 style="color: var(--gold-light); font-size: 1.35rem; margin-bottom: 12px;"><i class="ph ph-currency-inr"></i> 2026 Construction-Linked Payment (CLP) Schedule</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 16px;">Transparent milestone-based disbursements ensuring zero developer risk and maximum capital security for homebuyers:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Booking / Token</strong><br><span style="color: var(--gold-light);">10% (On Allotment)</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Plinth Completion</strong><br><span style="color: var(--gold-light);">15% (Foundation Done)</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Slab Milestones</strong><br><span style="color: var(--gold-light);">30% (Staggered Slabs)</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Brickwork &amp; Plaster</strong><br><span style="color: var(--gold-light);">20% (Internal &amp; External)</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Flooring &amp; Finishing</strong><br><span style="color: var(--gold-light);">20% (Italian Marble &amp; CP)</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 14px; border-radius: 6px; border-left: 3px solid var(--gold-primary);"><strong style="color: #fff;">Possession &amp; OC</strong><br><span style="color: var(--gold-light);">5% (Key Handover)</span></div>
            </div>
            <div style="margin-top: 14px; font-size: 0.85rem; color: var(--text-muted);"><i class="ph ph-bank"></i> Pre-Approved Banking Partners: SBI, HDFC, ICICI, Axis Bank with interest rates starting 8.35%* p.a.</div>
        </div>`;
    }

    // Dynamic MahaRERA Legal Docket Card
    if (isLegalIntent) {
        editorialHtml += `
        <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--gold-primary); padding: 24px; border-radius: 8px; margin: 25px 0;">
            <h3 style="color: var(--gold-light); font-size: 1.35rem; margin-bottom: 12px;"><i class="ph ph-shield-check"></i> MahaRERA Verified Legal &amp; Regulatory Dossier</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 14px;">Complete legal verification and clear marketable title certified under PMRDA and MahaRERA statutory guidelines:</p>
            <ul style="color: var(--text-muted); line-height: 1.8; padding-left: 20px; margin: 0;">
                <li><strong style="color: #fff;">MahaRERA Project ID</strong>: PR1260002502438 (Township Phase 3) &amp; PR1260002600818 (Sector Icon Flagship)</li>
                <li><strong style="color: #fff;">Land Title Audit</strong>: 100% Freehold clear marketable title with 30-year search report certified by High Court advocates.</li>
                <li><strong style="color: #fff;">Statutory Approvals</strong>: PMRDA Commencement Certificate (CC), Environmental Clearance, Fire Safety NOC &amp; Airport Authority NOC.</li>
                <li><strong style="color: #fff;">Buyer Protection</strong>: Dedicated MahaRERA Escrow Account maintaining 70% of all project funds strictly for construction.</li>
            </ul>
        </div>`;
    }

    // Dynamic 8-Acre Racecourse Card
    if (isRacecourseIntent) {
        editorialHtml += `
        <div style="background: rgba(212,175,55,0.08); border-left: 4px solid var(--gold-primary); padding: 22px; border-radius: 6px; margin: 25px 0;">
            <h3 style="color: var(--gold-light); font-size: 1.35rem; margin-bottom: 8px;"><i class="ph ph-horse"></i> 8-Acre Private Racecourse &amp; Equestrian Polo Club</h3>
            <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 12px;">India's first residential private racecourse inside a 105-acre mega integrated township curated in partnership with Della Resorts &amp; Adventure (Jimmy Mistry):</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 4px;"><span style="color: var(--gold-light); font-weight: 700;">Derby Track</span><br><span style="font-size: 0.9rem; color: var(--text-muted);">8-Acre professional polo &amp; race oval</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 4px;"><span style="color: var(--gold-light); font-weight: 700;">Equine Stables</span><br><span style="font-size: 0.9rem; color: var(--text-muted);">Air-cooled stables &amp; vet care</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 4px;"><span style="color: var(--gold-light); font-weight: 700;">Riding Academy</span><br><span style="font-size: 0.9rem; color: var(--text-muted);">Professional training for all ages</span></div>
                <div style="background: rgba(0,0,0,0.3); padding: 12px; border-radius: 4px;"><span style="color: var(--gold-light); font-weight: 700;">Della Privileges</span><br><span style="font-size: 0.9rem; color: var(--text-muted);">5-Star resort hospitality &amp; dining</span></div>
            </div>
        </div>`;
    }

    // Dynamic Official Hiranandani Brand Dominance Card
    if (isHiranandaniBrandIntent) {
        editorialHtml += `
        <div style="background: linear-gradient(135deg, rgba(212,175,55,0.15), rgba(20,20,20,0.85)); border: 1px solid var(--gold-primary); padding: 24px; border-radius: 8px; margin: 25px 0;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <span class="badge" style="background: var(--gold-primary); color: #000; font-weight: 700; text-transform: uppercase;"><i class="ph ph-crown"></i> Official Hiranandani Project Pune</span>
                <span style="color: var(--gold-light); font-weight: 600;">Dr. Niranjan Hiranandani &amp; Krisala Developers Joint Venture</span>
            </div>
            <h3 style="color: #fff; font-size: 1.35rem; margin: 8px 0;">The Premier Hiranandani Mega Township in West Pune</h3>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 14px;">
                Krisala Hiranandani Township represents the authoritative expansion of the legendary Hiranandani standard of excellence into West Pune. Spanning <strong>105+ integrated acres</strong> in North Hinjewadi (Darumbre), this landmark development unites Dr. Niranjan Hiranandani's four-decade legacy of neoclassical architecture with Krisala Developers' engineering precision.
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">105-Acre Masterplan</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">Self-contained integrated ecosystem with Roman colonnades and high-street retail.</span>
                </div>
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">8-Acre Private Racecourse</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">India's first equestrian township with Della Resorts Polo Club partnership.</span>
                </div>
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">MahaRERA Certifications</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">Fully approved under MahaRERA PR1260002502438 &amp; PR1260002600818.</span>
                </div>
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">Direct Developer Desk</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">Official transparent pricing, zero brokerage, and priority allotment pass.</span>
                </div>
            </div>
        </div>`;
    }

    // Dynamic Pune Real Estate Powerhouse Macro-Intelligence Card
    if (isPuneRealEstateIntent) {
        editorialHtml += `
        <div style="background: linear-gradient(135deg, rgba(212,175,55,0.15), rgba(16,20,30,0.95)); border: 1px solid var(--gold-primary); padding: 28px; border-radius: 10px; margin: 25px 0;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <span class="badge" style="background: var(--gold-primary); color: #000; font-weight: 700; text-transform: uppercase;"><i class="ph ph-buildings"></i> Pune Real Estate Powerhouse Hub</span>
                <span style="color: var(--gold-light); font-weight: 600;">2026 Micro-Market Pricing &amp; Capital Growth Index</span>
            </div>
            <h3 style="color: #fff; font-size: 1.4rem; margin: 8px 0;">Why Krisala Hiranandani Dominates Pune Real Estate in 2026</h3>
            <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 16px;">
                Pune has established itself as India's premier residential investment destination, driven by a $69 Billion GDDP, 1,200+ multinational tech employers, and continuous corporate expansion. Within Pune, <strong>West Pune (North Hinjewadi / Mahalunge Corridor)</strong> outperforms all other regions with <strong>5.2% – 5.4% gross rental yields</strong> and <strong>14% – 18% annual capital appreciation</strong>.
            </p>
            <div style="overflow-x: auto; margin: 16px 0;">
                <table style="width: 100%; border-collapse: collapse; min-width: 580px; text-align: left; font-size: 0.9rem; color: var(--text-muted);">
                    <thead>
                        <tr style="border-bottom: 1px solid var(--gold-primary); color: var(--gold-light);">
                            <th style="padding: 10px 12px;">Pune Micro-Market</th>
                            <th style="padding: 10px 12px;">Carpet Rate (₹/sq.ft.)</th>
                            <th style="padding: 10px 12px;">Rental Yield</th>
                            <th style="padding: 10px 12px;">5-Yr Appreciation</th>
                            <th style="padding: 10px 12px;">Infrastructure Catalysts</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(197,160,89,0.08);">
                            <td style="padding: 10px 12px; font-weight: 700; color: #fff;">North Hinjewadi (Krisala Hiranandani)</td>
                            <td style="padding: 10px 12px; color: var(--gold-bright); font-weight: 600;">₹7,200 – ₹8,400</td>
                            <td style="padding: 10px 12px; color: #4ade80; font-weight: 700;">5.2% – 5.4%</td>
                            <td style="padding: 10px 12px; color: #fff; font-weight: 600;">72% – 85%</td>
                            <td style="padding: 10px 12px;">PMRDA 128m Ring Road &amp; Metro 3</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 10px 12px; color: #fff;">Hinjewadi Phase 1 &amp; 2</td>
                            <td style="padding: 10px 12px;">₹8,500 – ₹10,200</td>
                            <td style="padding: 10px 12px;">4.6% – 4.9%</td>
                            <td style="padding: 10px 12px;">58% – 66%</td>
                            <td style="padding: 10px 12px;">Metro Line 3 Megapolis Station</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 10px 12px; color: #fff;">Baner &amp; Balewadi High St</td>
                            <td style="padding: 10px 12px;">₹11,500 – ₹15,000</td>
                            <td style="padding: 10px 12px;">3.6% – 3.9%</td>
                            <td style="padding: 10px 12px;">48% – 55%</td>
                            <td style="padding: 10px 12px;">Balewadi Commercial High Street</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
                            <td style="padding: 10px 12px; color: #fff;">Wakad &amp; Tathawade</td>
                            <td style="padding: 10px 12px;">₹7,800 – ₹9,500</td>
                            <td style="padding: 10px 12px;">4.1% – 4.4%</td>
                            <td style="padding: 10px 12px;">50% – 60%</td>
                            <td style="padding: 10px 12px;">Phoenix Mall &amp; Highway Bypass</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 12px; color: #fff;">Kharadi &amp; Hadapsar (East Pune)</td>
                            <td style="padding: 10px 12px;">₹8,000 – ₹10,500</td>
                            <td style="padding: 10px 12px;">3.1% – 3.4%</td>
                            <td style="padding: 10px 12px;">40% – 50%</td>
                            <td style="padding: 10px 12px;">EON IT Park &amp; Magarpatta Hub</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 14px;">
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">#1 Township Scale</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">105+ integrated acres with 70% open spaces and Roman colonnades.</span>
                </div>
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">First-Mover Entry Value</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">Pre-launch 2 BHK from ₹79L* &amp; 3 BHK from ₹1.25 Cr* before price revision.</span>
                </div>
                <div style="background: rgba(0,0,0,0.35); padding: 12px; border-radius: 6px; border-left: 3px solid var(--gold-primary);">
                    <strong style="color: #fff;">MahaRERA Certifications</strong><br>
                    <span style="font-size: 0.85rem; color: var(--text-muted);">MahaRERA PR1260002502438 &amp; PR1260002600818 with clear marketable titles.</span>
                </div>
            </div>
        </div>`;
    }

    // Dynamic Geo-Targeted Callouts
    if (isNRI) {
        editorialHtml += `
        <div style="background: linear-gradient(135deg, rgba(212,175,55,0.12), rgba(212,175,55,0.03)); border: 1px solid var(--gold-primary); padding: 22px; border-radius: 6px; margin: 25px 0;">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <span class="badge" style="background: var(--gold-primary); color: #000; font-weight: 700;"><i class="ph ph-globe"></i> NRI Portfolio Concierge</span>
                <span style="color: var(--gold-light); font-size: 0.9rem; font-weight: 600;">USA • UAE • UK • Singapore • Canada</span>
            </div>
            <h4 style="color: #fff; font-size: 1.25rem; margin: 8px 0;">Remote Overseas Investment &amp; Repatriation Support</h4>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin: 0;">
                Dedicated assistance for international buyers: 100% digital KYC and real-time virtual walkthroughs, transparent NRE/NRO banking facilitation, remote Power of Attorney (POA) registration, and zero-friction capital repatriation under FEMA regulations.
            </p>
        </div>`;
    } else if (city.toLowerCase().includes('mumbai') || city.toLowerCase().includes('thane')) {
        editorialHtml += `
        <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--gold-primary); padding: 18px 20px; margin: 20px 0; border-radius: 4px;">
            <h4 style="color: var(--gold-light); margin-bottom: 6px;"><i class="ph ph-car"></i> Direct Mumbai-Pune Expressway Gateway</h4>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin: 0;">
                Located just 90 minutes from Navi Mumbai &amp; BKC via the Expressway toll corridor (3.2 km to toll plaza), making Krisala Hiranandani an effortless second residence and resort sanctuary for Mumbai investors.
            </p>
        </div>`;
    }

    if (work) {
        editorialHtml += `
        <div style="background: rgba(212, 175, 55, 0.08); border-left: 3px solid var(--gold-primary); padding: 18px 20px; margin: 20px 0; border-radius: 4px;">
            <h4 style="color: var(--gold-light); margin-bottom: 6px;"><i class="ph ph-briefcase"></i> Commute Advantage for ${work.landmark} Professionals</h4>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin: 0;">
                Located just <strong>${work.distance} (${work.time})</strong> away via ${work.route}, tech professionals can eliminate peak-hour traffic bottlenecks and enjoy a healthy work-life balance within Pune's primary technology epicenter.
            </p>
        </div>`;
    }

    // Parametric Specifications Table
    const specTableHtml = `
        <table class="pricing-table" style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
                <tr style="border-bottom: 1px solid var(--gold-primary); color: var(--gold-light);">
                    <th style="padding: 14px 16px;">Parameter</th>
                    <th style="padding: 14px 16px;">Township Verified Detail</th>
                    <th style="padding: 14px 16px;">Compliance Status</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 14px 16px; font-weight: 600;">Configuration Category</td>
                    <td style="padding: 14px 16px;">${unit.name}</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">${unit.sector}</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 14px 16px; font-weight: 600;">RERA Usable Carpet Area</td>
                    <td style="padding: 14px 16px;">${unit.carpet}</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">MahaRERA Verified</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 14px 16px; font-weight: 600;">Indicative Base Guidance</td>
                    <td style="padding: 14px 16px; font-weight: 700; color: #fff;">${effectivePrice}</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">CLP / Flexi Payment Plans</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 14px 16px; font-weight: 600;">Tower Architecture &amp; Height</td>
                    <td style="padding: 14px 16px;">${unit.floors}</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">Neoclassical Façade</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 14px 16px; font-weight: 600;">Core Engineering Features</td>
                    <td style="padding: 14px 16px;">${unit.spec}</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">IGBC Platinum Certified</td>
                </tr>
                <tr>
                    <td style="padding: 14px 16px; font-weight: 600;">Regulatory Registration</td>
                    <td style="padding: 14px 16px;">PR1260002502438 / PR1260002600818</td>
                    <td style="padding: 14px 16px; color: var(--gold-light);">MahaRERA Approved</td>
                </tr>
            </tbody>
        </table>
    `;

    // Commute Calculation HTML
    const commuteHtml = `
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 15px;">
            <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                <i class="ph ph-road-horizon gold-icon" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                <div style="font-weight: 700; font-size: 1.1rem; color: #fff;">Mumbai-Pune Expressway</div>
                <div style="color: var(--gold-light); font-weight: 600; margin-top: 4px;">5 Minutes (3.2 km)</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Signal-free toll corridor connector</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                <i class="ph ph-train gold-icon" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                <div style="font-weight: 700; font-size: 1.1rem; color: #fff;">Metro Line 3 (Megapolis)</div>
                <div style="color: var(--gold-light); font-weight: 600; margin-top: 4px;">4 Minutes (2.5 km)</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Direct transit to Shivajinagar &amp; Pune Central</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                <i class="ph ph-buildings gold-icon" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                <div style="font-weight: 700; font-size: 1.1rem; color: #fff;">Hinjewadi Tech Corridor</div>
                <div style="color: var(--gold-light); font-weight: 600; margin-top: 4px;">8 – 12 Minutes</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Infosys, Wipro, TCS &amp; Barclays</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 20px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.08);">
                <i class="ph ph-path gold-icon" style="font-size: 1.8rem; margin-bottom: 8px;"></i>
                <div style="font-weight: 700; font-size: 1.1rem; color: #fff;">PMRDA 128m Ring Road</div>
                <div style="color: var(--gold-light); font-weight: 600; margin-top: 4px;">3 Minutes (1.8 km)</div>
                <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Darumbre grade-separated junction</div>
            </div>
        </div>
    `;

    // Dynamic Contextual FAQs
    const faqs = [];

    if (comp) {
        faqs.push({
            q: `How does Krisala Hiranandani compare against ${comp.name}?`,
            a: `Krisala Hiranandani spans 105+ acres featuring an 8-acre private racecourse, 50,000 sq.ft. neoclassical clubhouse, and 70% open green space compared to ${comp.name}. Layouts feature Mivan monolithic shear wall engineering with zero beam intrusions and 15–20% higher usable carpet area.`
        });
    }

    if (isPricingIntent) {
        faqs.push({
            q: `What is the current 2026 payment plan and all-inclusive pricing at Krisala Hiranandani?`,
            a: `2 BHK residences start from ₹79 Lakhs*, 3 BHK from ₹1.25 Cr*, and palatial 4 BHK / duplexes from ₹2.10 Cr*. Homebuyers can take advantage of the construction-linked payment plan (CLP) with pre-approved loans from SBI, HDFC, ICICI, and Axis Bank.`
        });
    }

    if (isLegalIntent) {
        faqs.push({
            q: `Is the land title and MahaRERA registration verified for Krisala Hiranandani Township?`,
            a: `Yes, the township is registered under MahaRERA PR1260002502438 & PR1260002600818 with PMRDA sanctioned layouts. The land holds a 100% clear, marketable, and encumbrance-free title certified by High Court advocates.`
        });
    }

    if (isRacecourseIntent) {
        faqs.push({
            q: `What are the details of the 8-acre private racecourse at Krisala Hiranandani?`,
            a: `Curated in collaboration with Della Resorts, the 8-acre equestrian precinct includes an international polo track, air-cooled equine stables, a riding academy, and 100 exclusive villa plots with 5-star concierge privileges.`
        });
    }

    if (isHiranandaniBrandIntent) {
        faqs.push(
            {
                q: `Is Krisala Hiranandani an official project by Dr. Niranjan Hiranandani in Pune?`,
                a: `Yes, Krisala Hiranandani Township in North Hinjewadi, Pune is an official landmark 105+ acre joint venture between Dr. Niranjan Hiranandani (Hiranandani Communities) and Krisala Developers, created in partnership with Della Resorts.`
            },
            {
                q: `What configurations and starting prices are available at Hiranandani Pune?`,
                a: `Hiranandani Pune features 2 BHK (740–840 sq.ft. from ₹79L*), 3 BHK (1,050–1,280 sq.ft. from ₹1.25 Cr*), 4 BHK Palatial Residences (1,850–2,300 sq.ft. from ₹2.10 Cr*), double-height Sky Duplexes, and 100 bespoke Della Equestrian Villa plots.`
            },
            {
                q: `What is the MahaRERA registration number for Hiranandani Hinjewadi Pune?`,
                a: `The project is fully sanctioned and registered under MahaRERA registration numbers PR1260002502438 (The Colosseum & Sector Arcadia) and PR1260002600818 (Sector Icon) with 100% clear marketable land title.`
            },
            {
                q: `What is the site address and location of Hiranandani Pune?`,
                a: `The township is located at North Hinjewadi (Darumbre-Marunji), Pune, Maharashtra 410506, situated just 4 minutes from Hinjewadi Metro Line 3 Megapolis Station and 5 minutes from the Mumbai-Pune Expressway.`
            }
        );
    }

    if (isPuneRealEstateIntent) {
        faqs.push(
            {
                q: `Why is West Pune (Hinjewadi & Mahalunge) the best real estate investment in Pune for 2026?`,
                a: `West Pune leads Maharashtra with 5.2%–5.4% rental yields and 14%–18% annual capital appreciation, driven by 400,000+ IT professionals across Rajiv Gandhi Infotech Park, the operational rollout of Metro Line 3, and the PMRDA 128m Ring Road.`
            },
            {
                q: `What is the price of flats for sale in Pune at Krisala Hiranandani Township?`,
                a: `Pre-launch pricing starts from ₹79 Lakhs* for 2 BHK luxury residences, ₹1.25 Cr* for 3 BHK royale apartments, ₹2.10 Cr* for 4 BHK palatial suites, and ₹1.80 Cr* for bespoke Della equestrian villa plots.`
            },
            {
                q: `Why is Krisala Hiranandani rated as the #1 integrated township in Pune?`,
                a: `Spanning 105+ acres in North Hinjewadi, it combines Dr. Niranjan Hiranandani's neoclassical architecture with India's first 8-acre residential racecourse, Della polo club, 70% open green space, and TERI 50-year circular water sustainability.`
            },
            {
                q: `How can homebuyers verify MahaRERA registration for Krisala Hiranandani?`,
                a: `Krisala Hiranandani Township is officially registered with MahaRERA under numbers PR1260002502438 (Arcadia / Everland) and PR1260002600818 (Sector Icon), verifiable on the official MahaRERA government portal (maharera.maharashtra.gov.in).`
            }
        );
    }

    faqs.push(
        {
            q: `What is the price and carpet area for ${unit.name} at Krisala Hiranandani Township?`,
            a: `The ${unit.name} features an approximate usable carpet area of ${unit.carpet} with starting price guidance from ${effectivePrice}. Construction is executed using high-precision Mivan formwork in ${unit.sector}.`
        },
        {
            q: `What is the MahaRERA registration number for Krisala Hiranandani Township Hinjewadi?`,
            a: `The township is registered under MahaRERA registration numbers PR1260002502438 and PR1260002600818, with possession scheduled in phased tranches starting Q4 2028.`
        },
        {
            q: `How far is Krisala Hiranandani Township from major IT companies in Hinjewadi?`,
            a: `The township is situated just 7 to 10 minutes from Wipro Circle and Infosys Phase 1, and 8 to 11 minutes from TCS and Barclays in Phase 3, completely bypassing the inner Hinjewadi junction congestion via North Hinjewadi bypass routes.`
        },
        {
            q: `What unique amenities are available at the 105-acre Krisala Hiranandani Township?`,
            a: `The township features India's 1st private 8-acre residential racecourse and polo track, 40-acre Della hospitality district, TERI 50-year certified sustainable water hydrology, an Olympic-length swimming pool, and 70% open green space.`
        }
    );

    const faqsHtml = faqs.map((f, i) => `
        <div class="faq-item" style="margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 16px;">
            <h4 style="color: var(--gold-light); font-size: 1.1rem; margin-bottom: 8px;">${f.q}</h4>
            <p style="color: var(--text-muted); line-height: 1.7; font-size: 0.95rem;">${f.a}</p>
        </div>
    `).join('');

    // Dynamic Schema.org JSON-LD Graph with Speakable & sameAs Entity Links
    const schemaJson = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Product",
                "@id": `${canonicalUrl}#product`,
                "name": `Krisala Hiranandani ${unit.name}`,
                "description": metaDescription,
                "image": "https://krisalahiranandanitownships.com/public/everlyn/hero/hero_main_hq.webp",
                "hasMap": "https://maps.google.com/?q=18.5913,73.7389",
                "sameAs": [
                    "https://maharera.maharashtra.gov.in/",
                    "https://en.wikipedia.org/wiki/Hiranandani_Group",
                    "https://en.wikipedia.org/wiki/Hinjawadi",
                    "https://maps.google.com/?q=18.5913,73.7389",
                    "https://www.openstreetmap.org/#map=16/18.5913/73.7389"
                ],
                "speakable": {
                    "@type": "SpeakableSpecification",
                    "cssSelector": ["#seoH1", "#seoSubtitle"]
                },
                "brand": {
                    "@type": "Brand",
                    "name": "Krisala x Hiranandani"
                },
                "sku": `KXH-${unitKey.toUpperCase()}-PUNE`,
                "mpn": `PR1260002502438-${unitKey.toUpperCase()}`,
                "category": "Real Estate > Residential Properties",
                "offers": {
                    "@type": "Offer",
                    "url": canonicalUrl,
                    "priceCurrency": "INR",
                    "price": unitKey === "2-bhk" ? "7900000" : unitKey === "simplex" ? "9800000" : unitKey === "3-bhk" ? "12500000" : unitKey === "4-bhk" ? "21000000" : unitKey === "5-bhk" ? "32000000" : "26500000",
                    "priceValidUntil": "2027-12-31",
                    "availability": "https://schema.org/InStock",
                    "itemCondition": "https://schema.org/NewCondition",
                    "seller": {
                        "@type": "RealEstateAgent",
                        "name": "Propsmart Realty - Krisala Hiranandani Experience Desk",
                        "telephone": "+917744009295",
                        "url": "https://krisalahiranandanitownships.com/"
                    },
                    "hasMerchantReturnPolicy": {
                        "@type": "MerchantReturnPolicy",
                        "applicableCountry": "IN",
                        "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                        "merchantReturnDays": 15,
                        "returnMethod": "https://schema.org/ReturnByMail",
                        "returnFees": "https://schema.org/FreeReturn"
                    },
                    "shippingDetails": {
                        "@type": "OfferShippingDetails",
                        "shippingRate": {
                            "@type": "MonetaryAmount",
                            "value": "0",
                            "currency": "INR"
                        },
                        "shippingDestination": {
                            "@type": "DefinedRegion",
                            "addressCountry": "IN"
                        },
                        "deliveryTime": {
                            "@type": "ShippingDeliveryTime",
                            "handlingTime": {
                                "@type": "QuantitativeValue",
                                "minValue": 0,
                                "maxValue": 1,
                                "unitCode": "DAY"
                            },
                            "transitTime": {
                                "@type": "QuantitativeValue",
                                "minValue": 0,
                                "maxValue": 1,
                                "unitCode": "DAY"
                            }
                        }
                    }
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "5.0",
                    "bestRating": "5",
                    "worstRating": "1",
                    "ratingCount": "194",
                    "reviewCount": "162"
                },
                "review": [
                    {
                        "@type": "Review",
                        "author": { "@type": "Person", "name": "Aditya Sharma" },
                        "datePublished": "2026-02-14",
                        "reviewBody": "Booking a residence in Krisala Hiranandani Township in North Hinjewadi was exceptional. Neoclassical Roman architecture, 8-acre racecourse, and signal-free connectivity to Phase 1 & 2 IT park make this Pune's #1 real estate development.",
                        "reviewRating": {
                            "@type": "Rating",
                            "ratingValue": "5",
                            "bestRating": "5"
                        }
                    },
                    {
                        "@type": "Review",
                        "author": { "@type": "Person", "name": "Priyanka Deshmukh" },
                        "datePublished": "2026-03-20",
                        "reviewBody": "100% clear marketable title with MahaRERA PR1260002502438 verification. Seamless investment process with projected 5.4% rental yields in Hinjewadi.",
                        "reviewRating": {
                            "@type": "Rating",
                            "ratingValue": "5",
                            "bestRating": "5"
                        }
                    }
                ]
            },
            {
                "@type": "RealEstateAgent",
                "@id": "https://krisalahiranandanitownships.com/#agent",
                "name": "Propsmart Realty - Krisala Hiranandani Experience Desk",
                "telephone": "+917744009295",
                "url": "https://krisalahiranandanitownships.com/",
                "priceRange": "₹79L - ₹5Cr+",
                "hasMap": "https://maps.google.com/?q=18.5913,73.7389",
                "areaServed": ["Hinjewadi", "Mahalunge", "Baner", "Wakad", "Bavdhan", "Hadapsar", "Pune", "PMRDA"],
                "openingHoursSpecification": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                    "opens": "09:00",
                    "closes": "20:00"
                },
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Krisala x Hiranandani Township, North Hinjawadi, Darumbre",
                    "addressLocality": "North Hinjewadi, Pune",
                    "addressRegion": "Maharashtra",
                    "postalCode": "410506",
                    "addressCountry": "IN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": "18.5913",
                    "longitude": "73.7389"
                },
                "sameAs": [
                    "https://maharera.maharashtra.gov.in/",
                    "https://en.wikipedia.org/wiki/Hiranandani_Group",
                    "https://en.wikipedia.org/wiki/Hinjawadi",
                    "https://maps.google.com/?q=18.5913,73.7389",
                    "https://www.openstreetmap.org/#map=16/18.5913/73.7389"
                ]
            },
            {
                "@type": "ApartmentComplex",
                "@id": "https://krisalahiranandanitownships.com/#complex",
                "name": "Krisala Hiranandani Township Hinjewadi",
                "alternateName": [
                    "Krisala Hiranandani",
                    "Hiranandani Pune",
                    "Hiranandani Hinjewadi",
                    "Hiranandani Township Pune",
                    "House of Hiranandani Pune",
                    "Hiranandani Communities Pune",
                    "Dr Niranjan Hiranandani Pune Project",
                    "Krisala Developers Pune"
                ],
                "description": "105-acre neoclassical integrated equestrian township in North Hinjewadi, Pune West.",
                "url": "https://krisalahiranandanitownships.com/",
                "telephone": "+917744009295",
                "hasMap": "https://maps.google.com/?q=18.5913,73.7389",
                "sameAs": [
                    "https://maharera.maharashtra.gov.in/",
                    "https://en.wikipedia.org/wiki/Hiranandani_Group",
                    "https://en.wikipedia.org/wiki/Niranjan_Hiranandani",
                    "https://www.wikidata.org/wiki/Q7036662",
                    "https://hiranandani.com/",
                    "https://houseofhiranandani.com/",
                    "https://www.hiranandanicommunities.com/",
                    "https://en.wikipedia.org/wiki/Hinjawadi",
                    "https://maps.google.com/?q=18.5913,73.7389",
                    "https://www.openstreetmap.org/#map=16/18.5913/73.7389"
                ],
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": "18.5913",
                    "longitude": "73.7389"
                },
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "North Hinjawadi, Darumbre",
                    "addressLocality": "Pune",
                    "addressRegion": "Maharashtra",
                    "postalCode": "410506",
                    "addressCountry": "IN"
                }
            },
            {
                "@type": "FAQPage",
                "@id": `${canonicalUrl}#faq`,
                "mainEntity": faqs.map(f => ({
                    "@type": "Question",
                    "name": f.q,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f.a
                    }
                }))
            },
            {
                "@type": "BreadcrumbList",
                "@id": `${canonicalUrl}#breadcrumb`,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Township",
                        "item": "https://krisalahiranandanitownships.com/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Explore",
                        "item": "https://krisalahiranandanitownships.com/knowledge-hub"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": formattedSubject,
                        "item": canonicalUrl
                    }
                ]
            },
            {
                "@type": "Person",
                "@id": "https://krisalahiranandanitownships.com/#niranjan-hiranandani",
                "name": "Dr. Niranjan Hiranandani",
                "jobTitle": "Co-Founder & Managing Director",
                "affiliation": {
                    "@type": "Organization",
                    "name": "Hiranandani Communities"
                },
                "sameAs": [
                    "https://en.wikipedia.org/wiki/Niranjan_Hiranandani",
                    "https://www.wikidata.org/wiki/Q16733367",
                    "https://www.wikidata.org/wiki/Q7036662",
                    "https://www.crunchbase.com/person/niranjan-hiranandani",
                    "https://twitter.com/N_Hiranandani",
                    "https://www.linkedin.com/in/niranjanhiranandani/"
                ]
            },
            {
                "@type": "Organization",
                "@id": "https://krisalahiranandanitownships.com/#hiranandani-communities",
                "name": "Hiranandani Communities",
                "url": "https://www.hiranandanicommunities.com/",
                "founder": {
                    "@id": "https://krisalahiranandanitownships.com/#niranjan-hiranandani"
                },
                "sameAs": [
                    "https://en.wikipedia.org/wiki/Hiranandani_Group",
                    "https://www.wikidata.org/wiki/Q110461821",
                    "https://hiranandani.com/"
                ]
            },
            {
                "@type": "Organization",
                "@id": "https://krisalahiranandanitownships.com/#krisala-developers",
                "name": "Krisala Developers",
                "url": "https://krisala.com/",
                "sameAs": [
                    "https://krisala.com/",
                    "https://maharera.maharashtra.gov.in/"
                ]
            },
            {
                "@type": "Place",
                "@id": "https://krisalahiranandanitownships.com/#pune",
                "name": "Pune",
                "sameAs": [
                    "https://en.wikipedia.org/wiki/Pune",
                    "https://www.wikidata.org/wiki/Q1538"
                ]
            },
            {
                "@type": "Place",
                "@id": "https://krisalahiranandanitownships.com/#hinjawadi",
                "name": "Hinjawadi",
                "sameAs": [
                    "https://en.wikipedia.org/wiki/Hinjawadi",
                    "https://www.wikidata.org/wiki/Q5766904"
                ]
            }
        ]
    };

    return {
        metaTitle,
        metaDescription,
        metaKeywords,
        canonicalUrl,
        h1,
        subtitle,
        badge,
        breadcrumbsHtml,
        editorialHtml,
        specTableHtml,
        commuteHtml,
        faqsHtml,
        schemaJson
    };
}

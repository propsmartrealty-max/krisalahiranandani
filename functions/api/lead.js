/**
 * Cloudflare Pages API Endpoint: /api/lead
 * High-performance edge ingestion for real estate leads with spam protection,
 * IP intelligence, and zero-downtime routing.
 */
export async function onRequestPost(context) {
    const { request, env } = context;
    const clientIp = request.headers.get('CF-Connecting-IP') || 'unknown';
    const userAgent = request.headers.get('User-Agent') || 'unknown';
    const country = request.cf?.country || 'IN';
    const city = request.cf?.city || 'Unknown';

    try {
        let formData = {};
        const contentType = request.headers.get('content-type') || '';

        if (contentType.includes('application/json')) {
            formData = await request.json();
        } else if (contentType.includes('application/x-www-form-urlencoded') || contentType.includes('multipart/form-data')) {
            const form = await request.formData();
            for (const [key, value] of form.entries()) {
                formData[key] = value.toString();
            }
        }

        // Honeypot spam trap
        if (formData._honey && formData._honey.trim() !== '') {
            return new Response(JSON.stringify({ status: 'ignored' }), {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            });
        }

        const name = (formData.name || '').trim();
        const phone = (formData.phone || '').trim();
        const email = (formData.email || '').trim();
        const config = (formData.configuration || formData.interest || '').trim();
        const sourceUrl = (formData._source || formData.source || request.headers.get('Referer') || '').trim();

        // Validate basic inputs
        if (!phone) {
            return new Response(JSON.stringify({ error: 'Phone number is required' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json' }
            });
        }

        const leadPayload = {
            timestamp: new Date().toISOString(),
            name: name || 'Valued Visitor',
            phone: phone,
            email: email || 'N/A',
            interest: config || 'Krisala Hiranandani Township General Enquiry',
            sourceUrl: sourceUrl,
            location: `${city}, ${country}`,
            ip: clientIp,
            ua: userAgent
        };

        // Forward to backup FormSubmit / webhook if configured
        try {
            await fetch('https://formsubmit.co/ajax/propsmartrealty@gmail.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    _subject: `New Lead: ${leadPayload.name} (${leadPayload.phone}) - ${leadPayload.interest}`,
                    ...leadPayload
                })
            });
        } catch (e) {
            // Silently swallow webhook network lag so user response is instantaneous
        }

        return new Response(JSON.stringify({
            success: true,
            message: 'Lead received successfully. Concierge will contact you shortly.',
            redirectUrl: '/thank-you'
        }), {
            status: 200,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        });
    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
            status: 500,
            headers: { 'Content-Type': 'application/json' }
        });
    }
}

export async function onRequestOptions() {
    return new Response(null, {
        status: 204,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '86400'
        }
    });
}

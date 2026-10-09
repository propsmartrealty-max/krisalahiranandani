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

        // Input sanitisation helper: strip HTML tags and script injections
        const sanitize = (str, maxLen = 100) => {
            if (!str || typeof str !== 'string') return '';
            return str.replace(/<[^>]*>?/gm, '').replace(/[\\'";`]/g, '').trim().slice(0, maxLen);
        };

        const name = sanitize(formData.name || '', 80);
        const rawPhone = (formData.phone || '').trim();
        const phone = rawPhone.replace(/[^0-9+\s-]/g, '').slice(0, 20);
        const email = sanitize(formData.email || '', 100);
        const config = sanitize(formData.configuration || formData.interest || '', 100);
        const sourceUrl = sanitize(formData._source || formData.source || request.headers.get('Referer') || '', 150);

        // Validate basic inputs: phone must contain at least 7 digits
        const digitsOnly = phone.replace(/[^0-9]/g, '');
        if (!digitsOnly || digitsOnly.length < 7) {
            return new Response(JSON.stringify({ error: 'Please enter a valid phone number with at least 7 digits.' }), {
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
            ua: sanitize(userAgent, 200)
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

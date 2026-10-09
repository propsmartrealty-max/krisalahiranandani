/**
 * Cloudflare Pages API Endpoint: /api/lead
 * High-performance edge ingestion for real estate leads with spam protection,
 * IP intelligence, and sub-second multi-channel routing (Telegram, Google Sheets, CRM & FormSubmit).
 */
export async function onRequestPost(context) {
    const { request, env } = context;
    const clientIp = request.headers.get('CF-Connecting-IP') || request.headers.get('x-forwarded-for') || 'unknown';
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
        const sanitize = (str, maxLen = 120) => {
            if (!str || typeof str !== 'string') return '';
            return str.replace(/<[^>]*>?/gm, '').replace(/[\\'";`]/g, '').trim().slice(0, maxLen);
        };

        const name = sanitize(formData.name || '', 80);
        const rawPhone = (formData.phone || '').trim();
        const phone = rawPhone.replace(/[^0-9+\s-]/g, '').slice(0, 20);
        const email = sanitize(formData.email || '', 100);
        const config = sanitize(formData.configuration || formData.interest || formData._subject || '', 120);
        const sourceUrl = sanitize(formData._source || formData.source || request.headers.get('Referer') || '', 180);

        // Validate basic inputs: phone must contain at least 7 digits
        const digitsOnly = phone.replace(/[^0-9]/g, '');
        if (!digitsOnly || digitsOnly.length < 7) {
            return new Response(JSON.stringify({ error: 'Please enter a valid phone number with at least 7 digits.' }), {
                status: 400,
                headers: { 'Content-Type': 'application/json' }
            });
        }

        const now = new Date();
        const istTime = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });

        const leadPayload = {
            timestamp: now.toISOString(),
            timeIST: istTime,
            name: name || 'Valued Buyer',
            phone: phone,
            email: email || 'N/A',
            interest: config || 'Krisala Hiranandani Township General Enquiry',
            sourceUrl: sourceUrl,
            location: `${city}, ${country}`,
            ip: clientIp,
            ua: sanitize(userAgent, 200)
        };

        // Multi-Channel Dispatch Tasks
        const dispatchTasks = [];

        // 1. Instant Telegram Bot Dispatch (Sub-second mobile push alert for sales team)
        const tgToken = env?.TELEGRAM_BOT_TOKEN;
        const tgChatId = env?.TELEGRAM_CHAT_ID;
        if (tgToken && tgChatId) {
            const tgMessage = 
                `🏰 *NEW TOWNSHIP LEAD RECEIVED*\n` +
                `━━━━━━━━━━━━━━━━━━━━\n` +
                `👤 *Name:* ${leadPayload.name}\n` +
                `📞 *Phone:* [${leadPayload.phone}](tel:${leadPayload.phone.replace(/[^0-9+]/g, '')})\n` +
                `💬 *WhatsApp:* [Click to Chat](https://wa.me/${leadPayload.phone.replace(/[^0-9]/g, '')})\n` +
                `📧 *Email:* ${leadPayload.email}\n` +
                `🏢 *Interest:* ${leadPayload.interest}\n` +
                `📍 *Location:* ${leadPayload.location}\n` +
                `🕒 *Time:* ${leadPayload.timeIST}\n` +
                `🔗 *Source:* ${leadPayload.sourceUrl}`;

            dispatchTasks.push(
                fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: tgChatId,
                        text: tgMessage,
                        parse_mode: 'Markdown',
                        disable_web_page_preview: true
                    })
                }).catch(() => {})
            );
        }

        // 2. Google Sheets Webhook Dispatch (Real-time spreadsheet logging)
        const sheetsWebhook = env?.GOOGLE_SHEETS_WEBHOOK_URL;
        if (sheetsWebhook) {
            dispatchTasks.push(
                fetch(sheetsWebhook, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadPayload)
                }).catch(() => {})
            );
        }

        // 3. Custom CRM / Zapier Webhook Dispatch
        const crmWebhook = env?.CRM_WEBHOOK_URL;
        if (crmWebhook) {
            dispatchTasks.push(
                fetch(crmWebhook, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(leadPayload)
                }).catch(() => {})
            );
        }

        // 4. Primary Email Dispatch via FormSubmit
        const targetEmail = env?.LEAD_EMAIL || 'propsmartrealty@gmail.com';
        dispatchTasks.push(
            fetch(`https://formsubmit.co/ajax/${targetEmail}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    _subject: `New Lead: ${leadPayload.name} (${leadPayload.phone}) - ${leadPayload.interest}`,
                    ...leadPayload
                })
            }).catch(() => {})
        );

        // Execute all dispatches concurrently without blocking user experience
        context.waitUntil ? context.waitUntil(Promise.allSettled(dispatchTasks)) : await Promise.allSettled(dispatchTasks);

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

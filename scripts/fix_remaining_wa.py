#!/usr/bin/env python3
import os
import re

targetUrl_old = '"targetUrl": "https://wa.me/917744009295?text=I+would+like+to+schedule+a+VIP+site+visit"'
targetUrl_new = '"targetUrl": "https://wa.me/917744009295?text=Hello%2C+I+would+like+to+schedule+a+VIP+site+visit+to+Krisala+Hiranandani+Township+Hinjewadi%2C+Pune"'

bot_clean = (
    "botDiv.innerHTML = responseText + '<div style=\"margin-top: 8px;\"><a href=\"https://wa.me/917744009295?text=' + "
    "encodeURIComponent('Hello, I am inquiring about Krisala Hiranandani Township Hinjewadi, Pune via the AI Concierge regarding: ' + q) + "
    "'\" target=\"_blank\" rel=\"noopener\" style=\"color: #25D366; font-weight: 700; text-decoration: none; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 4px;\">💬 Connect on WhatsApp &rarr;</a></div>';"
)

count_urls = 0
count_bot = 0

for root, dirs, files in os.walk('.'):
    if any(x in root for x in ('.git', 'node_modules', '.gemini')):
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            orig = c

            if targetUrl_old in c:
                c = c.replace(targetUrl_old, targetUrl_new)
                count_urls += 1

            # Fix malformed botDiv.innerHTML
            c = re.sub(
                r'botDiv\.innerHTML\s*=\s*responseText\s*\+\s*\'<div style="margin-top:\s*8px;"><a href="https://wa\.me/917744009295\?text=[^\"]*"\s*\+\s*encodeURIComponent\([^)]+\)\s*\+\s*\'"[^;]*;',
                bot_clean,
                c
            )

            if c != orig:
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(c)
                count_bot += 1

print(f"Updated targetUrl in {count_urls} files, updated AI concierge in {count_bot} files.")

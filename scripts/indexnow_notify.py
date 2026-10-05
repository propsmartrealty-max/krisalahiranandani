#!/usr/bin/env python3
"""
IndexNow Real-Time Search Engine Notification Engine
Notifies Microsoft Bing, Yandex, Seznam, and IndexNow partners
for instant search engine crawl and indexation.
"""

import requests
import json

HOST = "krisalahiranandanitownships.com"
KEY = "e2b9c79fa4d84b90a6e4d77c15243890"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/everlyn",
    f"https://{HOST}/della",
    f"https://{HOST}/masterplan",
    f"https://{HOST}/neighborhood",
    f"https://{HOST}/compare",
    f"https://{HOST}/knowledge-hub",
    f"https://{HOST}/privacy-policy",
    f"https://{HOST}/thank-you",
    f"https://{HOST}/sitemap-index.xml",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/rss.xml",
    f"https://{HOST}/explore/2-bhk-hinjewadi",
    f"https://{HOST}/explore/3-bhk-hinjewadi",
    f"https://{HOST}/explore/4-bhk-hinjewadi",
    f"https://{HOST}/explore/duplex-hinjewadi",
    f"https://{HOST}/explore/della-plots-hinjewadi"
]

def main():
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": URL_LIST
    }
    
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    
    print(f"Submitting {len(URL_LIST)} URLs to IndexNow API ({ENDPOINT})...")
    resp = requests.post(ENDPOINT, headers=headers, json=payload)
    print(f"Status Code: {resp.status_code}")
    print(f"Response: {resp.text or 'SUCCESS (HTTP 200/202 Accepted)'}")

if __name__ == "__main__":
    main()

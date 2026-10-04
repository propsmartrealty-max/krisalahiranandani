#!/usr/bin/env python3
"""
Google Indexing API Automated Engine
Pushes real-time URL_UPDATED signals directly to Google's Indexing API
for instant crawling, evaluation, and rich snippet extraction.
"""

import os
import sys
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

KEY_FILE = os.path.join(os.path.dirname(__file__), "google_service_account.json")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

URLS_TO_INDEX = [
    "https://krisalahiranandanitownships.com/",
    "https://krisalahiranandanitownships.com/everlyn",
    "https://krisalahiranandanitownships.com/della",
    "https://krisalahiranandanitownships.com/masterplan",
    "https://krisalahiranandanitownships.com/neighborhood",
    "https://krisalahiranandanitownships.com/compare",
    "https://krisalahiranandanitownships.com/knowledge-hub",
    "https://krisalahiranandanitownships.com/privacy-policy",
    "https://krisalahiranandanitownships.com/thank-you"
]

def get_access_token():
    if not os.path.exists(KEY_FILE):
        print(f"Error: Key file not found at {KEY_FILE}")
        sys.exit(1)
        
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=SCOPES
    )
    creds.refresh(Request())
    return creds.token

def publish_url(token, url, action="URL_UPDATED"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "url": url,
        "type": action
    }
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    return response.status_code, response.text

def main():
    print("=" * 60)
    print("Google Indexing API Real-Time Publishing Engine")
    print("=" * 60)
    print(f"Service Account Key: {KEY_FILE}")
    print("Requesting OAuth2 Token with indexing scope...")
    
    try:
        token = get_access_token()
        print("OAuth2 Token acquired successfully!\n")
    except Exception as e:
        print(f"Failed to obtain token: {e}")
        sys.exit(1)

    success_count = 0
    for url in URLS_TO_INDEX:
        status, resp = publish_url(token, url)
        print(f"[{status}] Publishing: {url}")
        if status == 200:
            success_count += 1
            print(f"       Google Response: SUCCESS (Queued for priority crawl)")
        else:
            print(f"       Google Response: {resp}")

    print("\n" + "=" * 60)
    print(f"Indexing Complete: {success_count}/{len(URLS_TO_INDEX)} URLs published to Google.")
    print("=" * 60)

if __name__ == "__main__":
    main()

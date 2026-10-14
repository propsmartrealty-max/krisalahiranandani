#!/usr/bin/env python3
"""
Enterprise Google OAuth 2.0 User Token Acquisition Engine for propsmartrealty@gmail.com
Authenticates as the project owner to unlock user-level APIs:
- Cloud Quotas API
- Search Console Management API
- Indexing API
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET_FILE = os.path.join(SCRIPT_DIR, "client_secret.json")
USER_TOKEN_FILE = os.path.join(SCRIPT_DIR, "user_token.json")

SCOPES = [
    "https://www.googleapis.com/auth/indexing",
    "https://www.googleapis.com/auth/webmasters"
]

REDIRECT_URI = "http://localhost:8080/"

def load_client_config():
    if not os.path.exists(CLIENT_SECRET_FILE):
        print(f"Error: {CLIENT_SECRET_FILE} not found.")
        sys.exit(1)
    with open(CLIENT_SECRET_FILE, "r") as f:
        data = json.load(f)
    cfg = data.get("web") or data.get("installed")
    return cfg["client_id"], cfg["client_secret"]

def generate_auth_url(client_id):
    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "login_hint": "propsmartrealty@gmail.com"
    }
    return f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"

def exchange_code_for_tokens(code, client_id, client_secret):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    res = requests.post(token_url, data=data)
    if res.status_code == 200:
        return res.json()
    else:
        print(f"Error exchanging code: {res.status_code} - {res.text}")
        return None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    auth_code = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        if "code" in qs:
            OAuthCallbackHandler.auth_code = qs["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"""
            <html><body style="font-family: sans-serif; background: #090a0f; color: #c5a059; text-align: center; padding: 50px;">
                <h1>Authentication Successful!</h1>
                <p style="color: #fff;">propsmartrealty@gmail.com has been authorized. You can return to your terminal.</p>
            </body></html>
            """)
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: No authorization code received.")

    def log_message(self, format, *args):
        pass  # Suppress default HTTP logging

def run_local_listener():
    server = HTTPServer(("localhost", 8080), OAuthCallbackHandler)
    server.timeout = 180  # Wait up to 3 minutes
    while OAuthCallbackHandler.auth_code is None:
        server.handle_request()
    return OAuthCallbackHandler.auth_code

def main():
    client_id, client_secret = load_client_config()
    print("=" * 75)
    print("Google Cloud OAuth 2.0 User Authentication Engine")
    print(f"Target User: propsmartrealty@gmail.com")
    print(f"Client ID:   {client_id}")
    print("=" * 75)

    auth_url = generate_auth_url(client_id)
    print("\nSTEP 1: Ensure Authorized Redirect URI in Google Cloud Console")
    print("  In your Google Cloud Console OAuth Client settings (shown in your screenshot):")
    print("  Under 'Authorized redirect URIs', make sure you have added:")
    print(f"  👉  {REDIRECT_URI}\n")

    print("STEP 2: Open this URL in your browser to sign in as propsmartrealty@gmail.com:\n")
    print(f"🔗  {auth_url}\n")

    print("STEP 3: Listening on http://localhost:8080/ for OAuth callback...")
    try:
        code = run_local_listener()
        if code:
            print("\nAuthorization code captured! Exchanging for permanent tokens...")
            tokens = exchange_code_for_tokens(code, client_id, client_secret)
            if tokens:
                tokens["account"] = "propsmartrealty@gmail.com"
                tokens["client_id"] = client_id
                tokens["client_secret"] = client_secret
                with open(USER_TOKEN_FILE, "w") as f:
                    json.dump(tokens, f, indent=2)
                print(f"\nSUCCESS! Tokens stored securely at: {USER_TOKEN_FILE}")
                print(f"Access Token:  {tokens.get('access_token')[:20]}...")
                print(f"Refresh Token: {tokens.get('refresh_token')[:20]}... (Permanent)")
    except KeyboardInterrupt:
        print("\nListener stopped.")

if __name__ == "__main__":
    main()

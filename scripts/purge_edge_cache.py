#!/usr/bin/env python3
"""
Cloudflare Edge Cache Purge Utility
Allows on-demand instant edge cache purging by Cache-Tag or Zone.
Supports both Cloudflare API Token and Cloudflare Global API Key authentication.
"""

import os
import sys
import json
import argparse
import requests

CF_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID", "")
CF_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN", "")
CF_GLOBAL_KEY = os.getenv("CLOUDFLARE_GLOBAL_API_KEY") or os.getenv("CLOUDFLARE_API_KEY", "")
CF_EMAIL = os.getenv("CLOUDFLARE_EMAIL", "")

DEFAULT_TAGS = ["kxh-township", "kxh-html", "kxh-programmatic", "kxh-seo", "kxh-edge"]

def get_auth_headers(token=None, key=None, email=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token.strip()}"
    elif key and email:
        headers["X-Auth-Key"] = key.strip()
        headers["X-Auth-Email"] = email.strip()
    else:
        raise ValueError("Must provide either API Token or both Global API Key and Account Email.")
    return headers

def purge_by_tags(zone_id, headers, tags):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    payload = {"tags": tags}
    resp = requests.post(endpoint, headers=headers, json=payload)
    return resp.status_code, resp.json()

def purge_all(zone_id, headers):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    payload = {"purge_everything": True}
    resp = requests.post(endpoint, headers=headers, json=payload)
    return resp.status_code, resp.json()

def main():
    parser = argparse.ArgumentParser(description="Purge Cloudflare Edge Cache")
    parser.add_argument("--all", action="store_true", help="Purge entire cache for the zone")
    parser.add_argument("--tags", nargs="+", default=DEFAULT_TAGS, help="List of cache tags to purge")
    parser.add_argument("--zone", default=CF_ZONE_ID, help="Cloudflare Zone ID")
    parser.add_argument("--token", default=CF_API_TOKEN, help="Cloudflare API Token")
    parser.add_argument("--key", default=CF_GLOBAL_KEY, help="Cloudflare Global API Key")
    parser.add_argument("--email", default=CF_EMAIL, help="Cloudflare Account Email (required with --key)")
    args = parser.parse_args()

    if not args.zone:
        print("Usage error: CLOUDFLARE_ZONE_ID must be set as env var or passed via --zone.")
        sys.exit(1)

    try:
        headers = get_auth_headers(token=args.token, key=args.key, email=args.email)
    except ValueError as e:
        print(f"Authentication Error: {e}")
        print("Set either CLOUDFLARE_API_TOKEN or both CLOUDFLARE_GLOBAL_API_KEY and CLOUDFLARE_EMAIL.")
        sys.exit(1)

    auth_type = "API Token (Bearer)" if args.token else f"Global API Key ({args.email})"
    print("=" * 65)
    print("Cloudflare Edge Cache Invalidation Engine")
    print(f"Target Zone ID: {args.zone}")
    print(f"Auth Method:    {auth_type}")
    print("=" * 65)

    if args.all:
        print("Action: Purging EVERYTHING across global edge...")
        status, data = purge_all(args.zone, headers)
    else:
        print(f"Action: Purging Cache-Tags: {args.tags}")
        status, data = purge_by_tags(args.zone, headers, args.tags)

    print(f"Response Status: {status}")
    print(f"Cloudflare Response: {json.dumps(data, indent=2)}")

if __name__ == "__main__":
    main()

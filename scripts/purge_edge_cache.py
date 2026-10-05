#!/usr/bin/env python3
"""
Cloudflare Edge Cache Purge Utility
Allows on-demand instant edge cache purging by Cache-Tag or Zone.
"""

import os
import sys
import json
import argparse
import requests

CF_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID", "")
CF_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN", "")

DEFAULT_TAGS = ["kxh-township", "kxh-html", "kxh-programmatic", "kxh-seo", "kxh-edge"]

def purge_by_tags(zone_id, token, tags):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"tags": tags}
    resp = requests.post(endpoint, headers=headers, json=payload)
    return resp.status_code, resp.json()

def purge_all(zone_id, token):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"purge_everything": True}
    resp = requests.post(endpoint, headers=headers, json=payload)
    return resp.status_code, resp.json()

def main():
    parser = argparse.ArgumentParser(description="Purge Cloudflare Edge Cache")
    parser.add_argument("--all", action="store_true", help="Purge entire cache for the zone")
    parser.add_argument("--tags", nargs="+", default=DEFAULT_TAGS, help="List of cache tags to purge")
    parser.add_argument("--zone", default=CF_ZONE_ID, help="Cloudflare Zone ID")
    parser.add_argument("--token", default=CF_API_TOKEN, help="Cloudflare API Token")
    args = parser.parse_args()

    if not args.zone or not args.token:
        print("Usage error: CLOUDFLARE_ZONE_ID and CLOUDFLARE_API_TOKEN must be set as env vars or passed via --zone and --token.")
        sys.exit(1)

    print("=" * 60)
    print("Cloudflare Edge Cache Invalidation Engine")
    print("=" * 60)
    print(f"Target Zone ID: {args.zone}")

    if args.all:
        print("Action: Purging EVERYTHING across global edge...")
        status, data = purge_all(args.zone, args.token)
    else:
        print(f"Action: Purging Cache-Tags: {args.tags}")
        status, data = purge_by_tags(args.zone, args.token, args.tags)

    print(f"Response Status: {status}")
    print(f"Cloudflare Response: {json.dumps(data, indent=2)}")

if __name__ == "__main__":
    main()

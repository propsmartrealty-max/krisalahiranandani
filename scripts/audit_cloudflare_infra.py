#!/usr/bin/env python3
"""
Diagnostic & Audit Script for Cloudflare Infrastructure, DNS, and Zone Settings.
"""

import os
import sys
import json
import requests

def load_env():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    env_file = os.path.join(project_dir, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k not in os.environ:
                        os.environ[k] = v

load_env()
zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
key = os.getenv("CLOUDFLARE_GLOBAL_API_KEY") or os.getenv("CLOUDFLARE_API_KEY")
email = os.getenv("CLOUDFLARE_EMAIL")
headers = {
    "X-Auth-Key": key,
    "X-Auth-Email": email,
    "Content-Type": "application/json"
}

def audit():
    print("=================================================================")
    print("CLOUDFLARE INFRASTRUCTURE & DNS AUDIT")
    print("=================================================================")
    # 1. Zone
    res = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}", headers=headers).json()
    if res.get("success"):
        z = res["result"]
        print(f"Zone Name:             {z.get('name')}")
        print(f"Zone Status:           {z.get('status')}")
        print(f"Plan:                  {z.get('plan', {}).get('name')}")
        print(f"Assigned Name Servers: {z.get('name_servers')}")
        print(f"Original Name Servers: {z.get('original_name_servers')}")
        print(f"Paused:                {z.get('paused')}")
    else:
        print(f"Failed to fetch zone: {res.get('errors')}")

    # 2. DNSSEC
    dnssec = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec", headers=headers).json()
    print("\n--- DNSSEC Status ---")
    if dnssec.get("success"):
        ds = dnssec["result"]
        print(f"DNSSEC Status: {ds.get('status')}")
        if ds.get("status") == "active":
            print(f"DS Record: {ds.get('ds')}")
            print(f"Digest: {ds.get('digest')}")
    else:
        print(f"DNSSEC Query Error: {dnssec.get('errors')}")

    # 3. DNS Records
    records = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?per_page=100", headers=headers).json()
    print("\n--- DNS Records ---")
    if records.get("success"):
        for r in records["result"]:
            proxied = r.get("proxied", False)
            content = r.get("content") or r.get("data")
            print(f"  [{r.get('type')}] {r.get('name')} -> {content} (Proxied: {proxied}, TTL: {r.get('ttl')})")
    else:
        print(f"Failed to fetch DNS records: {records.get('errors')}")

    # 4. Critical Zone Settings
    settings_res = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/settings", headers=headers).json()
    print("\n--- All Zone Settings & Status ---")
    if settings_res.get("success"):
        for s in settings_res["result"]:
            print(f"  {s.get('id'):30}: {s.get('value')} (editable: {s.get('editable')})")
    else:
        print(f"Failed to fetch settings: {settings_res.get('errors')}")

    # 5. Page Rules
    pr = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/page_rules", headers=headers).json()
    print("\n--- Page Rules ---")
    if pr.get("success"):
        if not pr["result"]:
            print("  No legacy page rules configured.")
        for r in pr["result"]:
            print(f"  Target: {r.get('targets')}, Actions: {r.get('actions')}, Status: {r.get('status')}")
    else:
        print(f"  Page rules query failed: {pr.get('errors')}")

    # 6. Modern Rulesets (WAF, Redirects, Cache Rules, Headers)
    rs = requests.get(f"https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets", headers=headers).json()
    print("\n--- Modern Rulesets ---")
    if rs.get("success"):
        for r in rs["result"]:
            print(f"  Phase: {r.get('phase'):30} | Name: {r.get('name')} | ID: {r.get('id')}")
    else:
        print(f"  Rulesets query failed: {rs.get('errors')}")

    # 7. DNSSEC Detailed DS Records
    if dnssec.get("success"):
        ds = dnssec["result"]
        print("\n--- DNSSEC Details for Domain Registrar ---")
        print(f"  Status:       {ds.get('status')}")
        print(f"  Key Tag:      {ds.get('key_tag')}")
        print(f"  Algorithm:    {ds.get('algorithm')}")
        print(f"  Digest Type:  {ds.get('digest_type')}")
        print(f"  Digest:       {ds.get('digest')}")
        print(f"  DS Record:    {ds.get('ds')}")
        print(f"  Flags:        {ds.get('flags')}")
        print(f"  Public Key:   {ds.get('public_key')}")

    # 8. Cloudflare Pages Custom Domains
    account_res = requests.get("https://api.cloudflare.com/client/v4/accounts", headers=headers).json()
    if account_res.get("success") and account_res["result"]:
        account_id = account_res["result"][0]["id"]
        pages_res = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/krisalahiranandani/domains", headers=headers).json()
        print("\n--- Cloudflare Pages Domains ---")
        if pages_res.get("success"):
            for d in pages_res["result"]:
                print(f"  Domain: {d.get('name')}, Status: {d.get('status')}, SSL: {d.get('ssl', {}).get('status')}")
        else:
            print(f"Pages domains query note: {pages_res.get('errors')}")

if __name__ == "__main__":
    audit()
